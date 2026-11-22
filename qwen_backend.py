"""Local Qwen generator for Colab: greedy decoding, 4-bit, with dynamic batching so threaded callers share GPU passes."""
import os, queue, threading, time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

MODEL = os.environ.get("QWEN_MODEL", "Qwen/Qwen2.5-7B-Instruct")
BATCH = int(os.environ.get("QWEN_BATCH", "6"))
MAX_NEW = int(os.environ.get("QWEN_MAX_NEW", "450"))
SYSTEM = "You are a text-only assistant. You have no tools and cannot read files."
_q, _started, _lock = queue.Queue(), False, threading.Lock()


def _load():
    tok = AutoTokenizer.from_pretrained(MODEL, padding_side="left")
    kw = dict(device_map="cuda", torch_dtype=torch.float16)
    if "7B" in MODEL or "14B" in MODEL:
        kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.float16)
    return tok, AutoModelForCausalLM.from_pretrained(MODEL, **kw).eval()


def _worker():
    tok, model = _load()
    print("qwen loaded:", MODEL, flush=True)
    while True:
        batch = [_q.get()]
        t_end = time.time() + 0.4
        while len(batch) < BATCH and time.time() < t_end:
            try:
                batch.append(_q.get(timeout=0.05))
            except queue.Empty:
                pass
        texts = [tok.apply_chat_template([{"role": "system", "content": SYSTEM}, {"role": "user", "content": b["prompt"]}],
                                         tokenize=False, add_generation_prompt=True) for b in batch]
        try:
            enc = tok(texts, return_tensors="pt", padding=True).to("cuda")
            with torch.no_grad():
                out = model.generate(**enc, max_new_tokens=MAX_NEW, do_sample=False, temperature=None, top_p=None, top_k=None)
            for b, o in zip(batch, out):
                b["result"] = tok.decode(o[enc["input_ids"].shape[1]:], skip_special_tokens=True).strip()
        except Exception as e:                       # e.g. CUDA OOM on a long batch: fall back to one-by-one
            torch.cuda.empty_cache()
            for b, t in zip(batch, texts):
                try:
                    enc = tok([t], return_tensors="pt").to("cuda")
                    with torch.no_grad():
                        o = model.generate(**enc, max_new_tokens=MAX_NEW, do_sample=False, temperature=None, top_p=None, top_k=None)
                    b["result"] = tok.decode(o[0][enc["input_ids"].shape[1]:], skip_special_tokens=True).strip()
                except Exception as e2:
                    b["result"] = f"ERROR: qwen failed {type(e2).__name__}"
        for b in batch:
            b["done"].set()


def generate(prompt):
    global _started
    with _lock:
        if not _started:
            threading.Thread(target=_worker, daemon=True).start(); _started = True
    item = {"prompt": prompt, "done": threading.Event(), "result": None}
    t0 = time.perf_counter(); _q.put(item); item["done"].wait()
    return item["result"], time.perf_counter() - t0
