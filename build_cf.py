"""Builds data_cf/: a copy of data/ with specific facts changed (counterfactual).

A model answering from memory of the real SRD gets these facts wrong, so correct answers
can only come from retrieved context. Every edit is scoped to one section and asserted.
"""
import os, re, shutil

SRC, DST = "data", "data_cf"

# (file, heading regex, [(old, new), ...]) -- each `old` must occur in that section; count recorded.
EDITS = [
    ("spells.md", r"#### Fireball", [("8d6 Fire damage", "9d6 Fire damage"), ("**Range:** 150 feet", "**Range:** 120 feet")]),
    ("spells.md", r"#### Counterspell", [("**Range:** 60 feet", "**Range:** 90 feet"), ("Constitution saving throw", "Wisdom saving throw")]),
    ("spells.md", r"#### Revivify", [("300+ GP", "500+ GP"), ("within the last minute", "within the last 10 minutes")]),
    ("spells.md", r"#### Shield", [("+5\nbonus to AC", "+4\nbonus to AC")]),
    ("magic-items.md", r"#### Bag of Holding", [("500 pounds", "800 pounds"), ("64 cubic feet", "96 cubic feet")]),
    ("magic-items.md", r"#### Cloak of Protection", [("+1 bonus to Armor Class", "+2 bonus to Armor Class")]),
    ("magic-items.md", r"#### Ring of Protection", [("Rare (Requires", "Uncommon (Requires")]),
    ("monsters-A-Z.md", r"### Owlbear", [("**AC** 13", "**AC** 15"), ("59 (7d10 + 21)", "66 (7d10 + 28)")]),
    ("monsters-A-Z.md", r"### Goblin Warrior", [("**AC** 15", "**AC** 17")]),
    ("animals.md", r"## Dire Wolf", [("**AC** 14", "**AC** 16")]),
    ("animals.md", r"## Wolf", [("Speed** 40 ft.", "Speed** 50 ft.")]),
    ("rules-glossary.md", r"#### Long Rest", [("at least 8 hours", "at least 10 hours")]),
    ("rules-glossary.md", r"#### Short Rest", [("a 1-hour period", "a 2-hour period")]),
    ("character-creation.md", r"_Point Cost\._", None),  # handled below (single paragraph)
    ("equipment.md", r"\*\*Topple\.\*\*", None),
    ("equipment.md", r"\*\*Push\.\*\*", None),
    ("classes.md", r"#### Level 2: Action Surge", [("level 17", "level 15")]),
    ("feats.md", r"#### Alert", [("add your Proficiency Bonus to the roll", "add twice your Proficiency Bonus to the roll")]),
    ("feats.md", r"#### Savage Attacker", [("Once per turn", "Twice per turn")]),
    ("character-origins.md", r"#### Soldier", [("Athletics and Intimidation", "Athletics and Perception")]),
    ("playing-the-game.md", r"#### Death Saving Throws", [("If the roll is 10 or higher", "If the roll is 12 or higher")]),
]
# single-line edits (paragraph/line scoped)
LINE_EDITS = [
    ("character-creation.md", "_Point Cost._", [("27 points", "30 points"), ("14 costs 7 of your 27 points", "14 costs 7 of your 30 points")]),
    ("equipment.md", "**Topple.**", [("Constitution saving throw", "Strength saving throw")]),
    ("equipment.md", "**Push.**", [("up to 10 feet", "up to 15 feet")]),
]
# Barbarian core traits table cell: "D12 per Barbarian level" appears once in the first table
CELL_EDITS = [("classes.md", "D12 per Barbarian level", "D10 per Barbarian level")]


def section_span(text, heading_re):
    m = re.search(rf"^{heading_re}.*$", text, flags=re.M)
    assert m, f"heading not found: {heading_re}"
    level = len(re.match(r"#+", m.group(0)).group(0)) if m.group(0).startswith("#") else 99
    nxt = re.search(rf"^#{{1,{level}}} ", text[m.end():], flags=re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return m.start(), end


def main():
    if os.path.exists(DST):
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)
    texts = {f: open(f"{DST}/{f}", encoding="utf-8-sig").read() for f in os.listdir(DST)}
    log = []
    for f, h, pairs in EDITS:
        if pairs is None:
            continue
        s, e = section_span(texts[f], h)
        sec = texts[f][s:e]
        for old, new in pairs:
            assert sec.count(old) >= 1, f"{f} {h}: '{old}' not found"
            sec = sec.replace(old, new)
            log.append((f, h, old, new))
        texts[f] = texts[f][:s] + sec + texts[f][e:]
    for f, marker, pairs in LINE_EDITS:
        lines = texts[f].split("\n")
        idx = [i for i, l in enumerate(lines) if marker in l]
        assert idx, f"{f}: marker {marker} not found"
        i = idx[0]
        for old, new in pairs:
            if old in lines[i]:
                lines[i] = lines[i].replace(old, new)
                log.append((f, marker, old, new))
        texts[f] = "\n".join(lines)
    for f, old, new in CELL_EDITS:
        assert texts[f].count(old) >= 1
        texts[f] = texts[f].replace(old, new, 1)
        log.append((f, "first table", old, new))
    for f, t in texts.items():
        with open(f"{DST}/{f}", "w", encoding="utf-8") as fh:
            fh.write(t)
    for l in log:
        print(f"{l[0]:22s} {l[1][:28]:28s} {l[2][:34]!r} -> {l[3][:34]!r}")
    print(len(log), "edits applied ->", DST)


if __name__ == "__main__":
    main()
