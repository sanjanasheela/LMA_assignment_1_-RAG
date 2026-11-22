import json
# (category, question, answerable_from_srd)  -- answerable: yes / partial / no ; "agg" = needs facts spread over many chunks
RAW = {
 "Character": [("What are the abilities and characteristics of a Wizard?","yes"),("What is the difference between an Elf and a Half-Elf?","partial"),
               ("Which character classes can use magic?","yes"),("What are the racial traits of a Dragonborn?","yes"),
               ("What abilities does a Tiefling character possess?","yes"),("What is the maximum level a character can reach?","yes"),
               ("How does a character's proficiency bonus work?","yes"),("What are the primary ability scores of a Barbarian?","yes")],
 "Spell": [("What does the Fireball spell do?","yes"),("What is the damage range of Magic Missile?","yes"),("Which spells require concentration?","yes"),
           ("What is the difference between Mage Hand and Minor Illusion?","yes"),("Which spells can heal a character?","yes"),
           ("What level is the Revivify spell?","yes"),("Can a Wizard learn healing spells?","yes"),
           ("What happens when a character loses concentration on a spell?","yes"),("Which spells deal lightning damage?","yes"),
           ("What are the components required to cast Counterspell?","yes")],
 "Class": [("What are the abilities of a Paladin?","yes"),("What is the difference between a Wizard and a Sorcerer?","yes"),
           ("Which class has the highest hit points?","yes"),("How does a Rogue perform Sneak Attack?","yes"),
           ("What are the special abilities of a Druid?","yes"),("Can a Fighter cast spells?","yes"),
           ("What are the subclasses available for Clerics?","yes"),("How does a Warlock regain spell slots?","yes")],
 "Monster": [("What are the abilities of a Beholder?","no"),("What is the Armor Class of an Ancient Red Dragon?","yes"),
             ("What damage types is a Troll vulnerable to?","yes"),("How can a Vampire be defeated?","partial"),
             ("What is the challenge rating of a Lich?","yes"),("Which monsters have resistance to fire damage?","yes"),
             ("What special abilities does a Mind Flayer possess?","no"),("What is the difference between a Goblin and a Hobgoblin?","yes")],
 "Equipment": [("What is the damage dealt by a Longsword?","yes"),("What is the difference between a Greatsword and a Greataxe?","yes"),
               ("Which weapons have the Finesse property?","yes"),("What is the Armor Class provided by Plate Armor?","yes"),
               ("Which magical weapons provide additional damage?","yes"),("What are the properties of a Longbow?","yes"),
               ("Which items require attunement?","yes")],
}
out, i = [], 1
for cat, qs in RAW.items():
    for q, ans in qs:
        out.append({"id": f"o{i}", "category": cat, "question": q, "answerable": ans}); i += 1
json.dump(out, open("questions_open.json", "w"), indent=1, ensure_ascii=False)
print(len(out), "open questions;", sum(q["answerable"] == "no" for q in out), "unanswerable;", sum(q["answerable"] == "partial" for q in out), "partial")
