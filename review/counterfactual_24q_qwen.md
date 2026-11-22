# Manual review: counterfactual_24q_qwen

Grade each answer against the SRD text. Suggested scale: correct 0 = wrong/missing, 1 = partly right, 2 = fully right; complete 0/1/2 = share of the question's parts answered; faithful Y/N = every claim is supported by the retrieved context.


---

## q1 (multi-part) Counterspell and Shield are both Abjuration spells cast as a Reaction. For each: what spell level is it? What is Counterspell's range and which saving throw does it force? What AC bonus does Shield give?

**Gold facts (counterfactual data):** Level 3; Level 1; 90 feet; Wisdom saving throw; +4 bonus to AC


### v0_closed_book  (0 chunks, 1 LLM call(s))

Sure, here are the details for both Counterspell and Shield:

### Counterspell
- **Spell Level:** 3rd level
- **Range:** Touch
- **Saving Throw:** Dexterity saving throw

### Shield
- **Spell Level:** 1st level
- **AC Bonus:** +5 (for 1 hour or until discharged)

*facts found (judge): 2/5; missing: 90 feet; Wisdom saving throw; +4 bonus to AC*


### v1_baseline  (3 chunks, 1 LLM call(s))

Counterspell is a Level 3 Abjuration spell. Its range is 90 feet. Counterspell does not force a saving throw. Shield gives a +4 bonus to AC.

*facts found (judge): 3/5; missing: Level 1; Wisdom saving throw*

*retrieved sections:* Spells > Shield | Spells > Counterspell | Monsters A–Z > Reactions

<details><summary>full retrieved context</summary>

```
[Spells > Shield]
#### Shield  
_Level 1 Abjuration (Sorcerer, Wizard)_  
**Casting Time:** Reaction, which you take when you are hit by an attack roll or targeted by the _Magic Missile_ spell
**Range:** Self
**Components:** V, S
**Duration:** 1 round  
An imperceptible barrier of magical force protects you. Until the start of your next turn, you have a +4
bonus to AC, including against the triggering attack, and you take no damage from _Magic Missile_.

---

[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

Counterspell is a 3rd-level Abjuration spell. Its range is 90 feet. Counterspell does not force a saving throw. Shield gives a +4 bonus to AC.

*facts found (judge): 3/5; missing: Level 1; Wisdom saving throw*


*re-ranking* (query: `Counterspell and Shield are both Abjuration spells cast as a Reaction. For each:`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.42 | yes | Spells > Counterspell |
| 2 | 1 | 1.61 | yes | Spells > Shield |
| 3 | 4 | 1.05 | yes | Monsters A–Z > Reactions |
| 4 | 3 | 0.98 |  | Monsters A–Z > Reactions |
| 5 | 6 | -1.01 |  | Spells > Counterspell |
| 6 | 5 | -1.28 |  | Spells > Shield of Faith |
| 7 | 9 | -2.30 |  | Spells > Healing Word |
| 8 | 7 | -2.65 |  | Spells > Cure Wounds |
| 9 | 8 | -3.08 |  | Spells > Mage Armor |
| 10 | 10 | -5.12 |  | Magic Items > Arrow-Catching Shield |

*retrieved sections:* Spells > Counterspell | Spells > Shield | Monsters A–Z > Reactions

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Spells > Shield]
#### Shield  
_Level 1 Abjuration (Sorcerer, Wizard)_  
**Casting Time:** Reaction, which you take when you are hit by an attack roll or targeted by the _Magic Missile_ spell
**Range:** Self
**Components:** V, S
**Duration:** 1 round  
An imperceptible barrier of magical force protects you. Until the start of your next turn, you have a +4
bonus to AC, including against the triggering attack, and you take no damage from _Magic Missile_.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

Counterspell is a 3rd-level Abjuration spell with a range of 90 feet and forces a Wisdom saving throw. Shield gives a +4 bonus to AC.

*facts found (judge): 2/5; missing: Level 1; 90 feet; +4 bonus to AC*


*re-ranking* (query: `Counterspell and Shield are both Abjuration spells cast as a Reaction. For each:`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.42 | yes | Spells > Counterspell |
| 2 | 1 | 1.61 | yes | Spells > Shield |
| 3 | 4 | 1.05 | yes | Monsters A–Z > Reactions |
| 4 | 3 | 0.98 | yes | Monsters A–Z > Reactions |
| 5 | 6 | -1.01 | yes | Spells > Counterspell |
| 6 | 5 | -1.28 | yes | Spells > Shield of Faith |
| 7 | 9 | -2.30 | yes | Spells > Healing Word |
| 8 | 7 | -2.65 | yes | Spells > Cure Wounds |
| 9 | 8 | -3.08 |  | Spells > Mage Armor |
| 10 | 10 | -5.12 |  | Magic Items > Arrow-Catching Shield |

*retrieved sections:* Spells > Counterspell | Spells > Shield | Monsters A–Z > Reactions | Spells > Shield of Faith | Spells > Healing Word | Spells > Cure Wounds

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Spells > Shield]
#### Shield  
_Level 1 Abjuration (Sorcerer, Wizard)_  
**Casting Time:** Reaction, which you take when you are hit by an attack roll or targeted by the _Magic Missile_ spell
**Range:** Self
**Components:** V, S
**Duration:** 1 round  
An imperceptible barrier of magical force protects you. Until the start of your next turn, you have a +4
bonus to AC, including against the triggering attack, and you take no damage from _Magic Missile_.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Spells > Shield of Faith]
#### Shield of Faith  
_Level 1 Abjuration (Cleric, Paladin)_  
**Casting Time:** Bonus Action
**Range:** 60 feet
**Components:** V, S, M (a prayer scroll)
**Duration:** Concentration, up to 10 minutes  
A shimmering field surrounds a creature of your choice within range, granting it a +2 bonus to AC for the duration.

---

[Spells > Healing Word]
#### Healing Word  
_Level 1 Abjuration (Bard, Cleric, Druid)_  
**Casting Time:** Bonus Action
**Range:** 60 feet
**Components:** V
**Duration:** Instantaneous  
A creature of your choice that you can see within range regains Hit Points equal to 2d4 plus your spellcasting ability modifier.  
_Using a Higher-Level Spell Slot._ The healing increases by 2d4 for each spell slot level above 1.

---

[Spells > Cure Wounds]
#### Cure Wounds  
_Level 1 Abjuration (Bard, Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S
**Duration:** Instantaneous  
A creature you touch regains a number of Hit Points equal to 2d8 plus your spellcasting ability modifier.  
_Using a Higher-Level Spell Slot._ The healing increases by 2d8 for each spell slot level above 1.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

Counterspell is a 3rd-level Abjuration spell. Its range is 90 feet. Counterspell does not force a saving throw. Shield gives a +4 bonus to AC.

*facts found (judge): 3/5; missing: Level 1; Wisdom saving throw*


*re-ranking* (query: `Counterspell and Shield are both Abjuration spells cast as a Reaction. For each:`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.42 | yes | Spells > Counterspell |
| 2 | 1 | 1.61 | yes | Spells > Shield |
| 3 | 4 | 1.05 | yes | Monsters A–Z > Reactions |
| 4 | 3 | 0.98 |  | Monsters A–Z > Reactions |
| 5 | 6 | -1.01 |  | Spells > Counterspell |
| 6 | 5 | -1.28 |  | Spells > Shield of Faith |
| 7 | 9 | -2.30 |  | Spells > Healing Word |
| 8 | 7 | -2.65 |  | Spells > Cure Wounds |
| 9 | 8 | -3.08 |  | Spells > Mage Armor |
| 10 | 10 | -5.12 |  | Magic Items > Arrow-Catching Shield |

*retrieved sections:* Spells > Counterspell | Spells > Shield | Monsters A–Z > Reactions

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Spells > Shield]
#### Shield  
_Level 1 Abjuration (Sorcerer, Wizard)_  
**Casting Time:** Reaction, which you take when you are hit by an attack roll or targeted by the _Magic Missile_ spell
**Range:** Self
**Components:** V, S
**Duration:** 1 round  
An imperceptible barrier of magical force protects you. Until the start of your next turn, you have a +4
bonus to AC, including against the triggering attack, and you take no damage from _Magic Missile_.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

Counterspell is a Level 3 Abjuration spell with a range of 90 feet and forces a Wisdom saving throw. Shield gives a +4 bonus to AC.

*facts found (judge): 4/5; missing: Level 1*


*re-ranking* (query: `Counterspell and Shield are both Abjuration spells cast as a Reaction. For each:`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.42 | yes | Spells > Counterspell |
| 2 | 1 | 1.61 | yes | Spells > Shield |
| 3 | 8 | 1.05 | yes | Monsters A–Z > Reactions |
| 4 | 6 | 0.98 | yes | Monsters A–Z > Reactions |
| 5 | 3 | -1.01 | yes | Spells > Counterspell |
| 6 | 4 | -1.28 | yes | Spells > Shield of Faith |
| 7 | 5 | -1.46 | yes | Spells > Reaction and Bonus Action Triggers |
| 8 | 21 | -2.30 | yes | Spells > Healing Word |
| 9 | 30 | -2.33 |  | Spells > Heal |
| 10 | 11 | -2.37 |  | Spells > Protection from Evil and Good |
| 11 | 17 | -2.65 |  | Spells > Cure Wounds |
| 12 | 10 | -2.73 |  | Spells > Aid |
| 13 | 26 | -2.85 |  | Spells > Lesser Restoration |
| 14 | 28 | -3.05 |  | Classes > Level 1 Paladin Spells |
| 15 | 19 | -3.08 |  | Spells > Mage Armor |
| 16 | 16 | -3.11 |  | Spells > Private Sanctum |
| 17 | 27 | -3.26 |  | Spells > Slow |
| 18 | 13 | -3.87 |  | Classes > Level 1: Spellcasting |
| 19 | 14 | -4.00 |  | Spells > Contingency |
| 20 | 25 | -4.02 |  | Spells > Casting Time |

*retrieved sections:* Spells > Counterspell | Spells > Shield | Monsters A–Z > Reactions | Spells > Shield of Faith | Spells > Reaction and Bonus Action Triggers | Spells > Healing Word

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Spells > Shield]
#### Shield  
_Level 1 Abjuration (Sorcerer, Wizard)_  
**Casting Time:** Reaction, which you take when you are hit by an attack roll or targeted by the _Magic Missile_ spell
**Range:** Self
**Components:** V, S
**Duration:** 1 round  
An imperceptible barrier of magical force protects you. Until the start of your next turn, you have a +4
bonus to AC, including against the triggering attack, and you take no damage from _Magic Missile_.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Spells > Shield of Faith]
#### Shield of Faith  
_Level 1 Abjuration (Cleric, Paladin)_  
**Casting Time:** Bonus Action
**Range:** 60 feet
**Components:** V, S, M (a prayer scroll)
**Duration:** Concentration, up to 10 minutes  
A shimmering field surrounds a creature of your choice within range, granting it a +2 bonus to AC for the duration.

---

[Spells > Reaction and Bonus Action Triggers]
### Reaction and Bonus Action Triggers  
A spell that has a casting time of a Reaction is cast in response to a trigger that is defined in the spell's Casting Time entry. Some spells that have a casting time of a Bonus Action are also cast in response to a trigger defined in the spell.

---

[Spells > Healing Word]
#### Healing Word  
_Level 1 Abjuration (Bard, Cleric, Druid)_  
**Casting Time:** Bonus Action
**Range:** 60 feet
**Components:** V
**Duration:** Instantaneous  
A creature of your choice that you can see within range regains Hit Points equal to 2d4 plus your spellcasting ability modifier.  
_Using a Higher-Level Spell Slot._ The healing increases by 2d4 for each spell slot level above 1.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

Counterspell is a 3rd-level Abjuration spell with a range of 90 feet and forces a Wisdom saving throw. Shield gives a +4 bonus to AC.

*facts found (judge): 4/5; missing: Level 1*


*re-ranking* (query: `Counterspell and Shield are both Abjuration spells cast as a Reaction. For each:`): candidate pool of 16, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.42 | yes | Spells > Counterspell |
| 2 | 1 | 1.61 | yes | Spells > Shield |
| 3 | 8 | 1.05 | yes | Monsters A–Z > Reactions |
| 4 | 6 | 0.98 | yes | Monsters A–Z > Reactions |
| 5 | 3 | -1.01 | yes | Spells > Counterspell |
| 6 | 4 | -1.28 | yes | Spells > Shield of Faith |
| 7 | 5 | -1.46 | yes | Spells > Reaction and Bonus Action Triggers |
| 8 | 10 | -2.73 | yes | Spells > Aid |
| 9 | 12 | -4.31 |  | Spells > Spell Level |
| 10 | 9 | -4.77 |  | Monsters > Spellcasting |
| 11 | 7 | -5.12 |  | Magic Items > Arrow-Catching Shield |
| 12 | 13 | -6.01 |  | Spells > Magic Missile |
| 13 | 11 | -6.17 |  | Rules Glossary > Reaction |
| 14 | 14 | -7.41 |  | Spells > Magic Missile |
| 15 | 15 | -9.44 |  | Classes > Paladin |
| 16 | 16 | -9.91 |  | Classes > Paladin |

*retrieved sections:* Spells > Counterspell | Spells > Shield | Monsters A–Z > Reactions | Spells > Shield of Faith | Spells > Reaction and Bonus Action Triggers | Spells > Aid

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Spells > Shield]
#### Shield  
_Level 1 Abjuration (Sorcerer, Wizard)_  
**Casting Time:** Reaction, which you take when you are hit by an attack roll or targeted by the _Magic Missile_ spell
**Range:** Self
**Components:** V, S
**Duration:** 1 round  
An imperceptible barrier of magical force protects you. Until the start of your next turn, you have a +4
bonus to AC, including against the triggering attack, and you take no damage from _Magic Missile_.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Spells > Shield of Faith]
#### Shield of Faith  
_Level 1 Abjuration (Cleric, Paladin)_  
**Casting Time:** Bonus Action
**Range:** 60 feet
**Components:** V, S, M (a prayer scroll)
**Duration:** Concentration, up to 10 minutes  
A shimmering field surrounds a creature of your choice within range, granting it a +2 bonus to AC for the duration.

---

[Spells > Reaction and Bonus Action Triggers]
### Reaction and Bonus Action Triggers  
A spell that has a casting time of a Reaction is cast in response to a trigger that is defined in the spell's Casting Time entry. Some spells that have a casting time of a Bonus Action are also cast in response to a trigger defined in the spell.

---

[Spells > Aid]
#### Aid  
_Level 2 Abjuration (Bard, Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** 30 feet
**Components:** V, S, M (a strip of white cloth)
**Duration:** 8 hours  
Choose up to three creatures within range. Each target's Hit Point maximum and current Hit Points increase by 5 for the duration.  
_Using a Higher-Level Spell Slot._ Each target's Hit Points increase by 5 for each spell slot level above 2.
```
</details>


### v6_agentic  (16 chunks, 3 LLM call(s))

Counterspell is a 3rd-level Abjuration spell. Its range is 90 feet. Counterspell forces a Wisdom saving throw. Shield gives an AC bonus determined by the Shield's rarity: +1 for uncommon, +2 for rare, or +3 for very rare.

*facts found (judge): 3/5; missing: Level 1; +4 bonus to AC*

*agentic sub-queries:* Counterspell / Shield / Abjuration / spell level / range / saving throw


*re-ranking* (query: `Counterspell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.03 | yes | Spells > Counterspell |
| 2 | 1 | 4.71 | yes | Spells > Counterspell |
| 3 | 6 | 1.46 | yes | Monsters A–Z > Reactions |
| 4 | 8 | 1.36 |  | Monsters A–Z > Reactions |
| 5 | 4 | -1.50 |  | Classes > Level 3 Warlock Spells |
| 6 | 5 | -2.26 |  | Classes > Level 3 Sorcerer Spells |
| 7 | 9 | -4.03 |  | Classes > Level 7: Countercharm |
| 8 | 3 | -10.41 |  | Classes > Level 3 Wizard Spells |
| 9 | 18 | -10.56 |  | Classes > Cantrips (Level 0 Sorcerer Spells) |
| 10 | 20 | -10.69 |  | Magic Items > Spell Scroll |
| 11 | 13 | -10.72 |  | Classes > Cantrips (Level 0 Bard Spells) |
| 12 | 19 | -10.85 |  | Spells > Vicious Mockery |
| 13 | 7 | -10.86 |  | Spells > Otherworldly Steed |
| 14 | 17 | -10.86 |  | Spells > Otherworldly Steed |
| 15 | 10 | -10.89 |  | Spells > Augury |
| 16 | 11 | -10.95 |  | Spells > Slow |
| 17 | 16 | -10.98 |  | Spells > Find Steed |
| 18 | 14 | -11.04 |  | Spells > Giant Insect |
| 19 | 12 | -11.28 |  | Spells > Modify Memory |
| 20 | 15 | -11.40 |  | Spells > Combining Spell Effects |


*re-ranking* (query: `Shield`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 4.55 | yes | Magic Items > Shield, +1, +2, or +3 |
| 2 | 7 | 4.53 | yes | Magic Items > Animated Shield |
| 3 | 1 | 4.48 | yes | Magic Items > Sentinel Shield |
| 4 | 17 | 4.07 |  | Spells > Fire Shield |
| 5 | 3 | 3.80 |  | Equipment > Armor Training |
| 6 | 6 | 3.67 |  | Magic Items > Shield of the Cavalier |
| 7 | 5 | 3.38 |  | Magic Items > Spellguard Shield |
| 8 | 9 | 3.26 |  | Magic Items > Shield of Missile Attraction |
| 9 | 2 | 3.17 |  | Magic Items > Animated Shield |
| 10 | 12 | 3.16 |  | Magic Items > Shield of the Cavalier |
| 11 | 8 | 3.01 |  | Magic Items > Arrow-Catching Shield |
| 12 | 10 | 2.89 |  | Magic Items > Shield of the Cavalier |
| 13 | 19 | 2.07 |  | Spells > Shield of Faith |
| 14 | 16 | 1.92 |  | Magic Items > Shield of the Cavalier |
| 15 | 20 | 1.33 |  | Spells > Fire Shield |
| 16 | 14 | 1.29 |  | Magic Items > Shield of the Cavalier |
| 17 | 11 | 1.10 |  | Equipment > One at a Time |
| 18 | 13 | -1.67 |  | Equipment > Armor |
| 19 | 15 | -1.91 |  | Magic Items > Bracers of Defense |
| 20 | 18 | -3.21 |  | Magic Items > Brooch of Shielding |


*re-ranking* (query: `Abjuration`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 17 | 3.55 | yes | Spells > Sanctuary |
| 2 | 4 | 3.44 | yes | Spells > Imprisonment |
| 3 | 5 | 3.44 | yes | Spells > Mind Blank |
| 4 | 2 | 3.41 |  | Spells > Banishment |
| 5 | 13 | 3.33 |  | Spells > Nondetection |
| 6 | 10 | 3.05 |  | Spells > Resistance |
| 7 | 7 | 2.99 |  | Spells > Dispel Magic |
| 8 | 11 | 2.77 |  | Spells > Holy Aura |
| 9 | 8 | 2.75 |  | Spells > Forbiddance |
| 10 | 3 | 2.72 |  | Spells > Contingency |
| 11 | 19 | 2.17 |  | Spells > Arcane Lock |
| 12 | 1 | 1.55 |  | Classes > Level 1 Cleric Spells |
| 13 | 9 | 1.23 |  | Classes > Level 5 Cleric Spells |
| 14 | 6 | 0.58 |  | Classes > Level 3 Cleric Spells |
| 15 | 18 | 0.28 |  | Classes > Level 2 Cleric Spells |
| 16 | 12 | -0.32 |  | Classes > Level 4 Paladin Spells |
| 17 | 16 | -0.39 |  | Classes > Level 1 Paladin Spells |
| 18 | 14 | -1.13 |  | Classes > Level 5 Paladin Spells |
| 19 | 15 | -1.27 |  | Classes > Level 3 Paladin Spells |
| 20 | 20 | -1.39 |  | Classes > Level 5 Cleric Spells |


*re-ranking* (query: `spell level`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 9.53 | yes | Spells > Spell Level |
| 2 | 2 | 7.38 | yes | Classes > Level 18: Spell Mastery |
| 3 | 10 | 6.50 | yes | Spells > Spell Slots |
| 4 | 3 | 6.47 |  | Classes > Level 5: Memorize Spell |
| 5 | 4 | 6.34 |  | Spells > Using a Higher-Level Spell Slot |
| 6 | 16 | 6.13 |  | Classes > Level 1: Spellcasting |
| 7 | 19 | 6.07 |  | Classes > Level 1: Spellcasting |
| 8 | 11 | 5.91 |  | Spells > Bestow Curse |
| 9 | 17 | 5.84 |  | Spells > Dispel Magic |
| 10 | 9 | 5.84 |  | Classes > Level 1: Spellcasting |
| 11 | 12 | 5.73 |  | Classes > Level 1: Spellcasting |
| 12 | 15 | 5.52 |  | Classes > Level 6: Natural Recovery |
| 13 | 18 | 4.87 |  | Character Creation > Spellcasting |
| 14 | 13 | 4.76 |  | Spells > Modify Memory |
| 15 | 7 | 4.53 |  | Spells > Blindness/Deafness |
| 16 | 6 | 4.38 |  | Spells > Dissonant Whispers |
| 17 | 20 | 4.29 |  | Spells > Magic Missile |
| 18 | 8 | 4.03 |  | Spells > Fog Cloud |
| 19 | 5 | 3.77 |  | Spells > Prayer of Healing |
| 20 | 14 | 0.51 |  | Classes > Level 6 Wizard Spells |


*re-ranking* (query: `range`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 4.93 | yes | Spells > Range |
| 2 | 1 | 4.89 | yes | Equipment > Properties |
| 3 | 3 | 3.22 | yes | Playing the Game > Range |
| 4 | 12 | 1.58 |  | Playing the Game > Your Turn |
| 5 | 4 | 0.55 |  | Spells > Range |
| 6 | 19 | -1.59 |  | Spells > Spare the Dying |
| 7 | 18 | -2.06 |  | Spells > Dimension Door |
| 8 | 6 | -2.31 |  | Spells > Knock |
| 9 | 9 | -2.96 |  | Classes > Distant Spell |
| 10 | 15 | -3.12 |  | Rules Glossary > Blindsight |
| 11 | 8 | -3.43 |  | Spells > Beacon of Hope |
| 12 | 17 | -3.92 |  | Spells > Druidcraft |
| 13 | 7 | -4.00 |  | Spells > True Seeing |
| 14 | 5 | -4.18 |  | Spells > Darkvision |
| 15 | 11 | -4.28 |  | Gameplay Toolbox > Parts of a Trap |
| 16 | 13 | -5.09 |  | Magic Items > Eyes of Minute Seeing |
| 17 | 10 | -7.29 |  | Playing the Game > Reach |
| 18 | 14 | -7.86 |  | Rules Glossary > Reach |
| 19 | 16 | -8.61 |  | Monsters A–Z > Deva |
| 20 | 20 | -9.68 |  | Equipment > Net (1 GP) |


*re-ranking* (query: `saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 9.77 | yes | Rules Glossary > Saving Throw |
| 2 | 11 | 9.51 |  | Playing the Game > Saving Throws |
| 3 | 1 | 7.83 |  | Rules Glossary > Save |
| 4 | 10 | 7.60 |  | Spells > Saving Throws |
| 5 | 2 | 7.43 |  | Playing the Game > Saving Throw Proficiencies |
| 6 | 12 | 7.28 |  | Playing the Game > Ability Modifier |
| 7 | 16 | 7.13 |  | Magic Items > Thunderous Greatclub |
| 8 | 7 | 7.06 |  | Monsters > Saving Throw Effect Notation |
| 9 | 9 | 6.95 |  | Spells > Power Word Stun |
| 10 | 4 | 6.86 |  | Playing the Game > Saving Throw Proficiencies |
| 11 | 18 | 6.84 |  | Playing the Game > Difficulty Class |
| 12 | 5 | 6.81 |  | Rules Glossary > Death Saving Throw |
| 13 | 13 | 6.68 |  | Rules Glossary > Stat Block |
| 14 | 19 | 6.64 |  | Spells > Flesh to Stone |
| 15 | 17 | 6.35 |  | Playing the Game > Half Damage |
| 16 | 8 | 6.18 |  | Playing the Game > Death Saving Throws |
| 17 | 20 | 6.18 |  | Spells > Targets |
| 18 | 14 | 6.05 |  | Playing the Game > Saving Throws and Damage |
| 19 | 15 | 5.65 |  | Spells > Symbol |
| 20 | 6 | 4.92 |  | Playing the Game > Proficiency Bonus |


*re-ranking* (query: `Counterspell level`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.82 | yes | Spells > Counterspell |
| 2 | 17 | 0.07 |  | Classes > Level 3 Warlock Spells |
| 3 | 2 | -0.60 | yes | Spells > Counterspell |
| 4 | 16 | -0.70 |  | Classes > Level 3 Sorcerer Spells |
| 5 | 14 | -2.86 |  | Monsters A–Z > Reactions |
| 6 | 12 | -3.39 | yes | Monsters A–Z > Reactions |
| 7 | 4 | -6.74 | yes | Spells > Spell Level |
| 8 | 13 | -8.23 |  | Classes > Level 14: Overchannel |
| 9 | 9 | -8.67 |  | Classes > Level 1: Spellcasting |
| 10 | 3 | -8.90 |  | Classes > Level 3 Wizard Spells |
| 11 | 5 | -9.05 |  | Classes > Level 1: Spellcasting |
| 12 | 19 | -9.33 |  | Spells > Hellish Rebuke |
| 13 | 8 | -9.43 |  | Classes > Level 1: Spellcasting |
| 14 | 20 | -9.80 |  | Character Creation > Write Your Level |
| 15 | 6 | -9.82 |  | Classes > Level 1: Spellcasting |
| 16 | 7 | -9.83 |  | Classes > Level 5: Memorize Spell |
| 17 | 18 | -9.89 |  | Character Creation > Spellcasting |
| 18 | 11 | -9.89 |  | Classes > Level 1: Spellcasting |
| 19 | 10 | -10.08 |  | Classes > Level 1: Spellcasting |
| 20 | 15 | -10.47 |  | Classes > Level 1: Spellcasting |


*re-ranking* (query: `Shield AC bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 6.60 |  | Magic Items > Arrow-Catching Shield |
| 2 | 2 | 6.21 |  | Magic Items > Shield of the Cavalier |
| 3 | 1 | 5.71 | yes | Magic Items > Shield, +1, +2, or +3 |
| 4 | 9 | 2.67 |  | Rules Glossary > Armor Training |
| 5 | 4 | 2.53 | yes | Magic Items > Animated Shield |
| 6 | 12 | 0.92 |  | Rules Glossary > Cover |
| 7 | 16 | 0.67 |  | Monsters A–Z > Reactions |
| 8 | 17 | 0.35 |  | Magic Items > Shield of the Cavalier |
| 9 | 6 | -0.87 |  | Magic Items > Bracers of Defense |
| 10 | 7 | -1.12 |  | Magic Items > Defender |
| 11 | 5 | -4.06 |  | Equipment > Armor Training |
| 12 | 10 | -4.84 | yes | Magic Items > Sentinel Shield |
| 13 | 11 | -5.60 |  | Magic Items > Spellguard Shield |
| 14 | 14 | -5.98 |  | Magic Items > Shield of Missile Attraction |
| 15 | 15 | -6.36 |  | Classes > Level 1: Unarmored Defense |
| 16 | 8 | -6.52 |  | Magic Items > Animated Shield |
| 17 | 20 | -6.63 |  | Magic Items > Shield of the Cavalier |
| 18 | 19 | -8.25 |  | Equipment > One at a Time |
| 19 | 13 | -8.68 |  | Playing the Game > Armor Class |
| 20 | 18 | -8.78 |  | Classes > Level 1: Unarmored Defense |

*retrieved sections:* Spells > Counterspell | Monsters A–Z > Reactions | Magic Items > Shield, +1, +2, or +3 | Magic Items > Animated Shield | Magic Items > Sentinel Shield | Spells > Sanctuary | Spells > Imprisonment | Spells > Mind Blank | Spells > Spell Level | Classes > Level 18: Spell Mastery | Spells > Spell Slots | Spells > Range | Equipment > Properties | Playing the Game > Range | Rules Glossary > Saving Throw

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Magic Items > Shield, +1, +2, or +3]
#### Shield, +1, +2, or +3  
_Armor (Shield), Uncommon (+1), Rare (+2), or Very Rare (+3)_  
While holding this Shield, you have a bonus to Armor Class determined by the Shield's rarity, in addition to the Shield's normal bonus to AC.

---

[Magic Items > Animated Shield]
While holding this Shield, you can take a Bonus Action to cause it to animate. The Shield leaps into the air and hovers in your space to protect you as if you were wielding it, leaving your hands free. The Shield remains animate for 1 minute, until you take a Bonus Action to end this effect, or until you die or have the Incapacitated condition, at which point the Shield falls to the ground or into your hand if you have one free.

---

[Magic Items > Sentinel Shield]
#### Sentinel Shield  
_Armor (Shield), Uncommon_  
While holding this Shield, you have Advantage on Initiative rolls and Wisdom (Perception) checks. The Shield is emblazoned with a symbol of an eye.

---

[Spells > Sanctuary]
#### Sanctuary  
_Level 1 Abjuration (Cleric)_  
**Casting Time:** Bonus Action
**Range:** 30 feet
**Components:** V, S, M (a shard of glass from a mirror)
**Duration:** 1 minute

---

[Spells > Imprisonment]
#### Imprisonment  
_Level 9 Abjuration (Warlock, Wizard)_  
**Casting Time:** 1 minute
**Range:** 30 feet
**Components:** V, S, M (a statuette of the target worth 5,000+ GP)
**Duration:** Until dispelled

---

[Spells > Mind Blank]
#### Mind Blank  
_Level 8 Abjuration (Bard, Wizard)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S
**Duration:** 24 hours

---

[Spells > Spell Level]
### Spell Level  
Every spell has a level from 0 to 9, which is indicated in a spell's description. A spell's level is an indicator of how powerful it is. Cantrips—simple spells that can be cast almost by rote—are level 0. The rules for each spellcasting class say when its members gain access to spells of certain levels.

---

[Classes > Level 18: Spell Mastery]
#### Level 18: Spell Mastery  
You have achieved such mastery over certain spells that you can cast them at will. Choose a level 1 and a level 2 spell in your spellbook that have a casting time of an action. You always have those spells prepared, and you can cast them at their lowest level without expending a spell slot. To cast either spell at a higher level, you must expend a spell slot.

---

[Spells > Spell Slots]
When you cast a spell, you expend a slot of that spell's level or higher, effectively "filling" a slot with the spell. Imagine a spell slot is a groove of a certain size—small for a level 1 slot and larger for a higher-level spell. A level 1 spell fits into a slot of any size, but a level 2 spell fits only into a slot that's at least level 2. So when a level 3 Wizard casts _Magic Missile_, a level 1 spell, that Wizard spends one of four level 1 slots and has three remaining.

---

[Spells > Range]
## Range  
A spell's range indicates how far from the spellcaster the spell's effect can originate, and the spell's description specifies which part of the effect is limited by the range.  
A range usually takes one of the following forms:  
**Distance**. The range is expressed in feet.  
**Touch**. The spell's effect originates on something, as defined by the spell, that the spellcaster must touch within their reach.

---

[Equipment > Properties]
**Range.** A Range weapon has a range in parentheses after the Ammunition or Thrown property. The range lists two numbers. The first is the weapon's normal range in feet, and the second is the weapon's long range. When attacking a target beyond normal range, you have Disadvantage on the attack roll. You can't attack a target beyond the long range.

---

[Playing the Game > Range]
#### Range  
You can make ranged attacks only against targets within a specified range. If a ranged attack, such as one made with a spell, has a single range, you can't attack a target beyond this range.  
Some ranged attacks, such as those made with a Longbow, have two ranges. The smaller number is the normal range, and the larger number is the long range. Your attack roll has Disadvantage when your target is beyond normal range, and you can't attack a target beyond long range.

---

[Rules Glossary > Saving Throw]
#### Saving Throw  
A saving throw—also called a save—represents an attempt to avoid or resist a threat. You normally make a saving throw only when a rule requires you to do so, but you can decide to fail the save without rolling. The result of a save is detailed in the effect that allowed it. If a target is forced to make a save and lacks the ability score used by it, the target automatically fails. _See also_ "Playing the Game" ("D20 Tests").
```
</details>


---

## q2 (multi-part) Give Fireball's damage dice, range and saving throw. Then for Revivify, give the material component and its cost, how recently the creature must have died, and how many Hit Points it revives with.

**Gold facts (counterfactual data):** 9d6; 120 feet; Dexterity; 500+ GP; within the last 10 minutes; 1 Hit Point


### v0_closed_book  (0 chunks, 1 LLM call(s))

Fireball:
- Damage Dice: 8d6 fire damage
- Range: 150 feet
- Saving Throw: Dexterity saving throw

Revivify:
- Material Component: A vial of blood from the creature that died
- Cost: The blood vial is worth at least 50 gp
- Recently Died: The creature must have died within the last 10 minutes
- Hit Points Revived: Up to 3d8 + the caster's spellcasting ability modifier hit points

*facts found (judge): 2/6; missing: 9d6; 120 feet; 500+ GP; 1 Hit Point*


### v1_baseline  (3 chunks, 1 LLM call(s))

Fireball's damage dice are 9d6, the range is 120 feet, and creatures make a Dexterity saving throw.

The information provided does not include details about Revivify. Therefore, the part about Revivify is missing.

*facts found (judge): 3/6; missing: 500+ GP; within the last 10 minutes; 1 Hit Point*

*retrieved sections:* Magic Items > Wand of Fireballs | Spells > Fireball | Spells > Delayed Blast Fireball

<details><summary>full retrieved context</summary>

```
[Magic Items > Wand of Fireballs]
_Regaining Charges._ The wand regains 1d6 + 1 expended charges daily at dawn. If you expend the wand's last charge, roll 1d20. On a 1, the wand crumbles into ashes and is destroyed.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The information provided does not include details about the spell Revivify or its material components, cost, or the time frame for reviving a creature. Therefore, the answer to the last part of the question is missing. 

For the given spells:
- **Fireball**: Damage dice - 9d6, Range - 120 feet, Saving throw - Dexterity.
- **Delayed Blast Fireball**: Not relevant to the question asked.

*facts found (judge): 3/6; missing: 500+ GP; within the last 10 minutes; 1 Hit Point*


*re-ranking* (query: `Give Fireball's damage dice, range and saving throw. Then for Revivify, give the`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.29 | yes | Spells > Fireball |
| 2 | 3 | 1.04 | yes | Spells > Delayed Blast Fireball |
| 3 | 9 | -3.79 | yes | Magic Items > Necklace of Fireballs |
| 4 | 6 | -4.38 |  | Spells > Revivify |
| 5 | 4 | -4.68 |  | Spells > Fireball |
| 6 | 8 | -5.04 |  | Spells > Delayed Blast Fireball |
| 7 | 1 | -5.47 |  | Magic Items > Wand of Fireballs |
| 8 | 7 | -6.04 |  | Magic Items > Staff of Fire |
| 9 | 5 | -7.05 |  | Magic Items > Staff of Power |
| 10 | 10 | -8.43 |  | Rules Glossary > Short Rest |

*retrieved sections:* Spells > Fireball | Spells > Delayed Blast Fireball | Magic Items > Necklace of Fireballs

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Magic Items > Necklace of Fireballs]
#### Necklace of Fireballs  
_Wondrous Item, Rare_  
This necklace has 1d6 + 3 beads hanging from it. You can take a Magic action to detach a bead and throw it up to 60 feet away. When it reaches the end of its trajectory, the bead detonates as a level 3 _Fireball_ (save DC 15).  
You can hurl multiple beads, or even the whole necklace, at one time. When you do so, increase the damage of the _Fireball_ by 1d6 for each bead after the first (maximum 12d6).
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

Fireball's damage dice are 9d6, the range is 120 feet, and creatures make a Dexterity saving throw.

Revivify requires a material component of a diamond worth 500+ GP, the creature must have died within the last 10 minutes, and it revives the creature with 1 Hit Point.

*facts found (judge): 6/6; missing: none*


*re-ranking* (query: `Give Fireball's damage dice, range and saving throw. Then for Revivify, give the`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.29 | yes | Spells > Fireball |
| 2 | 3 | 1.04 | yes | Spells > Delayed Blast Fireball |
| 3 | 9 | -3.79 | yes | Magic Items > Necklace of Fireballs |
| 4 | 6 | -4.38 | yes | Spells > Revivify |
| 5 | 4 | -4.68 | yes | Spells > Fireball |
| 6 | 8 | -5.04 | yes | Spells > Delayed Blast Fireball |
| 7 | 1 | -5.47 | yes | Magic Items > Wand of Fireballs |
| 8 | 7 | -6.04 | yes | Magic Items > Staff of Fire |
| 9 | 5 | -7.05 |  | Magic Items > Staff of Power |
| 10 | 10 | -8.43 |  | Rules Glossary > Short Rest |

*retrieved sections:* Spells > Fireball | Spells > Delayed Blast Fireball | Magic Items > Necklace of Fireballs | Spells > Revivify | Magic Items > Wand of Fireballs | Magic Items > Staff of Fire

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Magic Items > Necklace of Fireballs]
#### Necklace of Fireballs  
_Wondrous Item, Rare_  
This necklace has 1d6 + 3 beads hanging from it. You can take a Magic action to detach a bead and throw it up to 60 feet away. When it reaches the end of its trajectory, the bead detonates as a level 3 _Fireball_ (save DC 15).  
You can hurl multiple beads, or even the whole necklace, at one time. When you do so, increase the damage of the _Fireball_ by 1d6 for each bead after the first (maximum 12d6).

---

[Spells > Revivify]
#### Revivify  
_Level 3 Necromancy (Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S, M (a diamond worth 500+ GP, which the spell consumes)
**Duration:** Instantaneous  
You touch a creature that has died within the last 10 minutes. That creature revives with 1 Hit Point. This spell can't revive a creature that has died of old age, nor does it restore any missing body parts.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Spells > Delayed Blast Fireball]
When the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The base damage increases by 1d6 for each spell slot level above 7.

---

[Magic Items > Wand of Fireballs]
_Regaining Charges._ The wand regains 1d6 + 1 expended charges daily at dawn. If you expend the wand's last charge, roll 1d20. On a 1, the wand crumbles into ashes and is destroyed.

---

[Magic Items > Staff of Fire]
<th>Charge Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>*Burning Hands*</td>
<td>1</td>
<td>*Wall of Fire*</td>
<td>4</td>
</tr>
<tr>
<td>*Fireball*</td>
<td>3</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>  
_Regaining Charges._ The staff regains 1d6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 1, the staff crumbles into cinders and is destroyed.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The information provided does not include details about the spell Revivify or its material components, cost, or the time frame for reviving a creature. Therefore, the answer to the last part of the question is missing. 

For the given spells:
- **Fireball**: Damage dice - 9d6, Range - 120 feet, Saving throw - Dexterity.
- **Delayed Blast Fireball**: Not relevant to the question asked.

*facts found (judge): 3/6; missing: 500+ GP; within the last 10 minutes; 1 Hit Point*


*re-ranking* (query: `Give Fireball's damage dice, range and saving throw. Then for Revivify, give the`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.29 | yes | Spells > Fireball |
| 2 | 3 | 1.04 | yes | Spells > Delayed Blast Fireball |
| 3 | 9 | -3.79 | yes | Magic Items > Necklace of Fireballs |
| 4 | 6 | -4.38 |  | Spells > Revivify |
| 5 | 4 | -4.68 |  | Spells > Fireball |
| 6 | 8 | -5.04 |  | Spells > Delayed Blast Fireball |
| 7 | 1 | -5.47 |  | Magic Items > Wand of Fireballs |
| 8 | 7 | -6.04 |  | Magic Items > Staff of Fire |
| 9 | 10 | -6.42 |  | Magic Items > Wand of Fireballs |
| 10 | 5 | -7.05 |  | Magic Items > Staff of Power |

*retrieved sections:* Spells > Fireball | Spells > Delayed Blast Fireball | Magic Items > Necklace of Fireballs

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Magic Items > Necklace of Fireballs]
#### Necklace of Fireballs  
_Wondrous Item, Rare_  
This necklace has 1d6 + 3 beads hanging from it. You can take a Magic action to detach a bead and throw it up to 60 feet away. When it reaches the end of its trajectory, the bead detonates as a level 3 _Fireball_ (save DC 15).  
You can hurl multiple beads, or even the whole necklace, at one time. When you do so, increase the damage of the _Fireball_ by 1d6 for each bead after the first (maximum 12d6).
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

Fireball's damage dice are 9d6, the range is 120 feet, and the saving throw is Dexterity.

For Revivify, the material component is a diamond worth 500 GP, the cost is 500 GP (as it is consumed), the creature must have died within the last 10 minutes, and it revives with 1 Hit Point.

*facts found (judge): 6/6; missing: none*


*re-ranking* (query: `Give Fireball's damage dice, range and saving throw. Then for Revivify, give the`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.29 | yes | Spells > Fireball |
| 2 | 3 | 1.04 | yes | Spells > Delayed Blast Fireball |
| 3 | 21 | -1.32 | yes | Spells > Flaming Sphere |
| 4 | 27 | -2.92 | yes | Spells > Ice Knife |
| 5 | 6 | -3.56 | yes | Rules Glossary > Death Saving Throw |
| 6 | 18 | -3.79 | yes | Magic Items > Necklace of Fireballs |
| 7 | 29 | -3.92 | yes | Classes > Level 14: Devious Strikes |
| 8 | 1 | -4.38 | yes | Spells > Revivify |
| 9 | 10 | -4.68 |  | Spells > Fireball |
| 10 | 17 | -5.04 |  | Spells > Delayed Blast Fireball |
| 11 | 7 | -5.47 |  | Magic Items > Wand of Fireballs |
| 12 | 22 | -5.55 |  | Spells > Delayed Blast Fireball |
| 13 | 24 | -5.71 |  | Magic Items > Talisman of Pure Good |
| 14 | 15 | -6.04 |  | Magic Items > Staff of Fire |
| 15 | 26 | -6.34 |  | Gameplay Toolbox > Fire-Casting Statue |
| 16 | 19 | -6.42 |  | Magic Items > Wand of Fireballs |
| 17 | 12 | -7.05 |  | Magic Items > Staff of Power |
| 18 | 30 | -7.67 |  | Magic Items > Staff of the Magi |
| 19 | 25 | -7.76 |  | Rules Glossary > Hit Points |
| 20 | 5 | -8.22 |  | Rules Glossary > Hit Point Dice |

*retrieved sections:* Spells > Fireball | Spells > Delayed Blast Fireball | Spells > Flaming Sphere | Spells > Ice Knife | Rules Glossary > Death Saving Throw | Magic Items > Necklace of Fireballs | Classes > Level 14: Devious Strikes | Spells > Revivify

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Spells > Flaming Sphere]
**Duration:** Concentration, up to 1 minute  
You create a 5-foot-diameter sphere of fire in an unoccupied space on the ground within range. It lasts for the duration. Any creature that ends its turn within 5 feet of the sphere makes a Dexterity saving throw, taking 2d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Ice Knife]
**Duration:** Instantaneous  
You create a shard of ice and fling it at one creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Piercing damage. Hit or miss, the shard then explodes. The target and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 2d6 Cold damage.  
_Using a Higher-Level Spell Slot._ The Cold damage increases by 1d6 for each spell slot level above 1.

---

[Rules Glossary > Death Saving Throw]
#### Death Saving Throw  
A player character must make a Death Saving Throw (also called a Death Save) if they start their turn with 0 Hit Points. _See also_ "Playing the Game" ("Damage and Healing").

---

[Magic Items > Necklace of Fireballs]
#### Necklace of Fireballs  
_Wondrous Item, Rare_  
This necklace has 1d6 + 3 beads hanging from it. You can take a Magic action to detach a bead and throw it up to 60 feet away. When it reaches the end of its trajectory, the bead detonates as a level 3 _Fireball_ (save DC 15).  
You can hurl multiple beads, or even the whole necklace, at one time. When you do so, increase the damage of the _Fireball_ by 1d6 for each bead after the first (maximum 12d6).

---

[Classes > Level 14: Devious Strikes]
_Knock Out (Cost: 6d6)._ The target must succeed on a Constitution saving throw, or it has the Unconscious condition for 1 minute or until it takes any damage. The Unconscious target repeats the save at the end of each of its turns, ending the effect on itself on a success.  
_Obscure (Cost: 3d6)._ The target must succeed on a Dexterity saving throw, or it has the Blinded condition until the end of its next turn.

---

[Spells > Revivify]
#### Revivify  
_Level 3 Necromancy (Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S, M (a diamond worth 500+ GP, which the spell consumes)
**Duration:** Instantaneous  
You touch a creature that has died within the last 10 minutes. That creature revives with 1 Hit Point. This spell can't revive a creature that has died of old age, nor does it restore any missing body parts.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

Fireball's damage dice are 9d6, the range is 120 feet, and the saving throw is Dexterity.

Revivify's material component is a diamond worth 500+ GP, it can only revive a creature that has died within the last 10 minutes, and it revives the creature with 1 Hit Point.

*facts found (judge): 6/6; missing: none*


*re-ranking* (query: `Give Fireball's damage dice, range and saving throw. Then for Revivify, give the`): candidate pool of 21, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.29 | yes | Spells > Fireball |
| 2 | 3 | 1.04 | yes | Spells > Delayed Blast Fireball |
| 3 | 6 | -3.56 | yes | Rules Glossary > Death Saving Throw |
| 4 | 1 | -4.38 | yes | Spells > Revivify |
| 5 | 10 | -4.68 | yes | Spells > Fireball |
| 6 | 7 | -5.47 | yes | Magic Items > Wand of Fireballs |
| 7 | 15 | -7.82 | yes | Classes > Paladin |
| 8 | 16 | -7.99 | yes | Classes > Ranger |
| 9 | 19 | -8.19 |  | Rules Glossary > Dead |
| 10 | 5 | -8.22 |  | Rules Glossary > Hit Point Dice |
| 11 | 12 | -8.43 |  | Rules Glossary > Short Rest |
| 12 | 8 | -8.76 |  | Rules Glossary > Stat Block |
| 13 | 4 | -8.87 |  | Spells > True Resurrection |
| 14 | 18 | -8.98 |  | Rules Glossary > Dead |
| 15 | 9 | -9.29 |  | Character Creation > Fill In Numbers |
| 16 | 20 | -10.42 |  | Rules Glossary > Help [Action] |
| 17 | 13 | -10.70 |  | Rules Glossary > Short Rest |
| 18 | 14 | -10.81 |  | Classes > Paladin |
| 19 | 17 | -10.91 |  | Classes > Ranger |
| 20 | 11 | -11.09 |  | Rules Glossary > Sphere [Area of Effect] |

*retrieved sections:* Spells > Fireball | Spells > Delayed Blast Fireball | Rules Glossary > Death Saving Throw | Spells > Revivify | Magic Items > Wand of Fireballs | Classes > Paladin | Classes > Ranger

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Rules Glossary > Death Saving Throw]
#### Death Saving Throw  
A player character must make a Death Saving Throw (also called a Death Save) if they start their turn with 0 Hit Points. _See also_ "Playing the Game" ("Damage and Healing").

---

[Spells > Revivify]
#### Revivify  
_Level 3 Necromancy (Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S, M (a diamond worth 500+ GP, which the spell consumes)
**Duration:** Instantaneous  
You touch a creature that has died within the last 10 minutes. That creature revives with 1 Hit Point. This spell can't revive a creature that has died of old age, nor does it restore any missing body parts.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Magic Items > Wand of Fireballs]
_Regaining Charges._ The wand regains 1d6 + 1 expended charges daily at dawn. If you expend the wand's last charge, roll 1d20. On a 1, the wand crumbles into ashes and is destroyed.

---

[Classes > Paladin]
## Paladin  
**Core Paladin Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength and Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Paladin level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Wisdom and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Athletics, Insight, Intimidation, Medicine, Persuasion, or Religion</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>
<td>Armor Training</td>

---

[Classes > Ranger]
## Ranger  
**Core Ranger Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Dexterity and Wisdom</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Ranger level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Dexterity</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 3: Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>
```
</details>


### v6_agentic  (6 chunks, 3 LLM call(s))

Fireball's damage dice are 9d6, range is 120 feet, and creatures make a Dexterity saving throw.

For Revivify, the material component is a diamond worth 500 GP, the creature must have died within the last 10 minutes, and it revives with 1 Hit Point.

*facts found (judge): 5/6; missing: 500+ GP*

*agentic sub-queries:* Fireball / Revivify


*re-ranking* (query: `Fireball`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 12 | 5.21 | yes | Spells > Fireball |
| 2 | 14 | 4.80 | yes | Spells > Fireball |
| 3 | 2 | 4.02 | yes | Magic Items > Wand of Fireballs |
| 4 | 1 | 3.97 |  | Magic Items > Necklace of Fireballs |
| 5 | 17 | 3.59 |  | Spells > Delayed Blast Fireball |
| 6 | 8 | 3.44 |  | Spells > Delayed Blast Fireball |
| 7 | 16 | 3.02 |  | Magic Items > Wand of Fireballs |
| 8 | 9 | 2.52 |  | Monsters A–Z > Actions |
| 9 | 11 | 2.35 |  | Monsters A–Z > Actions |
| 10 | 6 | 1.66 |  | Magic Items > Helm of Brilliance |
| 11 | 4 | 1.58 |  | Magic Items > Staff of Fire |
| 12 | 20 | 1.47 |  | Character Creation > Tier 2 (Levels 5–10) |
| 13 | 3 | 1.20 |  | Magic Items > Staff of the Magi |
| 14 | 19 | 0.69 |  | Monsters A–Z > Actions |
| 15 | 7 | 0.00 |  | Magic Items > Hat of Many Spells |
| 16 | 5 | -0.60 |  | Magic Items > Staff of Power |
| 17 | 13 | -0.90 |  | Gameplay Toolbox > Fire-Casting Statue |
| 18 | 10 | -1.42 |  | Gameplay Toolbox > Fire-Casting Statue |
| 19 | 18 | -3.76 |  | Equipment > Tinderbox (5 SP) |
| 20 | 15 | -9.50 |  | Gameplay Toolbox > Spiked Pit |


*re-ranking* (query: `Revivify`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.38 | yes | Spells > Revivify |
| 2 | 2 | 2.59 | yes | Classes > Level 3 Paladin Spells |
| 3 | 3 | 2.14 | yes | Classes > Level 3: Life Domain Spells |
| 4 | 7 | 1.90 |  | Rules Glossary > Dead |
| 5 | 15 | 0.96 |  | Classes > Level 3 Cleric Spells |
| 6 | 16 | -0.07 |  | Classes > Level 3 Druid Spells |
| 7 | 11 | -0.26 |  | Classes > Level 3 Ranger Spells |
| 8 | 9 | -1.21 |  | Classes > Level 3: Life Domain Spells |
| 9 | 17 | -10.17 |  | Classes > Level 7 Cleric Spells |
| 10 | 13 | -10.22 |  | Classes > Level 3 Paladin Spells |
| 11 | 4 | -10.43 |  | Classes > Level 10: Self-Restoration |
| 12 | 6 | -10.60 |  | Spells > Reverse Gravity |
| 13 | 20 | -10.69 |  | Monsters A–Z > Bonus Actions |
| 14 | 8 | -10.81 |  | Spells > Wish |
| 15 | 19 | -10.86 |  | Monsters A–Z > Bonus Actions |
| 16 | 10 | -10.86 |  | Spells > Expeditious Retreat |
| 17 | 18 | -10.94 |  | Spells > Divine Favor |
| 18 | 12 | -11.02 |  | Feats > Alert |
| 19 | 14 | -11.10 |  | Classes > Level 20: Archdruid |
| 20 | 5 | -11.15 |  | Classes > Level 18: Superior Inspiration |

*retrieved sections:* Spells > Fireball | Magic Items > Wand of Fireballs | Spells > Revivify | Classes > Level 3 Paladin Spells | Classes > Level 3: Life Domain Spells

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Magic Items > Wand of Fireballs]
#### Wand of Fireballs  
_Wand, Rare (Requires Attunement by a Spellcaster)_  
This wand has 7 charges. While holding it, you can expend no more than 3 charges to cast _Fireball_ (save DC 15) from it. For 1 charge, you cast the level 3 version of the spell. You can increase the spell's level by 1 for each additional charge you expend.

---

[Spells > Revivify]
#### Revivify  
_Level 3 Necromancy (Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S, M (a diamond worth 500+ GP, which the spell consumes)
**Duration:** Instantaneous  
You touch a creature that has died within the last 10 minutes. That creature revives with 1 Hit Point. This spell can't revive a creature that has died of old age, nor does it restore any missing body parts.

---

[Classes > Level 3 Paladin Spells]
<td>Revivify</td>
<td>Necromancy</td>
<td>M</td>
</tr>
</tbody>
</table>

---

[Classes > Level 3: Life Domain Spells]
<td>Mass Healing Word, Revivify</td>
</tr>
<tr>
<td>7</td>
<td>Aura of Life, Death Ward</td>
</tr>
<tr>
<td>9</td>
<td>Greater Restoration, Mass Cure Wounds</td>
</tr>
</tbody>
</table>
```
</details>


---

## q3 (cross-file) What does the Alert feat let you add to your Initiative roll? And which background grants the Savage Attacker feat, what skill proficiencies does it give, and how often per turn can Savage Attacker be used?

**Gold facts (counterfactual data):** twice your Proficiency Bonus; Soldier; Athletics and Perception; Twice per turn


### v0_closed_book  (0 chunks, 1 LLM call(s))

The Alert feat lets you add your Wisdom modifier to your Initiative roll.

The Beast Tamer background grants the Savage Attacker feat. This background also provides proficiency in Animal Handling and Nature skills. The Savage Attacker feat allows you to make an additional attack when you hit with the first attack on your turn, but you can only use it once per turn.

*facts found (judge): 0/4; missing: twice your Proficiency Bonus; Soldier; Athletics and Perception; Twice per turn*


### v1_baseline  (3 chunks, 1 LLM call(s))

The Alert feat lets you add twice your Proficiency Bonus to your Initiative roll.

The context provided does not mention any background that grants the Savage Attacker feat or any skill proficiencies associated with it. Additionally, the frequency of using the Savage Attacker feat per turn is stated as "twice per turn."

*facts found (judge): 2/4; missing: Soldier; Athletics and Perception*

*retrieved sections:* Feats > Savage Attacker | Feats > Alert | Feats > Boon of Combat Prowess

<details><summary>full retrieved context</summary>

```
[Feats > Savage Attacker]
#### Savage Attacker  
_Origin Feat_  
You've trained to deal particularly damaging strikes. Twice per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

---

[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Feats > Boon of Combat Prowess]
### Epic Boon Feats  
#### Boon of Combat Prowess  
_Epic Boon Feat (Prerequisite: Level 19+)_  
You gain the following benefits.  
_Ability Score Increase._ Increase one ability score of your choice by 1, to a maximum of 30.  
_Peerless Aim._ When you miss with an attack roll, you can hit instead. Once you use this benefit, you can't use it again until the start of your next turn.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The Alert feat lets you add twice your Proficiency Bonus to your Initiative roll.

The context provided does not mention any background that grants the Savage Attacker feat, nor does it list any skill proficiencies associated with a background. Additionally, the context only describes the Savage Attacker feat itself without mentioning any backgrounds or skill proficiencies. Therefore, parts of the question regarding the background and skill proficiencies cannot be answered based on the given information.

*facts found (judge): 1/4; missing: Soldier; Athletics and Perception; Twice per turn*


*re-ranking* (query: `What does the Alert feat let you add to your Initiative roll? And which backgrou`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.76 | yes | Feats > Alert |
| 2 | 1 | 0.02 | yes | Feats > Savage Attacker |
| 3 | 3 | -3.17 | yes | Feats > Boon of Combat Prowess |
| 4 | 5 | -3.26 |  | Monsters > Initiative |
| 5 | 6 | -3.61 |  | Classes > Level 7: Feral Instinct |
| 6 | 4 | -3.85 |  | Playing the Game > Initiative |
| 7 | 7 | -5.93 |  | Rules Glossary > Help [Action] |
| 8 | 8 | -8.34 |  | Monsters A–Z > Actions |
| 9 | 10 | -8.36 |  | Classes > Level 5: Extra Attack |
| 10 | 9 | -9.14 |  | Classes > Level 13: Improved Brutal Strike |

*retrieved sections:* Feats > Alert | Feats > Savage Attacker | Feats > Boon of Combat Prowess

<details><summary>full retrieved context</summary>

```
[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Feats > Savage Attacker]
#### Savage Attacker  
_Origin Feat_  
You've trained to deal particularly damaging strikes. Twice per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

---

[Feats > Boon of Combat Prowess]
### Epic Boon Feats  
#### Boon of Combat Prowess  
_Epic Boon Feat (Prerequisite: Level 19+)_  
You gain the following benefits.  
_Ability Score Increase._ Increase one ability score of your choice by 1, to a maximum of 30.  
_Peerless Aim._ When you miss with an attack roll, you can hit instead. Once you use this benefit, you can't use it again until the start of your next turn.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The Alert feat lets you add twice your Proficiency Bonus to your Initiative roll.

The context provided does not contain information about which background grants the Savage Attacker feat, what skill proficiencies it gives, or how often per turn it can be used. Therefore, these parts are missing from the given information.

*facts found (judge): 1/4; missing: Soldier; Athletics and Perception; Twice per turn*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `What does the Alert feat let you add to your Initiative roll? And which backgrou`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.76 | yes | Feats > Alert |
| 2 | 1 | 0.02 | yes | Feats > Savage Attacker |
| 3 | 3 | -3.17 | yes | Feats > Boon of Combat Prowess |
| 4 | 5 | -3.26 | yes | Monsters > Initiative |
| 5 | 6 | -3.61 | yes | Classes > Level 7: Feral Instinct |
| 6 | 4 | -3.85 | yes | Playing the Game > Initiative |
| 7 | 7 | -5.93 | yes | Rules Glossary > Help [Action] |
| 8 | 8 | -8.34 |  | Monsters A–Z > Actions |
| 9 | 10 | -8.36 |  | Classes > Level 5: Extra Attack |
| 10 | 9 | -9.14 |  | Classes > Level 13: Improved Brutal Strike |

*retrieved sections:* Feats > Alert | Feats > Savage Attacker | Feats > Boon of Combat Prowess | Monsters > Initiative | Classes > Level 7: Feral Instinct | Playing the Game > Initiative | Rules Glossary > Help [Action] | Monsters A–Z > Reactions

<details><summary>full retrieved context</summary>

```
[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Feats > Savage Attacker]
#### Savage Attacker  
_Origin Feat_  
You've trained to deal particularly damaging strikes. Twice per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

---

[Feats > Boon of Combat Prowess]
### Epic Boon Feats  
#### Boon of Combat Prowess  
_Epic Boon Feat (Prerequisite: Level 19+)_  
You gain the following benefits.  
_Ability Score Increase._ Increase one ability score of your choice by 1, to a maximum of 30.  
_Peerless Aim._ When you miss with an attack roll, you can hit instead. Once you use this benefit, you can't use it again until the start of your next turn.

---

[Monsters > Initiative]
If you don't want to roll a monster's Initiative, use the Initiative score as the monster's Initiative in combat. Initiative is further detailed in "Playing the Game."

---

[Classes > Level 7: Feral Instinct]
#### Level 7: Feral Instinct  
Your instincts are so honed that you have Advantage on Initiative rolls.

---

[Playing the Game > Initiative]
**Surprise.** If a combatant is surprised by combat starting, that combatant has Disadvantage on their Initiative roll. For example, if an ambusher starts combat while hidden from a foe who is unaware that combat is starting, that foe is surprised.

---

[Rules Glossary > Help [Action]]
_Assist an Attack Roll._ You momentarily distract an enemy within 5 feet of you, giving Advantage to the next attack roll by one of your allies against that enemy. This benefit expires at the start of your next turn.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Burst of Ingenuity (2/Day)._** _Trigger:_ The sphinx or another creature within 30 feet makes an ability check or a saving throw. _Response:_ The sphinx adds 2 to the roll.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The Alert feat lets you add twice your Proficiency Bonus to your Initiative roll.

The context provided does not contain information about which background grants the Savage Attacker feat, what skill proficiencies it gives, or how often per turn Savage Attacker can be used.

*facts found (judge): 1/4; missing: Soldier; Athletics and Perception; Twice per turn*


*re-ranking* (query: `What does the Alert feat let you add to your Initiative roll? And which backgrou`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.76 | yes | Feats > Alert |
| 2 | 1 | 0.02 | yes | Feats > Savage Attacker |
| 3 | 9 | -2.82 | yes | Feats > Boon of Irresistible Offense |
| 4 | 3 | -3.17 |  | Feats > Boon of Combat Prowess |
| 5 | 5 | -3.26 |  | Monsters > Initiative |
| 6 | 4 | -3.85 |  | Playing the Game > Initiative |
| 7 | 6 | -5.93 |  | Rules Glossary > Help [Action] |
| 8 | 8 | -6.39 |  | Monsters A–Z > Reactions |
| 9 | 7 | -8.34 |  | Monsters A–Z > Actions |
| 10 | 10 | -8.69 |  | Monsters A–Z > Actions |

*retrieved sections:* Feats > Alert | Feats > Savage Attacker | Feats > Boon of Irresistible Offense

<details><summary>full retrieved context</summary>

```
[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Feats > Savage Attacker]
#### Savage Attacker  
_Origin Feat_  
You've trained to deal particularly damaging strikes. Twice per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

---

[Feats > Boon of Irresistible Offense]
_Overwhelming Strike._ When you roll a 20 on the d20 for an attack roll, you can deal extra damage to the target equal to the ability score increased by this feat. The extra damage's type is the same as the attack's type.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The Alert feat lets you add twice your Proficiency Bonus to your Initiative roll. The Soldier background grants the Savage Attacker feat, provides Skill Proficiencies in Athletics and Perception, and allows 2 uses per turn when hitting a target with a weapon.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What does the Alert feat let you add to your Initiative roll? And which backgrou`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.76 | yes | Feats > Alert |
| 2 | 1 | 0.02 | yes | Feats > Savage Attacker |
| 3 | 7 | -2.08 | yes | Character Origins > Soldier |
| 4 | 17 | -2.60 | yes | Playing the Game > Equipment Proficiencies |
| 5 | 19 | -2.80 | yes | Character Creation > Choose a Background |
| 6 | 16 | -2.82 | yes | Feats > Boon of Irresistible Offense |
| 7 | 5 | -3.17 | yes | Feats > Boon of Combat Prowess |
| 8 | 8 | -3.26 | yes | Monsters > Initiative |
| 9 | 6 | -3.85 |  | Playing the Game > Initiative |
| 10 | 21 | -3.92 |  | Character Origins > Criminal |
| 11 | 4 | -4.48 |  | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 12 | 9 | -4.49 |  | Character Origins > Skill Proficiencies |
| 13 | 3 | -4.62 |  | Feats > Grappler |
| 14 | 22 | -4.63 |  | Monsters > Initiative |
| 15 | 30 | -4.65 |  | Rules Glossary > Surprise |
| 16 | 29 | -5.03 |  | Playing the Game > The Bonus Doesn't Stack |
| 17 | 10 | -5.93 |  | Rules Glossary > Help [Action] |
| 18 | 13 | -6.19 |  | Playing the Game > Equipment Proficiencies |
| 19 | 14 | -6.39 |  | Monsters A–Z > Reactions |
| 20 | 15 | -6.81 |  | Magic Items > Bag of Tricks |

*retrieved sections:* Feats > Alert | Feats > Savage Attacker | Character Origins > Soldier | Playing the Game > Equipment Proficiencies | Character Creation > Choose a Background | Feats > Boon of Irresistible Offense | Feats > Boon of Combat Prowess | Monsters > Initiative

<details><summary>full retrieved context</summary>

```
[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Feats > Savage Attacker]
#### Savage Attacker  
_Origin Feat_  
You've trained to deal particularly damaging strikes. Twice per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

---

[Character Origins > Soldier]
#### Soldier  
**Ability Scores:** Strength, Dexterity, Constitution
**Feat:** Savage Attacker (see "Feats")
**Skill Proficiencies:** Athletics and Perception
**Tool Proficiency:** _Choose one kind of_ Gaming Set (see "Equipment")
**Equipment:** _Choose A or B:_ (A) Spear, Shortbow, 20 Arrows, Gaming Set (same as above), Healer's Kit, Quiver, Traveler's Clothes, 14 GP; or (B) 50 GP

---

[Playing the Game > Equipment Proficiencies]
### Equipment Proficiencies  
A character gains proficiency with various weapons and tools from their class and background. There are two categories of equipment proficiency:  
**Weapons.** Anyone can wield a weapon, but proficiency makes you better at wielding it. If you have proficiency with a weapon, you add your Proficiency Bonus to attack rolls you make with it.

---

[Character Creation > Choose a Background]
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>
<td>Constitution</td>
<td>Soldier</td>
</tr>
<tr>
<td>Intelligence</td>
<td>Acolyte</td>
</tr>
<tr>
<td>Wisdom</td>
<td>Acolyte</td>
</tr>
<tr>
<td>Charisma</td>
<td>Acolyte</td>
</tr>
</tbody>
</table>  
_Record Your Feat._ A background gives you a feat, which grants your character particular capabilities. Feats are detailed in "Feats." Write the feat on your character sheet.

---

[Feats > Boon of Irresistible Offense]
_Overwhelming Strike._ When you roll a 20 on the d20 for an attack roll, you can deal extra damage to the target equal to the ability score increased by this feat. The extra damage's type is the same as the attack's type.

---

[Feats > Boon of Combat Prowess]
### Epic Boon Feats  
#### Boon of Combat Prowess  
_Epic Boon Feat (Prerequisite: Level 19+)_  
You gain the following benefits.  
_Ability Score Increase._ Increase one ability score of your choice by 1, to a maximum of 30.  
_Peerless Aim._ When you miss with an attack roll, you can hit instead. Once you use this benefit, you can't use it again until the start of your next turn.

---

[Monsters > Initiative]
If you don't want to roll a monster's Initiative, use the Initiative score as the monster's Initiative in combat. Initiative is further detailed in "Playing the Game."
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The Alert feat lets you add twice your Proficiency Bonus to your Initiative roll.

The Soldier background grants the Savage Attacker feat. It gives the following skill proficiencies: Athletics and Perception. The Savage Attacker feat can be used twice per turn when you hit a target with a weapon.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What does the Alert feat let you add to your Initiative roll? And which backgrou`): candidate pool of 23, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.76 | yes | Feats > Alert |
| 2 | 1 | 0.02 | yes | Feats > Savage Attacker |
| 3 | 7 | -2.08 | yes | Character Origins > Soldier |
| 4 | 18 | -2.36 | yes | Playing the Game > Proficiency Bonus |
| 5 | 5 | -3.17 | yes | Feats > Boon of Combat Prowess |
| 6 | 8 | -3.26 | yes | Monsters > Initiative |
| 7 | 6 | -3.85 | yes | Playing the Game > Initiative |
| 8 | 4 | -4.48 | yes | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 9 | 9 | -4.49 |  | Character Origins > Skill Proficiencies |
| 10 | 11 | -4.57 |  | Character Origins > Feat |
| 11 | 3 | -4.62 |  | Feats > Grappler |
| 12 | 22 | -5.36 |  | Rules Glossary > Unarmed Strike |
| 13 | 10 | -5.93 |  | Rules Glossary > Help [Action] |
| 14 | 21 | -6.52 |  | Rules Glossary > Incapacitated [Condition] |
| 15 | 13 | -6.72 |  | Playing the Game > Skill Proficiencies |
| 16 | 12 | -8.07 |  | Playing the Game > Skill Proficiencies |
| 17 | 14 | -8.43 |  | Playing the Game > Skill Proficiencies |
| 18 | 19 | -8.53 |  | Monsters > Proficiency Bonus |
| 19 | 17 | -9.27 |  | Playing the Game > Proficiency |
| 20 | 16 | -9.47 |  | Playing the Game > Proficiency |

*retrieved sections:* Feats > Alert | Feats > Savage Attacker | Character Origins > Soldier | Playing the Game > Proficiency Bonus | Feats > Boon of Combat Prowess | Monsters > Initiative | Playing the Game > Initiative | Gameplay Toolbox > 3: Choose Skill Proficiencies

<details><summary>full retrieved context</summary>

```
[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Feats > Savage Attacker]
#### Savage Attacker  
_Origin Feat_  
You've trained to deal particularly damaging strikes. Twice per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

---

[Character Origins > Soldier]
#### Soldier  
**Ability Scores:** Strength, Dexterity, Constitution
**Feat:** Savage Attacker (see "Feats")
**Skill Proficiencies:** Athletics and Perception
**Tool Proficiency:** _Choose one kind of_ Gaming Set (see "Equipment")
**Equipment:** _Choose A or B:_ (A) Spear, Shortbow, 20 Arrows, Gaming Set (same as above), Healer's Kit, Quiver, Traveler's Clothes, 14 GP; or (B) 50 GP

---

[Playing the Game > Proficiency Bonus]
#### Proficiency Bonus  
You add your Proficiency Bonus to your attack roll when you attack using a weapon you have proficiency with, as well as when you attack with a spell. See "Proficiency" later in "Playing the Game" for more information about weapon proficiencies.

---

[Feats > Boon of Combat Prowess]
### Epic Boon Feats  
#### Boon of Combat Prowess  
_Epic Boon Feat (Prerequisite: Level 19+)_  
You gain the following benefits.  
_Ability Score Increase._ Increase one ability score of your choice by 1, to a maximum of 30.  
_Peerless Aim._ When you miss with an attack roll, you can hit instead. Once you use this benefit, you can't use it again until the start of your next turn.

---

[Monsters > Initiative]
If you don't want to roll a monster's Initiative, use the Initiative score as the monster's Initiative in combat. Initiative is further detailed in "Playing the Game."

---

[Playing the Game > Initiative]
**Surprise.** If a combatant is surprised by combat starting, that combatant has Disadvantage on their Initiative roll. For example, if an ambusher starts combat while hidden from a foe who is unaware that combat is starting, that foe is surprised.

---

[Gameplay Toolbox > 3: Choose Skill Proficiencies]
### 3: Choose Skill Proficiencies  
Choose two skills appropriate for the background. There needn't be a relationship between the skill proficiencies a background grants and the ability scores it increases.
```
</details>


### v6_agentic  (10 chunks, 3 LLM call(s))

The Alert feat lets you add twice your Proficiency Bonus to your Initiative roll.

The Soldier background grants the Savage Attacker feat, provides Skill Proficiencies in Athletics and Perception, and gives Tool Proficiency in a Gaming Set. The Savage Attacker feat can be used twice per turn when hitting a target with a weapon.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Alert / Savage Attacker feat / Savage Attacker feat / Savage Attacker feat


*re-ranking* (query: `Alert`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | 3.07 | yes | Spells > Alarm |
| 2 | 3 | 2.56 | yes | Spells > Alarm |
| 3 | 7 | 0.32 | yes | Magic Items > Rod of Alertness |
| 4 | 8 | -0.16 |  | Magic Items > Rod of Alertness |
| 5 | 16 | -0.32 |  | Magic Items > Weapon of Warning |
| 6 | 1 | -0.44 |  | Magic Items > Rod of Alertness |
| 7 | 2 | -0.76 | yes | Feats > Alert |
| 8 | 13 | -2.32 |  | Spells > Alarm |
| 9 | 4 | -2.33 | yes | Character Origins > Criminal |
| 10 | 10 | -8.20 |  | Playing the Game > Actions |
| 11 | 6 | -8.51 |  | Monsters A–Z > Reactions |
| 12 | 17 | -9.02 |  | Monsters A–Z > Reactions |
| 13 | 18 | -9.09 |  | Rules Glossary > Hide [Action] |
| 14 | 11 | -9.22 |  | Monsters A–Z > Reactions |
| 15 | 12 | -9.27 |  | Monsters A–Z > Actions |
| 16 | 9 | -9.53 |  | Monsters A–Z > Bonus Actions |
| 17 | 15 | -9.57 |  | Monsters A–Z > Bonus Actions |
| 18 | 14 | -9.78 |  | Playing the Game > Opportunity Attacks |
| 19 | 19 | -10.24 |  | Monsters A–Z > Actions |
| 20 | 20 | -10.48 |  | Playing the Game > Actions |


*re-ranking* (query: `Savage Attacker feat`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 8.16 | yes | Feats > Savage Attacker |
| 2 | 4 | 4.67 | yes | Character Origins > Soldier |
| 3 | 5 | -3.73 | yes | Feats > Great Weapon Fighting |
| 4 | 2 | -5.50 |  | Feats > Archery |
| 5 | 9 | -6.97 |  | Monsters A–Z > Actions |
| 6 | 13 | -8.30 |  | Monsters A–Z > Actions |
| 7 | 7 | -8.52 |  | Monsters A–Z > Actions |
| 8 | 19 | -8.64 |  | Feats > Feat Descriptions |
| 9 | 3 | -9.14 |  | Monsters A–Z > Actions |
| 10 | 18 | -9.22 |  | Classes > Level 1: Fighting Style |
| 11 | 17 | -9.39 |  | Monsters A–Z > Actions |
| 12 | 15 | -9.43 |  | Monsters A–Z > Actions |
| 13 | 8 | -9.64 |  | Character Origins > Feat |
| 14 | 6 | -9.73 |  | Feats > Parts of a Feat |
| 15 | 10 | -9.82 |  | Gameplay Toolbox > 2: Choose a Feat |
| 16 | 16 | -9.84 |  | Feats > Magic Initiate |
| 17 | 12 | -9.96 |  | Feats > Parts of a Feat |
| 18 | 20 | -10.08 |  | Feats > Ability Score Improvement |
| 19 | 11 | -10.10 |  | Monsters A–Z > Reactions |
| 20 | 14 | -10.22 |  | Spells > Faerie Fire |


*re-ranking* (query: `Savage Attacker feat`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 8.16 | yes | Feats > Savage Attacker |
| 2 | 4 | 4.67 | yes | Character Origins > Soldier |
| 3 | 5 | -3.73 | yes | Feats > Great Weapon Fighting |
| 4 | 2 | -5.50 |  | Feats > Archery |
| 5 | 9 | -6.97 |  | Monsters A–Z > Actions |
| 6 | 13 | -8.30 |  | Monsters A–Z > Actions |
| 7 | 7 | -8.52 |  | Monsters A–Z > Actions |
| 8 | 19 | -8.64 |  | Feats > Feat Descriptions |
| 9 | 3 | -9.14 |  | Monsters A–Z > Actions |
| 10 | 18 | -9.22 |  | Classes > Level 1: Fighting Style |
| 11 | 17 | -9.39 |  | Monsters A–Z > Actions |
| 12 | 15 | -9.43 |  | Monsters A–Z > Actions |
| 13 | 8 | -9.64 |  | Character Origins > Feat |
| 14 | 6 | -9.73 |  | Feats > Parts of a Feat |
| 15 | 10 | -9.82 |  | Gameplay Toolbox > 2: Choose a Feat |
| 16 | 16 | -9.84 |  | Feats > Magic Initiate |
| 17 | 12 | -9.96 |  | Feats > Parts of a Feat |
| 18 | 20 | -10.08 |  | Feats > Ability Score Improvement |
| 19 | 11 | -10.10 |  | Monsters A–Z > Reactions |
| 20 | 14 | -10.22 |  | Spells > Faerie Fire |


*re-ranking* (query: `Savage Attacker feat`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 8.16 | yes | Feats > Savage Attacker |
| 2 | 4 | 4.67 | yes | Character Origins > Soldier |
| 3 | 5 | -3.73 | yes | Feats > Great Weapon Fighting |
| 4 | 2 | -5.50 |  | Feats > Archery |
| 5 | 9 | -6.97 |  | Monsters A–Z > Actions |
| 6 | 13 | -8.30 |  | Monsters A–Z > Actions |
| 7 | 7 | -8.52 |  | Monsters A–Z > Actions |
| 8 | 19 | -8.64 |  | Feats > Feat Descriptions |
| 9 | 3 | -9.14 |  | Monsters A–Z > Actions |
| 10 | 18 | -9.22 |  | Classes > Level 1: Fighting Style |
| 11 | 17 | -9.39 |  | Monsters A–Z > Actions |
| 12 | 15 | -9.43 |  | Monsters A–Z > Actions |
| 13 | 8 | -9.64 |  | Character Origins > Feat |
| 14 | 6 | -9.73 |  | Feats > Parts of a Feat |
| 15 | 10 | -9.82 |  | Gameplay Toolbox > 2: Choose a Feat |
| 16 | 16 | -9.84 |  | Feats > Magic Initiate |
| 17 | 12 | -9.96 |  | Feats > Parts of a Feat |
| 18 | 20 | -10.08 |  | Feats > Ability Score Improvement |
| 19 | 11 | -10.10 |  | Monsters A–Z > Reactions |
| 20 | 14 | -10.22 |  | Spells > Faerie Fire |


*re-ranking* (query: `Alert feat`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.44 | yes | Feats > Alert |
| 2 | 7 | 1.64 | yes | Character Origins > Criminal |
| 3 | 19 | -3.00 | yes | Magic Items > Rod of Alertness |
| 4 | 15 | -3.64 |  | Feats > Magic Initiate |
| 5 | 3 | -3.85 |  | Feats > Boon of Irresistible Offense |
| 6 | 8 | -4.20 |  | Feats > Parts of a Feat |
| 7 | 16 | -4.21 |  | Magic Items > Rod of Alertness |
| 8 | 11 | -4.38 |  | Feats > Boon of Combat Prowess |
| 9 | 2 | -4.44 |  | Feats > Feat Descriptions |
| 10 | 4 | -4.45 |  | Feats > Boon of Irresistible Offense |
| 11 | 13 | -4.53 |  | Feats > Parts of a Feat |
| 12 | 20 | -4.67 |  | Feats > Ability Score Improvement |
| 13 | 10 | -5.19 |  | Character Origins > Feat |
| 14 | 12 | -5.63 |  | Gameplay Toolbox > 2: Choose a Feat |
| 15 | 17 | -8.03 |  | Classes > Level 1: Fighting Style |
| 16 | 6 | -10.09 |  | Monsters A–Z > Bonus Actions |
| 17 | 9 | -10.20 |  | Monsters A–Z > Actions |
| 18 | 14 | -10.36 |  | Monsters A–Z > Actions |
| 19 | 5 | -10.52 |  | Monsters A–Z > Reactions |
| 20 | 18 | -10.89 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Initiative roll`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 6.68 | yes | Rules Glossary > Initiative |
| 2 | 2 | 6.66 | yes | Playing the Game > Initiative |
| 3 | 1 | 5.79 | yes | Feats > Alert |
| 4 | 18 | 5.73 |  | Monsters > Initiative |
| 5 | 4 | 5.19 |  | Playing the Game > Initiative |
| 6 | 19 | 5.14 |  | Monsters > Initiative |
| 7 | 5 | 4.14 |  | Gameplay Toolbox > Rolling Stone |
| 8 | 9 | 3.93 |  | Rules Glossary > Surprise |
| 9 | 8 | 2.13 |  | Playing the Game > Combat Step by Step |
| 10 | 6 | 1.27 |  | Rules Glossary > Incapacitated [Condition] |
| 11 | 7 | 0.79 |  | Playing the Game > Initiative |
| 12 | 13 | 0.19 |  | Feats > Boon of Fate |
| 13 | 12 | -4.19 |  | Rules Glossary > Attack Roll |
| 14 | 20 | -4.21 |  | Playing the Game > Combat Step by Step |
| 15 | 17 | -4.52 |  | Playing the Game > Attack Rolls |
| 16 | 15 | -6.65 |  | Monsters A–Z > Succubus |
| 17 | 10 | -6.91 |  | Playing the Game > Roll Two D20s |
| 18 | 16 | -7.05 |  | Playing the Game > D20 Tests |
| 19 | 11 | -7.44 |  | Playing the Game > They Don't Stack |
| 20 | 14 | -8.44 |  | Rules Glossary > Advantage |

*retrieved sections:* Spells > Alarm | Magic Items > Rod of Alertness | Feats > Savage Attacker | Character Origins > Soldier | Feats > Great Weapon Fighting | Feats > Alert | Character Origins > Criminal | Rules Glossary > Initiative | Playing the Game > Initiative

<details><summary>full retrieved context</summary>

```
[Spells > Alarm]
**Duration:** 8 hours  
You set an alarm against intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot Cube. Until the spell ends, an alarm alerts you whenever a creature touches or enters the warded area. When you cast the spell, you can designate creatures that won't set off the alarm. You also choose whether the alarm is audible or mental:  
**Audible Alarm.** The alarm produces the sound of a handbell for 10 seconds within 60 feet of the warded area.

---

[Spells > Alarm]
**Mental Alarm.** You are alerted by a mental ping if you are within 1 mile of the warded area. This ping awakens you if you're asleep.

---

[Magic Items > Rod of Alertness]
The rod's head stops glowing and the effect ends after 10 minutes or when a creature takes a Magic action to pull the rod from the ground. Once used, this property can't be used again until the next dawn.

---

[Feats > Savage Attacker]
#### Savage Attacker  
_Origin Feat_  
You've trained to deal particularly damaging strikes. Twice per turn when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

---

[Character Origins > Soldier]
#### Soldier  
**Ability Scores:** Strength, Dexterity, Constitution
**Feat:** Savage Attacker (see "Feats")
**Skill Proficiencies:** Athletics and Perception
**Tool Proficiency:** _Choose one kind of_ Gaming Set (see "Equipment")
**Equipment:** _Choose A or B:_ (A) Spear, Shortbow, 20 Arrows, Gaming Set (same as above), Healer's Kit, Quiver, Traveler's Clothes, 14 GP; or (B) 50 GP

---

[Feats > Great Weapon Fighting]
#### Great Weapon Fighting  
_Fighting Style Feat (Prerequisite: Fighting Style Feature)_  
When you roll damage for an attack you make with a Melee weapon that you are holding with two hands, you can treat any 1 or 2 on a damage die as a 3. The weapon must have the Two-Handed or Versatile property to gain this benefit.

---

[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Character Origins > Criminal]
#### Criminal  
**Ability Scores:** Dexterity, Constitution, Intelligence
**Feat:** Alert (see "Feats")
**Skill Proficiencies:** Sleight of Hand and Stealth
**Tool Proficiency:** Thieves' Tools
**Equipment:** _Choose A or B:_ (A) 2 Daggers, Thieves' Tools, Crowbar, 2 Pouches, Traveler's Clothes, 16 GP; or (B) 50 GP

---

[Rules Glossary > Initiative]
#### Initiative  
Initiative determines the order of turns during combat. The combat rules in "Playing the Game" explain how to roll Initiative.  
Sometimes a GM might have combatants use their Initiative scores instead of rolling Initiative. Your Initiative score equals 10 plus your Dexterity modifier. If you have Advantage on Initiative rolls, increase your Initiative score by 5. If you have Disadvantage on those rolls, decrease that score by 5. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Initiative]
#### Initiative  
Initiative determines the order of turns during combat. When combat starts, every participant rolls Initiative; they make a Dexterity check that determines their place in the Initiative order. The GM rolls for monsters. For a group of identical creatures, the GM makes a single roll, so each member of the group has the same Initiative.
```
</details>


---

## q4 (cross-file) How much weight and volume can a Bag of Holding hold, and how much does the bag itself weigh? Also, what bonus does a Cloak of Protection give and does it need attunement?

**Gold facts (counterfactual data):** 800 pounds; 96 cubic feet; 5 pounds; +2 bonus to Armor Class; Requires Attunement


### v0_closed_book  (0 chunks, 1 LLM call(s))

A Bag of Holding can hold an unlimited amount of weight and volume, but it cannot expand to fill more than its own space. The bag itself weighs 2 pounds.

The Cloak of Protection gives the wearer a +1 bonus to AC and saving throws. It requires attunement by a character who is proficient in armor.

*facts found (judge): 1/5; missing: 800 pounds; 96 cubic feet; 5 pounds; +2 bonus to Armor Class*


### v1_baseline  (3 chunks, 1 LLM call(s))

A Bag of Holding can hold up to 800 pounds of material, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds.

The context provided does not mention a Cloak of Protection, so information about its bonus or attunement requirements is missing.

*facts found (judge): 3/5; missing: +2 bonus to Armor Class; Requires Attunement*

*retrieved sections:* Magic Items > Bag of Holding | Magic Items > Handy Haversack | Equipment > Backpack (2 GP)

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Magic Items > Handy Haversack]
#### Handy Haversack  
_Wondrous Item, Rare_  
This backpack has a central pouch and two side pouches, each of which is an extradimensional space. Each side pouch can hold up to 200 pounds of material, not exceeding a volume of 25 cubic feet. The central pouch can hold up to 500 pounds of material, not exceeding a volume of 64 cubic feet. The haversack always weighs 5 pounds, regardless of its contents.

---

[Equipment > Backpack (2 GP)]
#### Backpack (2 GP)  
A Backpack holds up to 30 pounds within 1 cubic foot. It can also serve as a saddlebag.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The Bag of Holding can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds.

The context provided does not mention a Cloak of Protection, so information about its bonus or attunement requirements is missing.

*facts found (judge): 3/5; missing: +2 bonus to Armor Class; Requires Attunement*


*re-ranking* (query: `How much weight and volume can a Bag of Holding hold, and how much does the bag `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.33 | yes | Magic Items > Bag of Holding |
| 2 | 3 | -1.37 | yes | Equipment > Backpack (2 GP) |
| 3 | 2 | -1.84 | yes | Magic Items > Handy Haversack |
| 4 | 7 | -3.75 |  | Magic Items > Bag of Holding |
| 5 | 8 | -3.83 |  | Equipment > Sack (1 CP) |
| 6 | 6 | -3.92 |  | Equipment > Pouch (5 SP) |
| 7 | 5 | -6.85 |  | Magic Items > Cloak of Protection |
| 8 | 9 | -9.45 |  | Magic Items > Cloak of the Bat |
| 9 | 10 | -9.92 |  | Magic Items > Wings of Flying |
| 10 | 4 | -10.25 |  | Playing the Game > Carrying Objects |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Backpack (2 GP) | Magic Items > Handy Haversack

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Backpack (2 GP)]
#### Backpack (2 GP)  
A Backpack holds up to 30 pounds within 1 cubic foot. It can also serve as a saddlebag.

---

[Magic Items > Handy Haversack]
#### Handy Haversack  
_Wondrous Item, Rare_  
This backpack has a central pouch and two side pouches, each of which is an extradimensional space. Each side pouch can hold up to 200 pounds of material, not exceeding a volume of 25 cubic feet. The central pouch can hold up to 500 pounds of material, not exceeding a volume of 64 cubic feet. The haversack always weighs 5 pounds, regardless of its contents.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

A Bag of Holding can hold up to 800 pounds of weight and a volume of 96 cubic feet. The bag itself weighs 5 pounds.

The Cloak of Protection gives a +2 bonus to Armor Class and saving throws while worn and requires attunement.

*facts found (judge): 4/5; missing: Requires Attunement*


*re-ranking* (query: `How much weight and volume can a Bag of Holding hold, and how much does the bag `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.33 | yes | Magic Items > Bag of Holding |
| 2 | 3 | -1.37 | yes | Equipment > Backpack (2 GP) |
| 3 | 2 | -1.84 | yes | Magic Items > Handy Haversack |
| 4 | 7 | -3.75 | yes | Magic Items > Bag of Holding |
| 5 | 8 | -3.83 | yes | Equipment > Sack (1 CP) |
| 6 | 6 | -3.92 | yes | Equipment > Pouch (5 SP) |
| 7 | 5 | -6.85 | yes | Magic Items > Cloak of Protection |
| 8 | 9 | -9.45 | yes | Magic Items > Cloak of the Bat |
| 9 | 10 | -9.92 |  | Magic Items > Wings of Flying |
| 10 | 4 | -10.25 |  | Playing the Game > Carrying Objects |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Backpack (2 GP) | Magic Items > Handy Haversack | Equipment > Sack (1 CP) | Equipment > Pouch (5 SP) | Magic Items > Cloak of Protection | Magic Items > Cloak of the Bat

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Backpack (2 GP)]
#### Backpack (2 GP)  
A Backpack holds up to 30 pounds within 1 cubic foot. It can also serve as a saddlebag.

---

[Magic Items > Handy Haversack]
#### Handy Haversack  
_Wondrous Item, Rare_  
This backpack has a central pouch and two side pouches, each of which is an extradimensional space. Each side pouch can hold up to 200 pounds of material, not exceeding a volume of 25 cubic feet. The central pouch can hold up to 500 pounds of material, not exceeding a volume of 64 cubic feet. The haversack always weighs 5 pounds, regardless of its contents.

---

[Magic Items > Bag of Holding]
If the bag is overloaded, pierced, or torn, it is destroyed, and its contents are scattered in the Astral Plane. If the bag is turned inside out, its contents spill forth unharmed, but the bag must be put right before it can be used again. The bag holds enough air for 10 minutes of breathing, divided by the number of breathing creatures inside.

---

[Equipment > Sack (1 CP)]
#### Sack (1 CP)  
A Sack holds up to 30 pounds within 1 cubic foot.

---

[Equipment > Pouch (5 SP)]
#### Pouch (5 SP)  
A Pouch holds up to 6 pounds within one-fifth of a cubic foot.

---

[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Cloak of the Bat]
#### Cloak of the Bat  
_Wondrous Item, Rare (Requires Attunement)_  
While wearing this cloak, you have Advantage on Dexterity (Stealth) checks. In an area of Dim Light or Darkness, you can grip the edges of the cloak and use it to gain a Fly Speed of 40 feet. If you ever fail to grip the cloak's edges while flying in this way, or if you are no longer in Dim Light or Darkness, you lose this Fly Speed.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The Bag of Holding can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds.

The context provided does not mention a Cloak of Protection, so information about its bonus or attunement requirements is missing.

*facts found (judge): 3/5; missing: +2 bonus to Armor Class; Requires Attunement*


*re-ranking* (query: `How much weight and volume can a Bag of Holding hold, and how much does the bag `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.33 | yes | Magic Items > Bag of Holding |
| 2 | 3 | -1.37 | yes | Equipment > Backpack (2 GP) |
| 3 | 2 | -1.84 | yes | Magic Items > Handy Haversack |
| 4 | 7 | -3.75 |  | Magic Items > Bag of Holding |
| 5 | 8 | -3.83 |  | Equipment > Sack (1 CP) |
| 6 | 6 | -3.92 |  | Equipment > Pouch (5 SP) |
| 7 | 5 | -6.85 |  | Magic Items > Cloak of Protection |
| 8 | 9 | -9.45 |  | Magic Items > Cloak of the Bat |
| 9 | 10 | -9.92 |  | Magic Items > Wings of Flying |
| 10 | 4 | -10.25 |  | Playing the Game > Carrying Objects |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Backpack (2 GP) | Magic Items > Handy Haversack

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Backpack (2 GP)]
#### Backpack (2 GP)  
A Backpack holds up to 30 pounds within 1 cubic foot. It can also serve as a saddlebag.

---

[Magic Items > Handy Haversack]
#### Handy Haversack  
_Wondrous Item, Rare_  
This backpack has a central pouch and two side pouches, each of which is an extradimensional space. Each side pouch can hold up to 200 pounds of material, not exceeding a volume of 25 cubic feet. The central pouch can hold up to 500 pounds of material, not exceeding a volume of 64 cubic feet. The haversack always weighs 5 pounds, regardless of its contents.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The Bag of Holding can hold up to 800 pounds of material, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds, regardless of its contents. 

The context provided does not mention a Cloak of Protection, so information about its bonus or attunement requirements is missing.

*facts found (judge): 3/5; missing: +2 bonus to Armor Class; Requires Attunement*


*re-ranking* (query: `How much weight and volume can a Bag of Holding hold, and how much does the bag `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.33 | yes | Magic Items > Bag of Holding |
| 2 | 23 | -1.37 | yes | Equipment > Backpack (2 GP) |
| 3 | 3 | -1.84 | yes | Magic Items > Handy Haversack |
| 4 | 6 | -3.75 | yes | Magic Items > Bag of Holding |
| 5 | 28 | -3.83 | yes | Equipment > Sack (1 CP) |
| 6 | 26 | -3.92 | yes | Equipment > Pouch (5 SP) |
| 7 | 14 | -4.92 | yes | Magic Items > Bag of Devouring |
| 8 | 30 | -5.47 | yes | Magic Items > Bag of Beans |
| 9 | 21 | -6.30 |  | Magic Items > Bag of Holding |
| 10 | 2 | -6.85 |  | Magic Items > Cloak of Protection |
| 11 | 18 | -6.86 |  | Magic Items > Bag of Devouring |
| 12 | 12 | -8.01 |  | Magic Items > Shield of the Cavalier |
| 13 | 13 | -8.06 |  | Magic Items > Bead of Force |
| 14 | 5 | -8.64 |  | Magic Items > Bag of Tricks |
| 15 | 7 | -8.81 |  | Magic Items > Cloak of the Manta Ray |
| 16 | 20 | -8.97 |  | Magic Items > Bag of Devouring |
| 17 | 17 | -9.29 |  | Magic Items > Staff of Power |
| 18 | 10 | -9.37 |  | Magic Items > Ring of Protection |
| 19 | 11 | -9.41 |  | Magic Items > Cloak of Elvenkind |
| 20 | 8 | -9.45 |  | Magic Items > Cloak of the Bat |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Backpack (2 GP) | Magic Items > Handy Haversack | Equipment > Sack (1 CP) | Equipment > Pouch (5 SP) | Magic Items > Bag of Devouring | Magic Items > Bag of Beans

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Backpack (2 GP)]
#### Backpack (2 GP)  
A Backpack holds up to 30 pounds within 1 cubic foot. It can also serve as a saddlebag.

---

[Magic Items > Handy Haversack]
#### Handy Haversack  
_Wondrous Item, Rare_  
This backpack has a central pouch and two side pouches, each of which is an extradimensional space. Each side pouch can hold up to 200 pounds of material, not exceeding a volume of 25 cubic feet. The central pouch can hold up to 500 pounds of material, not exceeding a volume of 64 cubic feet. The haversack always weighs 5 pounds, regardless of its contents.

---

[Magic Items > Bag of Holding]
If the bag is overloaded, pierced, or torn, it is destroyed, and its contents are scattered in the Astral Plane. If the bag is turned inside out, its contents spill forth unharmed, but the bag must be put right before it can be used again. The bag holds enough air for 10 minutes of breathing, divided by the number of breathing creatures inside.

---

[Equipment > Sack (1 CP)]
#### Sack (1 CP)  
A Sack holds up to 30 pounds within 1 cubic foot.

---

[Equipment > Pouch (5 SP)]
#### Pouch (5 SP)  
A Pouch holds up to 6 pounds within one-fifth of a cubic foot.

---

[Magic Items > Bag of Devouring]
Inanimate objects can be stored in the bag, which can hold a cubic foot of such material. However, once each day, the bag swallows any objects inside it and spits them out into another plane of existence. The GM determines the time and plane.  
If the bag is pierced or torn, it is destroyed, and anything contained within it is transported to a random location on the Astral Plane.

---

[Magic Items > Bag of Beans]
#### Bag of Beans  
_Wondrous Item, Rare_  
This heavy cloth bag contains 3d4 dry beans when found. The bag weighs half a pound regardless of how many beans it contains and becomes a non-magical item when it no longer contains any beans.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

A Bag of Holding can hold up to 800 pounds of material, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds, regardless of its contents.

The Cloak of Protection gives a +2 bonus to Armor Class and saving throws while worn and requires attunement.

*facts found (judge): 5/5; missing: none*


*re-ranking* (query: `How much weight and volume can a Bag of Holding hold, and how much does the bag `): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.33 | yes | Magic Items > Bag of Holding |
| 2 | 3 | -1.84 | yes | Magic Items > Handy Haversack |
| 3 | 6 | -3.75 | yes | Magic Items > Bag of Holding |
| 4 | 11 | -6.30 | yes | Magic Items > Bag of Holding |
| 5 | 2 | -6.85 | yes | Magic Items > Cloak of Protection |
| 6 | 5 | -8.64 | yes | Magic Items > Bag of Tricks |
| 7 | 7 | -8.81 | yes | Magic Items > Cloak of the Manta Ray |
| 8 | 10 | -9.37 | yes | Magic Items > Ring of Protection |
| 9 | 8 | -9.45 |  | Magic Items > Cloak of the Bat |
| 10 | 4 | -9.75 |  | Magic Items > Cloak of Invisibility |
| 11 | 9 | -9.92 |  | Magic Items > Wings of Flying |
| 12 | 19 | -11.17 |  | Rules Glossary > Invisible [Condition] |
| 13 | 18 | -11.21 |  | Rules Glossary > Invisible [Condition] |
| 14 | 16 | -11.22 |  | Spells > Saving Throws |
| 15 | 12 | -11.24 |  | Magic Items > Charges |
| 16 | 20 | -11.24 |  | Rules Glossary > Friendly [Attitude] |
| 17 | 14 | -11.25 |  | Monsters > Armor Class |
| 18 | 13 | -11.31 |  | Rules Glossary > Utilize [Action] |
| 19 | 15 | -11.31 |  | Character Creation > Armor Class |
| 20 | 17 | -11.32 |  | Playing the Game > Saving Throws |

*retrieved sections:* Magic Items > Bag of Holding | Magic Items > Handy Haversack | Magic Items > Cloak of Protection | Magic Items > Bag of Tricks | Magic Items > Cloak of the Manta Ray | Magic Items > Ring of Protection

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Magic Items > Handy Haversack]
#### Handy Haversack  
_Wondrous Item, Rare_  
This backpack has a central pouch and two side pouches, each of which is an extradimensional space. Each side pouch can hold up to 200 pounds of material, not exceeding a volume of 25 cubic feet. The central pouch can hold up to 500 pounds of material, not exceeding a volume of 64 cubic feet. The haversack always weighs 5 pounds, regardless of its contents.

---

[Magic Items > Bag of Holding]
If the bag is overloaded, pierced, or torn, it is destroyed, and its contents are scattered in the Astral Plane. If the bag is turned inside out, its contents spill forth unharmed, but the bag must be put right before it can be used again. The bag holds enough air for 10 minutes of breathing, divided by the number of breathing creatures inside.

---

[Magic Items > Bag of Holding]
Placing a _Bag of Holding_ inside an extradimensional space created by a _Handy Haversack_, _Portable Hole_, or similar item instantly destroys both items and opens a gate to the Astral Plane. The gate originates where the one item was placed inside the other. Any creature within a 10-foot-radius Sphere centered on the gate is sucked through it to a random location on the Astral Plane. The gate then closes. The gate is one-way and can't be reopened.

---

[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Bag of Tricks]
The creature is Friendly to you and your allies, and it acts immediately after you on your Initiative count. You can take a Bonus Action to command how the creature moves and what action it takes on its next turn, such as attacking an enemy. In the absence of such orders, the creature acts in a fashion appropriate to its nature.  
Once three fuzzy objects have been pulled from the bag, the bag can't be used again until the next dawn.  
**Gray Bag of Tricks**  
<table>
<thead>
<tr>
<th>1d8</th>

---

[Magic Items > Cloak of the Manta Ray]
#### Cloak of the Manta Ray  
_Wondrous Item, Uncommon (Requires Attunement)_  
While wearing this cloak, you can breathe underwater, and you have a Swim Speed of 60 feet.

---

[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.
```
</details>


### v6_agentic  (7 chunks, 3 LLM call(s))

A Bag of Holding can hold up to 800 pounds of weight and has an interior volume of 96 cubic feet. The bag itself weighs 5 pounds.

The Cloak of Protection gives a +2 bonus to Armor Class and saving throws while worn and requires attunement.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* Bag of Holding / Cloak of Protection / weight Bag of Holding / volume Bag of Holding / weight of Bag of Holding / attunement Cloak of Protection


*re-ranking* (query: `Bag of Holding`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.75 | yes | Magic Items > Bag of Holding |
| 2 | 3 | 7.65 | yes | Magic Items > Bag of Holding |
| 3 | 5 | 6.09 | yes | Magic Items > Bag of Holding |
| 4 | 2 | 5.31 |  | Magic Items > Bag of Devouring |
| 5 | 8 | 3.85 |  | Magic Items > Bag of Devouring |
| 6 | 20 | 2.97 |  | Magic Items > Mirror of Life Trapping |
| 7 | 16 | 1.75 |  | Monsters A–Z > Traits |
| 8 | 13 | -0.65 |  | Magic Items > Magic Item Categories |
| 9 | 10 | -1.47 |  | Magic Items > Bag of Devouring |
| 10 | 12 | -1.48 |  | Magic Items > Bag of Tricks |
| 11 | 19 | -1.65 | yes | Equipment > Backpack (2 GP) |
| 12 | 4 | -1.70 |  | Magic Items > Bag of Devouring |
| 13 | 7 | -1.84 |  | Magic Items > Bag of Tricks |
| 14 | 6 | -2.05 |  | Magic Items > Bag of Tricks |
| 15 | 11 | -3.48 |  | Magic Items > Bag of Beans |
| 16 | 9 | -4.34 |  | Magic Items > Bag of Beans |
| 17 | 14 | -4.40 |  | Magic Items > Bag of Beans |
| 18 | 17 | -4.71 |  | Magic Items > Handy Haversack |
| 19 | 15 | -5.40 |  | Magic Items > Bag of Beans |
| 20 | 18 | -10.20 |  | Playing the Game > Carrying Objects |


*re-ranking* (query: `Cloak of Protection`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.10 | yes | Magic Items > Cloak of Protection |
| 2 | 3 | 2.08 | yes | Magic Items > Cloak of Invisibility |
| 3 | 6 | 1.56 | yes | Magic Items > Cloak of Displacement |
| 4 | 2 | 1.23 |  | Magic Items > Cloak of Elvenkind |
| 5 | 5 | 0.69 |  | Magic Items > Cloak of the Bat |
| 6 | 9 | 0.18 |  | Magic Items > Cloak of Arachnida |
| 7 | 8 | -0.50 |  | Magic Items > Cloak of the Bat |
| 8 | 12 | -1.58 |  | Magic Items > Scarab of Protection |
| 9 | 7 | -1.76 |  | Magic Items > Mantle of Spell Resistance |
| 10 | 4 | -1.91 |  | Magic Items > Cloak of the Manta Ray |
| 11 | 17 | -2.80 |  | Classes > Level 15: Smite of Protection |
| 12 | 16 | -3.35 |  | Magic Items > Cloak of Arachnida |
| 13 | 10 | -3.74 |  | Magic Items > Ring of Protection |
| 14 | 13 | -4.94 |  | Spells > Protection from Evil and Good |
| 15 | 20 | -5.11 |  | Monsters A–Z > Bonus Actions |
| 16 | 18 | -5.14 |  | Monsters A–Z > Bonus Actions |
| 17 | 11 | -5.50 |  | Magic Items > Wings of Flying |
| 18 | 14 | -5.94 |  | Spells > Protection from Evil and Good |
| 19 | 15 | -6.08 |  | Rules Glossary > Cover |
| 20 | 19 | -10.33 |  | Magic Items > Armor of Invulnerability |


*re-ranking* (query: `weight Bag of Holding`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.30 | yes | Magic Items > Bag of Holding |
| 2 | 3 | 1.27 | yes | Magic Items > Bag of Holding |
| 3 | 19 | 0.31 | yes | Equipment > Backpack (2 GP) |
| 4 | 8 | -0.86 | yes | Magic Items > Bag of Holding |
| 5 | 2 | -2.25 |  | Magic Items > Bag of Devouring |
| 6 | 18 | -2.60 |  | Magic Items > Handy Haversack |
| 7 | 9 | -3.65 |  | Magic Items > Bag of Devouring |
| 8 | 20 | -4.37 |  | Monsters A–Z > Traits |
| 9 | 4 | -4.93 |  | Magic Items > Bag of Beans |
| 10 | 6 | -7.38 |  | Magic Items > Bag of Devouring |
| 11 | 17 | -8.45 |  | Magic Items > Immovable Rod |
| 12 | 5 | -8.54 |  | Magic Items > Bag of Devouring |
| 13 | 11 | -9.05 |  | Playing the Game > Carrying Objects |
| 14 | 15 | -9.12 |  | Magic Items > Bag of Tricks |
| 15 | 13 | -9.60 |  | Magic Items > Bead of Force |
| 16 | 10 | -9.80 |  | Magic Items > Bag of Tricks |
| 17 | 14 | -9.81 |  | Magic Items > Bag of Beans |
| 18 | 7 | -9.95 |  | Magic Items > Bag of Tricks |
| 19 | 16 | -10.28 |  | Equipment > Block and Tackle (1 GP) |
| 20 | 12 | -10.29 |  | Equipment > Mounts and Cargo |


*re-ranking* (query: `volume Bag of Holding`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.54 | yes | Magic Items > Bag of Holding |
| 2 | 2 | 0.98 | yes | Magic Items > Bag of Holding |
| 3 | 7 | -0.69 | yes | Magic Items > Bag of Holding |
| 4 | 3 | -2.57 |  | Magic Items > Bag of Devouring |
| 5 | 4 | -2.61 |  | Magic Items > Handy Haversack |
| 6 | 5 | -2.76 |  | Magic Items > Bag of Devouring |
| 7 | 18 | -3.41 | yes | Equipment > Backpack (2 GP) |
| 8 | 14 | -5.24 |  | Monsters A–Z > Traits |
| 9 | 17 | -6.21 |  | Equipment > Sack (1 CP) |
| 10 | 16 | -6.70 |  | Equipment > Pouch (5 SP) |
| 11 | 20 | -9.02 |  | Equipment > Vial (1 GP) |
| 12 | 15 | -9.28 |  | Equipment > Bucket (5 CP) |
| 13 | 12 | -9.53 |  | Magic Items > Bag of Beans |
| 14 | 8 | -9.64 |  | Magic Items > Bag of Beans |
| 15 | 6 | -9.87 |  | Magic Items > Bag of Devouring |
| 16 | 10 | -9.93 |  | Magic Items > Bag of Tricks |
| 17 | 13 | -9.94 |  | Magic Items > Bag of Tricks |
| 18 | 9 | -10.08 |  | Magic Items > Bag of Tricks |
| 19 | 11 | -10.12 |  | Magic Items > Bag of Devouring |
| 20 | 19 | -11.24 |  | Playing the Game > Carrying Objects |


*re-ranking* (query: `weight of Bag of Holding`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 8.34 | yes | Magic Items > Bag of Holding |
| 2 | 18 | 1.04 | yes | Equipment > Backpack (2 GP) |
| 3 | 4 | 0.40 | yes | Magic Items > Bag of Holding |
| 4 | 17 | -1.35 |  | Magic Items > Handy Haversack |
| 5 | 10 | -1.84 | yes | Magic Items > Bag of Holding |
| 6 | 2 | -2.68 |  | Magic Items > Bag of Devouring |
| 7 | 20 | -2.92 |  | Equipment > Pouch (5 SP) |
| 8 | 3 | -2.94 |  | Magic Items > Bag of Beans |
| 9 | 8 | -2.97 |  | Magic Items > Bag of Devouring |
| 10 | 19 | -5.11 |  | Monsters A–Z > Traits |
| 11 | 11 | -6.25 |  | Rules Glossary > Carrying Capacity |
| 12 | 6 | -7.50 |  | Magic Items > Bag of Devouring |
| 13 | 15 | -8.08 |  | Equipment > Artisan's Tools |
| 14 | 12 | -8.76 |  | Magic Items > Bead of Force |
| 15 | 5 | -8.77 |  | Magic Items > Bag of Devouring |
| 16 | 14 | -8.83 |  | Magic Items > Bag of Beans |
| 17 | 9 | -9.44 |  | Magic Items > Bag of Tricks |
| 18 | 7 | -9.82 |  | Magic Items > Bag of Tricks |
| 19 | 13 | -10.49 |  | Equipment > Mounts and Cargo |
| 20 | 16 | -10.69 |  | Equipment > Block and Tackle (1 GP) |


*re-ranking* (query: `attunement Cloak of Protection`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.76 | yes | Magic Items > Cloak of Protection |
| 2 | 2 | 4.18 | yes | Magic Items > Cloak of Invisibility |
| 3 | 5 | 3.63 | yes | Magic Items > Cloak of Displacement |
| 4 | 7 | 2.89 |  | Magic Items > Cloak of the Bat |
| 5 | 3 | 2.81 |  | Magic Items > Cloak of Elvenkind |
| 6 | 9 | 2.75 |  | Magic Items > Cloak of Arachnida |
| 7 | 6 | 2.13 |  | Magic Items > Mantle of Spell Resistance |
| 8 | 11 | 1.96 |  | Magic Items > Scarab of Protection |
| 9 | 4 | 1.63 |  | Magic Items > Cloak of the Manta Ray |
| 10 | 17 | 1.62 |  | Magic Items > Brooch of Shielding |
| 11 | 8 | 1.59 |  | Magic Items > Ring of Protection |
| 12 | 15 | 1.13 |  | Equipment > Attunement |
| 13 | 14 | -0.01 |  | Equipment > No More Than Three Items |
| 14 | 10 | -0.11 |  | Magic Items > Wings of Flying |
| 15 | 19 | -1.16 |  | Magic Items > Bracers of Defense |
| 16 | 18 | -4.67 |  | Magic Items > Hat of Disguise |
| 17 | 20 | -5.33 |  | Magic Items > Robe of Scintillating Colors |
| 18 | 12 | -7.71 |  | Classes > Level 15: Smite of Protection |
| 19 | 13 | -8.45 |  | Magic Items > Cloak of the Bat |
| 20 | 16 | -10.53 |  | Classes > Level 18: Aura Expansion |

*retrieved sections:* Magic Items > Bag of Holding | Magic Items > Cloak of Protection | Magic Items > Cloak of Invisibility | Magic Items > Cloak of Displacement | Equipment > Backpack (2 GP)

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Magic Items > Bag of Holding]
If the bag is overloaded, pierced, or torn, it is destroyed, and its contents are scattered in the Astral Plane. If the bag is turned inside out, its contents spill forth unharmed, but the bag must be put right before it can be used again. The bag holds enough air for 10 minutes of breathing, divided by the number of breathing creatures inside.

---

[Magic Items > Bag of Holding]
Placing a _Bag of Holding_ inside an extradimensional space created by a _Handy Haversack_, _Portable Hole_, or similar item instantly destroys both items and opens a gate to the Astral Plane. The gate originates where the one item was placed inside the other. Any creature within a 10-foot-radius Sphere centered on the gate is sucked through it to a random location on the Astral Plane. The gate then closes. The gate is one-way and can't be reopened.

---

[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Cloak of Invisibility]
#### Cloak of Invisibility  
_Wondrous Item, Legendary (Requires Attunement)_  
This cloak has 3 charges and regains 1d3 expended charges daily at dawn. While wearing the cloak, you can take a Magic action to pull its hood over your
head and expend 1 charge to give yourself the Invisible condition for 1 hour. The effect ends early if you pull the hood down (no action required) or cease wearing the cloak.

---

[Magic Items > Cloak of Displacement]
#### Cloak of Displacement  
_Wondrous Item, Rare (Requires Attunement)_  
While you wear this cloak, it magically projects an illusion that makes you appear to be standing in a place near your actual location, causing any creature to have Disadvantage on attack rolls against you. If you take damage, the property ceases to function until the start of your next turn. This property is suppressed while your Speed is 0.

---

[Equipment > Backpack (2 GP)]
#### Backpack (2 GP)  
A Backpack holds up to 30 pounds within 1 cubic foot. It can also serve as a saddlebag.
```
</details>


---

## q5 (cross-file) Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points, what does the Owlbear's Multiattack consist of, and what is its CR?

**Gold facts (counterfactual data):** AC 17; 3d6; AC 15; 7d10 + 28; two Rend attacks; CR 3


### v0_closed_book  (0 chunks, 1 LLM call(s))

Certainly! Here’s a comparison between the Goblin Warrior and the Owlbear based on the 2024 SRD 5.2:

### Goblin Warrior:
- **Armor Class (AC):** 13 (leather armor)
- **Hit Points (HP):** 17 (2d8 + 6)

### Owlbear:
- **Armor Class (AC):** 15 (+3 natural armor)
- **Hit Points (HP):** 90 (10d10 + 30)

### Owlbear's Multiattack:
The Owlbear's multiattack consists of:
- **Claw Attack:** Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 3) slashing damage.
- **Bite Attack:** Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 3) piercing damage.

### Owlbear's Challenge Rating (CR):
- **Challenge Rating (CR):** 3

This comparison shows that the Owlbear has significantly higher AC and HP compared to the Goblin Warrior, along with a more powerful multiattack.

*facts found (judge): 2/6; missing: AC 17; 3d6; 7d10 + 28; two Rend attacks*


### v1_baseline  (3 chunks, 1 LLM call(s))

The provided context does not include the AC (Armor Class), Hit Points, or Challenge Rating (CR) for either the Goblin or the Owlbear. Therefore, these parts are missing from the information given. 

- **Owlbear's Multiattack:** The owlbear makes two Rend attacks.
- **Owlbear's CR:** Missing.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*

*retrieved sections:* Monsters A–Z > Actions | Animals > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The eagle makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 5 (1d4 + 3) Slashing damage plus 3 (1d6) Radiant damage.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The provided context does not include the AC (Armor Class) or Hit Points for either the Goblin Warrior or the Owlbear. Therefore, those details are missing.

The Owlbear's Multiattack consists of two Rend attacks.

The Owlbear's Challenge Rating (CR) is not mentioned in the given context.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 2 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 9 | -6.02 |  | Monsters A–Z > Goblin Warrior |
| 4 | 4 | -7.11 | yes | Monsters A–Z > Actions |
| 5 | 3 | -8.03 |  | Animals > Actions |
| 6 | 10 | -8.95 |  | Monsters A–Z > Actions |
| 7 | 7 | -9.05 |  | Monsters A–Z > Actions |
| 8 | 8 | -9.36 |  | Monsters A–Z > Actions |
| 9 | 6 | -9.93 |  | Animals > Giant Owl |
| 10 | 5 | -10.74 |  | Gameplay Toolbox > Powerful Creatures |

*retrieved sections:* Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The warrior makes two Greatsword or Heavy Crossbow attacks.  
**_Greatsword._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 10 (2d6 + 3) Slashing damage.  
**_Heavy Crossbow._** _Ranged Attack Roll:_ +3, range 100/400 ft. _Hit:_ 12 (2d10 + 1) Piercing damage.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The provided context does not include the Armor Class (AC) or Hit Points for either the Goblin Warrior or the Owlbear. Additionally, the context only describes the actions and attacks for these creatures but does not provide their hit points or AC.

The Owlbear's Multiattack consists of making two Rend attacks.

The Owlbear's CR (Challenge Rating) is not mentioned in the given context.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 2 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 9 | -6.02 |  | Monsters A–Z > Goblin Warrior |
| 4 | 4 | -7.11 | yes | Monsters A–Z > Actions |
| 5 | 3 | -8.03 | yes | Animals > Actions |
| 6 | 10 | -8.95 | yes | Monsters A–Z > Actions |
| 7 | 7 | -9.05 | yes | Monsters A–Z > Actions |
| 8 | 8 | -9.36 | yes | Monsters A–Z > Actions |
| 9 | 6 | -9.93 |  | Animals > Giant Owl |
| 10 | 5 | -10.74 |  | Gameplay Toolbox > Powerful Creatures |

*retrieved sections:* Monsters A–Z > Actions | Animals > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The warrior makes two Greatsword or Heavy Crossbow attacks.  
**_Greatsword._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 10 (2d6 + 3) Slashing damage.  
**_Heavy Crossbow._** _Ranged Attack Roll:_ +3, range 100/400 ft. _Hit:_ 12 (2d10 + 1) Piercing damage.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The eagle makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 5 (1d4 + 3) Slashing damage plus 3 (1d6) Radiant damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The scout makes two attacks, using Shortsword and Longbow in any combination.  
**_Shortsword._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage.  
**_Longbow._** _Ranged Attack Roll:_ +4, range 150/600 ft. _Hit:_ 6 (1d8 + 2) Piercing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The centaur makes two attacks, using Pike or Longbow in any combination.  
**_Pike._** _Melee Attack Roll:_ +6, reach 10 ft. _Hit:_ 9 (1d10 + 4) Piercing damage.  
**_Longbow._** _Ranged Attack Roll:_ +4, range 150/600 ft. _Hit:_ 6 (1d8 + 2) Piercing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The pseudodragon makes two Bite attacks.  
**_Bite._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 4 (1d4 + 2) Piercing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The tough makes two attacks, using Warhammer or Heavy Crossbow in any combination.  
**_Warhammer._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 12 (2d8 + 3) Bludgeoning damage. If the target is a Large or smaller creature, the tough pushes the target up to 10 feet straight away from itself.  
**_Heavy Crossbow._** _Ranged Attack Roll:_ +4, range 100/400 ft. _Hit:_ 13 (2d10 + 2) Piercing damage.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The provided context does not include the AC (Armor Class) or Hit Points for either the Goblin Warrior or the Owlbear. Therefore, those details are missing.

The Owlbear's Multiattack consists of two Rend attacks.

The Owlbear's Challenge Rating (CR) is not mentioned in the given context.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 2 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 8 | -6.02 |  | Monsters A–Z > Goblin Warrior |
| 4 | 4 | -7.11 | yes | Monsters A–Z > Actions |
| 5 | 3 | -8.03 |  | Animals > Actions |
| 6 | 9 | -8.95 |  | Monsters A–Z > Actions |
| 7 | 6 | -9.05 |  | Monsters A–Z > Actions |
| 8 | 7 | -9.36 |  | Monsters A–Z > Actions |
| 9 | 10 | -9.54 |  | Monsters > Multiattack |
| 10 | 5 | -9.93 |  | Animals > Giant Owl |

*retrieved sections:* Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The warrior makes two Greatsword or Heavy Crossbow attacks.  
**_Greatsword._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 10 (2d6 + 3) Slashing damage.  
**_Heavy Crossbow._** _Ranged Attack Roll:_ +3, range 100/400 ft. _Hit:_ 12 (2d10 + 1) Piercing damage.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The Goblin Warrior's AC and Hit Points are not provided in the given context. The Owlbear's Multiattack consists of two Rend attacks. The Owlbear's CR is 1.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 3 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 4 | -5.16 | yes | Monsters A–Z > Bugbear Warrior |
| 4 | 11 | -5.21 | yes | Monsters A–Z > Reactions |
| 5 | 2 | -5.56 | yes | Monsters A–Z > Goblin Warrior |
| 6 | 7 | -5.74 | yes | Rules Glossary > Stat Block |
| 7 | 14 | -6.02 |  | Monsters A–Z > Goblin Warrior |
| 8 | 24 | -6.45 | yes | Spells > Wall of Stone |
| 9 | 30 | -7.02 | yes | Monsters A–Z > Legendary Actions |
| 10 | 28 | -7.05 |  | Monsters A–Z > Traits |
| 11 | 6 | -7.11 |  | Monsters A–Z > Actions |
| 12 | 22 | -7.27 |  | Monsters > Hit Points |
| 13 | 15 | -7.47 |  | Monsters A–Z > Reactions |
| 14 | 13 | -7.71 |  | Monsters A–Z > Reactions |
| 15 | 5 | -8.03 |  | Animals > Actions |
| 16 | 16 | -8.95 |  | Monsters A–Z > Actions |
| 17 | 19 | -8.99 |  | Monsters A–Z > Actions |
| 18 | 29 | -8.99 |  | Monsters A–Z > Actions |
| 19 | 10 | -9.05 |  | Monsters A–Z > Actions |
| 20 | 27 | -9.07 |  | Animals > Giant Owl |

*retrieved sections:* Monsters A–Z > Actions | Monsters A–Z > Bugbear Warrior | Monsters A–Z > Reactions | Monsters A–Z > Goblin Warrior | Rules Glossary > Stat Block | Spells > Wall of Stone | Monsters A–Z > Legendary Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Bugbear Warrior]
**Languages** Common, Goblin<br>
**CR** 1 (XP 200; PB +2)

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Parry._** _Trigger:_ The warrior is hit by a melee attack roll while holding a weapon. _Response:_ The warrior adds 2 to its AC against that attack, possibly causing it to miss.

---

[Monsters A–Z > Goblin Warrior]
**Languages** Common, Goblin<br>
**CR** 1/4 (XP 50; PB +2)

---

[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Spells > Wall of Stone]
The wall is an object made of stone that can be damaged and thus breached. Each panel has AC 15 and 30 Hit Points per inch of thickness, and it has Immunity to Poison and Psychic damage. Reducing a panel to 0 Hit Points destroys it and might cause connected panels to collapse at the GM's discretion.  
If you maintain your Concentration on this spell for its full duration, the wall becomes permanent and can't be dispelled. Otherwise, the wall disappears when the spell ends.

---

[Monsters A–Z > Legendary Actions]
**_Shimmering Shield._** The unicorn targets itself or one creature it can see within 60 feet of itself. The target gains 10 (3d6) Temporary Hit Points, and its AC increases by 2 until the end of the unicorn's next turn. <br>
&emsp;The unicorn can't take this action again until the start of its next turn.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The Goblin Warrior has an AC of 17 and 10 HP (3d6). The Owlbear has an AC of 15 and 66 HP (7d10 + 28).

The Owlbear's Multiattack consists of making two Rend attacks.

The Owlbear's CR is not explicitly stated in the given context.

*facts found (judge): 5/6; missing: CR 3*


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 16, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 3 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 14 | -4.03 | yes | Monsters A–Z > Owlbear |
| 4 | 4 | -5.16 | yes | Monsters A–Z > Bugbear Warrior |
| 5 | 12 | -5.22 | yes | Monsters A–Z > Goblin Warrior |
| 6 | 2 | -5.56 | yes | Monsters A–Z > Goblin Warrior |
| 7 | 7 | -5.74 | yes | Rules Glossary > Stat Block |
| 8 | 11 | -6.02 | yes | Monsters A–Z > Goblin Warrior |
| 9 | 6 | -7.11 |  | Monsters A–Z > Actions |
| 10 | 13 | -7.60 |  | Monsters A–Z > Owlbear |
| 11 | 5 | -8.03 |  | Animals > Actions |
| 12 | 10 | -9.05 |  | Monsters A–Z > Actions |
| 13 | 8 | -9.93 |  | Animals > Giant Owl |
| 14 | 16 | -10.61 |  | Animals > Eagle |
| 15 | 15 | -10.91 |  | Animals > Eagle |
| 16 | 9 | -11.40 |  | Spells > Effects |

*retrieved sections:* Monsters A–Z > Actions | Monsters A–Z > Owlbear | Monsters A–Z > Bugbear Warrior | Monsters A–Z > Goblin Warrior | Rules Glossary > Stat Block

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Owlbear]
## Owlbear  
### Owlbear  
_Large Monstrosity, Unaligned_  
**AC** 15 **Initiative** +1 (11) <br>
**HP** 66 (7d10 + 28) <br>
**Speed** 40 ft., Climb 40 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>20</td>
<td>+5</td>
<td>+5</td>
<td><strong>DEX</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>

---

[Monsters A–Z > Bugbear Warrior]
**Languages** Common, Goblin<br>
**CR** 1 (XP 200; PB +2)

---

[Monsters A–Z > Goblin Warrior]
### Goblin Warrior  
_Small Fey (Goblinoid), Chaotic Neutral_  
**AC** 17 **Initiative** +2 (12) <br>
**HP** 10 (3d6) <br>
**Speed** 30 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>

---

[Monsters A–Z > Goblin Warrior]
**Languages** Common, Goblin<br>
**CR** 1/4 (XP 50; PB +2)

---

[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Monsters A–Z > Goblin Warrior]
<td>+2</td>
<td><strong>CON</strong></td>
<td>10</td>
<td>+0</td>
<td>+0</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>10</td>
<td>+0</td>
<td>+0</td>
<td><strong>WIS</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
<td><strong>CHA</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
</tr>
</tbody>
</table>  
**Skills** Stealth +6<br>
**Gear** Leather Armor, Scimitar, Shield, Shortbow<br>
**Senses** Darkvision 60 ft.; Passive Perception 9<br>
**Languages** Common, Goblin<br>
```
</details>


### v6_agentic  (7 chunks, 3 LLM call(s))

The Goblin Warrior has an AC of 17 and 10 HP. The Owlbear has an AC of 15 and 66 HP.

The Owlbear's Multiattack consists of two Rend attacks. 

The Owlbear's Challenge Rating (CR) is 3.

*facts found (judge): 4/6; missing: 3d6; 7d10 + 28*

*agentic sub-queries:* Goblin Warrior AC / Goblin Warrior HP / Owlbear Multiattack / Owlbear CR


*re-ranking* (query: `Goblin Warrior AC`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.29 | yes | Monsters A–Z > Goblin Warrior |
| 2 | 6 | 3.00 | yes | Monsters A–Z > Bugbear Warrior |
| 3 | 5 | 2.72 | yes | Monsters A–Z > Hobgoblin Warrior |
| 4 | 1 | 2.23 |  | Monsters A–Z > Goblin Warrior |
| 5 | 3 | 1.07 |  | Monsters A–Z > Goblin Warrior |
| 6 | 4 | 0.93 |  | Monsters A–Z > Bugbear Warrior |
| 7 | 7 | -2.89 |  | Monsters A–Z > Warrior Infantry |
| 8 | 15 | -3.30 |  | Monsters A–Z > Reactions |
| 9 | 10 | -3.33 |  | Monsters A–Z > Gnoll Warrior |
| 10 | 17 | -3.43 |  | Monsters A–Z > Reactions |
| 11 | 13 | -3.93 |  | Monsters A–Z > Sahuagin Warrior |
| 12 | 9 | -3.96 |  | Monsters A–Z > Goblin Minion |
| 13 | 16 | -4.09 |  | Magic Items > Deck of Illusions |
| 14 | 12 | -4.65 |  | Monsters A–Z > Bugbear Stalker |
| 15 | 11 | -4.66 |  | Monsters A–Z > Hobgoblin Captain |
| 16 | 8 | -4.83 |  | Monsters A–Z > Hobgoblin Warrior |
| 17 | 20 | -8.27 |  | Monsters A–Z > Bugbear Warrior |
| 18 | 18 | -8.81 |  | Classes > Level 10: Heroic Warrior |
| 19 | 19 | -9.03 |  | Monsters A–Z > Warrior Veteran |
| 20 | 14 | -10.46 |  | Monsters A–Z > Worg |


*re-ranking* (query: `Goblin Warrior HP`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.77 | yes | Monsters A–Z > Goblin Warrior |
| 2 | 6 | 3.33 | yes | Monsters A–Z > Bugbear Warrior |
| 3 | 5 | 3.03 | yes | Monsters A–Z > Hobgoblin Warrior |
| 4 | 1 | 1.52 |  | Monsters A–Z > Goblin Warrior |
| 5 | 3 | 0.90 |  | Monsters A–Z > Goblin Warrior |
| 6 | 4 | 0.32 |  | Monsters A–Z > Bugbear Warrior |
| 7 | 7 | -1.97 |  | Monsters A–Z > Warrior Infantry |
| 8 | 11 | -2.34 |  | Monsters A–Z > Kobold Warrior |
| 9 | 10 | -2.62 |  | Monsters A–Z > Gnoll Warrior |
| 10 | 19 | -3.20 |  | Monsters A–Z > Reactions |
| 11 | 8 | -3.66 |  | Monsters A–Z > Goblin Minion |
| 12 | 18 | -3.86 |  | Magic Items > Deck of Illusions |
| 13 | 9 | -4.49 |  | Monsters A–Z > Hobgoblin Warrior |
| 14 | 12 | -4.52 |  | Monsters A–Z > Bugbear Stalker |
| 15 | 13 | -4.74 |  | Monsters A–Z > Hobgoblin Captain |
| 16 | 20 | -7.96 |  | Classes > Level 10: Heroic Warrior |
| 17 | 16 | -8.27 |  | Monsters A–Z > Traits |
| 18 | 14 | -8.39 |  | Monsters A–Z > Bugbear Warrior |
| 19 | 17 | -8.47 |  | Monsters A–Z > Gnoll Warrior |
| 20 | 15 | -9.05 |  | Monsters A–Z > Warrior Veteran |


*re-ranking* (query: `Owlbear Multiattack`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.51 | yes | Monsters A–Z > Actions |
| 2 | 7 | 1.09 | yes | Monsters A–Z > Actions |
| 3 | 3 | 0.21 | yes | Monsters A–Z > Owlbear |
| 4 | 6 | -1.93 |  | Monsters A–Z > Actions |
| 5 | 4 | -2.86 | yes | Monsters A–Z > Owlbear |
| 6 | 8 | -3.65 |  | Animals > Actions |
| 7 | 2 | -3.69 |  | Monsters > Multiattack |
| 8 | 5 | -4.86 |  | Monsters A–Z > Actions |
| 9 | 13 | -5.01 |  | Monsters A–Z > Actions |
| 10 | 17 | -5.37 |  | Animals > Actions |
| 11 | 19 | -5.70 |  | Monsters A–Z > Actions |
| 12 | 20 | -5.80 |  | Monsters A–Z > Actions |
| 13 | 9 | -5.86 |  | Monsters A–Z > Actions |
| 14 | 18 | -5.86 |  | Monsters A–Z > Actions |
| 15 | 16 | -5.87 |  | Animals > Actions |
| 16 | 12 | -5.92 |  | Monsters A–Z > Actions |
| 17 | 14 | -6.24 |  | Animals > Actions |
| 18 | 15 | -6.34 |  | Monsters A–Z > Actions |
| 19 | 11 | -6.61 |  | Monsters A–Z > Actions |
| 20 | 10 | -7.07 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Owlbear CR`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.80 | yes | Monsters A–Z > Owlbear |
| 2 | 2 | 1.44 | yes | Monsters A–Z > Owlbear |
| 3 | 15 | -0.36 | yes | Monsters A–Z > Actions |
| 4 | 16 | -3.37 |  | Animals > Giant Owl |
| 5 | 8 | -5.22 |  | Monsters A–Z > Bugbear Warrior |
| 6 | 6 | -6.07 |  | Monsters A–Z > Bugbear Stalker |
| 7 | 17 | -6.91 |  | Animals > Owl |
| 8 | 14 | -7.04 |  | Animals > Giant Owl |
| 9 | 20 | -7.50 |  | Rules Glossary > Challenge Rating |
| 10 | 19 | -7.91 |  | Animals > Giant Owl |
| 11 | 18 | -9.61 |  | Gameplay Toolbox > CR 0 Creatures |
| 12 | 7 | -10.46 |  | Monsters A–Z > Hell Hound |
| 13 | 4 | -10.65 |  | Monsters A–Z > Chimera |
| 14 | 3 | -10.75 |  | Monsters A–Z > Pegasus |
| 15 | 11 | -10.80 |  | Monsters A–Z > Green Hag |
| 16 | 9 | -10.84 |  | Monsters A–Z > Salamander |
| 17 | 13 | -10.86 |  | Monsters A–Z > Hobgoblin Captain |
| 18 | 5 | -10.88 |  | Monsters A–Z > Gargoyle |
| 19 | 10 | -10.90 |  | Monsters A–Z > Sphinx of Wonder |
| 20 | 12 | -10.91 |  | Monsters A–Z > Centaur Trooper |


*re-ranking* (query: `Owlbear HP`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.07 | yes | Monsters A–Z > Owlbear |
| 2 | 8 | 1.15 | yes | Monsters A–Z > Actions |
| 3 | 2 | -1.22 | yes | Monsters A–Z > Owlbear |
| 4 | 7 | -2.00 |  | Animals > Owl |
| 5 | 9 | -2.02 |  | Animals > Giant Owl |
| 6 | 10 | -7.78 |  | Animals > Giant Owl |
| 7 | 13 | -8.87 |  | Animals > Raven |
| 8 | 11 | -9.07 |  | Magic Items > Avatar of Death |
| 9 | 19 | -9.37 |  | Monsters A–Z > Sphinx of Lore |
| 10 | 17 | -9.59 |  | Animals > Elephant |
| 11 | 5 | -9.66 |  | Monsters A–Z > Unicorn |
| 12 | 6 | -9.66 |  | Monsters A–Z > Lich |
| 13 | 12 | -9.70 |  | Magic Items > Instant Fortress |
| 14 | 3 | -9.76 |  | Monsters A–Z > Weretiger |
| 15 | 14 | -9.79 |  | Magic Items > Rope of Entanglement |
| 16 | 15 | -9.87 |  | Monsters A–Z > Axe Beak |
| 17 | 4 | -9.90 |  | Monsters A–Z > Rakshasa |
| 18 | 18 | -10.09 |  | Equipment > Net (1 GP) |
| 19 | 16 | -10.46 |  | Monsters A–Z > Actions |
| 20 | 20 | -10.87 |  | Monsters A–Z > Traits |


*re-ranking* (query: `Owlbear AC`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.05 | yes | Monsters A–Z > Owlbear |
| 2 | 4 | 0.63 | yes | Monsters A–Z > Actions |
| 3 | 2 | -0.85 | yes | Monsters A–Z > Owlbear |
| 4 | 5 | -2.33 |  | Animals > Owl |
| 5 | 3 | -2.47 |  | Animals > Giant Owl |
| 6 | 11 | -7.50 |  | Animals > Giant Owl |
| 7 | 8 | -8.00 |  | Rules Glossary > Armor Class |
| 8 | 9 | -8.30 |  | Animals > Giant Eagle |
| 9 | 6 | -8.57 |  | Animals > Giant Owl |
| 10 | 20 | -8.66 |  | Monsters > Armor Class |
| 11 | 12 | -9.00 |  | Equipment > Armor |
| 12 | 7 | -9.03 |  | Playing the Game > Armor Class |
| 13 | 14 | -9.05 |  | Animals > Swarm of Ravens |
| 14 | 19 | -9.19 |  | Animals > Raven |
| 15 | 16 | -9.84 |  | Animals > Elephant |
| 16 | 17 | -10.08 |  | Monsters A–Z > Axe Beak |
| 17 | 10 | -10.15 |  | Playing the Game > Armor Class |
| 18 | 15 | -10.68 |  | Monsters A–Z > Actions |
| 19 | 13 | -10.84 |  | Character Creation > Fill In Numbers |
| 20 | 18 | -11.01 |  | Playing the Game > Rolling 20 or 1 |

*retrieved sections:* Monsters A–Z > Goblin Warrior | Monsters A–Z > Bugbear Warrior | Monsters A–Z > Hobgoblin Warrior | Monsters A–Z > Actions | Monsters A–Z > Owlbear

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Goblin Warrior]
### Goblin Warrior  
_Small Fey (Goblinoid), Chaotic Neutral_  
**AC** 17 **Initiative** +2 (12) <br>
**HP** 10 (3d6) <br>
**Speed** 30 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>

---

[Monsters A–Z > Bugbear Warrior]
### Bugbear Warrior  
_Medium Fey (Goblinoid), Chaotic Evil_  
**AC** 14 **Initiative** +2 (12) <br>
**HP** 33 (6d8 + 6) <br>
**Speed** 30 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>DEX</strong></td>
<td>14</td>
<td>+2</td>
<td>+2</td>

---

[Monsters A–Z > Hobgoblin Warrior]
## Hobgoblins  
### Hobgoblin Warrior  
_Medium Fey (Goblinoid), Lawful Evil_  
**AC** 18 **Initiative** +3 (13) <br>
**HP** 11 (2d8 + 2) <br>
**Speed** 30 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>13</td>
<td>+1</td>
<td>+1</td>
<td><strong>DEX</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The werebear makes two attacks, using Handaxe or Rend in any combination. It can replace one attack with a Bite attack.

---

[Monsters A–Z > Owlbear]
## Owlbear  
### Owlbear  
_Large Monstrosity, Unaligned_  
**AC** 15 **Initiative** +1 (11) <br>
**HP** 66 (7d10 + 28) <br>
**Speed** 40 ft., Climb 40 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>20</td>
<td>+5</td>
<td>+5</td>
<td><strong>DEX</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>

---

[Monsters A–Z > Owlbear]
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CON</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 3 (XP 700; PB +2)
```
</details>


---

## q6 (multi-part) What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and how much raw material is needed to make Plate Armor?

**Gold facts (counterfactual data):** 16 in Chain Mail; 1,500 GP; 750 GP


### v0_closed_book  (0 chunks, 1 LLM call(s))

Wearing Chain Mail gives you an Armor Class (AC) of 16.

Plate Armor sells for 3,500 gp.

To make Plate Armor, you need 80 pounds of raw materials.

*facts found (judge): 1/3; missing: 1,500 GP; 750 GP*


### v1_baseline  (3 chunks, 1 LLM call(s))

The context provided does not specify the AC for Chain Mail or the price and raw materials for Plate Armor. Therefore, the following parts are missing:

- AC for wearing Chain Mail
- Price of Plate Armor
- Raw materials needed to make Plate Armor

*facts found (judge): 0/3; missing: 16 in Chain Mail; 1,500 GP; 750 GP*

*retrieved sections:* Equipment > Armor | Equipment > Raw Materials | Magic Items > Elven Chain

<details><summary>full retrieved context</summary>

```
[Equipment > Armor]
<td>—</td>
<td>—</td>
<td>12 lb.</td>
<td>10 GP</td>
</tr>
<tr>
<td>Chain Shirt</td>
<td>13 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Scale Mail</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>Disadvantage</td>
<td>45 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Breastplate</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>400 GP</td>
</tr>
<tr>
<td>Half Plate Armor</td>
<td>15 + Dex modifier (max 2)</td>

---

[Equipment > Raw Materials]
### Raw Materials  
To make an item, you need raw materials worth half its purchase cost (round down). For example, you need 750 GP of raw materials to make Plate Armor, which sells for 1,500 GP. The GM determines whether appropriate raw materials are available.

---

[Magic Items > Elven Chain]
#### Elven Chain  
_Armor (Chain Mail or Chain Shirt), Rare_  
You gain a +1 bonus to Armor Class while you wear this armor. You are considered trained with this armor even if you lack training with Medium or Heavy armor.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The AC when wearing Chain Mail is 16 (10 + your Dexterity modifier).

Plate Armor sells for 1,500 GP.

To make Plate Armor, you need 750 GP of raw materials (half of its purchase cost, rounded down).

*facts found (judge): 3/3; missing: none*


*re-ranking* (query: `What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and h`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 3.07 | yes | Equipment > Raw Materials |
| 2 | 4 | 0.74 | yes | Equipment > Armor |
| 3 | 7 | -3.33 | yes | Magic Items > Time and Cost |
| 4 | 3 | -3.37 |  | Magic Items > Elven Chain |
| 5 | 6 | -4.29 |  | Magic Items > Armor |
| 6 | 1 | -4.85 |  | Equipment > Armor |
| 7 | 5 | -6.69 |  | Equipment > Armor |
| 8 | 9 | -9.13 |  | Character Creation > Fill In Numbers |
| 9 | 10 | -9.94 |  | Equipment > Armor |
| 10 | 8 | -10.09 |  | Monsters > Armor Class |

*retrieved sections:* Equipment > Raw Materials | Equipment > Armor | Magic Items > Time and Cost

<details><summary>full retrieved context</summary>

```
[Equipment > Raw Materials]
### Raw Materials  
To make an item, you need raw materials worth half its purchase cost (round down). For example, you need 750 GP of raw materials to make Plate Armor, which sells for 1,500 GP. The GM determines whether appropriate raw materials are available.

---

[Equipment > Armor]
**Armor Class (AC).** The table's Armor Class column tells you what your base AC is when you wear a type of armor. For example, if you wear Leather Armor, your base AC is 11 plus your Dexterity modifier, whereas your AC is 16 in Chain Mail.  
**Strength.** If the table shows a Strength score in the Strength column for an armor type, that armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the listed score.

---

[Magic Items > Time and Cost]
If a magic item incorporates an item that has a purchase cost (such as a weapon or a suit of armor), you must also pay that entire cost or craft that item using the rules in "Equipment." For example, to make _+1 Armor_ (Plate Armor), you must pay 3,500 GP or pay 2,000 GP and craft the armor.  
**Magic Item Crafting Time and Cost**  
<table>
<thead>
<tr>
<th>Item Rarity</th>
<th>Time*</th>
<th>Cost*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>
<td>5 days</td>
<td>50 GP</td>
</tr>
<tr>
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The base AC for wearing Chain Mail is 13 + your Dexterity modifier (max 2). Plate Armor sells for 1,500 GP. To make Plate Armor, you need 750 GP of raw materials.

*facts found (judge): 2/3; missing: 16 in Chain Mail*


*re-ranking* (query: `What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and h`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 3.07 | yes | Equipment > Raw Materials |
| 2 | 4 | 0.74 | yes | Equipment > Armor |
| 3 | 7 | -3.33 | yes | Magic Items > Time and Cost |
| 4 | 3 | -3.37 | yes | Magic Items > Elven Chain |
| 5 | 6 | -4.29 | yes | Magic Items > Armor |
| 6 | 1 | -4.85 | yes | Equipment > Armor |
| 7 | 5 | -6.69 | yes | Equipment > Armor |
| 8 | 9 | -9.13 | yes | Character Creation > Fill In Numbers |
| 9 | 10 | -9.94 |  | Equipment > Armor |
| 10 | 8 | -10.09 |  | Monsters > Armor Class |

*retrieved sections:* Equipment > Raw Materials | Equipment > Armor | Magic Items > Time and Cost | Magic Items > Elven Chain | Magic Items > Armor | Character Creation > Fill In Numbers

<details><summary>full retrieved context</summary>

```
[Equipment > Raw Materials]
### Raw Materials  
To make an item, you need raw materials worth half its purchase cost (round down). For example, you need 750 GP of raw materials to make Plate Armor, which sells for 1,500 GP. The GM determines whether appropriate raw materials are available.

---

[Equipment > Armor]
**Armor Class (AC).** The table's Armor Class column tells you what your base AC is when you wear a type of armor. For example, if you wear Leather Armor, your base AC is 11 plus your Dexterity modifier, whereas your AC is 16 in Chain Mail.  
**Strength.** If the table shows a Strength score in the Strength column for an armor type, that armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the listed score.

---

[Magic Items > Time and Cost]
If a magic item incorporates an item that has a purchase cost (such as a weapon or a suit of armor), you must also pay that entire cost or craft that item using the rules in "Equipment." For example, to make _+1 Armor_ (Plate Armor), you must pay 3,500 GP or pay 2,000 GP and craft the armor.  
**Magic Item Crafting Time and Cost**  
<table>
<thead>
<tr>
<th>Item Rarity</th>
<th>Time*</th>
<th>Cost*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>
<td>5 days</td>
<td>50 GP</td>
</tr>
<tr>

---

[Magic Items > Elven Chain]
#### Elven Chain  
_Armor (Chain Mail or Chain Shirt), Rare_  
You gain a +1 bonus to Armor Class while you wear this armor. You are considered trained with this armor even if you lack training with Medium or Heavy armor.

---

[Magic Items > Armor]
### Armor  
An item in the Armor category is typically a magical version of armor from "Equipment." Unless an armor's description notes otherwise, the armor must be worn for its magic to function.  
Some suits of magic armor specify the type of armor they are, such as Chain Mail or Plate Armor. If no type is specified, choose the type or determine it randomly.

---

[Equipment > Armor]
<td>—</td>
<td>—</td>
<td>12 lb.</td>
<td>10 GP</td>
</tr>
<tr>
<td>Chain Shirt</td>
<td>13 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Scale Mail</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>Disadvantage</td>
<td>45 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Breastplate</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>400 GP</td>
</tr>
<tr>
<td>Half Plate Armor</td>
<td>15 + Dex modifier (max 2)</td>

---

[Equipment > Armor]
<td>17</td>
<td>Str 15</td>
<td>Disadvantage</td>
<td>60 lb.</td>
<td>200 GP</td>
</tr>
<tr>
<td>Plate Armor</td>
<td>18</td>
<td>Str 15</td>
<td>Disadvantage</td>
<td>65 lb.</td>
<td>1,500 GP</td>
</tr>
<tr>
<th colspan="6"><em>Shield (Utilize Action to Don or Doff)</em></th>
</tr>
<tr>
<td>Shield</td>
<td>+2</td>
<td>—</td>
<td>—</td>
<td>6 lb.</td>
<td>10 GP</td>
</tr>
</tbody>
</table>

---

[Character Creation > Fill In Numbers]
_Armor Class_. Without armor or a shield, your base Armor Class is 10 plus your Dexterity modifier. If your starting equipment includes armor or a Shield (or both), calculate your AC using the rules in "Equipment." A class feature might give you a different way to calculate your AC.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The AC when wearing Chain Mail is 16 (10 + your Dexterity modifier).

Plate Armor sells for 1,500 GP.

To make Plate Armor, you need 750 GP of raw materials (half of its purchase cost, rounded down).

*facts found (judge): 3/3; missing: none*


*re-ranking* (query: `What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and h`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 3.07 | yes | Equipment > Raw Materials |
| 2 | 4 | 0.74 | yes | Equipment > Armor |
| 3 | 7 | -3.33 | yes | Magic Items > Time and Cost |
| 4 | 3 | -3.37 |  | Magic Items > Elven Chain |
| 5 | 6 | -4.29 |  | Magic Items > Armor |
| 6 | 1 | -4.85 |  | Equipment > Armor |
| 7 | 5 | -6.69 |  | Equipment > Armor |
| 8 | 10 | -6.76 |  | Equipment > Armor |
| 9 | 9 | -9.94 |  | Equipment > Armor |
| 10 | 8 | -10.09 |  | Monsters > Armor Class |

*retrieved sections:* Equipment > Raw Materials | Equipment > Armor | Magic Items > Time and Cost

<details><summary>full retrieved context</summary>

```
[Equipment > Raw Materials]
### Raw Materials  
To make an item, you need raw materials worth half its purchase cost (round down). For example, you need 750 GP of raw materials to make Plate Armor, which sells for 1,500 GP. The GM determines whether appropriate raw materials are available.

---

[Equipment > Armor]
**Armor Class (AC).** The table's Armor Class column tells you what your base AC is when you wear a type of armor. For example, if you wear Leather Armor, your base AC is 11 plus your Dexterity modifier, whereas your AC is 16 in Chain Mail.  
**Strength.** If the table shows a Strength score in the Strength column for an armor type, that armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the listed score.

---

[Magic Items > Time and Cost]
If a magic item incorporates an item that has a purchase cost (such as a weapon or a suit of armor), you must also pay that entire cost or craft that item using the rules in "Equipment." For example, to make _+1 Armor_ (Plate Armor), you must pay 3,500 GP or pay 2,000 GP and craft the armor.  
**Magic Item Crafting Time and Cost**  
<table>
<thead>
<tr>
<th>Item Rarity</th>
<th>Time*</th>
<th>Cost*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>
<td>5 days</td>
<td>50 GP</td>
</tr>
<tr>
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

Wearing Chain Mail gives you a base AC of 13 plus your Dexterity modifier (max 2).

Plate Armor sells for 1,500 GP.

To make Plate Armor, you need 750 GP of raw materials (half its purchase cost, rounded down).

*facts found (judge): 2/3; missing: 16 in Chain Mail*


*re-ranking* (query: `What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and h`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.07 | yes | Equipment > Raw Materials |
| 2 | 2 | 0.74 | yes | Equipment > Armor |
| 3 | 8 | -3.33 | yes | Magic Items > Time and Cost |
| 4 | 3 | -3.37 | yes | Magic Items > Elven Chain |
| 5 | 15 | -3.86 | yes | Magic Items > Magic Item Values by Rarity |
| 6 | 4 | -4.29 | yes | Magic Items > Armor |
| 7 | 6 | -4.85 | yes | Equipment > Armor |
| 8 | 5 | -5.19 | yes | Magic Items > Dwarven Plate |
| 9 | 24 | -6.69 |  | Equipment > Armor |
| 10 | 7 | -6.76 |  | Equipment > Armor |
| 11 | 12 | -6.83 |  | Classes > Paladin |
| 12 | 11 | -7.14 |  | Magic Items > Plate Armor of Etherealness |
| 13 | 13 | -7.29 |  | Magic Items > Armor of Invulnerability |
| 14 | 19 | -7.47 |  | Classes > Fighter |
| 15 | 9 | -7.76 |  | Magic Items > Dragon Scale Mail |
| 16 | 29 | -8.42 |  | Rules Glossary > Armor Class |
| 17 | 20 | -8.44 |  | Equipment > Barding |
| 18 | 26 | -8.56 |  | Magic Items > Time and Cost |
| 19 | 25 | -8.99 |  | Equipment > Crafting Nonmagical Items |
| 20 | 18 | -9.66 |  | Magic Items > Bracers of Defense |

*retrieved sections:* Equipment > Raw Materials | Equipment > Armor | Magic Items > Time and Cost | Magic Items > Elven Chain | Magic Items > Magic Item Values by Rarity | Magic Items > Armor | Magic Items > Dwarven Plate

<details><summary>full retrieved context</summary>

```
[Equipment > Raw Materials]
### Raw Materials  
To make an item, you need raw materials worth half its purchase cost (round down). For example, you need 750 GP of raw materials to make Plate Armor, which sells for 1,500 GP. The GM determines whether appropriate raw materials are available.

---

[Equipment > Armor]
**Armor Class (AC).** The table's Armor Class column tells you what your base AC is when you wear a type of armor. For example, if you wear Leather Armor, your base AC is 11 plus your Dexterity modifier, whereas your AC is 16 in Chain Mail.  
**Strength.** If the table shows a Strength score in the Strength column for an armor type, that armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the listed score.

---

[Magic Items > Time and Cost]
If a magic item incorporates an item that has a purchase cost (such as a weapon or a suit of armor), you must also pay that entire cost or craft that item using the rules in "Equipment." For example, to make _+1 Armor_ (Plate Armor), you must pay 3,500 GP or pay 2,000 GP and craft the armor.  
**Magic Item Crafting Time and Cost**  
<table>
<thead>
<tr>
<th>Item Rarity</th>
<th>Time*</th>
<th>Cost*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>
<td>5 days</td>
<td>50 GP</td>
</tr>
<tr>

---

[Magic Items > Elven Chain]
#### Elven Chain  
_Armor (Chain Mail or Chain Shirt), Rare_  
You gain a +1 bonus to Armor Class while you wear this armor. You are considered trained with this armor even if you lack training with Medium or Heavy armor.

---

[Magic Items > Magic Item Values by Rarity]
If a magic item incorporates an item that has a purchase cost in "Equipment" (such as a weapon or a suit of armor), add that item's cost to the magic item's value. For example, _+1 Armor_ (Plate Armor)
has a value of 5,500 GP, which is the sum of a Rare magic item's value (4,000 GP) and the cost of Plate Armor (1,500 GP).  
**Magic Item Rarities and Values**  
<table>
<thead>
<tr>
<th>Rarity</th>
<th>Value*</th>
<th>Rarity</th>
<th>Value*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>

---

[Magic Items > Armor]
### Armor  
An item in the Armor category is typically a magical version of armor from "Equipment." Unless an armor's description notes otherwise, the armor must be worn for its magic to function.  
Some suits of magic armor specify the type of armor they are, such as Chain Mail or Plate Armor. If no type is specified, choose the type or determine it randomly.

---

[Equipment > Armor]
<td>—</td>
<td>—</td>
<td>12 lb.</td>
<td>10 GP</td>
</tr>
<tr>
<td>Chain Shirt</td>
<td>13 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Scale Mail</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>Disadvantage</td>
<td>45 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Breastplate</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>400 GP</td>
</tr>
<tr>
<td>Half Plate Armor</td>
<td>15 + Dex modifier (max 2)</td>

---

[Magic Items > Dwarven Plate]
#### Dwarven Plate  
_Armor (Half Plate Armor or Plate Armor), Very Rare_  
While wearing this armor, you gain a +2 bonus to Armor Class. In addition, if an effect moves you against your will along the ground, you can take a Reaction to reduce the distance you are moved by up to 10 feet.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The base AC for wearing Chain Mail is 13 + your Dexterity modifier (max 2). Plate Armor sells for 1,500 GP. To make Plate Armor, you need 750 GP of raw materials (half its purchase cost, rounded down).

*facts found (judge): 2/3; missing: 16 in Chain Mail*


*re-ranking* (query: `What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and h`): candidate pool of 16, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.07 | yes | Equipment > Raw Materials |
| 2 | 2 | 0.74 | yes | Equipment > Armor |
| 3 | 8 | -3.33 | yes | Magic Items > Time and Cost |
| 4 | 3 | -3.37 | yes | Magic Items > Elven Chain |
| 5 | 4 | -4.29 | yes | Magic Items > Armor |
| 6 | 6 | -4.85 | yes | Equipment > Armor |
| 7 | 5 | -5.19 | yes | Magic Items > Dwarven Plate |
| 8 | 11 | -6.69 | yes | Equipment > Armor |
| 9 | 7 | -6.76 |  | Equipment > Armor |
| 10 | 9 | -7.76 |  | Magic Items > Dragon Scale Mail |
| 11 | 10 | -9.80 |  | Magic Items > Dragon Scale Mail |
| 12 | 12 | -10.09 |  | Monsters > Armor Class |
| 13 | 15 | -10.46 |  | Character Origins > Equipment |
| 14 | 13 | -10.53 |  | Playing the Game > Armor Class |
| 15 | 16 | -11.39 |  | Rules Glossary > Reaction |
| 16 | 14 | -11.44 |  | Rules Glossary > Round Down |

*retrieved sections:* Equipment > Raw Materials | Equipment > Armor | Magic Items > Time and Cost | Magic Items > Elven Chain | Magic Items > Armor | Magic Items > Dwarven Plate

<details><summary>full retrieved context</summary>

```
[Equipment > Raw Materials]
### Raw Materials  
To make an item, you need raw materials worth half its purchase cost (round down). For example, you need 750 GP of raw materials to make Plate Armor, which sells for 1,500 GP. The GM determines whether appropriate raw materials are available.

---

[Equipment > Armor]
**Armor Class (AC).** The table's Armor Class column tells you what your base AC is when you wear a type of armor. For example, if you wear Leather Armor, your base AC is 11 plus your Dexterity modifier, whereas your AC is 16 in Chain Mail.  
**Strength.** If the table shows a Strength score in the Strength column for an armor type, that armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the listed score.

---

[Magic Items > Time and Cost]
If a magic item incorporates an item that has a purchase cost (such as a weapon or a suit of armor), you must also pay that entire cost or craft that item using the rules in "Equipment." For example, to make _+1 Armor_ (Plate Armor), you must pay 3,500 GP or pay 2,000 GP and craft the armor.  
**Magic Item Crafting Time and Cost**  
<table>
<thead>
<tr>
<th>Item Rarity</th>
<th>Time*</th>
<th>Cost*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>
<td>5 days</td>
<td>50 GP</td>
</tr>
<tr>

---

[Magic Items > Elven Chain]
#### Elven Chain  
_Armor (Chain Mail or Chain Shirt), Rare_  
You gain a +1 bonus to Armor Class while you wear this armor. You are considered trained with this armor even if you lack training with Medium or Heavy armor.

---

[Magic Items > Armor]
### Armor  
An item in the Armor category is typically a magical version of armor from "Equipment." Unless an armor's description notes otherwise, the armor must be worn for its magic to function.  
Some suits of magic armor specify the type of armor they are, such as Chain Mail or Plate Armor. If no type is specified, choose the type or determine it randomly.

---

[Equipment > Armor]
<td>—</td>
<td>—</td>
<td>12 lb.</td>
<td>10 GP</td>
</tr>
<tr>
<td>Chain Shirt</td>
<td>13 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Scale Mail</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>Disadvantage</td>
<td>45 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Breastplate</td>
<td>14 + Dex modifier (max 2)</td>
<td>—</td>
<td>—</td>
<td>20 lb.</td>
<td>400 GP</td>
</tr>
<tr>
<td>Half Plate Armor</td>
<td>15 + Dex modifier (max 2)</td>

---

[Magic Items > Dwarven Plate]
#### Dwarven Plate  
_Armor (Half Plate Armor or Plate Armor), Very Rare_  
While wearing this armor, you gain a +2 bonus to Armor Class. In addition, if an effect moves you against your will along the ground, you can take a Reaction to reduce the distance you are moved by up to 10 feet.

---

[Equipment > Armor]
<td>17</td>
<td>Str 15</td>
<td>Disadvantage</td>
<td>60 lb.</td>
<td>200 GP</td>
</tr>
<tr>
<td>Plate Armor</td>
<td>18</td>
<td>Str 15</td>
<td>Disadvantage</td>
<td>65 lb.</td>
<td>1,500 GP</td>
</tr>
<tr>
<th colspan="6"><em>Shield (Utilize Action to Don or Doff)</em></th>
</tr>
<tr>
<td>Shield</td>
<td>+2</td>
<td>—</td>
<td>—</td>
<td>6 lb.</td>
<td>10 GP</td>
</tr>
</tbody>
</table>
```
</details>


### v6_agentic  (9 chunks, 3 LLM call(s))

Wearing Chain Mail gives a base AC of 16 (10 + your Dexterity modifier).

Plate Armor sells for 1,500 GP.

To make Plate Armor, you need 750 GP of raw materials.

*facts found (judge): 3/3; missing: none*

*agentic sub-queries:* Chain Mail AC / Plate Armor price / Plate Armor material


*re-ranking* (query: `Chain Mail AC`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 3.85 | yes | Equipment > Armor |
| 2 | 1 | -0.78 | yes | Magic Items > Elven Chain |
| 3 | 11 | -3.65 | yes | Classes > Paladin |
| 4 | 7 | -4.73 |  | Magic Items > Armor |
| 5 | 4 | -5.08 |  | Equipment > Armor |
| 6 | 20 | -5.73 |  | Classes > Fighter |
| 7 | 5 | -6.30 |  | Equipment > Chain (5 GP) |
| 8 | 8 | -6.44 |  | Equipment > Armor |
| 9 | 6 | -7.34 |  | Equipment > Chain (5 GP) |
| 10 | 10 | -8.10 |  | Equipment > Chain (5 GP) |
| 11 | 19 | -9.77 |  | Spells > Chain Lightning |
| 12 | 12 | -10.08 |  | Magic Items > Dragon Scale Mail |
| 13 | 15 | -10.18 |  | Classes > Investment of the Chain Master |
| 14 | 16 | -10.44 |  | Equipment > Hunting Trap (5 GP) |
| 15 | 3 | -10.47 |  | Magic Items > Dragon Scale Mail |
| 16 | 17 | -10.54 |  | Classes > Pact of the Chain |
| 17 | 18 | -10.65 |  | Magic Items > Dragon Scale Mail |
| 18 | 14 | -10.93 |  | Playing the Game > Armor Class |
| 19 | 9 | -11.14 |  | Magic Items > Dragon Scale Mail |
| 20 | 13 | -11.19 |  | Playing the Game > Armor Class |


*re-ranking* (query: `Plate Armor price`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 4.58 | yes | Magic Items > Magic Item Values by Rarity |
| 2 | 7 | 3.38 | yes | Magic Items > Time and Cost |
| 3 | 2 | 2.88 | yes | Equipment > Raw Materials |
| 4 | 4 | -1.59 |  | Equipment > Armor |
| 5 | 1 | -1.71 | yes | Magic Items > Dwarven Plate |
| 6 | 5 | -3.50 | yes | Magic Items > Plate Armor of Etherealness |
| 7 | 6 | -3.89 | yes | Magic Items > Armor of Invulnerability |
| 8 | 9 | -4.61 |  | Equipment > Armor |
| 9 | 8 | -4.82 |  | Magic Items > Armor |
| 10 | 18 | -5.23 |  | Equipment > Barding |
| 11 | 10 | -6.41 |  | Equipment > Armor |
| 12 | 20 | -7.76 |  | Equipment > Armor |
| 13 | 13 | -9.79 |  | Magic Items > Armor, +1, +2, or +3 |
| 14 | 16 | -9.89 |  | Magic Items > Glamoured Studded Leather |
| 15 | 15 | -9.92 |  | Magic Items > Demon Armor |
| 16 | 12 | -10.25 |  | Magic Items > Mithral Armor |
| 17 | 19 | -10.49 |  | Magic Items > Adamantine Armor |
| 18 | 14 | -10.65 | yes | Magic Items > Elven Chain |
| 19 | 17 | -10.70 |  | Monsters A–Z > Hobgoblin Captain |
| 20 | 11 | -10.96 |  | Character Creation > Note Armor Training |


*re-ranking* (query: `Plate Armor material`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | 3.98 | yes | Equipment > Raw Materials |
| 2 | 1 | 2.76 | yes | Magic Items > Dwarven Plate |
| 3 | 5 | 1.99 | yes | Magic Items > Plate Armor of Etherealness |
| 4 | 4 | 1.83 | yes | Magic Items > Armor of Invulnerability |
| 5 | 2 | 0.38 |  | Magic Items > Armor |
| 6 | 15 | -0.31 | yes | Magic Items > Magic Item Values by Rarity |
| 7 | 3 | -0.52 |  | Equipment > Armor |
| 8 | 6 | -3.01 |  | Equipment > Armor |
| 9 | 8 | -4.15 |  | Magic Items > Mithral Armor |
| 10 | 11 | -5.57 |  | Magic Items > Adamantine Armor |
| 11 | 10 | -6.50 |  | Equipment > Armor |
| 12 | 12 | -6.65 |  | Magic Items > Glamoured Studded Leather |
| 13 | 13 | -7.01 |  | Magic Items > Armor, +1, +2, or +3 |
| 14 | 17 | -7.35 |  | Magic Items > Demon Armor |
| 15 | 19 | -7.37 |  | Magic Items > Armor of Vulnerability |
| 16 | 16 | -7.66 | yes | Equipment > Armor |
| 17 | 20 | -7.93 |  | Equipment > Armor |
| 18 | 14 | -9.01 | yes | Magic Items > Elven Chain |
| 19 | 18 | -9.05 |  | Equipment > Armor Training |
| 20 | 9 | -9.20 |  | Character Creation > Note Armor Training |


*re-ranking* (query: `plate armor price`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 4.58 | yes | Magic Items > Magic Item Values by Rarity |
| 2 | 7 | 3.38 | yes | Magic Items > Time and Cost |
| 3 | 2 | 2.88 | yes | Equipment > Raw Materials |
| 4 | 4 | -1.59 |  | Equipment > Armor |
| 5 | 1 | -1.71 | yes | Magic Items > Dwarven Plate |
| 6 | 5 | -3.50 | yes | Magic Items > Plate Armor of Etherealness |
| 7 | 6 | -3.89 | yes | Magic Items > Armor of Invulnerability |
| 8 | 9 | -4.61 |  | Equipment > Armor |
| 9 | 8 | -4.82 |  | Magic Items > Armor |
| 10 | 18 | -5.23 |  | Equipment > Barding |
| 11 | 10 | -6.41 |  | Equipment > Armor |
| 12 | 20 | -7.76 |  | Equipment > Armor |
| 13 | 13 | -9.79 |  | Magic Items > Armor, +1, +2, or +3 |
| 14 | 16 | -9.89 |  | Magic Items > Glamoured Studded Leather |
| 15 | 15 | -9.92 |  | Magic Items > Demon Armor |
| 16 | 12 | -10.25 |  | Magic Items > Mithral Armor |
| 17 | 19 | -10.49 |  | Magic Items > Adamantine Armor |
| 18 | 14 | -10.65 | yes | Magic Items > Elven Chain |
| 19 | 17 | -10.70 |  | Monsters A–Z > Hobgoblin Captain |
| 20 | 11 | -10.96 |  | Character Creation > Note Armor Training |


*re-ranking* (query: `plate armor raw materials`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.28 | yes | Equipment > Raw Materials |
| 2 | 2 | -1.83 | yes | Magic Items > Dwarven Plate |
| 3 | 5 | -2.09 | yes | Magic Items > Armor of Invulnerability |
| 4 | 6 | -2.84 | yes | Magic Items > Plate Armor of Etherealness |
| 5 | 4 | -3.06 |  | Equipment > Armor |
| 6 | 13 | -3.28 | yes | Magic Items > Magic Item Values by Rarity |
| 7 | 3 | -3.81 |  | Magic Items > Armor |
| 8 | 9 | -4.76 | yes | Magic Items > Time and Cost |
| 9 | 7 | -5.13 |  | Equipment > Armor |
| 10 | 8 | -7.45 |  | Magic Items > Mithral Armor |
| 11 | 14 | -8.24 |  | Magic Items > Adamantine Armor |
| 12 | 12 | -8.61 |  | Magic Items > Time and Cost |
| 13 | 11 | -9.06 |  | Equipment > Armor |
| 14 | 15 | -9.84 |  | Magic Items > Glamoured Studded Leather |
| 15 | 18 | -9.95 |  | Magic Items > Armor, +1, +2, or +3 |
| 16 | 19 | -10.12 |  | Magic Items > Armor of Vulnerability |
| 17 | 20 | -10.54 | yes | Equipment > Armor |
| 18 | 17 | -10.57 |  | Equipment > Crafting Nonmagical Items |
| 19 | 16 | -10.92 | yes | Magic Items > Elven Chain |
| 20 | 10 | -10.96 |  | Character Creation > Note Armor Training |

*retrieved sections:* Equipment > Armor | Magic Items > Elven Chain | Classes > Paladin | Magic Items > Magic Item Values by Rarity | Magic Items > Time and Cost | Equipment > Raw Materials | Magic Items > Dwarven Plate | Magic Items > Plate Armor of Etherealness | Magic Items > Armor of Invulnerability

<details><summary>full retrieved context</summary>

```
[Equipment > Armor]
**Armor Class (AC).** The table's Armor Class column tells you what your base AC is when you wear a type of armor. For example, if you wear Leather Armor, your base AC is 11 plus your Dexterity modifier, whereas your AC is 16 in Chain Mail.  
**Strength.** If the table shows a Strength score in the Strength column for an armor type, that armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the listed score.

---

[Magic Items > Elven Chain]
#### Elven Chain  
_Armor (Chain Mail or Chain Shirt), Rare_  
You gain a +1 bonus to Armor Class while you wear this armor. You are considered trained with this armor even if you lack training with Medium or Heavy armor.

---

[Classes > Paladin]
</tr>
<tr>
<td>Armor Training</td>
<td>Light, Medium, and Heavy armor and Shields</td>
</tr>
<tr>
<td>Starting Equipment</td>
<td>Choose A or B: (A) Chain Mail, Shield, Longsword, 6 Javelins, Holy Symbol, Priest's Pack, and 9 GP; or (B) 150 GP</td>
</tr>
</tbody>
</table>

---

[Magic Items > Magic Item Values by Rarity]
If a magic item incorporates an item that has a purchase cost in "Equipment" (such as a weapon or a suit of armor), add that item's cost to the magic item's value. For example, _+1 Armor_ (Plate Armor)
has a value of 5,500 GP, which is the sum of a Rare magic item's value (4,000 GP) and the cost of Plate Armor (1,500 GP).  
**Magic Item Rarities and Values**  
<table>
<thead>
<tr>
<th>Rarity</th>
<th>Value*</th>
<th>Rarity</th>
<th>Value*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>

---

[Magic Items > Time and Cost]
If a magic item incorporates an item that has a purchase cost (such as a weapon or a suit of armor), you must also pay that entire cost or craft that item using the rules in "Equipment." For example, to make _+1 Armor_ (Plate Armor), you must pay 3,500 GP or pay 2,000 GP and craft the armor.  
**Magic Item Crafting Time and Cost**  
<table>
<thead>
<tr>
<th>Item Rarity</th>
<th>Time*</th>
<th>Cost*</th>
</tr>
</thead>
<tbody>
<tr>
<td>Common</td>
<td>5 days</td>
<td>50 GP</td>
</tr>
<tr>

---

[Equipment > Raw Materials]
### Raw Materials  
To make an item, you need raw materials worth half its purchase cost (round down). For example, you need 750 GP of raw materials to make Plate Armor, which sells for 1,500 GP. The GM determines whether appropriate raw materials are available.

---

[Magic Items > Dwarven Plate]
#### Dwarven Plate  
_Armor (Half Plate Armor or Plate Armor), Very Rare_  
While wearing this armor, you gain a +2 bonus to Armor Class. In addition, if an effect moves you against your will along the ground, you can take a Reaction to reduce the distance you are moved by up to 10 feet.

---

[Magic Items > Plate Armor of Etherealness]
#### Plate Armor of Etherealness  
_Armor (Half Plate Armor or Plate Armor), Legendary (Requires Attunement)_  
While you're wearing this armor, you can take a Magic action and use a command word to gain the effect of the _Etherealness_ spell. The spell ends immediately if you remove the armor or take a Magic action to repeat the command word. This property of the armor can't be used again until the next dawn.

---

[Magic Items > Armor of Invulnerability]
#### Armor of Invulnerability  
_Armor (Plate Armor), Legendary (Requires Attunement)_  
You have Resistance to Bludgeoning, Piercing, and Slashing damage while you wear this armor.  
**_Metal Shell._** You can take a Magic action to give yourself Immunity to Bludgeoning, Piercing, and Slashing damage for 10 minutes or until you are no longer wearing the armor. Once this property is used, it can't be used again until the next dawn.
```
</details>


---

## q7 (multi-part) What are the effects of the Grappled condition on Speed and on attacks, and what are the effects of the Prone condition on movement and on attack rolls against you?

**Gold facts (counterfactual data):** Speed is 0; other than the grappler; crawl; half your Speed; within 5 feet


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Grappled Condition:**
- **Speed:** A creature that is grappled has its speed reduced to 0.
- **Attacks:** When making an attack against a grappled creature, you have advantage on the attack roll.

**Prone Condition:**
- **Movement:** A prone creature's speed becomes 0, and it can only move by crawling.
- **Attack Rolls Against You:** When a creature makes an attack roll against a prone target, the attacker has disadvantage on the attack roll.

*facts found (judge): 2/5; missing: other than the grappler; half your Speed; within 5 feet*


### v1_baseline  (3 chunks, 1 LLM call(s))

The Grappled condition affects Speed and attacks as follows:

_Speed 0._ Your Speed is 0 and can't increase.
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.

The Prone condition affects movement and attack rolls against you as follows:

_Attacks Affected._ You have Disadvantage on attack rolls. An attack roll against you has Advantage if the attacker is within 5 feet of you. Otherwise, that attack roll has Disadvantage.

*facts found (judge): 3/5; missing: crawl; half your Speed*

*retrieved sections:* Rules Glossary > Grappled [Condition] | Feats > Grappler | Rules Glossary > Prone [Condition]

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Feats > Grappler]
_Attack Advantage._ You have Advantage on attack rolls against a creature Grappled by you.  
_Fast Wrestler._ You don't have to spend extra movement to move a creature Grappled by you if the creature is your size or smaller.

---

[Rules Glossary > Prone [Condition]]
_Attacks Affected._ You have Disadvantage on attack rolls. An attack roll against you has Advantage if the attacker is within 5 feet of you. Otherwise, that attack roll has Disadvantage.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The Grappled condition affects Speed by setting it to 0 and preventing it from increasing. It also gives disadvantage on attack rolls against any target other than the grappler.

The Prone condition restricts movement to either crawling or spending half your Speed (rounded down) to right yourself, ending the condition. Additionally, it makes attack rolls against you have advantage.

*facts found (judge): 4/5; missing: within 5 feet*


*re-ranking* (query: `What are the effects of the Grappled condition on Speed and on attacks, and what`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.84 | yes | Rules Glossary > Grappled [Condition] |
| 2 | 4 | 3.42 | yes | Rules Glossary > Unconscious [Condition] |
| 3 | 10 | 1.59 | yes | Rules Glossary > Prone [Condition] |
| 4 | 5 | 1.18 |  | Rules Glossary > Restrained [Condition] |
| 5 | 8 | -0.53 |  | Animals > Actions |
| 6 | 3 | -0.72 |  | Rules Glossary > Prone [Condition] |
| 7 | 7 | -1.34 |  | Animals > Actions |
| 8 | 2 | -1.91 |  | Feats > Grappler |
| 9 | 9 | -2.15 |  | Monsters A–Z > Actions |
| 10 | 6 | -5.21 |  | Feats > Grappler |

*retrieved sections:* Rules Glossary > Grappled [Condition] | Rules Glossary > Unconscious [Condition] | Rules Glossary > Prone [Condition]

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Rules Glossary > Unconscious [Condition]]
#### Unconscious [Condition]  
While you have the Unconscious condition, you experience the following effects.  
_Inert._ You have the Incapacitated and Prone conditions, and you drop whatever you're holding. When this condition ends, you remain Prone.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.

---

[Rules Glossary > Prone [Condition]]
#### Prone [Condition]  
While you have the Prone condition, you experience the following effects.  
_Restricted Movement._ Your only movement options are to crawl or to spend an amount of movement equal to half your Speed (round down) to right yourself and thereby end the condition. If your Speed is 0, you can't right yourself.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The Grappled condition sets your Speed to 0 and grants disadvantage on attack rolls against any target other than the grappler.

The Prone condition restricts movement to crawling or spending half your Speed (rounded down) to right yourself, and it imposes disadvantage on attack rolls against you. Additionally, if the attacker is within 5 feet, their attack rolls against you have advantage.

*facts found (judge): 5/5; missing: none*


*re-ranking* (query: `What are the effects of the Grappled condition on Speed and on attacks, and what`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.84 | yes | Rules Glossary > Grappled [Condition] |
| 2 | 4 | 3.42 | yes | Rules Glossary > Unconscious [Condition] |
| 3 | 10 | 1.59 | yes | Rules Glossary > Prone [Condition] |
| 4 | 5 | 1.18 | yes | Rules Glossary > Restrained [Condition] |
| 5 | 8 | -0.53 | yes | Animals > Actions |
| 6 | 3 | -0.72 | yes | Rules Glossary > Prone [Condition] |
| 7 | 7 | -1.34 | yes | Animals > Actions |
| 8 | 2 | -1.91 | yes | Feats > Grappler |
| 9 | 9 | -2.15 |  | Monsters A–Z > Actions |
| 10 | 6 | -5.21 |  | Feats > Grappler |

*retrieved sections:* Rules Glossary > Grappled [Condition] | Rules Glossary > Unconscious [Condition] | Rules Glossary > Prone [Condition] | Rules Glossary > Restrained [Condition] | Animals > Actions | Feats > Grappler

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Rules Glossary > Unconscious [Condition]]
#### Unconscious [Condition]  
While you have the Unconscious condition, you experience the following effects.  
_Inert._ You have the Incapacitated and Prone conditions, and you drop whatever you're holding. When this condition ends, you remain Prone.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.

---

[Rules Glossary > Prone [Condition]]
#### Prone [Condition]  
While you have the Prone condition, you experience the following effects.  
_Restricted Movement._ Your only movement options are to crawl or to spend an amount of movement equal to half your Speed (round down) to right yourself and thereby end the condition. If your Speed is 0, you can't right yourself.

---

[Rules Glossary > Restrained [Condition]]
#### Restrained [Condition]  
While you have the Restrained condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage, and your attack rolls have Disadvantage.  
_Saving Throws Affected._ You have Disadvantage on Dexterity saving throws.

---

[Animals > Actions]
### Actions  
<hr>  
**_Bite._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 6 (1d8 + 2) Piercing damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 12). While Grappled, the target has the Restrained condition.

---

[Rules Glossary > Prone [Condition]]
_Attacks Affected._ You have Disadvantage on attack rolls. An attack roll against you has Advantage if the attacker is within 5 feet of you. Otherwise, that attack roll has Disadvantage.

---

[Animals > Actions]
**_Tail._** _Melee Attack Roll:_ +8, reach 10 ft. _Hit:_ 18 (3d8 + 5) Bludgeoning damage. If the target is a Large or smaller creature, it has the Prone condition.

---

[Feats > Grappler]
_Attack Advantage._ You have Advantage on attack rolls against a creature Grappled by you.  
_Fast Wrestler._ You don't have to spend extra movement to move a creature Grappled by you if the creature is your size or smaller.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The Grappled condition affects Speed by setting it to 0 and preventing it from increasing. It also gives disadvantage on attack rolls against any target other than the grappler.

The Prone condition restricts movement to either crawling or spending half your Speed (rounded down) to right yourself, ending the condition. Additionally, it makes attack rolls against you have advantage.

*facts found (judge): 4/5; missing: within 5 feet*


*re-ranking* (query: `What are the effects of the Grappled condition on Speed and on attacks, and what`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.84 | yes | Rules Glossary > Grappled [Condition] |
| 2 | 4 | 3.42 | yes | Rules Glossary > Unconscious [Condition] |
| 3 | 10 | 1.59 | yes | Rules Glossary > Prone [Condition] |
| 4 | 5 | 1.18 |  | Rules Glossary > Restrained [Condition] |
| 5 | 8 | -0.53 |  | Animals > Actions |
| 6 | 3 | -0.72 |  | Rules Glossary > Prone [Condition] |
| 7 | 7 | -1.34 |  | Animals > Actions |
| 8 | 2 | -1.91 |  | Feats > Grappler |
| 9 | 9 | -2.15 |  | Monsters A–Z > Actions |
| 10 | 6 | -5.21 |  | Feats > Grappler |

*retrieved sections:* Rules Glossary > Grappled [Condition] | Rules Glossary > Unconscious [Condition] | Rules Glossary > Prone [Condition]

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Rules Glossary > Unconscious [Condition]]
#### Unconscious [Condition]  
While you have the Unconscious condition, you experience the following effects.  
_Inert._ You have the Incapacitated and Prone conditions, and you drop whatever you're holding. When this condition ends, you remain Prone.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.

---

[Rules Glossary > Prone [Condition]]
#### Prone [Condition]  
While you have the Prone condition, you experience the following effects.  
_Restricted Movement._ Your only movement options are to crawl or to spend an amount of movement equal to half your Speed (round down) to right yourself and thereby end the condition. If your Speed is 0, you can't right yourself.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The Grappled condition affects Speed by setting it to 0 and preventing it from increasing. It also gives disadvantage on attack rolls against any target other than the grappler.

The Prone condition restricts movement, allowing only crawling or using half your Speed (rounded down) to right yourself and end the condition. It also makes all attack rolls against you have advantage.

*facts found (judge): 4/5; missing: within 5 feet*


*re-ranking* (query: `What are the effects of the Grappled condition on Speed and on attacks, and what`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.84 | yes | Rules Glossary > Grappled [Condition] |
| 2 | 3 | 3.42 | yes | Rules Glossary > Unconscious [Condition] |
| 3 | 6 | 1.59 | yes | Rules Glossary > Prone [Condition] |
| 4 | 2 | 1.18 | yes | Rules Glossary > Restrained [Condition] |
| 5 | 7 | 0.61 | yes | Rules Glossary > Paralyzed [Condition] |
| 6 | 18 | -0.26 | yes | Animals > Actions |
| 7 | 15 | -0.53 | yes | Animals > Actions |
| 8 | 8 | -0.56 | yes | Rules Glossary > Petrified [Condition] |
| 9 | 4 | -0.72 |  | Rules Glossary > Prone [Condition] |
| 10 | 30 | -0.87 |  | Animals > Actions |
| 11 | 21 | -0.92 |  | Monsters A–Z > Actions |
| 12 | 20 | -1.15 |  | Monsters A–Z > Actions |
| 13 | 14 | -1.34 |  | Animals > Actions |
| 14 | 16 | -1.60 |  | Rules Glossary > Stunned [Condition] |
| 15 | 10 | -1.88 |  | Rules Glossary > Frightened [Condition] |
| 16 | 5 | -1.91 |  | Feats > Grappler |
| 17 | 28 | -1.97 |  | Animals > Actions |
| 18 | 13 | -2.06 |  | Rules Glossary > Blinded [Condition] |
| 19 | 17 | -2.15 |  | Monsters A–Z > Actions |
| 20 | 26 | -2.81 |  | Playing the Game > Actions |

*retrieved sections:* Rules Glossary > Grappled [Condition] | Rules Glossary > Unconscious [Condition] | Rules Glossary > Prone [Condition] | Rules Glossary > Restrained [Condition] | Rules Glossary > Paralyzed [Condition] | Animals > Actions | Rules Glossary > Petrified [Condition]

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Rules Glossary > Unconscious [Condition]]
#### Unconscious [Condition]  
While you have the Unconscious condition, you experience the following effects.  
_Inert._ You have the Incapacitated and Prone conditions, and you drop whatever you're holding. When this condition ends, you remain Prone.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.

---

[Rules Glossary > Prone [Condition]]
#### Prone [Condition]  
While you have the Prone condition, you experience the following effects.  
_Restricted Movement._ Your only movement options are to crawl or to spend an amount of movement equal to half your Speed (round down) to right yourself and thereby end the condition. If your Speed is 0, you can't right yourself.

---

[Rules Glossary > Restrained [Condition]]
#### Restrained [Condition]  
While you have the Restrained condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage, and your attack rolls have Disadvantage.  
_Saving Throws Affected._ You have Disadvantage on Dexterity saving throws.

---

[Rules Glossary > Paralyzed [Condition]]
#### Paralyzed [Condition]  
While you have the Paralyzed condition, you experience the following effects.  
_Incapacitated._ You have the Incapacitated condition.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Automatic Critical Hits._ Any attack roll that hits you is a Critical Hit if the attacker is within 5 feet of you.

---

[Animals > Actions]
**_Swallow._** The frog swallows a Small or smaller target it is grappling. While swallowed, the target isn't Grappled but has the Blinded and Restrained conditions, and it has Total Cover against attacks and other effects outside the frog. While swallowing the target, the frog can't use Bite, and if the frog dies, the swallowed target is no longer Restrained and can escape from the corpse using 5 feet of movement, exiting with the Prone condition. <br>

---

[Animals > Actions]
### Actions  
<hr>  
**_Bite._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 6 (1d8 + 2) Piercing damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 12). While Grappled, the target has the Restrained condition.

---

[Rules Glossary > Petrified [Condition]]
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.  
_Resist Damage._ You have Resistance to all damage.  
_Poison Immunity._ You have Immunity to the Poisoned condition.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The Grappled condition sets your Speed to 0 and gives disadvantage on attack rolls against any target other than the grappler.

The Prone condition restricts your movement options to crawling or spending half your Speed (rounded down) to right yourself, and it makes your Speed 0. Additionally, attack rolls against you have advantage.

*facts found (judge): 4/5; missing: within 5 feet*


*re-ranking* (query: `What are the effects of the Grappled condition on Speed and on attacks, and what`): candidate pool of 19, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.84 | yes | Rules Glossary > Grappled [Condition] |
| 2 | 3 | 3.42 | yes | Rules Glossary > Unconscious [Condition] |
| 3 | 6 | 1.59 | yes | Rules Glossary > Prone [Condition] |
| 4 | 2 | 1.18 | yes | Rules Glossary > Restrained [Condition] |
| 5 | 7 | 0.61 | yes | Rules Glossary > Paralyzed [Condition] |
| 6 | 8 | -0.56 | yes | Rules Glossary > Petrified [Condition] |
| 7 | 4 | -0.72 | yes | Rules Glossary > Prone [Condition] |
| 8 | 10 | -1.88 | yes | Rules Glossary > Frightened [Condition] |
| 9 | 5 | -1.91 |  | Feats > Grappler |
| 10 | 9 | -3.74 |  | Playing the Game > Dropping Prone |
| 11 | 16 | -5.21 |  | Feats > Grappler |
| 12 | 17 | -6.84 |  | Rules Glossary > Incapacitated [Condition] |
| 13 | 11 | -7.65 |  | Playing the Game > Attack Rolls |
| 14 | 12 | -8.51 |  | Spells > Attack Rolls |
| 15 | 13 | -10.58 |  | Rules Glossary > Disadvantage |
| 16 | 15 | -10.94 |  | Playing the Game > Saving Throws |
| 17 | 14 | -11.08 |  | Spells > Saving Throws |
| 18 | 18 | -11.09 |  | Rules Glossary > Size |
| 19 | 19 | -11.23 |  | Monsters > Size |

*retrieved sections:* Rules Glossary > Grappled [Condition] | Rules Glossary > Unconscious [Condition] | Rules Glossary > Prone [Condition] | Rules Glossary > Restrained [Condition] | Rules Glossary > Paralyzed [Condition] | Rules Glossary > Petrified [Condition] | Rules Glossary > Frightened [Condition]

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Rules Glossary > Unconscious [Condition]]
#### Unconscious [Condition]  
While you have the Unconscious condition, you experience the following effects.  
_Inert._ You have the Incapacitated and Prone conditions, and you drop whatever you're holding. When this condition ends, you remain Prone.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.

---

[Rules Glossary > Prone [Condition]]
#### Prone [Condition]  
While you have the Prone condition, you experience the following effects.  
_Restricted Movement._ Your only movement options are to crawl or to spend an amount of movement equal to half your Speed (round down) to right yourself and thereby end the condition. If your Speed is 0, you can't right yourself.

---

[Rules Glossary > Restrained [Condition]]
#### Restrained [Condition]  
While you have the Restrained condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage, and your attack rolls have Disadvantage.  
_Saving Throws Affected._ You have Disadvantage on Dexterity saving throws.

---

[Rules Glossary > Paralyzed [Condition]]
#### Paralyzed [Condition]  
While you have the Paralyzed condition, you experience the following effects.  
_Incapacitated._ You have the Incapacitated condition.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Automatic Critical Hits._ Any attack roll that hits you is a Critical Hit if the attacker is within 5 feet of you.

---

[Rules Glossary > Petrified [Condition]]
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ Attack rolls against you have Advantage.  
_Saving Throws Affected._ You automatically fail Strength and Dexterity saving throws.  
_Resist Damage._ You have Resistance to all damage.  
_Poison Immunity._ You have Immunity to the Poisoned condition.

---

[Rules Glossary > Prone [Condition]]
_Attacks Affected._ You have Disadvantage on attack rolls. An attack roll against you has Advantage if the attacker is within 5 feet of you. Otherwise, that attack roll has Disadvantage.

---

[Rules Glossary > Frightened [Condition]]
#### Frightened [Condition]  
While you have the Frightened condition, you experience the following effects.  
_Ability Checks and Attacks Affected._ You have Disadvantage on ability checks and attack rolls while the source of fear is within line of sight.  
_Can't Approach._ You can't willingly move closer to the source of fear.
```
</details>


### v6_agentic  (16 chunks, 3 LLM call(s))

The Grappled condition affects Speed and attacks as follows:

- **Speed**: Your Speed is 0 and can't increase.
- **Attacks**: You have Disadvantage on attack rolls against any target other than the grappler.

The Prone condition affects movement and attack rolls against you as follows:

- **Movement**: While Prone, your only movement options are to crawl or to spend an amount of movement equal to half your Speed (round down) to right yourself and thereby end the condition. If your Speed is 0, you can't right yourself.
- **Attack Rolls Against You**: There is no specific mention of how the Prone condition affects attack rolls against you.

*facts found (judge): 4/5; missing: within 5 feet*

*agentic sub-queries:* Grappled / Speed / attacks / Prone / movement / attack rolls


*re-ranking* (query: `Grappled`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.39 | yes | Rules Glossary > Grappling |
| 2 | 4 | 5.51 | yes | Rules Glossary > Grappling |
| 3 | 2 | 5.08 | yes | Rules Glossary > Grappled [Condition] |
| 4 | 6 | 3.63 |  | Animals > Actions |
| 5 | 3 | 3.58 |  | Animals > Actions |
| 6 | 5 | 3.58 |  | Feats > Grappler |
| 7 | 19 | 3.42 |  | Monsters A–Z > Bonus Actions |
| 8 | 16 | 3.03 |  | Monsters A–Z > Bonus Actions |
| 9 | 7 | 3.03 |  | Animals > Actions |
| 10 | 14 | 2.92 |  | Animals > Actions |
| 11 | 9 | 2.91 |  | Monsters A–Z > Actions |
| 12 | 20 | 2.71 |  | Monsters A–Z > Actions |
| 13 | 15 | 2.71 |  | Monsters A–Z > Actions |
| 14 | 8 | 2.37 |  | Monsters A–Z > Bonus Actions |
| 15 | 12 | 2.27 |  | Monsters A–Z > Actions |
| 16 | 11 | 1.94 |  | Monsters A–Z > Actions |
| 17 | 17 | 1.86 |  | Monsters A–Z > Actions |
| 18 | 18 | 1.63 |  | Monsters A–Z > Actions |
| 19 | 10 | 1.32 |  | Monsters A–Z > Actions |
| 20 | 13 | 1.12 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Speed`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 4.09 | yes | Rules Glossary > Speed |
| 2 | 7 | 4.08 | yes | Rules Glossary > Speed |
| 3 | 3 | 3.80 | yes | Rules Glossary > Speed |
| 4 | 5 | 3.36 |  | Playing the Game > Movement and Position |
| 5 | 20 | 3.24 |  | Monsters > Speed |
| 6 | 4 | 3.22 |  | Rules Glossary > Speed |
| 7 | 1 | 2.51 |  | Rules Glossary > Dash [Action] |
| 8 | 2 | 2.42 |  | Character Origins > Speed |
| 9 | 12 | 2.22 |  | Playing the Game > Your Turn |
| 10 | 9 | 2.03 |  | Rules Glossary > Fly Speed |
| 11 | 11 | 1.86 |  | Rules Glossary > Climb Speed |
| 12 | 13 | 1.50 |  | Equipment > Speed |
| 13 | 8 | 1.36 |  | Rules Glossary > Burrow Speed |
| 14 | 10 | 0.84 |  | Rules Glossary > Swim Speed |
| 15 | 18 | 0.82 |  | Rules Glossary > Petrified [Condition] |
| 16 | 15 | 0.52 |  | Rules Glossary > Dash [Action] |
| 17 | 16 | -1.06 |  | Equipment > Mastery Properties |
| 18 | 19 | -2.94 |  | Playing the Game > Mounting and Dismounting |
| 19 | 14 | -4.00 |  | Spells > Alter Self |
| 20 | 17 | -4.41 |  | Spells > Freedom of Movement |


*re-ranking* (query: `attacks`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 17 | 5.22 | yes | Playing the Game > Making an Attack |
| 2 | 4 | 4.79 | yes | Playing the Game > Melee Attacks |
| 3 | 14 | 3.91 | yes | Rules Glossary > Opportunity Attacks |
| 4 | 7 | 3.90 |  | Playing the Game > Ranged Attacks |
| 5 | 5 | 3.38 |  | Playing the Game > Opportunity Attacks |
| 6 | 3 | 2.50 |  | Rules Glossary > Attack [Action] |
| 7 | 11 | 2.10 |  | Playing the Game > Opportunity Attacks |
| 8 | 8 | 2.05 |  | Classes > Level 3: Deflect Attacks |
| 9 | 2 | 2.04 |  | Classes > Level 13: Studied Attacks |
| 10 | 9 | 1.55 |  | Monsters > Ammunition and Ranged Attacks |
| 11 | 18 | 1.31 |  | Playing the Game > Making an Attack |
| 12 | 10 | 0.84 |  | Classes > Level 3: Deflect Attacks |
| 13 | 20 | 0.70 |  | Playing the Game > Making an Attack |
| 14 | 6 | 0.48 |  | Classes > Level 11: Two Extra Attacks |
| 15 | 16 | 0.46 |  | Monsters A–Z > Actions |
| 16 | 12 | 0.45 |  | Monsters A–Z > Actions |
| 17 | 15 | 0.35 |  | Monsters A–Z > Actions |
| 18 | 1 | 0.34 |  | Classes > Level 20: Three Extra Attacks |
| 19 | 13 | 0.21 |  | Monsters A–Z > Actions |
| 20 | 19 | -1.14 |  | Classes > Level 13: Deflect Energy |


*re-ranking* (query: `Prone`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.07 | yes | Rules Glossary > Prone [Condition] |
| 2 | 1 | 4.03 | yes | Playing the Game > Dropping Prone |
| 3 | 4 | 2.69 | yes | Gameplay Toolbox > Rolling Stone |
| 4 | 11 | 2.45 |  | Rules Glossary > Prone [Condition] |
| 5 | 10 | 1.58 |  | Rules Glossary > Unconscious [Condition] |
| 6 | 5 | 1.51 |  | Animals > Actions |
| 7 | 3 | 1.35 |  | Animals > Actions |
| 8 | 7 | 1.22 |  | Animals > Actions |
| 9 | 14 | 0.90 |  | Monsters A–Z > Bonus Actions |
| 10 | 6 | 0.85 |  | Animals > Bonus Actions |
| 11 | 8 | 0.78 |  | Monsters A–Z > Bonus Actions |
| 12 | 9 | 0.56 |  | Playing the Game > Falling Off |
| 13 | 12 | 0.03 |  | Animals > Actions |
| 14 | 13 | -0.21 |  | Monsters A–Z > Bonus Actions |
| 15 | 16 | -0.25 |  | Monsters A–Z > Bonus Actions |
| 16 | 17 | -0.31 |  | Animals > Actions |
| 17 | 15 | -0.46 |  | Monsters A–Z > Bonus Actions |
| 18 | 20 | -0.48 |  | Animals > Actions |
| 19 | 19 | -1.28 |  | Animals > Actions |
| 20 | 18 | -2.17 |  | Gameplay Toolbox > Slippery Ice |


*re-ranking* (query: `movement`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.18 | yes | Playing the Game > Movement and Position |
| 2 | 18 | 2.06 | yes | Gameplay Toolbox > Special Movement |
| 3 | 2 | 1.96 | yes | Classes > Level 9: Acrobatic Movement |
| 4 | 7 | 1.06 |  | Playing the Game > Your Turn |
| 5 | 3 | 0.39 |  | Classes > Level 5: Fast Movement |
| 6 | 8 | -0.25 |  | Classes > Level 2: Unarmored Movement |
| 7 | 20 | -0.35 |  | Spells > Levitate |
| 8 | 5 | -0.37 |  | Spells > Freedom of Movement |
| 9 | 14 | -0.48 |  | Spells > Freedom of Movement |
| 10 | 19 | -0.96 |  | Playing the Game > Breaking Up Your Move |
| 11 | 17 | -1.10 |  | Spells > Telekinesis |
| 12 | 12 | -1.42 |  | Rules Glossary > Attack [Action] |
| 13 | 4 | -1.46 | yes | Rules Glossary > Prone [Condition] |
| 14 | 6 | -1.83 |  | Spells > Tree Stride |
| 15 | 11 | -2.96 |  | Animals > Bonus Actions |
| 16 | 13 | -3.13 |  | Monsters A–Z > Bonus Actions |
| 17 | 10 | -3.20 |  | Monsters A–Z > Bonus Actions |
| 18 | 9 | -3.38 |  | Monsters A–Z > Bonus Actions |
| 19 | 15 | -3.60 |  | Rules Glossary > Disengage [Action] |
| 20 | 16 | -4.44 |  | Rules Glossary > Teleportation |


*re-ranking* (query: `attack rolls`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 9.43 | yes | Rules Glossary > Attack Roll |
| 2 | 1 | 9.36 |  | Playing the Game > Attack Rolls |
| 3 | 5 | 7.54 |  | Spells > Attack Rolls |
| 4 | 9 | 6.75 |  | Rules Glossary > Invisible [Condition] |
| 5 | 11 | 6.68 |  | Classes > Level 2: Reckless Attack |
| 6 | 8 | 6.42 |  | Rules Glossary > Attack [Action] |
| 7 | 17 | 6.32 |  | Equipment > Properties |
| 8 | 6 | 6.15 |  | Playing the Game > Making an Attack |
| 9 | 14 | 5.94 |  | Magic Items > Staff of the Magi |
| 10 | 16 | 5.88 |  | Monsters A–Z > Actions |
| 11 | 15 | 5.54 |  | Magic Items > Staff of Power |
| 12 | 7 | 5.54 |  | Magic Items > Ring of Elemental Command |
| 13 | 13 | 5.37 |  | Monsters A–Z > Actions |
| 14 | 3 | 5.32 |  | Playing the Game > D20 Tests |
| 15 | 18 | 5.26 |  | Monsters A–Z > Actions |
| 16 | 2 | 5.19 |  | Magic Items > Defender |
| 17 | 19 | 4.74 |  | Magic Items > Hammer of Thunderbolts |
| 18 | 20 | 4.09 |  | Rules Glossary > Blinded [Condition] |
| 19 | 12 | 1.15 |  | Feats > Savage Attacker |
| 20 | 10 | -4.40 |  | Rules Glossary > Attack [Action] |

*retrieved sections:* Rules Glossary > Grappling | Rules Glossary > Grappled [Condition] | Rules Glossary > Speed | Playing the Game > Making an Attack | Playing the Game > Melee Attacks | Rules Glossary > Opportunity Attacks | Rules Glossary > Prone [Condition] | Playing the Game > Dropping Prone | Gameplay Toolbox > Rolling Stone | Playing the Game > Movement and Position | Gameplay Toolbox > Special Movement | Classes > Level 9: Acrobatic Movement | Rules Glossary > Attack Roll

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappling]
#### Grappling  
A creature can grapple another creature. Characters typically grapple by using an Unarmed Strike. Many monsters have special attacks that allow them to quickly grapple prey. However a grapple is initiated, it follows these rules. _See also_ "Unarmed Strike" and "Grappled."  
_Grappled Condition._ Successfully grappling a creature gives it the Grappled condition.

---

[Rules Glossary > Grappling]
_Ending a Grapple._ A Grappled creature can use its action to make a Strength (Athletics) or Dexterity (Acrobatics) check against the grapple's escape DC, ending the condition on itself on a success. The condition also ends if the grappler has the Incapacitated condition or if the distance between the Grappled target and the grappler exceeds the grapple's range. In addition, the grappler can release the target at any time (no action required).

---

[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Rules Glossary > Speed]
#### Speed  
A creature has a Speed, which is the distance in feet the creature can cover when it moves on its turn. _See also_ "Climbing," "Crawling," "Flying," "Jumping," "Swimming" and "Playing the Game" ("Combat").

---

[Rules Glossary > Speed]
use the new speed during the current move. For example, if you have a Speed of 30 and a Fly Speed of 40, you could fly 10 feet, walk 10 feet, and leap into the air to fly 20 feet more.

---

[Rules Glossary > Speed]
_Changes to Your Speeds._ If an effect increases or decreases your Speed for a time, any special speed you have increases or decreases by an equal amount for the same duration. For example, if your Speed is reduced to 0 and you have a Climb Speed, your Climb Speed is also reduced to 0. Similarly, if your Speed is halved and you have a Fly Speed, your Fly Speed is also halved.

---

[Playing the Game > Making an Attack]
### Making an Attack  
When you take the Attack action, you make an attack. Some other actions, Bonus Actions, and Reactions also let you make an attack. Whether you strike with a Melee weapon, fire a Ranged weapon, or make an attack roll as part of a spell, an attack has the following structure:  
**1: Choose a Target.** Pick a target within your attack's range: a creature, an object, or a location.

---

[Playing the Game > Melee Attacks]
### Melee Attacks  
A melee attack allows you to attack a target within your reach. A melee attack typically uses a handheld weapon or an Unarmed Strike. Many monsters make melee attacks with claws, teeth, or other body parts. A few spells also involve melee attacks.

---

[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").

---

[Rules Glossary > Prone [Condition]]
#### Prone [Condition]  
While you have the Prone condition, you experience the following effects.  
_Restricted Movement._ Your only movement options are to crawl or to spend an amount of movement equal to half your Speed (round down) to right yourself and thereby end the condition. If your Speed is 0, you can't right yourself.

---

[Playing the Game > Dropping Prone]
#### Dropping Prone  
On your turn, you can give yourself the Prone condition (see "Rules Glossary") without using an action or any of your Speed, but you can't do so if your Speed is 0.

---

[Gameplay Toolbox > Rolling Stone]
55 (10d10) Bludgeoning damage and have the Prone condition.

---

[Playing the Game > Movement and Position]
### Movement and Position  
On your turn, you can move a distance equal to your Speed or less. Or you can decide not to move.  
Your movement can include climbing, crawling, jumping, and swimming (each explained in "Rules Glossary"). These different modes of movement can be combined with your regular movement, or they can constitute your entire move.

---

[Gameplay Toolbox > Special Movement]
If the characters are flying or their special movement allows them to ignore Difficult Terrain, they can move at a Fast pace regardless of the terrain.

---

[Classes > Level 9: Acrobatic Movement]
#### Level 9: Acrobatic Movement  
While you aren't wearing armor or wielding a Shield, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the movement.

---

[Rules Glossary > Attack Roll]
#### Attack Roll  
An attack roll is a D20 Test that represents making an attack with a weapon, an Unarmed Strike, or a spell. _See also_ "Playing the Game" ("D20 Tests").
```
</details>


---

## q8 (multi-part) When can you make an Opportunity Attack and what does it cost? And what are the minimum lengths of a Long Rest (including how much must be sleep) and of a Short Rest, and how long must you wait between Long Rests?

**Gold facts (counterfactual data):** Reaction; at least 10 hours; at least 6 hours; 16 hours; 2-hour


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Opportunity Attack:**
- You can make an Opportunity Attack when an enemy leaves your reach after attacking you or another creature within your reach.
- It costs your action to make an Opportunity Attack.

**Rests:**
- **Short Rest:** A short rest lasts 1 hour and can include light activity like eating or standing guard. There is no specific requirement for sleep during a short rest.
- **Long Rest:** A long rest requires 8 hours of sleep and no significant activity. You must wait at least 8 hours between long rests before you can start another one.

These details are consistent with the 2024 SRD 5.2 for D&D 5e.

*facts found (judge): 0/5; missing: Reaction; at least 10 hours; at least 6 hours; 16 hours; 2-hour*


### v1_baseline  (3 chunks, 1 LLM call(s))

You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. It costs a Reaction to make this attack.

A Long Rest requires at least 10 hours total, including at least 6 hours of sleep and no more than 2 hours of light activity. You must wait at least 16 hours between Long Rests.

A Short Rest is 2 hours long and requires at least 1 Hit Point. No waiting period is mentioned between Short Rests.

*facts found (judge): 5/5; missing: none*

*retrieved sections:* Rules Glossary > Long Rest | Rules Glossary > Short Rest | Rules Glossary > Opportunity Attacks

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Long Rest]
#### Long Rest  
A Long Rest is a period of extended downtime—at least 10 hours—available to any creature. During a Long Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch.  
During sleep, you have the Unconscious condition. After you finish a Long Rest, you must wait at least 16 hours before starting another one.

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The context provided only discusses when an Opportunity Attack can be made and does not mention the costs associated with it, nor does it provide information about rest durations. Therefore, the following parts are missing:

- What the cost is for making an Opportunity Attack.
- The length of a Long Rest, including how much must be spent sleeping.
- The length of a Short Rest.
- How long one must wait between Long Rests.

*facts found (judge): 0/5; missing: Reaction; at least 10 hours; at least 6 hours; 16 hours; 2-hour*


*re-ranking* (query: `When can you make an Opportunity Attack and what does it cost? And what are the `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -0.85 | yes | Playing the Game > Opportunity Attacks |
| 2 | 3 | -1.10 | yes | Rules Glossary > Opportunity Attacks |
| 3 | 5 | -3.24 | yes | Playing the Game > Opportunity Attacks |
| 4 | 10 | -3.39 |  | Playing the Game > Opportunity Attacks |
| 5 | 1 | -4.17 |  | Rules Glossary > Long Rest |
| 6 | 9 | -5.74 |  | Rules Glossary > Long Rest |
| 7 | 2 | -5.99 |  | Rules Glossary > Short Rest |
| 8 | 6 | -6.21 |  | Rules Glossary > Long Rest |
| 9 | 8 | -6.73 |  | Rules Glossary > Long Rest |
| 10 | 7 | -7.13 |  | Playing the Game > Hit Points |

*retrieved sections:* Playing the Game > Opportunity Attacks | Rules Glossary > Opportunity Attacks

<details><summary>full retrieved context</summary>

```
[Playing the Game > Opportunity Attacks]
_Making an Opportunity Attack._ You can make an Opportunity Attack when a creature that you can see leaves your reach. To make the attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against that creature. The attack occurs right before it leaves your reach.

---

[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Opportunity Attacks]
_Avoiding Opportunity Attacks._ You can avoid provoking an Opportunity Attack by taking the Disengage action. You also don't provoke an Opportunity Attack when you Teleport or when you are moved without using your movement, action, Bonus Action, or Reaction. For example, you don't provoke an Opportunity Attack if an explosion hurls you out of a foe's reach or if you fall past an enemy.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

You can make an Opportunity Attack when a creature that you can see leaves your reach, using its action, bonus action, reaction, or one of its speeds. It costs a Reaction.

A Long Rest requires at least 10 hours total, including at least 6 hours of sleep. A Short Rest is a 2-hour period of downtime. You must wait at least 16 hours between Long Rests.

*facts found (judge): 5/5; missing: none*


*re-ranking* (query: `When can you make an Opportunity Attack and what does it cost? And what are the `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -0.85 | yes | Playing the Game > Opportunity Attacks |
| 2 | 3 | -1.10 | yes | Rules Glossary > Opportunity Attacks |
| 3 | 5 | -3.24 | yes | Playing the Game > Opportunity Attacks |
| 4 | 10 | -3.39 | yes | Playing the Game > Opportunity Attacks |
| 5 | 1 | -4.17 | yes | Rules Glossary > Long Rest |
| 6 | 9 | -5.74 | yes | Rules Glossary > Long Rest |
| 7 | 2 | -5.99 | yes | Rules Glossary > Short Rest |
| 8 | 6 | -6.21 | yes | Rules Glossary > Long Rest |
| 9 | 8 | -6.73 |  | Rules Glossary > Long Rest |
| 10 | 7 | -7.13 |  | Playing the Game > Hit Points |

*retrieved sections:* Playing the Game > Opportunity Attacks | Rules Glossary > Opportunity Attacks | Rules Glossary > Long Rest | Rules Glossary > Short Rest

<details><summary>full retrieved context</summary>

```
[Playing the Game > Opportunity Attacks]
_Making an Opportunity Attack._ You can make an Opportunity Attack when a creature that you can see leaves your reach. To make the attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against that creature. The attack occurs right before it leaves your reach.

---

[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Opportunity Attacks]
_Avoiding Opportunity Attacks._ You can avoid provoking an Opportunity Attack by taking the Disengage action. You also don't provoke an Opportunity Attack when you Teleport or when you are moved without using your movement, action, Bonus Action, or Reaction. For example, you don't provoke an Opportunity Attack if an explosion hurls you out of a foe's reach or if you fall past an enemy.

---

[Playing the Game > Opportunity Attacks]
#### Opportunity Attacks  
Combatants watch for enemies to drop their guard. If you move heedlessly past your foes, you put yourself in danger by provoking an Opportunity Attack.

---

[Rules Glossary > Long Rest]
#### Long Rest  
A Long Rest is a period of extended downtime—at least 10 hours—available to any creature. During a Long Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch.  
During sleep, you have the Unconscious condition. After you finish a Long Rest, you must wait at least 16 hours before starting another one.

---

[Rules Glossary > Long Rest]
You can resume a Long Rest immediately after an interruption. If you do so, the rest requires 1 additional hour per interruption to finish.

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Rules Glossary > Long Rest]
_Benefits of the Rest._ To start a Long Rest, you must have at least 1 Hit Point. When you finish the rest, you gain the following benefits:  
**Regain All HP.** You regain all lost Hit Points and all spent Hit Point Dice. If your Hit Point maximum was reduced, it returns to normal.  
**Ability Scores Restored.** If any of your ability scores were reduced, they return to normal.  
**Exhaustion Reduced.** If you have the Exhaustion condition, its level decreases by 1.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The context provided only discusses when an Opportunity Attack can be made and does not mention the costs associated with it, nor does it provide information about rest durations. Therefore, the following parts are missing:

- What the cost is for making an Opportunity Attack.
- The length of a Long Rest, including how much must be spent sleeping.
- The length of a Short Rest.
- How long one must wait between Long Rests.

*facts found (judge): 0/5; missing: Reaction; at least 10 hours; at least 6 hours; 16 hours; 2-hour*


*re-ranking* (query: `When can you make an Opportunity Attack and what does it cost? And what are the `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -0.85 | yes | Playing the Game > Opportunity Attacks |
| 2 | 3 | -1.10 | yes | Rules Glossary > Opportunity Attacks |
| 3 | 5 | -3.24 | yes | Playing the Game > Opportunity Attacks |
| 4 | 10 | -3.39 |  | Playing the Game > Opportunity Attacks |
| 5 | 1 | -4.17 |  | Rules Glossary > Long Rest |
| 6 | 9 | -5.74 |  | Rules Glossary > Long Rest |
| 7 | 2 | -5.99 |  | Rules Glossary > Short Rest |
| 8 | 6 | -6.21 |  | Rules Glossary > Long Rest |
| 9 | 8 | -6.73 |  | Rules Glossary > Long Rest |
| 10 | 7 | -7.13 |  | Playing the Game > Hit Points |

*retrieved sections:* Playing the Game > Opportunity Attacks | Rules Glossary > Opportunity Attacks

<details><summary>full retrieved context</summary>

```
[Playing the Game > Opportunity Attacks]
_Making an Opportunity Attack._ You can make an Opportunity Attack when a creature that you can see leaves your reach. To make the attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against that creature. The attack occurs right before it leaves your reach.

---

[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Opportunity Attacks]
_Avoiding Opportunity Attacks._ You can avoid provoking an Opportunity Attack by taking the Disengage action. You also don't provoke an Opportunity Attack when you Teleport or when you are moved without using your movement, action, Bonus Action, or Reaction. For example, you don't provoke an Opportunity Attack if an explosion hurls you out of a foe's reach or if you fall past an enemy.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

You can make an Opportunity Attack when a creature that you can see leaves your reach, using its action, its Bonus Action, its Reaction, or one of its speeds. It costs a Reaction to make the attack.

A Long Rest requires at least 10 hours, with at least 6 hours of sleep and no more than 2 hours of light activity. You must wait at least 16 hours between Long Rests.

*facts found (judge): 4/5; missing: 2-hour*


*re-ranking* (query: `When can you make an Opportunity Attack and what does it cost? And what are the `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -0.85 | yes | Playing the Game > Opportunity Attacks |
| 2 | 5 | -1.10 | yes | Rules Glossary > Opportunity Attacks |
| 3 | 6 | -3.24 | yes | Playing the Game > Opportunity Attacks |
| 4 | 15 | -3.29 | yes | Classes > Level 7: Defensive Tactics |
| 5 | 18 | -3.39 | yes | Playing the Game > Opportunity Attacks |
| 6 | 1 | -4.17 | yes | Rules Glossary > Long Rest |
| 7 | 22 | -5.65 | yes | Playing the Game > Actions |
| 8 | 16 | -5.74 | yes | Rules Glossary > Long Rest |
| 9 | 2 | -5.99 |  | Rules Glossary > Short Rest |
| 10 | 12 | -6.21 |  | Rules Glossary > Long Rest |
| 11 | 24 | -6.40 |  | Rules Glossary > Reaction |
| 12 | 7 | -6.73 |  | Rules Glossary > Long Rest |
| 13 | 19 | -6.96 |  | Magic Items > Quarterstaff of the Acrobat |
| 14 | 3 | -7.13 |  | Playing the Game > Hit Points |
| 15 | 23 | -7.43 |  | Rules Glossary > Per Day |
| 16 | 30 | -7.65 |  | Rules Glossary > Exhaustion [Condition] |
| 17 | 21 | -8.03 |  | Rules Glossary > Short Rest |
| 18 | 10 | -8.05 |  | Equipment > Attune during a Short Rest |
| 19 | 28 | -8.15 |  | Playing the Game > Duration |
| 20 | 9 | -8.21 |  | Character Origins > Elf |

*retrieved sections:* Playing the Game > Opportunity Attacks | Rules Glossary > Opportunity Attacks | Classes > Level 7: Defensive Tactics | Rules Glossary > Long Rest | Playing the Game > Actions

<details><summary>full retrieved context</summary>

```
[Playing the Game > Opportunity Attacks]
_Making an Opportunity Attack._ You can make an Opportunity Attack when a creature that you can see leaves your reach. To make the attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against that creature. The attack occurs right before it leaves your reach.

---

[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Opportunity Attacks]
_Avoiding Opportunity Attacks._ You can avoid provoking an Opportunity Attack by taking the Disengage action. You also don't provoke an Opportunity Attack when you Teleport or when you are moved without using your movement, action, Bonus Action, or Reaction. For example, you don't provoke an Opportunity Attack if an explosion hurls you out of a foe's reach or if you fall past an enemy.

---

[Classes > Level 7: Defensive Tactics]
#### Level 7: Defensive Tactics  
You gain one of the following feature options of your choice. Whenever you finish a Short or Long Rest, you can replace the chosen option with the other one.  
_Escape the Horde._ Opportunity Attacks have Disadvantage against you.  
_Multiattack Defense._ When a creature hits you with an attack roll, that creature has Disadvantage on all other attack rolls against you this turn.

---

[Playing the Game > Opportunity Attacks]
#### Opportunity Attacks  
Combatants watch for enemies to drop their guard. If you move heedlessly past your foes, you put yourself in danger by provoking an Opportunity Attack.

---

[Rules Glossary > Long Rest]
#### Long Rest  
A Long Rest is a period of extended downtime—at least 10 hours—available to any creature. During a Long Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch.  
During sleep, you have the Unconscious condition. After you finish a Long Rest, you must wait at least 16 hours before starting another one.

---

[Playing the Game > Actions]
</tr>
<tr>
<td>Disengage</td>
<td>Your movement doesn't provoke Opportunity Attacks for the rest of the turn.</td>
</tr>
<tr>
<td>Dodge</td>
<td>Until the start of your next turn, attack rolls against you have Disadvantage, and you make Dexterity saving throws with Advantage. You lose this benefit if you have the Incapacitated condition or if your Speed is 0.</td>
</tr>
<tr>
<td>Help</td>
<td>Help another creature's ability check or attack roll, or administer first aid.</td>
</tr>
<tr>

---

[Rules Glossary > Long Rest]
You can resume a Long Rest immediately after an interruption. If you do so, the rest requires 1 additional hour per interruption to finish.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

You can make an Opportunity Attack when a creature that you can see leaves your reach, and it costs a Reaction.

A Long Rest requires at least 10 hours, including at least 6 hours of sleep and up to 2 hours of light activity. You must wait at least 16 hours between Long Rests.

A Short Rest is 2 hours long and includes no more than 2 hours of light activity.

*facts found (judge): 5/5; missing: none*


*re-ranking* (query: `When can you make an Opportunity Attack and what does it cost? And what are the `): candidate pool of 21, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -0.85 | yes | Playing the Game > Opportunity Attacks |
| 2 | 5 | -1.10 | yes | Rules Glossary > Opportunity Attacks |
| 3 | 6 | -3.24 | yes | Playing the Game > Opportunity Attacks |
| 4 | 1 | -4.17 | yes | Rules Glossary > Long Rest |
| 5 | 2 | -5.99 | yes | Rules Glossary > Short Rest |
| 6 | 15 | -6.40 | yes | Rules Glossary > Reaction |
| 7 | 7 | -6.73 | yes | Rules Glossary > Long Rest |
| 8 | 3 | -7.13 | yes | Playing the Game > Hit Points |
| 9 | 14 | -8.03 |  | Rules Glossary > Short Rest |
| 10 | 10 | -8.05 |  | Equipment > Attune during a Short Rest |
| 11 | 9 | -8.21 |  | Character Origins > Elf |
| 12 | 18 | -8.50 |  | Rules Glossary > Unconscious [Condition] |
| 13 | 8 | -8.73 |  | Rules Glossary > Short Rest |
| 14 | 13 | -8.95 |  | Spells > Sleep |
| 15 | 17 | -9.43 |  | Rules Glossary > Unarmed Strike |
| 16 | 20 | -9.55 |  | Rules Glossary > Bloodied |
| 17 | 12 | -9.61 |  | Spells > Sleep |
| 18 | 19 | -9.70 |  | Rules Glossary > Unconscious [Condition] |
| 19 | 11 | -9.74 |  | Spells > Sleep |
| 20 | 16 | -9.96 |  | Rules Glossary > Unarmed Strike |

*retrieved sections:* Playing the Game > Opportunity Attacks | Rules Glossary > Opportunity Attacks | Rules Glossary > Long Rest | Rules Glossary > Short Rest | Rules Glossary > Reaction | Playing the Game > Hit Points

<details><summary>full retrieved context</summary>

```
[Playing the Game > Opportunity Attacks]
_Making an Opportunity Attack._ You can make an Opportunity Attack when a creature that you can see leaves your reach. To make the attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against that creature. The attack occurs right before it leaves your reach.

---

[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Opportunity Attacks]
_Avoiding Opportunity Attacks._ You can avoid provoking an Opportunity Attack by taking the Disengage action. You also don't provoke an Opportunity Attack when you Teleport or when you are moved without using your movement, action, Bonus Action, or Reaction. For example, you don't provoke an Opportunity Attack if an explosion hurls you out of a foe's reach or if you fall past an enemy.

---

[Rules Glossary > Long Rest]
#### Long Rest  
A Long Rest is a period of extended downtime—at least 10 hours—available to any creature. During a Long Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch.  
During sleep, you have the Unconscious condition. After you finish a Long Rest, you must wait at least 16 hours before starting another one.

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Rules Glossary > Reaction]
#### Reaction  
A Reaction is a special action taken in response to a trigger defined in the Reaction's description. You can take a Reaction on another creature's turn, and if you take it on your turn, you can do so even if you also take an action, a Bonus Action, or both. Once you take a Reaction, you can't take another one until the start of your next turn. The Opportunity Attack is a Reaction available to all creatures. _See also_ "Opportunity Attacks" and "Playing the Game" ("Actions").

---

[Rules Glossary > Long Rest]
**Special Feature.** Some features are recharged by a Long Rest. If you have such a feature, it recharges in the way specified in its description.  
_Interrupting the Rest._ A Long Rest is stopped by the following interruptions:  
- Rolling Initiative
- Casting a spell other than a cantrip
- Taking any damage
- 1 hour of walking or other physical exertion  
If you rested at least 1 hour before the interruption, you gain the benefits of a Short Rest. _See also_ "Short Rest."

---

[Playing the Game > Hit Points]
If you have half your Hit Points or fewer, you're Bloodied, which has no game effect on its own but which might trigger other game effects.  
> **RESTING**
>
> Adventurers can't spend every hour adventuring. They need rest. Any creature can take hour-long Short Rests in the midst of a day and an 8-hour Long Rest to end it. Regaining Hit Points is one of the main benefits of a rest. "Rules Glossary" provides the rules for Short and Long Rests.
```
</details>


### v6_agentic  (11 chunks, 3 LLM call(s))

You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. It costs a Reaction to make the attack.

A Long Rest requires at least 10 hours, including at least 6 hours of sleep. You must wait at least 16 hours before starting another Long Rest. If a Long Rest is interrupted, it requires 1 additional hour per interruption to finish.

A Short Rest lasts 2 hours and includes no more than 2 hours of light activity. You must wait at least 16 hours before starting another Short Rest. An interrupted Short Rest confers no benefits.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* Opportunity Attack / Long Rest / Short Rest / Sleep / Rest Between Long Rests


*re-ranking* (query: `Opportunity Attack`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 9.38 | yes | Rules Glossary > Opportunity Attacks |
| 2 | 2 | 8.41 | yes | Playing the Game > Opportunity Attacks |
| 3 | 4 | 8.32 | yes | Playing the Game > Opportunity Attacks |
| 4 | 1 | 7.71 |  | Playing the Game > Opportunity Attacks |
| 5 | 5 | 6.31 |  | Rules Glossary > Reaction |
| 6 | 10 | 4.33 |  | Playing the Game > Reactions |
| 7 | 11 | 3.59 |  | Magic Items > Mace of Terror |
| 8 | 8 | 3.03 |  | Rules Glossary > Disengage [Action] |
| 9 | 9 | 2.85 |  | Playing the Game > Actions |
| 10 | 20 | 2.67 |  | Animals > Traits |
| 11 | 6 | 2.54 |  | Monsters A–Z > Traits |
| 12 | 7 | 2.46 |  | Monsters A–Z > Traits |
| 13 | 12 | 2.33 |  | Spells > Shocking Grasp |
| 14 | 19 | 2.22 |  | Animals > Traits |
| 15 | 18 | 1.88 |  | Magic Items > Boots of Speed |
| 16 | 13 | 1.87 |  | Monsters A–Z > Actions |
| 17 | 14 | 0.98 |  | Monsters A–Z > Bonus Actions |
| 18 | 16 | -6.28 |  | Playing the Game > Making an Attack |
| 19 | 17 | -7.07 |  | Rules Glossary > Attack [Action] |
| 20 | 15 | -8.10 |  | Playing the Game > Attack Rolls |


*re-ranking* (query: `Long Rest`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 9.47 | yes | Rules Glossary > Long Rest |
| 2 | 3 | 6.75 | yes | Rules Glossary > Long Rest |
| 3 | 2 | 6.51 | yes | Rules Glossary > Long Rest |
| 4 | 4 | 6.22 |  | Rules Glossary > Long Rest |
| 5 | 14 | 4.32 | yes | Rules Glossary > Short Rest |
| 6 | 5 | 4.10 |  | Spells > Spell Slots |
| 7 | 12 | 3.65 |  | Spells > Divination |
| 8 | 6 | 3.38 |  | Rules Glossary > Exhaustion [Condition] |
| 9 | 15 | 2.96 |  | Spells > Preparing Spells |
| 10 | 17 | 2.63 |  | Monsters > Limited Usage |
| 11 | 19 | 2.46 |  | Playing the Game > Hit Points |
| 12 | 8 | 2.35 |  | Character Origins > Elf |
| 13 | 7 | 2.13 |  | Magic Items > Ring of X-ray Vision |
| 14 | 9 | 1.53 |  | Rules Glossary > Per Day |
| 15 | 20 | 1.02 |  | Playing the Game > Duration |
| 16 | 18 | 1.01 |  | Classes > Level 9: Indomitable |
| 17 | 11 | 0.27 |  | Spells > Resurrection |
| 18 | 16 | -0.33 | yes | Rules Glossary > Short Rest |
| 19 | 10 | -0.82 |  | Spells > Prayer of Healing |
| 20 | 13 | -0.88 |  | Character Origins > Orc |


*re-ranking* (query: `Short Rest`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 9.24 | yes | Rules Glossary > Short Rest |
| 2 | 2 | 7.16 | yes | Rules Glossary > Short Rest |
| 3 | 5 | 6.66 | yes | Equipment > Attune during a Short Rest |
| 4 | 4 | 5.60 | yes | Rules Glossary > Long Rest |
| 5 | 7 | 4.92 |  | Rules Glossary > Short Rest |
| 6 | 9 | 4.82 |  | Equipment > Attune during a Short Rest |
| 7 | 3 | 4.42 |  | Equipment > Attune during a Short Rest |
| 8 | 20 | 4.08 |  | Classes > Level 10: Tireless |
| 9 | 18 | 3.29 |  | Monsters > Limited Usage |
| 10 | 11 | 2.47 | yes | Rules Glossary > Long Rest |
| 11 | 8 | 2.15 |  | Rules Glossary > Hit Point Dice |
| 12 | 6 | 2.12 |  | Playing the Game > Hit Points |
| 13 | 15 | 1.83 |  | Playing the Game > Healing |
| 14 | 12 | 1.61 | yes | Rules Glossary > Long Rest |
| 15 | 16 | 0.82 |  | Rules Glossary > Knocking Out a Creature |
| 16 | 10 | 0.16 |  | Spells > Prayer of Healing |
| 17 | 17 | -0.27 |  | Rules Glossary > Long Rest |
| 18 | 13 | -0.67 |  | Equipment > Ending Attunement |
| 19 | 14 | -1.20 |  | Character Origins > Orc |
| 20 | 19 | -3.18 |  | Rules Glossary > Exhaustion [Condition] |


*re-ranking* (query: `Sleep`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.04 | yes | Spells > Sleep |
| 2 | 4 | 0.40 | yes | Rules Glossary > Long Rest |
| 3 | 3 | -0.37 | yes | Spells > Sleep |
| 4 | 18 | -0.63 |  | Spells > Dream |
| 5 | 6 | -1.03 |  | Spells > Sleep |
| 6 | 1 | -1.17 |  | Character Origins > Elf |
| 7 | 5 | -2.39 |  | Spells > Dream |
| 8 | 16 | -3.24 |  | Classes > Level 1 Wizard Spells |
| 9 | 13 | -3.50 |  | Monsters A–Z > Actions |
| 10 | 9 | -3.55 |  | Monsters A–Z > Actions |
| 11 | 7 | -3.62 |  | Spells > Symbol |
| 12 | 11 | -3.77 |  | Monsters A–Z > Actions |
| 13 | 14 | -4.19 |  | Spells > Imprisonment |
| 14 | 8 | -4.36 |  | Magic Items > Weapon of Warning |
| 15 | 17 | -5.30 |  | Spells > Symbol |
| 16 | 19 | -5.83 |  | Magic Items > Mirror of Life Trapping |
| 17 | 15 | -7.82 | yes | Rules Glossary > Short Rest |
| 18 | 10 | -8.52 |  | Playing the Game > Hit Points |
| 19 | 12 | -9.56 |  | Rules Glossary > Exhaustion [Condition] |
| 20 | 20 | -9.88 | yes | Rules Glossary > Long Rest |


*re-ranking* (query: `Rest Between Long Rests`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.74 | yes | Rules Glossary > Long Rest |
| 2 | 4 | 3.19 | yes | Rules Glossary > Long Rest |
| 3 | 3 | 2.98 | yes | Rules Glossary > Long Rest |
| 4 | 5 | 2.93 |  | Rules Glossary > Long Rest |
| 5 | 2 | 2.21 |  | Playing the Game > Hit Points |
| 6 | 20 | 0.29 |  | Spells > Preparing Spells |
| 7 | 15 | -0.59 |  | Spells > Augury |
| 8 | 10 | -1.14 |  | Spells > Divination |
| 9 | 19 | -1.72 | yes | Rules Glossary > Short Rest |
| 10 | 18 | -1.98 |  | Spells > Simulacrum |
| 11 | 6 | -2.72 |  | Spells > Spell Slots |
| 12 | 7 | -3.65 |  | Rules Glossary > Exhaustion [Condition] |
| 13 | 14 | -3.69 |  | Spells > Bonus Actions |
| 14 | 8 | -4.14 |  | Playing the Game > Duration |
| 15 | 11 | -4.54 |  | Magic Items > Ring of X-ray Vision |
| 16 | 9 | -6.51 |  | Character Origins > Elf |
| 17 | 13 | -7.02 |  | Rules Glossary > Per Day |
| 18 | 12 | -7.06 |  | Spells > Prayer of Healing |
| 19 | 17 | -7.37 |  | Character Origins > Orc |
| 20 | 16 | -7.42 |  | Spells > Resurrection |

*retrieved sections:* Rules Glossary > Opportunity Attacks | Playing the Game > Opportunity Attacks | Rules Glossary > Long Rest | Rules Glossary > Short Rest | Equipment > Attune during a Short Rest | Spells > Sleep

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Opportunity Attacks]
#### Opportunity Attacks  
You can make an Opportunity Attack when a creature that you can see leaves your reach using its action, its Bonus Action, its Reaction, or one of its speeds. To make the Opportunity Attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against the provoking creature. The attack occurs right before the creature leaves your reach. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Opportunity Attacks]
#### Opportunity Attacks  
Combatants watch for enemies to drop their guard. If you move heedlessly past your foes, you put yourself in danger by provoking an Opportunity Attack.

---

[Playing the Game > Opportunity Attacks]
_Making an Opportunity Attack._ You can make an Opportunity Attack when a creature that you can see leaves your reach. To make the attack, take a Reaction to make one melee attack with a weapon or an Unarmed Strike against that creature. The attack occurs right before it leaves your reach.

---

[Rules Glossary > Long Rest]
#### Long Rest  
A Long Rest is a period of extended downtime—at least 10 hours—available to any creature. During a Long Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch.  
During sleep, you have the Unconscious condition. After you finish a Long Rest, you must wait at least 16 hours before starting another one.

---

[Rules Glossary > Long Rest]
You can resume a Long Rest immediately after an interruption. If you do so, the rest requires 1 additional hour per interruption to finish.

---

[Rules Glossary > Long Rest]
**Special Feature.** Some features are recharged by a Long Rest. If you have such a feature, it recharges in the way specified in its description.  
_Interrupting the Rest._ A Long Rest is stopped by the following interruptions:  
- Rolling Initiative
- Casting a spell other than a cantrip
- Taking any damage
- 1 hour of walking or other physical exertion  
If you rested at least 1 hour before the interruption, you gain the benefits of a Short Rest. _See also_ "Short Rest."

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Rules Glossary > Short Rest]
_Interrupting the Rest._ A Short Rest is stopped by the following interruptions:  
- Rolling Initiative
- Casting a spell other than a cantrip
- Taking any damage  
An interrupted Short Rest confers no benefits.

---

[Equipment > Attune during a Short Rest]
Attuning to an item requires you to spend a Short Rest focused on only that item while being in physical contact with it (this can't be the same Short Rest used to learn the item's properties). This focus can take the form of weapon practice (for a Weapon), meditation (for a Wand), or some other appropriate activity. If the Short Rest is interrupted, the Attunement attempt fails. Otherwise, at the end of the Short Rest, you're attuned to the magic item and can access its full magical

---

[Spells > Sleep]
Creatures that don't sleep, such as elves, or that have Immunity to the Exhaustion condition automatically succeed on saves against this spell.

---

[Spells > Sleep]
#### Sleep  
_Level 1 Enchantment (Bard, Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 60 feet
**Components:** V, S, M (a pinch of sand or rose petals)
**Duration:** Concentration, up to 1 minute
```
</details>


---

## q9 (multi-part) Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each one do when you hit?

**Gold facts (counterfactual data):** Strength saving throw; Prone; 15 feet; Large or smaller; Disadvantage on its next attack roll; reduce its Speed by 10 feet


### v0_closed_book  (0 chunks, 1 LLM call(s))

Certainly! Here's a concise explanation of each weapon mastery property:

1. **Topple**: When you hit with a melee attack using a weapon that has the Topple property, you can attempt to knock your target prone. The target must make a Strength saving throw. On a failed save, they fall prone. On a successful save, they remain standing.

2. **Push**: When you hit with a melee attack using a weapon that has the Push property, you can push the target up to a number of feet equal to half your Strength modifier. The target must succeed on a Strength saving throw or be pushed away from you. They can use their action to move back into the space if they succeed on the saving throw.

3. **Sap**: When you hit with a melee attack using a weapon that has the Sap property, you can attempt to incapacitate the target. The target must make a Constitution saving throw. On a failed save, they are incapacitated until the end of their next turn. On a successful save, they are not incapacitated.

4. **Slow**: When you hit with a melee attack using a weapon that has the Slow property, you can slow the target. The target must make a Dexterity saving throw. On a failed save, they are slowed until the end of their next turn. On a successful save, they are not slowed.

Each property provides a different effect when the weapon hits, enhancing the combat options available to the character.

*facts found (judge): 2/6; missing: 15 feet; Large or smaller; Disadvantage on its next attack roll; reduce its Speed by 10 feet*


### v1_baseline  (3 chunks, 1 LLM call(s))

- **Topple:** Forces the creature to make a Strength saving throw. On a failed save, the creature becomes Prone.
- **Push:** Pushes the creature up to 15 feet straight away from the attacker if the target is Large or smaller.
- **Sap:** Grants the attacker Disadvantage on the target's next attack roll before the start of their next turn.
- **Slow:** Missing information about what Slow does.

*facts found (judge): 5/6; missing: reduce its Speed by 10 feet*

*retrieved sections:* Equipment > Mastery Properties | Classes > Level 9: Tactical Master

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Classes > Level 9: Tactical Master]
#### Level 9: Tactical Master  
When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack.

---

[Equipment > Mastery Properties]
**Topple.** If you hit a creature with this weapon, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.  
**Vex.** If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.  
**Weapons**  
<table>
<thead>
<tr>
<th>Name</th>
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

- **Topple:** The context does not mention a "Topple" property, so this part is missing.
- **Push:** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.
- **Sap:** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.
- **Slow:** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

*facts found (judge): 4/6; missing: Strength saving throw; Prone*


*re-ranking* (query: `Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.02 | yes | Equipment > Mastery Properties |
| 2 | 4 | 3.06 | yes | Equipment > Mastery Properties |
| 3 | 2 | 2.87 | yes | Classes > Level 9: Tactical Master |
| 4 | 3 | 2.33 |  | Equipment > Mastery Properties |
| 5 | 8 | 1.14 |  | Equipment > Mastery Properties |
| 6 | 5 | 0.46 |  | Classes > Level 1: Weapon Mastery |
| 7 | 6 | 0.00 |  | Classes > Level 1: Weapon Mastery |
| 8 | 7 | -0.04 |  | Classes > Level 1: Weapon Mastery |
| 9 | 9 | -6.37 |  | Equipment > Properties |
| 10 | 10 | -10.01 |  | Monsters A–Z > Actions |

*retrieved sections:* Equipment > Mastery Properties | Classes > Level 9: Tactical Master

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Equipment > Mastery Properties]
**Slow.** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

---

[Classes > Level 9: Tactical Master]
#### Level 9: Tactical Master  
When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

- **Topple:** Forces the creature to make a Strength saving throw. On a failed save, the creature becomes Prone.
- **Push:** Pushes the creature up to 15 feet straight away from the attacker if it is Large or smaller.
- **Sap:** Gives the target Disadvantage on its next attack roll before the start of the attacker's next turn.
- **Slow:** Reduces the creature's Speed by 10 feet until the start of the attacker's next turn. The reduction does not exceed 10 feet if the creature is hit more than once by weapons with this property.

*facts found (judge): 6/6; missing: none*


*re-ranking* (query: `Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.02 | yes | Equipment > Mastery Properties |
| 2 | 4 | 3.06 | yes | Equipment > Mastery Properties |
| 3 | 2 | 2.87 | yes | Classes > Level 9: Tactical Master |
| 4 | 3 | 2.33 | yes | Equipment > Mastery Properties |
| 5 | 8 | 1.14 | yes | Equipment > Mastery Properties |
| 6 | 5 | 0.46 | yes | Classes > Level 1: Weapon Mastery |
| 7 | 6 | 0.00 | yes | Classes > Level 1: Weapon Mastery |
| 8 | 7 | -0.04 | yes | Classes > Level 1: Weapon Mastery |
| 9 | 9 | -6.37 |  | Equipment > Properties |
| 10 | 10 | -10.01 |  | Monsters A–Z > Actions |

*retrieved sections:* Equipment > Mastery Properties | Classes > Level 9: Tactical Master | Classes > Level 1: Weapon Mastery

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Equipment > Mastery Properties]
**Slow.** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

---

[Classes > Level 9: Tactical Master]
#### Level 9: Tactical Master  
When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack.

---

[Equipment > Mastery Properties]
**Topple.** If you hit a creature with this weapon, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.  
**Vex.** If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.  
**Weapons**  
<table>
<thead>
<tr>
<th>Name</th>

---

[Equipment > Mastery Properties]
**Cleave.** If you hit a creature with a melee attack roll using this weapon, you can make a melee attack roll with the weapon against a second creature within 5 feet of the first that is also within your reach. On a hit, the second creature takes the weapon's damage, but don't add your ability modifier to that damage unless that modifier is negative. You can make this extra attack only once per turn.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency, such as Longswords and Javelins.  
Whenever you finish a Long Rest, you can change the kinds of weapons you chose. For example, you could switch to using the mastery properties of Halberds and Flails.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of three kinds of Simple or Martial weapons of your choice. Whenever you finish a Long Rest, you can practice weapon drills and change one of those weapon choices.  
When you reach certain Fighter levels, you gain the ability to use the mastery properties of more kinds of weapons, as shown in the Weapon Mastery column of the Fighter Features table.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of two kinds of Simple or Martial Melee weapons of your choice, such as Greataxes and Handaxes. Whenever you finish a Long Rest, you can practice weapon drills and change one of those weapon choices.  
When you reach certain Barbarian levels, you gain the ability to use the mastery properties of more kinds of weapons, as shown in the Weapon Mastery column of the Barbarian Features table.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

- **Topple:** The context does not mention a "Topple" property, so this part is missing.
- **Push:** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.
- **Sap:** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.
- **Slow:** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

*facts found (judge): 4/6; missing: Strength saving throw; Prone*


*re-ranking* (query: `Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.02 | yes | Equipment > Mastery Properties |
| 2 | 4 | 3.06 | yes | Equipment > Mastery Properties |
| 3 | 2 | 2.87 | yes | Classes > Level 9: Tactical Master |
| 4 | 3 | 2.33 |  | Equipment > Mastery Properties |
| 5 | 8 | 1.14 |  | Equipment > Mastery Properties |
| 6 | 5 | 0.46 |  | Classes > Level 1: Weapon Mastery |
| 7 | 6 | 0.00 |  | Classes > Level 1: Weapon Mastery |
| 8 | 7 | -0.04 |  | Classes > Level 1: Weapon Mastery |
| 9 | 9 | -6.37 |  | Equipment > Properties |
| 10 | 10 | -10.01 |  | Monsters A–Z > Actions |

*retrieved sections:* Equipment > Mastery Properties | Classes > Level 9: Tactical Master

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Equipment > Mastery Properties]
**Slow.** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

---

[Classes > Level 9: Tactical Master]
#### Level 9: Tactical Master  
When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

- **Topple:** If you hit a creature with a weapon that has this property, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature becomes Prone.
- **Push:** If you hit a creature with a weapon that has this property, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.
- **Sap:** If you hit a creature with a weapon that has this property, that creature has Disadvantage on its next attack roll before the start of your next turn.
- **Slow:** If you hit a creature with a weapon that has this property and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons with this property, the Speed reduction doesn't exceed 10 feet.

*facts found (judge): 6/6; missing: none*


*re-ranking* (query: `Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.02 | yes | Equipment > Mastery Properties |
| 2 | 3 | 3.06 | yes | Equipment > Mastery Properties |
| 3 | 2 | 2.87 | yes | Classes > Level 9: Tactical Master |
| 4 | 5 | 2.33 | yes | Equipment > Mastery Properties |
| 5 | 9 | 1.14 | yes | Equipment > Mastery Properties |
| 6 | 8 | 0.69 | yes | Equipment > Mastery Properties |
| 7 | 7 | 0.46 | yes | Classes > Level 1: Weapon Mastery |
| 8 | 4 | 0.00 | yes | Classes > Level 1: Weapon Mastery |
| 9 | 6 | -0.04 |  | Classes > Level 1: Weapon Mastery |
| 10 | 10 | -0.33 |  | Equipment > Mastery Properties |
| 11 | 12 | -0.77 |  | Equipment > Weapons |
| 12 | 22 | -2.17 |  | Equipment > Mastery Properties |
| 13 | 15 | -2.47 |  | Equipment > Mastery Properties |
| 14 | 24 | -3.76 |  | Equipment > Mastery Properties |
| 15 | 30 | -4.12 |  | Equipment > Mastery Properties |
| 16 | 14 | -4.40 |  | Equipment > Mastery Properties |
| 17 | 18 | -4.99 |  | Equipment > Mastery Properties |
| 18 | 11 | -6.37 |  | Equipment > Properties |
| 19 | 13 | -6.60 |  | Equipment > Weapons |
| 20 | 17 | -6.75 |  | Magic Items > Sword of Sharpness |

*retrieved sections:* Equipment > Mastery Properties | Classes > Level 9: Tactical Master | Classes > Level 1: Weapon Mastery

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Equipment > Mastery Properties]
**Slow.** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

---

[Classes > Level 9: Tactical Master]
#### Level 9: Tactical Master  
When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack.

---

[Equipment > Mastery Properties]
**Topple.** If you hit a creature with this weapon, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.  
**Vex.** If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.  
**Weapons**  
<table>
<thead>
<tr>
<th>Name</th>

---

[Equipment > Mastery Properties]
**Cleave.** If you hit a creature with a melee attack roll using this weapon, you can make a melee attack roll with the weapon against a second creature within 5 feet of the first that is also within your reach. On a hit, the second creature takes the weapon's damage, but don't add your ability modifier to that damage unless that modifier is negative. You can make this extra attack only once per turn.

---

[Equipment > Mastery Properties]
### Mastery Properties  
Each weapon has a mastery property, which is usable only by a character who has a feature, such as Weapon Mastery, that unlocks the property for the character. The properties are defined below.  
> **Improvised Weapons**
>
> If you use an object—such as a table leg, frying pan, or bottle—as a makeshift weapon, see "Improvised Weapons" in "Rules Glossary." Also see those rules if you wield a weapon in an unusual way, such as using a Ranged weapon to make a melee attack.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency, such as Longswords and Javelins.  
Whenever you finish a Long Rest, you can change the kinds of weapons you chose. For example, you could switch to using the mastery properties of Halberds and Flails.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of three kinds of Simple or Martial weapons of your choice. Whenever you finish a Long Rest, you can practice weapon drills and change one of those weapon choices.  
When you reach certain Fighter levels, you gain the ability to use the mastery properties of more kinds of weapons, as shown in the Weapon Mastery column of the Fighter Features table.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

- **Topple:** If you hit a creature with a weapon that has this property, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature becomes Prone.
- **Push:** If you hit a creature with a weapon that has this property, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.
- **Sap:** If you hit a creature with a weapon that has this property, that creature has Disadvantage on its next attack roll before the start of your next turn.
- **Slow:** If you hit a creature with a weapon that has this property and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons with this property, the Speed reduction doesn't exceed 10 feet.

*facts found (judge): 6/6; missing: none*


*re-ranking* (query: `Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each`): candidate pool of 24, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.02 | yes | Equipment > Mastery Properties |
| 2 | 3 | 3.06 | yes | Equipment > Mastery Properties |
| 3 | 2 | 2.87 | yes | Classes > Level 9: Tactical Master |
| 4 | 5 | 2.33 | yes | Equipment > Mastery Properties |
| 5 | 9 | 1.14 | yes | Equipment > Mastery Properties |
| 6 | 8 | 0.69 | yes | Equipment > Mastery Properties |
| 7 | 7 | 0.46 | yes | Classes > Level 1: Weapon Mastery |
| 8 | 4 | 0.00 | yes | Classes > Level 1: Weapon Mastery |
| 9 | 6 | -0.04 |  | Classes > Level 1: Weapon Mastery |
| 10 | 10 | -0.33 |  | Equipment > Mastery Properties |
| 11 | 14 | -0.77 |  | Equipment > Weapons |
| 12 | 15 | -6.60 |  | Equipment > Weapons |
| 13 | 21 | -7.79 |  | Playing the Game > Proficiency Bonus |
| 14 | 12 | -7.97 |  | Spells > Slow |
| 15 | 11 | -8.01 |  | Spells > Slow |
| 16 | 13 | -9.37 |  | Spells > Slow |
| 17 | 19 | -10.37 |  | Playing the Game > Ability Modifier |
| 18 | 17 | -10.82 |  | Classes > Fighter |
| 19 | 23 | -10.89 |  | Rules Glossary > Prone [Condition] |
| 20 | 20 | -10.95 |  | Playing the Game > Ability Modifier |

*retrieved sections:* Equipment > Mastery Properties | Classes > Level 9: Tactical Master | Classes > Level 1: Weapon Mastery

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Equipment > Mastery Properties]
**Slow.** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

---

[Classes > Level 9: Tactical Master]
#### Level 9: Tactical Master  
When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack.

---

[Equipment > Mastery Properties]
**Topple.** If you hit a creature with this weapon, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.  
**Vex.** If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.  
**Weapons**  
<table>
<thead>
<tr>
<th>Name</th>

---

[Equipment > Mastery Properties]
**Cleave.** If you hit a creature with a melee attack roll using this weapon, you can make a melee attack roll with the weapon against a second creature within 5 feet of the first that is also within your reach. On a hit, the second creature takes the weapon's damage, but don't add your ability modifier to that damage unless that modifier is negative. You can make this extra attack only once per turn.

---

[Equipment > Mastery Properties]
### Mastery Properties  
Each weapon has a mastery property, which is usable only by a character who has a feature, such as Weapon Mastery, that unlocks the property for the character. The properties are defined below.  
> **Improvised Weapons**
>
> If you use an object—such as a table leg, frying pan, or bottle—as a makeshift weapon, see "Improvised Weapons" in "Rules Glossary." Also see those rules if you wield a weapon in an unusual way, such as using a Ranged weapon to make a melee attack.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency, such as Longswords and Javelins.  
Whenever you finish a Long Rest, you can change the kinds of weapons you chose. For example, you could switch to using the mastery properties of Halberds and Flails.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of three kinds of Simple or Martial weapons of your choice. Whenever you finish a Long Rest, you can practice weapon drills and change one of those weapon choices.  
When you reach certain Fighter levels, you gain the ability to use the mastery properties of more kinds of weapons, as shown in the Weapon Mastery column of the Fighter Features table.
```
</details>


### v6_agentic  (15 chunks, 3 LLM call(s))

Sure, here are the descriptions of the weapon mastery properties Topple, Push, Sap, and Slow:

- **Topple**: When you hit a creature with this weapon, the target must succeed on a Dexterity saving throw or become Prone.
- **Push**: When you hit a creature with this weapon and deal damage to it, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.
- **Sap**: When you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.
- **Slow**: When you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons with this property, the Speed reduction doesn't exceed 10 feet.

*facts found (judge): 5/6; missing: Strength saving throw*

*agentic sub-queries:* Topple / Push / Sap / Slow


*re-ranking* (query: `Topple`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 1.42 | yes | Gameplay Toolbox > Collapsing Roof |
| 2 | 8 | 0.72 | yes | Equipment > Mastery Properties |
| 3 | 6 | -0.57 | yes | Classes > Level 3: Open Hand Technique |
| 4 | 18 | -0.78 |  | Equipment > Mastery Properties |
| 5 | 14 | -1.98 |  | Equipment > Mastery Properties |
| 6 | 16 | -2.31 | yes | Equipment > Mastery Properties |
| 7 | 12 | -3.10 |  | Equipment > Mastery Properties |
| 8 | 2 | -3.46 |  | Gameplay Toolbox > Collapsing Roof |
| 9 | 10 | -10.18 |  | Equipment > Mastery Properties |
| 10 | 9 | -10.19 |  | Animals > Ankylosaurus |
| 11 | 20 | -10.22 |  | Animals > Giant Hyena |
| 12 | 7 | -10.23 |  | Animals > Giant Goat |
| 13 | 13 | -10.24 |  | Animals > Triceratops |
| 14 | 19 | -10.25 |  | Monsters A–Z > Gladiator |
| 15 | 11 | -10.32 |  | Monsters A–Z > Cockatrice |
| 16 | 3 | -10.37 |  | Monsters A–Z > Shambling Mound |
| 17 | 15 | -10.39 |  | Monsters A–Z > Succubus |
| 18 | 17 | -10.89 |  | Feats > Boon of Combat Prowess |
| 19 | 5 | -10.92 |  | Feats > Ability Score Improvement |
| 20 | 1 | -11.13 |  | Feats > Feat Descriptions |


*re-ranking* (query: `Push`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | 2.54 | yes | Equipment > Mastery Properties |
| 2 | 4 | 1.37 | yes | Spells > Arcane Hand |
| 3 | 3 | 0.51 | yes | Classes > Level 2: Action Surge |
| 4 | 9 | 0.43 |  | Playing the Game > Ability Modifier |
| 5 | 5 | 0.17 | yes | Classes > Level 3: Open Hand Technique |
| 6 | 10 | -1.15 |  | Rules Glossary > Carrying Capacity |
| 7 | 2 | -1.56 |  | Rules Glossary > Unarmed Strike |
| 8 | 6 | -1.70 |  | Magic Items > Rod of Lordly Might |
| 9 | 15 | -1.85 |  | Magic Items > Bead of Force |
| 10 | 18 | -2.49 |  | Gameplay Toolbox > Extended Travel |
| 11 | 1 | -2.62 | yes | Classes > Level 9: Tactical Master |
| 12 | 20 | -3.88 |  | Spells > Resilient Sphere |
| 13 | 16 | -4.55 |  | Playing the Game > Adventuring Equipment |
| 14 | 13 | -4.93 |  | Classes > Monk Subclass: Warrior of the Open Hand |
| 15 | 19 | -8.81 |  | Rules Glossary > Ready [Action] |
| 16 | 8 | -9.13 |  | Playing the Game > Your Turn |
| 17 | 11 | -9.51 |  | Animals > Actions |
| 18 | 17 | -9.51 |  | Monsters A–Z > Actions |
| 19 | 12 | -9.59 |  | Monsters A–Z > Actions |
| 20 | 14 | -9.71 |  | Animals > Actions |


*re-ranking* (query: `Sap`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | -1.22 | yes | Equipment > Mastery Properties |
| 2 | 10 | -1.52 | yes | Equipment > Mastery Properties |
| 3 | 4 | -1.72 | yes | Equipment > Mastery Properties |
| 4 | 18 | -1.89 |  | Equipment > Mastery Properties |
| 5 | 14 | -2.98 |  | Equipment > Mastery Properties |
| 6 | 16 | -3.24 |  | Equipment > Mastery Properties |
| 7 | 2 | -3.37 | yes | Classes > Level 9: Tactical Master |
| 8 | 8 | -3.38 |  | Classes > Level 3: Cutting Words |
| 9 | 12 | -4.99 |  | Equipment > Mastery Properties |
| 10 | 1 | -10.36 |  | Spells > Geas |
| 11 | 9 | -10.46 |  | Monsters A–Z > Invisible Stalker |
| 12 | 5 | -10.47 |  | Monsters A–Z > Will-o'-Wisp |
| 13 | 19 | -10.59 |  | Monsters A–Z > Sphinx of Valor |
| 14 | 15 | -10.65 |  | Monsters A–Z > Imp |
| 15 | 17 | -10.70 |  | Monsters A–Z > Chain Devil |
| 16 | 20 | -10.76 |  | Monsters A–Z > Succubus |
| 17 | 11 | -10.78 |  | Monsters A–Z > Unicorn |
| 18 | 7 | -10.81 |  | Monsters A–Z > Deva |
| 19 | 3 | -10.92 |  | Monsters A–Z > Spy |
| 20 | 13 | -10.98 |  | Monsters A–Z > Druid |


*re-ranking* (query: `Slow`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 9 | 2.78 | yes | Spells > Slow |
| 2 | 2 | 2.36 | yes | Gameplay Toolbox > Slower Travelers |
| 3 | 7 | 2.13 | yes | Spells > Slow |
| 4 | 1 | 2.08 |  | Spells > Slow |
| 5 | 12 | 1.78 |  | Classes > Level 4: Slow Fall |
| 6 | 11 | 1.68 |  | Monsters A–Z > Bonus Actions |
| 7 | 4 | 1.20 |  | Gameplay Toolbox > Rolling Stone |
| 8 | 5 | -0.22 |  | Playing the Game > Travel Pace |
| 9 | 8 | -0.25 |  | Playing the Game > Travel Pace |
| 10 | 6 | -0.46 |  | Gameplay Toolbox > Travel Pace |
| 11 | 16 | -1.01 | yes | Equipment > Mastery Properties |
| 12 | 3 | -1.76 |  | Gameplay Toolbox > Good Roads |
| 13 | 20 | -1.88 |  | Gameplay Toolbox > Vehicles |
| 14 | 18 | -3.12 | yes | Classes > Level 9: Tactical Master |
| 15 | 10 | -3.81 |  | Playing the Game > Travel Pace |
| 16 | 19 | -7.26 |  | Gameplay Toolbox > Special Movement |
| 17 | 13 | -8.01 |  | Character Origins > Speed |
| 18 | 17 | -10.18 |  | Playing the Game > Travel Pace |
| 19 | 15 | -10.33 |  | Playing the Game > Travel |
| 20 | 14 | -11.04 |  | Playing the Game > Travel Pace |


*re-ranking* (query: `Slow (mastery property)`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.45 | yes | Equipment > Mastery Properties |
| 2 | 2 | 4.67 | yes | Classes > Level 9: Tactical Master |
| 3 | 18 | 3.79 | yes | Equipment > Mastery Properties |
| 4 | 19 | 2.71 |  | Equipment > Mastery Properties |
| 5 | 6 | 2.21 |  | Equipment > Mastery Properties |
| 6 | 17 | 1.74 | yes | Equipment > Weapons |
| 7 | 10 | 1.15 | yes | Equipment > Mastery Properties |
| 8 | 7 | 0.94 |  | Equipment > Mastery Properties |
| 9 | 20 | 0.43 |  | Equipment > Mastery Properties |
| 10 | 3 | -0.38 |  | Classes > Level 1: Weapon Mastery |
| 11 | 5 | -0.93 |  | Classes > Level 1: Weapon Mastery |
| 12 | 4 | -1.07 |  | Classes > Level 1: Weapon Mastery |
| 13 | 9 | -6.28 |  | Spells > Slow |
| 14 | 13 | -6.62 | yes | Spells > Slow |
| 15 | 14 | -6.74 |  | Magic Items > Ioun Stone |
| 16 | 15 | -7.41 |  | Gameplay Toolbox > Rolling Stone |
| 17 | 8 | -8.08 |  | Classes > Level 18: Spell Mastery |
| 18 | 11 | -8.41 | yes | Gameplay Toolbox > Slower Travelers |
| 19 | 12 | -10.06 |  | Magic Items > Rod of Rulership |
| 20 | 16 | -11.09 |  | Classes > Level 13: Use Magic Device |


*re-ranking* (query: `Sap (mastery property)`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 4.41 | yes | Equipment > Mastery Properties |
| 2 | 1 | 3.77 | yes | Classes > Level 9: Tactical Master |
| 3 | 4 | 3.32 | yes | Equipment > Weapons |
| 4 | 18 | 3.26 | yes | Equipment > Mastery Properties |
| 5 | 3 | 3.14 |  | Equipment > Mastery Properties |
| 6 | 11 | 2.83 | yes | Equipment > Mastery Properties |
| 7 | 14 | 2.51 |  | Equipment > Mastery Properties |
| 8 | 19 | 2.51 |  | Equipment > Mastery Properties |
| 9 | 20 | 2.19 |  | Equipment > Mastery Properties |
| 10 | 15 | 1.13 |  | Equipment > Mastery Properties |
| 11 | 9 | 0.63 |  | Equipment > Mastery Properties |
| 12 | 6 | -0.17 | yes | Equipment > Mastery Properties |
| 13 | 13 | -0.48 |  | Equipment > Mastery Properties |
| 14 | 5 | -0.55 |  | Classes > Level 1: Weapon Mastery |
| 15 | 17 | -0.61 | yes | Equipment > Mastery Properties |
| 16 | 8 | -1.12 |  | Classes > Level 1: Weapon Mastery |
| 17 | 7 | -1.27 |  | Classes > Level 1: Weapon Mastery |
| 18 | 10 | -8.81 |  | Classes > Level 18: Spell Mastery |
| 19 | 16 | -10.45 |  | Classes > Rogue Class Features |
| 20 | 12 | -10.47 |  | Magic Items > Rod of Rulership |

*retrieved sections:* Gameplay Toolbox > Collapsing Roof | Equipment > Mastery Properties | Classes > Level 3: Open Hand Technique | Spells > Arcane Hand | Classes > Level 2: Action Surge | Spells > Slow | Gameplay Toolbox > Slower Travelers | Classes > Level 9: Tactical Master | Equipment > Weapons

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Collapsing Roof]
The first creature that crosses the trip wire causes the supports to topple and the unstable section of ceiling to collapse. Each creature beneath the unstable section of ceiling must succeed on a DC 13 Dexterity saving throw, taking 11 (2d10) Bludgeoning damage on a failed save or half as much damage on a successful one. Rubble from the collapse turns the trapped area into Difficult Terrain.

---

[Equipment > Mastery Properties]
**Topple.** If you hit a creature with this weapon, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.  
**Vex.** If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.  
**Weapons**  
<table>
<thead>
<tr>
<th>Name</th>

---

[Classes > Level 3: Open Hand Technique]
#### Level 3: Open Hand Technique  
Whenever you hit a creature with an attack granted by your Flurry of Blows, you can impose one of the following effects on that target.  
**Addle.** The target can't make Opportunity Attacks until the start of its next turn.  
**Push.** The target must succeed on a Strength saving throw or be pushed up to 15 feet away from you.  
**Topple.** The target must succeed on a Dexterity saving throw or have the Prone condition.

---

[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Spells > Arcane Hand]
**Forceful Hand.** The hand attempts to push a Huge or smaller creature within 5 feet of it. The target must succeed on a Strength saving throw, or the hand pushes the target up to 5 feet plus a number of feet equal to five times your spellcasting ability modifier. The hand moves with the target, remaining within 5 feet of it.

---

[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Equipment > Mastery Properties]
<td>Sap</td>
<td>3 lb.</td>
<td>1 GP</td>
</tr>
<tr>
<th colspan="6"><em>Simple Ranged Weapons</em></th>
</tr>
<tr>
<td>Dart</td>
<td>1d4 Piercing</td>
<td>Finesse, Thrown (Range 20/60)</td>
<td>Vex</td>
<td>1/4 lb.</td>
<td>5 CP</td>
</tr>
<tr>
<td>Light Crossbow</td>
<td>1d8 Piercing</td>
<td>Ammunition (Range 80/320; Bolt), Loading, Two-Handed</td>
<td>Slow</td>
<td>5 lb.</td>
<td>25 GP</td>
</tr>
<tr>
<td>Shortbow</td>
<td>1d6 Piercing</td>

---

[Equipment > Mastery Properties]
<td>Nick</td>
<td>2 lb.</td>
<td>2 GP</td>
</tr>
<tr>
<td>Mace</td>
<td>1d6 Bludgeoning</td>
<td>—</td>
<td>Sap</td>
<td>4 lb.</td>
<td>5 GP</td>
</tr>
<tr>
<td>Quarterstaff</td>
<td>1d6 Bludgeoning</td>
<td>Versatile (1d8)</td>
<td>Topple</td>
<td>4 lb.</td>
<td>2 SP</td>
</tr>
<tr>
<td>Sickle</td>
<td>1d4 Slashing</td>
<td>Light</td>
<td>Nick</td>
<td>2 lb.</td>
<td>1 GP</td>
</tr>
<tr>
<td>Spear</td>
<td>1d6 Piercing</td>
<td>Thrown (Range 20/60), Versatile (1d8)</td>
<td>Sap</td>

---

[Spells > Slow]
An affected target repeats the save at the end of each of its turns, ending the spell on itself on a success.

---

[Gameplay Toolbox > Slower Travelers]
### Slower Travelers  
The group must move at a Slow pace if any group member's Speed is reduced to half or less of normal.

---

[Spells > Slow]
An affected target's Speed is halved, it takes a −2 penalty to AC and Dexterity saving throws, and it can't take Reactions. On its turns, it can take either an action or a Bonus Action, not both, and it can make only one attack if it takes the Attack action. If it casts a spell with a Somatic component, there is a 25 percent chance the spell fails as a result of the target making the spell's gestures too slowly.

---

[Equipment > Mastery Properties]
**Slow.** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

---

[Classes > Level 9: Tactical Master]
#### Level 9: Tactical Master  
When you attack with a weapon whose mastery property you can use, you can replace that property with the Push, Sap, or Slow property for that attack.

---

[Equipment > Mastery Properties]
<td>Slow</td>
<td>2 lb.</td>
<td>50 GP</td>
</tr>
<tr>
<td>Musket</td>
<td>1d12 Piercing</td>
<td>Ammunition (Range 40/120; Bullet), Loading, Two-Handed</td>
<td>Slow</td>
<td>10 lb.</td>
<td>500 GP</td>
</tr>
<tr>
<td>Pistol</td>
<td>1d10 Piercing</td>
<td>Ammunition (Range 30/90; Bullet), Loading</td>
<td>Vex</td>
<td>3 lb.</td>
<td>250 GP</td>
</tr>
</tbody>
</table>

---

[Equipment > Weapons]
**Mastery.** Each weapon has a mastery property, which is defined in the "Mastery Properties" section. To use that property, you must have a feature that lets you use it.  
> **Selling Equipment**
>
> Equipment fetches half its cost when sold. In contrast, trade goods and valuables—like gems and art objects—retain their full value in the marketplace. "Magic Items" has prices for magic items.
```
</details>


---

## q10 (cross-file) What does the Fighter's Action Surge give you and when does it recharge, at what level can it be used twice? And how does a Barbarian enter Rage, what armor prevents it, and how are Rage uses regained on a Short Rest?

**Gold facts (counterfactual data):** one additional action, except the Magic action; Short or Long Rest; level 15; Bonus Action; Heavy armor; one expended use when you finish a Short Rest


### v0_closed_book  (0 chunks, 1 LLM call(s))

The Action Surge feature for a Fighter allows you to take one additional action on your turn. This feature recharges after a short rest. A Fighter can use Action Surge once at 2nd level, and then again at 6th level.

A Barbarian enters Rage by taking the Rage action on their turn or by being reduced to 0 hit points. Rage lasts for 1 minute, and can be ended early as a bonus action. Certain effects can also end rage early. 

Barbarians are generally not prevented from entering rage by any armor type, as they can wear any type of armor without penalty. However, some specific class features or magic items might prevent or hinder entering rage in rare cases.

On a short rest, a Barbarian regains the ability to enter rage, effectively "resetting" their rage uses for the day. They can use the Rage feature multiple times between long rests, but only once per short rest.

*facts found (judge): 1/6; missing: one additional action, except the Magic action; Short or Long Rest; level 15; Heavy armor; one expended use when you finish a Short Rest*


### v1_baseline  (3 chunks, 1 LLM call(s))

The provided context does not contain information about the Fighter's Action Surge or the number of times a Barbarian can use Rage. The context only covers how a Barbarian enters Rage, the types of armor that prevent entering Rage, and how Rage uses are regained on a Short Rest. 

- A Barbarian can enter Rage as a Bonus Action if they are not wearing Heavy armor.
- Heavy armor prevents entering Rage.
- Rage uses are regained on a Short Rest.

*facts found (judge): 2/6; missing: one additional action, except the Magic action; Short or Long Rest; level 15; one expended use when you finish a Short Rest*

*retrieved sections:* Classes > Level 1: Rage

<details><summary>full retrieved context</summary>

```
[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 1: Rage]
While active, your Rage follows the rules below.  
_Damage Resistance._ You have Resistance to Bludgeoning, Piercing, and Slashing damage.  
_Rage Damage._ When you make an attack using Strength—with either a weapon or an Unarmed Strike—and deal damage to the target, you gain a bonus to the damage that increases as you gain levels as a Barbarian, as shown in the Rage Damage column of the Barbarian Features table.

---

[Classes > Level 1: Rage]
- Make an attack roll against an enemy.
- Force an enemy to make a saving throw.
- Take a Bonus Action to extend your Rage.  
Each time the Rage is extended, it lasts until the end of your next turn. You can maintain a Rage for up to 10 minutes.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The Fighter's Action Surge allows you to take one additional action on your turn (except the Magic action) and recharges after a Short or Long Rest. A Fighter can use Action Surge twice starting at level 15.

A Barbarian enters Rage as a Bonus Action if they are not wearing Heavy armor. Rage uses recharge after a Short Rest, and all uses are regained after a Long Rest.

*facts found (judge): 5/6; missing: one expended use when you finish a Short Rest*


*re-ranking* (query: `What does the Fighter's Action Surge give you and when does it recharge, at what`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 9 | 1.24 | yes | Classes > Level 2: Action Surge |
| 2 | 7 | 1.10 | yes | Classes > Level 1: Second Wind |
| 3 | 1 | -1.67 | yes | Classes > Level 1: Rage |
| 4 | 6 | -2.73 |  | Classes > Level 11: Relentless Rage |
| 5 | 4 | -4.27 |  | Classes > Level 15: Persistent Rage |
| 6 | 8 | -5.09 |  | Classes > Fighter Class Features |
| 7 | 3 | -5.66 |  | Classes > Level 1: Rage |
| 8 | 10 | -5.74 |  | Classes > Level 14: Intimidating Presence |
| 9 | 2 | -6.20 |  | Classes > Level 1: Rage |
| 10 | 5 | -7.09 |  | Classes > Level 1: Rage |

*retrieved sections:* Classes > Level 2: Action Surge | Classes > Level 1: Second Wind | Classes > Level 1: Rage

<details><summary>full retrieved context</summary>

```
[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Classes > Level 1: Second Wind]
#### Level 1: Second Wind  
You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.  
You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.  
When you reach certain Fighter levels, you gain more uses of this feature, as shown in the Second Wind column of the Fighter Features table.

---

[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The Fighter's Action Surge allows you to take one additional action on your turn, except the Magic action. It recharges after a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

A Barbarian enters Rage as a Bonus Action if they aren't wearing Heavy armor. They can enter their Rage the number of times shown for their level in the Rages column of the Barbarian Features table. Rage uses are regained on a Short Rest.

The context does not specify the exact number of times a Barbarian can enter Rage, nor the specific levels at which they gain additional uses of Rage. Additionally, the context does not provide information on how many uses of Rage a Barbarian has at different levels.

*facts found (judge): 5/6; missing: one expended use when you finish a Short Rest*


*re-ranking* (query: `What does the Fighter's Action Surge give you and when does it recharge, at what`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 9 | 1.24 | yes | Classes > Level 2: Action Surge |
| 2 | 7 | 1.10 | yes | Classes > Level 1: Second Wind |
| 3 | 1 | -1.67 | yes | Classes > Level 1: Rage |
| 4 | 6 | -2.73 | yes | Classes > Level 11: Relentless Rage |
| 5 | 4 | -4.27 | yes | Classes > Level 15: Persistent Rage |
| 6 | 8 | -5.09 | yes | Classes > Fighter Class Features |
| 7 | 3 | -5.66 | yes | Classes > Level 1: Rage |
| 8 | 10 | -5.74 | yes | Classes > Level 14: Intimidating Presence |
| 9 | 2 | -6.20 |  | Classes > Level 1: Rage |
| 10 | 5 | -7.09 |  | Classes > Level 1: Rage |

*retrieved sections:* Classes > Level 2: Action Surge | Classes > Level 1: Second Wind | Classes > Level 1: Rage | Classes > Level 11: Relentless Rage | Classes > Level 15: Persistent Rage | Classes > Fighter Class Features | Classes > Level 14: Intimidating Presence

<details><summary>full retrieved context</summary>

```
[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Classes > Level 1: Second Wind]
#### Level 1: Second Wind  
You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.  
You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.  
When you reach certain Fighter levels, you gain more uses of this feature, as shown in the Second Wind column of the Fighter Features table.

---

[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 11: Relentless Rage]
#### Level 11: Relentless Rage  
Your Rage can keep you fighting despite grievous wounds. If you drop to 0 Hit Points while your Rage is active and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, your Hit Points instead change to a number equal to twice your Barbarian level.  
Each time you use this feature after the first, the DC increases by 5. When you finish a Short or Long Rest, the DC resets to 10.

---

[Classes > Level 15: Persistent Rage]
#### Level 15: Persistent Rage  
When you roll Initiative, you can regain all expended uses of Rage. After you regain uses of Rage in this way, you can't do so again until you finish a Long Rest.  
In addition, your Rage is so fierce that it now lasts for 10 minutes without you needing to do anything to extend it from round to round. Your Rage ends early if you have the Unconscious condition (not just the Incapacitated condition) or don Heavy armor.

---

[Classes > Fighter Class Features]
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>17</td>
<td>+6</td>
<td>Action Surge (two uses), Indomitable (three uses)</td>
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>18</td>
<td>+6</td>
<td>Subclass feature</td>
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>19</td>
<td>+6</td>
<td>Epic Boon</td>
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>20</td>
<td>+6</td>
<td>Three Extra Attacks</td>
<td>4</td>
<td>6</td>
</tr>
</tbody>
</table>

---

[Classes > Level 1: Rage]
- Make an attack roll against an enemy.
- Force an enemy to make a saving throw.
- Take a Bonus Action to extend your Rage.  
Each time the Rage is extended, it lasts until the end of your next turn. You can maintain a Rage for up to 10 minutes.

---

[Classes > Level 14: Intimidating Presence]
Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a use of your Rage (no action required) to restore your use of it.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The Fighter's Action Surge allows you to take one additional action on your turn (except the Magic action) and recharges after a Short or Long Rest. A Fighter can use Action Surge twice starting at level 15.

A Barbarian enters Rage as a Bonus Action if they are not wearing Heavy armor. Rage uses recharge after a Short Rest, and all uses are regained after a Long Rest.

*facts found (judge): 5/6; missing: one expended use when you finish a Short Rest*


*re-ranking* (query: `What does the Fighter's Action Surge give you and when does it recharge, at what`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 9 | 1.24 | yes | Classes > Level 2: Action Surge |
| 2 | 7 | 1.10 | yes | Classes > Level 1: Second Wind |
| 3 | 1 | -1.67 | yes | Classes > Level 1: Rage |
| 4 | 6 | -2.73 |  | Classes > Level 11: Relentless Rage |
| 5 | 4 | -4.27 |  | Classes > Level 15: Persistent Rage |
| 6 | 8 | -5.09 |  | Classes > Fighter Class Features |
| 7 | 3 | -5.66 |  | Classes > Level 1: Rage |
| 8 | 10 | -5.74 |  | Classes > Level 14: Intimidating Presence |
| 9 | 2 | -6.20 |  | Classes > Level 1: Rage |
| 10 | 5 | -7.09 |  | Classes > Level 1: Rage |

*retrieved sections:* Classes > Level 2: Action Surge | Classes > Level 1: Second Wind | Classes > Level 1: Rage

<details><summary>full retrieved context</summary>

```
[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Classes > Level 1: Second Wind]
#### Level 1: Second Wind  
You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.  
You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.  
When you reach certain Fighter levels, you gain more uses of this feature, as shown in the Second Wind column of the Fighter Features table.

---

[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

Action Surge allows a Fighter to take one additional action on their turn, except the Magic action. It recharges after a Short or Long Rest. A Fighter can use it twice starting at level 15.

A Barbarian can enter Rage as a Bonus Action if they are not wearing Heavy armor. They can enter Rage the number of times shown for their level in the Rages column of the Barbarian Features table. Rage uses are regained on a Short Rest.

*facts found (judge): 5/6; missing: one expended use when you finish a Short Rest*


*re-ranking* (query: `What does the Fighter's Action Surge give you and when does it recharge, at what`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 1.24 | yes | Classes > Level 2: Action Surge |
| 2 | 2 | 1.10 | yes | Classes > Level 1: Second Wind |
| 3 | 1 | -1.67 | yes | Classes > Level 1: Rage |
| 4 | 3 | -2.73 | yes | Classes > Level 11: Relentless Rage |
| 5 | 25 | -3.01 | yes | Classes > Level 9: Indomitable |
| 6 | 11 | -3.04 | yes | Monsters > Limited Usage |
| 7 | 18 | -3.50 | yes | Classes > Level 3: Channel Divinity |
| 8 | 10 | -3.96 | yes | Classes > Level 6: Wholeness of Body |
| 9 | 5 | -4.27 |  | Classes > Level 15: Persistent Rage |
| 10 | 21 | -4.68 |  | Classes > Level 2: Channel Divinity |
| 11 | 19 | -4.73 |  | Classes > Level 2: Wild Shape |
| 12 | 20 | -5.09 |  | Classes > Fighter Class Features |
| 13 | 15 | -5.32 |  | Monsters > Limited Usage |
| 14 | 17 | -5.66 |  | Classes > Level 1: Rage |
| 15 | 13 | -5.74 |  | Classes > Level 14: Intimidating Presence |
| 16 | 6 | -6.20 |  | Classes > Level 1: Rage |
| 17 | 12 | -6.35 |  | Classes > Level 7: Instinctive Pounce |
| 18 | 16 | -6.57 |  | Rules Glossary > Long Rest |
| 19 | 8 | -7.09 |  | Classes > Level 1: Rage |
| 20 | 26 | -7.18 |  | Classes > Level 3: Frenzy |

*retrieved sections:* Classes > Level 2: Action Surge | Classes > Level 1: Second Wind | Classes > Level 1: Rage | Classes > Level 11: Relentless Rage | Classes > Level 9: Indomitable | Monsters > Limited Usage | Classes > Level 3: Channel Divinity | Classes > Level 6: Wholeness of Body

<details><summary>full retrieved context</summary>

```
[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Classes > Level 1: Second Wind]
#### Level 1: Second Wind  
You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.  
You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.  
When you reach certain Fighter levels, you gain more uses of this feature, as shown in the Second Wind column of the Fighter Features table.

---

[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 11: Relentless Rage]
#### Level 11: Relentless Rage  
Your Rage can keep you fighting despite grievous wounds. If you drop to 0 Hit Points while your Rage is active and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, your Hit Points instead change to a number equal to twice your Barbarian level.  
Each time you use this feature after the first, the DC increases by 5. When you finish a Short or Long Rest, the DC resets to 10.

---

[Classes > Level 9: Indomitable]
#### Level 9: Indomitable  
If you fail a saving throw, you can reroll it with a bonus equal to your Fighter level. You must use the new roll, and you can't use this feature again until you finish a Long Rest.  
You can use this feature twice before a Long Rest starting at level 13 and three times before a Long Rest starting at level 17.

---

[Monsters > Limited Usage]
**Recharge X–Y.** This notation means a monster can use the stat block part once. At the start of each of the monster's turns, roll 1d6. If the roll is within the number range given in the notation (represented by X–Y), the monster regains the use of that part, which also recharges when the monster finishes a Short or Long Rest. For example, "Recharge 5–6" in an action means a monster can take the action once. Then, at the start of each of the monster's turns, it regains the use of that action

---

[Classes > Level 3: Channel Divinity]
You can use this class's Channel Divinity twice. You regain one of its expended uses when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest. You gain an additional use when you reach Paladin level 11.  
> ### Breaking Your Oath
>
> A Paladin tries to hold to the highest standards of conduct, but even the most dedicated are fallible. Sometimes a Paladin transgresses their oath.
>

---

[Classes > Level 6: Wholeness of Body]
#### Level 6: Wholeness of Body  
You gain the ability to heal yourself. As a Bonus Action, you can roll your Martial Arts die. You regain a number of Hit Points equal to the number rolled plus your Wisdom modifier (minimum of 1 Hit Point regained).  
You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The Fighter's Action Surge allows you to take one additional action on your turn, except the Magic action. It recharges after a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

A Barbarian enters Rage as a Bonus Action if they are not wearing Heavy armor. They can enter their Rage the number of times shown for their level in the Rages column of the Barbarian Features table. Rage uses are regained on a Short Rest.

The context provided does not specify the exact number of times a Barbarian can enter Rage or the specific levels at which they can use it twice. Additionally, the context does not provide the exact wording for entering Rage or the specific levels for regaining Rage uses on a Short Rest.

*facts found (judge): 5/6; missing: one expended use when you finish a Short Rest*


*re-ranking* (query: `What does the Fighter's Action Surge give you and when does it recharge, at what`): candidate pool of 25, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 1.24 | yes | Classes > Level 2: Action Surge |
| 2 | 2 | 1.10 | yes | Classes > Level 1: Second Wind |
| 3 | 1 | -1.67 | yes | Classes > Level 1: Rage |
| 4 | 3 | -2.73 | yes | Classes > Level 11: Relentless Rage |
| 5 | 10 | -3.96 | yes | Classes > Level 6: Wholeness of Body |
| 6 | 5 | -4.27 | yes | Classes > Level 15: Persistent Rage |
| 7 | 6 | -6.20 | yes | Classes > Level 1: Rage |
| 8 | 18 | -6.59 | yes | Rules Glossary > Short Rest |
| 9 | 8 | -7.09 |  | Classes > Level 1: Rage |
| 10 | 7 | -8.45 |  | Classes > Barbarian Class Features |
| 11 | 9 | -8.56 |  | Classes > Level 3: Fighter Subclass |
| 12 | 11 | -9.38 |  | Classes > Fighter |
| 13 | 17 | -9.68 |  | Equipment > Armor |
| 14 | 13 | -9.76 |  | Classes > Barbarian |
| 15 | 12 | -9.81 |  | Classes > Fighter |
| 16 | 14 | -9.88 |  | Classes > Barbarian |
| 17 | 21 | -10.19 |  | Playing the Game > Your Turn |
| 18 | 24 | -10.41 |  | Rules Glossary > Unconscious [Condition] |
| 19 | 15 | -10.42 |  | Equipment > Armor |
| 20 | 22 | -10.44 |  | Playing the Game > Your Turn |

*retrieved sections:* Classes > Level 2: Action Surge | Classes > Level 1: Second Wind | Classes > Level 1: Rage | Classes > Level 11: Relentless Rage | Classes > Level 6: Wholeness of Body | Classes > Level 15: Persistent Rage | Rules Glossary > Short Rest

<details><summary>full retrieved context</summary>

```
[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Classes > Level 1: Second Wind]
#### Level 1: Second Wind  
You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.  
You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.  
When you reach certain Fighter levels, you gain more uses of this feature, as shown in the Second Wind column of the Fighter Features table.

---

[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 11: Relentless Rage]
#### Level 11: Relentless Rage  
Your Rage can keep you fighting despite grievous wounds. If you drop to 0 Hit Points while your Rage is active and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, your Hit Points instead change to a number equal to twice your Barbarian level.  
Each time you use this feature after the first, the DC increases by 5. When you finish a Short or Long Rest, the DC resets to 10.

---

[Classes > Level 6: Wholeness of Body]
#### Level 6: Wholeness of Body  
You gain the ability to heal yourself. As a Bonus Action, you can roll your Martial Arts die. You regain a number of Hit Points equal to the number rolled plus your Wisdom modifier (minimum of 1 Hit Point regained).  
You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 15: Persistent Rage]
#### Level 15: Persistent Rage  
When you roll Initiative, you can regain all expended uses of Rage. After you regain uses of Rage in this way, you can't do so again until you finish a Long Rest.  
In addition, your Rage is so fierce that it now lasts for 10 minutes without you needing to do anything to extend it from round to round. Your Rage ends early if you have the Unconscious condition (not just the Incapacitated condition) or don Heavy armor.

---

[Classes > Level 1: Rage]
While active, your Rage follows the rules below.  
_Damage Resistance._ You have Resistance to Bludgeoning, Piercing, and Slashing damage.  
_Rage Damage._ When you make an attack using Strength—with either a weapon or an Unarmed Strike—and deal damage to the target, you gain a bonus to the damage that increases as you gain levels as a Barbarian, as shown in the Rage Damage column of the Barbarian Features table.

---

[Rules Glossary > Short Rest]
**Spend Hit Point Dice.** You can spend one or more of your Hit Point Dice to regain Hit Points. For each Hit Point Die you spend in this way, roll the die and add your Constitution modifier to it. You regain Hit Points equal to the total (minimum of 1 Hit Point). You can decide to spend an additional Hit Point Die after each roll.  
**Special Feature.** Some features are recharged by a Short Rest. If you have such a feature, it recharges in the way specified in its description.
```
</details>


### v6_agentic  (14 chunks, 3 LLM call(s))

The Fighter's Action Surge allows you to take one additional action on your turn, except the Magic action. It recharges after a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

A Barbarian enters Rage as a Bonus Action if they aren't wearing Heavy armor. Armor of Vulnerability prevents a Barbarian from entering Rage if worn. Rage uses are regained when you finish a Short Rest.

*facts found (judge): 5/6; missing: one expended use when you finish a Short Rest*

*agentic sub-queries:* Action Surge / Fighter / Barbarian Rage / Armor Types / Rage Uses Regained


*re-ranking* (query: `Action Surge`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 7.73 | yes | Classes > Level 2: Action Surge |
| 2 | 6 | 1.65 | yes | Classes > Fighter Class Features |
| 3 | 8 | 1.26 | yes | Classes > Fighter Class Features |
| 4 | 1 | -6.16 |  | Rules Glossary > Action |
| 5 | 3 | -6.53 |  | Monsters A–Z > Actions |
| 6 | 9 | -6.72 |  | Rules Glossary > Bonus Action |
| 7 | 10 | -7.16 |  | Monsters A–Z > Actions |
| 8 | 7 | -7.27 |  | Monsters A–Z > Actions |
| 9 | 13 | -7.34 |  | Playing the Game > Bonus Actions |
| 10 | 14 | -7.36 |  | Monsters A–Z > Actions |
| 11 | 17 | -7.45 |  | Rules Glossary > Disengage [Action] |
| 12 | 5 | -7.77 |  | Monsters A–Z > Legendary Actions |
| 13 | 15 | -7.93 |  | Rules Glossary > Attack [Action] |
| 14 | 2 | -8.00 |  | Monsters A–Z > Bonus Actions |
| 15 | 16 | -8.15 |  | Rules Glossary > Attack [Action] |
| 16 | 12 | -8.15 |  | Monsters A–Z > Actions |
| 17 | 20 | -8.40 |  | Playing the Game > Bonus Actions |
| 18 | 19 | -8.50 |  | Spells > Expeditious Retreat |
| 19 | 18 | -9.06 |  | Monsters > Bonus Action |
| 20 | 11 | -9.30 |  | Rules Glossary > Utilize [Action] |


*re-ranking* (query: `Fighter`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 3.85 | yes | Classes > Fighter Class Features |
| 2 | 10 | 3.22 | yes | Classes > As a Multiclass Character |
| 3 | 2 | 3.21 | yes | Classes > As a Level 1 Character |
| 4 | 4 | 2.97 |  | Classes > Level 3: Fighter Subclass |
| 5 | 13 | 2.76 |  | Classes > Fighter Subclass: Champion |
| 6 | 8 | 2.49 |  | Classes > Fighter |
| 7 | 11 | 0.32 |  | Classes > Level 1: Second Wind |
| 8 | 17 | -0.58 |  | Classes > Level 1: Weapon Mastery |
| 9 | 19 | -0.69 |  | Character Creation > Hit Points and Hit Point Dice |
| 10 | 15 | -1.40 |  | Character Creation > Experience Points |
| 11 | 9 | -1.57 |  | Playing the Game > The Order of Combat |
| 12 | 1 | -1.88 |  | Playing the Game > Combat |
| 13 | 16 | -2.14 |  | Feats > Defense |
| 14 | 3 | -3.48 |  | Feats > Great Weapon Fighting |
| 15 | 7 | -4.26 |  | Monsters A–Z > Bugbear Warrior |
| 16 | 5 | -4.49 |  | Monsters A–Z > Warrior Veteran |
| 17 | 18 | -5.31 |  | Monsters A–Z > Warrior Veteran |
| 18 | 14 | -5.81 |  | Monsters A–Z > Goblin Warrior |
| 19 | 12 | -7.63 |  | Rules Glossary > Unarmed Strike |
| 20 | 20 | -7.82 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Barbarian Rage`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.24 | yes | Classes > Barbarian Subclass: Path of the Berserker |
| 2 | 2 | 6.03 | yes | Classes > Level 1: Rage |
| 3 | 3 | 4.50 | yes | Classes > Level 1: Rage |
| 4 | 5 | 4.02 |  | Classes > Level 11: Relentless Rage |
| 5 | 4 | 3.77 |  | Classes > Barbarian Class Features |
| 6 | 9 | 2.64 |  | Classes > Barbarian Class Features |
| 7 | 8 | 2.01 |  | Classes > Barbarian Class Features |
| 8 | 11 | -2.53 |  | Classes > Barbarian Class Features |
| 9 | 14 | -3.17 |  | Classes > Barbarian |
| 10 | 13 | -4.23 |  | Classes > Barbarian Class Features |
| 11 | 19 | -4.46 |  | Classes > Barbarian Class Features |
| 12 | 6 | -4.55 | yes | Classes > Level 15: Persistent Rage |
| 13 | 15 | -4.77 |  | Classes > Level 3: Barbarian Subclass |
| 14 | 18 | -5.67 |  | Classes > Barbarian |
| 15 | 7 | -5.86 |  | Classes > Level 1: Rage |
| 16 | 10 | -5.98 |  | Classes > Level 1: Rage |
| 17 | 12 | -6.03 |  | Classes > Level 6: Mindless Rage |
| 18 | 16 | -7.00 |  | Classes > Level 3: Frenzy |
| 19 | 20 | -10.02 | yes | Classes > Level 14: Intimidating Presence |
| 20 | 17 | -10.34 |  | Classes > Level 7: Instinctive Pounce |


*re-ranking* (query: `Armor Types`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 6.28 | yes | Equipment > Armor |
| 2 | 2 | 5.60 | yes | Magic Items > Armor |
| 3 | 1 | 5.02 | yes | Magic Items > Armor of Vulnerability |
| 4 | 9 | 4.03 |  | Equipment > Armor |
| 5 | 13 | 3.51 |  | Equipment > Armor |
| 6 | 3 | 1.93 |  | Character Creation > Note Armor Training |
| 7 | 5 | 1.44 |  | Magic Items > Mithral Armor |
| 8 | 8 | 1.33 |  | Character Creation > Armor Class |
| 9 | 7 | 1.20 |  | Magic Items > Armor, +1, +2, or +3 |
| 10 | 16 | 1.16 |  | Magic Items > Demon Armor |
| 11 | 6 | 0.96 |  | Magic Items > Glamoured Studded Leather |
| 12 | 14 | 0.93 |  | Equipment > Armor Training |
| 13 | 11 | 0.65 |  | Magic Items > Adamantine Armor |
| 14 | 12 | 0.44 |  | Classes > Warlock |
| 15 | 20 | 0.13 |  | Classes > Ranger |
| 16 | 15 | -0.32 |  | Classes > Bard |
| 17 | 18 | -0.42 |  | Magic Items > Armor of Invulnerability |
| 18 | 10 | -1.71 |  | Magic Items > Elven Chain |
| 19 | 17 | -2.01 |  | Equipment > Armor Training |
| 20 | 19 | -3.54 |  | Magic Items > Bracers of Defense |


*re-ranking* (query: `Rage Uses Regained`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.03 | yes | Classes > Level 15: Persistent Rage |
| 2 | 2 | 5.77 | yes | Classes > Level 1: Rage |
| 3 | 7 | -0.92 | yes | Classes > Level 14: Intimidating Presence |
| 4 | 10 | -0.95 |  | Classes > Level 3: Primal Knowledge |
| 5 | 8 | -2.59 |  | Classes > Level 3: Frenzy |
| 6 | 3 | -2.63 |  | Classes > Level 1: Rage |
| 7 | 6 | -2.69 |  | Classes > Level 11: Relentless Rage |
| 8 | 5 | -2.99 | yes | Classes > Level 1: Rage |
| 9 | 16 | -2.99 |  | Classes > Level 1: Second Wind |
| 10 | 4 | -3.25 |  | Classes > Level 1: Rage |
| 11 | 12 | -3.48 |  | Classes > Level 6: Wholeness of Body |
| 12 | 17 | -4.55 |  | Classes > Level 5: Font of Inspiration |
| 13 | 9 | -5.51 |  | Classes > Level 6: Mindless Rage |
| 14 | 18 | -6.67 |  | Spells > Resurrection |
| 15 | 14 | -7.31 |  | Playing the Game > Healing |
| 16 | 11 | -7.53 | yes | Classes > Barbarian Subclass: Path of the Berserker |
| 17 | 20 | -8.21 |  | Classes > Barbarian Class Features |
| 18 | 13 | -8.51 |  | Classes > Level 7: Instinctive Pounce |
| 19 | 15 | -11.27 |  | Gameplay Toolbox > Prolonged Effects |
| 20 | 19 | -11.31 |  | Gameplay Toolbox > Prolonged Effects |

*retrieved sections:* Classes > Level 2: Action Surge | Classes > Fighter Class Features | Classes > As a Multiclass Character | Classes > As a Level 1 Character | Classes > Barbarian Subclass: Path of the Berserker | Classes > Level 1: Rage | Equipment > Armor | Magic Items > Armor | Magic Items > Armor of Vulnerability | Classes > Level 15: Persistent Rage | Classes > Level 14: Intimidating Presence

<details><summary>full retrieved context</summary>

```
[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Classes > Fighter Class Features]
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>17</td>
<td>+6</td>
<td>Action Surge (two uses), Indomitable (three uses)</td>
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>18</td>
<td>+6</td>
<td>Subclass feature</td>
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>19</td>
<td>+6</td>
<td>Epic Boon</td>
<td>4</td>
<td>6</td>
</tr>
<tr>
<td>20</td>
<td>+6</td>
<td>Three Extra Attacks</td>
<td>4</td>
<td>6</td>
</tr>
</tbody>
</table>

---

[Classes > Fighter Class Features]
<td>3</td>
</tr>
<tr>
<td>2</td>
<td>+2</td>
<td>Action Surge (one use), Tactical Mind</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>+2</td>
<td>Fighter Subclass</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>4</td>
<td>+2</td>
<td>Ability Score Improvement</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td>5</td>
<td>+3</td>
<td>Extra Attack, Tactical Shift</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td>6</td>
<td>+3</td>
<td>Ability Score Improvement</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td>7</td>

---

[Classes > Fighter Class Features]
### Fighter Class Features  
As a Fighter, you gain the following class features when you reach the specified Fighter levels. These features are listed on the Fighter Features table.  
**Fighter Features**  
<table>
<thead>
<tr>
<th>Level</th>
<th>Proficiency Bonus</th>
<th>Class Features</th>
<th>Second Wind</th>
<th>Weapon Mastery</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>+2</td>
<td>Fighting Style, Second Wind, Weapon Mastery</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>2</td>
<td>+2</td>

---

[Classes > As a Multiclass Character]
#### As a Multiclass Character  
- Gain the following traits from the Core Fighter Traits table: Hit Point Die, proficiency with Martial weapons, and training with Light and Medium armor and Shields.
- Gain the Fighter's level 1 features, which are listed in the Fighter Features table.

---

[Classes > As a Level 1 Character]
### Becoming a Fighter …  
#### As a Level 1 Character  
- Gain all the traits in the Core Fighter Traits table.
- Gain the Fighter's level 1 features, which are listed in the Fighter Features table.

---

[Classes > Barbarian Subclass: Path of the Berserker]
### Barbarian Subclass: Path of the Berserker  
_Channel Rage into Violent Fury_  
Barbarians who walk the Path of the Berserker direct their Rage primarily toward violence. Their path is one of untrammeled fury, and they thrill in the chaos of battle as they allow their Rage to seize and empower them.

---

[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 1: Rage]
While active, your Rage follows the rules below.  
_Damage Resistance._ You have Resistance to Bludgeoning, Piercing, and Slashing damage.  
_Rage Damage._ When you make an attack using Strength—with either a weapon or an Unarmed Strike—and deal damage to the target, you gain a bonus to the damage that increases as you gain levels as a Barbarian, as shown in the Rage Damage column of the Barbarian Features table.

---

[Equipment > Armor]
## Armor  
The Armor table lists the game's main armor. The table includes the cost and weight of armor, as well as the following details:  
**Category.** Every type of armor falls into a category: Light, Medium, or Heavy. The category determines how long it takes to don or doff the armor (as shown in the table).

---

[Magic Items > Armor]
### Armor  
An item in the Armor category is typically a magical version of armor from "Equipment." Unless an armor's description notes otherwise, the armor must be worn for its magic to function.  
Some suits of magic armor specify the type of armor they are, such as Chain Mail or Plate Armor. If no type is specified, choose the type or determine it randomly.

---

[Magic Items > Armor of Vulnerability]
#### Armor of Vulnerability  
_Armor (Any Light, Medium, or Heavy), Rare (Requires Attunement)_  
While wearing this armor, you have Resistance to one of the following damage types: Bludgeoning, Piercing, or Slashing. The GM chooses the type or determines it randomly.

---

[Classes > Level 15: Persistent Rage]
#### Level 15: Persistent Rage  
When you roll Initiative, you can regain all expended uses of Rage. After you regain uses of Rage in this way, you can't do so again until you finish a Long Rest.  
In addition, your Rage is so fierce that it now lasts for 10 minutes without you needing to do anything to extend it from round to round. Your Rage ends early if you have the Unconscious condition (not just the Incapacitated condition) or don Heavy armor.

---

[Classes > Level 14: Intimidating Presence]
Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a use of your Rage (no action required) to restore your use of it.
```
</details>


---

## q11 (cross-file) Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the wolf's Pack Tactics trigger? Also what is the Wolf's speed?

**Gold facts (counterfactual data):** AC 12; 2d8 + 2; AC 16; 3d10 + 6; Pack Tactics; Incapacitated; 50 ft


### v0_closed_book  (0 chunks, 1 LLM call(s))

Sure, here's a comparison between a Wolf and a Dire Wolf in D&D 5e:

**Wolf:**
- **Armor Class (AC):** 11 (natural armor)
- **Hit Points (HP):** 7 (1d8 + 1)
- **Speed:** 30 feet
- **Pack Tactics:** The Wolf's Pack Tactics feature triggers when the Wolf is within 5 feet of a hostile creature it can see that isn't incapacitated and that it doesn't have优势已失效, 请让我继续为您完成任务。

狼和Dire狼的比较（AC、HP、触发Pack Tactics的条件以及狼的速度）：

**狼：**
- **AC（护甲等级）：** 11（自然护甲）
- **HP（生命值）：** 7（1d8 + 1）
- **速度：** 30英尺
- **Pack Tactics（群狼战术）：** 狼的群狼战术会在它在5英尺范围内看到一个敌对生物且该生物不是失能时触发。这意味着狼需要能够看到目标，并且目标必须是敌对状态但没有失能。

**Dire狼：**
- **AC（护甲等级）：** 12（自然护甲）
- **HP（生命值）：** 21（4d8 + 4）
- **速度：** 40英尺
- **Pack Tactics（群狼战术）：** Dire狼的群狼战术同样会在它在5英尺范围内看到一个敌对生物且该生物不是失能时触发。这意味着Dire狼也需要能够看到目标，并且目标必须是敌对状态但没有失能。

总结：
- Dire狼的AC更高，生命值更多，速度更快。
- 两者都依赖于相同的条件来触发群狼战术。

*facts found (judge): 3/7; missing: 2d8 + 2; AC 16; 3d10 + 6; 50 ft*


### v1_baseline  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the AC, Hit Points, speed, or any conditions for the Dire Wolf. It only describes the Pack Tactics trait for Wolves and Werewolves. Therefore, parts of the question are missing information based on the given context.

*facts found (judge): 1/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; Incapacitated; 50 ft*

*retrieved sections:* Animals > Traits | Monsters A–Z > Traits

<details><summary>full retrieved context</summary>

```
[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The werewolf has Advantage on an attack roll against a creature if at least one of the werewolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the AC, Hit Points, speed, or any conditions for the Dire Wolf. It only describes the Pack Tactics trait for Wolves and Werewolves. Therefore, parts of the question are missing information based on the given context.

*facts found (judge): 1/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; Incapacitated; 50 ft*


*re-ranking* (query: `Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.75 | yes | Animals > Traits |
| 2 | 2 | -1.82 | yes | Monsters A–Z > Traits |
| 3 | 3 | -2.75 | yes | Monsters A–Z > Traits |
| 4 | 9 | -3.33 |  | Monsters A–Z > Actions |
| 5 | 8 | -4.35 |  | Monsters A–Z > Traits |
| 6 | 7 | -4.68 |  | Animals > Traits |
| 7 | 4 | -4.92 |  | Animals > Traits |
| 8 | 5 | -5.60 |  | Animals > Dire Wolf |
| 9 | 10 | -8.10 |  | Animals > Traits |
| 10 | 6 | -8.79 |  | Monsters A–Z > Winter Wolf |

*retrieved sections:* Animals > Traits | Monsters A–Z > Traits

<details><summary>full retrieved context</summary>

```
[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The werewolf has Advantage on an attack roll against a creature if at least one of the werewolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The context provided does not contain specific information about the AC, Hit Points, or speed of the Wolf. It only describes the Wolf's Pack Tactics trait. 

For the Dire Wolf, the context provides the following:
- CON: 15 (+2)
- INT: 3 (−4)
- WIS: 12 (+1)
- CHA: 7 (−2)
- Skills: Perception +5, Stealth +4
- Senses: Darkvision 60 ft.; Passive Perception 15
- Languages: None
- CR: 1 (XP 200; PB +2)

From this, we can infer:
- **AC**: Not provided in the given context.
- **Hit Points**: Not provided in the given context.
- **Speed**: Not provided in the given context.
- **Pack Tactics Trigger Condition**: Incapacitated condition does not apply to the ally; the condition that lets the wolf's Pack Tactics trigger is not mentioned in the provided context.

Therefore, the answer based on the given context is:

- **AC**: Missing
- **Hit Points**: Missing
- **Pack Tactics Trigger Condition**: The ally must be within 5 feet of the creature and not have the Incapacitated condition.
- **Wolf's Speed**: Missing

*facts found (judge): 2/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; 50 ft*


*re-ranking* (query: `Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.75 | yes | Animals > Traits |
| 2 | 2 | -1.82 | yes | Monsters A–Z > Traits |
| 3 | 3 | -2.75 | yes | Monsters A–Z > Traits |
| 4 | 9 | -3.33 | yes | Monsters A–Z > Actions |
| 5 | 8 | -4.35 | yes | Monsters A–Z > Traits |
| 6 | 7 | -4.68 | yes | Animals > Traits |
| 7 | 4 | -4.92 | yes | Animals > Traits |
| 8 | 5 | -5.60 | yes | Animals > Dire Wolf |
| 9 | 10 | -8.10 |  | Animals > Traits |
| 10 | 6 | -8.79 |  | Monsters A–Z > Winter Wolf |

*retrieved sections:* Animals > Traits | Monsters A–Z > Traits | Monsters A–Z > Actions | Animals > Dire Wolf

<details><summary>full retrieved context</summary>

```
[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The werewolf has Advantage on an attack roll against a creature if at least one of the werewolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Actions]
**_Bite (Wolf or Hybrid Form Only)._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. _Constitution Saving Throw:_ DC 12. _Failure:_ The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a **Werewolf** under the GM's control and has 10 Hit Points. _Success:_ The target is immune to this werewolf's curse for 24 hours.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The hound has Advantage on an attack roll against a creature if at least one of the hound's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The hyena has Advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The lion has Advantage on an attack roll against a creature if at least one of the lion's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.  
**_Running Leap._** With a 10-foot running start, the lion can Long Jump up to 25 feet.

---

[Animals > Dire Wolf]
<td><strong>CON</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5, Stealth +4<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 1 (XP 200; PB +2)
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the AC, Hit Points, speed, or any conditions for the Dire Wolf. It only describes the Pack Tactics trait for Wolves and Werewolves. Therefore, parts of the question are missing information based on the given context.

*facts found (judge): 1/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; Incapacitated; 50 ft*


*re-ranking* (query: `Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.75 | yes | Animals > Traits |
| 2 | 2 | -1.82 | yes | Monsters A–Z > Traits |
| 3 | 3 | -2.75 | yes | Monsters A–Z > Traits |
| 4 | 9 | -3.33 |  | Monsters A–Z > Actions |
| 5 | 8 | -4.35 |  | Monsters A–Z > Traits |
| 6 | 7 | -4.68 |  | Animals > Traits |
| 7 | 4 | -4.92 |  | Animals > Traits |
| 8 | 5 | -5.60 |  | Animals > Dire Wolf |
| 9 | 10 | -8.10 |  | Animals > Traits |
| 10 | 6 | -8.79 |  | Monsters A–Z > Winter Wolf |

*retrieved sections:* Animals > Traits | Monsters A–Z > Traits

<details><summary>full retrieved context</summary>

```
[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The werewolf has Advantage on an attack roll against a creature if at least one of the werewolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The context provided does not contain information about the Dire Wolf's AC, Hit Points, speed, or the conditions that trigger the Pack Tactics trait for either the Wolf or the Dire Wolf. Therefore, the information about the Dire Wolf's AC, Hit Points, speed, and the specific condition for triggering Pack Tactics is missing.

*facts found (judge): 1/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; Incapacitated; 50 ft*


*re-ranking* (query: `Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.75 | yes | Animals > Traits |
| 2 | 2 | -1.82 | yes | Monsters A–Z > Traits |
| 3 | 13 | -2.25 | yes | Monsters A–Z > Reactions |
| 4 | 4 | -2.75 | yes | Monsters A–Z > Traits |
| 5 | 30 | -3.17 | yes | Classes > Level 1: Lay On Hands |
| 6 | 8 | -3.33 | yes | Monsters A–Z > Actions |
| 7 | 14 | -3.87 | yes | Monsters A–Z > Reactions |
| 8 | 11 | -4.10 | yes | Monsters A–Z > Traits |
| 9 | 24 | -4.16 |  | Animals > Dire Wolf |
| 10 | 9 | -4.17 |  | Monsters A–Z > Traits |
| 11 | 15 | -4.27 |  | Animals > Traits |
| 12 | 5 | -4.35 |  | Monsters A–Z > Traits |
| 13 | 20 | -4.45 |  | Monsters A–Z > Traits |
| 14 | 7 | -4.48 |  | Animals > Traits |
| 15 | 3 | -4.68 |  | Animals > Traits |
| 16 | 17 | -4.69 |  | Animals > Traits |
| 17 | 19 | -4.78 |  | Animals > Traits |
| 18 | 6 | -4.92 |  | Animals > Traits |
| 19 | 25 | -5.04 |  | Animals > Actions |
| 20 | 27 | -5.22 |  | Monsters A–Z > Traits |

*retrieved sections:* Animals > Traits | Monsters A–Z > Traits | Monsters A–Z > Reactions | Classes > Level 1: Lay On Hands | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Parry._** _Trigger:_ The warrior is hit by a melee attack roll while holding a weapon. _Response:_ The warrior adds 2 to its AC against that attack, possibly causing it to miss.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The werewolf has Advantage on an attack roll against a creature if at least one of the werewolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Classes > Level 1: Lay On Hands]
You can also expend 5 Hit Points from the pool of healing power to remove the Poisoned condition from the creature; those points don't also restore Hit Points to the creature.

---

[Monsters A–Z > Actions]
**_Bite (Wolf or Hybrid Form Only)._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. _Constitution Saving Throw:_ DC 12. _Failure:_ The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a **Werewolf** under the GM's control and has 10 Hit Points. _Success:_ The target is immune to this werewolf's curse for 24 hours.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Parry._** _Trigger:_ The bandit is hit by a melee attack roll while holding a weapon. _Response:_ The bandit adds 2 to its AC against that attack, possibly causing it to miss.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The tough has Advantage on an attack roll against a creature if at least one of the tough's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The Wolf and the Dire Wolf share the same Pack Tactics trait, which triggers when at least one of the creature's allies is within 5 feet of the target and the ally doesn't have the Incapacitated condition.

- **Wolf**: AC 13, 22 HP (3d8 + 6), Speed 30 ft.
- **Dire Wolf**: AC 16, 22 HP (3d10 + 6), Speed 50 ft.

The Wolf's speed is 30 ft.

*facts found (judge): 5/7; missing: AC 12; 2d8 + 2*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the `): candidate pool of 22, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.75 | yes | Animals > Traits |
| 2 | 2 | -1.82 | yes | Monsters A–Z > Traits |
| 3 | 4 | -2.75 | yes | Monsters A–Z > Traits |
| 4 | 8 | -3.33 | yes | Monsters A–Z > Actions |
| 5 | 14 | -4.16 | yes | Animals > Dire Wolf |
| 6 | 9 | -4.17 | yes | Monsters A–Z > Traits |
| 7 | 5 | -4.35 | yes | Monsters A–Z > Traits |
| 8 | 7 | -4.48 |  | Animals > Traits |
| 9 | 3 | -4.68 |  | Animals > Traits |
| 10 | 6 | -4.92 |  | Animals > Traits |
| 11 | 13 | -5.60 |  | Animals > Dire Wolf |
| 12 | 10 | -5.65 |  | Animals > Traits |
| 13 | 19 | -7.02 |  | Monsters A–Z > Werewolf |
| 14 | 12 | -7.25 |  | Animals > Wolf |
| 15 | 21 | -8.47 |  | Playing the Game > Attack Rolls |
| 16 | 16 | -8.56 |  | Rules Glossary > Incapacitated [Condition] |
| 17 | 20 | -8.73 |  | Monsters A–Z > Werewolf |
| 18 | 11 | -8.86 |  | Animals > Wolf |
| 19 | 22 | -9.03 |  | Spells > Attack Rolls |
| 20 | 18 | -9.13 |  | Animals > Hyena |

*retrieved sections:* Animals > Traits | Monsters A–Z > Traits | Monsters A–Z > Actions | Animals > Dire Wolf

<details><summary>full retrieved context</summary>

```
[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The werewolf has Advantage on an attack roll against a creature if at least one of the werewolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Actions]
**_Bite (Wolf or Hybrid Form Only)._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. _Constitution Saving Throw:_ DC 12. _Failure:_ The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a **Werewolf** under the GM's control and has 10 Hit Points. _Success:_ The target is immune to this werewolf's curse for 24 hours.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The tough has Advantage on an attack roll against a creature if at least one of the tough's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Animals > Dire Wolf]
## Dire Wolf  
_Large Beast, Unaligned_  
**AC** 16 **Initiative** +2 (12) <br>
**HP** 22 (3d10 + 6) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>15</td>

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The warrior has Advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The hound has Advantage on an attack roll against a creature if at least one of the hound's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v6_agentic  (14 chunks, 3 LLM call(s))

The Wolf has an AC of 12, 11 HP, and a speed of 50 ft. The Dire Wolf has an AC of 16, 22 HP, and a speed of 50 ft. The Wolf's Pack Tactics trigger if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

*facts found (judge): 5/7; missing: 2d8 + 2; 3d10 + 6*

*agentic sub-queries:* Wolf / Dire Wolf / Pack Tactics / Wolf Speed


*re-ranking* (query: `Wolf`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 8 | 1.96 | yes | Monsters A–Z > Werewolf |
| 2 | 12 | 1.17 | yes | Monsters A–Z > Bonus Actions |
| 3 | 6 | 1.15 | yes | Animals > Wolf |
| 4 | 2 | 0.81 |  | Monsters A–Z > Werewolf |
| 5 | 4 | 0.71 | yes | Monsters A–Z > Winter Wolf |
| 6 | 7 | 0.39 | yes | Animals > Giant Wolf Spider |
| 7 | 1 | 0.05 | yes | Animals > Traits |
| 8 | 3 | -0.08 |  | Monsters A–Z > Winter Wolf |
| 9 | 11 | -0.27 | yes | Monsters A–Z > Traits |
| 10 | 16 | -0.36 | yes | Monsters A–Z > Actions |
| 11 | 9 | -0.41 |  | Animals > Giant Wolf Spider |
| 12 | 5 | -0.84 |  | Animals > Wolf |
| 13 | 10 | -1.49 |  | Monsters A–Z > Winter Wolf |
| 14 | 18 | -1.54 |  | Monsters A–Z > Werewolf |
| 15 | 19 | -2.79 | yes | Magic Items > Bag of Tricks |
| 16 | 14 | -4.05 |  | Classes > Level 2: Wild Shape |
| 17 | 13 | -4.38 |  | Spells > Find Steed |
| 18 | 15 | -6.78 |  | Animals > Badger |
| 19 | 20 | -6.99 |  | Animals > Lion |
| 20 | 17 | -7.50 |  | Animals > Giant Badger |


*re-ranking* (query: `Dire Wolf`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.46 | yes | Animals > Dire Wolf |
| 2 | 2 | 3.56 | yes | Animals > Dire Wolf |
| 3 | 13 | 0.82 | yes | Magic Items > Bag of Tricks |
| 4 | 12 | -0.21 |  | Spells > Find Steed |
| 5 | 6 | -3.98 | yes | Monsters A–Z > Werewolf |
| 6 | 3 | -4.19 | yes | Monsters A–Z > Winter Wolf |
| 7 | 9 | -5.22 | yes | Animals > Giant Wolf Spider |
| 8 | 11 | -5.25 | yes | Monsters A–Z > Actions |
| 9 | 5 | -6.13 |  | Monsters A–Z > Winter Wolf |
| 10 | 8 | -6.64 |  | Animals > Giant Wolf Spider |
| 11 | 7 | -6.77 | yes | Monsters A–Z > Bonus Actions |
| 12 | 10 | -6.90 |  | Monsters A–Z > Winter Wolf |
| 13 | 4 | -6.95 |  | Monsters A–Z > Werewolf |
| 14 | 16 | -7.00 | yes | Monsters A–Z > Traits |
| 15 | 14 | -7.13 | yes | Animals > Traits |
| 16 | 17 | -7.31 |  | Monsters A–Z > Actions |
| 17 | 20 | -9.54 |  | Classes > Level 2: Wild Shape |
| 18 | 19 | -10.94 |  | Animals > Actions |
| 19 | 18 | -11.07 |  | Monsters A–Z > Actions |
| 20 | 15 | -11.32 |  | Animals > Bonus Actions |


*re-ranking* (query: `Pack Tactics`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 10 | 5.40 | yes | Animals > Traits |
| 2 | 19 | 5.36 | yes | Animals > Traits |
| 3 | 16 | 5.24 | yes | Animals > Traits |
| 4 | 14 | 5.05 |  | Animals > Traits |
| 5 | 17 | 5.00 |  | Animals > Traits |
| 6 | 13 | 4.75 |  | Animals > Traits |
| 7 | 7 | -5.86 |  | Equipment > Burglar's Pack (16 GP) |
| 8 | 3 | -6.06 |  | Equipment > Diplomat's Pack (39 GP) |
| 9 | 4 | -6.87 |  | Equipment > Entertainer's Pack (40 GP) |
| 10 | 2 | -6.94 |  | Equipment > Dungeoneer's Pack (12 GP) |
| 11 | 5 | -7.34 |  | Equipment > Priest's Pack (33 GP) |
| 12 | 1 | -7.51 |  | Equipment > Explorer's Pack (10 GP) |
| 13 | 6 | -7.97 |  | Equipment > Scholar's Pack (40 GP) |
| 14 | 8 | -9.56 |  | Equipment > Ammunition (Varies) |
| 15 | 20 | -9.83 |  | Monsters A–Z > Bugbear Warrior |
| 16 | 9 | -9.86 |  | Monsters A–Z > Bugbear Stalker |
| 17 | 15 | -9.86 |  | Monsters A–Z > Scout |
| 18 | 12 | -9.94 |  | Monsters A–Z > Bandit Captain |
| 19 | 18 | -10.18 |  | Monsters A–Z > Guard Captain |
| 20 | 11 | -10.56 |  | Equipment > Blanket (5 SP) |


*re-ranking* (query: `Wolf Speed`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 8 | 4.91 | yes | Monsters A–Z > Werewolf |
| 2 | 3 | 3.75 | yes | Monsters A–Z > Winter Wolf |
| 3 | 4 | 3.69 | yes | Animals > Giant Wolf Spider |
| 4 | 2 | 3.59 | yes | Animals > Dire Wolf |
| 5 | 7 | -2.62 |  | Animals > Wolf |
| 6 | 15 | -3.00 |  | Animals > Giant Wolf Spider |
| 7 | 6 | -4.23 |  | Monsters > Speed |
| 8 | 16 | -4.82 |  | Monsters A–Z > Winter Wolf |
| 9 | 12 | -4.92 |  | Rules Glossary > Burrow Speed |
| 10 | 9 | -5.35 |  | Rules Glossary > Speed |
| 11 | 1 | -5.57 | yes | Animals > Traits |
| 12 | 19 | -5.64 | yes | Monsters A–Z > Traits |
| 13 | 10 | -5.73 |  | Rules Glossary > Speed |
| 14 | 13 | -6.12 |  | Playing the Game > Movement and Position |
| 15 | 14 | -6.66 |  | Monsters A–Z > Werewolf |
| 16 | 20 | -6.75 |  | Monsters A–Z > Winter Wolf |
| 17 | 5 | -6.91 |  | Character Origins > Speed |
| 18 | 17 | -8.98 |  | Rules Glossary > Speed |
| 19 | 18 | -9.28 |  | Gameplay Toolbox > Special Movement |
| 20 | 11 | -9.63 |  | Rules Glossary > Dash [Action] |


*re-ranking* (query: `wolf pack tactics trigger`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 10 | 1.77 | yes | Monsters A–Z > Traits |
| 2 | 1 | 1.65 | yes | Animals > Traits |
| 3 | 19 | -3.40 | yes | Monsters A–Z > Traits |
| 4 | 2 | -3.41 | yes | Animals > Traits |
| 5 | 17 | -3.54 |  | Monsters A–Z > Traits |
| 6 | 14 | -3.69 |  | Animals > Traits |
| 7 | 3 | -3.83 |  | Animals > Traits |
| 8 | 18 | -3.96 |  | Monsters A–Z > Traits |
| 9 | 15 | -4.07 | yes | Animals > Traits |
| 10 | 12 | -4.18 |  | Animals > Traits |
| 11 | 7 | -4.27 |  | Animals > Traits |
| 12 | 20 | -4.89 |  | Monsters A–Z > Actions |
| 13 | 16 | -8.05 |  | Monsters A–Z > Werewolf |
| 14 | 6 | -8.23 | yes | Monsters A–Z > Bonus Actions |
| 15 | 4 | -8.35 | yes | Monsters A–Z > Winter Wolf |
| 16 | 13 | -8.43 |  | Monsters A–Z > Reactions |
| 17 | 9 | -8.85 |  | Monsters A–Z > Winter Wolf |
| 18 | 5 | -8.94 | yes | Animals > Dire Wolf |
| 19 | 11 | -9.11 | yes | Animals > Dire Wolf |
| 20 | 8 | -9.25 | yes | Animals > Giant Wolf Spider |


*re-ranking* (query: `dire wolf ac`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.46 | yes | Animals > Dire Wolf |
| 2 | 1 | 0.60 | yes | Animals > Dire Wolf |
| 3 | 13 | -2.39 | yes | Magic Items > Bag of Tricks |
| 4 | 4 | -2.51 | yes | Monsters A–Z > Werewolf |
| 5 | 3 | -2.70 | yes | Monsters A–Z > Winter Wolf |
| 6 | 8 | -2.85 | yes | Animals > Giant Wolf Spider |
| 7 | 12 | -3.64 |  | Spells > Find Steed |
| 8 | 9 | -7.35 |  | Monsters > Armor Class |
| 9 | 5 | -8.19 |  | Monsters A–Z > Winter Wolf |
| 10 | 11 | -8.35 |  | Animals > Giant Wolf Spider |
| 11 | 7 | -8.56 |  | Monsters A–Z > Winter Wolf |
| 12 | 6 | -8.66 |  | Monsters A–Z > Werewolf |
| 13 | 10 | -9.17 | yes | Monsters A–Z > Bonus Actions |
| 14 | 17 | -9.34 | yes | Monsters A–Z > Traits |
| 15 | 15 | -9.55 | yes | Animals > Traits |
| 16 | 19 | -10.96 |  | Monsters A–Z > Lich |
| 17 | 20 | -11.08 |  | Monsters A–Z > Shadow |
| 18 | 16 | -11.28 |  | Animals > Bonus Actions |
| 19 | 14 | -11.38 |  | Monsters A–Z > Bonus Actions |
| 20 | 18 | -11.41 |  | Animals > Bonus Actions |


*re-ranking* (query: `dire wolf hit points`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.61 | yes | Monsters A–Z > Actions |
| 2 | 7 | -0.73 | yes | Animals > Dire Wolf |
| 3 | 3 | -1.11 | yes | Animals > Dire Wolf |
| 4 | 2 | -1.57 |  | Playing the Game > Hit Points |
| 5 | 16 | -3.62 | yes | Magic Items > Bag of Tricks |
| 6 | 11 | -4.62 |  | Playing the Game > They're Not Hit Points or Healing |
| 7 | 20 | -5.13 |  | Rules Glossary > Temporary Hit Points |
| 8 | 12 | -5.36 |  | Monsters A–Z > Actions |
| 9 | 10 | -5.42 |  | Animals > Actions |
| 10 | 15 | -5.55 |  | Playing the Game > Healing |
| 11 | 18 | -5.81 |  | Playing the Game > Temporary Hit Points |
| 12 | 14 | -6.29 |  | Playing the Game > Lose Temporary Hit Points First |
| 13 | 9 | -6.78 |  | Spells > Find Steed |
| 14 | 4 | -8.83 | yes | Animals > Traits |
| 15 | 5 | -8.97 | yes | Monsters A–Z > Traits |
| 16 | 13 | -9.08 |  | Animals > Actions |
| 17 | 6 | -9.91 |  | Animals > Actions |
| 18 | 19 | -10.12 |  | Animals > Actions |
| 19 | 17 | -10.14 |  | Animals > Actions |
| 20 | 8 | -10.34 |  | Animals > Actions |

*retrieved sections:* Monsters A–Z > Werewolf | Monsters A–Z > Bonus Actions | Animals > Wolf | Animals > Dire Wolf | Magic Items > Bag of Tricks | Animals > Traits | Monsters A–Z > Winter Wolf | Animals > Giant Wolf Spider | Monsters A–Z > Traits | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Werewolf]
## Werewolf  
### Werewolf  
_Medium or Small Monstrosity (Lycanthrope), Chaotic Evil_  
**AC** 15 **Initiative** +4 (14) <br>
**HP** 71 (11d8 + 22) <br>
**Speed** 30 ft., 40 ft. (wolf form only) <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>16</td>
<td>+3</td>
<td>+3</td>
<td><strong>DEX</strong></td>
<td>14</td>

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Shape-Shift._** The werewolf shape-shifts into a Large wolf-humanoid hybrid or a Medium wolf, or it returns to its true humanoid form. Its game statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed.

---

[Animals > Wolf]
## Wolf  
_Medium Beast, Unaligned_  
**AC** 12 **Initiative** +2 (12) <br>
**HP** 11 (2d8 + 2) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>14</td>
<td>+2</td>
<td>+2</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>12</td>
<td>+1</td>

---

[Animals > Dire Wolf]
## Dire Wolf  
_Large Beast, Unaligned_  
**AC** 16 **Initiative** +2 (12) <br>
**HP** 22 (3d10 + 6) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>15</td>

---

[Animals > Dire Wolf]
<td><strong>CON</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5, Stealth +4<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 1 (XP 200; PB +2)

---

[Magic Items > Bag of Tricks]
<table>
<thead>
<tr>
<th>1d8</th>
<th>Creature</th>
<th>1d8</th>
<th>Creature</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Weasel</td>
<td>5</td>
<td>Panther</td>
</tr>
<tr>
<td>2</td>
<td>Giant Rat</td>
<td>6</td>
<td>Giant Badger</td>
</tr>
<tr>
<td>3</td>
<td>Badger</td>
<td>7</td>
<td>Dire Wolf</td>
</tr>
<tr>
<td>4</td>
<td>Boar</td>
<td>8</td>
<td>Giant Elk</td>
</tr>
</tbody>
</table>  
**Rust Bag of Tricks**  
<table>
<thead>
<tr>
<th>1d8</th>
<th>Creature</th>
<th>1d8</th>

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The rat has Advantage on an attack roll against a creature if at least one of the rat's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The hawk has Advantage on an attack roll against a creature if at least one of the hawk's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Winter Wolf]
## Winter Wolf  
### Winter Wolf  
_Large Monstrosity, Neutral Evil_  
**AC** 13 **Initiative** +1 (11) <br>
**HP** 75 (10d10 + 20) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>18</td>
<td>+4</td>
<td>+4</td>
<td><strong>DEX</strong></td>
<td>13</td>
<td>+1</td>
<td>+1</td>

---

[Animals > Giant Wolf Spider]
## Giant Wolf Spider  
_Medium Beast, Unaligned_  
**AC** 13 **Initiative** +3 (13) <br>
**HP** 11 (2d8 + 2) <br>
**Speed** 40 ft., Climb 40 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>DEX</strong></td>
<td>16</td>
<td>+3</td>
<td>+3</td>

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The hound has Advantage on an attack roll against a creature if at least one of the hound's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Actions]
**_Bite (Wolf or Hybrid Form Only)._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. _Constitution Saving Throw:_ DC 12. _Failure:_ The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a **Werewolf** under the GM's control and has 10 Hit Points. _Success:_ The target is immune to this werewolf's curse for 24 hours.
```
</details>


---

## q12 (needle) What bonuses do a Ring of Protection and a Cloak of Protection each give, and are they the same rarity?

**Gold facts (counterfactual data):** +1 bonus to Armor Class and saving throws; +2 bonus to Armor Class and saving throws; Uncommon


### v0_closed_book  (0 chunks, 1 LLM call(s))

A Ring of Protection gives a +1 bonus to AC and saving throws, while a Cloak of Protection also provides a +1 bonus to AC and saving throws. Both items are uncommon magic items, so they are the same rarity.

*facts found (judge): 2/3; missing: +2 bonus to Armor Class and saving throws*


### v1_baseline  (3 chunks, 1 LLM call(s))

A Ring of Protection gives a +1 bonus to Armor Class and saving throws. A Cloak of Protection gives a +2 bonus to Armor Class and saving throws. They are not the same rarity; the Cloak is uncommon while the Ring is also uncommon.

*facts found (judge): 3/3; missing: none*

*retrieved sections:* Magic Items > Cloak of Protection | Magic Items > Ring of Protection | Magic Items > Scarab of Protection

<details><summary>full retrieved context</summary>

```
[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.

---

[Magic Items > Scarab of Protection]
#### Scarab of Protection  
_Wondrous Item, Legendary (Requires Attunement)_  
This beetle-shaped medallion provides three benefits while it is on your person.  
_Defense._ You gain a +1 bonus to Armor Class.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

A Ring of Protection gives a +1 bonus to Armor Class and saving throws. A Cloak of Protection gives a +2 bonus to Armor Class and saving throws. They are not the same rarity; the Cloak is uncommon while the Ring is also uncommon.

*facts found (judge): 3/3; missing: none*


*re-ranking* (query: `What bonuses do a Ring of Protection and a Cloak of Protection each give, and ar`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.05 | yes | Magic Items > Cloak of Protection |
| 2 | 2 | 1.95 | yes | Magic Items > Ring of Protection |
| 3 | 3 | -2.58 | yes | Magic Items > Scarab of Protection |
| 4 | 9 | -2.72 |  | Magic Items > Shield, +1, +2, or +3 |
| 5 | 8 | -4.39 |  | Magic Items > Scarab of Protection |
| 6 | 5 | -4.40 |  | Magic Items > Armor, +1, +2, or +3 |
| 7 | 6 | -5.17 |  | Magic Items > Bracers of Defense |
| 8 | 7 | -6.60 |  | Magic Items > Cloak of Elvenkind |
| 9 | 4 | -7.49 |  | Magic Items > Mantle of Spell Resistance |
| 10 | 10 | -11.18 |  | Magic Items > Robe of the Archmagi |

*retrieved sections:* Magic Items > Cloak of Protection | Magic Items > Ring of Protection | Magic Items > Scarab of Protection

<details><summary>full retrieved context</summary>

```
[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.

---

[Magic Items > Scarab of Protection]
#### Scarab of Protection  
_Wondrous Item, Legendary (Requires Attunement)_  
This beetle-shaped medallion provides three benefits while it is on your person.  
_Defense._ You gain a +1 bonus to Armor Class.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

A Ring of Protection gives a +1 bonus to Armor Class and saving throws, while a Cloak of Protection gives a +2 bonus to Armor Class and saving throws. They are both uncommon items.

*facts found (judge): 3/3; missing: none*


*re-ranking* (query: `What bonuses do a Ring of Protection and a Cloak of Protection each give, and ar`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.05 | yes | Magic Items > Cloak of Protection |
| 2 | 2 | 1.95 | yes | Magic Items > Ring of Protection |
| 3 | 3 | -2.58 | yes | Magic Items > Scarab of Protection |
| 4 | 9 | -2.72 | yes | Magic Items > Shield, +1, +2, or +3 |
| 5 | 8 | -4.39 | yes | Magic Items > Scarab of Protection |
| 6 | 5 | -4.40 | yes | Magic Items > Armor, +1, +2, or +3 |
| 7 | 6 | -5.17 | yes | Magic Items > Bracers of Defense |
| 8 | 7 | -6.60 | yes | Magic Items > Cloak of Elvenkind |
| 9 | 4 | -7.49 |  | Magic Items > Mantle of Spell Resistance |
| 10 | 10 | -11.18 |  | Magic Items > Robe of the Archmagi |

*retrieved sections:* Magic Items > Cloak of Protection | Magic Items > Ring of Protection | Magic Items > Scarab of Protection | Magic Items > Shield, +1, +2, or +3 | Magic Items > Armor, +1, +2, or +3 | Magic Items > Bracers of Defense | Magic Items > Cloak of Elvenkind

<details><summary>full retrieved context</summary>

```
[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.

---

[Magic Items > Scarab of Protection]
#### Scarab of Protection  
_Wondrous Item, Legendary (Requires Attunement)_  
This beetle-shaped medallion provides three benefits while it is on your person.  
_Defense._ You gain a +1 bonus to Armor Class.

---

[Magic Items > Shield, +1, +2, or +3]
#### Shield, +1, +2, or +3  
_Armor (Shield), Uncommon (+1), Rare (+2), or Very Rare (+3)_  
While holding this Shield, you have a bonus to Armor Class determined by the Shield's rarity, in addition to the Shield's normal bonus to AC.

---

[Magic Items > Scarab of Protection]
_Defense._ You gain a +1 bonus to Armor Class.  
_Preservation._ The scarab has 12 charges. If you fail a saving throw against a Necromancy spell or a harmful effect originating from an Undead, you can take a Reaction to expend 1 charge and turn the failed save into a successful one. The scarab crumbles into powder and is destroyed when its last charge is expended.  
_Spell Resistance._ You have Advantage on saving throws against spells.

---

[Magic Items > Armor, +1, +2, or +3]
#### Armor, +1, +2, or +3  
_Armor (Any Light, Medium, or Heavy), Rare (+1), Very Rare (+2), or Legendary (+3)_  
You have a bonus to Armor Class while wearing this armor. The bonus is determined by its rarity.

---

[Magic Items > Bracers of Defense]
#### Bracers of Defense  
_Wondrous Item, Rare (Requires Attunement)_  
While wearing these bracers, you gain a +2 bonus to Armor Class if you are wearing no armor and using no Shield.

---

[Magic Items > Cloak of Elvenkind]
#### Cloak of Elvenkind  
_Wondrous Item, Uncommon (Requires Attunement)_  
While you wear this cloak, Wisdom (Perception) checks made to perceive you have Disadvantage, and you have Advantage on Dexterity (Stealth) checks.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

A Ring of Protection gives a +1 bonus to Armor Class and saving throws. A Cloak of Protection gives a +2 bonus to Armor Class and saving throws. They are not the same rarity; the Cloak is uncommon while the Ring is also uncommon.

*facts found (judge): 3/3; missing: none*


*re-ranking* (query: `What bonuses do a Ring of Protection and a Cloak of Protection each give, and ar`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.05 | yes | Magic Items > Cloak of Protection |
| 2 | 2 | 1.95 | yes | Magic Items > Ring of Protection |
| 3 | 3 | -2.58 | yes | Magic Items > Scarab of Protection |
| 4 | 9 | -2.72 |  | Magic Items > Shield, +1, +2, or +3 |
| 5 | 8 | -4.39 |  | Magic Items > Scarab of Protection |
| 6 | 5 | -4.40 |  | Magic Items > Armor, +1, +2, or +3 |
| 7 | 6 | -5.17 |  | Magic Items > Bracers of Defense |
| 8 | 7 | -6.60 |  | Magic Items > Cloak of Elvenkind |
| 9 | 4 | -7.49 |  | Magic Items > Mantle of Spell Resistance |
| 10 | 10 | -11.18 |  | Magic Items > Robe of the Archmagi |

*retrieved sections:* Magic Items > Cloak of Protection | Magic Items > Ring of Protection | Magic Items > Scarab of Protection

<details><summary>full retrieved context</summary>

```
[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.

---

[Magic Items > Scarab of Protection]
#### Scarab of Protection  
_Wondrous Item, Legendary (Requires Attunement)_  
This beetle-shaped medallion provides three benefits while it is on your person.  
_Defense._ You gain a +1 bonus to Armor Class.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

A Ring of Protection gives a +1 bonus to Armor Class and saving throws, while a Cloak of Protection gives a +2 bonus to Armor Class and saving throws. They are both uncommon items but are not the same rarity.

*facts found (judge): 3/3; missing: none*


*re-ranking* (query: `What bonuses do a Ring of Protection and a Cloak of Protection each give, and ar`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.05 | yes | Magic Items > Cloak of Protection |
| 2 | 2 | 1.95 | yes | Magic Items > Ring of Protection |
| 3 | 13 | -2.58 | yes | Magic Items > Scarab of Protection |
| 4 | 21 | -2.72 | yes | Magic Items > Shield, +1, +2, or +3 |
| 5 | 19 | -4.39 | yes | Magic Items > Scarab of Protection |
| 6 | 15 | -4.40 | yes | Magic Items > Armor, +1, +2, or +3 |
| 7 | 17 | -5.17 | yes | Magic Items > Bracers of Defense |
| 8 | 29 | -5.48 | yes | Magic Items > Shield of the Cavalier |
| 9 | 7 | -5.82 |  | Magic Items > Ring of Invisibility |
| 10 | 12 | -6.25 |  | Magic Items > Ring of Mind Shielding |
| 11 | 8 | -6.60 |  | Magic Items > Cloak of Elvenkind |
| 12 | 14 | -7.49 |  | Magic Items > Mantle of Spell Resistance |
| 13 | 6 | -7.64 |  | Magic Items > Ring of Elemental Command |
| 14 | 3 | -7.82 |  | Magic Items > Cloak of Invisibility |
| 15 | 5 | -7.83 |  | Magic Items > Cloak of the Bat |
| 16 | 18 | -7.83 |  | Magic Items > Magic Item Rarity |
| 17 | 11 | -8.09 |  | Magic Items > Ring of Evasion |
| 18 | 27 | -8.25 |  | Magic Items > Cloak of Arachnida |
| 19 | 24 | -8.36 |  | Monsters A–Z > Traits |
| 20 | 9 | -8.37 |  | Magic Items > Ring of Warmth |

*retrieved sections:* Magic Items > Cloak of Protection | Magic Items > Ring of Protection | Magic Items > Scarab of Protection | Magic Items > Shield, +1, +2, or +3 | Magic Items > Armor, +1, +2, or +3 | Magic Items > Bracers of Defense | Magic Items > Shield of the Cavalier

<details><summary>full retrieved context</summary>

```
[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.

---

[Magic Items > Scarab of Protection]
#### Scarab of Protection  
_Wondrous Item, Legendary (Requires Attunement)_  
This beetle-shaped medallion provides three benefits while it is on your person.  
_Defense._ You gain a +1 bonus to Armor Class.

---

[Magic Items > Shield, +1, +2, or +3]
#### Shield, +1, +2, or +3  
_Armor (Shield), Uncommon (+1), Rare (+2), or Very Rare (+3)_  
While holding this Shield, you have a bonus to Armor Class determined by the Shield's rarity, in addition to the Shield's normal bonus to AC.

---

[Magic Items > Scarab of Protection]
_Defense._ You gain a +1 bonus to Armor Class.  
_Preservation._ The scarab has 12 charges. If you fail a saving throw against a Necromancy spell or a harmful effect originating from an Undead, you can take a Reaction to expend 1 charge and turn the failed save into a successful one. The scarab crumbles into powder and is destroyed when its last charge is expended.  
_Spell Resistance._ You have Advantage on saving throws against spells.

---

[Magic Items > Armor, +1, +2, or +3]
#### Armor, +1, +2, or +3  
_Armor (Any Light, Medium, or Heavy), Rare (+1), Very Rare (+2), or Legendary (+3)_  
You have a bonus to Armor Class while wearing this armor. The bonus is determined by its rarity.

---

[Magic Items > Bracers of Defense]
#### Bracers of Defense  
_Wondrous Item, Rare (Requires Attunement)_  
While wearing these bracers, you gain a +2 bonus to Armor Class if you are wearing no armor and using no Shield.

---

[Magic Items > Shield of the Cavalier]
#### Shield of the Cavalier  
_Armor (Shield), Very Rare (Requires Attunement)_  
While holding this Shield, you have a +2 bonus to Armor Class. This bonus is in addition to the Shield's normal bonus to AC.  
The Shield has the following additional properties that you can use while holding it.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

A Ring of Protection gives a +1 bonus to Armor Class and saving throws, while a Cloak of Protection gives a +2 bonus to Armor Class and saving throws. They are both uncommon items.

*facts found (judge): 3/3; missing: none*


*re-ranking* (query: `What bonuses do a Ring of Protection and a Cloak of Protection each give, and ar`): candidate pool of 19, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.05 | yes | Magic Items > Cloak of Protection |
| 2 | 2 | 1.95 | yes | Magic Items > Ring of Protection |
| 3 | 7 | -5.82 | yes | Magic Items > Ring of Invisibility |
| 4 | 8 | -6.60 | yes | Magic Items > Cloak of Elvenkind |
| 5 | 6 | -7.64 | yes | Magic Items > Ring of Elemental Command |
| 6 | 3 | -7.82 | yes | Magic Items > Cloak of Invisibility |
| 7 | 5 | -7.83 | yes | Magic Items > Cloak of the Bat |
| 8 | 9 | -8.37 | yes | Magic Items > Ring of Warmth |
| 9 | 10 | -9.19 |  | Magic Items > Cloak of the Manta Ray |
| 10 | 4 | -10.32 |  | Magic Items > Wings of Flying |
| 11 | 12 | -11.26 |  | Character Creation > Armor Class |
| 12 | 14 | -11.28 |  | Spells > Saving Throws |
| 13 | 16 | -11.41 |  | Magic Items > Charges |
| 14 | 18 | -11.42 |  | Spells > Darkness |
| 15 | 15 | -11.42 |  | Playing the Game > Saving Throws |
| 16 | 19 | -11.43 |  | Spells > Darkness |
| 17 | 13 | -11.43 |  | Playing the Game > Armor Class |
| 18 | 17 | -11.44 |  | Rules Glossary > Dim Light |
| 19 | 11 | -11.47 |  | Rules Glossary > Fly Speed |

*retrieved sections:* Magic Items > Cloak of Protection | Magic Items > Ring of Protection | Magic Items > Ring of Invisibility | Magic Items > Cloak of Elvenkind | Magic Items > Ring of Elemental Command | Magic Items > Cloak of Invisibility | Magic Items > Cloak of the Bat | Magic Items > Ring of Warmth

<details><summary>full retrieved context</summary>

```
[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.

---

[Magic Items > Ring of Invisibility]
#### Ring of Invisibility  
_Ring, Legendary (Requires Attunement)_  
While wearing this ring, you can take a Magic action to give yourself the Invisible condition. You remain Invisible until the ring is removed or until you take a Bonus Action to become visible again.

---

[Magic Items > Cloak of Elvenkind]
#### Cloak of Elvenkind  
_Wondrous Item, Uncommon (Requires Attunement)_  
While you wear this cloak, Wisdom (Perception) checks made to perceive you have Disadvantage, and you have Advantage on Dexterity (Stealth) checks.

---

[Magic Items > Ring of Elemental Command]
**Elemental Bane.** While wearing the ring, you have Advantage on attack rolls against Elementals and they have Disadvantage on attack rolls against you.

---

[Magic Items > Cloak of Invisibility]
#### Cloak of Invisibility  
_Wondrous Item, Legendary (Requires Attunement)_  
This cloak has 3 charges and regains 1d3 expended charges daily at dawn. While wearing the cloak, you can take a Magic action to pull its hood over your
head and expend 1 charge to give yourself the Invisible condition for 1 hour. The effect ends early if you pull the hood down (no action required) or cease wearing the cloak.

---

[Magic Items > Cloak of the Bat]
#### Cloak of the Bat  
_Wondrous Item, Rare (Requires Attunement)_  
While wearing this cloak, you have Advantage on Dexterity (Stealth) checks. In an area of Dim Light or Darkness, you can grip the edges of the cloak and use it to gain a Fly Speed of 40 feet. If you ever fail to grip the cloak's edges while flying in this way, or if you are no longer in Dim Light or Darkness, you lose this Fly Speed.

---

[Magic Items > Ring of Warmth]
#### Ring of Warmth  
_Ring, Uncommon (Requires Attunement)_  
If you take Cold damage while wearing this ring, the ring reduces the damage you take by 2d8.  
In addition, while wearing this ring, you and everything you wear and carry are unharmed by temperatures of 0 degrees Fahrenheit or lower.
```
</details>


### v6_agentic  (16 chunks, 3 LLM call(s))

A Ring of Protection gives a +1 bonus to Armor Class and saving throws. A Cloak of Protection gives a +2 bonus to Armor Class and saving throws. They are both uncommon, but not the same rarity. The Ring of Protection is uncommon, while the Cloak of Protection is uncommon as well, but the question implies they are different items, so their exact rarity relative to each other is not specified in the context provided.

*facts found (judge): 3/3; missing: none*

*agentic sub-queries:* Ring of Protection / Cloak of Protection / bonus / rarity


*re-ranking* (query: `Ring of Protection`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.98 | yes | Magic Items > Ring of Protection |
| 2 | 8 | 4.70 | yes | Magic Items > Ring of Mind Shielding |
| 3 | 11 | 1.48 | yes | Magic Items > Ring of Mind Shielding |
| 4 | 2 | 0.27 |  | Magic Items > Ring of Warmth |
| 5 | 3 | -0.55 | yes | Magic Items > Ring of Evasion |
| 6 | 20 | -0.68 |  | Magic Items > Ring of Free Action |
| 7 | 6 | -1.06 |  | Magic Items > Ring of Invisibility |
| 8 | 17 | -1.25 |  | Magic Items > Ring of Elemental Command |
| 9 | 19 | -2.88 |  | Magic Items > Ring of Animal Influence |
| 10 | 15 | -3.21 |  | Magic Items > Ring of Regeneration |
| 11 | 10 | -3.29 | yes | Magic Items > Scarab of Protection |
| 12 | 9 | -3.90 |  | Magic Items > Ring of Jumping |
| 13 | 13 | -4.20 |  | Magic Items > Ring of Spell Turning |
| 14 | 4 | -4.33 |  | Magic Items > Ring of Feather Falling |
| 15 | 14 | -4.52 |  | Magic Items > Ring of Swimming |
| 16 | 16 | -4.84 | yes | Magic Items > Cloak of Protection |
| 17 | 18 | -4.86 |  | Magic Items > Ring of Spell Storing |
| 18 | 5 | -5.27 |  | Magic Items > Ring of Water Walking |
| 19 | 7 | -6.06 |  | Magic Items > Ring of Telekinesis |
| 20 | 12 | -6.96 |  | Magic Items > Ring of Three Wishes |


*re-ranking* (query: `Cloak of Protection`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.10 | yes | Magic Items > Cloak of Protection |
| 2 | 3 | 2.08 | yes | Magic Items > Cloak of Invisibility |
| 3 | 6 | 1.56 | yes | Magic Items > Cloak of Displacement |
| 4 | 2 | 1.23 |  | Magic Items > Cloak of Elvenkind |
| 5 | 5 | 0.69 |  | Magic Items > Cloak of the Bat |
| 6 | 9 | 0.18 |  | Magic Items > Cloak of Arachnida |
| 7 | 8 | -0.50 |  | Magic Items > Cloak of the Bat |
| 8 | 12 | -1.58 | yes | Magic Items > Scarab of Protection |
| 9 | 7 | -1.76 |  | Magic Items > Mantle of Spell Resistance |
| 10 | 4 | -1.91 |  | Magic Items > Cloak of the Manta Ray |
| 11 | 17 | -2.80 |  | Classes > Level 15: Smite of Protection |
| 12 | 16 | -3.35 |  | Magic Items > Cloak of Arachnida |
| 13 | 10 | -3.74 | yes | Magic Items > Ring of Protection |
| 14 | 13 | -4.94 |  | Spells > Protection from Evil and Good |
| 15 | 20 | -5.11 |  | Monsters A–Z > Bonus Actions |
| 16 | 18 | -5.14 |  | Monsters A–Z > Bonus Actions |
| 17 | 11 | -5.50 |  | Magic Items > Wings of Flying |
| 18 | 14 | -5.94 |  | Spells > Protection from Evil and Good |
| 19 | 15 | -6.08 |  | Rules Glossary > Cover |
| 20 | 19 | -10.33 |  | Magic Items > Armor of Invulnerability |


*re-ranking* (query: `bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 4.79 | yes | Rules Glossary > Bonus Action |
| 2 | 2 | 4.55 | yes | Playing the Game > Bonus Actions |
| 3 | 11 | 4.44 | yes | Playing the Game > Proficiency |
| 4 | 4 | 3.75 |  | Playing the Game > Bonus Actions |
| 5 | 8 | 2.85 |  | Playing the Game > The Bonus Doesn't Stack |
| 6 | 10 | 2.26 |  | Playing the Game > The Bonus Doesn't Stack |
| 7 | 17 | 1.63 |  | Monsters A–Z > Bonus Actions |
| 8 | 9 | 1.61 |  | Playing the Game > Proficiency Bonus |
| 9 | 20 | 1.57 |  | Monsters A–Z > Bonus Actions |
| 10 | 18 | 1.48 |  | Monsters A–Z > Bonus Actions |
| 11 | 14 | 1.47 |  | Monsters A–Z > Bonus Actions |
| 12 | 7 | 1.41 |  | Monsters A–Z > Bonus Actions |
| 13 | 15 | 1.41 |  | Monsters A–Z > Bonus Actions |
| 14 | 6 | 1.41 |  | Monsters A–Z > Bonus Actions |
| 15 | 16 | 1.35 |  | Monsters A–Z > Bonus Actions |
| 16 | 13 | 1.32 |  | Monsters A–Z > Bonus Actions |
| 17 | 12 | 1.29 |  | Monsters A–Z > Bonus Actions |
| 18 | 1 | 1.29 |  | Monsters A–Z > Bonus Actions |
| 19 | 5 | 1.10 |  | Monsters A–Z > Bonus Actions |
| 20 | 19 | 1.04 |  | Monsters A–Z > Bonus Actions |


*re-ranking* (query: `rarity`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.01 | yes | Magic Items > Magic Item Rarity |
| 2 | 4 | 3.57 | yes | Magic Items > Magic Item Values by Rarity |
| 3 | 6 | 1.94 | yes | Magic Items > Potion of Giant Strength |
| 4 | 15 | 1.86 |  | Magic Items > Potions of Healing |
| 5 | 9 | 1.78 |  | Magic Items > Magic Item Values by Rarity |
| 6 | 2 | 1.33 |  | Magic Items > Magic Item Values by Rarity |
| 7 | 7 | 1.27 |  | Magic Items > Hat of Many Spells |
| 8 | 5 | 1.13 |  | Magic Items > Magic Item Values by Rarity |
| 9 | 18 | 0.73 |  | Magic Items > Belt of Giant Strength |
| 10 | 3 | 0.72 |  | Magic Items > Feather Token |
| 11 | 8 | -0.01 |  | Magic Items > Ammunition, +1, +2, or +3 |
| 12 | 11 | -0.96 |  | Magic Items > Armor, +1, +2, or +3 |
| 13 | 10 | -1.30 |  | Magic Items > Shield, +1, +2, or +3 |
| 14 | 13 | -1.34 |  | Magic Items > Weapon, +1, +2, or +3 |
| 15 | 14 | -1.43 |  | Magic Items > Spell Scroll |
| 16 | 12 | -1.92 |  | Magic Items > Wand of the War Mage, +1, +2, or +3 |
| 17 | 19 | -6.70 |  | Magic Items > Ioun Stone |
| 18 | 20 | -8.29 |  | Magic Items > Spell Scroll |
| 19 | 16 | -10.19 |  | Magic Items > Rod of Security |
| 20 | 17 | -10.71 |  | Magic Items > Robe of Scintillating Colors |


*re-ranking* (query: `Ring of Protection bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.71 | yes | Magic Items > Ring of Protection |
| 2 | 6 | 0.89 | yes | Magic Items > Ring of the Ram |
| 3 | 12 | 0.08 | yes | Classes > Level 6: Aura of Protection |
| 4 | 4 | -0.11 |  | Magic Items > Ring of Invisibility |
| 5 | 9 | -0.45 |  | Magic Items > Ring of Spell Storing |
| 6 | 2 | -0.58 | yes | Magic Items > Scarab of Protection |
| 7 | 10 | -1.07 |  | Magic Items > Ring of the Ram |
| 8 | 3 | -1.15 | yes | Magic Items > Cloak of Protection |
| 9 | 17 | -1.73 |  | Magic Items > Scarab of Protection |
| 10 | 5 | -2.97 |  | Magic Items > Ring of Warmth |
| 11 | 16 | -3.24 |  | Magic Items > Ring of Elemental Command |
| 12 | 7 | -3.54 | yes | Magic Items > Ring of Evasion |
| 13 | 20 | -5.88 |  | Magic Items > Ring of Animal Influence |
| 14 | 11 | -6.17 |  | Magic Items > Ring of Regeneration |
| 15 | 13 | -6.79 |  | Magic Items > Ring of Spell Turning |
| 16 | 15 | -6.97 |  | Magic Items > Ring of Jumping |
| 17 | 14 | -7.73 |  | Magic Items > Ring of Feather Falling |
| 18 | 8 | -8.22 |  | Magic Items > Ring of Three Wishes |
| 19 | 18 | -8.23 |  | Magic Items > Ring of Water Walking |
| 20 | 19 | -8.82 |  | Magic Items > Ring of Telekinesis |


*re-ranking* (query: `Cloak of Protection bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.76 | yes | Magic Items > Cloak of Protection |
| 2 | 17 | 0.52 | yes | Classes > Level 6: Aura of Protection |
| 3 | 5 | 0.50 | yes | Magic Items > Scarab of Protection |
| 4 | 2 | 0.02 | yes | Magic Items > Ring of Protection |
| 5 | 15 | -0.01 |  | Magic Items > Scarab of Protection |
| 6 | 4 | -0.94 |  | Magic Items > Cloak of Elvenkind |
| 7 | 3 | -1.00 | yes | Magic Items > Cloak of Invisibility |
| 8 | 7 | -1.91 | yes | Magic Items > Cloak of Displacement |
| 9 | 13 | -1.98 |  | Rules Glossary > Cover |
| 10 | 16 | -2.03 |  | Classes > Level 20: Holy Nimbus |
| 11 | 8 | -2.18 |  | Magic Items > Cloak of the Bat |
| 12 | 10 | -2.43 |  | Magic Items > Cloak of Arachnida |
| 13 | 6 | -3.65 |  | Magic Items > Mantle of Spell Resistance |
| 14 | 11 | -4.53 |  | Magic Items > Cloak of the Bat |
| 15 | 9 | -4.85 |  | Magic Items > Cloak of the Manta Ray |
| 16 | 12 | -5.81 |  | Classes > Level 15: Smite of Protection |
| 17 | 20 | -6.14 |  | Magic Items > Defender |
| 18 | 19 | -6.87 |  | Spells > Protection from Evil and Good |
| 19 | 14 | -7.79 |  | Magic Items > Wings of Flying |
| 20 | 18 | -9.36 |  | Classes > Level 18: Aura Expansion |


*re-ranking* (query: `rarity of Ring of Protection`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -0.95 | yes | Magic Items > Ring of Protection |
| 2 | 15 | -1.78 | yes | Magic Items > Ring of Mind Shielding |
| 3 | 3 | -5.00 | yes | Magic Items > Ring of Evasion |
| 4 | 18 | -5.16 |  | Magic Items > Ring of Regeneration |
| 5 | 2 | -5.33 |  | Magic Items > Ring of Warmth |
| 6 | 20 | -6.75 |  | Magic Items > Ring of Animal Influence |
| 7 | 6 | -6.84 |  | Magic Items > Ring of Invisibility |
| 8 | 14 | -7.27 |  | Magic Items > Ring of the Ram |
| 9 | 4 | -7.40 |  | Magic Items > Ring of Spell Storing |
| 10 | 5 | -7.65 |  | Magic Items > Ring of Feather Falling |
| 11 | 8 | -8.52 | yes | Magic Items > Scarab of Protection |
| 12 | 9 | -9.00 |  | Magic Items > Ring of Telekinesis |
| 13 | 16 | -9.22 |  | Magic Items > Ring of Elemental Command |
| 14 | 13 | -9.81 |  | Magic Items > Ring of Jumping |
| 15 | 12 | -9.96 |  | Magic Items > Ring of Spell Turning |
| 16 | 11 | -10.02 |  | Magic Items > Ring of Spell Storing |
| 17 | 17 | -10.07 |  | Magic Items > Ring of Elemental Command |
| 18 | 7 | -10.24 | yes | Magic Items > Cloak of Protection |
| 19 | 19 | -10.53 |  | Magic Items > Ring of Water Walking |
| 20 | 10 | -10.85 |  | Magic Items > Ring of Three Wishes |


*re-ranking* (query: `rarity of Cloak of Protection`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.41 | yes | Magic Items > Cloak of Protection |
| 2 | 6 | -2.29 | yes | Magic Items > Cloak of Displacement |
| 3 | 8 | -2.66 |  | Magic Items > Cloak of Arachnida |
| 4 | 4 | -2.84 |  | Magic Items > Cloak of the Bat |
| 5 | 5 | -3.12 | yes | Magic Items > Cloak of Invisibility |
| 6 | 14 | -3.20 |  | Magic Items > Shield, +1, +2, or +3 |
| 7 | 18 | -4.39 |  | Classes > Level 15: Smite of Protection |
| 8 | 2 | -4.47 |  | Magic Items > Cloak of Elvenkind |
| 9 | 7 | -6.43 |  | Magic Items > Mantle of Spell Resistance |
| 10 | 19 | -6.63 | yes | Magic Items > Magic Item Rarity |
| 11 | 11 | -6.67 | yes | Magic Items > Scarab of Protection |
| 12 | 10 | -6.83 |  | Magic Items > Cloak of the Bat |
| 13 | 20 | -7.24 |  | Magic Items > Potions of Healing |
| 14 | 3 | -7.48 |  | Magic Items > Cloak of the Manta Ray |
| 15 | 13 | -8.70 |  | Magic Items > Armor, +1, +2, or +3 |
| 16 | 12 | -8.93 |  | Magic Items > Wings of Flying |
| 17 | 16 | -9.00 |  | Magic Items > Hat of Many Spells |
| 18 | 15 | -9.10 |  | Spells > Protection from Evil and Good |
| 19 | 9 | -9.34 | yes | Magic Items > Ring of Protection |
| 20 | 17 | -9.65 |  | Magic Items > Magic Item Values by Rarity |

*retrieved sections:* Magic Items > Ring of Protection | Magic Items > Ring of Mind Shielding | Magic Items > Cloak of Protection | Magic Items > Cloak of Invisibility | Magic Items > Cloak of Displacement | Rules Glossary > Bonus Action | Playing the Game > Bonus Actions | Playing the Game > Proficiency | Magic Items > Magic Item Rarity | Magic Items > Magic Item Values by Rarity | Magic Items > Potion of Giant Strength | Magic Items > Ring of the Ram | Classes > Level 6: Aura of Protection | Magic Items > Scarab of Protection | Magic Items > Ring of Evasion

<details><summary>full retrieved context</summary>

```
[Magic Items > Ring of Protection]
#### Ring of Protection  
_Ring, Uncommon (Requires Attunement)_  
You gain a +1 bonus to Armor Class and saving throws while wearing this ring.

---

[Magic Items > Ring of Mind Shielding]
#### Ring of Mind Shielding  
_Ring, Uncommon (Requires Attunement)_  
While wearing this ring, you are immune to magic that allows other creatures to read your thoughts, determine whether you are lying, know your alignment, or know your creature type. Creatures can telepathically communicate with you only if you allow it.

---

[Magic Items > Ring of Mind Shielding]
You can take a Magic action to cause the ring to become imperceptible until you take another Magic action to make it perceptible, until you remove the ring, or until you die.  
If you die while wearing the ring, your soul enters it, unless it already houses a soul. You can remain in the ring or depart for the afterlife. As long as your soul is in the ring, you can telepathically communicate with any creature wearing it. A wearer can't prevent this telepathic communication.

---

[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

---

[Magic Items > Cloak of Invisibility]
#### Cloak of Invisibility  
_Wondrous Item, Legendary (Requires Attunement)_  
This cloak has 3 charges and regains 1d3 expended charges daily at dawn. While wearing the cloak, you can take a Magic action to pull its hood over your
head and expend 1 charge to give yourself the Invisible condition for 1 hour. The effect ends early if you pull the hood down (no action required) or cease wearing the cloak.

---

[Magic Items > Cloak of Displacement]
#### Cloak of Displacement  
_Wondrous Item, Rare (Requires Attunement)_  
While you wear this cloak, it magically projects an illusion that makes you appear to be standing in a place near your actual location, causing any creature to have Disadvantage on attack rolls against you. If you take damage, the property ceases to function until the start of your next turn. This property is suppressed while your Speed is 0.

---

[Rules Glossary > Bonus Action]
#### Bonus Action  
A Bonus Action is a special action that you can take on the same turn that you take an action. You can't take more than one Bonus Action on a turn, and you have a Bonus Action to take only if a rule explicitly says so. _See also_ "Playing the Game" ("Actions").

---

[Playing the Game > Bonus Actions]
### Bonus Actions  
Various class features, spells, and other abilities let you take an additional action on your turn called a Bonus Action. The Cunning Action feature, for example, allows a Rogue to take a Bonus Action. You can take a Bonus Action only when a special ability, a spell, or another feature of the game states that you can do something as a Bonus Action. You otherwise don't have a Bonus Action to take.

---

[Playing the Game > Proficiency]
This bonus is applied to a D20 Test when the creature has proficiency in a skill, in a saving throw, or with an item that the creature uses to make the D20 Test. The bonus is also used for spell attacks and for calculating the DC of saving throws for spells.  
**Proficiency Bonus**  
<table>
<thead>
<tr>
<th>Level or CR</th>
<th>Bonus</th>
<th>Level or CR</th>
<th>Bonus</th>
</tr>
</thead>
<tbody>
<tr>
<td>Up to 4</td>
<td>+2</td>
<td>17–20</td>
<td>+6</td>
</tr>
<tr>
<td>5–8</td>
<td>+3</td>

---

[Magic Items > Magic Item Rarity]
## Magic Item Rarity  
Every magic item has a rarity, which provides a rough measure of an item's power relative to other magic items. The rarities are shown in the Magic Item Rarities and Values table.  
Common magic items, such as a _Potion of Healing_, are the most plentiful. Artifacts, such as the _Dragon Orb_, are priceless, unique, and difficult to acquire.

---

[Magic Items > Magic Item Values by Rarity]
Common magic items can often be bought in a town or city. Uncommon and Rare magic items are usually found only in cities, and rarer magic items might be sold only in wondrous locations, such as a city on another plane of existence. If you allow characters to buy and sell magic items in your campaign, rarity can help you set prices for those items. Gold Piece values are provided in the Magic Item Rarities and Values table, though a seller might ask for a service rather than coin as payment.

---

[Magic Items > Potion of Giant Strength]
#### Potion of Giant Strength  
_Potion, Rarity Varies_  
When you drink this potion, your Strength score changes for 1 hour. The type of giant determines the score (see the table below). The potion has no effect on you if your Strength is equal to or greater than that score.  
This potion's transparent liquid has floating in it a sliver of light resembling a giant's fingernail.  
<table>
<thead>
<tr>
<th>Potion</th>
<th>Str.</th>
<th>Rarity</th>
</tr>
</thead>
<tbody>
<tr>

---

[Magic Items > Ring of the Ram]
Alternatively, you can expend 1 to 3 of the ring's charges as a Magic action to try to break a nonmagical object you can see within 60 feet of yourself that isn't being worn or carried. The ring makes a Strength check with a +5 bonus for each charge you spend.

---

[Classes > Level 6: Aura of Protection]
#### Level 6: Aura of Protection  
You radiate a protective, unseeable aura in a 10-foot Emanation that originates from you. The aura is inactive while you have the Incapacitated condition.  
You and your allies in the aura gain a bonus to saving throws equal to your Charisma modifier (minimum bonus of +1).  
If another Paladin is present, a creature can benefit from only one Aura of Protection at a time; the creature chooses which aura while in them.

---

[Magic Items > Scarab of Protection]
#### Scarab of Protection  
_Wondrous Item, Legendary (Requires Attunement)_  
This beetle-shaped medallion provides three benefits while it is on your person.  
_Defense._ You gain a +1 bonus to Armor Class.

---

[Magic Items > Ring of Evasion]
#### Ring of Evasion  
_Ring, Rare (Requires Attunement)_  
This ring has 3 charges, and it regains 1d3 expended charges daily at dawn. When you fail a Dexterity saving throw while wearing the ring, you can take a Reaction to expend 1 charge to succeed on that save instead.
```
</details>


---

## q13 (multi-part) What are the options for generating ability scores in character creation: give the Standard Array, the point-buy budget with the cost of a score of 14, and the random method.

**Gold facts (counterfactual data):** 15, 14, 13, 12, 10, 8; 30 points; 14 costs 7; four d6s


### v0_closed_book  (0 chunks, 1 LLM call(s))

Sure, here are the options for generating ability scores in character creation for Dungeons & Dragons 5th Edition:

1. **Standard Array**: 
   - The standard array is {15, 14, 13, 12, 10, 8}.

2. **Point Buy**:
   - The point buy system allows you to spend points to assign ability scores. Each score of 14 costs 2 points.

3. **Random Method**:
   - Roll four six-sided dice and drop the lowest die, then sum the remaining three dice for each ability score. Repeat this process for all six abilities.

*facts found (judge): 2/4; missing: 30 points; 14 costs 7*


### v1_baseline  (3 chunks, 1 LLM call(s))

The options for generating ability scores in character creation are:

- **Standard Array:** 15, 14, 13, 12, 10, 8
- **Point-Buy Budget:** 30 points (a score of 14 costs 7 points)
- **Random Method:** Roll four d6s and sum the highest three dice, repeat this five more times to get six numbers

*facts found (judge): 4/4; missing: none*

*retrieved sections:* Character Creation > Assign Ability Scores | Character Creation > Generate Your Scores

<details><summary>full retrieved context</summary>

```
[Character Creation > Assign Ability Scores]
#### Assign Ability Scores  
Once you've generated six scores, assign them to Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma, keeping in mind your class's primary ability. Fill in the ability modifiers as well.

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>

---

[Character Creation > Generate Your Scores]
#### Generate Your Scores  
Determine your ability scores by using one of the following three methods. Your GM might prefer you to use a particular one.  
_Standard Array._ Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.  
_Random Generation._ Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The options for generating ability scores in character creation are:

- **Standard Array:** Use the scores 15, 14, 13, 12, 10, 8.
- **Point Cost:** You have 30 points to spend, with a score of 14 costing 7 points.
- **Random Generation:** Roll four d6s and sum the highest three dice, repeating this process five more times to get six scores.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the options for generating ability scores in character creation: give t`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 3.56 | yes | Character Creation > Generate Your Scores |
| 2 | 4 | 3.54 | yes | Character Creation > Assign Ability Scores |
| 3 | 2 | 3.38 | yes | Character Creation > Generate Your Scores |
| 4 | 7 | 0.73 |  | Character Creation > Step 3: Ability Scores |
| 5 | 1 | 0.05 |  | Character Creation > Assign Ability Scores |
| 6 | 8 | -0.67 |  | Character Creation > Adjust Ability Scores |
| 7 | 6 | -2.21 |  | Character Creation > Generate Your Scores |
| 8 | 5 | -2.50 |  | Character Origins > Ability Scores |
| 9 | 10 | -3.73 |  | Character Creation > Fill In Numbers |
| 10 | 9 | -4.26 |  | Character Creation > Gaining a Level |

*retrieved sections:* Character Creation > Generate Your Scores | Character Creation > Assign Ability Scores

<details><summary>full retrieved context</summary>

```
[Character Creation > Generate Your Scores]
#### Generate Your Scores  
Determine your ability scores by using one of the following three methods. Your GM might prefer you to use a particular one.  
_Standard Array._ Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.  
_Random Generation._ Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

---

[Character Creation > Assign Ability Scores]
If you're using the Standard Array option, consult the Standard Array by Class table for suggestions on where to assign scores for your character's class. The table puts the highest scores in a class's main abilities. If you used a different method to generate the scores, you may still use this table to guide where you place your highest and lowest scores.  
**Standard Array by Class**  
<table>
<thead>
<tr>
<th>Class</th>
<th>Str.</th>
<th>Dex.</th>
<th>Con.</th>
<th>Int.</th>
<th>Wis.</th>

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The options for generating ability scores in character creation are:

- **Standard Array:** Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.
- **Point Buy:** You have 30 points to spend on your ability scores. A score of 14 costs 7 points.
- **Random Generation:** Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the options for generating ability scores in character creation: give t`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 3.56 | yes | Character Creation > Generate Your Scores |
| 2 | 4 | 3.54 | yes | Character Creation > Assign Ability Scores |
| 3 | 2 | 3.38 | yes | Character Creation > Generate Your Scores |
| 4 | 7 | 0.73 | yes | Character Creation > Step 3: Ability Scores |
| 5 | 1 | 0.05 | yes | Character Creation > Assign Ability Scores |
| 6 | 8 | -0.67 | yes | Character Creation > Adjust Ability Scores |
| 7 | 6 | -2.21 | yes | Character Creation > Generate Your Scores |
| 8 | 5 | -2.50 | yes | Character Origins > Ability Scores |
| 9 | 10 | -3.73 |  | Character Creation > Fill In Numbers |
| 10 | 9 | -4.26 |  | Character Creation > Gaining a Level |

*retrieved sections:* Character Creation > Generate Your Scores | Character Creation > Assign Ability Scores | Character Creation > Step 3: Ability Scores | Character Creation > Adjust Ability Scores | Character Origins > Ability Scores

<details><summary>full retrieved context</summary>

```
[Character Creation > Generate Your Scores]
#### Generate Your Scores  
Determine your ability scores by using one of the following three methods. Your GM might prefer you to use a particular one.  
_Standard Array._ Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.  
_Random Generation._ Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

---

[Character Creation > Assign Ability Scores]
If you're using the Standard Array option, consult the Standard Array by Class table for suggestions on where to assign scores for your character's class. The table puts the highest scores in a class's main abilities. If you used a different method to generate the scores, you may still use this table to guide where you place your highest and lowest scores.  
**Standard Array by Class**  
<table>
<thead>
<tr>
<th>Class</th>
<th>Str.</th>
<th>Dex.</th>
<th>Con.</th>
<th>Int.</th>
<th>Wis.</th>

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>

---

[Character Creation > Step 3: Ability Scores]
### Step 3: Ability Scores  
To determine your character's ability scores, you first generate a set of six numbers using the instructions below and then assign them to your six abilities. "Playing the Game" explains what each ability means.

---

[Character Creation > Assign Ability Scores]
#### Assign Ability Scores  
Once you've generated six scores, assign them to Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma, keeping in mind your class's primary ability. Fill in the ability modifiers as well.

---

[Character Creation > Adjust Ability Scores]
#### Adjust Ability Scores  
After assigning your ability scores, adjust them according to your background. Your background lists three abilities; increase one of those scores by 2 and a different one by 1, or increase all three by 1. None of these increases can raise a score above 20.  
Some players like to increase their class's primary ability, while others prefer to increase a low score.

---

[Character Creation > Generate Your Scores]
<td>2</td>
<td>14</td>
<td>7</td>
</tr>
<tr>
<td>11</td>
<td>3</td>
<td>15</td>
<td>9</td>
</tr>
</tbody>
</table>

---

[Character Origins > Ability Scores]
#### Ability Scores  
A background lists three of your character's ability scores. Increase one by 2 and another one by 1, or increase all three by 1. None of these increases can raise a score above 20.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The options for generating ability scores in character creation are:

- **Standard Array:** Use the scores 15, 14, 13, 12, 10, 8.
- **Point Cost:** You have 30 points to spend, with a score of 14 costing 7 points.
- **Random Generation:** Roll four d6s and sum the highest three dice, repeating this process five more times to get six scores.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the options for generating ability scores in character creation: give t`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 3.56 | yes | Character Creation > Generate Your Scores |
| 2 | 4 | 3.54 | yes | Character Creation > Assign Ability Scores |
| 3 | 2 | 3.38 | yes | Character Creation > Generate Your Scores |
| 4 | 7 | 0.73 |  | Character Creation > Step 3: Ability Scores |
| 5 | 1 | 0.05 |  | Character Creation > Assign Ability Scores |
| 6 | 8 | -0.67 |  | Character Creation > Adjust Ability Scores |
| 7 | 6 | -2.21 |  | Character Creation > Generate Your Scores |
| 8 | 5 | -2.50 |  | Character Origins > Ability Scores |
| 9 | 10 | -3.73 |  | Character Creation > Fill In Numbers |
| 10 | 9 | -4.26 |  | Character Creation > Gaining a Level |

*retrieved sections:* Character Creation > Generate Your Scores | Character Creation > Assign Ability Scores

<details><summary>full retrieved context</summary>

```
[Character Creation > Generate Your Scores]
#### Generate Your Scores  
Determine your ability scores by using one of the following three methods. Your GM might prefer you to use a particular one.  
_Standard Array._ Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.  
_Random Generation._ Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

---

[Character Creation > Assign Ability Scores]
If you're using the Standard Array option, consult the Standard Array by Class table for suggestions on where to assign scores for your character's class. The table puts the highest scores in a class's main abilities. If you used a different method to generate the scores, you may still use this table to guide where you place your highest and lowest scores.  
**Standard Array by Class**  
<table>
<thead>
<tr>
<th>Class</th>
<th>Str.</th>
<th>Dex.</th>
<th>Con.</th>
<th>Int.</th>
<th>Wis.</th>

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The options for generating ability scores in character creation are:

- **Standard Array**: Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.
- **Point Cost**: You have 30 points to spend on your ability scores. A score of 14 costs 7 points.
- **Random Generation**: Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the options for generating ability scores in character creation: give t`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 3.56 | yes | Character Creation > Generate Your Scores |
| 2 | 1 | 3.54 | yes | Character Creation > Assign Ability Scores |
| 3 | 2 | 3.38 | yes | Character Creation > Generate Your Scores |
| 4 | 4 | 0.73 | yes | Character Creation > Step 3: Ability Scores |
| 5 | 5 | 0.05 | yes | Character Creation > Assign Ability Scores |
| 6 | 6 | -0.67 | yes | Character Creation > Adjust Ability Scores |
| 7 | 17 | -1.09 | yes | Character Creation > Choose a Background |
| 8 | 9 | -1.35 | yes | Character Creation > Determine Ability Modifiers |
| 9 | 8 | -2.19 |  | Character Creation > Gaining a Level |
| 10 | 20 | -2.21 |  | Character Creation > Generate Your Scores |
| 11 | 23 | -2.29 |  | Character Creation > Determine Ability Modifiers |
| 12 | 7 | -2.50 |  | Character Origins > Ability Scores |
| 13 | 10 | -3.56 |  | Character Creation > Prerequisites |
| 14 | 15 | -3.73 |  | Character Creation > Fill In Numbers |
| 15 | 29 | -3.90 |  | Character Creation > Experience Points |
| 16 | 11 | -4.26 |  | Character Creation > Gaining a Level |
| 17 | 22 | -4.45 |  | Character Creation > Fill In Numbers |
| 18 | 21 | -4.53 |  | Character Creation > Create Your Character |
| 19 | 25 | -4.56 |  | Character Creation > Level Advancement |
| 20 | 13 | -4.91 |  | Playing the Game > Ability Scores |

*retrieved sections:* Character Creation > Generate Your Scores | Character Creation > Assign Ability Scores | Character Creation > Step 3: Ability Scores | Character Creation > Adjust Ability Scores | Character Creation > Choose a Background | Character Creation > Determine Ability Modifiers

<details><summary>full retrieved context</summary>

```
[Character Creation > Generate Your Scores]
#### Generate Your Scores  
Determine your ability scores by using one of the following three methods. Your GM might prefer you to use a particular one.  
_Standard Array._ Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.  
_Random Generation._ Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

---

[Character Creation > Assign Ability Scores]
If you're using the Standard Array option, consult the Standard Array by Class table for suggestions on where to assign scores for your character's class. The table puts the highest scores in a class's main abilities. If you used a different method to generate the scores, you may still use this table to guide where you place your highest and lowest scores.  
**Standard Array by Class**  
<table>
<thead>
<tr>
<th>Class</th>
<th>Str.</th>
<th>Dex.</th>
<th>Con.</th>
<th>Int.</th>
<th>Wis.</th>

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>

---

[Character Creation > Step 3: Ability Scores]
### Step 3: Ability Scores  
To determine your character's ability scores, you first generate a set of six numbers using the instructions below and then assign them to your six abilities. "Playing the Game" explains what each ability means.

---

[Character Creation > Assign Ability Scores]
#### Assign Ability Scores  
Once you've generated six scores, assign them to Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma, keeping in mind your class's primary ability. Fill in the ability modifiers as well.

---

[Character Creation > Adjust Ability Scores]
#### Adjust Ability Scores  
After assigning your ability scores, adjust them according to your background. Your background lists three abilities; increase one of those scores by 2 and a different one by 1, or increase all three by 1. None of these increases can raise a score above 20.  
Some players like to increase their class's primary ability, while others prefer to increase a low score.

---

[Character Creation > Choose a Background]
The background you choose influences step 3, when you determine your character's ability scores. If you're having trouble choosing, the Ability Scores and Backgrounds table shows which backgrounds benefit which ability scores. Look for your class's primary ability there.  
**Ability Scores and Backgrounds**  
<table>
<thead>
<tr>
<th>Ability</th>
<th>Background</th>
</tr>
</thead>
<tbody>
<tr>
<td>Strength</td>
<td>Soldier</td>
</tr>
<tr>
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>

---

[Character Creation > Determine Ability Modifiers]
#### Determine Ability Modifiers  
Finally, determine your ability modifiers using the Ability Scores and Modifiers table. Write the modifier next to each of your scores.  
**Ability Scores and Modifiers**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Modifier</th>
<th>Score</th>
<th>Modifier</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>−4</td>
<td>12–13</td>
<td>+1</td>
</tr>
<tr>
<td>4–5</td>
<td>−3</td>
<td>14–15</td>
<td>+2</td>
</tr>
<tr>
<td>6–7</td>
<td>−2</td>
<td>16–17</td>
<td>+3</td>
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The options for generating ability scores in character creation are:

- **Standard Array:** Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.
- **Point Cost:** You have 30 points to spend on your ability scores. A score of 14 costs 7 points.
- **Random Generation:** Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the options for generating ability scores in character creation: give t`): candidate pool of 18, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 3.56 | yes | Character Creation > Generate Your Scores |
| 2 | 1 | 3.54 | yes | Character Creation > Assign Ability Scores |
| 3 | 2 | 3.38 | yes | Character Creation > Generate Your Scores |
| 4 | 4 | 0.73 | yes | Character Creation > Step 3: Ability Scores |
| 5 | 5 | 0.05 | yes | Character Creation > Assign Ability Scores |
| 6 | 6 | -0.67 | yes | Character Creation > Adjust Ability Scores |
| 7 | 9 | -1.35 | yes | Character Creation > Determine Ability Modifiers |
| 8 | 8 | -2.19 | yes | Character Creation > Gaining a Level |
| 9 | 7 | -2.50 |  | Character Origins > Ability Scores |
| 10 | 10 | -3.56 |  | Character Creation > Prerequisites |
| 11 | 12 | -4.91 |  | Playing the Game > Ability Scores |
| 12 | 11 | -5.97 |  | Monsters > Ability Scores |
| 13 | 17 | -6.81 |  | Playing the Game > Ability Modifiers |
| 14 | 18 | -7.26 |  | Playing the Game > Ability Modifiers |
| 15 | 16 | -7.40 |  | Magic Items > Abilities |
| 16 | 13 | -9.99 |  | Spells > Creation |
| 17 | 14 | -10.73 |  | Spells > Creation |
| 18 | 15 | -11.06 |  | Spells > Creation |

*retrieved sections:* Character Creation > Generate Your Scores | Character Creation > Assign Ability Scores | Character Creation > Step 3: Ability Scores | Character Creation > Adjust Ability Scores | Character Creation > Determine Ability Modifiers | Character Creation > Gaining a Level

<details><summary>full retrieved context</summary>

```
[Character Creation > Generate Your Scores]
#### Generate Your Scores  
Determine your ability scores by using one of the following three methods. Your GM might prefer you to use a particular one.  
_Standard Array._ Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.  
_Random Generation._ Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

---

[Character Creation > Assign Ability Scores]
If you're using the Standard Array option, consult the Standard Array by Class table for suggestions on where to assign scores for your character's class. The table puts the highest scores in a class's main abilities. If you used a different method to generate the scores, you may still use this table to guide where you place your highest and lowest scores.  
**Standard Array by Class**  
<table>
<thead>
<tr>
<th>Class</th>
<th>Str.</th>
<th>Dex.</th>
<th>Con.</th>
<th>Int.</th>
<th>Wis.</th>

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>

---

[Character Creation > Step 3: Ability Scores]
### Step 3: Ability Scores  
To determine your character's ability scores, you first generate a set of six numbers using the instructions below and then assign them to your six abilities. "Playing the Game" explains what each ability means.

---

[Character Creation > Assign Ability Scores]
#### Assign Ability Scores  
Once you've generated six scores, assign them to Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma, keeping in mind your class's primary ability. Fill in the ability modifiers as well.

---

[Character Creation > Adjust Ability Scores]
#### Adjust Ability Scores  
After assigning your ability scores, adjust them according to your background. Your background lists three abilities; increase one of those scores by 2 and a different one by 1, or increase all three by 1. None of these increases can raise a score above 20.  
Some players like to increase their class's primary ability, while others prefer to increase a low score.

---

[Character Creation > Determine Ability Modifiers]
#### Determine Ability Modifiers  
Finally, determine your ability modifiers using the Ability Scores and Modifiers table. Write the modifier next to each of your scores.  
**Ability Scores and Modifiers**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Modifier</th>
<th>Score</th>
<th>Modifier</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>−4</td>
<td>12–13</td>
<td>+1</td>
</tr>
<tr>
<td>4–5</td>
<td>−3</td>
<td>14–15</td>
<td>+2</td>
</tr>
<tr>
<td>6–7</td>
<td>−2</td>
<td>16–17</td>
<td>+3</td>

---

[Character Creation > Gaining a Level]
**5: Adjust Ability Modifiers.** If you choose a feat that increases one or more of your ability scores, your ability modifier also changes if the new score is an even number. When that happens, adjust all the numbers on your character sheet that use that ability modifier. When your Constitution modifier increases by 1, your Hit Point maximum increases by 1 for each level you have attained. For example, if a character reaches level 8 and increases their Constitution score from 17 to 18, the
```
</details>


### v6_agentic  (11 chunks, 3 LLM call(s))

The options for generating ability scores in character creation are:

- **Standard Array:** Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.
- **Point Buy:** You have 30 points to spend on your ability scores. A score of 14 costs 7 points.
- **Random Generation:** Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Standard Array / Point-buy Budget / Random Method


*re-ranking* (query: `Standard Array`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.34 | yes | Character Creation > Assign Ability Scores |
| 2 | 3 | 1.82 | yes | Character Creation > Generate Your Scores |
| 3 | 5 | -6.01 | yes | Character Creation > Choose Languages |
| 4 | 15 | -8.73 |  | Magic Items > Special Purpose |
| 5 | 7 | -8.98 |  | Magic Items > Special Purpose |
| 6 | 11 | -9.66 |  | Spells > Color Spray |
| 7 | 9 | -9.74 |  | Character Creation > Starting Equipment |
| 8 | 13 | -10.24 |  | Character Creation > Choose Languages |
| 9 | 6 | -11.06 |  | Equipment > Manacles (2 GP) |
| 10 | 17 | -11.19 |  | Equipment > Properties |
| 11 | 8 | -11.20 |  | Equipment > Properties |
| 12 | 19 | -11.26 |  | Classes > Wizard Spell List |
| 13 | 14 | -11.33 |  | Magic Items > Efficient Quiver |
| 14 | 20 | -11.35 |  | Character Origins > Sage |
| 15 | 10 | -11.36 |  | Magic Items > Oathbow |
| 16 | 16 | -11.36 |  | Spells > Magic Missile |
| 17 | 12 | -11.38 |  | Magic Items > Elemental Gem |
| 18 | 4 | -11.40 |  | Magic Items > Magic Item Values by Rarity |
| 19 | 18 | -11.42 |  | Magic Items > Spells Cast from Items |
| 20 | 2 | -11.44 |  | Equipment > Properties |


*re-ranking* (query: `Point-buy Budget`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | -6.32 | yes | Character Creation > Generate Your Scores |
| 2 | 14 | -8.90 | yes | Gameplay Toolbox > Step 3: Spend Your Budget |
| 3 | 11 | -9.13 | yes | Gameplay Toolbox > Step 3: Spend Your Budget |
| 4 | 13 | -9.41 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 5 | 7 | -9.62 |  | Gameplay Toolbox > Step 2: Determine Your XP Budget |
| 6 | 9 | -10.37 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 7 | 1 | -10.51 |  | Character Creation > Starting Equipment |
| 8 | 12 | -10.65 |  | Character Creation > Experience Points |
| 9 | 17 | -10.83 |  | Equipment > Time |
| 10 | 16 | -10.97 |  | Equipment > Ammunition (Varies) |
| 11 | 5 | -11.06 |  | Classes > Distant Spell |
| 12 | 15 | -11.10 |  | Equipment > Food, Drink, and Lodging |
| 13 | 3 | -11.17 |  | Classes > Subtle Spell |
| 14 | 6 | -11.22 |  | Classes > Extended Spell |
| 15 | 19 | -11.23 |  | Rules Glossary > Cone [Area of Effect] |
| 16 | 10 | -11.24 |  | Equipment > Weapons |
| 17 | 20 | -11.31 |  | Equipment > Aristocratic (10 GP per Day) |
| 18 | 4 | -11.33 |  | Character Creation > Hit Points and Hit Point Dice |
| 19 | 8 | -11.39 |  | Equipment > Poor (2 SP per Day) |
| 20 | 18 | -11.43 |  | Equipment > Artisan's Tools |


*re-ranking* (query: `Random Method`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | -2.89 | yes | Magic Items > Hat of Many Spells |
| 2 | 4 | -4.04 | yes | Magic Items > Deck of Illusions |
| 3 | 17 | -4.22 | yes | Magic Items > Amulet of the Planes |
| 4 | 1 | -5.14 |  | Magic Items > Amulet of the Planes |
| 5 | 7 | -5.30 |  | Spells > Confusion |
| 6 | 2 | -5.56 |  | Magic Items > Hat of Many Spells |
| 7 | 11 | -5.92 |  | Magic Items > Mysterious Deck |
| 8 | 12 | -6.08 |  | Magic Items > Sphere of Annihilation |
| 9 | 5 | -6.56 |  | Magic Items > Staff of the Magi |
| 10 | 6 | -6.74 |  | Magic Items > Staff of Power |
| 11 | 18 | -6.93 |  | Magic Items > Bag of Beans |
| 12 | 14 | -7.67 |  | Spells > Gaseous Form |
| 13 | 20 | -8.22 |  | Magic Items > Potion of Resistance |
| 14 | 8 | -8.57 |  | Magic Items > Amulet of the Planes |
| 15 | 15 | -9.29 |  | Magic Items > Wand of Wonder |
| 16 | 9 | -9.41 |  | Magic Items > Abilities |
| 17 | 19 | -9.51 | yes | Character Creation > Assign Ability Scores |
| 18 | 10 | -10.24 |  | Magic Items > Dimensional Shackles |
| 19 | 16 | -10.44 |  | Magic Items > Bag of Beans |
| 20 | 13 | -10.96 |  | Magic Items > Luck Blade |


*re-ranking* (query: `Standard Array by Class`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.98 | yes | Character Creation > Assign Ability Scores |
| 2 | 9 | -1.09 | yes | Character Creation > Generate Your Scores |
| 3 | 13 | -8.84 | yes | Character Creation > Choose Languages |
| 4 | 19 | -8.95 |  | Character Creation > Fill In Numbers |
| 5 | 18 | -9.02 |  | Classes > Wizard Class Features |
| 6 | 15 | -9.75 |  | Playing the Game > Difficulty Class |
| 7 | 2 | -9.81 |  | Character Creation > Fill In Numbers |
| 8 | 8 | -9.86 |  | Classes > Level 3: Draconic Resilience |
| 9 | 11 | -10.03 |  | Character Creation > Choose Languages |
| 10 | 3 | -10.27 |  | Character Creation > Armor Class |
| 11 | 4 | -10.39 |  | Magic Items > Shield, +1, +2, or +3 |
| 12 | 6 | -10.50 |  | Magic Items > Armor, +1, +2, or +3 |
| 13 | 14 | -10.51 |  | Classes > Sorcerer |
| 14 | 7 | -10.62 |  | Character Creation > Proficiencies |
| 15 | 10 | -10.73 |  | Classes > Paladin |
| 16 | 17 | -10.73 |  | Magic Items > Special Purpose |
| 17 | 16 | -10.74 |  | Classes > Level 3: Land's Aid |
| 18 | 20 | -10.77 |  | Classes > Wizard |
| 19 | 12 | -10.78 |  | Playing the Game > Armor Class |
| 20 | 5 | -10.78 |  | Character Creation > Create Your Character |


*re-ranking* (query: `Ability Score Point Costs`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 8.30 | yes | Character Creation > Generate Your Scores |
| 2 | 2 | -0.35 | yes | Playing the Game > Ability Scores |
| 3 | 19 | -2.17 | yes | Playing the Game > Ability Scores |
| 4 | 8 | -3.73 |  | Character Origins > Ability Scores |
| 5 | 4 | -3.98 |  | Character Creation > Gaining a Level |
| 6 | 3 | -4.03 |  | Feats > Ability Score Improvement |
| 7 | 5 | -4.64 |  | Character Creation > Adjust Ability Scores |
| 8 | 17 | -4.83 |  | Classes > Level 4: Ability Score Improvement |
| 9 | 20 | -4.90 |  | Classes > Level 4: Ability Score Improvement |
| 10 | 15 | -4.99 |  | Classes > Level 4: Ability Score Improvement |
| 11 | 6 | -5.01 |  | Classes > Level 4: Ability Score Improvement |
| 12 | 14 | -5.04 |  | Classes > Level 4: Ability Score Improvement |
| 13 | 10 | -5.04 |  | Classes > Level 4: Ability Score Improvement |
| 14 | 16 | -5.07 |  | Classes > Level 4: Ability Score Improvement |
| 15 | 13 | -5.15 |  | Classes > Level 4: Ability Score Improvement |
| 16 | 11 | -5.16 |  | Classes > Level 4: Ability Score Improvement |
| 17 | 9 | -5.16 |  | Classes > Level 4: Ability Score Improvement |
| 18 | 12 | -5.21 |  | Classes > Level 4: Ability Score Improvement |
| 19 | 7 | -5.31 |  | Classes > Level 4: Ability Score Improvement |
| 20 | 18 | -9.53 |  | Character Creation > Gaining a Level |

*retrieved sections:* Character Creation > Assign Ability Scores | Character Creation > Generate Your Scores | Character Creation > Choose Languages | Gameplay Toolbox > Step 3: Spend Your Budget | Magic Items > Hat of Many Spells | Magic Items > Deck of Illusions | Magic Items > Amulet of the Planes | Playing the Game > Ability Scores

<details><summary>full retrieved context</summary>

```
[Character Creation > Assign Ability Scores]
If you're using the Standard Array option, consult the Standard Array by Class table for suggestions on where to assign scores for your character's class. The table puts the highest scores in a class's main abilities. If you used a different method to generate the scores, you may still use this table to guide where you place your highest and lowest scores.  
**Standard Array by Class**  
<table>
<thead>
<tr>
<th>Class</th>
<th>Str.</th>
<th>Dex.</th>
<th>Con.</th>
<th>Int.</th>
<th>Wis.</th>

---

[Character Creation > Generate Your Scores]
#### Generate Your Scores  
Determine your ability scores by using one of the following three methods. Your GM might prefer you to use a particular one.  
_Standard Array._ Use the following six scores for your abilities: 15, 14, 13, 12, 10, 8.  
_Random Generation._ Roll four d6s and record the total of the highest three dice. Do this five more times, so you have six numbers.

---

[Character Creation > Choose Languages]
The Standard Languages table lists languages that are widespread in the setting. Every player character knows Common. The other standard languages originated with the first members of the most prominent species in the setting and have since spread widely.  
**Standard Languages**  
<table>
<thead>
<tr>
<th>1d12</th>
<th>Language</th>
</tr>
</thead>
<tbody>
<tr>
<td>—</td>
<td>Common</td>
</tr>
<tr>
<td>1</td>
<td>Common Sign Language</td>
</tr>
<tr>
<td>2</td>
<td>Draconic</td>
</tr>
<tr>

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>

---

[Gameplay Toolbox > Step 3: Spend Your Budget]
**Example 2.** A moderate-difficulty encounter for five level 3 characters has an XP budget of 225 × 5, for a total of 1,125 XP. With that, you could build either of these encounters:  
- **2 Druids** (450 XP each) and **9 Stirges** (25 XP each), for 1,125 XP total
- **1 Wight** (700 XP), **1 Warhorse Skeleton** (100 XP), and **6 Skeletons** (50 XP each), for 1,100 XP total

---

[Gameplay Toolbox > Step 3: Spend Your Budget]
**Example 3.** A high-difficulty encounter for six level 15 characters has an XP budget of 7,800 × 6, for a total of 46,800 XP. With that, you could build this encounter:  
• **2 Adult Red Dragons** (18,000 XP each) and **2 Fire Giants** (5,000 XP each), for 46,000 XP total

---

[Magic Items > Hat of Many Spells]
</tr>
</thead>
<tbody>
<tr>
<td>01–50</td>
<td>You cast a random spell determined by rolling 1d10: on a **1**, *Enlarge/Reduce* (enlarge effect); on a **2**, *Enlarge/Reduce* (reduce effect); on a **3**, *Faerie Fire*; on a **4**, *Fireball*; on a **5**, *Gust of Wind*; on a **6**, *Invisibility* (cast on yourself); on a **7**, *Lightning Bolt*; on an **8**, *Phantasmal Force*; on a **9**, *Polymorph*; on a **10**, *Stinking Cloud*.</td>
</tr>
<tr>
<td>51–55</td>

---

[Magic Items > Deck of Illusions]
The magic of the deck functions only if its cards are drawn at random. You can take a Magic action to draw a card at random from the deck and throw it to the ground at a point within 30 feet of yourself. An illusion of a creature, determined by rolling on the Deck of Illusions table, forms over the thrown card and remains until dispelled. The illusory creature created by the card looks and behaves like a real creature of its kind, except that it can do no harm. While you are within 120 feet of

---

[Magic Items > Amulet of the Planes]
</tr>
<tr>
<td>71–80</td>
<td>Random location on an Outer Plane determined by rolling 1d8: on a 1, Arborea; on a 2, Arcadia; on a 3, the Beastlands; on a 4, Bytopia; on a 5, Elysium; on a 6, Mechanus; on a 7, Mount Celestia; on an 8, Ysgard</td>
</tr>
<tr>
<td>81–90</td>
<td>Random location on an Outer Plane determined by rolling 1d8: on a 1, the Abyss; on a 2, Acheron; on a 3, Carceri; on a 4, Gehenna; on a 5, Hades; on a 6, Limbo; on a 7, the Nine Hells; on an 8, Pandemonium</td>
</tr>
<tr>

---

[Playing the Game > Ability Scores]
### Ability Scores  
Each ability has a score from 1 to 20, although some monsters have a score as high as 30. The score represents the magnitude of an ability. The Ability Scores table summarizes what the scores mean.  
**Ability Scores**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>This is the lowest a score can normally go. If an effect reduces a score to 0, that effect explains what happens.</td>
</tr>
<tr>
<td>2–9</td>

---

[Playing the Game > Ability Scores]
</tr>
<tr>
<td>2–9</td>
<td>This represents a weak capability.</td>
</tr>
<tr>
<td>10–11</td>
<td>This represents the human average.</td>
</tr>
<tr>
<td>12–19</td>
<td>This represents a strong capability.</td>
</tr>
<tr>
<td>20</td>
<td>This is the highest an adventurer's score can go unless a feature says otherwise.</td>
</tr>
<tr>
<td>21–29</td>
<td>This represents an extraordinary capability.</td>
</tr>
<tr>
<td>30</td>
<td>This is the highest a score can go.</td>
</tr>
</tbody>
</table>
```
</details>


---

## q14 (needle) List the four types of poison and say which can be applied to a weapon as a Bonus Action.

**Gold facts (counterfactual data):** Contact; Ingested; Inhaled; Injury; Bonus Action


### v0_closed_book  (0 chunks, 1 LLM call(s))

The four types of poison in D&D 5e are:

1. Acidic
2. Bleeding
3. Blinding
4. Poison

Of these, only the "Poison" type of poison can be applied to a weapon as a Bonus Action.

*facts found (judge): 1/5; missing: Contact; Ingested; Inhaled; Injury*


### v1_baseline  (3 chunks, 1 LLM call(s))

The four types of poison are Contact, Injury, Poison, and Basic (as listed in the context). The Injury type can be applied to a weapon as a Bonus Action.

*facts found (judge): 3/5; missing: Ingested; Inhaled*

*retrieved sections:* Equipment > Poison, Basic (100 GP) | Gameplay Toolbox > Poison

<details><summary>full retrieved context</summary>

```
[Equipment > Poison, Basic (100 GP)]
#### Poison, Basic (100 GP)  
As a Bonus Action, you can use a vial of Basic Poison to coat one weapon or up to three pieces of ammunition. A creature that takes Piercing or Slashing damage from the poisoned weapon or ammunition takes an extra 1d4 Poison damage. Once applied, the poison retains potency for 1 minute or until its damage is dealt, whichever comes first.

---

[Gameplay Toolbox > Poison]
**Injury.** Injury poison can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object. The poison remains potent until delivered through a wound or washed off. A creature that takes Piercing or Slashing damage from an object coated with the poison is exposed to its effects.

---

[Gameplay Toolbox > Poison]
## Poison  
Given their insidious and deadly nature, poisons are a favorite tool among assassins and evil creatures.  
Poisons come in the following four types:  
**Contact.** Contact poison can be smeared on an object and remains potent until it is touched or washed off. A creature that touches contact poison with exposed skin suffers its effects.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The context provided does not list four types of poison. It only describes two types of poison: Basic Poison and Dagger of Venom's poison. Additionally, only Basic Poison can be applied to a weapon as a Bonus Action.

*facts found (judge): 1/5; missing: Contact; Ingested; Inhaled; Injury*


*re-ranking* (query: `List the four types of poison and say which can be applied to a weapon as a Bonu`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.47 | yes | Gameplay Toolbox > Poison |
| 2 | 1 | 5.26 | yes | Equipment > Poison, Basic (100 GP) |
| 3 | 5 | 1.70 | yes | Magic Items > Dagger of Venom |
| 4 | 3 | 1.20 |  | Gameplay Toolbox > Poison |
| 5 | 8 | -2.52 |  | Monsters A–Z > Actions |
| 6 | 4 | -5.56 |  | Gameplay Toolbox > Sample Poisons |
| 7 | 10 | -6.89 |  | Animals > Actions |
| 8 | 6 | -7.10 |  | Monsters A–Z > Actions |
| 9 | 9 | -7.40 |  | Gameplay Toolbox > Poison |
| 10 | 7 | -7.94 |  | Animals > Actions |

*retrieved sections:* Gameplay Toolbox > Poison | Equipment > Poison, Basic (100 GP) | Magic Items > Dagger of Venom

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Poison]
**Injury.** Injury poison can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object. The poison remains potent until delivered through a wound or washed off. A creature that takes Piercing or Slashing damage from an object coated with the poison is exposed to its effects.

---

[Equipment > Poison, Basic (100 GP)]
#### Poison, Basic (100 GP)  
As a Bonus Action, you can use a vial of Basic Poison to coat one weapon or up to three pieces of ammunition. A creature that takes Piercing or Slashing damage from the poisoned weapon or ammunition takes an extra 1d4 Poison damage. Once applied, the poison retains potency for 1 minute or until its damage is dealt, whichever comes first.

---

[Magic Items > Dagger of Venom]
#### Dagger of Venom  
_Weapon (Dagger), Rare_  
You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon.  
You can take a Bonus Action to magically coat the blade with poison. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take 2d10 Poison damage and have the Poisoned condition for 1 minute. The weapon can't be used this way again until the next dawn.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The four types of poison are Contact, Ingested, Inhaled, and Injury. Only Injury poison can be applied to a weapon as a Bonus Action.

*facts found (judge): 5/5; missing: none*


*re-ranking* (query: `List the four types of poison and say which can be applied to a weapon as a Bonu`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.47 | yes | Gameplay Toolbox > Poison |
| 2 | 1 | 5.26 | yes | Equipment > Poison, Basic (100 GP) |
| 3 | 5 | 1.70 | yes | Magic Items > Dagger of Venom |
| 4 | 3 | 1.20 | yes | Gameplay Toolbox > Poison |
| 5 | 8 | -2.52 | yes | Monsters A–Z > Actions |
| 6 | 4 | -5.56 | yes | Gameplay Toolbox > Sample Poisons |
| 7 | 10 | -6.89 | yes | Animals > Actions |
| 8 | 6 | -7.10 | yes | Monsters A–Z > Actions |
| 9 | 9 | -7.40 |  | Gameplay Toolbox > Poison |
| 10 | 7 | -7.94 |  | Animals > Actions |

*retrieved sections:* Gameplay Toolbox > Poison | Equipment > Poison, Basic (100 GP) | Magic Items > Dagger of Venom | Monsters A–Z > Actions | Gameplay Toolbox > Sample Poisons | Animals > Actions

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Poison]
**Injury.** Injury poison can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object. The poison remains potent until delivered through a wound or washed off. A creature that takes Piercing or Slashing damage from an object coated with the poison is exposed to its effects.

---

[Equipment > Poison, Basic (100 GP)]
#### Poison, Basic (100 GP)  
As a Bonus Action, you can use a vial of Basic Poison to coat one weapon or up to three pieces of ammunition. A creature that takes Piercing or Slashing damage from the poisoned weapon or ammunition takes an extra 1d4 Poison damage. Once applied, the poison retains potency for 1 minute or until its damage is dealt, whichever comes first.

---

[Magic Items > Dagger of Venom]
#### Dagger of Venom  
_Weapon (Dagger), Rare_  
You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon.  
You can take a Bonus Action to magically coat the blade with poison. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take 2d10 Poison damage and have the Poisoned condition for 1 minute. The weapon can't be used this way again until the next dawn.

---

[Gameplay Toolbox > Poison]
## Poison  
Given their insidious and deadly nature, poisons are a favorite tool among assassins and evil creatures.  
Poisons come in the following four types:  
**Contact.** Contact poison can be smeared on an object and remains potent until it is touched or washed off. A creature that touches contact poison with exposed skin suffers its effects.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Rend._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 4 (1d6 + 1) Slashing damage.  
**_Fetid Cloud (1/Day)._** _Constitution Saving Throw:_ DC 11, each creature in a 10-foot Emanation originating from the dretch. _Failure:_ The target has the Poisoned condition until the end of its next turn. While Poisoned, the creature can take either an action or a Bonus Action on its turn, not both, and it can't take Reactions.

---

[Gameplay Toolbox > Sample Poisons]
### Sample Poisons  
Example poisons are detailed here in alphabetical order. Each poison's description includes the suggested price for a single dose of the poison, its type (contact, ingested, inhaled, or injury), and a description of the poison's debilitating effects.

---

[Animals > Actions]
### Actions  
<hr>  
**_Sting._** _Melee Attack Roll:_ +2, reach 5 ft. _Hit:_ 1 Piercing damage plus 3 (1d6) Poison damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The assassin makes three attacks, using Shortsword or Light Crossbow in any combination.  
**_Shortsword._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 7 (1d6 + 4) Piercing damage plus 17 (5d6) Poison damage, and the target has the Poisoned condition until the start of the assassin's next turn.  
**_Light Crossbow._** _Ranged Attack Roll:_ +7, range 80/320 ft. _Hit:_ 8 (1d8 + 4) Piercing damage plus 21 (6d6) Poison damage.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The context provided does not list four types of poison. It only describes two types of poison: Basic Poison and Dagger of Venom's poison. Additionally, only Basic Poison can be applied to a weapon as a Bonus Action.

*facts found (judge): 1/5; missing: Contact; Ingested; Inhaled; Injury*


*re-ranking* (query: `List the four types of poison and say which can be applied to a weapon as a Bonu`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.47 | yes | Gameplay Toolbox > Poison |
| 2 | 1 | 5.26 | yes | Equipment > Poison, Basic (100 GP) |
| 3 | 5 | 1.70 | yes | Magic Items > Dagger of Venom |
| 4 | 3 | 1.20 |  | Gameplay Toolbox > Poison |
| 5 | 7 | -2.52 |  | Monsters A–Z > Actions |
| 6 | 4 | -5.56 |  | Gameplay Toolbox > Sample Poisons |
| 7 | 6 | -7.10 |  | Monsters A–Z > Actions |
| 8 | 8 | -7.40 |  | Gameplay Toolbox > Poison |
| 9 | 10 | -7.57 |  | Monsters A–Z > Actions |
| 10 | 9 | -8.27 |  | Monsters A–Z > Actions |

*retrieved sections:* Gameplay Toolbox > Poison | Equipment > Poison, Basic (100 GP) | Magic Items > Dagger of Venom

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Poison]
**Injury.** Injury poison can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object. The poison remains potent until delivered through a wound or washed off. A creature that takes Piercing or Slashing damage from an object coated with the poison is exposed to its effects.

---

[Equipment > Poison, Basic (100 GP)]
#### Poison, Basic (100 GP)  
As a Bonus Action, you can use a vial of Basic Poison to coat one weapon or up to three pieces of ammunition. A creature that takes Piercing or Slashing damage from the poisoned weapon or ammunition takes an extra 1d4 Poison damage. Once applied, the poison retains potency for 1 minute or until its damage is dealt, whichever comes first.

---

[Magic Items > Dagger of Venom]
#### Dagger of Venom  
_Weapon (Dagger), Rare_  
You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon.  
You can take a Bonus Action to magically coat the blade with poison. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take 2d10 Poison damage and have the Poisoned condition for 1 minute. The weapon can't be used this way again until the next dawn.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The four types of poison are Contact, Injury, Light, and none of them can be directly applied to a weapon as a Bonus Action based on the given context. The Injury type can be applied to a weapon or ammunition as a Bonus Action, but it is not explicitly listed as one of the four types of poison.

*facts found (judge): 3/5; missing: Ingested; Inhaled*


*re-ranking* (query: `List the four types of poison and say which can be applied to a weapon as a Bonu`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.47 | yes | Gameplay Toolbox > Poison |
| 2 | 1 | 5.26 | yes | Equipment > Poison, Basic (100 GP) |
| 3 | 4 | 1.70 | yes | Magic Items > Dagger of Venom |
| 4 | 3 | 1.20 | yes | Gameplay Toolbox > Poison |
| 5 | 23 | 0.44 | yes | Equipment > Properties |
| 6 | 14 | -0.18 | yes | Classes > Pact of the Blade |
| 7 | 16 | -0.85 | yes | Equipment > Mastery Properties |
| 8 | 12 | -1.59 | yes | Magic Items > Dancing Sword |
| 9 | 10 | -1.66 |  | Magic Items > Quarterstaff of the Acrobat |
| 10 | 27 | -1.70 |  | Magic Items > Scimitar of Speed |
| 11 | 9 | -2.52 |  | Monsters A–Z > Actions |
| 12 | 28 | -3.51 |  | Classes > Level 5: Cunning Strike |
| 13 | 25 | -3.56 |  | Magic Items > Potions |
| 14 | 22 | -4.77 |  | Playing the Game > Order of Application |
| 15 | 5 | -5.56 |  | Gameplay Toolbox > Sample Poisons |
| 16 | 19 | -5.98 |  | Monsters A–Z > Actions |
| 17 | 18 | -6.03 |  | Classes > Transmuted Spell |
| 18 | 21 | -6.49 |  | Monsters A–Z > Actions |
| 19 | 7 | -7.10 |  | Monsters A–Z > Actions |
| 20 | 11 | -7.40 |  | Gameplay Toolbox > Poison |

*retrieved sections:* Gameplay Toolbox > Poison | Equipment > Poison, Basic (100 GP) | Magic Items > Dagger of Venom | Equipment > Properties | Classes > Pact of the Blade | Equipment > Mastery Properties | Magic Items > Dancing Sword

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Poison]
**Injury.** Injury poison can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object. The poison remains potent until delivered through a wound or washed off. A creature that takes Piercing or Slashing damage from an object coated with the poison is exposed to its effects.

---

[Equipment > Poison, Basic (100 GP)]
#### Poison, Basic (100 GP)  
As a Bonus Action, you can use a vial of Basic Poison to coat one weapon or up to three pieces of ammunition. A creature that takes Piercing or Slashing damage from the poisoned weapon or ammunition takes an extra 1d4 Poison damage. Once applied, the poison retains potency for 1 minute or until its damage is dealt, whichever comes first.

---

[Magic Items > Dagger of Venom]
#### Dagger of Venom  
_Weapon (Dagger), Rare_  
You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon.  
You can take a Bonus Action to magically coat the blade with poison. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take 2d10 Poison damage and have the Poisoned condition for 1 minute. The weapon can't be used this way again until the next dawn.

---

[Gameplay Toolbox > Poison]
## Poison  
Given their insidious and deadly nature, poisons are a favorite tool among assassins and evil creatures.  
Poisons come in the following four types:  
**Contact.** Contact poison can be smeared on an object and remains potent until it is touched or washed off. A creature that touches contact poison with exposed skin suffers its effects.

---

[Equipment > Properties]
**Light.** When you take the Attack action on your turn and attack with a Light weapon, you can make one extra attack as a Bonus Action later on the same turn. That extra attack must be made with a different Light weapon, and you don't add your ability modifier to the extra attack's damage unless that modifier is negative. For example, you can attack with a Shortsword in one hand and a Dagger in the other using the Attack action and a Bonus Action, but you don't add your Strength or Dexterity

---

[Classes > Pact of the Blade]
#### Pact of the Blade  
As a Bonus Action, you can conjure a pact weapon in your hand—a Simple or Martial Melee weapon of your choice with which you bond—or create a bond with a magic weapon you touch; you can't bond with a magic weapon if someone else is attuned to it or another Warlock is bonded with it. Until the bond ends, you have proficiency with the weapon, and you can use it as a Spellcasting Focus.

---

[Equipment > Mastery Properties]
**Graze.** If your attack roll with this weapon misses a creature, you can deal damage to that creature equal to the ability modifier you used to make the attack roll. This damage is the same type dealt by the weapon, and the damage can be increased only by increasing the ability modifier.  
**Nick.** When you make the extra attack of the Light property, you can make it as part of the Attack action instead of as a Bonus Action. You can make this extra attack only once per turn.

---

[Magic Items > Dancing Sword]
While the weapon hovers, you can take a Bonus Action to cause it to fly up to 30 feet to another spot within 30 feet of you. As part of the same Bonus Action, you can cause the weapon to attack one creature within 5 feet of the weapon.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The four types of poison are Contact, Ingested, Inhaled, and Injury. Contact and Injury poisons can be applied to a weapon as a Bonus Action.

*facts found (judge): 5/5; missing: none*


*re-ranking* (query: `List the four types of poison and say which can be applied to a weapon as a Bonu`): candidate pool of 16, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.47 | yes | Gameplay Toolbox > Poison |
| 2 | 1 | 5.26 | yes | Equipment > Poison, Basic (100 GP) |
| 3 | 4 | 1.70 | yes | Magic Items > Dagger of Venom |
| 4 | 3 | 1.20 | yes | Gameplay Toolbox > Poison |
| 5 | 10 | -1.66 | yes | Magic Items > Quarterstaff of the Acrobat |
| 6 | 9 | -2.52 | yes | Monsters A–Z > Actions |
| 7 | 15 | -2.64 | yes | Spells > Magic Weapon |
| 8 | 5 | -5.56 | yes | Gameplay Toolbox > Sample Poisons |
| 9 | 7 | -7.10 |  | Monsters A–Z > Actions |
| 10 | 14 | -10.03 |  | Playing the Game > Damage Rolls |
| 11 | 12 | -10.15 |  | Spells > Attack Rolls |
| 12 | 6 | -10.38 |  | Spells > Symbol |
| 13 | 13 | -10.43 |  | Playing the Game > Damage Rolls |
| 14 | 8 | -10.49 |  | Spells > Glyph of Warding |
| 15 | 11 | -11.18 |  | Playing the Game > Attack Rolls |
| 16 | 16 | -11.37 |  | Magic Items > "The Next Dawn" |

*retrieved sections:* Gameplay Toolbox > Poison | Equipment > Poison, Basic (100 GP) | Magic Items > Dagger of Venom | Magic Items > Quarterstaff of the Acrobat | Monsters A–Z > Actions | Spells > Magic Weapon | Gameplay Toolbox > Sample Poisons

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Poison]
**Injury.** Injury poison can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object. The poison remains potent until delivered through a wound or washed off. A creature that takes Piercing or Slashing damage from an object coated with the poison is exposed to its effects.

---

[Equipment > Poison, Basic (100 GP)]
#### Poison, Basic (100 GP)  
As a Bonus Action, you can use a vial of Basic Poison to coat one weapon or up to three pieces of ammunition. A creature that takes Piercing or Slashing damage from the poisoned weapon or ammunition takes an extra 1d4 Poison damage. Once applied, the poison retains potency for 1 minute or until its damage is dealt, whichever comes first.

---

[Magic Items > Dagger of Venom]
#### Dagger of Venom  
_Weapon (Dagger), Rare_  
You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon.  
You can take a Bonus Action to magically coat the blade with poison. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take 2d10 Poison damage and have the Poisoned condition for 1 minute. The weapon can't be used this way again until the next dawn.

---

[Gameplay Toolbox > Poison]
## Poison  
Given their insidious and deadly nature, poisons are a favorite tool among assassins and evil creatures.  
Poisons come in the following four types:  
**Contact.** Contact poison can be smeared on an object and remains potent until it is touched or washed off. A creature that touches contact poison with exposed skin suffers its effects.

---

[Magic Items > Quarterstaff of the Acrobat]
#### Quarterstaff of the Acrobat  
_Weapon (Quarterstaff), Very Rare (Requires Attunement)_  
You have a +2 bonus to attack rolls and damage rolls made with this magic weapon.  
While holding this weapon, you can cause it to emit green Dim Light out to 10 feet, either as a Bonus Action or after you roll Initiative, or you can extinguish the light as a Bonus Action.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Rend._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 4 (1d6 + 1) Slashing damage.  
**_Fetid Cloud (1/Day)._** _Constitution Saving Throw:_ DC 11, each creature in a 10-foot Emanation originating from the dretch. _Failure:_ The target has the Poisoned condition until the end of its next turn. While Poisoned, the creature can take either an action or a Bonus Action on its turn, not both, and it can't take Reactions.

---

[Spells > Magic Weapon]
#### Magic Weapon  
_Level 2 Transmutation (Paladin, Ranger, Sorcerer, Wizard)_  
**Casting Time:** Bonus Action
**Range:** Touch
**Components:** V, S
**Duration:** 1 hour  
You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a +1 bonus to attack rolls and damage rolls. The spell ends early if you cast it again.  
_Using a Higher-Level Spell Slot._ The bonus increases to +2 with a level 3–5 spell slot. The bonus increases to +3 with a level 6+ spell slot.

---

[Gameplay Toolbox > Sample Poisons]
### Sample Poisons  
Example poisons are detailed here in alphabetical order. Each poison's description includes the suggested price for a single dose of the poison, its type (contact, ingested, inhaled, or injury), and a description of the poison's debilitating effects.
```
</details>


### v6_agentic  (11 chunks, 3 LLM call(s))

The four types of poison are Contact, Injury, Ingested, and Basic (as listed in the context).

Basic Poison can be applied to a weapon as a Bonus Action.

*facts found (judge): 4/5; missing: Inhaled*

*agentic sub-queries:* poison / bonus action / weapon


*re-ranking* (query: `poison`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 6.42 | yes | Gameplay Toolbox > Poison |
| 2 | 3 | 5.97 | yes | Gameplay Toolbox > Poison |
| 3 | 12 | 3.20 | yes | Gameplay Toolbox > Poison |
| 4 | 9 | 3.04 |  | Gameplay Toolbox > Sample Poisons |
| 5 | 15 | 2.83 |  | Gameplay Toolbox > Harvesting Poison |
| 6 | 4 | 2.78 |  | Gameplay Toolbox > Purchasing Poison |
| 7 | 6 | 2.24 |  | Magic Items > Potion of Poison |
| 8 | 5 | 2.09 |  | Gameplay Toolbox > Harvesting Poison |
| 9 | 10 | 1.54 |  | Gameplay Toolbox > Wyvern Poison (1,200 GP) |
| 10 | 13 | 1.45 |  | Spells > Protection from Poison |
| 11 | 8 | 1.10 |  | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 12 | 18 | 0.87 |  | Magic Items > Periapt of Proof against Poison |
| 13 | 19 | 0.68 |  | Magic Items > Dagger of Venom |
| 14 | 17 | 0.57 |  | Spells > Detect Poison and Disease |
| 15 | 1 | 0.26 |  | Gameplay Toolbox > Harvesting Poison |
| 16 | 11 | 0.25 |  | Spells > Poison Spray |
| 17 | 20 | 0.11 |  | Gameplay Toolbox > Torpor (600 GP) |
| 18 | 7 | -0.05 |  | Gameplay Toolbox > Pale Tincture (250 GP) |
| 19 | 14 | -0.61 |  | Gameplay Toolbox > Midnight Tears (1,500 GP) |
| 20 | 16 | -0.72 |  | Gameplay Toolbox > Burnt Othur Fumes (500 GP) |


*re-ranking* (query: `bonus action`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 10.24 | yes | Rules Glossary > Bonus Action |
| 2 | 1 | 9.05 | yes | Playing the Game > Bonus Actions |
| 3 | 4 | 8.24 | yes | Playing the Game > Bonus Actions |
| 4 | 3 | 7.36 |  | Monsters > Bonus Action |
| 5 | 5 | 6.70 |  | Monsters A–Z > Bonus Actions |
| 6 | 18 | 6.64 |  | Monsters A–Z > Bonus Actions |
| 7 | 6 | 6.61 |  | Monsters A–Z > Bonus Actions |
| 8 | 16 | 6.52 |  | Animals > Bonus Actions |
| 9 | 10 | 6.51 |  | Monsters A–Z > Bonus Actions |
| 10 | 9 | 6.46 |  | Monsters A–Z > Bonus Actions |
| 11 | 17 | 6.42 |  | Animals > Bonus Actions |
| 12 | 8 | 6.32 |  | Monsters A–Z > Bonus Actions |
| 13 | 7 | 6.24 |  | Monsters A–Z > Bonus Actions |
| 14 | 19 | 6.13 |  | Classes > Level 2: Monk's Focus |
| 15 | 14 | 6.08 |  | Monsters A–Z > Bonus Actions |
| 16 | 13 | 5.87 |  | Magic Items > Elemental Gem |
| 17 | 11 | 5.54 |  | Equipment > Properties |
| 18 | 15 | 5.48 |  | Monsters > Stat Block Overview |
| 19 | 20 | 5.28 |  | Spells > Expeditious Retreat |
| 20 | 12 | 3.65 |  | Feats > Boon of the Night Spirit |


*re-ranking* (query: `weapon`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.54 | yes | Rules Glossary > Weapon |
| 2 | 11 | 5.22 | yes | Equipment > Weapons |
| 3 | 13 | 4.00 | yes | Equipment > Weapons |
| 4 | 14 | 3.51 |  | Magic Items > Weapon, +1, +2, or +3 |
| 5 | 2 | 3.45 |  | Rules Glossary > Weapon Attack |
| 6 | 3 | 3.41 |  | Magic Items > Vicious Weapon |
| 7 | 9 | 2.58 |  | Magic Items > Weapon of Warning |
| 8 | 15 | 2.57 |  | Magic Items > Luck Blade |
| 9 | 7 | 2.23 |  | Magic Items > Sword of Sharpness |
| 10 | 17 | 2.23 |  | Equipment > Properties |
| 11 | 18 | 2.04 |  | Magic Items > Dancing Sword |
| 12 | 16 | 1.88 |  | Magic Items > Thunderous Greatclub |
| 13 | 6 | 1.85 |  | Magic Items > Defender |
| 14 | 8 | 1.76 |  | Magic Items > Vorpal Sword |
| 15 | 10 | 1.66 |  | Equipment > Properties |
| 16 | 19 | 1.30 |  | Magic Items > Berserker Axe |
| 17 | 5 | 1.08 |  | Magic Items > Dragon Slayer |
| 18 | 12 | 1.03 |  | Magic Items > Hammer of Thunderbolts |
| 19 | 4 | 0.23 |  | Magic Items > Flame Tongue |
| 20 | 20 | -0.07 |  | Magic Items > Hammer of Thunderbolts |


*re-ranking* (query: `poison properties`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.94 | yes | Gameplay Toolbox > Poison |
| 2 | 3 | 0.12 | yes | Gameplay Toolbox > Poison |
| 3 | 1 | -1.72 | yes | Equipment > Poison, Basic (100 GP) |
| 4 | 7 | -2.44 |  | Magic Items > Potion of Poison |
| 5 | 6 | -2.56 |  | Gameplay Toolbox > Sample Poisons |
| 6 | 11 | -3.26 |  | Magic Items > Periapt of Proof against Poison |
| 7 | 19 | -3.29 |  | Rules Glossary > Poisoned [Condition] |
| 8 | 5 | -3.99 |  | Gameplay Toolbox > Purchasing Poison |
| 9 | 14 | -4.10 |  | Gameplay Toolbox > Harvesting Poison |
| 10 | 12 | -4.62 |  | Gameplay Toolbox > Wyvern Poison (1,200 GP) |
| 11 | 10 | -5.15 |  | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 12 | 8 | -5.49 |  | Gameplay Toolbox > Pale Tincture (250 GP) |
| 13 | 17 | -5.60 |  | Magic Items > Rod of Alertness |
| 14 | 9 | -5.68 |  | Gameplay Toolbox > Harvesting Poison |
| 15 | 13 | -5.87 |  | Gameplay Toolbox > Midnight Tears (1,500 GP) |
| 16 | 15 | -6.28 |  | Gameplay Toolbox > Torpor (600 GP) |
| 17 | 4 | -7.11 |  | Gameplay Toolbox > Harvesting Poison |
| 18 | 18 | -9.67 | yes | Equipment > Weapons |
| 19 | 16 | -10.36 |  | Equipment > Properties |
| 20 | 20 | -10.71 |  | Magic Items > Sentient Magic Items |


*re-ranking* (query: `bonus action examples`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 9.32 | yes | Playing the Game > Bonus Actions |
| 2 | 2 | 6.66 | yes | Rules Glossary > Bonus Action |
| 3 | 12 | 6.63 | yes | Equipment > Properties |
| 4 | 6 | 5.83 |  | Monsters A–Z > Bonus Actions |
| 5 | 5 | 5.72 |  | Monsters A–Z > Bonus Actions |
| 6 | 9 | 5.14 |  | Monsters A–Z > Bonus Actions |
| 7 | 7 | 5.01 |  | Monsters A–Z > Bonus Actions |
| 8 | 8 | 4.89 |  | Monsters A–Z > Bonus Actions |
| 9 | 10 | 4.76 |  | Monsters A–Z > Bonus Actions |
| 10 | 3 | 4.67 |  | Monsters > Bonus Action |
| 11 | 4 | 4.56 | yes | Playing the Game > Bonus Actions |
| 12 | 16 | 4.34 |  | Monsters > Stat Block Overview |
| 13 | 20 | 4.13 |  | Monsters > Resistances and Vulnerabilities |
| 14 | 18 | 3.48 |  | Rules Glossary > Stat Block |
| 15 | 15 | 3.21 |  | Monsters A–Z > Bonus Actions |
| 16 | 13 | 1.70 |  | Feats > Boon of the Night Spirit |
| 17 | 11 | 1.56 |  | Equipment > Properties |
| 18 | 17 | -1.53 |  | Rules Glossary > Ready [Action] |
| 19 | 19 | -9.56 |  | Gameplay Toolbox > 2: Choose a Feat |
| 20 | 14 | -10.14 |  | Playing the Game > Ability Modifier |

*retrieved sections:* Gameplay Toolbox > Poison | Rules Glossary > Bonus Action | Playing the Game > Bonus Actions | Rules Glossary > Weapon | Equipment > Weapons | Equipment > Poison, Basic (100 GP) | Equipment > Properties

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Poison]
## Poison  
Given their insidious and deadly nature, poisons are a favorite tool among assassins and evil creatures.  
Poisons come in the following four types:  
**Contact.** Contact poison can be smeared on an object and remains potent until it is touched or washed off. A creature that touches contact poison with exposed skin suffers its effects.

---

[Gameplay Toolbox > Poison]
**Injury.** Injury poison can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object. The poison remains potent until delivered through a wound or washed off. A creature that takes Piercing or Slashing damage from an object coated with the poison is exposed to its effects.

---

[Gameplay Toolbox > Poison]
**Ingested.** A creature must swallow an entire dose of ingested poison to suffer its effects. The dose can be delivered in food or a liquid. You may decide that a partial dose has a reduced effect, such as allowing Advantage on the saving throw or dealing only half as much damage on a failed save.

---

[Rules Glossary > Bonus Action]
#### Bonus Action  
A Bonus Action is a special action that you can take on the same turn that you take an action. You can't take more than one Bonus Action on a turn, and you have a Bonus Action to take only if a rule explicitly says so. _See also_ "Playing the Game" ("Actions").

---

[Playing the Game > Bonus Actions]
### Bonus Actions  
Various class features, spells, and other abilities let you take an additional action on your turn called a Bonus Action. The Cunning Action feature, for example, allows a Rogue to take a Bonus Action. You can take a Bonus Action only when a special ability, a spell, or another feature of the game states that you can do something as a Bonus Action. You otherwise don't have a Bonus Action to take.

---

[Playing the Game > Bonus Actions]
You can take only one Bonus Action on your turn, so you must choose which Bonus Action to use if you have more than one available.  
You choose when to take a Bonus Action during your turn unless the Bonus Action's timing is specified. Anything that deprives you of your ability to take actions also prevents you from taking a Bonus Action.

---

[Rules Glossary > Weapon]
#### Weapon  
A weapon is an object that is in the Simple or Martial weapon category. _See also_ "Equipment" ("Weapons").

---

[Equipment > Weapons]
**Melee or Ranged.** A weapon is classified as either Melee or Ranged. A Melee weapon is used to attack a target within 5 feet, whereas a Ranged weapon is used to attack at a greater distance.  
**Damage.** The table lists the amount of damage a weapon deals when an attacker hits with it as well as the type of that damage.  
**Properties.** Any properties a weapon has are listed in the Properties column. Each property is defined in the "Properties" section.

---

[Equipment > Weapons]
## Weapons  
The Weapons table in this section shows the game's main weapons. The table lists the cost and weight of each weapon, as well as the following details:  
**Category.** Every weapon falls into a category: Simple or Martial. Weapon proficiencies are usually tied to one of these categories. For example, you might have proficiency with Simple weapons.

---

[Equipment > Poison, Basic (100 GP)]
#### Poison, Basic (100 GP)  
As a Bonus Action, you can use a vial of Basic Poison to coat one weapon or up to three pieces of ammunition. A creature that takes Piercing or Slashing damage from the poisoned weapon or ammunition takes an extra 1d4 Poison damage. Once applied, the poison retains potency for 1 minute or until its damage is dealt, whichever comes first.

---

[Equipment > Properties]
**Light.** When you take the Attack action on your turn and attack with a Light weapon, you can make one extra attack as a Bonus Action later on the same turn. That extra attack must be made with a different Light weapon, and you don't add your ability modifier to the extra attack's damage unless that modifier is negative. For example, you can attack with a Shortsword in one hand and a Dagger in the other using the Attack action and a Bonus Action, but you don't add your Strength or Dexterity
```
</details>


---

## q15 (multi-part) Describe death saving throws: what roll counts as a success, what happens on a natural 1 and a natural 20, and what DC and check is needed to stabilize a creature with the Help action?

**Gold facts (counterfactual data):** 12 or higher; third failure; two failures; regain 1 Hit Point; DC 10 Wisdom (Medicine)


### v0_closed_book  (0 chunks, 1 LLM call(s))

Death saving throws in Dungeons & Dragons 5e are used when a character is at 0 hit points but not yet dead. Here’s a concise breakdown:

- **Success**: A roll of 10 or higher on a d20.
- **Failure**: A roll of 9 or lower on a d20.
- **Natural 1**: Automatically fails the save.
- **Natural 20**: Automatically succeeds the save.

To **stabilize** a creature using the Help action, the stabilizing character must succeed on a DC 10 Wisdom (Medicine) check. This does not require a death saving throw; it simply helps the creature avoid dying outright.

*facts found (judge): 1/5; missing: 12 or higher; third failure; two failures; regain 1 Hit Point*


### v1_baseline  (3 chunks, 1 LLM call(s))

Death saving throws involve rolling a 1d20. A roll of 12 or higher is a success, while a roll of 11 or lower is a failure. On your third success, you become stable. On your third failure, you die. Successes and failures do not need to be consecutive; keep track of both until you reach three of a kind.

A roll of 1 on the d20 results in two failures. A roll of 20 on the d20 grants 1 Hit Point.

To stabilize a creature with 0 Hit Points using the Help action, a DC 10 Wisdom (Medicine) check is required. If successful, the creature stops making death saving throws but remains unconscious. If the creature takes any damage while stabilized, it stops being stabilized and starts making death saving throws again. A stabilized creature that is not healed regains 1 Hit Point after 1d4 hours.

*facts found (judge): 5/5; missing: none*

*retrieved sections:* Playing the Game > Death Saving Throws | Playing the Game > Stabilizing a Character

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
_Three Successes/Failures._ Roll 1d20. If the roll is 12 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become Stable (see "Stabilizing a Character" below). On your third failure, you die.  
The successes and failures don't need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

---

[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

Death saving throws are made by rolling 1d20:

- **Success:** Rolling 12 or higher.
- **Failure:** Rolling 11 or lower.
- **Natural 1:** Counts as two failures.
- **Natural 20:** Regains 1 Hit Point.

No DC or check is provided in the context for stabilizing a creature with the Help action.

*facts found (judge): 3/5; missing: third failure; DC 10 Wisdom (Medicine)*


*re-ranking* (query: `Describe death saving throws: what roll counts as a success, what happens on a n`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.18 | yes | Playing the Game > Death Saving Throws |
| 2 | 3 | 3.17 | yes | Playing the Game > Death Saving Throws |
| 3 | 7 | 1.70 | yes | Monsters A–Z > Actions |
| 4 | 10 | 1.46 |  | Monsters A–Z > Actions |
| 5 | 2 | 1.30 |  | Playing the Game > Stabilizing a Character |
| 6 | 6 | 0.21 |  | Playing the Game > D20 Tests |
| 7 | 4 | -1.58 |  | Rules Glossary > Stat Block |
| 8 | 8 | -2.27 |  | Monsters A–Z > Actions |
| 9 | 9 | -2.35 |  | Monsters A–Z > Actions |
| 10 | 5 | -2.76 |  | Rules Glossary > Stable |

*retrieved sections:* Playing the Game > Death Saving Throws | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
_Three Successes/Failures._ Roll 1d20. If the roll is 12 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become Stable (see "Stabilizing a Character" below). On your third failure, you die.  
The successes and failures don't need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Monsters A–Z > Actions]
**_Paralyzing Breath._** _Constitution Saving Throw:_ DC 20, each creature in a 60-foot Cone. _First Failure:_ The target has the Incapacitated condition until the end of its next turn, when it repeats the save. _Second Failure:_ The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

Death saving throws involve rolling a 1d20. A roll of 12 or higher is a success, while a roll of 11 or lower is a failure. Rolling a 1 results in two failures, and rolling a 20 grants 1 Hit Point. To stabilize a creature with 0 Hit Points using the Help action, a DC 10 Wisdom (Medicine) check is required.

*facts found (judge): 3/5; missing: third failure; regain 1 Hit Point*


*re-ranking* (query: `Describe death saving throws: what roll counts as a success, what happens on a n`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.18 | yes | Playing the Game > Death Saving Throws |
| 2 | 3 | 3.17 | yes | Playing the Game > Death Saving Throws |
| 3 | 7 | 1.70 | yes | Monsters A–Z > Actions |
| 4 | 10 | 1.46 | yes | Monsters A–Z > Actions |
| 5 | 2 | 1.30 | yes | Playing the Game > Stabilizing a Character |
| 6 | 6 | 0.21 | yes | Playing the Game > D20 Tests |
| 7 | 4 | -1.58 | yes | Rules Glossary > Stat Block |
| 8 | 8 | -2.27 | yes | Monsters A–Z > Actions |
| 9 | 9 | -2.35 |  | Monsters A–Z > Actions |
| 10 | 5 | -2.76 |  | Rules Glossary > Stable |

*retrieved sections:* Playing the Game > Death Saving Throws | Monsters A–Z > Actions | Playing the Game > Stabilizing a Character | Playing the Game > D20 Tests | Rules Glossary > Stat Block

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
_Three Successes/Failures._ Roll 1d20. If the roll is 12 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become Stable (see "Stabilizing a Character" below). On your third failure, you die.  
The successes and failures don't need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Monsters A–Z > Actions]
**_Paralyzing Breath._** _Constitution Saving Throw:_ DC 20, each creature in a 60-foot Cone. _First Failure:_ The target has the Incapacitated condition until the end of its next turn, when it repeats the save. _Second Failure:_ The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.

---

[Monsters A–Z > Actions]
**_Bite._** _Melee Attack Roll:_ +14, reach 10 ft. _Hit:_ 18 (3d6 + 8) Piercing damage. If the target is a creature, it must make the following saving throw. _Constitution Saving Throw:_ DC 21. _Failure:_ The target has the Poisoned condition. While Poisoned, the target can't regain Hit Points and takes 21 (6d6) Poison damage at the start of each of its turns, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds

---

[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Playing the Game > D20 Tests]
## D20 Tests  
When the outcome of an action is uncertain, the game uses a d20 roll to determine success or failure. These rolls are called D20 Tests, and they come in three kinds: ability checks, saving throws, and attack rolls. They follow these steps:

---

[Rules Glossary > Stat Block]
_Saving Throw Effect Notation._ If an effect forces a saving throw, the effect's entry starts by identifying the kind of saving throw required and then provides the save's DC, a description of which creatures must make the save, and what happens on a failed or a successful save.

---

[Monsters A–Z > Actions]
**_Sleep Breath._** _Constitution Saving Throw:_ DC 11, each creature in a 15-foot Cone. _Failure:_ The target has the Incapacitated condition until the end of its next turn, at which point it repeats the save. _Second Failure:_ The target has the Unconscious condition for 1 minute. This effect ends for the target if it takes damage or a creature within 5 feet of it takes an action to wake it.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

Death saving throws are made by rolling 1d20:

- **Success:** Rolling 12 or higher.
- **Failure:** Rolling 11 or lower.
- **Natural 1:** Counts as two failures.
- **Natural 20:** Regains 1 Hit Point.

No DC or check is provided in the context for stabilizing a creature with the Help action.

*facts found (judge): 3/5; missing: third failure; DC 10 Wisdom (Medicine)*


*re-ranking* (query: `Describe death saving throws: what roll counts as a success, what happens on a n`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.18 | yes | Playing the Game > Death Saving Throws |
| 2 | 3 | 3.17 | yes | Playing the Game > Death Saving Throws |
| 3 | 7 | 1.70 | yes | Monsters A–Z > Actions |
| 4 | 10 | 1.46 |  | Monsters A–Z > Actions |
| 5 | 2 | 1.30 |  | Playing the Game > Stabilizing a Character |
| 6 | 6 | 0.21 |  | Playing the Game > D20 Tests |
| 7 | 4 | -1.58 |  | Rules Glossary > Stat Block |
| 8 | 8 | -2.27 |  | Monsters A–Z > Actions |
| 9 | 9 | -2.35 |  | Monsters A–Z > Actions |
| 10 | 5 | -2.76 |  | Rules Glossary > Stable |

*retrieved sections:* Playing the Game > Death Saving Throws | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
_Three Successes/Failures._ Roll 1d20. If the roll is 12 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become Stable (see "Stabilizing a Character" below). On your third failure, you die.  
The successes and failures don't need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Monsters A–Z > Actions]
**_Paralyzing Breath._** _Constitution Saving Throw:_ DC 20, each creature in a 60-foot Cone. _First Failure:_ The target has the Incapacitated condition until the end of its next turn, when it repeats the save. _Second Failure:_ The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

Death saving throws involve rolling a 1d20. A roll of 12 or higher is a success, while a roll of 11 or lower is a failure. Rolling a 1 results in two failures, and rolling a 20 grants 1 Hit Point. To stabilize a creature with 0 Hit Points using the Help action, a DC 10 Wisdom (Medicine) check is required.

*facts found (judge): 4/5; missing: third failure*


*re-ranking* (query: `Describe death saving throws: what roll counts as a success, what happens on a n`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 3.18 | yes | Playing the Game > Death Saving Throws |
| 2 | 2 | 3.17 | yes | Playing the Game > Death Saving Throws |
| 3 | 13 | 1.70 | yes | Monsters A–Z > Actions |
| 4 | 23 | 1.46 | yes | Monsters A–Z > Actions |
| 5 | 1 | 1.30 | yes | Playing the Game > Stabilizing a Character |
| 6 | 18 | 1.28 | yes | Spells > Earthquake |
| 7 | 4 | 1.25 | yes | Classes > Level 18: Survivor |
| 8 | 9 | 0.76 | yes | Monsters A–Z > Traits |
| 9 | 8 | 0.21 |  | Playing the Game > D20 Tests |
| 10 | 27 | -0.57 |  | Playing the Game > Rolling 20 or 1 |
| 11 | 30 | -0.67 |  | Monsters A–Z > Actions |
| 12 | 25 | -0.96 |  | Magic Items > Energy Bow |
| 13 | 28 | -1.23 |  | Playing the Game > D20 Tests |
| 14 | 6 | -1.58 |  | Rules Glossary > Stat Block |
| 15 | 10 | -1.60 |  | Spells > Saving Throws |
| 16 | 5 | -1.87 |  | Playing the Game > Death Saving Throws |
| 17 | 14 | -2.15 |  | Gameplay Toolbox > Rolling Stone |
| 18 | 17 | -2.27 |  | Monsters A–Z > Actions |
| 19 | 22 | -2.35 |  | Monsters A–Z > Actions |
| 20 | 7 | -2.76 |  | Rules Glossary > Stable |

*retrieved sections:* Playing the Game > Death Saving Throws | Monsters A–Z > Actions | Playing the Game > Stabilizing a Character | Spells > Earthquake | Classes > Level 18: Survivor | Monsters A–Z > Traits

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
_Three Successes/Failures._ Roll 1d20. If the roll is 12 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become Stable (see "Stabilizing a Character" below). On your third failure, you die.  
The successes and failures don't need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Monsters A–Z > Actions]
**_Paralyzing Breath._** _Constitution Saving Throw:_ DC 20, each creature in a 60-foot Cone. _First Failure:_ The target has the Incapacitated condition until the end of its next turn, when it repeats the save. _Second Failure:_ The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.

---

[Monsters A–Z > Actions]
**_Bite._** _Melee Attack Roll:_ +14, reach 10 ft. _Hit:_ 18 (3d6 + 8) Piercing damage. If the target is a creature, it must make the following saving throw. _Constitution Saving Throw:_ DC 21. _Failure:_ The target has the Poisoned condition. While Poisoned, the target can't regain Hit Points and takes 21 (6d6) Poison damage at the start of each of its turns, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds

---

[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Spells > Earthquake]
A creature within a distance from a collapsing structure equal to half the structure's height makes a Dexterity saving throw. On a failed save, the creature takes 12d6 Bludgeoning damage, has the Prone condition, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape. On a successful save, the creature takes half as much damage only.

---

[Classes > Level 18: Survivor]
#### Level 18: Survivor  
You attain the pinnacle of resilience in battle, giving you these benefits.  
_Defy Death._ You have Advantage on Death Saving Throws. Moreover, when you roll 18–20 on a Death Saving Throw, you gain the benefit of rolling a 20 on it.  
_Heroic Rally._ At the start of each of your turns, you regain Hit Points equal to 5 plus your Constitution modifier if you are Bloodied and have at least 1 Hit Point.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Death Throes._** The balor explodes when it dies. _Dexterity Saving Throw:_ DC 20, each creature in a 30-foot Emanation originating from the balor. _Failure:_ 31 (9d6) Fire damage plus 31 (9d6) Force damage. _Success:_ Half damage. _Failure or Success:_ If the balor dies outside the Abyss, it gains a new body instantly, reviving with all its Hit Points somewhere in the Abyss.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

Death saving throws involve rolling a 1d20. A roll of 12 or higher is a success, while a roll of 11 or lower is a failure. Rolling a 1 results in two failures, and rolling a 20 grants 1 Hit Point. 

To stabilize a creature with 0 Hit Points using the Help action, a DC 10 Wisdom (Medicine) check is required. No specific DC is mentioned for stabilizing a character; the check is made against this DC.

*facts found (judge): 4/5; missing: third failure*


*re-ranking* (query: `Describe death saving throws: what roll counts as a success, what happens on a n`): candidate pool of 17, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 3.18 | yes | Playing the Game > Death Saving Throws |
| 2 | 2 | 3.17 | yes | Playing the Game > Death Saving Throws |
| 3 | 1 | 1.30 | yes | Playing the Game > Stabilizing a Character |
| 4 | 4 | 1.25 | yes | Classes > Level 18: Survivor |
| 5 | 9 | 0.76 | yes | Monsters A–Z > Traits |
| 6 | 8 | 0.21 | yes | Playing the Game > D20 Tests |
| 7 | 6 | -1.58 | yes | Rules Glossary > Stat Block |
| 8 | 10 | -1.60 | yes | Spells > Saving Throws |
| 9 | 5 | -1.87 |  | Playing the Game > Death Saving Throws |
| 10 | 7 | -2.76 |  | Rules Glossary > Stable |
| 11 | 13 | -3.42 |  | Rules Glossary > Death Saving Throw |
| 12 | 14 | -5.94 |  | Rules Glossary > Unconscious [Condition] |
| 13 | 16 | -7.58 |  | Rules Glossary > Critical Hit |
| 14 | 11 | -9.21 |  | Rules Glossary > Help [Action] |
| 15 | 17 | -10.39 |  | Rules Glossary > Bloodied |
| 16 | 15 | -10.41 |  | Rules Glossary > Unconscious [Condition] |
| 17 | 12 | -10.91 |  | Rules Glossary > Help [Action] |

*retrieved sections:* Playing the Game > Death Saving Throws | Playing the Game > Stabilizing a Character | Classes > Level 18: Survivor | Monsters A–Z > Traits | Playing the Game > D20 Tests | Rules Glossary > Stat Block | Spells > Saving Throws

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
_Three Successes/Failures._ Roll 1d20. If the roll is 12 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become Stable (see "Stabilizing a Character" below). On your third failure, you die.  
The successes and failures don't need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Classes > Level 18: Survivor]
#### Level 18: Survivor  
You attain the pinnacle of resilience in battle, giving you these benefits.  
_Defy Death._ You have Advantage on Death Saving Throws. Moreover, when you roll 18–20 on a Death Saving Throw, you gain the benefit of rolling a 20 on it.  
_Heroic Rally._ At the start of each of your turns, you regain Hit Points equal to 5 plus your Constitution modifier if you are Bloodied and have at least 1 Hit Point.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Death Throes._** The balor explodes when it dies. _Dexterity Saving Throw:_ DC 20, each creature in a 30-foot Emanation originating from the balor. _Failure:_ 31 (9d6) Fire damage plus 31 (9d6) Force damage. _Success:_ Half damage. _Failure or Success:_ If the balor dies outside the Abyss, it gains a new body instantly, reviving with all its Hit Points somewhere in the Abyss.

---

[Playing the Game > D20 Tests]
## D20 Tests  
When the outcome of an action is uncertain, the game uses a d20 roll to determine success or failure. These rolls are called D20 Tests, and they come in three kinds: ability checks, saving throws, and attack rolls. They follow these steps:

---

[Rules Glossary > Stat Block]
_Saving Throw Effect Notation._ If an effect forces a saving throw, the effect's entry starts by identifying the kind of saving throw required and then provides the save's DC, a description of which creatures must make the save, and what happens on a failed or a successful save.

---

[Spells > Saving Throws]
## Saving Throws  
Many spells specify that a target makes a saving throw to avoid some or all of a spell's effects. The spell specifies the ability that the target uses for the save and what happens on a success or failure. Here's how to calculate the DC for your spells:  
**Spell save DC** = 8 + your spellcasting ability modifier + your Proficiency Bonus
```
</details>


### v6_agentic  (9 chunks, 3 LLM call(s))

Death saving throws involve rolling a d20. A roll of 10 or higher is a success, while a roll of 9 or lower is a failure. On a natural 1, you suffer two failures. On a natural 20, you regain 1 Hit Point.

To stabilize a creature with 0 Hit Points using the Help action, a DC 10 Wisdom (Medicine) check is required.

*facts found (judge): 3/5; missing: 12 or higher; third failure*

*agentic sub-queries:* death saving throw / natural 1 death save / natural 20 death save / stabilize with help action


*re-ranking* (query: `death saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 8.45 | yes | Playing the Game > Death Saving Throws |
| 2 | 1 | 8.13 | yes | Rules Glossary > Death Saving Throw |
| 3 | 2 | 7.71 | yes | Playing the Game > Death Saving Throws |
| 4 | 13 | 6.33 |  | Playing the Game > Death Saving Throws |
| 5 | 12 | 5.47 |  | Playing the Game > Saving Throws |
| 6 | 6 | 5.35 |  | Playing the Game > Falling Unconscious |
| 7 | 11 | 5.15 | yes | Playing the Game > Stabilizing a Character |
| 8 | 8 | 5.15 | yes | Classes > Level 18: Survivor |
| 9 | 15 | 5.11 |  | Monsters A–Z > Traits |
| 10 | 14 | 4.93 |  | Monsters A–Z > Traits |
| 11 | 4 | 4.90 |  | Spells > Finger of Death |
| 12 | 19 | 4.70 |  | Monsters A–Z > Actions |
| 13 | 9 | 4.39 |  | Rules Glossary > Saving Throw |
| 14 | 5 | 3.94 |  | Spells > Circle of Death |
| 15 | 17 | 3.87 |  | Monsters A–Z > Traits |
| 16 | 10 | 3.55 |  | Rules Glossary > Stable |
| 17 | 20 | 2.64 |  | Classes > Level 17: Quivering Palm |
| 18 | 16 | 1.14 |  | Gameplay Toolbox > Poisoned Needle |
| 19 | 7 | 1.08 |  | Rules Glossary > Save |
| 20 | 18 | -6.17 |  | Spells > Resurrection |


*re-ranking* (query: `natural 1 death save`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.27 | yes | Magic Items > Periapt of Wound Closure |
| 2 | 5 | -0.15 | yes | Playing the Game > Death Saving Throws |
| 3 | 3 | -1.09 | yes | Playing the Game > Death Saving Throws |
| 4 | 9 | -1.21 |  | Playing the Game > Death Saving Throws |
| 5 | 10 | -1.23 | yes | Rules Glossary > Death Saving Throw |
| 6 | 4 | -1.31 | yes | Playing the Game > Stabilizing a Character |
| 7 | 6 | -4.01 |  | Playing the Game > Falling Unconscious |
| 8 | 19 | -4.48 |  | Spells > Finger of Death |
| 9 | 12 | -4.63 |  | Classes > Level 6: Natural Recovery |
| 10 | 2 | -4.86 |  | Spells > Circle of Death |
| 11 | 14 | -5.18 |  | Monsters A–Z > Death Dog |
| 12 | 20 | -5.30 |  | Magic Items > Avatar of Death |
| 13 | 13 | -5.88 |  | Playing the Game > Saving Throws |
| 14 | 15 | -6.14 |  | Spells > Phantasmal Killer |
| 15 | 16 | -6.66 |  | Playing the Game > Rolling 20 or 1 |
| 16 | 11 | -6.72 |  | Spells > Phantasmal Killer |
| 17 | 7 | -8.30 |  | Spells > Resurrection |
| 18 | 18 | -8.32 |  | Spells > Death Ward |
| 19 | 17 | -8.38 |  | Spells > Weird |
| 20 | 8 | -9.05 |  | Spells > Raise Dead |


*re-ranking* (query: `natural 20 death save`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.24 | yes | Playing the Game > Death Saving Throws |
| 2 | 1 | 2.22 | yes | Classes > Level 18: Survivor |
| 3 | 15 | 0.87 | yes | Magic Items > Bag of Beans |
| 4 | 4 | -0.85 | yes | Magic Items > Periapt of Wound Closure |
| 5 | 5 | -0.97 |  | Playing the Game > Rolling 20 or 1 |
| 6 | 20 | -1.51 |  | Monsters A–Z > Actions |
| 7 | 12 | -1.98 |  | Magic Items > Avatar of Death |
| 8 | 6 | -3.30 | yes | Playing the Game > Death Saving Throws |
| 9 | 11 | -3.57 | yes | Rules Glossary > Death Saving Throw |
| 10 | 9 | -3.89 | yes | Playing the Game > Stabilizing a Character |
| 11 | 8 | -5.74 |  | Spells > Finger of Death |
| 12 | 16 | -5.76 |  | Monsters A–Z > Death Dog |
| 13 | 3 | -6.18 |  | Spells > Circle of Death |
| 14 | 7 | -6.42 |  | Classes > Level 20: Words of Creation |
| 15 | 10 | -7.89 |  | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 16 | 19 | -8.69 |  | Spells > Phantasmal Killer |
| 17 | 17 | -9.00 |  | Classes > Level 3: Land's Aid |
| 18 | 13 | -9.01 |  | Spells > Spare the Dying |
| 19 | 14 | -9.06 |  | Spells > Phantasmal Killer |
| 20 | 18 | -10.07 |  | Classes > Level 6: Natural Recovery |


*re-ranking* (query: `stabilize with help action`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.60 | yes | Playing the Game > Stabilizing a Character |
| 2 | 4 | 0.42 | yes | Rules Glossary > Help [Action] |
| 3 | 10 | -0.21 | yes | Rules Glossary > Help [Action] |
| 4 | 6 | -1.99 |  | Equipment > Healer's Kit (5 GP) |
| 5 | 2 | -3.92 |  | Playing the Game > One Thing at a Time |
| 6 | 12 | -4.73 |  | Playing the Game > Actions |
| 7 | 18 | -6.49 |  | Classes > Level 10: Tireless |
| 8 | 16 | -6.52 |  | Rules Glossary > Action |
| 9 | 19 | -9.45 |  | Monsters A–Z > Bonus Actions |
| 10 | 11 | -9.59 |  | Spells > Aid |
| 11 | 9 | -10.22 |  | Monsters A–Z > Actions |
| 12 | 7 | -10.29 |  | Classes > Level 10: Divine Intervention |
| 13 | 3 | -10.53 |  | Spells > Hold Person |
| 14 | 15 | -10.58 |  | Monsters A–Z > Actions |
| 15 | 13 | -10.61 |  | Spells > Hold Monster |
| 16 | 17 | -10.76 |  | Monsters A–Z > Bonus Actions |
| 17 | 8 | -10.97 |  | Playing the Game > Adventuring Equipment |
| 18 | 5 | -10.99 |  | Classes > Level 9: Abjure Foes |
| 19 | 14 | -11.28 |  | Character Creation > The Nine Alignments |
| 20 | 20 | -11.35 |  | Rules Glossary > Indifferent [Attitude] |

*retrieved sections:* Playing the Game > Death Saving Throws | Rules Glossary > Death Saving Throw | Magic Items > Periapt of Wound Closure | Classes > Level 18: Survivor | Magic Items > Bag of Beans | Playing the Game > Stabilizing a Character | Rules Glossary > Help [Action]

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
#### Death Saving Throws  
Whenever you start your turn with 0 Hit Points, you must make a Death Saving Throw to determine whether you creep closer to death or hang on to life. Unlike other saving throws, this one isn't tied to an ability score. You're in the hands of fate now.

---

[Rules Glossary > Death Saving Throw]
#### Death Saving Throw  
A player character must make a Death Saving Throw (also called a Death Save) if they start their turn with 0 Hit Points. _See also_ "Playing the Game" ("Damage and Healing").

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Magic Items > Periapt of Wound Closure]
#### Periapt of Wound Closure  
_Wondrous Item, Uncommon (Requires Attunement)_  
While wearing this pendant, you gain the following benefits.  
**_Life Preservation._** Whenever you make a Death Saving Throw, you can change a roll of 9 or lower to a 10, turning a failed save into a successful one.  
**_Natural Healing Boost._** Whenever you roll a Hit Point Die to regain Hit Points, double the number of Hit Points it restores.

---

[Classes > Level 18: Survivor]
#### Level 18: Survivor  
You attain the pinnacle of resilience in battle, giving you these benefits.  
_Defy Death._ You have Advantage on Death Saving Throws. Moreover, when you roll 18–20 on a Death Saving Throw, you gain the benefit of rolling a 20 on it.  
_Heroic Rally._ At the start of each of your turns, you regain Hit Points equal to 5 plus your Constitution modifier if you are Bloodied and have at least 1 Hit Point.

---

[Magic Items > Bag of Beans]
</tr>
<tr>
<td>81–90</td>
<td>A nest of 1d4 + 3 rainbow-colored eggs springs up. Any creature that eats an egg makes a DC 20 Constitution saving throw. On a successful save, a creature permanently increases its lowest ability score by 1, randomly choosing among equally low scores. On a failed save, the creature takes 10d6 Force damage from an internal explosion.</td>
</tr>
<tr>
<td>91–95</td>

---

[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Rules Glossary > Help [Action]]
#### Help [Action]  
When you take the Help action, you do one of the following.  
_Assist an Ability Check._ Choose one of your skill or tool proficiencies and one ally who is near
enough for you to assist verbally or physically when they make an ability check. That ally has Advantage on the next ability check they make with the chosen skill or tool. This benefit expires if the ally doesn't use it before the start of your next turn. The GM has final say on whether your assistance is possible.

---

[Rules Glossary > Help [Action]]
_Assist an Attack Roll._ You momentarily distract an enemy within 5 feet of you, giving Advantage to the next attack roll by one of your allies against that enemy. This benefit expires at the start of your next turn.
```
</details>


---

## q16 (cross-file) What are the Hit Point Die and saving throw proficiencies of the Barbarian and of the Bard?

**Gold facts (counterfactual data):** D10 per Barbarian level; D8 per Bard level; Strength and Constitution; Dexterity and Charisma


### v0_closed_book  (0 chunks, 1 LLM call(s))

The Barbarian's Hit Point Die is 12d and they have proficiency in Strength and Constitution saving throws.

The Bard's Hit Point Die is 6d and they have proficiency in Wisdom, Dexterity, and Charisma saving throws.

*facts found (judge): 2/4; missing: D10 per Barbarian level; D8 per Bard level*


### v1_baseline  (3 chunks, 1 LLM call(s))

The Hit Point Die for the Barbarian is D10 per Barbarian level. The saving throw proficiencies for the Barbarian are Strength and Constitution.

The Hit Point Die for the Bard is D8 per Bard level. The saving throw proficiencies for the Bard are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*

*retrieved sections:* Classes > Barbarian | Classes > As a Multiclass Character | Classes > Bard

<details><summary>full retrieved context</summary>

```
[Classes > Barbarian]
# Classes  
## Barbarian  
**Core Barbarian Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Barbarian level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Constitution</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Classes > As a Multiclass Character]
#### As a Multiclass Character  
• Gain the following traits from the Core Bard Traits table: Hit Point Die, proficiency in one skill of your choice, proficiency with one Musical Instrument of your choice, and training with Light armor.
• Gain the Bard's level 1 features, which are listed in the Bard Features table. See the multiclassing rules in "Character Creation" to determine your available spell slots.

---

[Classes > Bard]
## Bard  
**Core Bard Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Bard level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose any 3 skills (see Playing the Game)</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Tool Proficiencies</td>
<td>Choose 3 Musical Instruments (see Equipment)</td>
</tr>
<tr>
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The Hit Point Die for the Barbarian is D10 per Barbarian level, and their saving throw proficiencies are Strength and Constitution.

The Hit Point Die for the Bard is D8 per Bard level, and their saving throw proficiencies are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Hit Point Die and saving throw proficiencies of the Barbarian and o`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.07 | yes | Classes > Barbarian |
| 2 | 3 | 2.28 | yes | Classes > Bard |
| 3 | 5 | -0.03 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 7 | -0.75 |  | Classes > As a Multiclass Character |
| 5 | 2 | -1.94 |  | Classes > As a Multiclass Character |
| 6 | 4 | -6.92 |  | Classes > Level 1: Bardic Inspiration |
| 7 | 9 | -7.94 |  | Classes > Level 1: Bardic Inspiration |
| 8 | 10 | -8.08 |  | Classes > Level 14: Peerless Skill |
| 9 | 6 | -9.03 |  | Classes > Bard Class Features |
| 10 | 8 | -11.34 |  | Playing the Game > D20 Tests |

*retrieved sections:* Classes > Barbarian | Classes > Bard | Playing the Game > Saving Throw Proficiencies

<details><summary>full retrieved context</summary>

```
[Classes > Barbarian]
# Classes  
## Barbarian  
**Core Barbarian Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Barbarian level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Constitution</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Classes > Bard]
## Bard  
**Core Bard Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Bard level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose any 3 skills (see Playing the Game)</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Tool Proficiencies</td>
<td>Choose 3 Musical Instruments (see Equipment)</td>
</tr>
<tr>

---

[Playing the Game > Saving Throw Proficiencies]
Each class gives proficiency in at least two saving throws, representing that class's training in evading or resisting certain threats. Wizards, for example, are proficient in Intelligence and Wisdom saves; they train to resist mental assault.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The Hit Point Die for the Barbarian is D10 per Barbarian level, and their saving throw proficiencies are Strength and Constitution.

The Hit Point Die for the Bard is D8 per Bard level, and their saving throw proficiencies are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Hit Point Die and saving throw proficiencies of the Barbarian and o`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.07 | yes | Classes > Barbarian |
| 2 | 3 | 2.28 | yes | Classes > Bard |
| 3 | 5 | -0.03 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 7 | -0.75 | yes | Classes > As a Multiclass Character |
| 5 | 2 | -1.94 | yes | Classes > As a Multiclass Character |
| 6 | 4 | -6.92 | yes | Classes > Level 1: Bardic Inspiration |
| 7 | 9 | -7.94 | yes | Classes > Level 1: Bardic Inspiration |
| 8 | 10 | -8.08 | yes | Classes > Level 14: Peerless Skill |
| 9 | 6 | -9.03 |  | Classes > Bard Class Features |
| 10 | 8 | -11.34 |  | Playing the Game > D20 Tests |

*retrieved sections:* Classes > Barbarian | Classes > Bard | Playing the Game > Saving Throw Proficiencies | Classes > As a Multiclass Character | Classes > Level 1: Bardic Inspiration | Classes > Level 14: Peerless Skill

<details><summary>full retrieved context</summary>

```
[Classes > Barbarian]
# Classes  
## Barbarian  
**Core Barbarian Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Barbarian level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Constitution</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Classes > Bard]
## Bard  
**Core Bard Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Bard level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose any 3 skills (see Playing the Game)</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Tool Proficiencies</td>
<td>Choose 3 Musical Instruments (see Equipment)</td>
</tr>
<tr>

---

[Playing the Game > Saving Throw Proficiencies]
Each class gives proficiency in at least two saving throws, representing that class's training in evading or resisting certain threats. Wizards, for example, are proficient in Intelligence and Wisdom saves; they train to resist mental assault.

---

[Classes > As a Multiclass Character]
#### As a Multiclass Character  
• Gain the following traits from the Core Barbarian Traits table: Hit Point Die, proficiency with Martial weapons, and training with Shields.
• Gain the Barbarian's level 1 features, which are listed in the Barbarian Features table.

---

[Classes > As a Multiclass Character]
#### As a Multiclass Character  
• Gain the following traits from the Core Bard Traits table: Hit Point Die, proficiency in one skill of your choice, proficiency with one Musical Instrument of your choice, and training with Light armor.
• Gain the Bard's level 1 features, which are listed in the Bard Features table. See the multiclassing rules in "Character Creation" to determine your available spell slots.

---

[Classes > Level 1: Bardic Inspiration]
_At Higher Levels._ Your Bardic Inspiration die changes when you reach certain Bard levels, as shown in the Bardic Die column of the Bard Features table. The die becomes a d8 at level 5, a d10 at level 10, and a d12 at level 15.

---

[Classes > Level 1: Bardic Inspiration]
Once within the next hour when the creature fails a D20 Test, the creature can roll the Bardic Inspiration die and add the number rolled to the d20, potentially turning the failure into a success. A Bardic Inspiration die is expended when it's rolled.  
_Number of Uses._ You can confer a Bardic Inspiration die a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 14: Peerless Skill]
#### Level 14: Peerless Skill  
When you make an ability check or attack roll and fail, you can expend one use of Bardic Inspiration; roll the Bardic Inspiration die, and add the number rolled to the d20, potentially turning a failure into a success. On a failure, the Bardic Inspiration isn't expended.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The Hit Point Die for the Barbarian is D10 per Barbarian level, and their saving throw proficiencies are Strength and Constitution.

The Hit Point Die for the Bard is D8 per Bard level, and their saving throw proficiencies are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Hit Point Die and saving throw proficiencies of the Barbarian and o`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.07 | yes | Classes > Barbarian |
| 2 | 3 | 2.28 | yes | Classes > Bard |
| 3 | 5 | -0.03 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 7 | -0.75 |  | Classes > As a Multiclass Character |
| 5 | 2 | -1.94 |  | Classes > As a Multiclass Character |
| 6 | 4 | -6.92 |  | Classes > Level 1: Bardic Inspiration |
| 7 | 9 | -7.94 |  | Classes > Level 1: Bardic Inspiration |
| 8 | 10 | -8.08 |  | Classes > Level 14: Peerless Skill |
| 9 | 6 | -9.03 |  | Classes > Bard Class Features |
| 10 | 8 | -11.34 |  | Playing the Game > D20 Tests |

*retrieved sections:* Classes > Barbarian | Classes > Bard | Playing the Game > Saving Throw Proficiencies

<details><summary>full retrieved context</summary>

```
[Classes > Barbarian]
# Classes  
## Barbarian  
**Core Barbarian Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Barbarian level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Constitution</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Classes > Bard]
## Bard  
**Core Bard Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Bard level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose any 3 skills (see Playing the Game)</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Tool Proficiencies</td>
<td>Choose 3 Musical Instruments (see Equipment)</td>
</tr>
<tr>

---

[Playing the Game > Saving Throw Proficiencies]
Each class gives proficiency in at least two saving throws, representing that class's training in evading or resisting certain threats. Wizards, for example, are proficient in Intelligence and Wisdom saves; they train to resist mental assault.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The Hit Point Die for the Barbarian is D10 per Barbarian level, and their saving throw proficiencies are Strength and Constitution.

The Hit Point Die for the Bard is D8 per Bard level, and their saving throw proficiencies are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Hit Point Die and saving throw proficiencies of the Barbarian and o`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.07 | yes | Classes > Barbarian |
| 2 | 2 | 2.28 | yes | Classes > Bard |
| 3 | 21 | -0.01 | yes | Classes > Level 2: Wild Shape |
| 4 | 6 | -0.03 | yes | Playing the Game > Saving Throw Proficiencies |
| 5 | 14 | -0.14 | yes | Classes > Sorcerer |
| 6 | 15 | -0.14 | yes | Classes > Warlock |
| 7 | 12 | -0.19 | yes | Classes > Rogue |
| 8 | 29 | -0.19 | yes | Classes > Paladin |
| 9 | 5 | -0.20 |  | Classes > Cleric |
| 10 | 10 | -0.34 |  | Playing the Game > Saving Throw Proficiencies |
| 11 | 23 | -0.46 |  | Classes > Fighter |
| 12 | 11 | -0.59 |  | Classes > Druid |
| 13 | 25 | -0.59 |  | Classes > Monk |
| 14 | 7 | -0.69 |  | Playing the Game > Death Saving Throws |
| 15 | 3 | -0.75 |  | Classes > As a Multiclass Character |
| 16 | 27 | -1.00 |  | Classes > Ranger |
| 17 | 4 | -1.94 |  | Classes > As a Multiclass Character |
| 18 | 9 | -3.10 |  | Character Creation > Gaining a Level |
| 19 | 13 | -4.52 |  | Classes > As a Multiclass Character |
| 20 | 17 | -5.39 |  | Character Creation > Hit Points and Hit Point Dice |

*retrieved sections:* Classes > Barbarian | Classes > Bard | Classes > Level 2: Wild Shape | Playing the Game > Saving Throw Proficiencies | Classes > Sorcerer | Classes > Warlock | Classes > Rogue | Classes > Paladin

<details><summary>full retrieved context</summary>

```
[Classes > Barbarian]
# Classes  
## Barbarian  
**Core Barbarian Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Barbarian level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Constitution</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Classes > Bard]
## Bard  
**Core Bard Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Bard level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose any 3 skills (see Playing the Game)</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Tool Proficiencies</td>
<td>Choose 3 Musical Instruments (see Equipment)</td>
</tr>
<tr>

---

[Classes > Level 2: Wild Shape]
**Game Statistics.** Your game statistics are replaced by the Beast's stat block, but you retain your creature type; Hit Points; Hit Point Dice; Intelligence, Wisdom, and Charisma scores; class features; languages; and feats. You also retain your skill and saving throw proficiencies and use your Proficiency Bonus for them, in addition to gaining the proficiencies of the creature. If a skill or saving throw modifier in the Beast's stat block is higher than yours, use the one in the stat block.

---

[Playing the Game > Saving Throw Proficiencies]
Each class gives proficiency in at least two saving throws, representing that class's training in evading or resisting certain threats. Wizards, for example, are proficient in Intelligence and Wisdom saves; they train to resist mental assault.

---

[Classes > Sorcerer]
## Sorcerer  
**Core Sorcerer Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D6 per Sorcerer level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Constitution and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Arcana, Deception, Insight, Intimidation, Persuasion, or Religion</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Armor Training</td>
<td>None</td>
</tr>

---

[Classes > Warlock]
## Warlock  
**Core Warlock Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Warlock level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Wisdom and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Arcana, Deception, History, Intimidation, Investigation, Nature, or Religion</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Armor Training</td>
<td>Light armor</td>

---

[Classes > Rogue]
## Rogue  
**Core Rogue Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Dexterity</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Rogue level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Intelligence</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 4: Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Persuasion, Sleight of Hand, or Stealth</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>

---

[Classes > Paladin]
## Paladin  
**Core Paladin Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength and Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Paladin level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Wisdom and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Athletics, Insight, Intimidation, Medicine, Persuasion, or Religion</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>
<td>Armor Training</td>
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The Hit Point Die for the Barbarian is D10 per Barbarian level, and their saving throw proficiencies are Strength and Constitution.

The Hit Point Die for the Bard is D8 per Bard level, and their saving throw proficiencies are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Hit Point Die and saving throw proficiencies of the Barbarian and o`): candidate pool of 22, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.07 | yes | Classes > Barbarian |
| 2 | 2 | 2.28 | yes | Classes > Bard |
| 3 | 6 | -0.03 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 5 | -0.20 | yes | Classes > Cleric |
| 5 | 10 | -0.34 | yes | Playing the Game > Saving Throw Proficiencies |
| 6 | 7 | -0.69 | yes | Playing the Game > Death Saving Throws |
| 7 | 3 | -0.75 | yes | Classes > As a Multiclass Character |
| 8 | 4 | -1.94 | yes | Classes > As a Multiclass Character |
| 9 | 9 | -3.10 |  | Character Creation > Gaining a Level |
| 10 | 13 | -5.00 |  | Monsters A–Z > Traits |
| 11 | 12 | -6.43 |  | Monsters A–Z > Traits |
| 12 | 8 | -6.92 |  | Classes > Level 1: Bardic Inspiration |
| 13 | 19 | -7.74 |  | Playing the Game > Proficiency |
| 14 | 17 | -8.74 |  | Playing the Game > Skill Proficiencies |
| 15 | 18 | -9.62 |  | Character Origins > Skill Proficiencies |
| 16 | 20 | -10.23 |  | Rules Glossary > Proficiency |
| 17 | 14 | -10.30 |  | Character Creation > Proficiencies |
| 18 | 11 | -10.85 |  | Classes > Barbarian |
| 19 | 15 | -10.93 |  | Equipment > Weapons |
| 20 | 16 | -11.38 |  | Equipment > Weapons |

*retrieved sections:* Classes > Barbarian | Classes > Bard | Playing the Game > Saving Throw Proficiencies | Classes > Cleric | Playing the Game > Death Saving Throws | Classes > As a Multiclass Character

<details><summary>full retrieved context</summary>

```
[Classes > Barbarian]
# Classes  
## Barbarian  
**Core Barbarian Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Barbarian level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Constitution</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Classes > Bard]
## Bard  
**Core Bard Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Bard level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose any 3 skills (see Playing the Game)</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Tool Proficiencies</td>
<td>Choose 3 Musical Instruments (see Equipment)</td>
</tr>
<tr>

---

[Playing the Game > Saving Throw Proficiencies]
Each class gives proficiency in at least two saving throws, representing that class's training in evading or resisting certain threats. Wizards, for example, are proficient in Intelligence and Wisdom saves; they train to resist mental assault.

---

[Classes > Cleric]
## Cleric  
**Core Cleric Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Wisdom</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Cleric level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Wisdom and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: History, Insight, Medicine, Persuasion, or Religion</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Armor Training</td>
<td>Light and Medium armor and Shields</td>
</tr>

---

[Playing the Game > Saving Throw Proficiencies]
### Saving Throw Proficiencies  
Proficiency in a saving throw lets a character add their Proficiency Bonus to saves that use a particular ability. For example, proficiency in Wisdom saves lets you add your Proficiency Bonus to your Wisdom saves. Some monsters also have saving throw proficiencies, as noted in their stat blocks.

---

[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Classes > As a Multiclass Character]
#### As a Multiclass Character  
• Gain the following traits from the Core Barbarian Traits table: Hit Point Die, proficiency with Martial weapons, and training with Shields.
• Gain the Barbarian's level 1 features, which are listed in the Barbarian Features table.

---

[Classes > As a Multiclass Character]
#### As a Multiclass Character  
• Gain the following traits from the Core Bard Traits table: Hit Point Die, proficiency in one skill of your choice, proficiency with one Musical Instrument of your choice, and training with Light armor.
• Gain the Bard's level 1 features, which are listed in the Bard Features table. See the multiclassing rules in "Character Creation" to determine your available spell slots.
```
</details>


### v6_agentic  (8 chunks, 3 LLM call(s))

The Hit Point Die for the Barbarian is D10 per Barbarian level, and for the Bard, it is D8 per Bard level.

The saving throw proficiencies for the Barbarian are Strength and Constitution.

The saving throw proficiencies for the Bard are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* barbarian hit point die / barbarian saving throw proficiencies / bard hit point die / bard saving throw proficiencies


*re-ranking* (query: `barbarian hit point die`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 5.89 | yes | Classes > As a Multiclass Character |
| 2 | 2 | 4.81 | yes | Classes > Barbarian |
| 3 | 10 | 4.38 | yes | Character Creation > Gaining a Level |
| 4 | 8 | 3.61 |  | Classes > Level 11: Relentless Rage |
| 5 | 20 | 0.02 |  | Character Creation > Hit Points and Hit Point Dice |
| 6 | 4 | -0.19 |  | Classes > As a Multiclass Character |
| 7 | 18 | -0.44 |  | Monsters > Hit Points |
| 8 | 16 | -1.31 |  | Playing the Game > Instant Death |
| 9 | 7 | -1.33 |  | Playing the Game > Hit Points |
| 10 | 12 | -1.49 |  | Rules Glossary > Short Rest |
| 11 | 14 | -1.51 |  | Character Creation > Fill In Numbers |
| 12 | 3 | -1.91 |  | Playing the Game > Instant Death |
| 13 | 11 | -2.82 |  | Playing the Game > Dropping to 0 Hit Points |
| 14 | 1 | -4.43 |  | Playing the Game > Death Saving Throws |
| 15 | 5 | -4.54 |  | Rules Glossary > Hit Point Dice |
| 16 | 13 | -5.21 |  | Classes > Barbarian Class Features |
| 17 | 9 | -5.43 |  | Classes > Barbarian Class Features |
| 18 | 15 | -7.55 |  | Playing the Game > Lose Temporary Hit Points First |
| 19 | 17 | -7.72 |  | Classes > Barbarian Class Features |
| 20 | 19 | -8.08 |  | Animals > Actions |


*re-ranking* (query: `barbarian saving throw proficiencies`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.88 | yes | Classes > Barbarian |
| 2 | 1 | 4.19 | yes | Playing the Game > Saving Throw Proficiencies |
| 3 | 3 | 3.61 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 19 | 1.92 |  | Classes > Level 11: Relentless Rage |
| 5 | 13 | 1.62 |  | Classes > Level 2: Wild Shape |
| 6 | 7 | 1.26 |  | Classes > Warlock |
| 7 | 8 | 0.29 |  | Classes > Sorcerer |
| 8 | 20 | 0.28 |  | Classes > Wizard |
| 9 | 6 | 0.02 |  | Classes > Druid |
| 10 | 9 | -0.18 | yes | Classes > Bard |
| 11 | 15 | -0.30 |  | Classes > Cleric |
| 12 | 14 | -7.12 |  | Classes > Barbarian Class Features |
| 13 | 16 | -7.52 |  | Classes > Barbarian Class Features |
| 14 | 17 | -9.11 |  | Classes > Level 3: Bonus Proficiencies |
| 15 | 5 | -9.35 | yes | Classes > As a Multiclass Character |
| 16 | 18 | -9.53 |  | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 17 | 12 | -9.67 |  | Classes > Barbarian Class Features |
| 18 | 4 | -10.06 |  | Character Creation > Proficiencies |
| 19 | 11 | -10.28 |  | Character Creation > Choose a Background |
| 20 | 10 | -10.30 |  | Character Origins > Skill Proficiencies |


*re-ranking* (query: `bard hit point die`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 6.12 | yes | Classes > As a Multiclass Character |
| 2 | 4 | 4.33 | yes | Classes > Bard |
| 3 | 5 | 3.04 | yes | Spells > Power Word Kill |
| 4 | 1 | 0.80 |  | Classes > Level 1: Bardic Inspiration |
| 5 | 15 | 0.44 |  | Classes > Level 1: Bardic Inspiration |
| 6 | 11 | 0.42 |  | Classes > As a Multiclass Character |
| 7 | 17 | -0.13 | yes | Character Creation > Gaining a Level |
| 8 | 6 | -0.20 |  | Classes > As a Multiclass Character |
| 9 | 16 | -0.36 |  | Character Creation > Fill In Numbers |
| 10 | 13 | -0.50 |  | Rules Glossary > Short Rest |
| 11 | 20 | -1.04 |  | Monsters > Hit Points |
| 12 | 7 | -1.83 |  | Playing the Game > Instant Death |
| 13 | 12 | -2.02 |  | Playing the Game > Hit Points |
| 14 | 9 | -2.13 |  | Playing the Game > Instant Death |
| 15 | 14 | -2.20 |  | Classes > Level 3: Cutting Words |
| 16 | 8 | -2.86 |  | Classes > Bard Class Features |
| 17 | 3 | -3.83 |  | Playing the Game > Death Saving Throws |
| 18 | 10 | -4.79 |  | Rules Glossary > Hit Point Dice |
| 19 | 19 | -7.02 |  | Classes > Bard Class Features |
| 20 | 18 | -7.40 |  | Classes > Bard Class Features |


*re-ranking* (query: `bard saving throw proficiencies`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.41 | yes | Classes > Bard |
| 2 | 1 | 4.04 | yes | Playing the Game > Saving Throw Proficiencies |
| 3 | 3 | 3.37 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 20 | 0.37 |  | Classes > Sorcerer |
| 5 | 15 | 0.35 | yes | Classes > Barbarian |
| 6 | 10 | 0.20 |  | Classes > Druid |
| 7 | 16 | 0.12 |  | Classes > Level 2: Wild Shape |
| 8 | 13 | 0.03 |  | Classes > Rogue |
| 9 | 12 | -0.38 |  | Classes > Fighter |
| 10 | 19 | -0.65 |  | Classes > Ranger |
| 11 | 4 | -1.96 |  | Classes > Level 2: Expertise |
| 12 | 14 | -6.63 |  | Playing the Game > Proficiency Bonus |
| 13 | 11 | -7.43 |  | Classes > Level 14: Peerless Skill |
| 14 | 17 | -8.28 |  | Classes > Bard Class Features |
| 15 | 8 | -8.58 |  | Classes > Level 3: Bonus Proficiencies |
| 16 | 9 | -9.50 | yes | Classes > As a Multiclass Character |
| 17 | 5 | -9.67 |  | Character Creation > Proficiencies |
| 18 | 18 | -9.70 |  | Classes > Level 10: Magical Secrets |
| 19 | 7 | -9.81 |  | Character Creation > Choose a Background |
| 20 | 6 | -9.89 |  | Character Origins > Skill Proficiencies |


*re-ranking* (query: `bard hit point die`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 6.12 | yes | Classes > As a Multiclass Character |
| 2 | 4 | 4.33 | yes | Classes > Bard |
| 3 | 5 | 3.04 | yes | Spells > Power Word Kill |
| 4 | 1 | 0.80 |  | Classes > Level 1: Bardic Inspiration |
| 5 | 15 | 0.44 |  | Classes > Level 1: Bardic Inspiration |
| 6 | 11 | 0.42 |  | Classes > As a Multiclass Character |
| 7 | 17 | -0.13 | yes | Character Creation > Gaining a Level |
| 8 | 6 | -0.20 |  | Classes > As a Multiclass Character |
| 9 | 16 | -0.36 |  | Character Creation > Fill In Numbers |
| 10 | 13 | -0.50 |  | Rules Glossary > Short Rest |
| 11 | 20 | -1.04 |  | Monsters > Hit Points |
| 12 | 7 | -1.83 |  | Playing the Game > Instant Death |
| 13 | 12 | -2.02 |  | Playing the Game > Hit Points |
| 14 | 9 | -2.13 |  | Playing the Game > Instant Death |
| 15 | 14 | -2.20 |  | Classes > Level 3: Cutting Words |
| 16 | 8 | -2.86 |  | Classes > Bard Class Features |
| 17 | 3 | -3.83 |  | Playing the Game > Death Saving Throws |
| 18 | 10 | -4.79 |  | Rules Glossary > Hit Point Dice |
| 19 | 19 | -7.02 |  | Classes > Bard Class Features |
| 20 | 18 | -7.40 |  | Classes > Bard Class Features |


*re-ranking* (query: `bard saving throw proficiencies`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.41 | yes | Classes > Bard |
| 2 | 1 | 4.04 | yes | Playing the Game > Saving Throw Proficiencies |
| 3 | 3 | 3.37 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 20 | 0.37 |  | Classes > Sorcerer |
| 5 | 15 | 0.35 | yes | Classes > Barbarian |
| 6 | 10 | 0.20 |  | Classes > Druid |
| 7 | 16 | 0.12 |  | Classes > Level 2: Wild Shape |
| 8 | 13 | 0.03 |  | Classes > Rogue |
| 9 | 12 | -0.38 |  | Classes > Fighter |
| 10 | 19 | -0.65 |  | Classes > Ranger |
| 11 | 4 | -1.96 |  | Classes > Level 2: Expertise |
| 12 | 14 | -6.63 |  | Playing the Game > Proficiency Bonus |
| 13 | 11 | -7.43 |  | Classes > Level 14: Peerless Skill |
| 14 | 17 | -8.28 |  | Classes > Bard Class Features |
| 15 | 8 | -8.58 |  | Classes > Level 3: Bonus Proficiencies |
| 16 | 9 | -9.50 | yes | Classes > As a Multiclass Character |
| 17 | 5 | -9.67 |  | Character Creation > Proficiencies |
| 18 | 18 | -9.70 |  | Classes > Level 10: Magical Secrets |
| 19 | 7 | -9.81 |  | Character Creation > Choose a Background |
| 20 | 6 | -9.89 |  | Character Origins > Skill Proficiencies |

*retrieved sections:* Classes > As a Multiclass Character | Classes > Barbarian | Character Creation > Gaining a Level | Playing the Game > Saving Throw Proficiencies | Classes > Bard | Spells > Power Word Kill

<details><summary>full retrieved context</summary>

```
[Classes > As a Multiclass Character]
#### As a Multiclass Character  
• Gain the following traits from the Core Barbarian Traits table: Hit Point Die, proficiency with Martial weapons, and training with Shields.
• Gain the Barbarian's level 1 features, which are listed in the Barbarian Features table.

---

[Classes > Barbarian]
# Classes  
## Barbarian  
**Core Barbarian Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Strength</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Barbarian level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Constitution</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 2: Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Character Creation > Gaining a Level]
**2: Adjust Hit Points and Hit Point Dice.** Each time you gain a level, you gain an additional Hit Die. Roll that die, add your Constitution modifier to the roll, and add the total (minimum of 1) to your Hit Point maximum. Instead of rolling, you can use the fixed value shown in the Fixed Hit Points by Class table.  
**Fixed Hit Points by Class**  
<table>
<thead>
<tr>
<th>Class</th>
<th>Hit Points per Level</th>
</tr>
</thead>
<tbody>
<tr>
<td>Barbarian</td>
<td>7 + Con. modifier</td>
</tr>

---

[Playing the Game > Saving Throw Proficiencies]
### Saving Throw Proficiencies  
Proficiency in a saving throw lets a character add their Proficiency Bonus to saves that use a particular ability. For example, proficiency in Wisdom saves lets you add your Proficiency Bonus to your Wisdom saves. Some monsters also have saving throw proficiencies, as noted in their stat blocks.

---

[Playing the Game > Saving Throw Proficiencies]
Each class gives proficiency in at least two saving throws, representing that class's training in evading or resisting certain threats. Wizards, for example, are proficient in Intelligence and Wisdom saves; they train to resist mental assault.

---

[Classes > As a Multiclass Character]
#### As a Multiclass Character  
• Gain the following traits from the Core Bard Traits table: Hit Point Die, proficiency in one skill of your choice, proficiency with one Musical Instrument of your choice, and training with Light armor.
• Gain the Bard's level 1 features, which are listed in the Bard Features table. See the multiclassing rules in "Character Creation" to determine your available spell slots.

---

[Classes > Bard]
## Bard  
**Core Bard Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Charisma</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D8 per Bard level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Dexterity and Charisma</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose any 3 skills (see Playing the Game)</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple weapons</td>
</tr>
<tr>
<td>Tool Proficiencies</td>
<td>Choose 3 Musical Instruments (see Equipment)</td>
</tr>
<tr>

---

[Spells > Power Word Kill]
#### Power Word Kill  
_Level 9 Enchantment (Bard, Sorcerer, Warlock, Wizard)_  
**Casting Time:** Action
**Range:** 60 feet
**Component:** V
**Duration:** Instantaneous  
You compel one creature you can see within range to die. If the target has 100 Hit Points or fewer, it dies. Otherwise, it takes 12d12 Psychic damage.
```
</details>


---

## q17 (reasoning) A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What is its attack bonus, its damage on a hit, the extra damage if the attack roll had Advantage, and what AC must the attack beat?

**Gold facts (counterfactual data):** +4; 5 (1d6 + 2); 2 (1d4); 16 in Chain Mail


### v0_closed_book  (0 chunks, 1 LLM call(s))

A Goblin Warrior in D&D 5e has the following stats for an attack with its Scimitar:

- **Attack Bonus:** The Goblin Warrior has a +6 to hit with a Scimitar.
- **Damage on a Hit:** On a successful hit, it deals 1d6 slashing damage.
- **Extra Damage with Advantage:** If the attack roll had advantage, the Goblin Warrior would deal an additional 1d6 slashing damage.
- **AC to Beat:** The attack must beat the target's Armor Class (AC). For a character wearing Chain Mail, the AC is 16.

So, to summarize:
- Attack Bonus: +6
- Damage on a Hit: 1d6 slashing
- Extra Damage with Advantage: +1d6 slashing
- AC to Beat: 16

*facts found (judge): 1/4; missing: +4; 5 (1d6 + 2); 2 (1d4)*


### v1_baseline  (3 chunks, 1 LLM call(s))

The goblin's attack bonus with Scimitar is +4. 

On a hit, the goblin deals 5 (1d6 + 2) slashing damage.

If the attack roll had Advantage, there is an extra 2 (1d4) slashing damage.

The attack must beat an AC of 17 (since Chain Mail provides an AC of 16 and the goblin adds +4 to its attack roll).

*facts found (judge): 4/4; missing: none*

*retrieved sections:* Monsters A–Z > Actions | Monsters A–Z > Reactions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Parry._** _Trigger:_ The warrior is hit by a melee attack roll while holding a weapon. _Response:_ The warrior adds 2 to its AC against that attack, possibly causing it to miss.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The goblin's attack bonus with its Scimitar is +4. On a hit, the damage is 5 (1d6 + 2) slashing damage. If the attack roll had Advantage, there is an extra 2 (1d4) slashing damage. The attack must beat the character's AC minus the goblin's attack bonus of +4.

*facts found (judge): 3/4; missing: 16 in Chain Mail*


*re-ranking* (query: `A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.06 | yes | Monsters A–Z > Actions |
| 2 | 10 | -2.23 | yes | Magic Items > Scimitar of Speed |
| 3 | 2 | -2.77 | yes | Monsters A–Z > Actions |
| 4 | 7 | -3.85 |  | Monsters A–Z > Actions |
| 5 | 5 | -4.80 |  | Monsters A–Z > Reactions |
| 6 | 4 | -5.55 |  | Magic Items > Dragon Scale Mail |
| 7 | 8 | -6.22 |  | Monsters A–Z > Reactions |
| 8 | 3 | -6.24 |  | Monsters A–Z > Reactions |
| 9 | 9 | -8.94 |  | Monsters A–Z > Reactions |
| 10 | 6 | -9.41 |  | Feats > Defense |

*retrieved sections:* Monsters A–Z > Actions | Magic Items > Scimitar of Speed

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Magic Items > Scimitar of Speed]
#### Scimitar of Speed  
_Weapon (Scimitar), Very Rare (Requires Attunement)_  
You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. In addition, you can make one attack with it as a Bonus Action on each of your turns.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The goblin's attack bonus with its Scimitar is +4. On a hit, it deals 5 (1d6 + 2) slashing damage. If the attack roll had Advantage, there would be an additional 2 (1d4) slashing damage. The attack must beat an AC of 15 (assuming the character is wearing Chain Mail, which provides an AC of 16 without any other modifiers).

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.06 | yes | Monsters A–Z > Actions |
| 2 | 10 | -2.23 | yes | Magic Items > Scimitar of Speed |
| 3 | 2 | -2.77 | yes | Monsters A–Z > Actions |
| 4 | 7 | -3.85 | yes | Monsters A–Z > Actions |
| 5 | 5 | -4.80 | yes | Monsters A–Z > Reactions |
| 6 | 4 | -5.55 | yes | Magic Items > Dragon Scale Mail |
| 7 | 8 | -6.22 | yes | Monsters A–Z > Reactions |
| 8 | 3 | -6.24 | yes | Monsters A–Z > Reactions |
| 9 | 9 | -8.94 |  | Monsters A–Z > Reactions |
| 10 | 6 | -9.41 |  | Feats > Defense |

*retrieved sections:* Monsters A–Z > Actions | Magic Items > Scimitar of Speed | Monsters A–Z > Reactions | Magic Items > Dragon Scale Mail

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Magic Items > Scimitar of Speed]
#### Scimitar of Speed  
_Weapon (Scimitar), Very Rare (Requires Attunement)_  
You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. In addition, you can make one attack with it as a Bonus Action on each of your turns.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 4 (1d6 + 1) Slashing damage.  
**_Light Crossbow._** _Ranged Attack Roll:_ +3, range 80/320 ft. _Hit:_ 5 (1d8 + 1) Piercing damage.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Redirect Attack._** _Trigger:_ A creature the goblin can see makes an attack roll against it. _Response:_ The goblin chooses a Small or Medium ally within 5 feet of itself. The goblin and that ally swap places, and the ally becomes the target of the attack instead.

---

[Magic Items > Dragon Scale Mail]
While wearing this armor, you gain a +1 bonus to Armor Class, you have Advantage on saving throws against the breath weapons of Dragons, and you have Resistance to one damage type determined by the kind of dragon that provided the scales (see the accompanying table).

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protection._** _Trigger:_ An attack roll hits the wearer of the guardian's amulet while the wearer is within 5 feet of the guardian. _Response:_ The wearer gains a +5 bonus to AC, including against the triggering attack and possibly causing it to miss, until the start of the guardian's next turn.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Parry._** _Trigger:_ The warrior is hit by a melee attack roll while holding a weapon. _Response:_ The warrior adds 2 to its AC against that attack, possibly causing it to miss.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

Attack Bonus: +4  
Damage on a Hit: 5 (1d6 + 2) Slashing damage  
Extra Damage with Advantage: 2 (1d4) Slashing damage  
AC to Beat: Not specified in the given context.

*facts found (judge): 3/4; missing: 16 in Chain Mail*


*re-ranking* (query: `A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.06 | yes | Monsters A–Z > Actions |
| 2 | 2 | -2.77 | yes | Monsters A–Z > Actions |
| 3 | 6 | -3.85 | yes | Monsters A–Z > Actions |
| 4 | 4 | -4.80 |  | Monsters A–Z > Reactions |
| 5 | 7 | -6.22 |  | Monsters A–Z > Reactions |
| 6 | 3 | -6.24 |  | Monsters A–Z > Reactions |
| 7 | 9 | -7.59 |  | Monsters A–Z > Actions |
| 8 | 10 | -8.14 |  | Monsters A–Z > Actions |
| 9 | 8 | -8.94 |  | Monsters A–Z > Reactions |
| 10 | 5 | -9.41 |  | Feats > Defense |

*retrieved sections:* Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 4 (1d6 + 1) Slashing damage.  
**_Light Crossbow._** _Ranged Attack Roll:_ +3, range 80/320 ft. _Hit:_ 5 (1d8 + 1) Piercing damage.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The goblin's attack bonus with Scimitar is +4. 

On a hit, the damage is 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.

The goblin's AC is not provided in the given context, so that part is missing.

The attack must beat an AC of 11 (since the goblin has a +4 attack bonus and the character is wearing Chain Mail, which has an AC of 11).

*facts found (judge): 3/4; missing: 16 in Chain Mail*


*re-ranking* (query: `A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.06 | yes | Monsters A–Z > Actions |
| 2 | 2 | -2.77 | yes | Monsters A–Z > Actions |
| 3 | 4 | -3.36 | yes | Monsters A–Z > Actions |
| 4 | 16 | -3.44 | yes | Magic Items > Sword of Sharpness |
| 5 | 21 | -3.57 | yes | Magic Items > Sword of Life Stealing |
| 6 | 13 | -3.85 | yes | Monsters A–Z > Actions |
| 7 | 30 | -3.91 | yes | Magic Items > Elven Chain |
| 8 | 23 | -4.76 | yes | Magic Items > Mace of Smiting |
| 9 | 10 | -4.80 |  | Monsters A–Z > Reactions |
| 10 | 5 | -4.98 |  | Monsters > Attack Notation |
| 11 | 15 | -6.22 |  | Monsters A–Z > Reactions |
| 12 | 3 | -6.24 |  | Monsters A–Z > Reactions |
| 13 | 28 | -6.52 |  | Rules Glossary > Stat Block |
| 14 | 11 | -6.55 |  | Classes > Level 1: Sneak Attack |
| 15 | 9 | -6.60 |  | Monsters A–Z > Actions |
| 16 | 19 | -7.07 |  | Classes > Level 3: Frenzy |
| 17 | 8 | -7.24 |  | Monsters A–Z > Traits |
| 18 | 14 | -7.29 |  | Monsters A–Z > Actions |
| 19 | 22 | -7.32 |  | Monsters A–Z > Actions |
| 20 | 7 | -7.52 |  | Monsters A–Z > Actions |

*retrieved sections:* Monsters A–Z > Actions | Magic Items > Sword of Sharpness | Magic Items > Sword of Life Stealing | Magic Items > Elven Chain | Magic Items > Mace of Smiting

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The bandit makes two attacks, using Scimitar and Pistol in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 6 (1d6 + 3) Slashing damage.  
**_Pistol._** _Ranged Attack Roll:_ +5, range 30/90 ft. _Hit:_ 8 (1d10 + 3) Piercing damage.

---

[Magic Items > Sword of Sharpness]
#### Sword of Sharpness  
_Weapon (Glaive, Greatsword, Longsword, or Scimitar), Very Rare (Requires Attunement)_  
When you attack an object with this magic weapon and hit, maximize your weapon damage dice against the target.  
When you attack a creature with this weapon and roll a 20 on the d20 for the attack roll, that target takes an extra 14 Slashing damage and gains 1 Exhaustion level.

---

[Magic Items > Sword of Life Stealing]
#### Sword of Life Stealing  
_Weapon (Glaive, Greatsword, Longsword, Rapier, Scimitar, or Shortsword), Rare (Requires Attunement)_  
When you attack a creature with this magic weapon and roll a 20 on the d20 for the attack roll, that target takes an extra 15 Necrotic damage if it isn't a Construct or an Undead, and you gain Temporary Hit Points equal to the amount of Necrotic damage taken.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 4 (1d6 + 1) Slashing damage.  
**_Light Crossbow._** _Ranged Attack Roll:_ +3, range 80/320 ft. _Hit:_ 5 (1d8 + 1) Piercing damage.

---

[Magic Items > Elven Chain]
#### Elven Chain  
_Armor (Chain Mail or Chain Shirt), Rare_  
You gain a +1 bonus to Armor Class while you wear this armor. You are considered trained with this armor even if you lack training with Medium or Heavy armor.

---

[Magic Items > Mace of Smiting]
#### Mace of Smiting  
_Weapon (Mace), Rare_  
You gain a +1 bonus to attack rolls and damage rolls made with this magic weapon. The bonus increases to +3 when you use the weapon to attack a Construct.  
When you roll a 20 on an attack roll made with this weapon, the target takes an extra 7 Bludgeoning damage, or 14 Bludgeoning damage if it's a Construct. If a Construct has 25 Hit Points or fewer after taking this damage, it is destroyed.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The goblin warrior's attack bonus with its Scimitar is +4. 

On a hit, the damage is 5 (1d6 + 2) Slashing damage. If the attack roll had Advantage, there would be an additional 2 (1d4) Slashing damage.

The attack must beat the target's AC, which includes their armor bonus. Since the character is wearing Chain Mail, their AC is 16 (10 + 6 from Chain Mail). So, the goblin warrior's Scimitar attack must beat an AC of 16.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What `): candidate pool of 16, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.06 | yes | Monsters A–Z > Actions |
| 2 | 2 | -2.77 | yes | Monsters A–Z > Actions |
| 3 | 4 | -3.36 | yes | Monsters A–Z > Actions |
| 4 | 11 | -4.06 | yes | Monsters A–Z > Goblin Warrior |
| 5 | 12 | -4.10 | yes | Monsters A–Z > Goblin Warrior |
| 6 | 13 | -4.77 | yes | Monsters A–Z > Goblin Warrior |
| 7 | 10 | -4.80 | yes | Monsters A–Z > Reactions |
| 8 | 5 | -4.98 | yes | Monsters > Attack Notation |
| 9 | 3 | -6.24 |  | Monsters A–Z > Reactions |
| 10 | 9 | -6.60 |  | Monsters A–Z > Actions |
| 11 | 8 | -7.24 |  | Monsters A–Z > Traits |
| 12 | 7 | -7.52 |  | Monsters A–Z > Actions |
| 13 | 6 | -7.65 |  | Equipment > Armor |
| 14 | 14 | -10.19 |  | Monsters A–Z > Bandit |
| 15 | 15 | -10.50 |  | Monsters A–Z > Bandit |
| 16 | 16 | -10.53 |  | Rules Glossary > Monster |

*retrieved sections:* Monsters A–Z > Actions | Monsters A–Z > Goblin Warrior | Monsters A–Z > Reactions | Monsters > Attack Notation

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The bandit makes two attacks, using Scimitar and Pistol in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 6 (1d6 + 3) Slashing damage.  
**_Pistol._** _Ranged Attack Roll:_ +5, range 30/90 ft. _Hit:_ 8 (1d10 + 3) Piercing damage.

---

[Monsters A–Z > Goblin Warrior]
<td>+2</td>
<td><strong>CON</strong></td>
<td>10</td>
<td>+0</td>
<td>+0</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>10</td>
<td>+0</td>
<td>+0</td>
<td><strong>WIS</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
<td><strong>CHA</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
</tr>
</tbody>
</table>  
**Skills** Stealth +6<br>
**Gear** Leather Armor, Scimitar, Shield, Shortbow<br>
**Senses** Darkvision 60 ft.; Passive Perception 9<br>
**Languages** Common, Goblin<br>

---

[Monsters A–Z > Goblin Warrior]
**Languages** Common, Goblin<br>
**CR** 1/4 (XP 50; PB +2)

---

[Monsters A–Z > Goblin Warrior]
### Goblin Warrior  
_Small Fey (Goblinoid), Chaotic Neutral_  
**AC** 17 **Initiative** +2 (12) <br>
**HP** 10 (3d6) <br>
**Speed** 30 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Redirect Attack._** _Trigger:_ A creature the goblin can see makes an attack roll against it. _Response:_ The goblin chooses a Small or Medium ally within 5 feet of itself. The goblin and that ally swap places, and the ally becomes the target of the attack instead.

---

[Monsters > Attack Notation]
#### Attack Notation  
The entry for a monster's attack identifies whether the attack is a melee or a ranged attack and then provides the attack roll's bonus, its reach or range, and what happens on a hit. An attack is against one target unless its entry says otherwise. For details on different kinds of attacks, see "Playing the Game" and "Spells."  
**_Hit._** Any damage dealt or other effects that occur as a result of an attack hitting a target are described after the "Hit:" notation.
```
</details>


### v6_agentic  (16 chunks, 3 LLM call(s))

The goblin warrior's attack bonus with its Scimitar is +5 (Dexterity modifier + Proficiency Bonus).

On a hit, the goblin warrior deals 6 (1d6 + 3) Slashing damage.

If the attack roll had Advantage, the goblin would deal an additional 2d6 + 3 Slashing damage (since the Sword of Sharpness maximizes the damage dice).

The attack must beat the character's Armor Class (AC) while wearing Chain Mail, which is 16 (11 + Dexterity modifier + Chain Mail bonus of +5).

The extra damage from Advantage is 2d6 + 3.

*facts found (judge): 1/4; missing: +4; 5 (1d6 + 2); 2 (1d4)*

*agentic sub-queries:* Scimitar / Chain Mail / Goblin / Attack Bonus / Damage on Hit / Advantage


*re-ranking* (query: `Scimitar`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.02 | yes | Magic Items > Scimitar of Speed |
| 2 | 3 | 2.00 | yes | Monsters A–Z > Actions |
| 3 | 17 | 1.59 | yes | Magic Items > Sword of Sharpness |
| 4 | 9 | 1.43 |  | Magic Items > Vorpal Sword |
| 5 | 7 | 1.41 |  | Monsters A–Z > Actions |
| 6 | 13 | 1.27 |  | Monsters A–Z > Actions |
| 7 | 5 | 1.25 |  | Monsters A–Z > Actions |
| 8 | 19 | 1.00 |  | Magic Items > Frost Brand |
| 9 | 2 | 0.96 |  | Magic Items > Dancing Sword |
| 10 | 11 | 0.23 |  | Magic Items > Luck Blade |
| 11 | 15 | -0.93 |  | Classes > Ranger |
| 12 | 4 | -7.56 |  | Monsters A–Z > Planetar |
| 13 | 8 | -8.80 |  | Monsters A–Z > Werebear |
| 14 | 6 | -9.43 |  | Magic Items > Robe of Scintillating Colors |
| 15 | 18 | -10.28 |  | Animals > Giant Vulture |
| 16 | 14 | -10.57 |  | Animals > Giant Constrictor Snake |
| 17 | 10 | -10.62 |  | Animals > Triceratops |
| 18 | 16 | -10.67 |  | Animals > Killer Whale |
| 19 | 12 | -10.70 |  | Monsters A–Z > Dryad |
| 20 | 20 | -10.79 |  | Animals > Plesiosaurus |


*re-ranking* (query: `Chain Mail`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.42 | yes | Magic Items > Elven Chain |
| 2 | 19 | -0.42 | yes | Equipment > Armor |
| 3 | 15 | -0.54 | yes | Classes > Paladin |
| 4 | 7 | -0.94 |  | Magic Items > Armor |
| 5 | 3 | -2.07 |  | Equipment > Armor |
| 6 | 17 | -2.58 |  | Classes > Fighter |
| 7 | 8 | -3.34 |  | Equipment > Armor |
| 8 | 4 | -3.41 |  | Equipment > Chain (5 GP) |
| 9 | 5 | -5.59 |  | Equipment > Chain (5 GP) |
| 10 | 10 | -6.77 |  | Equipment > Chain (5 GP) |
| 11 | 13 | -6.90 |  | Spells > Chain Lightning |
| 12 | 12 | -7.78 |  | Classes > Investment of the Chain Master |
| 13 | 2 | -7.84 |  | Magic Items > Dragon Scale Mail |
| 14 | 9 | -8.63 |  | Magic Items > Dragon Scale Mail |
| 15 | 14 | -8.96 |  | Equipment > Hunting Trap (5 GP) |
| 16 | 11 | -9.27 |  | Magic Items > Dragon Scale Mail |
| 17 | 6 | -10.15 |  | Magic Items > Dragon Scale Mail |
| 18 | 16 | -11.07 |  | Spells > Sending |
| 19 | 18 | -11.07 |  | Spells > Sending |
| 20 | 20 | -11.34 |  | Spells > Animal Messenger |


*re-ranking* (query: `Goblin`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 11 | 2.53 | yes | Monsters A–Z > Reactions |
| 2 | 1 | 2.39 | yes | Monsters A–Z > Goblin Warrior |
| 3 | 3 | 2.20 | yes | Monsters A–Z > Goblin Minion |
| 4 | 2 | 1.57 |  | Monsters A–Z > Bonus Actions |
| 5 | 8 | 1.54 |  | Monsters A–Z > Actions |
| 6 | 4 | 1.14 |  | Monsters A–Z > Bugbear Warrior |
| 7 | 7 | 1.11 |  | Monsters A–Z > Bugbear Stalker |
| 8 | 6 | 0.90 |  | Monsters A–Z > Hobgoblin Captain |
| 9 | 5 | 0.06 |  | Monsters A–Z > Goblin Boss |
| 10 | 9 | -0.39 |  | Monsters A–Z > Goblin Minion |
| 11 | 20 | -0.57 |  | Character Creation > Trinkets |
| 12 | 16 | -1.76 |  | Monsters A–Z > Bugbear Warrior |
| 13 | 14 | -1.78 |  | Monsters A–Z > Bugbear Stalker |
| 14 | 12 | -1.82 |  | Monsters A–Z > Hobgoblin Warrior |
| 15 | 15 | -2.59 |  | Character Creation > Trinkets |
| 16 | 17 | -2.71 |  | Monsters A–Z > Hobgoblin Captain |
| 17 | 13 | -4.44 |  | Character Creation > Choose Languages |
| 18 | 18 | -7.26 |  | Character Origins > Gnome |
| 19 | 10 | -9.33 |  | Monsters A–Z > Worg |
| 20 | 19 | -10.04 |  | Monsters A–Z > Bonus Actions |


*re-ranking* (query: `Attack Bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 13 | 7.66 | yes | Character Creation > Fill In Numbers |
| 2 | 14 | 6.28 | yes | Magic Items > Iron Bands |
| 3 | 1 | 5.90 | yes | Playing the Game > Proficiency Bonus |
| 4 | 3 | 5.64 |  | Equipment > Properties |
| 5 | 19 | 5.52 |  | Character Creation > Fill In Numbers |
| 6 | 2 | 5.43 |  | Classes > Level 13: Improved Brutal Strike |
| 7 | 16 | 4.60 |  | Magic Items > Arrow-Catching Shield |
| 8 | 9 | 4.29 |  | Monsters > Attack Notation |
| 9 | 5 | 4.07 |  | Rules Glossary > Stat Block |
| 10 | 10 | 3.71 |  | Rules Glossary > Opportunity Attacks |
| 11 | 11 | 3.56 |  | Monsters A–Z > Reactions |
| 12 | 7 | 3.52 |  | Playing the Game > Making an Attack |
| 13 | 6 | 3.35 |  | Monsters A–Z > Bonus Actions |
| 14 | 4 | 3.27 |  | Feats > Archery |
| 15 | 8 | 3.16 |  | Monsters A–Z > Bonus Actions |
| 16 | 18 | -2.12 |  | Equipment > Properties |
| 17 | 12 | -2.38 |  | Feats > Defense |
| 18 | 15 | -3.03 |  | Classes > Level 5: Extra Attack |
| 19 | 17 | -3.39 |  | Classes > Level 20: Three Extra Attacks |
| 20 | 20 | -4.00 |  | Classes > Level 11: Two Extra Attacks |


*re-ranking* (query: `Damage on Hit`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 5.32 | yes | Rules Glossary > Damage |
| 2 | 1 | 4.36 | yes | Rules Glossary > Unarmed Strike |
| 3 | 6 | 4.18 | yes | Playing the Game > Making an Attack |
| 4 | 19 | 4.10 |  | Monsters > Damage Notation |
| 5 | 15 | 3.96 |  | Spells > Ice Knife |
| 6 | 5 | 3.86 |  | Rules Glossary > Hit Points |
| 7 | 2 | 3.72 |  | Playing the Game > Instant Death |
| 8 | 13 | 2.49 |  | Rules Glossary > Critical Hit |
| 9 | 3 | 2.33 |  | Playing the Game > Hit Points |
| 10 | 7 | 2.15 |  | Playing the Game > Lose Temporary Hit Points First |
| 11 | 12 | 1.62 |  | Spells > Harm |
| 12 | 9 | 1.23 |  | Playing the Game > Death Saving Throws |
| 13 | 20 | 0.66 |  | Magic Items > Mace of Disruption |
| 14 | 8 | 0.38 |  | Rules Glossary > Temporary Hit Points |
| 15 | 11 | 0.24 |  | Monsters A–Z > Traits |
| 16 | 18 | -2.01 |  | Playing the Game > Damage against Multiple Targets |
| 17 | 14 | -2.01 |  | Rules Glossary > Damage Roll |
| 18 | 10 | -3.02 |  | Rules Glossary > Damage Threshold |
| 19 | 17 | -3.77 |  | Spells > Shatter |
| 20 | 16 | -6.54 |  | Rules Glossary > Damage Threshold |


*re-ranking* (query: `Advantage`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 4.91 | yes | Playing the Game > Advantage/Disadvantage |
| 2 | 1 | 4.08 |  | Rules Glossary > Advantage |
| 3 | 4 | 0.71 |  | Feats > Grappler |
| 4 | 3 | -0.28 |  | Playing the Game > They Don't Stack |
| 5 | 7 | -0.77 |  | Rules Glossary > Friendly [Attitude] |
| 6 | 17 | -1.17 |  | Rules Glossary > Invisible [Condition] |
| 7 | 6 | -1.45 |  | Playing the Game > Roll Two D20s |
| 8 | 16 | -2.08 |  | Rules Glossary > Prone [Condition] |
| 9 | 10 | -2.22 |  | Monsters A–Z > Traits |
| 10 | 9 | -2.36 |  | Monsters A–Z > Traits |
| 11 | 19 | -2.47 |  | Monsters A–Z > Traits |
| 12 | 11 | -2.58 |  | Monsters A–Z > Traits |
| 13 | 15 | -2.69 |  | Monsters A–Z > Traits |
| 14 | 14 | -2.74 |  | Monsters A–Z > Traits |
| 15 | 8 | -2.78 |  | Monsters A–Z > Traits |
| 16 | 18 | -2.90 |  | Magic Items > Cloak of Elvenkind |
| 17 | 13 | -2.91 |  | Monsters A–Z > Traits |
| 18 | 20 | -3.36 |  | Magic Items > Sentinel Shield |
| 19 | 12 | -3.83 |  | Magic Items > Spellguard Shield |
| 20 | 5 | -3.93 |  | Rules Glossary > Charmed [Condition] |

*retrieved sections:* Magic Items > Scimitar of Speed | Monsters A–Z > Actions | Magic Items > Sword of Sharpness | Magic Items > Elven Chain | Equipment > Armor | Classes > Paladin | Monsters A–Z > Reactions | Monsters A–Z > Goblin Warrior | Monsters A–Z > Goblin Minion | Character Creation > Fill In Numbers | Magic Items > Iron Bands | Playing the Game > Proficiency Bonus | Rules Glossary > Damage | Rules Glossary > Unarmed Strike | Playing the Game > Making an Attack | Playing the Game > Advantage/Disadvantage

<details><summary>full retrieved context</summary>

```
[Magic Items > Scimitar of Speed]
#### Scimitar of Speed  
_Weapon (Scimitar), Very Rare (Requires Attunement)_  
You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. In addition, you can make one attack with it as a Bonus Action on each of your turns.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The bandit makes two attacks, using Scimitar and Pistol in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 6 (1d6 + 3) Slashing damage.  
**_Pistol._** _Ranged Attack Roll:_ +5, range 30/90 ft. _Hit:_ 8 (1d10 + 3) Piercing damage.

---

[Magic Items > Sword of Sharpness]
#### Sword of Sharpness  
_Weapon (Glaive, Greatsword, Longsword, or Scimitar), Very Rare (Requires Attunement)_  
When you attack an object with this magic weapon and hit, maximize your weapon damage dice against the target.  
When you attack a creature with this weapon and roll a 20 on the d20 for the attack roll, that target takes an extra 14 Slashing damage and gains 1 Exhaustion level.

---

[Magic Items > Elven Chain]
#### Elven Chain  
_Armor (Chain Mail or Chain Shirt), Rare_  
You gain a +1 bonus to Armor Class while you wear this armor. You are considered trained with this armor even if you lack training with Medium or Heavy armor.

---

[Equipment > Armor]
**Armor Class (AC).** The table's Armor Class column tells you what your base AC is when you wear a type of armor. For example, if you wear Leather Armor, your base AC is 11 plus your Dexterity modifier, whereas your AC is 16 in Chain Mail.  
**Strength.** If the table shows a Strength score in the Strength column for an armor type, that armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the listed score.

---

[Classes > Paladin]
</tr>
<tr>
<td>Armor Training</td>
<td>Light, Medium, and Heavy armor and Shields</td>
</tr>
<tr>
<td>Starting Equipment</td>
<td>Choose A or B: (A) Chain Mail, Shield, Longsword, 6 Javelins, Holy Symbol, Priest's Pack, and 9 GP; or (B) 150 GP</td>
</tr>
</tbody>
</table>

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Redirect Attack._** _Trigger:_ A creature the goblin can see makes an attack roll against it. _Response:_ The goblin chooses a Small or Medium ally within 5 feet of itself. The goblin and that ally swap places, and the ally becomes the target of the attack instead.

---

[Monsters A–Z > Goblin Warrior]
**Languages** Common, Goblin<br>
**CR** 1/4 (XP 50; PB +2)

---

[Monsters A–Z > Goblin Minion]
## Goblins  
### Goblin Minion  
_Small Fey (Goblinoid), Chaotic Neutral_  
**AC** 12 **Initiative** +2 (12) <br>
**HP** 7 (2d6) <br>
**Speed** 30 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>

---

[Character Creation > Fill In Numbers]
_Attacks_. In the Weapons & Damage Cantrips section of the character sheet, write your starting weapons. The attack roll bonus for a weapon with which you have proficiency is one of the following unless a weapon's property says otherwise:  
Melee attack bonus = Strength modifier + Proficiency Bonus
Ranged attack bonus = Dexterity modifier + Proficiency Bonus

---

[Magic Items > Iron Bands]
Make a ranged attack roll with an attack bonus equal to your Dexterity modifier plus your Proficiency Bonus. On a hit, the target has the Restrained condition until you take a Bonus Action to issue a command that releases it. Doing so or missing with the attack causes the bands to contract and become a sphere once more.

---

[Playing the Game > Proficiency Bonus]
#### Proficiency Bonus  
You add your Proficiency Bonus to your attack roll when you attack using a weapon you have proficiency with, as well as when you attack with a spell. See "Proficiency" later in "Playing the Game" for more information about weapon proficiencies.

---

[Rules Glossary > Damage]
#### Damage  
Damage represents harm that causes a creature or an object to lose Hit Points.

---

[Rules Glossary > Unarmed Strike]
_Damage._ You make an attack roll against the target. Your bonus to the roll equals your Strength modifier plus your Proficiency Bonus. On a hit, the target takes Bludgeoning damage equal to 1 plus your Strength modifier.

---

[Playing the Game > Making an Attack]
**3: Resolve the Attack.** Make the attack roll, as detailed earlier in "Playing the Game." On a hit, you roll damage unless the particular attack has rules that specify otherwise. Some attacks cause special effects in addition to or instead of damage.  
> **Unseen Attackers and Targets**
>

---

[Playing the Game > Advantage/Disadvantage]
### Advantage/Disadvantage  
Sometimes a D20 Test is modified by Advantage or Disadvantage. Advantage reflects the positive circumstances surrounding a d20 roll, while Disadvantage reflects negative circumstances.  
You usually acquire Advantage or Disadvantage through the use of special abilities and actions. The GM can also decide that circumstances grant Advantage or impose Disadvantage.
```
</details>


---

## q18 (reasoning) A wizard casts Fireball using a 5th-level spell slot. How much damage dice does it deal in total, and what saving throw do targets make?

**Gold facts (counterfactual data):** Dexterity; 11d6


### v0_closed_book  (0 chunks, 1 LLM call(s))

When a wizard casts Fireball using a 5th-level spell slot, it deals 8d6 fire damage in total. Targets make a Dexterity saving throw to avoid taking damage.

*facts found (judge): 1/2; missing: 11d6*


### v1_baseline  (3 chunks, 1 LLM call(s))

A wizard casting Fireball using a 5th-level spell slot deals a total of 13d6 Fire damage. Targets make a Dexterity saving throw.

*facts found (judge): 1/2; missing: 11d6*

*retrieved sections:* Spells > Fireball | Spells > Delayed Blast Fireball

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
When the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The base damage increases by 1d6 for each spell slot level above 7.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The Fireball spell deals 9d6 Fire damage to each creature in its area. When cast using a 5th-level spell slot, the damage is increased by 3d6. Therefore, the total damage dice dealt is 12d6. Targets make a Dexterity saving throw to resist the damage.

*facts found (judge): 1/2; missing: 11d6*


*re-ranking* (query: `A wizard casts Fireball using a 5th-level spell slot. How much damage dice does `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 8 | 2.98 | yes | Spells > Wall of Fire |
| 2 | 2 | 2.40 | yes | Spells > Fireball |
| 3 | 4 | 1.97 | yes | Playing the Game > Damage against Multiple Targets |
| 4 | 7 | 1.82 |  | Spells > Flame Strike |
| 5 | 3 | 0.85 |  | Spells > Delayed Blast Fireball |
| 6 | 5 | 0.79 |  | Spells > Wall of Fire |
| 7 | 1 | 0.64 |  | Spells > Fireball |
| 8 | 9 | -1.03 |  | Spells > Circle of Death |
| 9 | 6 | -1.14 |  | Spells > Burning Hands |
| 10 | 10 | -6.10 |  | Classes > As a Multiclass Character |

*retrieved sections:* Spells > Wall of Fire | Spells > Fireball | Playing the Game > Damage against Multiple Targets

<details><summary>full retrieved context</summary>

```
[Spells > Wall of Fire]
When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.  
One side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Playing the Game > Damage against Multiple Targets]
#### Damage against Multiple Targets  
When you create a damaging effect that forces two or more targets to make saving throws against it at the same time, roll the damage once for all the targets. For example, when a wizard casts _Fireball_, the spell's damage is rolled once for all creatures caught in the blast.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

A wizard casting Fireball using a 5th-level spell slot deals 14d6 Fire damage in total (9d6 base + 5d6 from the higher-level slot) and targets make a Dexterity saving throw.

*facts found (judge): 1/2; missing: 11d6*


*re-ranking* (query: `A wizard casts Fireball using a 5th-level spell slot. How much damage dice does `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 8 | 2.98 | yes | Spells > Wall of Fire |
| 2 | 2 | 2.40 | yes | Spells > Fireball |
| 3 | 4 | 1.97 | yes | Playing the Game > Damage against Multiple Targets |
| 4 | 7 | 1.82 | yes | Spells > Flame Strike |
| 5 | 3 | 0.85 | yes | Spells > Delayed Blast Fireball |
| 6 | 5 | 0.79 | yes | Spells > Wall of Fire |
| 7 | 1 | 0.64 | yes | Spells > Fireball |
| 8 | 9 | -1.03 | yes | Spells > Circle of Death |
| 9 | 6 | -1.14 |  | Spells > Burning Hands |
| 10 | 10 | -6.10 |  | Classes > As a Multiclass Character |

*retrieved sections:* Spells > Wall of Fire | Spells > Fireball | Playing the Game > Damage against Multiple Targets | Spells > Flame Strike | Spells > Delayed Blast Fireball | Spells > Circle of Death

<details><summary>full retrieved context</summary>

```
[Spells > Wall of Fire]
When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.  
One side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Playing the Game > Damage against Multiple Targets]
#### Damage against Multiple Targets  
When you create a damaging effect that forces two or more targets to make saving throws against it at the same time, roll the damage once for all the targets. For example, when a wizard casts _Fireball_, the spell's damage is rolled once for all creatures caught in the blast.

---

[Spells > Flame Strike]
_Using a Higher-Level Spell Slot._ The Fire damage and the Radiant damage increase by 1d6 for each spell slot level above 5.

---

[Spells > Delayed Blast Fireball]
When the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The base damage increases by 1d6 for each spell slot level above 7.

---

[Spells > Wall of Fire]
_Using a Higher-Level Spell Slot._ The damage increases by 1d8 for each spell slot level above 4.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Spells > Circle of Death]
_Using a Higher-Level Spell Slot._ The damage increases by 2d8 for each spell slot level above 6.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

A Fireball cast using a 5th-level spell slot deals 14d6 Fire damage in total (9d6 base + 5d6 from the higher-level slot). Targets make a Dexterity saving throw.

*facts found (judge): 1/2; missing: 11d6*


*re-ranking* (query: `A wizard casts Fireball using a 5th-level spell slot. How much damage dice does `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 8 | 2.98 | yes | Spells > Wall of Fire |
| 2 | 2 | 2.40 | yes | Spells > Fireball |
| 3 | 10 | 2.12 | yes | Spells > Cloudkill |
| 4 | 4 | 1.97 |  | Playing the Game > Damage against Multiple Targets |
| 5 | 7 | 1.82 |  | Spells > Flame Strike |
| 6 | 3 | 0.85 |  | Spells > Delayed Blast Fireball |
| 7 | 5 | 0.79 |  | Spells > Wall of Fire |
| 8 | 1 | 0.64 |  | Spells > Fireball |
| 9 | 9 | -1.03 |  | Spells > Circle of Death |
| 10 | 6 | -1.14 |  | Spells > Burning Hands |

*retrieved sections:* Spells > Wall of Fire | Spells > Fireball | Spells > Cloudkill

<details><summary>full retrieved context</summary>

```
[Spells > Wall of Fire]
When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.  
One side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Cloudkill]
Each creature in the Sphere makes a Constitution saving throw, taking 5d8 Poison damage on a failed save or half as much damage on a successful one. A creature must also make this save when the Sphere moves into its space and when it enters the Sphere or ends its turn there. A creature makes this save only once per turn.  
The Sphere moves 10 feet away from you at the start of each of your turns.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d8 for each spell slot level above 5.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

A wizard casting Fireball using a 5th-level spell slot deals a total of 15d6 Fire damage in total (9d6 base damage + 6d6 from the higher-level slot). Targets make a Dexterity saving throw.

*facts found (judge): 1/2; missing: 11d6*


*re-ranking* (query: `A wizard casts Fireball using a 5th-level spell slot. How much damage dice does `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 10 | 3.82 | yes | Classes > Level 14: Overchannel |
| 2 | 6 | 3.28 | yes | Spells > Chain Lightning |
| 3 | 11 | 3.06 | yes | Spells > Searing Smite |
| 4 | 19 | 2.98 | yes | Spells > Wall of Fire |
| 5 | 26 | 2.58 | yes | Spells > Wall of Ice |
| 6 | 5 | 2.40 | yes | Spells > Fireball |
| 7 | 4 | 2.12 | yes | Spells > Cloudkill |
| 8 | 2 | 1.97 | yes | Playing the Game > Damage against Multiple Targets |
| 9 | 25 | 1.86 |  | Spells > Flame Strike |
| 10 | 9 | 1.82 |  | Spells > Flame Strike |
| 11 | 20 | 1.74 |  | Spells > Conjure Woodland Beings |
| 12 | 22 | 1.45 |  | Spells > Insect Plague |
| 13 | 30 | 0.99 |  | Spells > Conjure Animals |
| 14 | 28 | 0.92 |  | Spells > Ice Knife |
| 15 | 3 | 0.85 |  | Spells > Delayed Blast Fireball |
| 16 | 14 | 0.79 |  | Spells > Flame Blade |
| 17 | 15 | 0.79 |  | Spells > Wall of Fire |
| 18 | 23 | 0.68 |  | Spells > Inflict Wounds |
| 19 | 1 | 0.64 |  | Spells > Fireball |
| 20 | 7 | -0.09 |  | Spells > Delayed Blast Fireball |

*retrieved sections:* Classes > Level 14: Overchannel | Spells > Chain Lightning | Spells > Searing Smite | Spells > Wall of Fire | Spells > Wall of Ice | Spells > Fireball | Spells > Cloudkill | Playing the Game > Damage against Multiple Targets

<details><summary>full retrieved context</summary>

```
[Classes > Level 14: Overchannel]
#### Level 14: Overchannel  
You can increase the power of your spells. When you cast a Wizard spell with a spell slot of levels 1–5 that deals damage, you can deal maximum damage with that spell on the turn you cast it.  
The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a Long Rest, you take 2d12 Necrotic damage for each level of the spell slot immediately after you cast it. This damage ignores Resistance and Immunity.

---

[Spells > Chain Lightning]
Each target makes a Dexterity saving throw, taking 10d8 Lightning damage on a failed save or half as much damage on a successful one.  
_Using a Higher-Level Spell Slot._ One additional bolt leaps from the first target to another target for each spell slot level above 6.

---

[Spells > Searing Smite]
**Component:** V
**Duration:** 1 minute  
As you hit the target, it takes an extra 1d6 Fire damage from the attack. At the start of each of its turns until the spell ends, the target takes 1d6 Fire damage and then makes a Constitution saving throw. On a failed save, the spell continues. On a successful save, the spell ends.  
_Using a Higher-Level Spell Slot._ All the damage increases by 1d6 for each spell slot level above 1.

---

[Spells > Wall of Fire]
When the wall appears, each creature in its area makes a Dexterity saving throw, taking 5d8 Fire damage on a failed save or half as much damage on a successful one.  
One side of the wall, selected by you when you cast this spell, deals 5d8 Fire damage to each creature that ends its turn within 10 feet of that side or inside the wall. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there. The other side of the wall deals no damage.

---

[Spells > Wall of Ice]
A creature moving through the sheet of frigid air for the first time on a turn makes a Constitution saving throw, taking 5d6 Cold damage on a failed save or half as much damage on a successful one.
_Using a Higher-Level Spell Slot._ The damage the wall deals when it appears increases by 2d6 and the damage from passing through the sheet of frigid air increases by 1d6 for each spell slot level above 6.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Cloudkill]
Each creature in the Sphere makes a Constitution saving throw, taking 5d8 Poison damage on a failed save or half as much damage on a successful one. A creature must also make this save when the Sphere moves into its space and when it enters the Sphere or ends its turn there. A creature makes this save only once per turn.  
The Sphere moves 10 feet away from you at the start of each of your turns.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d8 for each spell slot level above 5.

---

[Playing the Game > Damage against Multiple Targets]
#### Damage against Multiple Targets  
When you create a damaging effect that forces two or more targets to make saving throws against it at the same time, roll the damage once for all the targets. For example, when a wizard casts _Fireball_, the spell's damage is rolled once for all creatures caught in the blast.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

A wizard casting Fireball using a 5th-level spell slot deals a total of 15d6 Fire damage. Targets make a Dexterity saving throw.

*facts found (judge): 1/2; missing: 11d6*


*re-ranking* (query: `A wizard casts Fireball using a 5th-level spell slot. How much damage dice does `): candidate pool of 17, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 10 | 3.82 | yes | Classes > Level 14: Overchannel |
| 2 | 6 | 3.28 | yes | Spells > Chain Lightning |
| 3 | 5 | 2.40 | yes | Spells > Fireball |
| 4 | 4 | 2.12 | yes | Spells > Cloudkill |
| 5 | 2 | 1.97 | yes | Playing the Game > Damage against Multiple Targets |
| 6 | 9 | 1.82 | yes | Spells > Flame Strike |
| 7 | 3 | 0.85 | yes | Spells > Delayed Blast Fireball |
| 8 | 1 | 0.64 | yes | Spells > Fireball |
| 9 | 7 | -0.09 |  | Spells > Delayed Blast Fireball |
| 10 | 8 | -0.39 |  | Spells > Using a Higher-Level Spell Slot |
| 11 | 16 | -3.98 |  | Spells > Saving Throws |
| 12 | 12 | -6.36 |  | Spells > Targets |
| 13 | 13 | -6.39 |  | Spells > Targets |
| 14 | 17 | -6.54 |  | Playing the Game > Saving Throws |
| 15 | 15 | -7.39 |  | Rules Glossary > Burning [Hazard] |
| 16 | 11 | -9.85 |  | Spells > Targets |
| 17 | 14 | -11.33 |  | Rules Glossary > Sphere [Area of Effect] |

*retrieved sections:* Classes > Level 14: Overchannel | Spells > Chain Lightning | Spells > Fireball | Spells > Cloudkill | Playing the Game > Damage against Multiple Targets | Spells > Flame Strike | Spells > Delayed Blast Fireball

<details><summary>full retrieved context</summary>

```
[Classes > Level 14: Overchannel]
#### Level 14: Overchannel  
You can increase the power of your spells. When you cast a Wizard spell with a spell slot of levels 1–5 that deals damage, you can deal maximum damage with that spell on the turn you cast it.  
The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a Long Rest, you take 2d12 Necrotic damage for each level of the spell slot immediately after you cast it. This damage ignores Resistance and Immunity.

---

[Spells > Chain Lightning]
Each target makes a Dexterity saving throw, taking 10d8 Lightning damage on a failed save or half as much damage on a successful one.  
_Using a Higher-Level Spell Slot._ One additional bolt leaps from the first target to another target for each spell slot level above 6.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Cloudkill]
Each creature in the Sphere makes a Constitution saving throw, taking 5d8 Poison damage on a failed save or half as much damage on a successful one. A creature must also make this save when the Sphere moves into its space and when it enters the Sphere or ends its turn there. A creature makes this save only once per turn.  
The Sphere moves 10 feet away from you at the start of each of your turns.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d8 for each spell slot level above 5.

---

[Playing the Game > Damage against Multiple Targets]
#### Damage against Multiple Targets  
When you create a damaging effect that forces two or more targets to make saving throws against it at the same time, roll the damage once for all the targets. For example, when a wizard casts _Fireball_, the spell's damage is rolled once for all creatures caught in the blast.

---

[Spells > Flame Strike]
_Using a Higher-Level Spell Slot._ The Fire damage and the Radiant damage increase by 1d6 for each spell slot level above 5.

---

[Spells > Delayed Blast Fireball]
When the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The base damage increases by 1d6 for each spell slot level above 7.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.
```
</details>


### v6_agentic  (12 chunks, 3 LLM call(s))

A wizard casting Fireball using a 5th-level spell slot deals 9d6 + 2d6 damage in total (9d6 for the base level plus 1d6 for each level above 3, for a total of 2 levels above 3). Targets make a Dexterity saving throw.

*facts found (judge): 1/2; missing: 11d6*

*agentic sub-queries:* Fireball / 5th-level spell slot / damage dice / saving throw


*re-ranking* (query: `Fireball`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 12 | 5.21 | yes | Spells > Fireball |
| 2 | 14 | 4.80 | yes | Spells > Fireball |
| 3 | 2 | 4.02 | yes | Magic Items > Wand of Fireballs |
| 4 | 1 | 3.97 |  | Magic Items > Necklace of Fireballs |
| 5 | 17 | 3.59 |  | Spells > Delayed Blast Fireball |
| 6 | 8 | 3.44 |  | Spells > Delayed Blast Fireball |
| 7 | 16 | 3.02 |  | Magic Items > Wand of Fireballs |
| 8 | 9 | 2.52 |  | Monsters A–Z > Actions |
| 9 | 11 | 2.35 |  | Monsters A–Z > Actions |
| 10 | 6 | 1.66 |  | Magic Items > Helm of Brilliance |
| 11 | 4 | 1.58 |  | Magic Items > Staff of Fire |
| 12 | 20 | 1.47 |  | Character Creation > Tier 2 (Levels 5–10) |
| 13 | 3 | 1.20 |  | Magic Items > Staff of the Magi |
| 14 | 19 | 0.69 |  | Monsters A–Z > Actions |
| 15 | 7 | 0.00 |  | Magic Items > Hat of Many Spells |
| 16 | 5 | -0.60 |  | Magic Items > Staff of Power |
| 17 | 13 | -0.90 |  | Gameplay Toolbox > Fire-Casting Statue |
| 18 | 10 | -1.42 |  | Gameplay Toolbox > Fire-Casting Statue |
| 19 | 18 | -3.76 |  | Equipment > Tinderbox (5 SP) |
| 20 | 15 | -9.50 |  | Gameplay Toolbox > Spiked Pit |


*re-ranking* (query: `5th-level spell slot`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.07 | yes | Classes > Level 2: Font of Magic |
| 2 | 6 | 4.50 | yes | Spells > Hold Monster |
| 3 | 20 | 4.36 | yes | Spells > Flame Strike |
| 4 | 18 | 4.21 |  | Spells > Cone of Cold |
| 5 | 8 | 3.89 |  | Spells > Mass Cure Wounds |
| 6 | 3 | 3.87 |  | Spells > Spell Slots |
| 7 | 2 | 3.13 |  | Spells > Using a Higher-Level Spell Slot |
| 8 | 9 | 2.61 |  | Spells > Charm Monster |
| 9 | 14 | 2.58 |  | Spells > Circle of Death |
| 10 | 10 | 2.38 |  | Spells > Wall of Fire |
| 11 | 17 | 1.99 |  | Spells > Enhance Ability |
| 12 | 19 | 1.84 |  | Spells > Hold Person |
| 13 | 11 | 1.68 |  | Spells > Blindness/Deafness |
| 14 | 15 | 1.59 |  | Spells > Bane |
| 15 | 12 | 1.51 |  | Spells > Charm Person |
| 16 | 7 | 1.50 |  | Spells > Magic Missile |
| 17 | 13 | 1.45 |  | Spells > Burning Hands |
| 18 | 4 | 1.45 |  | Spells > Heroism |
| 19 | 5 | 1.43 |  | Spells > Prayer of Healing |
| 20 | 16 | 1.29 |  | Spells > Animal Friendship |


*re-ranking* (query: `damage dice`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 6.28 | yes | Playing the Game > Damage Rolls |
| 2 | 6 | 5.66 | yes | Playing the Game > Damage Rolls |
| 3 | 5 | 5.11 | yes | Playing the Game > Critical Hits |
| 4 | 3 | 3.53 |  | Rules Glossary > Critical Hit |
| 5 | 19 | 2.99 |  | Feats > Savage Attacker |
| 6 | 7 | 2.41 |  | Rules Glossary > Damage Roll |
| 7 | 11 | 0.10 |  | Rules Glossary > Damage |
| 8 | 14 | -0.60 |  | Playing the Game > Instant Death |
| 9 | 17 | -0.71 |  | Monsters > Damage Notation |
| 10 | 10 | -1.22 |  | Rules Glossary > Damage Threshold |
| 11 | 13 | -1.99 |  | Playing the Game > Half Damage |
| 12 | 16 | -3.70 |  | Playing the Game > Death Saving Throws |
| 13 | 1 | -4.17 |  | Rules Glossary > Hit Point Dice |
| 14 | 12 | -4.65 |  | Rules Glossary > Damage Threshold |
| 15 | 18 | -5.21 |  | Character Creation > Fill In Numbers |
| 16 | 15 | -6.25 |  | Character Creation > Hit Points and Hit Point Dice |
| 17 | 9 | -6.34 |  | Monsters > Hit Points |
| 18 | 4 | -7.43 |  | Monsters > Hit Points |
| 19 | 8 | -8.31 |  | Monsters > Hit Points |
| 20 | 20 | -8.52 |  | Character Creation > Hit Points and Hit Point Dice |


*re-ranking* (query: `saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 9.77 | yes | Rules Glossary > Saving Throw |
| 2 | 11 | 9.51 | yes | Playing the Game > Saving Throws |
| 3 | 1 | 7.83 | yes | Rules Glossary > Save |
| 4 | 10 | 7.60 |  | Spells > Saving Throws |
| 5 | 2 | 7.43 |  | Playing the Game > Saving Throw Proficiencies |
| 6 | 12 | 7.28 |  | Playing the Game > Ability Modifier |
| 7 | 16 | 7.13 |  | Magic Items > Thunderous Greatclub |
| 8 | 7 | 7.06 |  | Monsters > Saving Throw Effect Notation |
| 9 | 9 | 6.95 |  | Spells > Power Word Stun |
| 10 | 4 | 6.86 |  | Playing the Game > Saving Throw Proficiencies |
| 11 | 18 | 6.84 |  | Playing the Game > Difficulty Class |
| 12 | 5 | 6.81 |  | Rules Glossary > Death Saving Throw |
| 13 | 13 | 6.68 |  | Rules Glossary > Stat Block |
| 14 | 19 | 6.64 |  | Spells > Flesh to Stone |
| 15 | 17 | 6.35 |  | Playing the Game > Half Damage |
| 16 | 8 | 6.18 |  | Playing the Game > Death Saving Throws |
| 17 | 20 | 6.18 |  | Spells > Targets |
| 18 | 14 | 6.05 |  | Playing the Game > Saving Throws and Damage |
| 19 | 15 | 5.65 |  | Spells > Symbol |
| 20 | 6 | 4.92 |  | Playing the Game > Proficiency Bonus |

*retrieved sections:* Spells > Fireball | Magic Items > Wand of Fireballs | Classes > Level 2: Font of Magic | Spells > Hold Monster | Spells > Flame Strike | Playing the Game > Damage Rolls | Playing the Game > Critical Hits | Rules Glossary > Saving Throw | Playing the Game > Saving Throws | Rules Glossary > Save

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Magic Items > Wand of Fireballs]
#### Wand of Fireballs  
_Wand, Rare (Requires Attunement by a Spellcaster)_  
This wand has 7 charges. While holding it, you can expend no more than 3 charges to cast _Fireball_ (save DC 15) from it. For 1 charge, you cast the level 3 version of the spell. You can increase the spell's level by 1 for each additional charge you expend.

---

[Classes > Level 2: Font of Magic]
_Creating Spell Slots._ As a Bonus Action, you can transform unexpended Sorcery Points into one spell slot. The Creating Spell Slots table shows the cost of creating a spell slot of a given level, and it lists the minimum Sorcerer level you must be to create a slot. You can create a spell slot no higher than level 5.  
Any spell slot you create with this feature vanishes when you finish a Long Rest.  
**Creating Spell Slots**  
<table>
<thead>
<tr>
<th>Spell Slot Level</th>

---

[Spells > Hold Monster]
_Using a Higher-Level Spell Slot._ You can target one additional creature for each spell slot level above 5.

---

[Spells > Flame Strike]
_Using a Higher-Level Spell Slot._ The Fire damage and the Radiant damage increase by 1d6 for each spell slot level above 5.

---

[Playing the Game > Damage Rolls]
### Damage Rolls  
Each weapon, spell, and damaging monster ability specifies the damage it deals. You roll the damage dice, add any modifiers, and deal the damage to your target. If there's a penalty to the damage, it's possible to deal 0 damage but not negative damage.

---

[Playing the Game > Damage Rolls]
When attacking with a weapon, you add your ability modifier—the same modifier used for the attack roll—to the damage roll. A spell tells you which dice to roll for damage and whether to add any modifiers. Unless a rule says otherwise, you don't add your ability modifier to a fixed damage amount that doesn't use a roll, such as the damage of a Blowgun. See "Equipment" for weapons' damage dice and "Spells" for spells' damage dice.

---

[Playing the Game > Critical Hits]
### Critical Hits  
When you score a Critical Hit, you deal extra damage. Roll the attack's damage dice twice, add them together, and add any relevant modifiers as normal. For example, if you score a Critical Hit with a Dagger, roll 2d4 for the damage rather than 1d4, and add your relevant ability modifier. If the attack involves other damage dice, such as from the Rogue's Sneak Attack feature, you also roll those dice twice.

---

[Rules Glossary > Saving Throw]
#### Saving Throw  
A saving throw—also called a save—represents an attempt to avoid or resist a threat. You normally make a saving throw only when a rule requires you to do so, but you can decide to fail the save without rolling. The result of a save is detailed in the effect that allowed it. If a target is forced to make a save and lacks the ability score used by it, the target automatically fails. _See also_ "Playing the Game" ("D20 Tests").

---

[Playing the Game > Saving Throws]
### Saving Throws  
A saving throw—also called a save—represents an attempt to evade or resist a threat, such as a fiery explosion, a blast of poisonous gas, or a spell trying to invade your mind. You don't normally choose to make a save; you must make one because your character or a monster (if you're the GM) is at risk. A save's result is detailed in the effect that caused it.  
If you don't want to resist the effect, you can choose to fail the save without rolling.

---

[Rules Glossary > Save]
#### Save  
Save is another name for a saving throw. _See also_ "Saving Throw."
```
</details>


---

## q19 (needle) What are the Owlbear's Rend attack bonus, damage and damage type, and what does the Goblin Warrior's Nimble Escape let it do?

**Gold facts (counterfactual data):** +7; 14 (2d8 + 5); Slashing; Disengage or Hide


### v0_closed_book  (0 chunks, 1 LLM call(s))

The Owlbear's Rend attack has a bonus of +5 to hit and deals 2d8+3 slashing damage.

The Goblin Warrior's Nimble Escape allows the goblin to take the Dash action as a bonus action on their turn, provided they aren't restrained or knocked prone.

*facts found (judge): 1/4; missing: +7; 14 (2d8 + 5); Disengage or Hide*


### v1_baseline  (3 chunks, 1 LLM call(s))

The Owlbear's Rend attack has a bonus of +7, deals 14 (2d8 + 5) slashing damage.

The second part of your question asks about the Goblin Warrior's Nimble Escape action, but there is no information provided in the given context about a Goblin Warrior or its Nimble Escape action. Therefore, the answer to the second part of the question is missing based on the provided context.

*facts found (judge): 3/4; missing: Disengage or Hide*

*retrieved sections:* Monsters A–Z > Actions | Animals > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The eagle makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 5 (1d4 + 3) Slashing damage plus 3 (1d6) Radiant damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of Weakening Breath.  
**_Rend._** _Melee Attack Roll:_ +10, reach 10 ft. _Hit:_ 17 (2d10 + 6) Slashing damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 17, each creature in a 30-foot Cone. _Failure:_ 55 (10d10) Fire damage. _Success:_ Half damage.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the Goblin Warrior or its actions, specifically the Nimble Escape ability. Therefore, the second part of the question regarding the Goblin Warrior's Nimble Escape cannot be answered based on the given information. 

Owlbear's Rend attack details:
- Bonus: +7
- Damage: 14 (2d8 + 5) Slashing damage
- Damage Type: Slashing

*facts found (judge): 3/4; missing: Disengage or Hide*


*re-ranking* (query: `What are the Owlbear's Rend attack bonus, damage and damage type, and what does `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.98 | yes | Monsters A–Z > Actions |
| 2 | 8 | -1.60 | yes | Monsters A–Z > Actions |
| 3 | 7 | -1.71 | yes | Monsters A–Z > Actions |
| 4 | 2 | -1.88 |  | Animals > Actions |
| 5 | 6 | -1.90 |  | Monsters A–Z > Actions |
| 6 | 9 | -1.95 |  | Monsters A–Z > Bonus Actions |
| 7 | 5 | -2.06 |  | Monsters A–Z > Actions |
| 8 | 3 | -2.32 |  | Monsters A–Z > Actions |
| 9 | 4 | -2.52 |  | Monsters A–Z > Actions |
| 10 | 10 | -3.40 |  | Animals > Actions |

*retrieved sections:* Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of (A) Sleep Breath or (B) Spellcasting to cast _Scorching Ray_.  
**_Rend._** _Melee Attack Roll:_ +11, reach 10 ft. _Hit:_ 17 (2d10 + 6) Slashing damage plus 4 (1d8) Fire damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 18, each creature in a 60-foot-long, 5-foot-wide Line. _Failure:_ 45 (10d8) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast _Shatter_ (level 3 version).  
**_Rend._** _Melee Attack Roll:_ +16, reach 15 ft. _Hit:_ 18 (2d8 + 9) Slashing damage plus 11 (2d10) Lightning damage.  
**_Lightning Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 23, each creature in a 120-foot-long, 10-foot-wide Line. _Failure:_ 88 (16d10) Lightning damage. _Success:_ Half damage.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The Owlbear's Rend attack has a bonus of +7, deals 14 (2d8 + 5) slashing damage.

The Goblin Warrior's Nimble Escape lets it take the Disengage or Hide action.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Owlbear's Rend attack bonus, damage and damage type, and what does `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.98 | yes | Monsters A–Z > Actions |
| 2 | 8 | -1.60 | yes | Monsters A–Z > Actions |
| 3 | 7 | -1.71 | yes | Monsters A–Z > Actions |
| 4 | 2 | -1.88 | yes | Animals > Actions |
| 5 | 6 | -1.90 | yes | Monsters A–Z > Actions |
| 6 | 9 | -1.95 | yes | Monsters A–Z > Bonus Actions |
| 7 | 5 | -2.06 | yes | Monsters A–Z > Actions |
| 8 | 3 | -2.32 | yes | Monsters A–Z > Actions |
| 9 | 4 | -2.52 |  | Monsters A–Z > Actions |
| 10 | 10 | -3.40 |  | Animals > Actions |

*retrieved sections:* Monsters A–Z > Actions | Animals > Actions | Monsters A–Z > Bonus Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of (A) Sleep Breath or (B) Spellcasting to cast _Scorching Ray_.  
**_Rend._** _Melee Attack Roll:_ +11, reach 10 ft. _Hit:_ 17 (2d10 + 6) Slashing damage plus 4 (1d8) Fire damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 18, each creature in a 60-foot-long, 5-foot-wide Line. _Failure:_ 45 (10d8) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast _Shatter_ (level 3 version).  
**_Rend._** _Melee Attack Roll:_ +16, reach 15 ft. _Hit:_ 18 (2d8 + 9) Slashing damage plus 11 (2d10) Lightning damage.  
**_Lightning Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 23, each creature in a 120-foot-long, 10-foot-wide Line. _Failure:_ 88 (16d10) Lightning damage. _Success:_ Half damage.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The eagle makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 5 (1d4 + 3) Slashing damage plus 3 (1d6) Radiant damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +14, reach 15 ft. _Hit:_ 17 (2d8 + 8) Slashing damage plus 7 (2d6) Cold damage.  
**_Cold Breath (Recharge 5–6)._** _Constitution Saving Throw:_ DC 22, each creature in a 90-foot Cone. _Failure:_ 63 (14d8) Cold damage. _Success:_ Half damage.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Nimble Escape._** The goblin takes the Disengage or Hide action.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of (A) Repulsion Breath or (B) Spellcasting to cast _Guiding Bolt_ (level 2 version).  
**_Rend._** _Melee Attack Roll:_ +16, reach 15 ft. _Hit:_ 18 (2d8 + 9) Slashing damage plus 9 (2d8) Lightning damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of Weakening Breath.  
**_Rend._** _Melee Attack Roll:_ +10, reach 10 ft. _Hit:_ 17 (2d10 + 6) Slashing damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 17, each creature in a 30-foot Cone. _Failure:_ 55 (10d10) Fire damage. _Success:_ Half damage.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the Goblin Warrior or its actions, specifically the Nimble Escape ability. Therefore, the second part of the question regarding the Goblin Warrior's Nimble Escape cannot be answered based on the given information. 

Owlbear's Rend attack details:
- Bonus: +7
- Damage: 14 (2d8 + 5) Slashing damage
- Damage Type: Slashing

*facts found (judge): 3/4; missing: Disengage or Hide*


*re-ranking* (query: `What are the Owlbear's Rend attack bonus, damage and damage type, and what does `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.98 | yes | Monsters A–Z > Actions |
| 2 | 8 | -1.60 | yes | Monsters A–Z > Actions |
| 3 | 7 | -1.71 | yes | Monsters A–Z > Actions |
| 4 | 2 | -1.88 |  | Animals > Actions |
| 5 | 6 | -1.90 |  | Monsters A–Z > Actions |
| 6 | 9 | -1.95 |  | Monsters A–Z > Bonus Actions |
| 7 | 5 | -2.06 |  | Monsters A–Z > Actions |
| 8 | 3 | -2.32 |  | Monsters A–Z > Actions |
| 9 | 4 | -2.52 |  | Monsters A–Z > Actions |
| 10 | 10 | -3.40 |  | Animals > Actions |

*retrieved sections:* Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of (A) Sleep Breath or (B) Spellcasting to cast _Scorching Ray_.  
**_Rend._** _Melee Attack Roll:_ +11, reach 10 ft. _Hit:_ 17 (2d10 + 6) Slashing damage plus 4 (1d8) Fire damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 18, each creature in a 60-foot-long, 5-foot-wide Line. _Failure:_ 45 (10d8) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast _Shatter_ (level 3 version).  
**_Rend._** _Melee Attack Roll:_ +16, reach 15 ft. _Hit:_ 18 (2d8 + 9) Slashing damage plus 11 (2d10) Lightning damage.  
**_Lightning Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 23, each creature in a 120-foot-long, 10-foot-wide Line. _Failure:_ 88 (16d10) Lightning damage. _Success:_ Half damage.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The Owlbear's Rend attack has a bonus of +7, deals 14 (2d8 + 5) slashing damage.

The Goblin Warrior's Nimble Escape lets the goblin take the Disengage or Hide action.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Owlbear's Rend attack bonus, damage and damage type, and what does `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.98 | yes | Monsters A–Z > Actions |
| 2 | 5 | -0.82 | yes | Monsters A–Z > Bonus Actions |
| 3 | 12 | -1.17 | yes | Spells > Actions |
| 4 | 27 | -1.60 | yes | Monsters A–Z > Actions |
| 5 | 25 | -1.71 | yes | Monsters A–Z > Actions |
| 6 | 8 | -1.88 | yes | Animals > Actions |
| 7 | 22 | -1.90 | yes | Monsters A–Z > Actions |
| 8 | 2 | -1.95 | yes | Monsters A–Z > Bonus Actions |
| 9 | 4 | -2.06 |  | Monsters A–Z > Actions |
| 10 | 7 | -2.14 |  | Monsters A–Z > Actions |
| 11 | 13 | -2.20 |  | Monsters A–Z > Actions |
| 12 | 3 | -2.32 |  | Monsters A–Z > Actions |
| 13 | 16 | -2.52 |  | Monsters A–Z > Actions |
| 14 | 28 | -3.42 |  | Magic Items > Dragon Slayer |
| 15 | 9 | -3.74 |  | Animals > Bonus Actions |
| 16 | 6 | -3.96 |  | Animals > Actions |
| 17 | 10 | -4.04 |  | Animals > Bonus Actions |
| 18 | 11 | -5.13 |  | Spells > Shillelagh |
| 19 | 29 | -5.26 |  | Classes > Level 1: Sneak Attack |
| 20 | 18 | -5.28 |  | Monsters > Attack Notation |

*retrieved sections:* Monsters A–Z > Actions | Monsters A–Z > Bonus Actions | Spells > Actions | Animals > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Rampage (1/Day)._** Immediately after dealing damage to a creature that is already Bloodied, the gnoll moves up to half its Speed, and it makes one Rend attack.

---

[Spells > Actions]
#### Actions  
_Multiattack._ The spirit makes a number of Rend attacks equal to half the spell's level (round down), and it uses Breath Weapon.  
_Rend. Melee Attack Roll:_ Bonus equals your spell attack modifier, reach 10 feet. _Hit:_ 1d6 + 4 + the spell's level Piercing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of (A) Sleep Breath or (B) Spellcasting to cast _Scorching Ray_.  
**_Rend._** _Melee Attack Roll:_ +11, reach 10 ft. _Hit:_ 17 (2d10 + 6) Slashing damage plus 4 (1d8) Fire damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 18, each creature in a 60-foot-long, 5-foot-wide Line. _Failure:_ 45 (10d8) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of Spellcasting to cast _Shatter_ (level 3 version).  
**_Rend._** _Melee Attack Roll:_ +16, reach 15 ft. _Hit:_ 18 (2d8 + 9) Slashing damage plus 11 (2d10) Lightning damage.  
**_Lightning Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 23, each creature in a 120-foot-long, 10-foot-wide Line. _Failure:_ 88 (16d10) Lightning damage. _Success:_ Half damage.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The eagle makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 5 (1d4 + 3) Slashing damage plus 3 (1d6) Radiant damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +14, reach 15 ft. _Hit:_ 17 (2d8 + 8) Slashing damage plus 7 (2d6) Cold damage.  
**_Cold Breath (Recharge 5–6)._** _Constitution Saving Throw:_ DC 22, each creature in a 90-foot Cone. _Failure:_ 63 (14d8) Cold damage. _Success:_ Half damage.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Nimble Escape._** The goblin takes the Disengage or Hide action.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

The Owlbear's Rend attack has a bonus of +7, deals 14 (2d8 + 5) slashing damage.

The Goblin's Nimble Escape lets it take the Disengage or Hide action.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Owlbear's Rend attack bonus, damage and damage type, and what does `): candidate pool of 23, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.98 | yes | Monsters A–Z > Actions |
| 2 | 5 | -0.82 | yes | Monsters A–Z > Bonus Actions |
| 3 | 8 | -1.88 | yes | Animals > Actions |
| 4 | 2 | -1.95 | yes | Monsters A–Z > Bonus Actions |
| 5 | 4 | -2.06 | yes | Monsters A–Z > Actions |
| 6 | 7 | -2.14 | yes | Monsters A–Z > Actions |
| 7 | 3 | -2.32 | yes | Monsters A–Z > Actions |
| 8 | 9 | -3.74 | yes | Animals > Bonus Actions |
| 9 | 6 | -3.96 |  | Animals > Actions |
| 10 | 10 | -4.04 |  | Animals > Bonus Actions |
| 11 | 11 | -6.46 |  | Monsters A–Z > Owlbear |
| 12 | 12 | -7.38 |  | Monsters A–Z > Owlbear |
| 13 | 21 | -7.40 |  | Playing the Game > Half Damage |
| 14 | 15 | -7.60 |  | Monsters A–Z > Goblin Warrior |
| 15 | 13 | -7.97 |  | Monsters A–Z > Goblin Warrior |
| 16 | 22 | -8.38 |  | Spells > Guiding Bolt |
| 17 | 14 | -8.90 |  | Monsters A–Z > Goblin Warrior |
| 18 | 23 | -10.48 |  | Rules Glossary > Bloodied |
| 19 | 16 | -10.50 |  | Rules Glossary > Disengage [Action] |
| 20 | 20 | -10.80 |  | Rules Glossary > Cone [Area of Effect] |

*retrieved sections:* Monsters A–Z > Actions | Monsters A–Z > Bonus Actions | Animals > Actions | Animals > Bonus Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Rampage (1/Day)._** Immediately after dealing damage to a creature that is already Bloodied, the gnoll moves up to half its Speed, and it makes one Rend attack.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The eagle makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 5 (1d4 + 3) Slashing damage plus 3 (1d6) Radiant damage.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Nimble Escape._** The goblin takes the Disengage or Hide action.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of (A) Repulsion Breath or (B) Spellcasting to cast _Guiding Bolt_ (level 2 version).  
**_Rend._** _Melee Attack Roll:_ +16, reach 15 ft. _Hit:_ 18 (2d8 + 9) Slashing damage plus 9 (2d8) Lightning damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The nalfeshnee makes three Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +10, reach 10 ft. _Hit:_ 16 (2d10 + 5) Slashing damage plus 11 (2d10) Force damage.  
**_Teleport._** The nalfeshnee teleports up to 120 feet to an unoccupied space it can see.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of Weakening Breath.  
**_Rend._** _Melee Attack Roll:_ +10, reach 10 ft. _Hit:_ 17 (2d10 + 6) Slashing damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 17, each creature in a 30-foot Cone. _Failure:_ 55 (10d10) Fire damage. _Success:_ Half damage.

---

[Animals > Bonus Actions]
### Bonus Actions  
<hr>  
**_Nimble Escape._** The panther takes the Disengage or Hide action.
```
</details>


### v6_agentic  (10 chunks, 3 LLM call(s))

The Owlbear's Rend attack has a bonus of +7, deals 14 (2d8 + 5) slashing damage.

The Goblin Warrior's Nimble Escape lets it take either the Disengage or Hide action.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Owlbear Rend / Goblin Warrior Nimble Escape


*re-ranking* (query: `Owlbear Rend`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.95 | yes | Monsters A–Z > Actions |
| 2 | 13 | -0.86 | yes | Monsters A–Z > Actions |
| 3 | 2 | -0.96 | yes | Monsters A–Z > Owlbear |
| 4 | 8 | -3.81 |  | Monsters A–Z > Owlbear |
| 5 | 4 | -5.13 |  | Monsters A–Z > Actions |
| 6 | 14 | -5.26 |  | Monsters A–Z > Actions |
| 7 | 11 | -5.31 |  | Monsters A–Z > Actions |
| 8 | 9 | -5.33 |  | Monsters A–Z > Actions |
| 9 | 15 | -5.52 |  | Monsters A–Z > Actions |
| 10 | 12 | -5.75 |  | Monsters A–Z > Actions |
| 11 | 5 | -5.98 |  | Monsters A–Z > Actions |
| 12 | 7 | -6.02 |  | Monsters A–Z > Actions |
| 13 | 17 | -6.14 |  | Animals > Actions |
| 14 | 19 | -6.60 |  | Animals > Actions |
| 15 | 3 | -6.96 |  | Monsters A–Z > Actions |
| 16 | 10 | -7.00 |  | Monsters A–Z > Actions |
| 17 | 6 | -7.10 |  | Monsters A–Z > Actions |
| 18 | 18 | -8.85 |  | Animals > Owl |
| 19 | 16 | -9.22 |  | Animals > Giant Owl |
| 20 | 20 | -10.02 |  | Animals > Giant Owl |


*re-ranking* (query: `Goblin Warrior Nimble Escape`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.99 | yes | Monsters A–Z > Bonus Actions |
| 2 | 2 | -0.27 | yes | Monsters A–Z > Goblin Warrior |
| 3 | 6 | -1.13 | yes | Animals > Bonus Actions |
| 4 | 3 | -1.31 |  | Animals > Bonus Actions |
| 5 | 5 | -2.48 |  | Monsters A–Z > Goblin Warrior |
| 6 | 4 | -2.79 |  | Monsters A–Z > Goblin Warrior |
| 7 | 7 | -3.15 |  | Monsters A–Z > Hobgoblin Warrior |
| 8 | 8 | -3.39 |  | Monsters A–Z > Bugbear Warrior |
| 9 | 9 | -3.98 |  | Monsters A–Z > Bugbear Warrior |
| 10 | 16 | -4.56 |  | Monsters A–Z > Reactions |
| 11 | 11 | -5.10 |  | Monsters A–Z > Actions |
| 12 | 15 | -5.12 |  | Magic Items > Deck of Illusions |
| 13 | 19 | -6.71 |  | Monsters A–Z > Bugbear Stalker |
| 14 | 10 | -6.73 |  | Monsters A–Z > Goblin Minion |
| 15 | 20 | -8.45 |  | Monsters A–Z > Hobgoblin Captain |
| 16 | 17 | -8.63 |  | Monsters A–Z > Hobgoblin Warrior |
| 17 | 13 | -8.87 |  | Monsters A–Z > Gnoll Warrior |
| 18 | 12 | -9.64 |  | Monsters A–Z > Warrior Infantry |
| 19 | 14 | -9.69 |  | Monsters A–Z > Sahuagin Warrior |
| 20 | 18 | -11.03 |  | Classes > Level 10: Heroic Warrior |


*re-ranking* (query: `Owlbear Rend attack bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.33 | yes | Monsters A–Z > Actions |
| 2 | 2 | 1.68 | yes | Spells > Actions |
| 3 | 7 | 0.17 | yes | Monsters A–Z > Bonus Actions |
| 4 | 14 | -0.36 | yes | Monsters A–Z > Actions |
| 5 | 3 | -1.46 | yes | Animals > Actions |
| 6 | 4 | -2.34 |  | Monsters A–Z > Actions |
| 7 | 12 | -2.52 |  | Monsters A–Z > Actions |
| 8 | 10 | -2.61 |  | Monsters A–Z > Actions |
| 9 | 19 | -2.65 |  | Monsters A–Z > Actions |
| 10 | 18 | -2.71 |  | Monsters A–Z > Actions |
| 11 | 17 | -2.97 |  | Monsters A–Z > Actions |
| 12 | 11 | -3.04 |  | Animals > Actions |
| 13 | 20 | -3.09 | yes | Monsters A–Z > Owlbear |
| 14 | 9 | -3.10 |  | Monsters A–Z > Actions |
| 15 | 15 | -3.19 |  | Monsters A–Z > Actions |
| 16 | 6 | -3.39 |  | Animals > Actions |
| 17 | 13 | -3.71 |  | Monsters A–Z > Actions |
| 18 | 8 | -3.77 |  | Monsters A–Z > Actions |
| 19 | 5 | -3.77 |  | Animals > Actions |
| 20 | 16 | -4.37 |  | Monsters A–Z > Legendary Actions |


*re-ranking* (query: `Owlbear Rend damage`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.44 | yes | Monsters A–Z > Actions |
| 2 | 2 | -0.47 | yes | Animals > Actions |
| 3 | 20 | -1.92 | yes | Monsters A–Z > Actions |
| 4 | 6 | -2.29 |  | Monsters A–Z > Actions |
| 5 | 17 | -2.35 |  | Monsters A–Z > Actions |
| 6 | 13 | -2.41 |  | Monsters A–Z > Actions |
| 7 | 11 | -2.44 |  | Monsters A–Z > Actions |
| 8 | 10 | -2.52 |  | Monsters A–Z > Actions |
| 9 | 16 | -2.55 |  | Monsters A–Z > Actions |
| 10 | 8 | -2.61 |  | Monsters A–Z > Actions |
| 11 | 5 | -2.62 |  | Monsters A–Z > Actions |
| 12 | 14 | -2.74 |  | Monsters A–Z > Actions |
| 13 | 12 | -2.95 |  | Monsters A–Z > Actions |
| 14 | 7 | -3.05 |  | Monsters A–Z > Actions |
| 15 | 4 | -3.13 |  | Animals > Actions |
| 16 | 9 | -3.29 |  | Monsters A–Z > Actions |
| 17 | 3 | -3.40 |  | Animals > Actions |
| 18 | 15 | -3.56 | yes | Spells > Actions |
| 19 | 19 | -3.92 | yes | Monsters A–Z > Owlbear |
| 20 | 18 | -4.36 |  | Animals > Actions |


*re-ranking* (query: `Owlbear Rend damage type`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.88 | yes | Monsters A–Z > Actions |
| 2 | 2 | -1.53 | yes | Animals > Actions |
| 3 | 20 | -3.21 | yes | Monsters A–Z > Actions |
| 4 | 19 | -3.52 |  | Monsters A–Z > Actions |
| 5 | 11 | -3.53 |  | Monsters A–Z > Actions |
| 6 | 6 | -3.55 |  | Monsters A–Z > Actions |
| 7 | 9 | -3.56 |  | Monsters A–Z > Actions |
| 8 | 7 | -3.60 |  | Monsters A–Z > Actions |
| 9 | 13 | -3.65 |  | Monsters A–Z > Actions |
| 10 | 5 | -3.73 |  | Monsters A–Z > Actions |
| 11 | 10 | -3.85 |  | Monsters A–Z > Actions |
| 12 | 14 | -3.87 | yes | Monsters A–Z > Owlbear |
| 13 | 12 | -4.04 |  | Monsters A–Z > Actions |
| 14 | 15 | -4.10 |  | Monsters A–Z > Actions |
| 15 | 4 | -4.19 |  | Animals > Actions |
| 16 | 8 | -4.21 |  | Monsters A–Z > Actions |
| 17 | 3 | -4.46 |  | Animals > Actions |
| 18 | 17 | -7.19 |  | Playing the Game > Resistance and Vulnerability |
| 19 | 16 | -9.15 |  | Classes > Level 3: Deflect Attacks |
| 20 | 18 | -9.22 |  | Rules Glossary > Vulnerability |


*re-ranking* (query: `Goblin Warrior Nimble Escape`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.99 | yes | Monsters A–Z > Bonus Actions |
| 2 | 2 | -0.27 | yes | Monsters A–Z > Goblin Warrior |
| 3 | 6 | -1.13 | yes | Animals > Bonus Actions |
| 4 | 3 | -1.31 |  | Animals > Bonus Actions |
| 5 | 5 | -2.48 |  | Monsters A–Z > Goblin Warrior |
| 6 | 4 | -2.79 |  | Monsters A–Z > Goblin Warrior |
| 7 | 7 | -3.15 |  | Monsters A–Z > Hobgoblin Warrior |
| 8 | 8 | -3.39 |  | Monsters A–Z > Bugbear Warrior |
| 9 | 9 | -3.98 |  | Monsters A–Z > Bugbear Warrior |
| 10 | 16 | -4.56 |  | Monsters A–Z > Reactions |
| 11 | 11 | -5.10 |  | Monsters A–Z > Actions |
| 12 | 15 | -5.12 |  | Magic Items > Deck of Illusions |
| 13 | 19 | -6.71 |  | Monsters A–Z > Bugbear Stalker |
| 14 | 10 | -6.73 |  | Monsters A–Z > Goblin Minion |
| 15 | 20 | -8.45 |  | Monsters A–Z > Hobgoblin Captain |
| 16 | 17 | -8.63 |  | Monsters A–Z > Hobgoblin Warrior |
| 17 | 13 | -8.87 |  | Monsters A–Z > Gnoll Warrior |
| 18 | 12 | -9.64 |  | Monsters A–Z > Warrior Infantry |
| 19 | 14 | -9.69 |  | Monsters A–Z > Sahuagin Warrior |
| 20 | 18 | -11.03 |  | Classes > Level 10: Heroic Warrior |

*retrieved sections:* Monsters A–Z > Actions | Monsters A–Z > Owlbear | Monsters A–Z > Bonus Actions | Monsters A–Z > Goblin Warrior | Animals > Bonus Actions | Spells > Actions | Animals > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The werebear makes two attacks, using Handaxe or Rend in any combination. It can replace one attack with a Bite attack.

---

[Monsters A–Z > Owlbear]
## Owlbear  
### Owlbear  
_Large Monstrosity, Unaligned_  
**AC** 15 **Initiative** +1 (11) <br>
**HP** 66 (7d10 + 28) <br>
**Speed** 40 ft., Climb 40 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>20</td>
<td>+5</td>
<td>+5</td>
<td><strong>DEX</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Nimble Escape._** The goblin takes the Disengage or Hide action.

---

[Monsters A–Z > Goblin Warrior]
### Goblin Warrior  
_Small Fey (Goblinoid), Chaotic Neutral_  
**AC** 17 **Initiative** +2 (12) <br>
**HP** 10 (3d6) <br>
**Speed** 30 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>8</td>
<td>−1</td>
<td>−1</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>

---

[Animals > Bonus Actions]
### Bonus Actions  
<hr>  
**_Nimble Escape._** The panther takes the Disengage or Hide action.

---

[Spells > Actions]
#### Actions  
_Multiattack._ The spirit makes a number of Rend attacks equal to half the spell's level (round down), and it uses Breath Weapon.  
_Rend. Melee Attack Roll:_ Bonus equals your spell attack modifier, reach 10 feet. _Hit:_ 1d6 + 4 + the spell's level Piercing damage.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Rampage (1/Day)._** Immediately after dealing damage to a creature that is already Bloodied, the gnoll moves up to half its Speed, and it makes one Rend attack.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The eagle makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 5 (1d4 + 3) Slashing damage plus 3 (1d6) Radiant damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The dragon makes three Rend attacks. It can replace one attack with a use of (A) Slowing Breath or (B) Spellcasting to cast _Mind Spike_ (level 5 version).  
**_Rend._** _Melee Attack Roll:_ +15, reach 15 ft. _Hit:_ 19 (2d10 + 8) Slashing damage plus 9 (2d8) Acid damage.  
**_Acid Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 22, each creature in an 90-foot-long, 10-foot-wide Line. _Failure:_ 63 (14d8) Acid damage. _Success:_ Half damage.
```
</details>


---

## q20 (needle) Which classes can cast Counterspell, and which classes can cast Revivify?

**Gold facts (counterfactual data):** Sorcerer, Warlock, Wizard; Cleric, Druid, Paladin, Ranger


### v0_closed_book  (0 chunks, 1 LLM call(s))

Counterspell can be cast by any spellcaster class that has the spell on their spell list, including:
- Wizard
- Sorcerer
- Warlock
- Cleric
- Druid
- Bard
- Paladin
- Ranger

Revivify can only be cast by:
- Cleric
- Druid
- Paladin
- Ranger

Note that a character must meet the spell's level requirements and have the spell prepared (if applicable).

*facts found (judge): 2/2; missing: none*


### v1_baseline  (3 chunks, 1 LLM call(s))

The context provided does not contain information about which classes can cast Counterspell or Revivify. Therefore, I cannot answer this question based on the given information.

*facts found (judge): 0/2; missing: Sorcerer, Warlock, Wizard; Cleric, Druid, Paladin, Ranger*

*note:* Replayed retrieval differs from the stored context by 3 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.

*retrieved sections:* Monsters A–Z > Reactions | Classes > Level 1: Spellcasting

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Classes > Level 1: Spellcasting]
1 and 2 in any combination, chosen from your spellbook.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The given context does not provide information on which classes can cast Counterspell or Revivify. Information on class abilities to cast specific spells like Counterspell or Revivify is missing.

*facts found (judge): 0/2; missing: Sorcerer, Warlock, Wizard; Cleric, Druid, Paladin, Ranger*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 |  | Spells > Counterspell |
| 2 | 2 | 0.14 | yes | Monsters A–Z > Reactions |
| 3 | 4 | -0.15 | yes | Monsters A–Z > Reactions |
| 4 | 8 | -1.67 | yes | Classes > Level 2: Wild Shape |
| 5 | 3 | -2.71 |  | Spells > Counterspell |
| 6 | 10 | -4.46 |  | Classes > Transmuted Spell |
| 7 | 5 | -5.23 |  | Classes > Level 1: Spellcasting |
| 8 | 6 | -5.26 |  | Classes > Level 1: Spellcasting |
| 9 | 7 | -7.49 |  | Spells > Forbiddance |
| 10 | 9 | -8.05 |  | Monsters > Spellcasting |

*retrieved sections:* Monsters A–Z > Reactions | Classes > Level 2: Wild Shape

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Classes > Level 2: Wild Shape]
**No Spellcasting.** You can't cast spells, but shapeshifting doesn't break your Concentration or otherwise interfere with a spell you've already cast.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The context provided does not mention classes that can cast Counterspell or Revivify. Therefore, I cannot answer which classes can cast these spells based on the given information.

*facts found (judge): 0/2; missing: Sorcerer, Warlock, Wizard; Cleric, Druid, Paladin, Ranger*

*note:* Replayed retrieval differs from the stored context by 2 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 |  | Spells > Counterspell |
| 2 | 2 | 0.14 | yes | Monsters A–Z > Reactions |
| 3 | 4 | -0.15 | yes | Monsters A–Z > Reactions |
| 4 | 8 | -1.67 | yes | Classes > Level 2: Wild Shape |
| 5 | 3 | -2.71 |  | Spells > Counterspell |
| 6 | 10 | -4.46 | yes | Classes > Transmuted Spell |
| 7 | 5 | -5.23 | yes | Classes > Level 1: Spellcasting |
| 8 | 6 | -5.26 | yes | Classes > Level 1: Spellcasting |
| 9 | 7 | -7.49 |  | Spells > Forbiddance |
| 10 | 9 | -8.05 |  | Monsters > Spellcasting |

*retrieved sections:* Monsters A–Z > Reactions | Classes > Level 2: Wild Shape | Classes > Level 1: Spellcasting | Classes > Transmuted Spell

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Classes > Level 2: Wild Shape]
**No Spellcasting.** You can't cast spells, but shapeshifting doesn't break your Concentration or otherwise interfere with a spell you've already cast.

---

[Classes > Level 1: Spellcasting]
#### Level 1: Spellcasting  
You have learned to cast spells through your bardic arts. See "Spells" for the rules on spellcasting. The information below details how you use those rules with Bard spells, which appear in the Bard spell list later in the class's description.  
_Cantrips._ You know two cantrips of your choice from the Bard spell list. _Dancing Lights_ and _Vicious Mockery_ are recommended.

---

[Classes > Transmuted Spell]
#### Transmuted Spell  
_Cost: 1 Sorcery Point_  
When you cast a spell that deals a type of damage from the following list, you can spend 1 Sorcery Point to change that damage type to one of the other listed types: Acid, Cold, Fire, Lightning, Poison, Thunder.

---

[Classes > Level 1: Spellcasting]
_Prepared Spells of Level 1+._ You prepare the list of level 1+ spells that are available for you to cast with this feature. To start, choose four level 1 spells from the Bard spell list. _Charm Person_, _Color Spray_, _Dissonant Whispers_, and _Healing Word_ are recommended.

---

[Classes > Level 1: Spellcasting]
1 and 2 in any combination, chosen from your spellbook.

---

[Classes > Level 1: Spellcasting]
six Sorcerer spells of level 1 or 2 in any combination.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The context provided does not mention Revivify or any classes that can cast it. The context only discusses Counterspell and its availability to Sorcerer, Warlock, and Wizard classes. Therefore, I can only answer the first part of the question:

Counterspell can be cast by Sorcerer, Warlock, and Wizard classes.

*facts found (judge): 1/2; missing: Cleric, Druid, Paladin, Ranger*


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 | yes | Spells > Counterspell |
| 2 | 2 | -2.71 | yes | Spells > Counterspell |
| 3 | 9 | -4.28 | yes | Classes > Level 1: Spellcasting |
| 4 | 7 | -4.46 |  | Classes > Transmuted Spell |
| 5 | 8 | -4.54 |  | Classes > Level 1: Spellcasting |
| 6 | 10 | -5.13 |  | Classes > Level 1: Spellcasting |
| 7 | 3 | -5.23 |  | Classes > Level 1: Spellcasting |
| 8 | 4 | -5.26 |  | Classes > Level 1: Spellcasting |
| 9 | 5 | -7.49 |  | Spells > Forbiddance |
| 10 | 6 | -8.05 |  | Monsters > Spellcasting |

*retrieved sections:* Spells > Counterspell | Classes > Level 1: Spellcasting

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Classes > Level 1: Spellcasting]
#### Level 1: Spellcasting  
You have learned to cast spells through your bardic arts. See "Spells" for the rules on spellcasting. The information below details how you use those rules with Bard spells, which appear in the Bard spell list later in the class's description.  
_Cantrips._ You know two cantrips of your choice from the Bard spell list. _Dancing Lights_ and _Vicious Mockery_ are recommended.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

Counterspell can be cast by Sorcerer, Warlock, and Wizard classes.

Revivify can be cast by Cleric, Druid, Paladin, and Ranger classes.

*facts found (judge): 2/2; missing: none*


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 | yes | Spells > Counterspell |
| 2 | 4 | 0.75 | yes | Classes > Level 3 Paladin Spells |
| 3 | 29 | 0.26 | yes | Monsters A–Z > Reactions |
| 4 | 24 | 0.14 | yes | Monsters A–Z > Reactions |
| 5 | 3 | -0.97 | yes | Spells > Revivify |
| 6 | 18 | -1.18 | yes | Classes > Level 3: Life Domain Spells |
| 7 | 8 | -1.18 | yes | Classes > Master of Myriad Forms |
| 8 | 28 | -1.67 | yes | Classes > Level 2: Wild Shape |
| 9 | 5 | -1.99 |  | Classes > Level 1: Spellcasting |
| 10 | 11 | -2.11 |  | Classes > Mask of Many Faces |
| 11 | 2 | -2.71 |  | Spells > Counterspell |
| 12 | 9 | -3.60 |  | Classes > Armor of Shadows |
| 13 | 25 | -3.73 |  | Classes > Level 1: Spellcasting |
| 14 | 15 | -4.04 |  | Rules Glossary > Dead |
| 15 | 10 | -4.16 |  | Classes > Level 1: Spellcasting |
| 16 | 6 | -4.28 |  | Classes > Level 1: Spellcasting |
| 17 | 27 | -4.33 |  | Classes > Level 1: Spellcasting |
| 18 | 19 | -4.46 |  | Classes > Transmuted Spell |
| 19 | 20 | -4.54 |  | Classes > Level 1: Spellcasting |
| 20 | 7 | -4.66 |  | Classes > Level 1: Spellcasting |

*retrieved sections:* Spells > Counterspell | Classes > Level 3 Paladin Spells | Monsters A–Z > Reactions | Spells > Revivify | Classes > Level 3: Life Domain Spells | Classes > Master of Myriad Forms | Classes > Level 2: Wild Shape

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Classes > Level 3 Paladin Spells]
<td>Revivify</td>
<td>Necromancy</td>
<td>M</td>
</tr>
</tbody>
</table>

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The mage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Spells > Revivify]
#### Revivify  
_Level 3 Necromancy (Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S, M (a diamond worth 500+ GP, which the spell consumes)
**Duration:** Instantaneous  
You touch a creature that has died within the last 10 minutes. That creature revives with 1 Hit Point. This spell can't revive a creature that has died of old age, nor does it restore any missing body parts.

---

[Classes > Level 3: Life Domain Spells]
<td>Mass Healing Word, Revivify</td>
</tr>
<tr>
<td>7</td>
<td>Aura of Life, Death Ward</td>
</tr>
<tr>
<td>9</td>
<td>Greater Restoration, Mass Cure Wounds</td>
</tr>
</tbody>
</table>

---

[Classes > Master of Myriad Forms]
#### Master of Myriad Forms  
_Prerequisite: Level 5+ Warlock_  
You can cast _Alter Self_ without expending a spell slot.

---

[Classes > Level 2: Wild Shape]
**No Spellcasting.** You can't cast spells, but shapeshifting doesn't break your Concentration or otherwise interfere with a spell you've already cast.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

Counterspell can be cast by Sorcerer, Warlock, and Wizard classes. Revivify can be cast by Cleric, Druid, Paladin, and Ranger classes.

*facts found (judge): 2/2; missing: none*


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 16, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 | yes | Spells > Counterspell |
| 2 | 4 | 0.75 | yes | Classes > Level 3 Paladin Spells |
| 3 | 3 | -0.97 | yes | Spells > Revivify |
| 4 | 8 | -1.18 | yes | Classes > Master of Myriad Forms |
| 5 | 5 | -1.99 | yes | Classes > Level 1: Spellcasting |
| 6 | 2 | -2.71 | yes | Spells > Counterspell |
| 7 | 9 | -3.60 | yes | Classes > Armor of Shadows |
| 8 | 10 | -4.16 | yes | Classes > Level 1: Spellcasting |
| 9 | 6 | -4.28 |  | Classes > Level 1: Spellcasting |
| 10 | 7 | -4.66 |  | Classes > Level 1: Spellcasting |
| 11 | 16 | -9.31 |  | Classes > Sorcerer Spell List |
| 12 | 12 | -9.95 |  | Classes > Paladin |
| 13 | 15 | -10.20 |  | Classes > Ranger |
| 14 | 14 | -10.50 |  | Classes > Ranger |
| 15 | 13 | -10.55 |  | Classes > Paladin |
| 16 | 11 | -11.31 |  | Rules Glossary > Reaction |

*retrieved sections:* Spells > Counterspell | Classes > Level 3 Paladin Spells | Spells > Revivify | Classes > Master of Myriad Forms | Classes > Level 1: Spellcasting | Classes > Armor of Shadows

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Classes > Level 3 Paladin Spells]
<td>Revivify</td>
<td>Necromancy</td>
<td>M</td>
</tr>
</tbody>
</table>

---

[Spells > Revivify]
#### Revivify  
_Level 3 Necromancy (Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S, M (a diamond worth 500+ GP, which the spell consumes)
**Duration:** Instantaneous  
You touch a creature that has died within the last 10 minutes. That creature revives with 1 Hit Point. This spell can't revive a creature that has died of old age, nor does it restore any missing body parts.

---

[Classes > Master of Myriad Forms]
#### Master of Myriad Forms  
_Prerequisite: Level 5+ Warlock_  
You can cast _Alter Self_ without expending a spell slot.

---

[Classes > Level 1: Spellcasting]
#### Level 1: Spellcasting  
Drawing from your innate magic, you can cast spells. See "Spells" for the rules on spellcasting. The information below details how you use those rules with Sorcerer spells, which appear in the Sorcerer spell list later in the class's description.

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Classes > Armor of Shadows]
#### Armor of Shadows  
You can cast _Mage Armor_ on yourself without expending a spell slot.

---

[Classes > Level 1: Spellcasting]
#### Level 1: Spellcasting  
You have learned to cast spells through studying the mystical forces of nature. See "Spells" for the rules on spellcasting. The information below details how you use those rules with Druid spells, which appear on the Druid spell list later in the class's description.  
_Cantrips._ You know two cantrips of your choice from the Druid spell list. _Druidcraft_ and _Produce Flame_ are recommended.
```
</details>


### v6_agentic  (16 chunks, 3 LLM call(s))

Counterspell can be cast by Sorcerer, Warlock, and Wizard classes.

Revivify can be cast by Cleric, Druid, Paladin, and Ranger classes.

*facts found (judge): 2/2; missing: none*

*agentic sub-queries:* Counterspell / Revivify / classes / cast / Counterspell / cast


*re-ranking* (query: `Counterspell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.03 | yes | Spells > Counterspell |
| 2 | 1 | 4.71 | yes | Spells > Counterspell |
| 3 | 6 | 1.46 | yes | Monsters A–Z > Reactions |
| 4 | 8 | 1.36 |  | Monsters A–Z > Reactions |
| 5 | 4 | -1.50 |  | Classes > Level 3 Warlock Spells |
| 6 | 5 | -2.26 |  | Classes > Level 3 Sorcerer Spells |
| 7 | 9 | -4.03 |  | Classes > Level 7: Countercharm |
| 8 | 3 | -10.41 |  | Classes > Level 3 Wizard Spells |
| 9 | 18 | -10.56 |  | Classes > Cantrips (Level 0 Sorcerer Spells) |
| 10 | 20 | -10.69 |  | Magic Items > Spell Scroll |
| 11 | 13 | -10.72 |  | Classes > Cantrips (Level 0 Bard Spells) |
| 12 | 19 | -10.85 |  | Spells > Vicious Mockery |
| 13 | 7 | -10.86 |  | Spells > Otherworldly Steed |
| 14 | 17 | -10.86 |  | Spells > Otherworldly Steed |
| 15 | 10 | -10.89 |  | Spells > Augury |
| 16 | 11 | -10.95 |  | Spells > Slow |
| 17 | 16 | -10.98 |  | Spells > Find Steed |
| 18 | 14 | -11.04 |  | Spells > Giant Insect |
| 19 | 12 | -11.28 |  | Spells > Modify Memory |
| 20 | 15 | -11.40 |  | Spells > Combining Spell Effects |


*re-ranking* (query: `Revivify`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.38 | yes | Spells > Revivify |
| 2 | 2 | 2.59 | yes | Classes > Level 3 Paladin Spells |
| 3 | 3 | 2.14 | yes | Classes > Level 3: Life Domain Spells |
| 4 | 7 | 1.90 |  | Rules Glossary > Dead |
| 5 | 15 | 0.96 |  | Classes > Level 3 Cleric Spells |
| 6 | 16 | -0.07 |  | Classes > Level 3 Druid Spells |
| 7 | 11 | -0.26 |  | Classes > Level 3 Ranger Spells |
| 8 | 9 | -1.21 | yes | Classes > Level 3: Life Domain Spells |
| 9 | 17 | -10.17 |  | Classes > Level 7 Cleric Spells |
| 10 | 13 | -10.22 | yes | Classes > Level 3 Paladin Spells |
| 11 | 4 | -10.43 |  | Classes > Level 10: Self-Restoration |
| 12 | 6 | -10.60 |  | Spells > Reverse Gravity |
| 13 | 20 | -10.69 |  | Monsters A–Z > Bonus Actions |
| 14 | 8 | -10.81 |  | Spells > Wish |
| 15 | 19 | -10.86 |  | Monsters A–Z > Bonus Actions |
| 16 | 10 | -10.86 |  | Spells > Expeditious Retreat |
| 17 | 18 | -10.94 |  | Spells > Divine Favor |
| 18 | 12 | -11.02 |  | Feats > Alert |
| 19 | 14 | -11.10 |  | Classes > Level 20: Archdruid |
| 20 | 5 | -11.15 |  | Classes > Level 18: Superior Inspiration |


*re-ranking* (query: `classes`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 20 | 2.67 | yes | Monsters > Armor Class |
| 2 | 18 | 1.78 | yes | Classes > Level 3: Fighter Subclass |
| 3 | 13 | 0.07 | yes | Classes > Level 7: Additional Fighting Style |
| 4 | 10 | -0.03 |  | Classes > Level 3: Bonus Proficiencies |
| 5 | 15 | -0.06 |  | Classes > Fighter Subclass: Champion |
| 6 | 11 | -0.16 |  | Classes > Level 1: Spellcasting |
| 7 | 5 | -0.25 |  | Classes > Level 1: Spellcasting |
| 8 | 9 | -0.31 |  | Classes > Level 14: Intimidating Presence |
| 9 | 7 | -0.38 |  | Classes > Level 1: Spellcasting |
| 10 | 14 | -0.39 |  | Character Creation > Multiclassing |
| 11 | 3 | -0.44 |  | Classes > Level 3: Cutting Words |
| 12 | 17 | -0.51 |  | Classes > Rogue Class Features |
| 13 | 1 | -0.77 |  | Classes > Level 9: Abjure Foes |
| 14 | 2 | -0.96 |  | Classes > Level 3: Land's Aid |
| 15 | 6 | -1.41 |  | Classes > Level 10: Magical Secrets |
| 16 | 16 | -1.61 |  | Classes > Level 14: Hurl Through Hell |
| 17 | 4 | -1.71 |  | Classes > Level 17: Quivering Palm |
| 18 | 19 | -2.13 |  | Classes > Level 4 Sorcerer Spells |
| 19 | 8 | -2.53 |  | Classes > Level 6 Wizard Spells |
| 20 | 12 | -2.95 |  | Classes > Eldritch Mind |


*re-ranking* (query: `cast`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | 2.29 | yes | Spells > Casting Spells |
| 2 | 12 | 1.69 | yes | Spells > Casting without Slots |
| 3 | 6 | 1.41 | yes | Spells > Casting without Slots |
| 4 | 8 | 1.25 |  | Spells > Casting without Slots |
| 5 | 14 | 1.12 |  | Spells > Longer Casting Times |
| 6 | 16 | 1.11 |  | Spells > Contingency |
| 7 | 4 | 0.40 |  | Magic Items > Spells Cast from Items |
| 8 | 18 | 0.17 |  | Character Creation > Spellcasting |
| 9 | 20 | -1.24 |  | Magic Items > Helm of Telepathy |
| 10 | 10 | -1.31 |  | Classes > Level 2: Wild Shape |
| 11 | 1 | -1.37 |  | Classes > Fiendish Vigor |
| 12 | 11 | -1.70 |  | Monsters A–Z > Bonus Actions |
| 13 | 15 | -2.01 |  | Monsters A–Z > Bonus Actions |
| 14 | 9 | -2.58 |  | Character Creation > Spellcasting |
| 15 | 5 | -2.65 |  | Monsters A–Z > Bonus Actions |
| 16 | 13 | -2.73 |  | Character Creation > Spellcasting |
| 17 | 17 | -3.07 |  | Monsters A–Z > Bonus Actions |
| 18 | 3 | -3.09 |  | Monsters A–Z > Bonus Actions |
| 19 | 2 | -3.70 |  | Classes > Misty Visions |
| 20 | 19 | -10.23 |  | Character Creation > Spellcasting |


*re-ranking* (query: `Counterspell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.03 | yes | Spells > Counterspell |
| 2 | 1 | 4.71 | yes | Spells > Counterspell |
| 3 | 6 | 1.46 | yes | Monsters A–Z > Reactions |
| 4 | 8 | 1.36 |  | Monsters A–Z > Reactions |
| 5 | 4 | -1.50 |  | Classes > Level 3 Warlock Spells |
| 6 | 5 | -2.26 |  | Classes > Level 3 Sorcerer Spells |
| 7 | 9 | -4.03 |  | Classes > Level 7: Countercharm |
| 8 | 3 | -10.41 |  | Classes > Level 3 Wizard Spells |
| 9 | 18 | -10.56 |  | Classes > Cantrips (Level 0 Sorcerer Spells) |
| 10 | 20 | -10.69 |  | Magic Items > Spell Scroll |
| 11 | 13 | -10.72 |  | Classes > Cantrips (Level 0 Bard Spells) |
| 12 | 19 | -10.85 |  | Spells > Vicious Mockery |
| 13 | 7 | -10.86 |  | Spells > Otherworldly Steed |
| 14 | 17 | -10.86 |  | Spells > Otherworldly Steed |
| 15 | 10 | -10.89 |  | Spells > Augury |
| 16 | 11 | -10.95 |  | Spells > Slow |
| 17 | 16 | -10.98 |  | Spells > Find Steed |
| 18 | 14 | -11.04 |  | Spells > Giant Insect |
| 19 | 12 | -11.28 |  | Spells > Modify Memory |
| 20 | 15 | -11.40 |  | Spells > Combining Spell Effects |


*re-ranking* (query: `cast`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | 2.29 | yes | Spells > Casting Spells |
| 2 | 12 | 1.69 | yes | Spells > Casting without Slots |
| 3 | 6 | 1.41 | yes | Spells > Casting without Slots |
| 4 | 8 | 1.25 |  | Spells > Casting without Slots |
| 5 | 14 | 1.12 |  | Spells > Longer Casting Times |
| 6 | 16 | 1.11 |  | Spells > Contingency |
| 7 | 4 | 0.40 |  | Magic Items > Spells Cast from Items |
| 8 | 18 | 0.17 |  | Character Creation > Spellcasting |
| 9 | 20 | -1.24 |  | Magic Items > Helm of Telepathy |
| 10 | 10 | -1.31 |  | Classes > Level 2: Wild Shape |
| 11 | 1 | -1.37 |  | Classes > Fiendish Vigor |
| 12 | 11 | -1.70 |  | Monsters A–Z > Bonus Actions |
| 13 | 15 | -2.01 |  | Monsters A–Z > Bonus Actions |
| 14 | 9 | -2.58 |  | Character Creation > Spellcasting |
| 15 | 5 | -2.65 |  | Monsters A–Z > Bonus Actions |
| 16 | 13 | -2.73 |  | Character Creation > Spellcasting |
| 17 | 17 | -3.07 |  | Monsters A–Z > Bonus Actions |
| 18 | 3 | -3.09 |  | Monsters A–Z > Bonus Actions |
| 19 | 2 | -3.70 |  | Classes > Misty Visions |
| 20 | 19 | -10.23 |  | Character Creation > Spellcasting |


*re-ranking* (query: `paladin spells at level 3`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 7.14 | yes | Classes > Level 3: Oath of Devotion Spells |
| 2 | 10 | 7.10 | yes | Classes > Level 3 Paladin Spells |
| 3 | 1 | 7.03 | yes | Classes > Level 3 Paladin Spells |
| 4 | 11 | 5.48 |  | Classes > Level 3: Paladin Subclass |
| 5 | 4 | 5.22 |  | Classes > Level 1: Spellcasting |
| 6 | 17 | 5.09 |  | Classes > Level 3: Channel Divinity |
| 7 | 16 | 4.91 |  | Classes > Level 3: Channel Divinity |
| 8 | 3 | 4.84 |  | Classes > Level 1: Spellcasting |
| 9 | 20 | 4.58 |  | Classes > Level 2 Paladin Spells |
| 10 | 7 | 4.34 |  | Classes > Level 1: Spellcasting |
| 11 | 15 | 4.26 |  | Classes > Level 4 Paladin Spells |
| 12 | 9 | 4.16 |  | Classes > Level 1: Spellcasting |
| 13 | 18 | 4.02 |  | Classes > Level 1 Paladin Spells |
| 14 | 5 | 4.01 |  | Classes > Level 1: Spellcasting |
| 15 | 6 | 3.86 |  | Classes > Paladin Class Features |
| 16 | 14 | 3.86 |  | Classes > Level 5 Paladin Spells |
| 17 | 8 | 3.74 |  | Classes > Level 1: Spellcasting |
| 18 | 12 | 3.66 |  | Classes > Level 1 Paladin Spells |
| 19 | 19 | 3.05 |  | Spells > Zone of Truth |
| 20 | 13 | 2.95 |  | Classes > Paladin Spell List |


*re-ranking* (query: `cleric spells at level 3`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 7.61 | yes | Classes > Level 3: Life Domain Spells |
| 2 | 10 | 7.29 | yes | Classes > Level 3 Cleric Spells |
| 3 | 1 | 7.26 |  | Classes > Level 1: Spellcasting |
| 4 | 16 | 6.18 |  | Spells > Dispel Magic |
| 5 | 15 | 5.97 |  | Spells > Sending |
| 6 | 19 | 5.63 |  | Spells > Water Walk |
| 7 | 4 | 5.28 |  | Classes > Level 1: Spellcasting |
| 8 | 20 | 5.24 |  | Spells > Remove Curse |
| 9 | 11 | 5.13 |  | Classes > Level 3: Cleric Subclass |
| 10 | 5 | 5.03 |  | Classes > Level 1: Spellcasting |
| 11 | 7 | 4.78 |  | Classes > Level 2: Fighting Style |
| 12 | 9 | 4.10 |  | Classes > Level 1: Spellcasting |
| 13 | 8 | 3.77 |  | Classes > Level 1: Spellcasting |
| 14 | 13 | 3.30 |  | Classes > Cantrips (Level 0 Cleric Spells) |
| 15 | 12 | 3.27 |  | Classes > Cleric Spell List |
| 16 | 3 | 3.20 |  | Classes > Level 1: Spellcasting |
| 17 | 6 | 2.95 |  | Classes > Cleric Class Features |
| 18 | 17 | 2.73 |  | Classes > Level 20: Signature Spells |
| 19 | 14 | 2.35 |  | Spells > Divine Word |
| 20 | 18 | 2.19 |  | Classes > As a Multiclass Character |


*re-ranking* (query: `druid spells at level 3`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | 7.24 |  | Classes > Level 3: Circle of the Land Spells |
| 2 | 2 | 6.98 |  | Classes > Level 1: Spellcasting |
| 3 | 12 | 6.84 |  | Classes > Level 3 Druid Spells |
| 4 | 1 | 6.71 |  | Classes > Level 3 Druid Spells |
| 5 | 20 | 6.17 |  | Spells > Dispel Magic |
| 6 | 17 | 5.59 |  | Classes > Level 3: Circle of the Land Spells |
| 7 | 18 | 5.49 |  | Spells > Call Lightning |
| 8 | 16 | 5.18 |  | Classes > Level 3: Druid Subclass |
| 9 | 11 | 5.17 |  | Classes > Level 3: Land's Aid |
| 10 | 15 | 4.79 |  | Classes > Level 6: Natural Recovery |
| 11 | 9 | 4.31 |  | Classes > Level 1: Spellcasting |
| 12 | 8 | 4.23 |  | Classes > Level 1: Spellcasting |
| 13 | 3 | 3.55 |  | Classes > Level 1: Spellcasting |
| 14 | 6 | 3.13 |  | Classes > Level 1: Spellcasting |
| 15 | 14 | 3.05 |  | Classes > Level 9 Druid Spells |
| 16 | 4 | 2.94 |  | Classes > Level 7 Druid Spells |
| 17 | 19 | 2.62 |  | Classes > Level 5 Druid Spells |
| 18 | 13 | 2.34 |  | Classes > Druid Spell List |
| 19 | 5 | 2.34 |  | Classes > Level 1: Spellcasting |
| 20 | 10 | 1.89 |  | Classes > Druid Class Features |


*re-ranking* (query: `ranger spells at level 3`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 7.52 |  | Character Creation > Spellcasting |
| 2 | 12 | 7.46 |  | Classes > Level 3 Ranger Spells |
| 3 | 8 | 6.24 |  | Character Creation > Spellcasting |
| 4 | 1 | 4.94 |  | Classes > Level 1: Spellcasting |
| 5 | 17 | 4.74 |  | Classes > Level 2 Ranger Spells |
| 6 | 20 | 4.64 |  | Classes > Level 3: Ranger Subclass |
| 7 | 13 | 4.57 |  | Classes > Level 4 Ranger Spells |
| 8 | 15 | 4.14 |  | Classes > Level 1 Ranger Spells |
| 9 | 7 | 4.00 |  | Classes > Level 1: Spellcasting |
| 10 | 5 | 3.91 |  | Classes > Level 1: Spellcasting |
| 11 | 11 | 3.90 |  | Classes > Level 5 Ranger Spells |
| 12 | 3 | 3.75 |  | Classes > Level 1: Spellcasting |
| 13 | 2 | 3.53 |  | Classes > Ranger Class Features |
| 14 | 10 | 3.44 |  | Classes > Level 1 Ranger Spells |
| 15 | 9 | 3.18 |  | Classes > Ranger Spell List |
| 16 | 6 | 3.02 |  | Classes > Level 1: Spellcasting |
| 17 | 14 | 2.80 |  | Spells > Ensnaring Strike |
| 18 | 18 | 2.69 |  | Spells > Silence |
| 19 | 16 | 2.40 |  | Spells > Tree Stride |
| 20 | 19 | 2.25 |  | Character Creation > Tier 3 (Levels 11–16) |

*retrieved sections:* Spells > Counterspell | Monsters A–Z > Reactions | Spells > Revivify | Classes > Level 3 Paladin Spells | Classes > Level 3: Life Domain Spells | Monsters > Armor Class | Classes > Level 3: Fighter Subclass | Classes > Level 7: Additional Fighting Style | Spells > Casting Spells | Spells > Casting without Slots | Classes > Level 3: Oath of Devotion Spells | Classes > Level 3 Cleric Spells

<details><summary>full retrieved context</summary>

```
[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Spells > Revivify]
#### Revivify  
_Level 3 Necromancy (Cleric, Druid, Paladin, Ranger)_  
**Casting Time:** Action
**Range:** Touch
**Components:** V, S, M (a diamond worth 500+ GP, which the spell consumes)
**Duration:** Instantaneous  
You touch a creature that has died within the last 10 minutes. That creature revives with 1 Hit Point. This spell can't revive a creature that has died of old age, nor does it restore any missing body parts.

---

[Classes > Level 3 Paladin Spells]
<td>Revivify</td>
<td>Necromancy</td>
<td>M</td>
</tr>
</tbody>
</table>

---

[Classes > Level 3: Life Domain Spells]
<td>Mass Healing Word, Revivify</td>
</tr>
<tr>
<td>7</td>
<td>Aura of Life, Death Ward</td>
</tr>
<tr>
<td>9</td>
<td>Greater Restoration, Mass Cure Wounds</td>
</tr>
</tbody>
</table>

---

[Monsters > Armor Class]
### Armor Class  
A monster's Armor Class (AC) includes its natural armor, Dexterity, gear, and other defenses. See "Playing the Game" for information on Armor Class.

---

[Classes > Level 3: Fighter Subclass]
#### Level 3: Fighter Subclass  
You gain a Fighter subclass of your choice. The Champion subclass is detailed after this class's description. A subclass is a specialization that grants you features at certain Fighter levels. For the rest of your career, you gain each of your subclass's features that are of your Fighter level or lower.

---

[Classes > Level 7: Additional Fighting Style]
#### Level 7: Additional Fighting Style  
You gain another Fighting Style feat of your choice.

---

[Spells > Casting Spells]
## Casting Spells  
Each spell description has a series of entries that provide the details needed to cast the spell. The following sections explain each of those entries, which follow a spell's name.  
> **Casting in Armor**
>
> You must have training with any armor you are wearing to cast spells while wearing it. You are otherwise too hampered by the armor for spellcasting.

---

[Spells > Casting without Slots]
**Special Abilities.** Some characters and monsters have special abilities that allow them to cast specific spells without a spell slot. This casting is usually limited in another way, such as being able to cast the spell a limited number of times per day.  
**Magic Items.** _Spell Scrolls_ and some other magic items contain spells that can be cast without a spell slot. The description of such an item specifies how many times a spell can be cast from it.

---

[Spells > Casting without Slots]
**Rituals.** Certain spells have the Ritual tag in the Casting Time entry. Such a spell can be cast following the normal rules for spellcasting, or it can be cast as a Ritual. The Ritual version of a spell takes 10 minutes longer to cast than normal, but it doesn't expend a spell slot. To cast a spell as a Ritual, a spellcaster must have it prepared.

---

[Classes > Level 3: Oath of Devotion Spells]
#### Level 3: Oath of Devotion Spells  
The magic of your oath ensures you always have certain spells ready; when you reach a Paladin level specified in the Oath of Devotion Spells table, you thereafter always have the listed spells prepared.  
**Oath of Devotion Spells**  
<table>
<thead>
<tr>
<th>Paladin Level</th>
<th>Spells</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>Protection from Evil and Good, Shield of Faith</td>
</tr>
<tr>
<td>5</td>
<td>Aid, Zone of Truth</td>
</tr>
<tr>

---

[Classes > Level 3 Paladin Spells]
#### Level 3 Paladin Spells  
<table>
<thead>
<tr>
<th>Spell</th>
<th>School</th>
<th>Special</th>
</tr>
</thead>
<tbody>
<tr>
<td>Create Food and Water</td>
<td>Conjuration</td>
<td>—</td>
</tr>
<tr>
<td>Daylight</td>
<td>Evocation</td>
<td>—</td>
</tr>
<tr>
<td>Dispel Magic</td>
<td>Abjuration</td>
<td>—</td>
</tr>
<tr>
<td>Magic Circle</td>
<td>Abjuration</td>
<td>M</td>
</tr>
<tr>
<td>Remove Curse</td>
<td>Abjuration</td>
<td>—</td>
</tr>
<tr>
<td>Revivify</td>
<td>Necromancy</td>
<td>M</td>

---

[Classes > Level 3: Life Domain Spells]
#### Level 3: Life Domain Spells  
Your connection to this divine domain ensures you always have certain spells ready. When you reach a Cleric level specified in the Life Domain Spells table, you thereafter always have the listed spells prepared.  
**Life Domain Spells**  
<table>
<thead>
<tr>
<th>Cleric Level</th>
<th>Prepared Spells</th>
</tr>
</thead>
<tbody>
<tr>
<td>3</td>
<td>Aid, Bless, Cure Wounds, Lesser Restoration</td>
</tr>
<tr>
<td>5</td>
<td>Mass Healing Word, Revivify</td>
</tr>

---

[Classes > Level 3 Cleric Spells]
#### Level 3 Cleric Spells  
<table>
<thead>
<tr>
<th>Spell</th>
<th>School</th>
<th>Special</th>
</tr>
</thead>
<tbody>
<tr>
<td>Animate Dead</td>
<td>Necromancy</td>
<td>—</td>
</tr>
<tr>
<td>Beacon of Hope</td>
<td>Abjuration</td>
<td>C</td>
</tr>
<tr>
<td>Bestow Curse</td>
<td>Necromancy</td>
<td>C</td>
</tr>
<tr>
<td>Clairvoyance</td>
<td>Divination</td>
<td>C, M</td>
</tr>
<tr>
<td>Create Food and Water</td>
<td>Conjuration</td>
<td>—</td>
</tr>
<tr>
<td>Daylight</td>
<td>Evocation</td>
```
</details>


---

## q21 (multi-topic) Answer all three: (1) What is the minimum length of a Long Rest? (2) How many pounds can a Bag of Holding hold? (3) What damage does Fireball deal?

**Gold facts (counterfactual data):** at least 10 hours; 800 pounds; 9d6


### v0_closed_book  (0 chunks, 1 LLM call(s))

(1) The minimum length of a Long Rest is 8 hours.
(2) A Bag of Holding can hold an unlimited amount of weight, but it cannot exceed its volume capacity.
(3) A Fireball spell deals 8d6 fire damage.

*facts found (judge): 0/3; missing: at least 10 hours; 800 pounds; 9d6*


### v1_baseline  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the minimum length of a Long Rest or how many pounds a Bag of Holding can hold. Therefore, these parts of the question cannot be answered based on the given information.

Regarding the Fireball spell, it deals 8d6 Fire damage when cast using a 3rd-level spell slot. Each level above 3 increases the damage by 1d6. So, for example, casting Fireball with a 4th-level slot would deal 9d6 Fire damage.

*facts found (judge): 1/3; missing: at least 10 hours; 800 pounds*

*retrieved sections:* Spells > Fireball | Magic Items > Staff of Fire | Spells > Flaming Sphere

<details><summary>full retrieved context</summary>

```
[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Magic Items > Staff of Fire]
<th>Charge Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>*Burning Hands*</td>
<td>1</td>
<td>*Wall of Fire*</td>
<td>4</td>
</tr>
<tr>
<td>*Fireball*</td>
<td>3</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>  
_Regaining Charges._ The staff regains 1d6 + 4 expended charges daily at dawn. If you expend the last charge, roll 1d20. On a 1, the staff crumbles into cinders and is destroyed.

---

[Spells > Flaming Sphere]
**Duration:** Concentration, up to 1 minute  
You create a 5-foot-diameter sphere of fire in an unoccupied space on the ground within range. It lasts for the duration. Any creature that ends its turn within 5 feet of the sphere makes a Dexterity saving throw, taking 2d6 Fire damage on a failed save or half as much damage on a successful one.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the minimum length of a Long Rest or the damage dealt by Fireball. These details are missing from the given information.

*facts found (judge): 0/3; missing: at least 10 hours; 800 pounds; 9d6*


*re-ranking* (query: `Answer all three: (1) What is the minimum length of a Long Rest? (2) How many po`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | -1.11 | yes | Magic Items > Bag of Holding |
| 2 | 8 | -6.56 | yes | Equipment > Basket (4 SP) |
| 3 | 6 | -8.95 | yes | Rules Glossary > Carrying Capacity |
| 4 | 10 | -10.02 |  | Rules Glossary > Carrying Capacity |
| 5 | 7 | -10.29 |  | Monsters A–Z > Actions |
| 6 | 1 | -10.72 |  | Spells > Fireball |
| 7 | 3 | -10.91 |  | Spells > Flaming Sphere |
| 8 | 4 | -10.95 |  | Monsters A–Z > Traits |
| 9 | 9 | -11.06 |  | Spells > Delayed Blast Fireball |
| 10 | 2 | -11.18 |  | Magic Items > Staff of Fire |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Basket (4 SP) | Rules Glossary > Carrying Capacity

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Basket (4 SP)]
#### Basket (4 SP)  
A Basket holds up to 40 pounds within 2 cubic feet.

---

[Rules Glossary > Carrying Capacity]
#### Carrying Capacity  
Your size and Strength score determine the maximum weight in pounds that you can carry, as shown in the Carrying Capacity table. The table also shows the maximum weight you can drag, lift, or push.  
While dragging, lifting, or pushing weight in excess of the maximum weight you can carry, your Speed can be no more than 5 feet.  
**Carrying Capacity**  
<table>
<thead>
<tr>
<th>Creature Size</th>
<th>Carry</th>
<th>Drag/Lift/Push</th>
</tr>
</thead>
<tbody>
<tr>
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The context provided does not contain information about the minimum length of a Long Rest, so that part of the question cannot be answered based on the given information. 

A Bag of Holding can hold up to 800 pounds.

Fireball deals 3d6 Fire damage.

*facts found (judge): 1/3; missing: at least 10 hours; 9d6*


*re-ranking* (query: `Answer all three: (1) What is the minimum length of a Long Rest? (2) How many po`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | -1.11 | yes | Magic Items > Bag of Holding |
| 2 | 8 | -6.56 | yes | Equipment > Basket (4 SP) |
| 3 | 6 | -8.95 | yes | Rules Glossary > Carrying Capacity |
| 4 | 10 | -10.02 | yes | Rules Glossary > Carrying Capacity |
| 5 | 7 | -10.29 | yes | Monsters A–Z > Actions |
| 6 | 1 | -10.72 | yes | Spells > Fireball |
| 7 | 3 | -10.91 | yes | Spells > Flaming Sphere |
| 8 | 4 | -10.95 | yes | Monsters A–Z > Traits |
| 9 | 9 | -11.06 |  | Spells > Delayed Blast Fireball |
| 10 | 2 | -11.18 |  | Magic Items > Staff of Fire |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Basket (4 SP) | Rules Glossary > Carrying Capacity | Monsters A–Z > Actions | Spells > Fireball | Spells > Flaming Sphere | Monsters A–Z > Traits

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Basket (4 SP)]
#### Basket (4 SP)  
A Basket holds up to 40 pounds within 2 cubic feet.

---

[Rules Glossary > Carrying Capacity]
#### Carrying Capacity  
Your size and Strength score determine the maximum weight in pounds that you can carry, as shown in the Carrying Capacity table. The table also shows the maximum weight you can drag, lift, or push.  
While dragging, lifting, or pushing weight in excess of the maximum weight you can carry, your Speed can be no more than 5 feet.  
**Carrying Capacity**  
<table>
<thead>
<tr>
<th>Creature Size</th>
<th>Carry</th>
<th>Drag/Lift/Push</th>
</tr>
</thead>
<tbody>
<tr>

---

[Rules Glossary > Carrying Capacity]
</tr>
</thead>
<tbody>
<tr>
<td>Tiny</td>
<td>Str. × 7.5 lb.</td>
<td>Str. × 15 lb.</td>
</tr>
<tr>
<td>Small/Medium</td>
<td>Str. × 15 lb.</td>
<td>Str. × 30 lb.</td>
</tr>
<tr>
<td>Large</td>
<td>Str. × 30 lb.</td>
<td>Str. × 60 lb.</td>
</tr>
<tr>
<td>Huge</td>
<td>Str. × 60 lb.</td>
<td>Str. × 120 lb.</td>
</tr>
<tr>
<td>Gargantuan</td>
<td>Str. × 120 lb.</td>
<td>Str. × 240 lb.</td>
</tr>
</tbody>
</table>

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Claw._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 3 (1d4 + 1) Slashing damage plus 3 (1d6) Fire damage.  
**_Fire Breath (Recharge 6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 15-foot Cone. _Failure:_ 7 (2d6) Fire damage. _Success:_ Half damage.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Spells > Flaming Sphere]
**Duration:** Concentration, up to 1 minute  
You create a 5-foot-diameter sphere of fire in an unoccupied space on the ground within range. It lasts for the duration. Any creature that ends its turn within 5 feet of the sphere makes a Dexterity saving throw, taking 2d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Fire Aura._** At the end of each of the salamander's turns, each creature of the salamander's choice in a 5-foot Emanation originating from the salamander takes 7 (2d6) Fire damage.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The context provided does not contain information about the minimum length of a Long Rest or the damage dealt by Fireball. These details are missing from the given information.

*facts found (judge): 0/3; missing: at least 10 hours; 800 pounds; 9d6*


*re-ranking* (query: `Answer all three: (1) What is the minimum length of a Long Rest? (2) How many po`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | -1.11 | yes | Magic Items > Bag of Holding |
| 2 | 5 | -6.56 | yes | Equipment > Basket (4 SP) |
| 3 | 3 | -8.95 | yes | Rules Glossary > Carrying Capacity |
| 4 | 6 | -10.02 |  | Rules Glossary > Carrying Capacity |
| 5 | 4 | -10.29 |  | Monsters A–Z > Actions |
| 6 | 7 | -10.81 |  | Magic Items > Necklace of Fireballs |
| 7 | 9 | -10.90 |  | Playing the Game > Carrying Objects |
| 8 | 8 | -10.91 |  | Monsters A–Z > Actions |
| 9 | 10 | -11.15 |  | Magic Items > Staff of Power |
| 10 | 1 | -11.18 |  | Magic Items > Staff of Fire |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Basket (4 SP) | Rules Glossary > Carrying Capacity

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Basket (4 SP)]
#### Basket (4 SP)  
A Basket holds up to 40 pounds within 2 cubic feet.

---

[Rules Glossary > Carrying Capacity]
#### Carrying Capacity  
Your size and Strength score determine the maximum weight in pounds that you can carry, as shown in the Carrying Capacity table. The table also shows the maximum weight you can drag, lift, or push.  
While dragging, lifting, or pushing weight in excess of the maximum weight you can carry, your Speed can be no more than 5 feet.  
**Carrying Capacity**  
<table>
<thead>
<tr>
<th>Creature Size</th>
<th>Carry</th>
<th>Drag/Lift/Push</th>
</tr>
</thead>
<tbody>
<tr>
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

(1) The minimum length of a Long Rest is not explicitly stated in the provided context. It is implied to be at least 1 hour since a Long Rest can be interrupted after at least 1 hour of rest with certain activities.

(2) A Bag of Holding can hold up to 800 pounds.

(3) The damage dealt by Fireball is not mentioned in the provided context.

*facts found (judge): 1/3; missing: at least 10 hours; 9d6*


*re-ranking* (query: `Answer all three: (1) What is the minimum length of a Long Rest? (2) How many po`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.11 | yes | Magic Items > Bag of Holding |
| 2 | 26 | -5.32 | yes | Equipment > Sack (1 CP) |
| 3 | 14 | -5.39 | yes | Magic Items > Rope of Climbing |
| 4 | 3 | -6.49 | yes | Magic Items > Efficient Quiver |
| 5 | 15 | -6.56 | yes | Equipment > Basket (4 SP) |
| 6 | 5 | -7.00 | yes | Rules Glossary > Long Rest |
| 7 | 8 | -7.30 | yes | Rules Glossary > Long Rest |
| 8 | 22 | -8.24 | yes | Magic Items > Bag of Beans |
| 9 | 18 | -8.55 |  | Magic Items > Rod of Lordly Might |
| 10 | 4 | -8.77 |  | Rules Glossary > Short Rest |
| 11 | 11 | -8.95 |  | Rules Glossary > Carrying Capacity |
| 12 | 12 | -9.54 |  | Monsters A–Z > Traits |
| 13 | 17 | -10.02 |  | Rules Glossary > Carrying Capacity |
| 14 | 20 | -10.20 |  | Classes > Level 1: Pact Magic |
| 15 | 13 | -10.29 |  | Monsters A–Z > Actions |
| 16 | 25 | -10.40 |  | Classes > Level 1: Spellcasting |
| 17 | 16 | -10.73 |  | Magic Items > Bag of Tricks |
| 18 | 24 | -10.76 |  | Classes > Level 1: Spellcasting |
| 19 | 27 | -10.79 |  | Classes > Level 1: Spellcasting |
| 20 | 19 | -10.81 |  | Magic Items > Necklace of Fireballs |

*retrieved sections:* Magic Items > Bag of Holding | Equipment > Sack (1 CP) | Magic Items > Rope of Climbing | Magic Items > Efficient Quiver | Equipment > Basket (4 SP) | Rules Glossary > Long Rest | Magic Items > Bag of Beans

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Equipment > Sack (1 CP)]
#### Sack (1 CP)  
A Sack holds up to 30 pounds within 1 cubic foot.

---

[Magic Items > Rope of Climbing]
This 60-foot length of rope can hold up to 3,000 pounds. While holding one end of the rope, you can take a Magic action to command the other end of the rope to animate and move toward a destination you choose, up to the rope's length away from you. That end moves 10 feet on your turn when you first command it and 10 feet at the start of each of your subsequent turns until reaching its destination or until you tell it to stop. You can also tell the rope to fasten itself securely to an object or

---

[Magic Items > Efficient Quiver]
#### Efficient Quiver  
_Wondrous Item, Uncommon_  
Each of the quiver's three compartments connects to an extradimensional space that allows the quiver to hold numerous items while never weighing more than 2 pounds. The shortest compartment can hold up to 60 Arrows, Bolts, or similar objects. The midsize compartment holds up to 18 Javelins or similar objects. The longest compartment holds up to 6 long objects, such as bows, Quarterstaffs, or Spears.

---

[Equipment > Basket (4 SP)]
#### Basket (4 SP)  
A Basket holds up to 40 pounds within 2 cubic feet.

---

[Rules Glossary > Long Rest]
_Benefits of the Rest._ To start a Long Rest, you must have at least 1 Hit Point. When you finish the rest, you gain the following benefits:  
**Regain All HP.** You regain all lost Hit Points and all spent Hit Point Dice. If your Hit Point maximum was reduced, it returns to normal.  
**Ability Scores Restored.** If any of your ability scores were reduced, they return to normal.  
**Exhaustion Reduced.** If you have the Exhaustion condition, its level decreases by 1.

---

[Rules Glossary > Long Rest]
**Special Feature.** Some features are recharged by a Long Rest. If you have such a feature, it recharges in the way specified in its description.  
_Interrupting the Rest._ A Long Rest is stopped by the following interruptions:  
- Rolling Initiative
- Casting a spell other than a cantrip
- Taking any damage
- 1 hour of walking or other physical exertion  
If you rested at least 1 hour before the interruption, you gain the benefits of a Short Rest. _See also_ "Short Rest."

---

[Magic Items > Bag of Beans]
#### Bag of Beans  
_Wondrous Item, Rare_  
This heavy cloth bag contains 3d4 dry beans when found. The bag weighs half a pound regardless of how many beans it contains and becomes a non-magical item when it no longer contains any beans.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

(1) The minimum length of a Long Rest is not explicitly stated in the provided context, so this part is missing.
(2) A Bag of Holding can hold up to 800 pounds.
(3) The context provided does not contain information about the damage dealt by a Fireball spell, so this part is missing.

*facts found (judge): 1/3; missing: at least 10 hours; 9d6*


*re-ranking* (query: `Answer all three: (1) What is the minimum length of a Long Rest? (2) How many po`): candidate pool of 24, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.11 | yes | Magic Items > Bag of Holding |
| 2 | 3 | -6.49 | yes | Magic Items > Efficient Quiver |
| 3 | 11 | -6.78 | yes | Magic Items > Bag of Holding |
| 4 | 5 | -7.00 | yes | Rules Glossary > Long Rest |
| 5 | 8 | -7.30 | yes | Rules Glossary > Long Rest |
| 6 | 12 | -8.46 | yes | Magic Items > Bag of Holding |
| 7 | 4 | -8.77 | yes | Rules Glossary > Short Rest |
| 8 | 17 | -8.91 | yes | Rules Glossary > Exhaustion [Condition] |
| 9 | 13 | -10.72 |  | Spells > Fireball |
| 10 | 21 | -10.72 |  | Spells > Cone of Cold |
| 11 | 7 | -10.93 |  | Magic Items > Staff of Fire |
| 12 | 6 | -11.03 |  | Magic Items > Wand of Fireballs |
| 13 | 16 | -11.09 |  | Playing the Game > Ability Scores |
| 14 | 14 | -11.09 |  | Spells > Fireball |
| 15 | 18 | -11.10 |  | Rules Glossary > Exhaustion [Condition] |
| 16 | 2 | -11.15 |  | Magic Items > Staff of Power |
| 17 | 15 | -11.16 |  | Playing the Game > Ability Scores |
| 18 | 9 | -11.18 |  | Magic Items > Staff of Fire |
| 19 | 10 | -11.20 |  | Spells > Effects |
| 20 | 20 | -11.21 |  | Magic Items > Charges |

*retrieved sections:* Magic Items > Bag of Holding | Magic Items > Efficient Quiver | Rules Glossary > Long Rest | Rules Glossary > Short Rest | Rules Glossary > Exhaustion [Condition]

<details><summary>full retrieved context</summary>

```
[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Magic Items > Efficient Quiver]
#### Efficient Quiver  
_Wondrous Item, Uncommon_  
Each of the quiver's three compartments connects to an extradimensional space that allows the quiver to hold numerous items while never weighing more than 2 pounds. The shortest compartment can hold up to 60 Arrows, Bolts, or similar objects. The midsize compartment holds up to 18 Javelins or similar objects. The longest compartment holds up to 6 long objects, such as bows, Quarterstaffs, or Spears.

---

[Magic Items > Bag of Holding]
If the bag is overloaded, pierced, or torn, it is destroyed, and its contents are scattered in the Astral Plane. If the bag is turned inside out, its contents spill forth unharmed, but the bag must be put right before it can be used again. The bag holds enough air for 10 minutes of breathing, divided by the number of breathing creatures inside.

---

[Rules Glossary > Long Rest]
_Benefits of the Rest._ To start a Long Rest, you must have at least 1 Hit Point. When you finish the rest, you gain the following benefits:  
**Regain All HP.** You regain all lost Hit Points and all spent Hit Point Dice. If your Hit Point maximum was reduced, it returns to normal.  
**Ability Scores Restored.** If any of your ability scores were reduced, they return to normal.  
**Exhaustion Reduced.** If you have the Exhaustion condition, its level decreases by 1.

---

[Rules Glossary > Long Rest]
**Special Feature.** Some features are recharged by a Long Rest. If you have such a feature, it recharges in the way specified in its description.  
_Interrupting the Rest._ A Long Rest is stopped by the following interruptions:  
- Rolling Initiative
- Casting a spell other than a cantrip
- Taking any damage
- 1 hour of walking or other physical exertion  
If you rested at least 1 hour before the interruption, you gain the benefits of a Short Rest. _See also_ "Short Rest."

---

[Magic Items > Bag of Holding]
Placing a _Bag of Holding_ inside an extradimensional space created by a _Handy Haversack_, _Portable Hole_, or similar item instantly destroys both items and opens a gate to the Astral Plane. The gate originates where the one item was placed inside the other. Any creature within a 10-foot-radius Sphere centered on the gate is sucked through it to a random location on the Astral Plane. The gate then closes. The gate is one-way and can't be reopened.

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Rules Glossary > Exhaustion [Condition]]
_Removing Exhaustion Levels._ Finishing a Long Rest removes 1 of your Exhaustion levels. When your Exhaustion level reaches 0, the condition ends.
```
</details>


### v6_agentic  (9 chunks, 3 LLM call(s))

(1) The minimum length of a Long Rest is 10 hours.
(2) A Bag of Holding can hold up to 800 pounds.
(3) Fireball deals 9d6 Fire damage on a failed saving throw, or half as much on a successful one.

*facts found (judge): 3/3; missing: none*

*agentic sub-queries:* long rest duration / bag of holding weight capacity / fireball damage


*re-ranking* (query: `long rest duration`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.64 | yes | Rules Glossary > Long Rest |
| 2 | 2 | 4.54 | yes | Rules Glossary > Long Rest |
| 3 | 4 | 3.20 | yes | Rules Glossary > Long Rest |
| 4 | 18 | 2.67 |  | Rules Glossary > Short Rest |
| 5 | 3 | 2.61 |  | Playing the Game > Duration |
| 6 | 5 | 1.84 |  | Rules Glossary > Long Rest |
| 7 | 13 | 1.18 |  | Gameplay Toolbox > Rest and Recuperation |
| 8 | 12 | 0.75 |  | Character Origins > Elf |
| 9 | 7 | 0.50 |  | Spells > Prayer of Healing |
| 10 | 6 | -0.06 |  | Playing the Game > Hit Points |
| 11 | 16 | -0.24 |  | Spells > Augury |
| 12 | 10 | -0.42 |  | Character Origins > Goliath |
| 13 | 9 | -0.59 |  | Spells > Spell Slots |
| 14 | 15 | -0.75 |  | Spells > Divination |
| 15 | 20 | -1.14 |  | Monsters > Limited Usage |
| 16 | 8 | -1.60 |  | Rules Glossary > Exhaustion [Condition] |
| 17 | 19 | -1.88 |  | Spells > Preparing Spells |
| 18 | 14 | -2.04 |  | Spells > Resurrection |
| 19 | 11 | -2.88 |  | Rules Glossary > Per Day |
| 20 | 17 | -3.54 |  | Character Origins > Orc |


*re-ranking* (query: `bag of holding weight capacity`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.02 | yes | Magic Items > Bag of Holding |
| 2 | 5 | -0.94 | yes | Magic Items > Bag of Holding |
| 3 | 3 | -2.26 | yes | Rules Glossary > Carrying Capacity |
| 4 | 20 | -2.76 |  | Magic Items > Handy Haversack |
| 5 | 12 | -3.39 |  | Magic Items > Bag of Holding |
| 6 | 4 | -4.65 |  | Magic Items > Bag of Devouring |
| 7 | 10 | -5.47 |  | Magic Items > Bag of Devouring |
| 8 | 6 | -6.55 |  | Magic Items > Bag of Beans |
| 9 | 2 | -7.01 |  | Playing the Game > Carrying Objects |
| 10 | 19 | -7.10 |  | Equipment > Other Tools |
| 11 | 11 | -7.58 |  | Magic Items > Bag of Devouring |
| 12 | 7 | -7.79 |  | Equipment > Mounts and Cargo |
| 13 | 8 | -9.33 |  | Magic Items > Bag of Devouring |
| 14 | 9 | -9.49 |  | Magic Items > Carpet of Flying |
| 15 | 15 | -10.18 |  | Magic Items > Bag of Beans |
| 16 | 17 | -10.32 |  | Equipment > Artisan's Tools |
| 17 | 14 | -10.42 |  | Magic Items > Bag of Tricks |
| 18 | 13 | -10.47 |  | Magic Items > Bag of Tricks |
| 19 | 16 | -10.62 |  | Equipment > Block and Tackle (1 GP) |
| 20 | 18 | -10.93 |  | Magic Items > Bead of Force |


*re-ranking* (query: `fireball damage`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 5.93 | yes | Spells > Delayed Blast Fireball |
| 2 | 4 | 4.58 | yes | Spells > Delayed Blast Fireball |
| 3 | 2 | 4.06 | yes | Spells > Fireball |
| 4 | 3 | 3.99 |  | Spells > Delayed Blast Fireball |
| 5 | 1 | 3.83 |  | Spells > Fireball |
| 6 | 5 | 3.49 |  | Playing the Game > Damage against Multiple Targets |
| 7 | 7 | 3.06 |  | Magic Items > Necklace of Fireballs |
| 8 | 17 | 2.69 |  | Monsters A–Z > Actions |
| 9 | 18 | 2.09 |  | Monsters A–Z > Actions |
| 10 | 14 | 0.12 |  | Playing the Game > Damage Types |
| 11 | 10 | -0.91 |  | Magic Items > Staff of Fire |
| 12 | 8 | -2.43 |  | Spells > Delayed Blast Fireball |
| 13 | 9 | -2.91 |  | Monsters A–Z > Actions |
| 14 | 12 | -2.93 |  | Magic Items > Wand of Fireballs |
| 15 | 20 | -3.28 |  | Monsters A–Z > Actions |
| 16 | 15 | -4.03 |  | Rules Glossary > Damage |
| 17 | 11 | -5.02 |  | Magic Items > Staff of the Magi |
| 18 | 19 | -6.74 |  | Spells > Meteor Swarm |
| 19 | 13 | -7.19 |  | Rules Glossary > Damage Roll |
| 20 | 16 | -7.57 |  | Rules Glossary > Damage Threshold |

*retrieved sections:* Rules Glossary > Long Rest | Magic Items > Bag of Holding | Rules Glossary > Carrying Capacity | Spells > Delayed Blast Fireball | Spells > Fireball

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Long Rest]
#### Long Rest  
A Long Rest is a period of extended downtime—at least 10 hours—available to any creature. During a Long Rest, you sleep for at least 6 hours and perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch.  
During sleep, you have the Unconscious condition. After you finish a Long Rest, you must wait at least 16 hours before starting another one.

---

[Rules Glossary > Long Rest]
You can resume a Long Rest immediately after an interruption. If you do so, the rest requires 1 additional hour per interruption to finish.

---

[Rules Glossary > Long Rest]
**Special Feature.** Some features are recharged by a Long Rest. If you have such a feature, it recharges in the way specified in its description.  
_Interrupting the Rest._ A Long Rest is stopped by the following interruptions:  
- Rolling Initiative
- Casting a spell other than a cantrip
- Taking any damage
- 1 hour of walking or other physical exertion  
If you rested at least 1 hour before the interruption, you gain the benefits of a Short Rest. _See also_ "Short Rest."

---

[Magic Items > Bag of Holding]
#### Bag of Holding  
_Wondrous Item, Uncommon_  
This bag has an interior space considerably larger than its outside dimensions—roughly 2 feet square and 4 feet deep on the inside. The bag can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag weighs 5 pounds, regardless of its contents. Retrieving an item from the bag requires a Utilize action.

---

[Magic Items > Bag of Holding]
If the bag is overloaded, pierced, or torn, it is destroyed, and its contents are scattered in the Astral Plane. If the bag is turned inside out, its contents spill forth unharmed, but the bag must be put right before it can be used again. The bag holds enough air for 10 minutes of breathing, divided by the number of breathing creatures inside.

---

[Rules Glossary > Carrying Capacity]
#### Carrying Capacity  
Your size and Strength score determine the maximum weight in pounds that you can carry, as shown in the Carrying Capacity table. The table also shows the maximum weight you can drag, lift, or push.  
While dragging, lifting, or pushing weight in excess of the maximum weight you can carry, your Speed can be no more than 5 feet.  
**Carrying Capacity**  
<table>
<thead>
<tr>
<th>Creature Size</th>
<th>Carry</th>
<th>Drag/Lift/Push</th>
</tr>
</thead>
<tbody>
<tr>

---

[Spells > Delayed Blast Fireball]
The spell's base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn't ended.  
If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.
```
</details>


---

## q22 (multi-topic) Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skills does the Soldier background give? (3) What is the Owlbear's AC?

**Gold facts (counterfactual data):** DC 10; Athletics and Perception; AC 15


### v0_closed_book  (0 chunks, 1 LLM call(s))

(1) The DC check to stabilize a dying creature is typically 10. A creature can be stabilized with a successful DC 10 Constitution (Healing) check by a healer or through the use of the Aid spell.

(2) The Soldier background gives proficiency in two weapons of your choice, proficiency in light armor, and access to two combat styles. Additionally, you gain the Soldiers Call feature, which allows you to command allies within 60 feet to take the Attack action on their turn, provided they can see or hear you.

(3) An Owlbear has an Armor Class (AC) of 15. This is calculated as 10 + 1 (proficiency bonus for most creatures) + 4 (natural armor).

*facts found (judge): 2/3; missing: Athletics and Perception*


### v1_baseline  (3 chunks, 1 LLM call(s))

The provided context does not contain information about DC checks to stabilize a dying creature, the skills given by the Soldier background, or the Owlbear's AC. Therefore, I cannot answer these questions based solely on the given information.

*facts found (judge): 0/3; missing: DC 10; Athletics and Perception; AC 15*

*retrieved sections:* Animals > Giant Owl | Animals > Swarm of Ravens | Classes > Ranger

<details><summary>full retrieved context</summary>

```
[Animals > Giant Owl]
<td>+2</td>
<td><strong>CON</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>10</td>
<td>+0</td>
<td>+0</td>
<td><strong>WIS</strong></td>
<td>14</td>
<td>+2</td>
<td>+4</td>
<td><strong>CHA</strong></td>
<td>10</td>
<td>+0</td>
<td>+0</td>
</tr>
</tbody>
</table>  
**Skills** Perception +6, Stealth +6<br>
**Resistances** Necrotic, Radiant<br>
**Senses** Darkvision 120 ft.; Passive Perception 16<br>

---

[Animals > Swarm of Ravens]
**Immunities** Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned<br>
**Senses** Passive Perception 15<br>
**Languages** None<br>
**CR** 1/4 (XP 50; PB +2)

---

[Classes > Ranger]
## Ranger  
**Core Ranger Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Dexterity and Wisdom</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Ranger level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Dexterity</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 3: Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The context provided does not contain information about stabilizing a dying creature's DC check, the skills given by the Soldier background, or the Owlbear's AC. Therefore, parts (1), (2), and (3) are missing from the given context.

*facts found (judge): 0/3; missing: DC 10; Athletics and Perception; AC 15*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skill`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | -5.80 | yes | Animals > Actions |
| 2 | 5 | -9.69 | yes | Monsters A–Z > Shadow |
| 3 | 8 | -9.76 |  | Monsters A–Z > Death Dog |
| 4 | 3 | -9.84 |  | Classes > Ranger |
| 5 | 2 | -10.05 |  | Animals > Swarm of Ravens |
| 6 | 9 | -10.56 |  | Animals > Giant Vulture |
| 7 | 4 | -10.61 |  | Animals > Vulture |
| 8 | 6 | -10.61 |  | Animals > Owl |
| 9 | 10 | -10.65 |  | Animals > Hawk |
| 10 | 1 | -10.66 |  | Animals > Giant Owl |

*retrieved sections:* Animals > Actions | Character Creation > Choose a Background | Monsters A–Z > Shadow

<details><summary>full retrieved context</summary>

```
[Animals > Actions]
### Actions  
<hr>  
**_Beaks._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.  
**_Cacophony (Recharge 6)._** _Wisdom Saving Throw:_ DC 10, one creature in the swarm's space. _Failure:_ The target has the Deafened condition until the start of the swarm's next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

---

[Character Creation > Choose a Background]
The background you choose influences step 3, when you determine your character's ability scores. If you're having trouble choosing, the Ability Scores and Backgrounds table shows which backgrounds benefit which ability scores. Look for your class's primary ability there.  
**Ability Scores and Backgrounds**  
<table>
<thead>
<tr>
<th>Ability</th>
<th>Background</th>
</tr>
</thead>
<tbody>
<tr>
<td>Strength</td>
<td>Soldier</td>
</tr>
<tr>
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>

---

[Monsters A–Z > Shadow]
**Immunities** Necrotic, Poison; Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious<br>
**Senses** Darkvision 60 ft.; Passive Perception 10<br>
**Languages** None<br>
**CR** 1/2 (XP 100; PB +2)
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The provided context does not contain information about an Owlbear or its Armor Class (AC). Additionally, there is no mention of a DC check to stabilize a dying creature in the given context. Lastly, the context does not list the skills given by the Soldier background. Therefore, parts (1), (2), and (3) of the question cannot be answered based solely on the provided information.

*facts found (judge): 0/3; missing: DC 10; Athletics and Perception; AC 15*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skill`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | -5.80 | yes | Animals > Actions |
| 2 | 5 | -9.69 | yes | Monsters A–Z > Shadow |
| 3 | 8 | -9.76 | yes | Monsters A–Z > Death Dog |
| 4 | 3 | -9.84 | yes | Classes > Ranger |
| 5 | 2 | -10.05 | yes | Animals > Swarm of Ravens |
| 6 | 9 | -10.56 | yes | Animals > Giant Vulture |
| 7 | 4 | -10.61 | yes | Animals > Vulture |
| 8 | 6 | -10.61 |  | Animals > Owl |
| 9 | 10 | -10.65 |  | Animals > Hawk |
| 10 | 1 | -10.66 |  | Animals > Giant Owl |

*retrieved sections:* Animals > Actions | Character Creation > Choose a Background | Monsters A–Z > Shadow | Monsters A–Z > Death Dog | Classes > Ranger | Animals > Swarm of Ravens | Animals > Giant Vulture | Animals > Vulture

<details><summary>full retrieved context</summary>

```
[Animals > Actions]
### Actions  
<hr>  
**_Beaks._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.  
**_Cacophony (Recharge 6)._** _Wisdom Saving Throw:_ DC 10, one creature in the swarm's space. _Failure:_ The target has the Deafened condition until the start of the swarm's next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

---

[Character Creation > Choose a Background]
The background you choose influences step 3, when you determine your character's ability scores. If you're having trouble choosing, the Ability Scores and Backgrounds table shows which backgrounds benefit which ability scores. Look for your class's primary ability there.  
**Ability Scores and Backgrounds**  
<table>
<thead>
<tr>
<th>Ability</th>
<th>Background</th>
</tr>
</thead>
<tbody>
<tr>
<td>Strength</td>
<td>Soldier</td>
</tr>
<tr>
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>

---

[Monsters A–Z > Shadow]
**Immunities** Necrotic, Poison; Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious<br>
**Senses** Darkvision 60 ft.; Passive Perception 10<br>
**Languages** None<br>
**CR** 1/2 (XP 100; PB +2)

---

[Monsters A–Z > Death Dog]
<td>14</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>14</td>
<td>+2</td>
<td>+2</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>13</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>6</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5, Stealth +4<br>
**Immunities** Blinded, Charmed, Deafened, Frightened, Stunned, Unconscious<br>

---

[Classes > Ranger]
## Ranger  
**Core Ranger Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Dexterity and Wisdom</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Ranger level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Dexterity</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 3: Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Animals > Swarm of Ravens]
**Immunities** Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned<br>
**Senses** Passive Perception 15<br>
**Languages** None<br>
**CR** 1/4 (XP 50; PB +2)

---

[Animals > Giant Vulture]
<td>10</td>
<td>+0</td>
<td>+0</td>
<td><strong>CON</strong></td>
<td>16</td>
<td>+3</td>
<td>+3</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>6</td>
<td>−2</td>
<td>−2</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +3<br>
**Resistances** Necrotic<br>
**Senses** Darkvision 60 ft.; Passive Perception 13<br>

---

[Animals > Vulture]
<td>+0</td>
<td><strong>CON</strong></td>
<td>13</td>
<td>+1</td>
<td>+1</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>2</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>4</td>
<td>−3</td>
<td>−3</td>
</tr>
</tbody>
</table>  
**Skills** Perception +3<br>
**Senses** Passive Perception 13<br>
**Languages** None<br>
**CR** 0 (XP 10; PB +2)
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The provided context does not contain information about stabilizing a dying creature, the Soldier background, or the Owlbear's AC. Therefore, the following parts are missing:

1. The DC check to stabilize a dying creature.
2. The skills given by the Soldier background.
3. The Owlbear's AC.

*facts found (judge): 0/3; missing: DC 10; Athletics and Perception; AC 15*


*re-ranking* (query: `Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skill`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | -5.80 | yes | Animals > Actions |
| 2 | 5 | -9.69 | yes | Monsters A–Z > Shadow |
| 3 | 8 | -9.76 | yes | Monsters A–Z > Death Dog |
| 4 | 3 | -9.84 |  | Classes > Ranger |
| 5 | 2 | -10.05 |  | Animals > Swarm of Ravens |
| 6 | 9 | -10.56 |  | Animals > Giant Vulture |
| 7 | 4 | -10.61 |  | Animals > Vulture |
| 8 | 6 | -10.61 |  | Animals > Owl |
| 9 | 10 | -10.65 |  | Animals > Hawk |
| 10 | 1 | -10.66 |  | Animals > Giant Owl |

*retrieved sections:* Animals > Actions | Monsters A–Z > Shadow | Monsters A–Z > Death Dog

<details><summary>full retrieved context</summary>

```
[Animals > Actions]
### Actions  
<hr>  
**_Beaks._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.  
**_Cacophony (Recharge 6)._** _Wisdom Saving Throw:_ DC 10, one creature in the swarm's space. _Failure:_ The target has the Deafened condition until the start of the swarm's next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

---

[Monsters A–Z > Shadow]
**Immunities** Necrotic, Poison; Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious<br>
**Senses** Darkvision 60 ft.; Passive Perception 10<br>
**Languages** None<br>
**CR** 1/2 (XP 100; PB +2)

---

[Monsters A–Z > Death Dog]
<td>14</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>14</td>
<td>+2</td>
<td>+2</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>13</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>6</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5, Stealth +4<br>
**Immunities** Blinded, Charmed, Deafened, Frightened, Stunned, Unconscious<br>
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

The provided context does not contain information about a DC check to stabilize a dying creature, the skills given by the Soldier background, or the Owlbear's AC. Therefore, I cannot answer these questions based solely on the given information.

*facts found (judge): 0/3; missing: DC 10; Athletics and Perception; AC 15*


*re-ranking* (query: `Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skill`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 22 | -5.63 | yes | Spells > Minor Illusion |
| 2 | 14 | -5.80 | yes | Animals > Actions |
| 3 | 16 | -6.51 | yes | Rules Glossary > Influence [Action] |
| 4 | 18 | -7.34 | yes | Gameplay Toolbox > 1: Choose Abilities |
| 5 | 28 | -7.36 | yes | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 6 | 3 | -7.52 | yes | Character Creation > Choose a Background |
| 7 | 11 | -7.72 | yes | Character Creation > Choose a Background |
| 8 | 26 | -7.88 | yes | Character Creation > Choose a Background |
| 9 | 13 | -8.03 |  | Character Creation > Adjust Ability Scores |
| 10 | 7 | -8.14 |  | Character Origins > Ability Scores |
| 11 | 15 | -8.41 |  | Monsters A–Z > Traits |
| 12 | 24 | -9.64 |  | Playing the Game > Armor Class |
| 13 | 27 | -9.67 |  | Monsters A–Z > Air Elemental |
| 14 | 10 | -9.69 |  | Monsters A–Z > Shadow |
| 15 | 17 | -9.76 |  | Monsters A–Z > Death Dog |
| 16 | 6 | -9.84 |  | Classes > Ranger |
| 17 | 1 | -9.98 |  | Monsters A–Z > Owlbear |
| 18 | 9 | -9.99 |  | Character Creation > Create Your Character |
| 19 | 4 | -10.05 |  | Animals > Swarm of Ravens |
| 20 | 29 | -10.20 |  | Monsters A–Z > Dust Mephit |

*retrieved sections:* Spells > Minor Illusion | Animals > Actions | Rules Glossary > Influence [Action] | Gameplay Toolbox > 1: Choose Abilities | Gameplay Toolbox > 3: Choose Skill Proficiencies | Character Creation > Choose a Background

<details><summary>full retrieved context</summary>

```
[Spells > Minor Illusion]
If a creature takes a Study action to examine the sound or image, the creature can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the illusion becomes faint to the creature.

---

[Animals > Actions]
### Actions  
<hr>  
**_Beaks._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.  
**_Cacophony (Recharge 6)._** _Wisdom Saving Throw:_ DC 10, one creature in the swarm's space. _Failure:_ The target has the Deafened condition until the start of the swarm's next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

---

[Rules Glossary > Influence [Action]]
_Hesitant._ If you urge the monster to do something that it is hesitant to do, you must make an ability check, which is affected by the monster's attitude: Indifferent, Friendly, or Hostile, each of which is defined in this glossary. The Influence Checks table suggests which ability check to make based on how you're interacting with the monster. The GM chooses the check, which has a default DC equal to 15 or the monster's Intelligence score, whichever is higher. On a successful check, the

---

[Gameplay Toolbox > 1: Choose Abilities]
### 1: Choose Abilities  
Choose three abilities that seem appropriate for the background:  
**Strength or Dexterity.** These abilities are ideal for a background involving physical exertion.
**Constitution.** This ability is ideal for a background that involves endurance or long hours of activity.
**Intelligence or Wisdom.** One or both abilities are ideal for a background that focuses on cerebral or spiritual matters.

---

[Gameplay Toolbox > 3: Choose Skill Proficiencies]
### 3: Choose Skill Proficiencies  
Choose two skills appropriate for the background. There needn't be a relationship between the skill proficiencies a background grants and the ability scores it increases.

---

[Character Creation > Choose a Background]
The background you choose influences step 3, when you determine your character's ability scores. If you're having trouble choosing, the Ability Scores and Backgrounds table shows which backgrounds benefit which ability scores. Look for your class's primary ability there.  
**Ability Scores and Backgrounds**  
<table>
<thead>
<tr>
<th>Ability</th>
<th>Background</th>
</tr>
</thead>
<tbody>
<tr>
<td>Strength</td>
<td>Soldier</td>
</tr>
<tr>
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>

---

[Character Creation > Choose a Background]
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>
<td>Constitution</td>
<td>Soldier</td>
</tr>
<tr>
<td>Intelligence</td>
<td>Acolyte</td>
</tr>
<tr>
<td>Wisdom</td>
<td>Acolyte</td>
</tr>
<tr>
<td>Charisma</td>
<td>Acolyte</td>
</tr>
</tbody>
</table>  
_Record Your Feat._ A background gives you a feat, which grants your character particular capabilities. Feats are detailed in "Feats." Write the feat on your character sheet.

---

[Character Creation > Choose a Background]
_Note Proficiencies._ Your background gives proficiency in two skills and with one tool. Record this information on your character sheet.  
Your class also gives proficiencies. Check your class description in "Classes" and note the proficiencies on your character sheet.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

(1) The DC check to stabilize a dying creature is not provided in the given context. It is typically 10, but this information is not present here.

(2) The Soldier background gives the following skills: Athletics and Perception.

(3) The Owlbear's AC is not explicitly stated in the given context. However, based on the stats provided, we can infer that its Armor Class (AC) is 12.

*facts found (judge): 2/3; missing: AC 15*


*re-ranking* (query: `Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skill`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | -7.52 | yes | Character Creation > Choose a Background |
| 2 | 7 | -8.14 | yes | Character Origins > Ability Scores |
| 3 | 11 | -8.80 | yes | Character Origins > Soldier |
| 4 | 10 | -9.69 | yes | Monsters A–Z > Shadow |
| 5 | 6 | -9.84 | yes | Classes > Ranger |
| 6 | 1 | -9.98 | yes | Monsters A–Z > Owlbear |
| 7 | 9 | -9.99 | yes | Character Creation > Create Your Character |
| 8 | 4 | -10.05 | yes | Animals > Swarm of Ravens |
| 9 | 12 | -10.42 |  | Monsters A–Z > Owlbear |
| 10 | 13 | -10.53 |  | Monsters > Ability Scores |
| 11 | 16 | -10.59 |  | Rules Glossary > Frightened [Condition] |
| 12 | 8 | -10.61 |  | Animals > Vulture |
| 13 | 2 | -10.66 |  | Animals > Giant Owl |
| 14 | 19 | -10.79 |  | Rules Glossary > Petrified [Condition] |
| 15 | 5 | -10.85 |  | Spells > Effects |
| 16 | 14 | -10.87 |  | Playing the Game > Ability Scores |
| 17 | 15 | -10.91 |  | Rules Glossary > Charmed [Condition] |
| 18 | 18 | -11.07 |  | Rules Glossary > Paralyzed [Condition] |
| 19 | 20 | -11.14 |  | Rules Glossary > Petrified [Condition] |
| 20 | 17 | -11.24 |  | Rules Glossary > Grappled [Condition] |

*retrieved sections:* Character Creation > Choose a Background | Character Origins > Ability Scores | Character Origins > Soldier | Monsters A–Z > Shadow | Classes > Ranger | Monsters A–Z > Owlbear | Character Creation > Create Your Character | Animals > Swarm of Ravens

<details><summary>full retrieved context</summary>

```
[Character Creation > Choose a Background]
The background you choose influences step 3, when you determine your character's ability scores. If you're having trouble choosing, the Ability Scores and Backgrounds table shows which backgrounds benefit which ability scores. Look for your class's primary ability there.  
**Ability Scores and Backgrounds**  
<table>
<thead>
<tr>
<th>Ability</th>
<th>Background</th>
</tr>
</thead>
<tbody>
<tr>
<td>Strength</td>
<td>Soldier</td>
</tr>
<tr>
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>

---

[Character Origins > Ability Scores]
#### Ability Scores  
A background lists three of your character's ability scores. Increase one by 2 and another one by 1, or increase all three by 1. None of these increases can raise a score above 20.

---

[Character Origins > Soldier]
#### Soldier  
**Ability Scores:** Strength, Dexterity, Constitution
**Feat:** Savage Attacker (see "Feats")
**Skill Proficiencies:** Athletics and Perception
**Tool Proficiency:** _Choose one kind of_ Gaming Set (see "Equipment")
**Equipment:** _Choose A or B:_ (A) Spear, Shortbow, 20 Arrows, Gaming Set (same as above), Healer's Kit, Quiver, Traveler's Clothes, 14 GP; or (B) 50 GP

---

[Monsters A–Z > Shadow]
**Immunities** Necrotic, Poison; Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious<br>
**Senses** Darkvision 60 ft.; Passive Perception 10<br>
**Languages** None<br>
**CR** 1/2 (XP 100; PB +2)

---

[Classes > Ranger]
## Ranger  
**Core Ranger Traits**  
<table>
<tbody>
<tr>
<td>Primary Ability</td>
<td>Dexterity and Wisdom</td>
</tr>
<tr>
<td>Hit Point Die</td>
<td>D10 per Ranger level</td>
</tr>
<tr>
<td>Saving Throw Proficiencies</td>
<td>Strength and Dexterity</td>
</tr>
<tr>
<td>Skill Proficiencies</td>
<td>Choose 3: Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, or Survival</td>
</tr>
<tr>
<td>Weapon Proficiencies</td>
<td>Simple and Martial weapons</td>
</tr>
<tr>

---

[Monsters A–Z > Owlbear]
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CON</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 3 (XP 700; PB +2)

---

[Character Creation > Create Your Character]
2. **Determine Origin.** A character's origin includes two elements: background and species. How did the character spend the years leading up to a life of adventure? Who are the character's ancestors? You can also choose your character's languages.
3. **Determine Ability Scores.** Much of what your character does in the game depends on the character's six abilities.
4. **Choose an Alignment.** Alignment is a shorthand for your character's moral compass.

---

[Animals > Swarm of Ravens]
**Immunities** Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned<br>
**Senses** Passive Perception 15<br>
**Languages** None<br>
**CR** 1/4 (XP 50; PB +2)
```
</details>


### v6_agentic  (11 chunks, 3 LLM call(s))

(1) The DC check to stabilize a dying creature is 10 (Wisdom (Medicine)).
(2) The Soldier background gives proficiency in Athletics and Perception.
(3) The Owlbear's Armor Class (AC) is 15.

*facts found (judge): 3/3; missing: none*

*agentic sub-queries:* stable DC / Soldier background skills / Owlbear AC


*re-ranking* (query: `stable DC`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.06 | yes | Playing the Game > Stabilizing a Character |
| 2 | 14 | -1.22 | yes | Rules Glossary > Stable |
| 3 | 15 | -4.62 | yes | Magic Items > Staff of Power |
| 4 | 12 | -4.78 |  | Spells > Bonus Actions |
| 5 | 10 | -4.79 |  | Equipment > Chain (5 GP) |
| 6 | 4 | -5.32 |  | Equipment > Chain (5 GP) |
| 7 | 2 | -5.32 |  | Gameplay Toolbox > Falling Net |
| 8 | 5 | -5.33 |  | Equipment > Rope (1 GP) |
| 9 | 3 | -5.69 |  | Playing the Game > Difficulty Class |
| 10 | 8 | -5.83 |  | Playing the Game > Difficulty Class |
| 11 | 13 | -6.33 |  | Playing the Game > Falling Off |
| 12 | 17 | -6.41 |  | Magic Items > Staff of Withering |
| 13 | 7 | -6.45 |  | Playing the Game > Death Saving Throws |
| 14 | 9 | -6.46 |  | Equipment > Manacles (2 GP) |
| 15 | 6 | -6.49 |  | Spells > Saving Throws |
| 16 | 16 | -6.55 |  | Spells > Spare the Dying |
| 17 | 11 | -7.00 |  | Gameplay Toolbox > Fear Effects |
| 18 | 20 | -7.04 |  | Equipment > Other Tools |
| 19 | 19 | -7.80 |  | Monsters A–Z > Actions |
| 20 | 18 | -8.03 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Soldier background skills`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 1.92 | yes | Character Origins > Soldier |
| 2 | 1 | 1.85 | yes | Character Creation > Choose a Background |
| 3 | 2 | 1.77 | yes | Character Creation > Choose a Background |
| 4 | 3 | -3.88 |  | Character Origins > Skill Proficiencies |
| 5 | 14 | -4.52 |  | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 6 | 10 | -5.69 |  | Playing the Game > Equipment Proficiencies |
| 7 | 5 | -6.25 |  | Character Creation > Choose a Background |
| 8 | 18 | -6.82 |  | Classes > Fighter |
| 9 | 19 | -7.22 |  | Gameplay Toolbox > Creating a Background |
| 10 | 17 | -7.85 |  | Classes > Ranger |
| 11 | 9 | -8.18 |  | Character Origins > Tool Proficiency |
| 12 | 15 | -8.51 |  | Classes > Paladin |
| 13 | 11 | -9.30 |  | Character Creation > Choose a Background |
| 14 | 8 | -9.31 |  | Character Origins > Character Backgrounds |
| 15 | 6 | -9.41 |  | Character Origins > Equipment |
| 16 | 20 | -9.50 |  | Classes > Warlock |
| 17 | 16 | -10.36 |  | Character Origins > Parts of a Background |
| 18 | 7 | -10.47 |  | Character Creation > Choose a Background |
| 19 | 12 | -10.78 |  | Playing the Game > Skill List |
| 20 | 13 | -10.99 |  | Classes > Level 9: Expertise |


*re-ranking* (query: `Owlbear AC`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.05 | yes | Monsters A–Z > Owlbear |
| 2 | 4 | 0.63 | yes | Monsters A–Z > Actions |
| 3 | 2 | -0.85 | yes | Monsters A–Z > Owlbear |
| 4 | 5 | -2.33 |  | Animals > Owl |
| 5 | 3 | -2.47 |  | Animals > Giant Owl |
| 6 | 11 | -7.50 |  | Animals > Giant Owl |
| 7 | 8 | -8.00 |  | Rules Glossary > Armor Class |
| 8 | 9 | -8.30 |  | Animals > Giant Eagle |
| 9 | 6 | -8.57 |  | Animals > Giant Owl |
| 10 | 20 | -8.66 |  | Monsters > Armor Class |
| 11 | 12 | -9.00 |  | Equipment > Armor |
| 12 | 7 | -9.03 |  | Playing the Game > Armor Class |
| 13 | 14 | -9.05 |  | Animals > Swarm of Ravens |
| 14 | 19 | -9.19 |  | Animals > Raven |
| 15 | 16 | -9.84 |  | Animals > Elephant |
| 16 | 17 | -10.08 |  | Monsters A–Z > Axe Beak |
| 17 | 10 | -10.15 |  | Playing the Game > Armor Class |
| 18 | 15 | -10.68 |  | Monsters A–Z > Actions |
| 19 | 13 | -10.84 |  | Character Creation > Fill In Numbers |
| 20 | 18 | -11.01 |  | Playing the Game > Rolling 20 or 1 |


*re-ranking* (query: `DC for stabilizing a dying creature`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.47 | yes | Playing the Game > Stabilizing a Character |
| 2 | 18 | 1.56 | yes | Playing the Game > Healing |
| 3 | 3 | -0.83 | yes | Gameplay Toolbox > Assassin's Blood (150 GP) |
| 4 | 7 | -1.04 |  | Gameplay Toolbox > Spider's Sting (200 GP) |
| 5 | 6 | -1.10 |  | Gameplay Toolbox > Crawler Mucus (200 GP) |
| 6 | 16 | -1.26 |  | Monsters A–Z > Actions |
| 7 | 5 | -1.90 |  | Gameplay Toolbox > Torpor (600 GP) |
| 8 | 19 | -2.22 |  | Gameplay Toolbox > Malice (250 GP) |
| 9 | 4 | -2.25 |  | Monsters A–Z > Actions |
| 10 | 2 | -2.59 |  | Spells > Spare the Dying |
| 11 | 13 | -2.65 |  | Gameplay Toolbox > Serpent Venom (200 GP) |
| 12 | 8 | -2.76 |  | Monsters A–Z > Actions |
| 13 | 20 | -3.57 |  | Spells > Raise Dead |
| 14 | 11 | -3.59 |  | Monsters A–Z > Actions |
| 15 | 15 | -3.64 |  | Gameplay Toolbox > Truth Serum (150 GP) |
| 16 | 12 | -4.46 |  | Spells > Minor Illusion |
| 17 | 10 | -5.88 | yes | Rules Glossary > Stable |
| 18 | 17 | -5.99 |  | Spells > Major Image |
| 19 | 14 | -7.67 |  | Spells > Circle of Death |
| 20 | 9 | -9.18 |  | Gameplay Toolbox > Falling Net |


*re-ranking* (query: `skills given by Soldier background`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | 2.36 | yes | Character Origins > Soldier |
| 2 | 3 | 0.98 | yes | Character Creation > Choose a Background |
| 3 | 1 | 0.53 | yes | Character Creation > Choose a Background |
| 4 | 2 | -1.08 |  | Character Origins > Skill Proficiencies |
| 5 | 14 | -2.98 |  | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 6 | 4 | -3.96 |  | Character Creation > Choose a Background |
| 7 | 9 | -4.70 |  | Playing the Game > Equipment Proficiencies |
| 8 | 19 | -5.88 |  | Classes > Fighter |
| 9 | 7 | -5.89 |  | Character Origins > Tool Proficiency |
| 10 | 15 | -7.40 |  | Classes > Ranger |
| 11 | 20 | -8.15 |  | Character Creation > Adjust Ability Scores |
| 12 | 16 | -8.17 |  | Gameplay Toolbox > Creating a Background |
| 13 | 17 | -8.20 |  | Classes > Paladin |
| 14 | 11 | -9.28 |  | Character Creation > Fill In Numbers |
| 15 | 10 | -9.52 |  | Character Creation > Choose a Background |
| 16 | 8 | -9.78 |  | Playing the Game > Skill List |
| 17 | 6 | -9.95 |  | Character Origins > Equipment |
| 18 | 13 | -10.28 |  | Classes > Level 3: Bonus Proficiencies |
| 19 | 18 | -10.63 |  | Character Origins > Parts of a Background |
| 20 | 12 | -10.91 |  | Playing the Game > Determining Skills |


*re-ranking* (query: `AC of Owlbear`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.76 | yes | Monsters A–Z > Owlbear |
| 2 | 4 | -1.68 | yes | Monsters A–Z > Actions |
| 3 | 2 | -2.83 | yes | Monsters A–Z > Owlbear |
| 4 | 3 | -3.58 |  | Animals > Giant Owl |
| 5 | 5 | -3.79 |  | Animals > Owl |
| 6 | 7 | -6.28 |  | Playing the Game > Armor Class |
| 7 | 10 | -7.61 |  | Rules Glossary > Armor Class |
| 8 | 20 | -8.75 |  | Spells > Shield of Faith |
| 9 | 9 | -8.90 |  | Equipment > Armor |
| 10 | 13 | -9.02 |  | Animals > Swarm of Ravens |
| 11 | 11 | -9.20 |  | Animals > Giant Eagle |
| 12 | 8 | -9.32 |  | Animals > Giant Owl |
| 13 | 6 | -9.63 |  | Animals > Giant Owl |
| 14 | 19 | -9.82 |  | Animals > Raven |
| 15 | 14 | -9.85 |  | Playing the Game > Armor Class |
| 16 | 15 | -10.33 |  | Animals > Elephant |
| 17 | 17 | -10.42 |  | Monsters A–Z > Axe Beak |
| 18 | 18 | -10.50 |  | Playing the Game > Cover |
| 19 | 12 | -10.82 |  | Rules Glossary > Cover |
| 20 | 16 | -11.15 |  | Playing the Game > Rolling 20 or 1 |

*retrieved sections:* Playing the Game > Stabilizing a Character | Rules Glossary > Stable | Magic Items > Staff of Power | Character Origins > Soldier | Character Creation > Choose a Background | Monsters A–Z > Owlbear | Monsters A–Z > Actions | Playing the Game > Healing | Gameplay Toolbox > Assassin's Blood (150 GP)

<details><summary>full retrieved context</summary>

```
[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Rules Glossary > Stable]
#### Stable  
A creature is Stable if it has 0 Hit Points but isn't required to make Death Saving Throws. _See also_ "Playing the Game" ("Damage and Healing").

---

[Magic Items > Staff of Power]
creature in the area makes a DC 17 Dexterity saving throw. On a failed save, a creature takes Force damage equal to 4 times the number of charges in the staff. On a successful save, a creature takes half as much damage.

---

[Character Origins > Soldier]
#### Soldier  
**Ability Scores:** Strength, Dexterity, Constitution
**Feat:** Savage Attacker (see "Feats")
**Skill Proficiencies:** Athletics and Perception
**Tool Proficiency:** _Choose one kind of_ Gaming Set (see "Equipment")
**Equipment:** _Choose A or B:_ (A) Spear, Shortbow, 20 Arrows, Gaming Set (same as above), Healer's Kit, Quiver, Traveler's Clothes, 14 GP; or (B) 50 GP

---

[Character Creation > Choose a Background]
The background you choose influences step 3, when you determine your character's ability scores. If you're having trouble choosing, the Ability Scores and Backgrounds table shows which backgrounds benefit which ability scores. Look for your class's primary ability there.  
**Ability Scores and Backgrounds**  
<table>
<thead>
<tr>
<th>Ability</th>
<th>Background</th>
</tr>
</thead>
<tbody>
<tr>
<td>Strength</td>
<td>Soldier</td>
</tr>
<tr>
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>

---

[Character Creation > Choose a Background]
<td>Dexterity</td>
<td>Soldier</td>
</tr>
<tr>
<td>Constitution</td>
<td>Soldier</td>
</tr>
<tr>
<td>Intelligence</td>
<td>Acolyte</td>
</tr>
<tr>
<td>Wisdom</td>
<td>Acolyte</td>
</tr>
<tr>
<td>Charisma</td>
<td>Acolyte</td>
</tr>
</tbody>
</table>  
_Record Your Feat._ A background gives you a feat, which grants your character particular capabilities. Feats are detailed in "Feats." Write the feat on your character sheet.

---

[Monsters A–Z > Owlbear]
## Owlbear  
### Owlbear  
_Large Monstrosity, Unaligned_  
**AC** 15 **Initiative** +1 (11) <br>
**HP** 66 (7d10 + 28) <br>
**Speed** 40 ft., Climb 40 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>20</td>
<td>+5</td>
<td>+5</td>
<td><strong>DEX</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The owlbear makes two Rend attacks.  
**_Rend._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 14 (2d8 + 5) Slashing damage.

---

[Monsters A–Z > Owlbear]
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CON</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 3 (XP 700; PB +2)

---

[Playing the Game > Healing]
> **Knocking Out a Creature**
>
> When you would reduce a creature to 0 Hit Points with a melee attack, you can instead reduce the creature to 1 Hit Point and give it the Unconscious condition. It then starts a Short Rest, at the end of which that condition ends on it. The condition ends early if the creature regains any Hit Points or if someone takes an action to administer first aid to it, making a successful DC 10 Wisdom (Medicine) check.

---

[Gameplay Toolbox > Assassin's Blood (150 GP)]
#### Assassin's Blood (150 GP)  
_Ingested Poison_  
A creature subjected to Assassin's Blood makes a DC 10 Constitution saving throw. On a failed save, the creature takes 6 (1d12) Poison damage and has the Poisoned condition for 24 hours. On a successful save, the creature takes half as much damage only.
```
</details>


---

## q23 (multi-topic) Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add to Initiative? (3) What saving throw does Topple force? (4) What is the point-buy budget?

**Gold facts (counterfactual data):** AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points


### v0_closed_book  (0 chunks, 1 LLM call(s))

(1) A Dire Wolf's Armor Class (AC) is 13.
(2) The Alert feat adds advantage on initiative checks or rolls.
(3) Topple forces a Strength saving throw.
(4) The point-buy budget for character creation in D&D 5e is typically 27 ability score points.

*facts found (judge): 1/4; missing: AC 16; twice your Proficiency Bonus; 30 points*


### v1_baseline  (3 chunks, 1 LLM call(s))

The context provided does not contain information about a Dire Wolf's AC, the Alert feat, the Topple action, or the point-buy budget. Therefore, the following parts are missing:

1. The Dire Wolf's AC.
2. The amount the Alert feat adds to Initiative.
3. The saving throw forced by Topple.
4. The point-buy budget.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*

*retrieved sections:* Rules Glossary > Stat Block | Animals > Traits | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The hound makes two Bite attacks.  
**_Bite._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 7 (1d8 + 3) Piercing damage plus 3 (1d6) Fire damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 12, each creature in a 15-foot Cone. _Failure:_ 17 (5d6) Fire damage. _Success:_ Half damage.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The provided context does not contain information about a Dire Wolf's AC, the Alert feat, the saving throw for Topple, or the point-buy budget. Therefore, the following parts are missing:

1. The Dire Wolf's AC.
2. The amount the Alert feat adds to Initiative.
3. The saving throw forced by Topple.
4. The point-buy budget.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 2 | 8 | -8.81 |  | Monsters A–Z > Succubus |
| 3 | 2 | -9.65 | yes | Animals > Traits |
| 4 | 9 | -9.68 | yes | Monsters A–Z > Traits |
| 5 | 4 | -10.73 |  | Monsters A–Z > Actions |
| 6 | 5 | -10.76 |  | Animals > Actions |
| 7 | 7 | -10.79 |  | Monsters A–Z > Bonus Actions |
| 8 | 3 | -10.93 |  | Monsters A–Z > Actions |
| 9 | 6 | -10.93 |  | Monsters A–Z > Bonus Actions |
| 10 | 10 | -11.17 |  | Animals > Traits |

*retrieved sections:* Rules Glossary > Stat Block | Animals > Traits | Monsters A–Z > Traits

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The context provided does not contain information about a Dire Wolf's AC, the Alert feat, the Topple action, or the point-buy budget. Therefore, the following parts are missing:

1. The Dire Wolf's AC is not specified.
2. The Alert feat and its effect on Initiative are not mentioned.
3. There is no mention of the Topple action or its associated saving throw.
4. The point-buy budget for character creation is not included in the given context.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 2 | 8 | -8.81 |  | Monsters A–Z > Succubus |
| 3 | 2 | -9.65 | yes | Animals > Traits |
| 4 | 9 | -9.68 | yes | Monsters A–Z > Traits |
| 5 | 4 | -10.73 | yes | Monsters A–Z > Actions |
| 6 | 5 | -10.76 | yes | Animals > Actions |
| 7 | 7 | -10.79 | yes | Monsters A–Z > Bonus Actions |
| 8 | 3 | -10.93 | yes | Monsters A–Z > Actions |
| 9 | 6 | -10.93 |  | Monsters A–Z > Bonus Actions |
| 10 | 10 | -11.17 |  | Animals > Traits |

*retrieved sections:* Rules Glossary > Stat Block | Animals > Traits | Monsters A–Z > Traits | Monsters A–Z > Actions | Animals > Actions | Monsters A–Z > Bonus Actions

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Claw._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 3 (1d4 + 1) Slashing damage plus 3 (1d6) Fire damage.  
**_Fire Breath (Recharge 6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 15-foot Cone. _Failure:_ 7 (2d6) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Claw._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 10 (2d6 + 3) Slashing damage.  
**_Death Glare (Recharge 5–6)._** _Wisdom Saving Throw:_ DC 11, one Frightened creature the hag can see within 30 feet. _Failure:_ If the target has 20 Hit Points or fewer, it drops to 0 Hit Points. Otherwise, the target takes 13 (3d8) Psychic damage.

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The lion makes two Rend attacks. It can replace one attack with a use of Roar.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 7 (1d8 + 3) Slashing damage.  
**_Roar._** _Wisdom Saving Throw:_ DC 11, one creature within 15 feet. _Failure:_ The target has the Frightened condition until the start of the lion's next turn.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Teleport (Recharge 4–6)._** The dog teleports up to 40 feet to an unoccupied space it can see.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The hound makes two Bite attacks.  
**_Bite._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 7 (1d8 + 3) Piercing damage plus 3 (1d6) Fire damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 12, each creature in a 15-foot Cone. _Failure:_ 17 (5d6) Fire damage. _Success:_ Half damage.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The provided context does not contain information about a Dire Wolf's AC, the Alert feat, the saving throw for Topple, or the point-buy budget. Therefore, the following parts are missing:

1. The Dire Wolf's AC.
2. The amount the Alert feat adds to Initiative.
3. The saving throw forced by Topple.
4. The point-buy budget.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 2 | 8 | -8.81 |  | Monsters A–Z > Succubus |
| 3 | 2 | -9.65 | yes | Animals > Traits |
| 4 | 9 | -9.68 | yes | Monsters A–Z > Traits |
| 5 | 4 | -10.73 |  | Monsters A–Z > Actions |
| 6 | 5 | -10.76 |  | Animals > Actions |
| 7 | 7 | -10.79 |  | Monsters A–Z > Bonus Actions |
| 8 | 3 | -10.93 |  | Monsters A–Z > Actions |
| 9 | 6 | -10.93 |  | Monsters A–Z > Bonus Actions |
| 10 | 10 | -11.17 |  | Animals > Traits |

*retrieved sections:* Rules Glossary > Stat Block | Animals > Traits | Monsters A–Z > Traits

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

(1) A Dire Wolf's AC is 16.
(2) The Alert feat adds twice the user's Proficiency Bonus to the Initiative roll.
(3) The context provided does not mention a saving throw called Topple, so this part is missing.
(4) The point-buy budget is not mentioned in the given context, so this part is also missing.

*facts found (judge): 2/4; missing: Strength saving throw; 30 points*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | -2.93 | yes | Animals > Dire Wolf |
| 2 | 3 | -6.09 | yes | Feats > Alert |
| 3 | 2 | -6.88 | yes | Animals > Dire Wolf |
| 4 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 5 | 27 | -8.62 | yes | Spells > Find Steed |
| 6 | 16 | -8.81 |  | Monsters A–Z > Succubus |
| 7 | 4 | -9.65 | yes | Animals > Traits |
| 8 | 18 | -9.68 | yes | Monsters A–Z > Traits |
| 9 | 19 | -9.94 | yes | Character Origins > Criminal |
| 10 | 29 | -10.30 |  | Monsters A–Z > Actions |
| 11 | 6 | -10.46 |  | Monsters A–Z > Traits |
| 12 | 9 | -10.73 |  | Monsters A–Z > Actions |
| 13 | 22 | -10.73 |  | Monsters A–Z > Actions |
| 14 | 8 | -10.75 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 15 | 11 | -10.76 |  | Animals > Actions |
| 16 | 14 | -10.79 |  | Monsters A–Z > Bonus Actions |
| 17 | 28 | -10.81 |  | Monsters A–Z > Bonus Actions |
| 18 | 30 | -10.87 |  | Monsters A–Z > Bonus Actions |
| 19 | 26 | -10.90 |  | Monsters A–Z > Actions |
| 20 | 15 | -10.90 |  | Monsters A–Z > Traits |

*retrieved sections:* Animals > Dire Wolf | Feats > Alert | Rules Glossary > Stat Block | Spells > Find Steed | Animals > Traits | Monsters A–Z > Traits | Character Origins > Criminal

<details><summary>full retrieved context</summary>

```
[Animals > Dire Wolf]
## Dire Wolf  
_Large Beast, Unaligned_  
**AC** 16 **Initiative** +2 (12) <br>
**HP** 22 (3d10 + 6) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>15</td>

---

[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Animals > Dire Wolf]
<td><strong>CON</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5, Stealth +4<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 1 (XP 200; PB +2)

---

[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Spells > Find Steed]
The steed resembles a Large, rideable animal of your choice, such as a horse, a camel, a dire wolf, or an elk. Whenever you cast the spell, choose the steed's creature type—Celestial, Fey, or Fiend—which determines certain traits in the stat block.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Character Origins > Criminal]
#### Criminal  
**Ability Scores:** Dexterity, Constitution, Intelligence
**Feat:** Alert (see "Feats")
**Skill Proficiencies:** Sleight of Hand and Stealth
**Tool Proficiency:** Thieves' Tools
**Equipment:** _Choose A or B:_ (A) 2 Daggers, Thieves' Tools, Crowbar, 2 Pouches, Traveler's Clothes, 16 GP; or (B) 50 GP
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

(1) A Dire Wolf's AC is 16.
(2) The Alert feat adds twice the user's Proficiency Bonus to the Initiative roll.
(3) The information provided does not mention a saving throw called Topple, so this part is missing.
(4) The point-buy budget is not mentioned in the given context, so this part is also missing.

*facts found (judge): 2/4; missing: Strength saving throw; 30 points*


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 19, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | -2.93 | yes | Animals > Dire Wolf |
| 2 | 3 | -6.09 | yes | Feats > Alert |
| 3 | 2 | -6.88 | yes | Animals > Dire Wolf |
| 4 | 16 | -6.99 | yes | Animals > Wolf |
| 5 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 6 | 4 | -9.65 | yes | Animals > Traits |
| 7 | 17 | -9.98 | yes | Monsters > Armor Class |
| 8 | 18 | -10.05 | yes | Playing the Game > Armor Class |
| 9 | 11 | -10.23 |  | Character Origins > Feat |
| 10 | 6 | -10.46 |  | Monsters A–Z > Traits |
| 11 | 15 | -10.52 |  | Animals > Wolf |
| 12 | 14 | -10.61 |  | Rules Glossary > Incapacitated [Condition] |
| 13 | 9 | -10.73 |  | Monsters A–Z > Actions |
| 14 | 8 | -10.75 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 15 | 7 | -10.93 |  | Monsters A–Z > Actions |
| 16 | 13 | -11.05 |  | Rules Glossary > Monster |
| 17 | 12 | -11.07 |  | Rules Glossary > Ally |
| 18 | 10 | -11.18 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 19 | 19 | -11.27 |  | Rules Glossary > Hit Point Dice |

*retrieved sections:* Animals > Dire Wolf | Feats > Alert | Animals > Wolf | Rules Glossary > Stat Block | Animals > Traits | Monsters > Armor Class | Playing the Game > Armor Class

<details><summary>full retrieved context</summary>

```
[Animals > Dire Wolf]
## Dire Wolf  
_Large Beast, Unaligned_  
**AC** 16 **Initiative** +2 (12) <br>
**HP** 22 (3d10 + 6) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>15</td>

---

[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Animals > Dire Wolf]
<td><strong>CON</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5, Stealth +4<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 1 (XP 200; PB +2)

---

[Animals > Wolf]
## Wolf  
_Medium Beast, Unaligned_  
**AC** 12 **Initiative** +2 (12) <br>
**HP** 11 (2d8 + 2) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>14</td>
<td>+2</td>
<td>+2</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>12</td>
<td>+1</td>

---

[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Monsters > Armor Class]
### Armor Class  
A monster's Armor Class (AC) includes its natural armor, Dexterity, gear, and other defenses. See "Playing the Game" for information on Armor Class.

---

[Playing the Game > Armor Class]
_Only One Base AC._ Some spells and class features give characters a different way to calculate their AC. A character with multiple features that give different ways to calculate AC must choose which one to use; only one base calculation can be in effect for a creature.
```
</details>


### v6_agentic  (15 chunks, 3 LLM call(s))

(1) A Dire Wolf's AC is 16.
(2) The Alert feat adds twice the Proficiency Bonus to the Initiative roll.
(3) Topple forces a Strength saving throw.
(4) The point-buy budget is 30 points.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Dire Wolf AC / Alert feat Initiative / Topple saving throw / Point-buy budget


*re-ranking* (query: `Dire Wolf AC`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.46 | yes | Animals > Dire Wolf |
| 2 | 1 | 0.60 | yes | Animals > Dire Wolf |
| 3 | 13 | -2.39 | yes | Magic Items > Bag of Tricks |
| 4 | 4 | -2.51 | yes | Monsters A–Z > Werewolf |
| 5 | 3 | -2.70 |  | Monsters A–Z > Winter Wolf |
| 6 | 8 | -2.85 |  | Animals > Giant Wolf Spider |
| 7 | 12 | -3.64 |  | Spells > Find Steed |
| 8 | 9 | -7.35 |  | Monsters > Armor Class |
| 9 | 5 | -8.19 |  | Monsters A–Z > Winter Wolf |
| 10 | 11 | -8.35 |  | Animals > Giant Wolf Spider |
| 11 | 7 | -8.56 |  | Monsters A–Z > Winter Wolf |
| 12 | 6 | -8.66 |  | Monsters A–Z > Werewolf |
| 13 | 10 | -9.17 |  | Monsters A–Z > Bonus Actions |
| 14 | 17 | -9.34 |  | Monsters A–Z > Traits |
| 15 | 15 | -9.55 |  | Animals > Traits |
| 16 | 19 | -10.96 |  | Monsters A–Z > Lich |
| 17 | 20 | -11.08 |  | Monsters A–Z > Shadow |
| 18 | 16 | -11.28 |  | Animals > Bonus Actions |
| 19 | 14 | -11.38 |  | Monsters A–Z > Bonus Actions |
| 20 | 18 | -11.41 |  | Animals > Bonus Actions |


*re-ranking* (query: `Alert feat Initiative`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.08 | yes | Feats > Alert |
| 2 | 13 | -3.69 | yes | Character Origins > Criminal |
| 3 | 8 | -4.78 | yes | Monsters > Initiative |
| 4 | 12 | -4.79 |  | Playing the Game > Initiative |
| 5 | 6 | -6.29 |  | Monsters > Initiative |
| 6 | 14 | -7.17 |  | Playing the Game > Initiative |
| 7 | 20 | -7.45 |  | Feats > Boon of Combat Prowess |
| 8 | 11 | -8.17 |  | Feats > Magic Initiate |
| 9 | 19 | -8.21 |  | Feats > Parts of a Feat |
| 10 | 4 | -8.76 |  | Feats > Feat Descriptions |
| 11 | 15 | -8.87 |  | Feats > Parts of a Feat |
| 12 | 5 | -9.09 |  | Classes > Level 19: Epic Boon |
| 13 | 7 | -9.41 |  | Classes > Level 19: Epic Boon |
| 14 | 2 | -9.43 |  | Classes > Level 19: Epic Boon |
| 15 | 10 | -9.50 |  | Classes > Level 19: Epic Boon |
| 16 | 3 | -9.50 |  | Classes > Level 19: Epic Boon |
| 17 | 17 | -9.51 |  | Gameplay Toolbox > 2: Choose a Feat |
| 18 | 16 | -9.79 |  | Character Origins > Feat |
| 19 | 9 | -9.82 |  | Classes > Level 19: Epic Boon |
| 20 | 18 | -11.34 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Topple saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 5.94 | yes | Gameplay Toolbox > Collapsing Roof |
| 2 | 11 | 5.38 | yes | Equipment > Mastery Properties |
| 3 | 8 | 3.82 | yes | Classes > Level 3: Open Hand Technique |
| 4 | 7 | 2.70 | yes | Playing the Game > Saving Throws |
| 5 | 13 | 1.31 |  | Rules Glossary > Save |
| 6 | 9 | 1.31 |  | Magic Items > Thunderous Greatclub |
| 7 | 12 | 1.09 |  | Spells > Flesh to Stone |
| 8 | 18 | 0.96 |  | Playing the Game > Ability Modifier |
| 9 | 20 | 0.33 |  | Spells > Hideous Laughter |
| 10 | 1 | 0.18 |  | Playing the Game > Saving Throw Proficiencies |
| 11 | 14 | 0.11 |  | Magic Items > Wand of Wonder |
| 12 | 16 | -0.12 |  | Rules Glossary > Death Saving Throw |
| 13 | 19 | -0.37 |  | Rules Glossary > Stat Block |
| 14 | 10 | -0.68 |  | Classes > Level 9: Indomitable |
| 15 | 3 | -0.95 |  | Playing the Game > Saving Throw Proficiencies |
| 16 | 4 | -1.43 |  | Spells > Bane |
| 17 | 6 | -1.61 |  | Classes > Careful Spell |
| 18 | 17 | -2.22 |  | Playing the Game > Saving Throws and Damage |
| 19 | 5 | -2.59 |  | Classes > Level 14: Disciplined Survivor |
| 20 | 15 | -3.82 |  | Classes > Eldritch Mind |


*re-ranking* (query: `Point-buy budget`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | -6.32 | yes | Character Creation > Generate Your Scores |
| 2 | 14 | -8.90 | yes | Gameplay Toolbox > Step 3: Spend Your Budget |
| 3 | 11 | -9.13 | yes | Gameplay Toolbox > Step 3: Spend Your Budget |
| 4 | 13 | -9.41 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 5 | 7 | -9.62 |  | Gameplay Toolbox > Step 2: Determine Your XP Budget |
| 6 | 9 | -10.37 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 7 | 1 | -10.51 |  | Character Creation > Starting Equipment |
| 8 | 12 | -10.65 |  | Character Creation > Experience Points |
| 9 | 17 | -10.83 |  | Equipment > Time |
| 10 | 16 | -10.97 |  | Equipment > Ammunition (Varies) |
| 11 | 5 | -11.06 |  | Classes > Distant Spell |
| 12 | 15 | -11.10 |  | Equipment > Food, Drink, and Lodging |
| 13 | 3 | -11.17 |  | Classes > Subtle Spell |
| 14 | 6 | -11.22 |  | Classes > Extended Spell |
| 15 | 19 | -11.23 |  | Rules Glossary > Cone [Area of Effect] |
| 16 | 10 | -11.24 |  | Equipment > Weapons |
| 17 | 20 | -11.31 |  | Equipment > Aristocratic (10 GP per Day) |
| 18 | 4 | -11.33 |  | Character Creation > Hit Points and Hit Point Dice |
| 19 | 8 | -11.39 |  | Equipment > Poor (2 SP per Day) |
| 20 | 18 | -11.43 |  | Equipment > Artisan's Tools |


*re-ranking* (query: `dire_wolf_ac`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.27 | yes | Animals > Dire Wolf |
| 2 | 2 | 0.33 | yes | Animals > Dire Wolf |
| 3 | 4 | -1.94 | yes | Monsters A–Z > Werewolf |
| 4 | 3 | -1.99 |  | Monsters A–Z > Winter Wolf |
| 5 | 7 | -2.78 |  | Animals > Giant Wolf Spider |
| 6 | 11 | -3.02 | yes | Magic Items > Bag of Tricks |
| 7 | 10 | -3.99 |  | Spells > Find Steed |
| 8 | 5 | -7.35 |  | Monsters A–Z > Werewolf |
| 9 | 6 | -7.59 |  | Monsters A–Z > Winter Wolf |
| 10 | 17 | -7.80 |  | Monsters A–Z > Bonus Actions |
| 11 | 8 | -7.99 |  | Monsters A–Z > Winter Wolf |
| 12 | 9 | -8.18 |  | Animals > Giant Wolf Spider |
| 13 | 13 | -8.24 |  | Animals > Traits |
| 14 | 15 | -8.25 |  | Monsters A–Z > Traits |
| 15 | 14 | -10.81 |  | Monsters A–Z > Horned Devil |
| 16 | 20 | -10.90 |  | Monsters A–Z > Sphinx of Lore |
| 17 | 16 | -10.99 |  | Monsters A–Z > Ice Devil |
| 18 | 12 | -11.07 |  | Monsters A–Z > Succubus |
| 19 | 19 | -11.14 |  | Monsters A–Z > Nalfeshnee |
| 20 | 18 | -11.17 |  | Monsters A–Z > Hezrou |


*re-ranking* (query: `alert_feat_initiative_bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.05 | yes | Feats > Alert |
| 2 | 8 | 0.06 | yes | Feats > Boon of Fate |
| 3 | 2 | -1.30 | yes | Monsters > Initiative |
| 4 | 5 | -4.43 |  | Feats > Defense |
| 5 | 14 | -4.82 |  | Rules Glossary > Initiative |
| 6 | 17 | -4.84 |  | Feats > Archery |
| 7 | 16 | -5.51 | yes | Character Origins > Criminal |
| 8 | 6 | -6.02 |  | Monsters > Initiative |
| 9 | 19 | -6.12 |  | Playing the Game > Initiative |
| 10 | 13 | -7.04 |  | Feats > Ability Score Improvement |
| 11 | 9 | -8.81 |  | Classes > Level 19: Epic Boon |
| 12 | 12 | -8.94 |  | Classes > Level 19: Epic Boon |
| 13 | 20 | -9.02 |  | Feats > Parts of a Feat |
| 14 | 4 | -9.02 |  | Classes > Level 19: Epic Boon |
| 15 | 3 | -9.02 |  | Classes > Level 19: Epic Boon |
| 16 | 10 | -9.03 |  | Feats > Feat Descriptions |
| 17 | 18 | -9.05 |  | Monsters A–Z > Bonus Actions |
| 18 | 7 | -9.16 |  | Classes > Level 19: Epic Boon |
| 19 | 15 | -9.33 |  | Classes > Level 4: Ability Score Improvement |
| 20 | 11 | -9.36 |  | Classes > Level 19: Epic Boon |


*re-ranking* (query: `topple_saving_throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 4.88 | yes | Gameplay Toolbox > Collapsing Roof |
| 2 | 10 | 4.52 | yes | Equipment > Mastery Properties |
| 3 | 7 | 2.96 | yes | Playing the Game > Saving Throws |
| 4 | 8 | 2.48 | yes | Classes > Level 3: Open Hand Technique |
| 5 | 12 | 2.18 |  | Rules Glossary > Save |
| 6 | 17 | 0.98 |  | Playing the Game > Ability Modifier |
| 7 | 19 | 0.66 |  | Rules Glossary > Stat Block |
| 8 | 9 | 0.45 |  | Magic Items > Thunderous Greatclub |
| 9 | 1 | 0.27 |  | Playing the Game > Saving Throw Proficiencies |
| 10 | 14 | -0.01 |  | Spells > Hideous Laughter |
| 11 | 15 | -0.22 |  | Rules Glossary > Death Saving Throw |
| 12 | 3 | -0.64 |  | Playing the Game > Saving Throw Proficiencies |
| 13 | 11 | -0.73 |  | Spells > Black Tentacles |
| 14 | 5 | -1.18 |  | Classes > Careful Spell |
| 15 | 4 | -1.18 |  | Spells > Bane |
| 16 | 13 | -1.75 |  | Playing the Game > Saving Throws and Damage |
| 17 | 20 | -1.83 |  | Classes > Level 9: Indomitable |
| 18 | 16 | -2.45 |  | Classes > Heightened Spell |
| 19 | 6 | -2.54 |  | Classes > Level 14: Disciplined Survivor |
| 20 | 18 | -6.97 |  | Magic Items > Dust of Sneezing and Choking |


*re-ranking* (query: `point_buy_budget`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | -5.41 | yes | Character Creation > Generate Your Scores |
| 2 | 17 | -8.16 | yes | Gameplay Toolbox > Step 3: Spend Your Budget |
| 3 | 13 | -8.27 | yes | Gameplay Toolbox > Step 3: Spend Your Budget |
| 4 | 15 | -8.42 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 5 | 10 | -8.47 |  | Gameplay Toolbox > Step 2: Determine Your XP Budget |
| 6 | 11 | -9.55 |  | Gameplay Toolbox > Step 3: Spend Your Budget |
| 7 | 5 | -9.78 |  | Classes > Distant Spell |
| 8 | 4 | -9.79 |  | Character Creation > Starting Equipment |
| 9 | 19 | -9.89 |  | Character Creation > Experience Points |
| 10 | 1 | -10.16 |  | Classes > Subtle Spell |
| 11 | 6 | -10.17 |  | Classes > Twinned Spell |
| 12 | 20 | -10.20 |  | Classes > Careful Spell |
| 13 | 7 | -10.41 |  | Classes > Extended Spell |
| 14 | 8 | -10.42 |  | Classes > Empowered Spell |
| 15 | 18 | -10.50 |  | Equipment > Ammunition (Varies) |
| 16 | 14 | -10.68 |  | Equipment > Food, Drink, and Lodging |
| 17 | 16 | -10.75 |  | Classes > Heightened Spell |
| 18 | 12 | -11.00 |  | Equipment > Weapons |
| 19 | 3 | -11.26 |  | Character Creation > Hit Points and Hit Point Dice |
| 20 | 9 | -11.35 |  | Equipment > Poor (2 SP per Day) |

*retrieved sections:* Animals > Dire Wolf | Magic Items > Bag of Tricks | Feats > Alert | Character Origins > Criminal | Monsters > Initiative | Gameplay Toolbox > Collapsing Roof | Equipment > Mastery Properties | Classes > Level 3: Open Hand Technique | Character Creation > Generate Your Scores | Gameplay Toolbox > Step 3: Spend Your Budget | Monsters A–Z > Werewolf | Feats > Boon of Fate | Playing the Game > Saving Throws

<details><summary>full retrieved context</summary>

```
[Animals > Dire Wolf]
## Dire Wolf  
_Large Beast, Unaligned_  
**AC** 16 **Initiative** +2 (12) <br>
**HP** 22 (3d10 + 6) <br>
**Speed** 50 ft. <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>17</td>
<td>+3</td>
<td>+3</td>
<td><strong>DEX</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
<td><strong>CON</strong></td>
<td>15</td>

---

[Animals > Dire Wolf]
<td><strong>CON</strong></td>
<td>15</td>
<td>+2</td>
<td>+2</td>
</tr>
<tr>
<td><strong>INT</strong></td>
<td>3</td>
<td>−4</td>
<td>−4</td>
<td><strong>WIS</strong></td>
<td>12</td>
<td>+1</td>
<td>+1</td>
<td><strong>CHA</strong></td>
<td>7</td>
<td>−2</td>
<td>−2</td>
</tr>
</tbody>
</table>  
**Skills** Perception +5, Stealth +4<br>
**Senses** Darkvision 60 ft.; Passive Perception 15<br>
**Languages** None<br>
**CR** 1 (XP 200; PB +2)

---

[Magic Items > Bag of Tricks]
<table>
<thead>
<tr>
<th>1d8</th>
<th>Creature</th>
<th>1d8</th>
<th>Creature</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Weasel</td>
<td>5</td>
<td>Panther</td>
</tr>
<tr>
<td>2</td>
<td>Giant Rat</td>
<td>6</td>
<td>Giant Badger</td>
</tr>
<tr>
<td>3</td>
<td>Badger</td>
<td>7</td>
<td>Dire Wolf</td>
</tr>
<tr>
<td>4</td>
<td>Boar</td>
<td>8</td>
<td>Giant Elk</td>
</tr>
</tbody>
</table>  
**Rust Bag of Tricks**  
<table>
<thead>
<tr>
<th>1d8</th>
<th>Creature</th>
<th>1d8</th>

---

[Feats > Alert]
### Origin Feats  
#### Alert  
_Origin Feat_  
You gain the following benefits.  
_Initiative Proficiency._ When you roll Initiative, you can add twice your Proficiency Bonus to the roll.  
_Initiative Swap._ Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

---

[Character Origins > Criminal]
#### Criminal  
**Ability Scores:** Dexterity, Constitution, Intelligence
**Feat:** Alert (see "Feats")
**Skill Proficiencies:** Sleight of Hand and Stealth
**Tool Proficiency:** Thieves' Tools
**Equipment:** _Choose A or B:_ (A) 2 Daggers, Thieves' Tools, Crowbar, 2 Pouches, Traveler's Clothes, 16 GP; or (B) 50 GP

---

[Monsters > Initiative]
### Initiative  
The Initiative entry specifies the monster's Initiative modifier followed by the monster's Initiative score in parentheses. Use the modifier when you roll to determine a monster's Initiative. A monster's Initiative modifier is typically equal to its Dexterity modifier, but some monsters have additional modifiers, such as Proficiency Bonus, applied to that number.

---

[Gameplay Toolbox > Collapsing Roof]
The first creature that crosses the trip wire causes the supports to topple and the unstable section of ceiling to collapse. Each creature beneath the unstable section of ceiling must succeed on a DC 13 Dexterity saving throw, taking 11 (2d10) Bludgeoning damage on a failed save or half as much damage on a successful one. Rubble from the collapse turns the trapped area into Difficult Terrain.

---

[Equipment > Mastery Properties]
**Topple.** If you hit a creature with this weapon, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.  
**Vex.** If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.  
**Weapons**  
<table>
<thead>
<tr>
<th>Name</th>

---

[Classes > Level 3: Open Hand Technique]
#### Level 3: Open Hand Technique  
Whenever you hit a creature with an attack granted by your Flurry of Blows, you can impose one of the following effects on that target.  
**Addle.** The target can't make Opportunity Attacks until the start of its next turn.  
**Push.** The target must succeed on a Strength saving throw or be pushed up to 15 feet away from you.  
**Topple.** The target must succeed on a Dexterity saving throw or have the Prone condition.

---

[Character Creation > Generate Your Scores]
_Point Cost._ You have 30 points to spend on your ability scores. The cost of each score is shown on the Ability Score Point Costs table. For example, a score of 14 costs 7 of your 30 points.  
**Ability Score Point Costs**  
<table>
<thead>
<tr>
<th>Score</th>
<th>Cost</th>
<th>Score</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>8</td>
<td>0</td>
<td>12</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>13</td>
<td>5</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>14</td>
<td>7</td>
</tr>

---

[Gameplay Toolbox > Step 3: Spend Your Budget]
**Example 2.** A moderate-difficulty encounter for five level 3 characters has an XP budget of 225 × 5, for a total of 1,125 XP. With that, you could build either of these encounters:  
- **2 Druids** (450 XP each) and **9 Stirges** (25 XP each), for 1,125 XP total
- **1 Wight** (700 XP), **1 Warhorse Skeleton** (100 XP), and **6 Skeletons** (50 XP each), for 1,100 XP total

---

[Gameplay Toolbox > Step 3: Spend Your Budget]
**Example 3.** A high-difficulty encounter for six level 15 characters has an XP budget of 7,800 × 6, for a total of 46,800 XP. With that, you could build this encounter:  
• **2 Adult Red Dragons** (18,000 XP each) and **2 Fire Giants** (5,000 XP each), for 46,000 XP total

---

[Monsters A–Z > Werewolf]
## Werewolf  
### Werewolf  
_Medium or Small Monstrosity (Lycanthrope), Chaotic Evil_  
**AC** 15 **Initiative** +4 (14) <br>
**HP** 71 (11d8 + 22) <br>
**Speed** 30 ft., 40 ft. (wolf form only) <br>  
<table>
<thead>
<tr>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
<th></th>
<th></th>
<th>MOD</th>
<th>SAVE</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>STR</strong></td>
<td>16</td>
<td>+3</td>
<td>+3</td>
<td><strong>DEX</strong></td>
<td>14</td>

---

[Feats > Boon of Fate]
#### Boon of Fate  
_Epic Boon Feat (Prerequisite: Level 19+)_  
You gain the following benefits.  
_Ability Score Increase._ Increase one ability score of your choice by 1, to a maximum of 30.  
_Improve Fate._ When you or another creature within 60 feet of you succeeds on or fails a D20 Test, you can roll 2d4 and apply the total rolled as a bonus or penalty to the d20 roll. Once you use this benefit, you can't use it again until you roll Initiative or finish a Short or Long Rest.

---

[Playing the Game > Saving Throws]
### Saving Throws  
A saving throw—also called a save—represents an attempt to evade or resist a threat, such as a fiery explosion, a blast of poisonous gas, or a spell trying to invade your mind. You don't normally choose to make a save; you must make one because your character or a monster (if you're the GM) is at risk. A save's result is detailed in the effect that caused it.  
If you don't want to resist the effect, you can choose to fail the save without rolling.
```
</details>


---

## q24 (multi-topic) Answer all four: (1) How far does Push move a creature and what size limit applies? (2) How long is a Short Rest? (3) What is the range of Fireball? (4) What AC bonus does Shield give?

**Gold facts (counterfactual data):** 15 feet; Large or smaller; 2-hour; 120 feet; +4 bonus to AC


### v0_closed_book  (0 chunks, 1 LLM call(s))

Sure, here are the answers:

1. **Push**: The Push action can move a creature up to half its speed. There is no size limit for this movement; it applies to any creature regardless of size.

2. **Short Rest**: A Short Rest lasts 1 hour.

3. **Fireball**: The Fireball spell has a range of 150 feet.

4. **Shield**: The Shield spell gives you a +2 bonus to AC while it is active.

*facts found (judge): 0/5; missing: 15 feet; Large or smaller; 2-hour; 120 feet; +4 bonus to AC*


### v1_baseline  (3 chunks, 1 LLM call(s))

The provided context does not contain information about Push, Short Rest, Fireball, or Shield. Therefore, the following parts are missing:

1. How far does Push move a creature and what size limit applies?
2. How long is a Short Rest?
3. What is the range of Fireball?
4. What AC bonus does Shield give?

*facts found (judge): 0/5; missing: 15 feet; Large or smaller; 2-hour; 120 feet; +4 bonus to AC*

*retrieved sections:* Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Greatclub._** _Melee Attack Roll:_ +6, reach 5 ft. _Hit:_ 13 (2d8 + 4) Bludgeoning damage.  
**_Javelin._** _Melee or Ranged Attack Roll:_ +6, reach 5 ft. or range 30/120 ft. _Hit:_ 11 (2d6 + 4) Piercing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Claw._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 3 (1d4 + 1) Slashing damage plus 3 (1d6) Fire damage.  
**_Fire Breath (Recharge 6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 15-foot Cone. _Failure:_ 7 (2d6) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Spear._** _Melee or Ranged Attack Roll:_ +3, reach 5 ft. or range 20/60 ft. _Hit:_ 4 (1d6 + 1) Piercing damage.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

The provided context does not contain information about Push, Short Rest, Fireball range, or Shield's AC bonus. Therefore, the following parts are missing:

1. How far does Push move a creature and what size limit applies?
2. How long is a Short Rest?
3. What is the range of Fireball?
4. What AC bonus does Shield give?

*facts found (judge): 0/5; missing: 15 feet; Large or smaller; 2-hour; 120 feet; +4 bonus to AC*


*re-ranking* (query: `Answer all four: (1) How far does Push move a creature and what size limit appli`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -5.85 | yes | Playing the Game > Reach |
| 2 | 8 | -6.31 | yes | Monsters A–Z > Actions |
| 3 | 7 | -6.77 | yes | Monsters A–Z > Actions |
| 4 | 2 | -7.80 |  | Monsters A–Z > Actions |
| 5 | 3 | -8.17 |  | Monsters A–Z > Actions |
| 6 | 6 | -8.54 |  | Monsters A–Z > Actions |
| 7 | 9 | -8.95 |  | Animals > Actions |
| 8 | 5 | -9.00 |  | Monsters A–Z > Actions |
| 9 | 10 | -9.31 |  | Monsters A–Z > Actions |
| 10 | 1 | -9.44 |  | Monsters A–Z > Actions |

*retrieved sections:* Playing the Game > Reach | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Playing the Game > Reach]
#### Reach  
A creature has a 5-foot reach and can thus attack targets within 5 feet when making a melee attack. Certain creatures have melee attacks with a reach greater than 5 feet, as noted in their descriptions.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Ocean Spear._** _Melee or Ranged Attack Roll:_ +2, reach 5 ft. or range 20/60 ft. _Hit:_ 3 (1d6) Piercing damage plus 2 (1d4) Cold damage. If the target is a creature, its Speed decreases by 10 feet until the end of its next turn. _Hit or Miss:_ The spear magically returns to the merfolk's hand immediately after a ranged attack.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Rend._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 7 (1d10 + 2) Slashing damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 20-foot-long, 5-foot-wide Line. _Failure:_ 14 (4d6) Fire damage. _Success:_ Half damage.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The provided context does not contain information about Push, Short Rest, Fireball range, or Shield's AC bonus. Therefore, the requested details are missing based on the given information.

*facts found (judge): 0/5; missing: 15 feet; Large or smaller; 2-hour; 120 feet; +4 bonus to AC*


*re-ranking* (query: `Answer all four: (1) How far does Push move a creature and what size limit appli`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -5.85 | yes | Playing the Game > Reach |
| 2 | 8 | -6.31 | yes | Monsters A–Z > Actions |
| 3 | 7 | -6.77 | yes | Monsters A–Z > Actions |
| 4 | 2 | -7.80 | yes | Monsters A–Z > Actions |
| 5 | 3 | -8.17 | yes | Monsters A–Z > Actions |
| 6 | 6 | -8.54 | yes | Monsters A–Z > Actions |
| 7 | 9 | -8.95 | yes | Animals > Actions |
| 8 | 5 | -9.00 | yes | Monsters A–Z > Actions |
| 9 | 10 | -9.31 |  | Monsters A–Z > Actions |
| 10 | 1 | -9.44 |  | Monsters A–Z > Actions |

*retrieved sections:* Playing the Game > Reach | Monsters A–Z > Actions | Animals > Actions

<details><summary>full retrieved context</summary>

```
[Playing the Game > Reach]
#### Reach  
A creature has a 5-foot reach and can thus attack targets within 5 feet when making a melee attack. Certain creatures have melee attacks with a reach greater than 5 feet, as noted in their descriptions.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Ocean Spear._** _Melee or Ranged Attack Roll:_ +2, reach 5 ft. or range 20/60 ft. _Hit:_ 3 (1d6) Piercing damage plus 2 (1d4) Cold damage. If the target is a creature, its Speed decreases by 10 feet until the end of its next turn. _Hit or Miss:_ The spear magically returns to the merfolk's hand immediately after a ranged attack.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Rend._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 7 (1d10 + 2) Slashing damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 20-foot-long, 5-foot-wide Line. _Failure:_ 14 (4d6) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Claw._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 3 (1d4 + 1) Slashing damage plus 3 (1d6) Fire damage.  
**_Fire Breath (Recharge 6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 15-foot Cone. _Failure:_ 7 (2d6) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Spear._** _Melee or Ranged Attack Roll:_ +3, reach 5 ft. or range 20/60 ft. _Hit:_ 4 (1d6 + 1) Piercing damage.

---

[Monsters A–Z > Actions]
**_Handaxe (Humanoid or Hybrid Form Only)._** Melee or _Ranged Attack Roll:_ +7, reach 5 ft or range 20/60 ft. _Hit:_ 14 (3d6 + 4) Slashing damage.  
**_Rend (Bear or Hybrid Form Only)._** _Melee Attack Roll:_ +7, reach 5 ft. _Hit:_ 13 (2d8 + 4) Slashing damage.

---

[Animals > Actions]
### Actions  
<hr>  
**_Tentacles._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 1 Bludgeoning damage.

---

[Monsters A–Z > Actions]
**_Scratch._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 10 (2d6 + 3) Slashing damage.  
**_Longbow (Humanoid or Hybrid Form Only)._** _Ranged Attack Roll:_ +4, range 150/600 ft. _Hit:_ 11 (2d8 + 2) Piercing damage.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

The provided context does not contain information about Push, Short Rest, Fireball range, or Shield's AC bonus. Therefore, the following parts are missing:

1. How far does Push move a creature and what size limit applies?
2. How long is a Short Rest?
3. What is the range of Fireball?
4. What AC bonus does Shield give?

*facts found (judge): 0/5; missing: 15 feet; Large or smaller; 2-hour; 120 feet; +4 bonus to AC*


*re-ranking* (query: `Answer all four: (1) How far does Push move a creature and what size limit appli`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -5.85 | yes | Playing the Game > Reach |
| 2 | 8 | -6.31 | yes | Monsters A–Z > Actions |
| 3 | 7 | -6.77 | yes | Monsters A–Z > Actions |
| 4 | 2 | -7.80 |  | Monsters A–Z > Actions |
| 5 | 3 | -8.17 |  | Monsters A–Z > Actions |
| 6 | 6 | -8.54 |  | Monsters A–Z > Actions |
| 7 | 9 | -8.95 |  | Animals > Actions |
| 8 | 5 | -9.00 |  | Monsters A–Z > Actions |
| 9 | 10 | -9.31 |  | Monsters A–Z > Actions |
| 10 | 1 | -9.44 |  | Monsters A–Z > Actions |

*retrieved sections:* Playing the Game > Reach | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Playing the Game > Reach]
#### Reach  
A creature has a 5-foot reach and can thus attack targets within 5 feet when making a melee attack. Certain creatures have melee attacks with a reach greater than 5 feet, as noted in their descriptions.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Ocean Spear._** _Melee or Ranged Attack Roll:_ +2, reach 5 ft. or range 20/60 ft. _Hit:_ 3 (1d6) Piercing damage plus 2 (1d4) Cold damage. If the target is a creature, its Speed decreases by 10 feet until the end of its next turn. _Hit or Miss:_ The spear magically returns to the merfolk's hand immediately after a ranged attack.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Rend._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 7 (1d10 + 2) Slashing damage.  
**_Fire Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 20-foot-long, 5-foot-wide Line. _Failure:_ 14 (4d6) Fire damage. _Success:_ Half damage.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

(1) Push moves a creature up to 10 feet directly away from the character. The size limit is that the target must be the character's size or smaller to be knocked down.
(2) A Short Rest lasts 2 hours.
(3) The range of Fireball is not provided in the given context.
(4) The context does not provide the AC bonus given by the Shield of the Cavalier.

*facts found (judge): 1/5; missing: 15 feet; Large or smaller; 120 feet; +4 bonus to AC*


*re-ranking* (query: `Answer all four: (1) How far does Push move a creature and what size limit appli`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 10 | -3.74 | yes | Magic Items > Shield of the Cavalier |
| 2 | 28 | -5.43 | yes | Monsters A–Z > Actions |
| 3 | 2 | -5.69 | yes | Rules Glossary > Short Rest |
| 4 | 7 | -5.85 | yes | Playing the Game > Reach |
| 5 | 12 | -5.90 | yes | Character Origins > Orc |
| 6 | 4 | -6.28 | yes | Playing the Game > Travel Pace |
| 7 | 23 | -6.30 | yes | Spells > Prayer of Healing |
| 8 | 15 | -6.31 | yes | Monsters A–Z > Actions |
| 9 | 13 | -6.77 |  | Monsters A–Z > Actions |
| 10 | 22 | -7.55 |  | Monsters A–Z > Actions |
| 11 | 16 | -7.74 |  | Spells > Shield of Faith |
| 12 | 3 | -7.80 |  | Monsters A–Z > Actions |
| 13 | 24 | -8.08 |  | Monsters A–Z > Actions |
| 14 | 26 | -8.11 |  | Monsters A–Z > Actions |
| 15 | 29 | -8.11 |  | Playing the Game > Hit Points |
| 16 | 5 | -8.17 |  | Monsters A–Z > Actions |
| 17 | 14 | -8.40 |  | Monsters A–Z > Traits |
| 18 | 11 | -8.54 |  | Monsters A–Z > Actions |
| 19 | 17 | -8.95 |  | Animals > Actions |
| 20 | 9 | -9.00 |  | Monsters A–Z > Actions |

*retrieved sections:* Magic Items > Shield of the Cavalier | Monsters A–Z > Actions | Rules Glossary > Short Rest | Playing the Game > Reach | Character Origins > Orc | Playing the Game > Travel Pace | Spells > Prayer of Healing

<details><summary>full retrieved context</summary>

```
[Magic Items > Shield of the Cavalier]
_Forceful Bash._ When you take the Attack action, you can make one of the attack rolls using the Shield against a target within 5 feet of yourself. Apply your Proficiency Bonus and Strength modifier to the attack roll. On a hit, the Shield deals Force damage to the target equal to 2d6 + 2 plus your Strength modifier, and if the target is a creature, you can push it up to 10 feet directly away from yourself. If the creature is your size or smaller, you can also knock it down, giving it the Prone

---

[Monsters A–Z > Actions]
**_Lightning Breath (Recharge 5–6)._** _Dexterity Saving Throw:_ DC 19, each creature in a 90-foot-long, 5-foot-wide Line. _Failure:_ 55 (10d10) Lightning damage. _Success:_ Half damage.  
**_Repulsion Breath._** _Strength Saving Throw:_ DC 19, each creature in a 30-foot Cone. _Failure:_ The target is pushed up to 60 feet straight away from the dragon and has the Prone condition.

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Playing the Game > Reach]
#### Reach  
A creature has a 5-foot reach and can thus attack targets within 5 feet when making a melee attack. Certain creatures have melee attacks with a reach greater than 5 feet, as noted in their descriptions.

---

[Character Origins > Orc]
#### Orc  
**Creature Type:** Humanoid
**Size:** Medium (about 6–7 feet tall)
**Speed:** 30 feet  
As an Orc, you have these special traits.  
_Adrenaline Rush._ You can take the Dash action as a Bonus Action. When you do so, you gain a number of Temporary Hit Points equal to your Proficiency Bonus.  
You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Short or Long Rest.

---

[Playing the Game > Travel Pace]
While traveling outside combat, a group can move at a Fast, Normal, or Slow pace, as shown on the Travel Pace table. The table states how far the party can move in a period of time; if riding horses or other mounts, the group can move twice that distance for 1 hour, after which the mounts need a Short or Long Rest before they can move at that increased pace again (see "Equipment" for a selection of mounts for sale). "Gameplay Toolbox" has rules that affect which pace you can choose in certain

---

[Spells > Prayer of Healing]
#### Prayer of Healing  
_Level 2 Abjuration (Cleric, Paladin)_  
**Casting Time:** 10 minutes
**Range:** 30 feet
**Components:** V
**Duration:** Instantaneous  
Up to five creatures of your choice who remain within range for the spell's entire casting gain the benefits of a Short Rest and also regain 2d8 Hit Points. A creature can't be affected by this spell again until that creature finishes a Long Rest.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Ocean Spear._** _Melee or Ranged Attack Roll:_ +2, reach 5 ft. or range 20/60 ft. _Hit:_ 3 (1d6) Piercing damage plus 2 (1d4) Cold damage. If the target is a creature, its Speed decreases by 10 feet until the end of its next turn. _Hit or Miss:_ The spear magically returns to the merfolk's hand immediately after a ranged attack.
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

(1) Push moves a creature up to 10 feet directly away from the character. The size limit for being pushed down is if the creature is the character's size or smaller.
(2) A Short Rest lasts 2 hours.
(3) The range of Fireball is not provided in the given context.
(4) The context does not provide information about the AC bonus given by the Shield.

*facts found (judge): 1/5; missing: 15 feet; Large or smaller; 120 feet; +4 bonus to AC*


*re-ranking* (query: `Answer all four: (1) How far does Push move a creature and what size limit appli`): candidate pool of 25, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 10 | -3.74 | yes | Magic Items > Shield of the Cavalier |
| 2 | 2 | -5.69 | yes | Rules Glossary > Short Rest |
| 3 | 7 | -5.85 | yes | Playing the Game > Reach |
| 4 | 4 | -6.28 | yes | Playing the Game > Travel Pace |
| 5 | 11 | -7.23 | yes | Rules Glossary > Size |
| 6 | 3 | -7.80 | yes | Monsters A–Z > Actions |
| 7 | 5 | -8.17 | yes | Monsters A–Z > Actions |
| 8 | 23 | -8.71 | yes | Spells > Slow |
| 9 | 16 | -8.80 |  | Spells > Fireball |
| 10 | 12 | -8.83 |  | Monsters > Size |
| 11 | 9 | -9.00 |  | Monsters A–Z > Actions |
| 12 | 15 | -9.07 |  | Rules Glossary > Short Rest |
| 13 | 1 | -9.44 |  | Monsters A–Z > Actions |
| 14 | 8 | -9.90 |  | Spells > Find the Path |
| 15 | 19 | -10.28 |  | Rules Glossary > Cone [Area of Effect] |
| 16 | 13 | -10.36 |  | Character Origins > Size |
| 17 | 14 | -10.36 |  | Rules Glossary > Short Rest |
| 18 | 18 | -10.69 |  | Spells > Shield |
| 19 | 6 | -10.79 |  | Magic Items > Shield, +1, +2, or +3 |
| 20 | 17 | -10.83 |  | Spells > Fireball |

*retrieved sections:* Magic Items > Shield of the Cavalier | Rules Glossary > Short Rest | Playing the Game > Reach | Playing the Game > Travel Pace | Rules Glossary > Size | Monsters A–Z > Actions | Spells > Slow

<details><summary>full retrieved context</summary>

```
[Magic Items > Shield of the Cavalier]
_Forceful Bash._ When you take the Attack action, you can make one of the attack rolls using the Shield against a target within 5 feet of yourself. Apply your Proficiency Bonus and Strength modifier to the attack roll. On a hit, the Shield deals Force damage to the target equal to 2d6 + 2 plus your Strength modifier, and if the target is a creature, you can push it up to 10 feet directly away from yourself. If the creature is your size or smaller, you can also knock it down, giving it the Prone

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Playing the Game > Reach]
#### Reach  
A creature has a 5-foot reach and can thus attack targets within 5 feet when making a melee attack. Certain creatures have melee attacks with a reach greater than 5 feet, as noted in their descriptions.

---

[Playing the Game > Travel Pace]
While traveling outside combat, a group can move at a Fast, Normal, or Slow pace, as shown on the Travel Pace table. The table states how far the party can move in a period of time; if riding horses or other mounts, the group can move twice that distance for 1 hour, after which the mounts need a Short or Long Rest before they can move at that increased pace again (see "Equipment" for a selection of mounts for sale). "Gameplay Toolbox" has rules that affect which pace you can choose in certain

---

[Rules Glossary > Size]
#### Size  
A creature or an object belongs to a size category: Tiny, Small, Medium, Large, Huge, or Gargantuan. A creature's size determines how much space the creature occupies in combat. An object's size affects its Hit Points. _See also_ "Breaking Objects" and "Playing the Game" ("Combat").

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Claw._** _Melee Attack Roll:_ +3, reach 5 ft. _Hit:_ 3 (1d4 + 1) Slashing damage plus 3 (1d6) Fire damage.  
**_Fire Breath (Recharge 6)._** _Dexterity Saving Throw:_ DC 11, each creature in a 15-foot Cone. _Failure:_ 7 (2d6) Fire damage. _Success:_ Half damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Spear._** _Melee or Ranged Attack Roll:_ +3, reach 5 ft. or range 20/60 ft. _Hit:_ 4 (1d6 + 1) Piercing damage.

---

[Spells > Slow]
#### Slow  
_Level 3 Transmutation (Bard, Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a drop of molasses)
**Duration:** Concentration, up to 1 minute  
You alter time around up to six creatures of your choice in a 40-foot Cube within range. Each target must succeed on a Wisdom saving throw or be affected by this spell for the duration.
```
</details>


### v6_agentic  (12 chunks, 3 LLM call(s))

(1) The Push property moves a creature up to 15 feet straight away from the wielder, provided the target is Large or smaller.
(2) A Short Rest lasts for 2 hours.
(3) The range of Fireball is 120 feet.
(4) The Shield gives a bonus to Armor Class equal to the Shield's rarity: +1 for uncommon, +2 for rare, and +3 for very rare.

*facts found (judge): 4/5; missing: +4 bonus to AC*

*agentic sub-queries:* Push / Short Rest / Fireball / Shield


*re-ranking* (query: `Push`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 7 | 2.54 | yes | Equipment > Mastery Properties |
| 2 | 4 | 1.37 | yes | Spells > Arcane Hand |
| 3 | 3 | 0.51 | yes | Classes > Level 2: Action Surge |
| 4 | 9 | 0.43 |  | Playing the Game > Ability Modifier |
| 5 | 5 | 0.17 |  | Classes > Level 3: Open Hand Technique |
| 6 | 10 | -1.15 |  | Rules Glossary > Carrying Capacity |
| 7 | 2 | -1.56 |  | Rules Glossary > Unarmed Strike |
| 8 | 6 | -1.70 |  | Magic Items > Rod of Lordly Might |
| 9 | 15 | -1.85 |  | Magic Items > Bead of Force |
| 10 | 18 | -2.49 |  | Gameplay Toolbox > Extended Travel |
| 11 | 1 | -2.62 |  | Classes > Level 9: Tactical Master |
| 12 | 20 | -3.88 |  | Spells > Resilient Sphere |
| 13 | 16 | -4.55 |  | Playing the Game > Adventuring Equipment |
| 14 | 13 | -4.93 |  | Classes > Monk Subclass: Warrior of the Open Hand |
| 15 | 19 | -8.81 |  | Rules Glossary > Ready [Action] |
| 16 | 8 | -9.13 |  | Playing the Game > Your Turn |
| 17 | 11 | -9.51 |  | Animals > Actions |
| 18 | 17 | -9.51 |  | Monsters A–Z > Actions |
| 19 | 12 | -9.59 |  | Monsters A–Z > Actions |
| 20 | 14 | -9.71 |  | Animals > Actions |


*re-ranking* (query: `Short Rest`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 9.24 | yes | Rules Glossary > Short Rest |
| 2 | 2 | 7.16 | yes | Rules Glossary > Short Rest |
| 3 | 5 | 6.66 | yes | Equipment > Attune during a Short Rest |
| 4 | 4 | 5.60 |  | Rules Glossary > Long Rest |
| 5 | 7 | 4.92 |  | Rules Glossary > Short Rest |
| 6 | 9 | 4.82 |  | Equipment > Attune during a Short Rest |
| 7 | 3 | 4.42 |  | Equipment > Attune during a Short Rest |
| 8 | 20 | 4.08 |  | Classes > Level 10: Tireless |
| 9 | 18 | 3.29 |  | Monsters > Limited Usage |
| 10 | 11 | 2.47 |  | Rules Glossary > Long Rest |
| 11 | 8 | 2.15 |  | Rules Glossary > Hit Point Dice |
| 12 | 6 | 2.12 |  | Playing the Game > Hit Points |
| 13 | 15 | 1.83 |  | Playing the Game > Healing |
| 14 | 12 | 1.61 |  | Rules Glossary > Long Rest |
| 15 | 16 | 0.82 |  | Rules Glossary > Knocking Out a Creature |
| 16 | 10 | 0.16 |  | Spells > Prayer of Healing |
| 17 | 17 | -0.27 |  | Rules Glossary > Long Rest |
| 18 | 13 | -0.67 |  | Equipment > Ending Attunement |
| 19 | 14 | -1.20 |  | Character Origins > Orc |
| 20 | 19 | -3.18 |  | Rules Glossary > Exhaustion [Condition] |


*re-ranking* (query: `Fireball`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 12 | 5.21 | yes | Spells > Fireball |
| 2 | 14 | 4.80 | yes | Spells > Fireball |
| 3 | 2 | 4.02 | yes | Magic Items > Wand of Fireballs |
| 4 | 1 | 3.97 |  | Magic Items > Necklace of Fireballs |
| 5 | 17 | 3.59 |  | Spells > Delayed Blast Fireball |
| 6 | 8 | 3.44 |  | Spells > Delayed Blast Fireball |
| 7 | 16 | 3.02 |  | Magic Items > Wand of Fireballs |
| 8 | 9 | 2.52 |  | Monsters A–Z > Actions |
| 9 | 11 | 2.35 |  | Monsters A–Z > Actions |
| 10 | 6 | 1.66 |  | Magic Items > Helm of Brilliance |
| 11 | 4 | 1.58 |  | Magic Items > Staff of Fire |
| 12 | 20 | 1.47 |  | Character Creation > Tier 2 (Levels 5–10) |
| 13 | 3 | 1.20 |  | Magic Items > Staff of the Magi |
| 14 | 19 | 0.69 |  | Monsters A–Z > Actions |
| 15 | 7 | 0.00 |  | Magic Items > Hat of Many Spells |
| 16 | 5 | -0.60 |  | Magic Items > Staff of Power |
| 17 | 13 | -0.90 |  | Gameplay Toolbox > Fire-Casting Statue |
| 18 | 10 | -1.42 |  | Gameplay Toolbox > Fire-Casting Statue |
| 19 | 18 | -3.76 |  | Equipment > Tinderbox (5 SP) |
| 20 | 15 | -9.50 |  | Gameplay Toolbox > Spiked Pit |


*re-ranking* (query: `Shield`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 4.55 | yes | Magic Items > Shield, +1, +2, or +3 |
| 2 | 7 | 4.53 | yes | Magic Items > Animated Shield |
| 3 | 1 | 4.48 | yes | Magic Items > Sentinel Shield |
| 4 | 17 | 4.07 |  | Spells > Fire Shield |
| 5 | 3 | 3.80 |  | Equipment > Armor Training |
| 6 | 6 | 3.67 |  | Magic Items > Shield of the Cavalier |
| 7 | 5 | 3.38 |  | Magic Items > Spellguard Shield |
| 8 | 9 | 3.26 |  | Magic Items > Shield of Missile Attraction |
| 9 | 2 | 3.17 |  | Magic Items > Animated Shield |
| 10 | 12 | 3.16 |  | Magic Items > Shield of the Cavalier |
| 11 | 8 | 3.01 |  | Magic Items > Arrow-Catching Shield |
| 12 | 10 | 2.89 |  | Magic Items > Shield of the Cavalier |
| 13 | 19 | 2.07 |  | Spells > Shield of Faith |
| 14 | 16 | 1.92 |  | Magic Items > Shield of the Cavalier |
| 15 | 20 | 1.33 |  | Spells > Fire Shield |
| 16 | 14 | 1.29 |  | Magic Items > Shield of the Cavalier |
| 17 | 11 | 1.10 |  | Equipment > One at a Time |
| 18 | 13 | -1.67 |  | Equipment > Armor |
| 19 | 15 | -1.91 |  | Magic Items > Bracers of Defense |
| 20 | 18 | -3.21 |  | Magic Items > Brooch of Shielding |

*retrieved sections:* Equipment > Mastery Properties | Spells > Arcane Hand | Classes > Level 2: Action Surge | Rules Glossary > Short Rest | Equipment > Attune during a Short Rest | Spells > Fireball | Magic Items > Wand of Fireballs | Magic Items > Shield, +1, +2, or +3 | Magic Items > Animated Shield | Magic Items > Sentinel Shield

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Spells > Arcane Hand]
**Forceful Hand.** The hand attempts to push a Huge or smaller creature within 5 feet of it. The target must succeed on a Strength saving throw, or the hand pushes the target up to 5 feet plus a number of feet equal to five times your spellcasting ability modifier. The hand moves with the target, remaining within 5 feet of it.

---

[Classes > Level 2: Action Surge]
#### Level 2: Action Surge  
You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action, except the Magic action.  
Once you use this feature, you can't do so again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest but only once on a turn.

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:

---

[Rules Glossary > Short Rest]
_Interrupting the Rest._ A Short Rest is stopped by the following interruptions:  
- Rolling Initiative
- Casting a spell other than a cantrip
- Taking any damage  
An interrupted Short Rest confers no benefits.

---

[Equipment > Attune during a Short Rest]
Attuning to an item requires you to spend a Short Rest focused on only that item while being in physical contact with it (this can't be the same Short Rest used to learn the item's properties). This focus can take the form of weapon practice (for a Weapon), meditation (for a Wand), or some other appropriate activity. If the Short Rest is interrupted, the Attunement attempt fails. Otherwise, at the end of the Short Rest, you're attuned to the magic item and can access its full magical

---

[Spells > Fireball]
#### Fireball  
_Level 3 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Instantaneous  
A bright streak flashes from you to a point you choose within range and then blossoms with a low roar into a fiery explosion. Each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw, taking 9d6 Fire damage on a failed save or half as much damage on a successful one.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Magic Items > Wand of Fireballs]
#### Wand of Fireballs  
_Wand, Rare (Requires Attunement by a Spellcaster)_  
This wand has 7 charges. While holding it, you can expend no more than 3 charges to cast _Fireball_ (save DC 15) from it. For 1 charge, you cast the level 3 version of the spell. You can increase the spell's level by 1 for each additional charge you expend.

---

[Magic Items > Shield, +1, +2, or +3]
#### Shield, +1, +2, or +3  
_Armor (Shield), Uncommon (+1), Rare (+2), or Very Rare (+3)_  
While holding this Shield, you have a bonus to Armor Class determined by the Shield's rarity, in addition to the Shield's normal bonus to AC.

---

[Magic Items > Animated Shield]
While holding this Shield, you can take a Bonus Action to cause it to animate. The Shield leaps into the air and hovers in your space to protect you as if you were wielding it, leaving your hands free. The Shield remains animate for 1 minute, until you take a Bonus Action to end this effect, or until you die or have the Incapacitated condition, at which point the Shield falls to the ground or into your hand if you have one free.

---

[Magic Items > Sentinel Shield]
#### Sentinel Shield  
_Armor (Shield), Uncommon_  
While holding this Shield, you have Advantage on Initiative rolls and Wisdom (Perception) checks. The Shield is emblazoned with a symbol of an eye.
```
</details>
