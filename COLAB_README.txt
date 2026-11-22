Colab run (Qwen generator). After unzipping into /content/rag:
  pip install -q sentence-transformers chromadb langchain-text-splitters networkx scikit-learn bitsandbytes accelerate
  export LLM_BACKEND=qwen QWEN_MODEL=Qwen/Qwen2.5-7B-Instruct
  python build_cf.py                                  # makes data_cf/ from data/
  python run_eval.py --model qwen --workers 6 --out results_v2_qwen.json
  python judge.py results_v2_qwen.json                # Qwen judges Qwen
  python run_open.py --model qwen --workers 6 --out results_open_qwen.json
  python evaluate_open.py results_open_qwen.json eval_open_qwen.json review/metrics_open_qwen.md
  python export_review.py   (edit the paths inside, or use the notebook cell that does it)
