"""Writes questions_v2.json and verifies every gold fact appears in data_cf/ (except 'derived' facts)."""
import json, re, glob

Q = [
 # (type, question, facts, derived_facts)
 ("multi-part", "Counterspell and Shield are both Abjuration spells cast as a Reaction. For each: what spell level is it? What is Counterspell's range and which saving throw does it force? What AC bonus does Shield give?", ["Level 3", "Level 1", "90 feet", "Wisdom saving throw", "+4 bonus to AC"], []),
 ("multi-part", "Give Fireball's damage dice, range and saving throw. Then for Revivify, give the material component and its cost, how recently the creature must have died, and how many Hit Points it revives with.", ["9d6", "120 feet", "Dexterity", "500+ GP", "within the last 10 minutes", "1 Hit Point"], []),
 ("cross-file", "What does the Alert feat let you add to your Initiative roll? And which background grants the Savage Attacker feat, what skill proficiencies does it give, and how often per turn can Savage Attacker be used?", ["twice your Proficiency Bonus", "Soldier", "Athletics and Perception", "Twice per turn"], []),
 ("cross-file", "How much weight and volume can a Bag of Holding hold, and how much does the bag itself weigh? Also, what bonus does a Cloak of Protection give and does it need attunement?", ["800 pounds", "96 cubic feet", "5 pounds", "+2 bonus to Armor Class", "Requires Attunement"], []),
 ("cross-file", "Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points, what does the Owlbear's Multiattack consist of, and what is its CR?", ["AC 17", "3d6", "AC 15", "7d10 + 28", "two Rend attacks", "CR 3"], []),
 ("multi-part", "What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and how much raw material is needed to make Plate Armor?", ["16 in Chain Mail", "1,500 GP", "750 GP"], []),
 ("multi-part", "What are the effects of the Grappled condition on Speed and on attacks, and what are the effects of the Prone condition on movement and on attack rolls against you?", ["Speed is 0", "other than the grappler", "crawl", "half your Speed", "within 5 feet"], []),
 ("multi-part", "When can you make an Opportunity Attack and what does it cost? And what are the minimum lengths of a Long Rest (including how much must be sleep) and of a Short Rest, and how long must you wait between Long Rests?", ["Reaction", "at least 10 hours", "at least 6 hours", "16 hours", "2-hour"], []),
 ("multi-part", "Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each one do when you hit?", ["Strength saving throw", "Prone", "15 feet", "Large or smaller", "Disadvantage on its next attack roll", "reduce its Speed by 10 feet"], []),
 ("cross-file", "What does the Fighter's Action Surge give you and when does it recharge, at what level can it be used twice? And how does a Barbarian enter Rage, what armor prevents it, and how are Rage uses regained on a Short Rest?", ["one additional action, except the Magic action", "Short or Long Rest", "level 15", "Bonus Action", "Heavy armor", "one expended use when you finish a Short Rest"], []),
 ("cross-file", "Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the wolf's Pack Tactics trigger? Also what is the Wolf's speed?", ["AC 12", "2d8 + 2", "AC 16", "3d10 + 6", "Pack Tactics", "Incapacitated", "50 ft"], []),
 ("needle", "What bonuses do a Ring of Protection and a Cloak of Protection each give, and are they the same rarity?", ["+1 bonus to Armor Class and saving throws", "+2 bonus to Armor Class and saving throws", "Uncommon"], []),
 ("multi-part", "What are the options for generating ability scores in character creation: give the Standard Array, the point-buy budget with the cost of a score of 14, and the random method.", ["15, 14, 13, 12, 10, 8", "30 points", "14 costs 7", "four d6s"], []),
 ("needle", "List the four types of poison and say which can be applied to a weapon as a Bonus Action.", ["Contact", "Ingested", "Inhaled", "Injury", "Bonus Action"], []),
 ("multi-part", "Describe death saving throws: what roll counts as a success, what happens on a natural 1 and a natural 20, and what DC and check is needed to stabilize a creature with the Help action?", ["12 or higher", "third failure", "two failures", "regain 1 Hit Point", "DC 10 Wisdom (Medicine)"], []),
 ("cross-file", "What are the Hit Point Die and saving throw proficiencies of the Barbarian and of the Bard?", ["D10 per Barbarian level", "D8 per Bard level", "Strength and Constitution", "Dexterity and Charisma"], []),
 ("reasoning", "A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What is its attack bonus, its damage on a hit, the extra damage if the attack roll had Advantage, and what AC must the attack beat?", ["+4", "5 (1d6 + 2)", "2 (1d4)", "16 in Chain Mail"], []),
 ("reasoning", "A wizard casts Fireball using a 5th-level spell slot. How much damage dice does it deal in total, and what saving throw do targets make?", ["Dexterity"], ["11d6"]),
 ("needle", "What are the Owlbear's Rend attack bonus, damage and damage type, and what does the Goblin Warrior's Nimble Escape let it do?", ["+7", "14 (2d8 + 5)", "Slashing", "Disengage or Hide"], []),
 ("needle", "Which classes can cast Counterspell, and which classes can cast Revivify?", ["Sorcerer, Warlock, Wizard", "Cleric, Druid, Paladin, Ranger"], []),
 ("multi-topic", "Answer all three: (1) What is the minimum length of a Long Rest? (2) How many pounds can a Bag of Holding hold? (3) What damage does Fireball deal?", ["at least 10 hours", "800 pounds", "9d6"], []),
 ("multi-topic", "Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skills does the Soldier background give? (3) What is the Owlbear's AC?", ["DC 10", "Athletics and Perception", "AC 15"], []),
 ("multi-topic", "Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add to Initiative? (3) What saving throw does Topple force? (4) What is the point-buy budget?", ["AC 16", "twice your Proficiency Bonus", "Strength saving throw", "30 points"], []),
 ("multi-topic", "Answer all four: (1) How far does Push move a creature and what size limit applies? (2) How long is a Short Rest? (3) What is the range of Fireball? (4) What AC bonus does Shield give?", ["15 feet", "Large or smaller", "2-hour", "120 feet", "+4 bonus to AC"], []),
]

def norm(t): return " ".join(re.findall(r"[a-z0-9+]+", t.lower().replace("−", "-")))

def main():
    corpus = norm(" ".join(open(f, encoding="utf-8-sig").read() for f in glob.glob("data_cf/*.md")))
    out, bad = [], 0
    for i, (typ, q, facts, derived) in enumerate(Q, 1):
        for f in facts:
            if f" {norm(f)} " not in f" {corpus} ":
                print(f"q{i}: FACT NOT IN DATA: {f!r}"); bad += 1
        out.append({"id": i, "type": typ, "question": q, "facts": facts, "derived_facts": derived})
    json.dump(out, open("questions_v2.json", "w"), indent=2, ensure_ascii=False)
    print(len(out), "questions;", bad, "unverified facts")

main()
