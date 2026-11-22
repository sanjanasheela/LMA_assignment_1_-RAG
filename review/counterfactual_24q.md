# Manual review: counterfactual_24q

Grade each answer against the SRD text. Suggested scale: correct 0 = wrong/missing, 1 = partly right, 2 = fully right; complete 0/1/2 = share of the question's parts answered; faithful Y/N = every claim is supported by the retrieved context.


---

## q1 (multi-part) Counterspell and Shield are both Abjuration spells cast as a Reaction. For each: what spell level is it? What is Counterspell's range and which saving throw does it force? What AC bonus does Shield give?

**Gold facts (counterfactual data):** Level 3; Level 1; 90 feet; Wisdom saving throw; +4 bonus to AC


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Counterspell:** 3rd-level Abjuration. Its range is 60 feet. It doesn't force a saving throw. If the target spell is 3rd level or lower, it's countered automatically. If it's higher, the target makes an ability check using its spellcasting ability, with a DC of 10 + the spell's level.

**Shield:** 1st-level Abjuration. It gives a +5 bonus to AC until the start of your next turn, including against the triggering attack.

*facts found (judge): 2/5; missing: 90 feet; Wisdom saving throw; +4 bonus to AC*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Spell levels:**
- **Counterspell:** Level 3
- **Shield:** Level 1

**Counterspell's range:** 90 feet.

**Saving throw:** The Context doesn't say. Counterspell's entry lists no saving throw, so that part can't be answered from the Context.

**Shield's AC bonus:** +4 to AC, including against the triggering attack.

*facts found (judge): 4/5; missing: Wisdom saving throw*

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

**Counterspell:** Level 3. Its range is 90 feet. The Context doesn't list a saving throw for Counterspell, so I can't say which one it forces.

**Shield:** Level 1. It gives a +4 bonus to AC, including against the triggering attack.

*facts found (judge): 4/5; missing: Wisdom saving throw*


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

**Counterspell:** Level 3.
**Shield:** Level 1.

Counterspell has a range of 90 feet and forces a Wisdom saving throw.

Shield gives a +4 bonus to AC.

*facts found (judge): 3/5; missing: 90 feet; Wisdom saving throw*


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

**Spell levels:** Counterspell is level 3. Shield is level 1.

**Counterspell:** The range is 90 feet. The Context does not state which saving throw Counterspell forces, so that part can't be answered from the Context.

**Shield:** It gives a +4 bonus to AC, including against the triggering attack.

*facts found (judge): 4/5; missing: Wisdom saving throw*


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

**Spell levels:** Counterspell is level 3. Shield is level 1.

**Counterspell:** Its range is 90 feet. It forces a Wisdom saving throw on the creature casting the spell.

**Shield:** It gives a +4 bonus to AC.

*facts found (judge): 2/5; missing: 90 feet; Wisdom saving throw; +4 bonus to AC*


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

**Spell levels:** Counterspell is level 3. Shield is level 1.

**Counterspell:** Its range is 90 feet, and it forces a Wisdom saving throw.

**Shield:** It gives a +4 bonus to AC, including against the triggering attack.

*facts found (judge): 5/5; missing: none*


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


### v6_agentic  (8 chunks, 3 LLM call(s))

**Counterspell:** Level 3. Its range is 90 feet. It forces a Wisdom saving throw. The Wisdom save appears in a separate Counterspell entry that has no level or range listed, so I'm relying on that entry for the saving throw.

**Shield:** Level 1. It gives a +4 bonus to AC.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* Counterspell spell D&D 5e level range saving throw / Shield spell D&D 5e level AC bonus reaction / Abjuration school spellcasting reaction

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Counterspell spell D&D 5e level range saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 20 | 2.64 | yes | Spells > Seeming |
| 2 | 2 | 1.53 | yes | Spells > Counterspell |
| 3 | 5 | 0.92 |  | Spells > Blight |
| 4 | 16 | 0.70 |  | Classes > Level 7: Countercharm |
| 5 | 3 | 0.65 |  | Spells > Bane |
| 6 | 18 | 0.64 |  | Spells > Inflict Wounds |
| 7 | 4 | 0.34 |  | Spells > Blindness/Deafness |
| 8 | 12 | -0.03 |  | Spells > Compulsion |
| 9 | 6 | -0.07 |  | Spells > Hideous Laughter |
| 10 | 7 | -0.15 |  | Spells > Befuddlement |
| 11 | 8 | -0.42 |  | Magic Items > Spell Scroll |
| 12 | 14 | -0.44 |  | Spells > Bless |
| 13 | 1 | -1.04 | yes | Spells > Counterspell |
| 14 | 10 | -4.32 |  | Spells > Otherworldly Steed |
| 15 | 9 | -5.55 |  | Spells > Confusion |
| 16 | 19 | -8.33 |  | Classes > Level 14: Overchannel |
| 17 | 11 | -9.26 |  | Character Creation > Starting at Higher Levels |
| 18 | 15 | -10.11 |  | Spells > Scrying |
| 19 | 13 | -10.43 |  | Spells > Scrying |
| 20 | 17 | -10.65 |  | Playing the Game > Rhythm of Play |


*re-ranking* (query: `Shield spell D&D 5e level AC bonus reaction`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.51 | yes | Spells > Shield |
| 2 | 2 | 2.29 | yes | Magic Items > Arrow-Catching Shield |
| 3 | 5 | 1.89 | yes | Spells > Shield of Faith |
| 4 | 3 | -1.10 |  | Magic Items > Shield, +1, +2, or +3 |
| 5 | 4 | -1.16 |  | Magic Items > Shield of the Cavalier |
| 6 | 15 | -1.44 |  | Rules Glossary > Armor Training |
| 7 | 11 | -1.51 |  | Spells > Reaction and Bonus Action Triggers |
| 8 | 6 | -3.35 |  | Magic Items > Animated Shield |
| 9 | 17 | -3.40 |  | Magic Items > Shield of the Cavalier |
| 10 | 10 | -3.47 |  | Monsters A–Z > Reactions |
| 11 | 9 | -3.87 |  | Monsters A–Z > Reactions |
| 12 | 8 | -4.00 |  | Magic Items > Shield of the Cavalier |
| 13 | 7 | -6.50 |  | Magic Items > Spellguard Shield |
| 14 | 18 | -7.01 |  | Classes > Level 1 Paladin Spells |
| 15 | 12 | -8.37 |  | Magic Items > Shield of Missile Attraction |
| 16 | 16 | -8.46 | yes | Spells > Counterspell |
| 17 | 13 | -8.74 |  | Magic Items > Bracers of Defense |
| 18 | 20 | -9.67 |  | Character Creation > Starting at Higher Levels |
| 19 | 19 | -9.98 |  | Classes > Level 1: Unarmored Defense |
| 20 | 14 | -10.62 |  | Magic Items > Animated Shield |


*re-ranking* (query: `Abjuration school spellcasting reaction`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 0.91 | yes | Spells > Counterspell |
| 2 | 14 | -0.62 | yes | Spells > Shield |
| 3 | 19 | -0.89 | yes | Spells > Healing Word |
| 4 | 1 | -1.07 |  | Spells > School of Magic |
| 5 | 3 | -2.08 |  | Classes > Level 5 Paladin Spells |
| 6 | 12 | -2.23 |  | Classes > Level 2 Paladin Spells |
| 7 | 4 | -2.25 |  | Classes > Level 4 Paladin Spells |
| 8 | 7 | -2.38 |  | Classes > Level 3 Paladin Spells |
| 9 | 6 | -2.59 |  | Classes > Level 3 Warlock Spells |
| 10 | 10 | -2.93 |  | Classes > Level 4 Cleric Spells |
| 11 | 9 | -3.02 |  | Classes > Level 3 Sorcerer Spells |
| 12 | 8 | -3.23 |  | Classes > Level 5 Cleric Spells |
| 13 | 16 | -3.49 |  | Classes > Level 2 Cleric Spells |
| 14 | 13 | -3.54 |  | Classes > Level 8 Wizard Spells |
| 15 | 17 | -3.90 |  | Classes > Level 9 Cleric Spells |
| 16 | 11 | -3.91 |  | Classes > Level 3 Ranger Spells |
| 17 | 15 | -4.34 |  | Classes > Level 9 Warlock Spells |
| 18 | 20 | -4.98 |  | Classes > Level 3 Cleric Spells |
| 19 | 18 | -5.00 |  | Classes > Level 6 Wizard Spells |
| 20 | 5 | -6.67 |  | Classes > Level 3 Wizard Spells |

*retrieved sections:* Spells > Seeming | Spells > Counterspell | Spells > Hold Monster | Spells > Shield | Magic Items > Arrow-Catching Shield | Spells > Shield of Faith | Spells > Healing Word

<details><summary>full retrieved context</summary>

```
[Spells > Seeming]
#### Seeming  
_Level 5 Illusion (Bard, Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 30 feet
**Components:** V, S
**Duration:** 8 hours  
You give an illusory appearance to each creature of your choice that you can see within range. An unwilling target can make a Charisma saving throw, and if it succeeds, it is unaffected by this spell.

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Spells > Hold Monster]
#### Hold Monster  
_Level 5 Enchantment (Bard, Sorcerer, Warlock, Wizard)_  
**Casting Time:** Action
**Range:** 90 feet
**Components:** V, S, M (a straight piece of iron)
**Duration:** Concentration, up to 1 minute  
Choose a creature that you can see within range. The target must succeed on a Wisdom saving throw or have the Paralyzed condition for the duration. At the end of each of its turns, the target repeats the save, ending the spell on itself on a success.

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

[Magic Items > Arrow-Catching Shield]
#### Arrow-Catching Shield  
_Armor (Shield), Rare (Requires Attunement)_  
You gain a +2 bonus to Armor Class against ranged attack rolls while you wield this Shield. This bonus is in addition to the Shield's normal bonus to AC.  
Whenever an attacker makes a ranged attack roll against a target within 5 feet of you, you can take a Reaction to become the target of the attack instead.

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

[Spells > Counterspell]
#### Counterspell  
_Level 3 Abjuration (Sorcerer, Warlock, Wizard)_  
**Casting Time:** Reaction, which you take when you see a creature within 60 feet of yourself casting a spell with Verbal, Somatic, or Material components
**Range:** 90 feet
**Components:** S
**Duration:** Instantaneous

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


---

## q2 (multi-part) Give Fireball's damage dice, range and saving throw. Then for Revivify, give the material component and its cost, how recently the creature must have died, and how many Hit Points it revives with.

**Gold facts (counterfactual data):** 9d6; 120 feet; Dexterity; 500+ GP; within the last 10 minutes; 1 Hit Point


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Fireball:** 8d6 fire damage, range 150 feet, and a Dexterity saving throw. A creature takes half damage on a successful save.

**Revivify:**
- **Material component:** Diamonds worth 300 GP, which the spell consumes.
- **Recency:** The creature must have died within the last minute.
- **Hit Points on return:** It returns to life with 1 Hit Point.

*facts found (judge): 2/6; missing: 9d6; 120 feet; 500+ GP; within the last 10 minutes*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Fireball:** 9d6 Fire damage (half on a successful save), range 120 feet, Dexterity saving throw.

**Revivify:** The Context doesn't include the Revivify spell, so I can't give its material component, cost, time-of-death limit, or revived Hit Points.

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

**Fireball:** 9d6 Fire damage, 120-foot range, Dexterity saving throw (half damage on a success).

**Revivify:** The Context doesn't include the Revivify spell, so I can't give its material component, cost, recent-death window, or revived Hit Points.

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

**Fireball:**
- **Damage dice:** 9d6 Fire damage (half on a successful save)
- **Range:** 120 feet
- **Saving throw:** Dexterity

**Revivify:**
- **Material component:** A diamond worth 500+ GP, which the spell consumes
- **Cost:** 500+ GP
- **Time since death:** The creature must have died within the last 10 minutes.
- **Hit Points on revival:** 1

*facts found (judge): 3/6; missing: 9d6; 500+ GP; within the last 10 minutes*


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

**Fireball:**
- **Damage dice:** 9d6 Fire damage (half on a successful save)
- **Range:** 120 feet
- **Saving throw:** Dexterity

**Revivify:** The Context doesn't include a Revivify entry, so I can't give its material component, cost, how recently the creature must have died, or the Hit Points it revives with.

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

**Fireball:** Deals 9d6 Fire damage. Its range is 120 feet, and targets make a Dexterity saving throw. A failed save takes full damage, and a successful save takes half.

**Revivify:** The material component is a diamond worth 500+ GP, which the spell consumes. The creature must have died within the last 10 minutes. It revives with 1 Hit Point.

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

**Fireball:** Deals 9d6 Fire damage, has a range of 120 feet, and requires a Dexterity saving throw. A failed save takes the full damage, and a successful save takes half.

**Revivify:** The material component is a diamond worth 500+ GP, which the spell consumes. The creature must have died within the last 10 minutes, and it revives with 1 Hit Point.

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


### v6_agentic  (10 chunks, 3 LLM call(s))

**Fireball:** 9d6 Fire damage (half on a successful save), range 120 feet, Dexterity saving throw.

**Revivify:** The material component is a diamond worth 500+ GP, which the spell consumes. The creature must have died within the last 10 minutes, and it revives with 1 Hit Point.

*facts found (judge): 6/6; missing: none*

*agentic sub-queries:* Fireball spell damage dice range saving throw / Revivify spell material component cost / Revivify spell how recently died / Revivify spell hit points revived


*re-ranking* (query: `Fireball spell damage dice range saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | 5.40 | yes | Spells > Delayed Blast Fireball |
| 2 | 3 | 5.27 | yes | Spells > Delayed Blast Fireball |
| 3 | 18 | 5.25 | yes | Spells > Meteor Swarm |
| 4 | 1 | 5.07 | yes | Spells > Fireball |
| 5 | 10 | 4.74 |  | Spells > Searing Smite |
| 6 | 8 | 4.49 |  | Spells > Flame Strike |
| 7 | 12 | 4.41 |  | Spells > Harm |
| 8 | 11 | 3.93 |  | Spells > Chain Lightning |
| 9 | 19 | 3.29 |  | Spells > Flaming Sphere |
| 10 | 2 | 3.23 |  | Playing the Game > Damage against Multiple Targets |
| 11 | 17 | 3.17 |  | Spells > Sunburst |
| 12 | 15 | 2.61 |  | Spells > Inflict Wounds |
| 13 | 20 | 2.01 |  | Spells > Ice Knife |
| 14 | 16 | 0.20 |  | Spells > Prismatic Wall |
| 15 | 6 | -0.18 |  | Spells > Delayed Blast Fireball |
| 16 | 4 | -0.19 |  | Spells > Fireball |
| 17 | 9 | -0.58 |  | Magic Items > Necklace of Fireballs |
| 18 | 13 | -2.36 |  | Playing the Game > Damage Rolls |
| 19 | 7 | -2.67 |  | Spells > Delayed Blast Fireball |
| 20 | 14 | -3.62 |  | Magic Items > Staff of Power |


*re-ranking* (query: `Revivify spell material component cost`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 8 | 0.05 | yes | Spells > Revivify |
| 2 | 2 | -0.14 | yes | Spells > Material (M) |
| 3 | 3 | -0.65 | yes | Classes > Subtle Spell |
| 4 | 1 | -0.82 |  | Spells > Material (M) |
| 5 | 5 | -2.06 |  | Equipment > Spellcasting |
| 6 | 16 | -2.18 |  | Spells > Components |
| 7 | 20 | -3.22 |  | Classes > Level 18: Beast Spells |
| 8 | 7 | -3.59 |  | Spells > Creation |
| 9 | 4 | -4.06 |  | Equipment > Component Pouch (25 GP) |
| 10 | 6 | -4.52 |  | Spells > Material (M) |
| 11 | 17 | -5.83 |  | Classes > Level 3 Paladin Spells |
| 12 | 18 | -6.76 |  | Magic Items > Spell Scroll |
| 13 | 19 | -8.50 |  | Classes > Empowered Spell |
| 14 | 11 | -8.99 |  | Classes > Transmuted Spell |
| 15 | 9 | -9.21 |  | Classes > Seeking Spell |
| 16 | 13 | -9.53 |  | Equipment > Time and Cost |
| 17 | 10 | -10.14 |  | Magic Items > Time and Cost |
| 18 | 15 | -10.38 |  | Magic Items > Staff of Frost |
| 19 | 14 | -10.41 |  | Magic Items > Staff of Fire |
| 20 | 12 | -10.92 |  | Magic Items > Time and Cost |


*re-ranking* (query: `Revivify spell how recently died`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.40 | yes | Spells > Revivify |
| 2 | 13 | 1.28 | yes | Rules Glossary > Dead |
| 3 | 9 | -0.63 | yes | Spells > Resurrection |
| 4 | 8 | -1.41 |  | Classes > Level 3: Life Domain Spells |
| 5 | 7 | -1.79 |  | Spells > Raise Dead |
| 6 | 4 | -2.00 |  | Spells > True Resurrection |
| 7 | 15 | -2.08 | yes | Spells > Resurrection |
| 8 | 6 | -3.45 |  | Spells > Speak with Dead |
| 9 | 3 | -3.63 |  | Spells > Resurrection |
| 10 | 5 | -4.10 |  | Spells > True Resurrection |
| 11 | 14 | -5.06 |  | Spells > Gentle Repose |
| 12 | 11 | -5.29 |  | Classes > Level 3 Paladin Spells |
| 13 | 2 | -5.51 |  | Spells > Speak with Dead |
| 14 | 10 | -9.32 |  | Playing the Game > Skill Proficiencies |
| 15 | 17 | -9.50 |  | Spells > Wish |
| 16 | 19 | -9.54 |  | Spells > Gentle Repose |
| 17 | 20 | -10.15 |  | Classes > Level 7 Cleric Spells |
| 18 | 18 | -10.81 |  | Spells > Identify |
| 19 | 12 | -11.18 |  | Magic Items > Rod of Absorption |
| 20 | 16 | -11.26 |  | Character Creation > Fill In Numbers |


*re-ranking* (query: `Revivify spell hit points revived`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.93 | yes | Spells > Revivify |
| 2 | 14 | 5.62 | yes | Rules Glossary > Dead |
| 3 | 16 | 3.50 | yes | Spells > Resurrection |
| 4 | 15 | 3.38 |  | Playing the Game > Healing |
| 5 | 5 | 2.74 |  | Classes > Level 3: Disciple of Life |
| 6 | 7 | 2.66 |  | Spells > Disintegrate |
| 7 | 11 | 2.29 |  | Classes > Level 17: Supreme Healing |
| 8 | 3 | 2.20 |  | Classes > Level 6: Blessed Healer |
| 9 | 4 | 0.98 |  | Playing the Game > Healing |
| 10 | 6 | 0.54 |  | Spells > True Resurrection |
| 11 | 8 | 0.32 |  | Spells > Shapechange |
| 12 | 2 | 0.02 |  | Spells > Traits |
| 13 | 19 | -0.80 |  | Playing the Game > They're Not Hit Points or Healing |
| 14 | 13 | -2.24 |  | Classes > Level 1: Lay On Hands |
| 15 | 10 | -2.25 |  | Playing the Game > Temporary Hit Points |
| 16 | 18 | -2.26 |  | Spells > Greater Restoration |
| 17 | 20 | -2.45 | yes | Spells > Resurrection |
| 18 | 17 | -3.66 |  | Rules Glossary > Healing |
| 19 | 12 | -4.30 |  | Rules Glossary > Temporary Hit Points |
| 20 | 9 | -5.14 |  | Playing the Game > Lose Temporary Hit Points First |


*re-ranking* (query: `Fireball spell damage range saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 6.67 | yes | Spells > Delayed Blast Fireball |
| 2 | 4 | 6.46 | yes | Spells > Delayed Blast Fireball |
| 3 | 1 | 6.24 | yes | Spells > Fireball |
| 4 | 8 | 5.62 |  | Spells > Flame Strike |
| 5 | 13 | 5.51 |  | Spells > Searing Smite |
| 6 | 10 | 5.28 |  | Spells > Harm |
| 7 | 17 | 5.01 |  | Spells > Flaming Sphere |
| 8 | 11 | 4.84 |  | Spells > Chain Lightning |
| 9 | 18 | 4.56 |  | Spells > Sunburst |
| 10 | 5 | 3.50 |  | Playing the Game > Damage against Multiple Targets |
| 11 | 16 | 3.42 |  | Spells > Inflict Wounds |
| 12 | 20 | 3.26 |  | Spells > Ice Knife |
| 13 | 15 | 3.02 |  | Spells > Shatter |
| 14 | 14 | 1.83 |  | Spells > Freezing Sphere |
| 15 | 6 | 0.99 |  | Spells > Delayed Blast Fireball |
| 16 | 9 | 0.87 |  | Magic Items > Necklace of Fireballs |
| 17 | 3 | 0.80 |  | Spells > Fireball |
| 18 | 12 | -0.31 |  | Monsters A–Z > Actions |
| 19 | 7 | -0.94 |  | Spells > Delayed Blast Fireball |
| 20 | 19 | -3.31 |  | Magic Items > Staff of Power |

*retrieved sections:* Spells > Delayed Blast Fireball | Spells > Meteor Swarm | Spells > Revivify | Spells > Material (M) | Classes > Subtle Spell | Rules Glossary > Dead | Spells > Resurrection | Spells > Fireball

<details><summary>full retrieved context</summary>

```
[Spells > Delayed Blast Fireball]
The spell's base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn't ended.  
If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.

---

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Spells > Meteor Swarm]
**Duration:** Instantaneous  
Blazing orbs of fire plummet to the ground at four different points you can see within range. Each creature in a 40-foot-radius Sphere centered on each of those points makes a Dexterity saving throw. A creature takes 20d6 Fire damage and 20d6 Bludgeoning damage on a failed save or half as much damage on a successful one. A creature in the area of more than one fiery Sphere is affected only once.

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

[Spells > Material (M)]
### Material (M)  
A Material component is a particular material used in a spell's casting, as specified in parentheses in the Components entry. These materials aren't consumed by the spell unless the spell's description states otherwise. The spellcaster must have a hand free to access them, but it can be the same hand used to perform Somatic components, if any.

---

[Classes > Subtle Spell]
#### Subtle Spell  
_Cost: 1 Sorcery Point_  
When you cast a spell, you can spend 1 Sorcery Point to cast it without any Verbal, Somatic, or Material components, except Material components that are consumed by the spell or that have a cost specified in the spell.

---

[Rules Glossary > Dead]
#### Dead  
A dead creature has no Hit Points and can't regain them unless it is first revived by magic such as the _Raise Dead_ or _Revivify_ spell. When such a spell is cast, the spirit knows who is casting it and can refuse. The spirit of a dead creature has left the body and departed for the Outer Planes, and reviving the creature requires calling the spirit back.

---

[Spells > Resurrection]
Casting this spell to revive a creature that has been dead for 365 days or longer taxes you. Until you finish a Long Rest, you can't cast spells again, and you have Disadvantage on D20 Tests.

---

[Spells > Resurrection]
The creature returns to life with all its Hit Points. This spell also neutralizes any poisons that affected the creature at the time of death. This spell closes all mortal wounds and restores any missing body parts.  
Coming back from the dead is an ordeal. The target takes a −4 penalty to D20 Tests. Every time the target finishes a Long Rest, the penalty is reduced by 1 until it becomes 0.

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

## q3 (cross-file) What does the Alert feat let you add to your Initiative roll? And which background grants the Savage Attacker feat, what skill proficiencies does it give, and how often per turn can Savage Attacker be used?

**Gold facts (counterfactual data):** twice your Proficiency Bonus; Soldier; Athletics and Perception; Twice per turn


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Alert:** When you roll Initiative, you can add your Proficiency Bonus to the roll.

**Background:** Soldier grants the Savage Attacker feat. It gives proficiency in **Athletics** and **Intimidation**.

**Savage Attacker frequency:** Once per turn. When you hit with a weapon, you roll that weapon's damage dice twice and use either result against the target.

*facts found (judge): 1/4; missing: twice your Proficiency Bonus; Athletics and Perception; Twice per turn*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Alert:** You can add twice your Proficiency Bonus to your Initiative roll.

**Background granting Savage Attacker:** The Context doesn't say which background grants this feat, so I can't answer.

**Skill proficiencies:** The Context doesn't list any skill proficiencies, so I can't answer.

**Savage Attacker frequency:** Twice per turn, when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll.

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

The Alert feat lets you add **twice your Proficiency Bonus** to your Initiative roll.

The Context does not say which background grants Savage Attacker or what skill proficiencies that background gives, so I can't answer those parts. The Context only describes the Savage Attacker feat itself.

Savage Attacker can be used **twice per turn**, when you hit a target with a weapon. You roll the weapon's damage dice twice and use either roll against the target.

*facts found (judge): 2/4; missing: Soldier; Athletics and Perception*


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
| 8 | 10 | -6.39 |  | Monsters A–Z > Reactions |
| 9 | 8 | -8.34 |  | Monsters A–Z > Actions |
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

**Alert:** When you roll Initiative, you can add twice your Proficiency Bonus to the roll.

**Savage Attacker:**
- **Background that grants it:** The Context doesn't say. It describes Savage Attacker as an Origin Feat but doesn't list which backgrounds grant it.
- **Skill proficiencies:** The Context doesn't include this, since it doesn't cover any background.
- **Frequency:** Twice per turn. When you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

*facts found (judge): 2/4; missing: Soldier; Athletics and Perception*


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
| 8 | 10 | -6.39 | yes | Monsters A–Z > Reactions |
| 9 | 8 | -8.34 |  | Monsters A–Z > Actions |
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

**Alert:** You can add twice your Proficiency Bonus to your Initiative roll.

**Background granting Savage Attacker:** The Context doesn't say. It describes the Savage Attacker feat but doesn't list any backgrounds.

**Skill proficiencies:** The Context doesn't include this. It doesn't mention any background, so it has no skill proficiencies to report.

**Savage Attacker frequency:** Twice per turn. When you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

*facts found (judge): 2/4; missing: Soldier; Athletics and Perception*


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

The Alert feat lets you add **twice your Proficiency Bonus** to your Initiative roll.

The **Soldier** background grants the Savage Attacker feat. Its skill proficiencies are **Athletics and Perception**. Savage Attacker can be used **twice per turn**, when you hit a target with a weapon.

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

**1. Alert and Initiative:** When you roll Initiative, you can add twice your Proficiency Bonus to the roll.

**2. Savage Attacker:**
- **Background:** The Soldier origin grants the Savage Attacker feat. The Context calls these "Character Origins" rather than backgrounds.
- **Skill proficiencies:** Athletics and Perception.
- **Frequency:** Twice per turn, when you hit a target with a weapon, you can roll the weapon's damage dice twice and use either roll against the target.

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


### v6_agentic  (16 chunks, 3 LLM call(s))

The Alert feat lets you add **twice your Proficiency Bonus** to your Initiative roll.

The **Soldier** background grants the Savage Attacker feat. It gives **Athletics and Perception** as skill proficiencies. You can use Savage Attacker **twice per turn** when you hit a target with a weapon.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Alert feat / Savage Attacker feat / Initiative roll / Soldier background / Entertainer background / Half-Orc


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


*re-ranking* (query: `Soldier background`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | 3.67 | yes | Character Creation > Choose a Background |
| 2 | 1 | 3.02 | yes | Character Creation > Choose a Background |
| 3 | 2 | -1.14 | yes | Character Origins > Soldier |
| 4 | 12 | -4.29 |  | Gameplay Toolbox > Creating a Background |
| 5 | 18 | -5.24 |  | Monsters A–Z > Warrior Infantry |
| 6 | 9 | -5.61 | yes | Character Origins > Character Backgrounds |
| 7 | 13 | -5.71 |  | Gameplay Toolbox > 1: Choose Abilities |
| 8 | 16 | -6.45 |  | Monsters A–Z > Warrior Infantry |
| 9 | 3 | -7.81 |  | Character Creation > Choose a Background |
| 10 | 4 | -7.88 |  | Character Origins > Parts of a Background |
| 11 | 8 | -8.19 |  | Character Origins > Feat |
| 12 | 6 | -8.34 |  | Character Origins > Equipment |
| 13 | 7 | -8.42 |  | Character Origins > Skill Proficiencies |
| 14 | 14 | -8.81 |  | Character Creation > Step 2: Character Origin |
| 15 | 10 | -8.85 |  | Character Creation > Choose a Background |
| 16 | 11 | -9.34 |  | Character Origins > Tool Proficiency |
| 17 | 15 | -9.46 |  | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 18 | 17 | -9.84 |  | Classes > Ranger Class Features |
| 19 | 19 | -9.85 |  | Classes > Ranger |
| 20 | 20 | -10.12 |  | Classes > Paladin Class Features |


*re-ranking* (query: `Entertainer background`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 15 | -2.02 | yes | Equipment > Entertainer's Pack (40 GP) |
| 2 | 5 | -5.90 | yes | Character Origins > Character Backgrounds |
| 3 | 10 | -6.75 | yes | Classes > Bard |
| 4 | 16 | -6.79 |  | Gameplay Toolbox > Creating a Background |
| 5 | 8 | -7.54 | yes | Character Creation > Choose a Background |
| 6 | 17 | -7.55 |  | Gameplay Toolbox > 1: Choose Abilities |
| 7 | 3 | -7.68 |  | Character Origins > Feat |
| 8 | 4 | -7.89 | yes | Character Creation > Choose a Background |
| 9 | 1 | -8.03 |  | Character Origins > Parts of a Background |
| 10 | 7 | -8.03 |  | Character Creation > Step 2: Character Origin |
| 11 | 2 | -8.22 |  | Character Creation > Choose a Background |
| 12 | 6 | -8.81 |  | Character Origins > Skill Proficiencies |
| 13 | 11 | -9.04 |  | Character Creation > Choose a Background |
| 14 | 9 | -9.10 |  | Character Origins > Equipment |
| 15 | 13 | -9.71 |  | Character Origins > Tool Proficiency |
| 16 | 14 | -10.20 |  | Character Creation > Choose a Background |
| 17 | 19 | -10.26 |  | Gameplay Toolbox > 3: Choose Skill Proficiencies |
| 18 | 18 | -10.36 |  | Character Creation > Trinkets |
| 19 | 12 | -10.44 |  | Character Creation > Imagine Your Past and Present |
| 20 | 20 | -10.96 |  | Character Creation > Trinkets |


*re-ranking* (query: `Half-Orc`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | -0.93 | yes | Character Creation > Choose a Species |
| 2 | 4 | -1.74 | yes | Character Origins > Orc |
| 3 | 8 | -3.51 | yes | Character Origins > Orc |
| 4 | 1 | -4.57 |  | Monsters A–Z > Half-Dragon |
| 5 | 2 | -5.38 |  | Monsters A–Z > Half-Dragon |
| 6 | 5 | -5.68 |  | Character Origins > Halfling |
| 7 | 11 | -6.71 |  | Character Creation > Choose Languages |
| 8 | 13 | -7.71 |  | Playing the Game > Half Damage |
| 9 | 9 | -8.87 |  | Character Creation > Choose Languages |
| 10 | 17 | -9.36 |  | Spells > Prismatic Spray |
| 11 | 20 | -9.62 |  | Magic Items > Ring of Shooting Stars |
| 12 | 15 | -10.47 |  | Spells > Reincarnate |
| 13 | 14 | -11.15 |  | Monsters A–Z > Doppelganger |
| 14 | 18 | -11.18 |  | Monsters A–Z > Gladiator |
| 15 | 16 | -11.21 |  | Monsters A–Z > Incubus |
| 16 | 10 | -11.23 |  | Monsters A–Z > Centaur Trooper |
| 17 | 19 | -11.24 |  | Animals > Plesiosaurus |
| 18 | 3 | -11.33 |  | Monsters A–Z > Zombie |
| 19 | 7 | -11.39 |  | Monsters A–Z > Blink Dog |
| 20 | 12 | -11.42 |  | Monsters A–Z > Centaur Trooper |

*retrieved sections:* Feats > Alert | Character Origins > Criminal | Magic Items > Rod of Alertness | Feats > Savage Attacker | Character Origins > Soldier | Feats > Great Weapon Fighting | Rules Glossary > Initiative | Playing the Game > Initiative | Character Creation > Choose a Background | Equipment > Entertainer's Pack (40 GP) | Character Origins > Character Backgrounds | Classes > Bard | Character Creation > Choose a Species | Character Origins > Orc

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

[Character Origins > Criminal]
#### Criminal  
**Ability Scores:** Dexterity, Constitution, Intelligence
**Feat:** Alert (see "Feats")
**Skill Proficiencies:** Sleight of Hand and Stealth
**Tool Proficiency:** Thieves' Tools
**Equipment:** _Choose A or B:_ (A) 2 Daggers, Thieves' Tools, Crowbar, 2 Pouches, Traveler's Clothes, 16 GP; or (B) 50 GP

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

[Rules Glossary > Initiative]
#### Initiative  
Initiative determines the order of turns during combat. The combat rules in "Playing the Game" explain how to roll Initiative.  
Sometimes a GM might have combatants use their Initiative scores instead of rolling Initiative. Your Initiative score equals 10 plus your Dexterity modifier. If you have Advantage on Initiative rolls, increase your Initiative score by 5. If you have Disadvantage on those rolls, decrease that score by 5. _See also_ "Playing the Game" ("Combat").

---

[Playing the Game > Initiative]
#### Initiative  
Initiative determines the order of turns during combat. When combat starts, every participant rolls Initiative; they make a Dexterity check that determines their place in the Initiative order. The GM rolls for monsters. For a group of identical creatures, the GM makes a single roll, so each member of the group has the same Initiative.

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

[Equipment > Entertainer's Pack (40 GP)]
#### Entertainer's Pack (40 GP)  
An Entertainer's Pack contains the following items: Backpack, Bedroll, Bell, Bullseye Lantern, 3 Costumes, Mirror, 8 flasks of Oil, 9 days of Rations, Tinderbox, and Waterskin.

---

[Character Origins > Character Backgrounds]
# Character Origins  
## Character Backgrounds  
Your character's background is a collection of characteristics that represent the place and occupation that were most formative before your character embarked on a life of adventure.

---

[Classes > Bard]
</tr>
<tr>
<td>Armor Training</td>
<td>Light armor</td>
</tr>
<tr>
<td>Starting Equipment</td>
<td>Choose A or B: (A) Leather Armor, 2 Daggers, Musical Instrument of your choice, Entertainer's Pack, and 19 GP; or (B) 90 GP</td>
</tr>
</tbody>
</table>

---

[Character Creation > Choose a Species]
#### Choose a Species  
Choose a species for your character. The following species options are detailed in "Character Origins": Dragonborn, Dwarf, Elf, Gnome, Goliath, Halfling, Human, Orc, and Tiefling. Once you've chosen a species, write it on your character sheet. Then record your species' traits.

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

[Character Origins > Orc]
_Darkvision._ You have Darkvision with a range of 120 feet.  
_Relentless Endurance._ When you are reduced to 0 Hit Points but not killed outright, you can drop to 1 Hit Point instead. Once you use this trait, you can't do so again until you finish a Long Rest.
```
</details>


---

## q4 (cross-file) How much weight and volume can a Bag of Holding hold, and how much does the bag itself weigh? Also, what bonus does a Cloak of Protection give and does it need attunement?

**Gold facts (counterfactual data):** 800 pounds; 96 cubic feet; 5 pounds; +2 bonus to Armor Class; Requires Attunement


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Bag of Holding:** It can hold up to **500 pounds** and **64 cubic feet** of material. The bag itself weighs **15 pounds**, regardless of what's inside. If you exceed the weight or volume limit, the bag tears and is destroyed, and its contents are scattered in the Astral Plane.

**Cloak of Protection:** It gives a **+1 bonus to AC and to saving throws**. It **does require attunement**.

*facts found (judge): 1/5; missing: 800 pounds; 96 cubic feet; 5 pounds; +2 bonus to Armor Class*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Bag of Holding:** It can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds, regardless of its contents.

**Cloak of Protection:** The Context doesn't include the Cloak of Protection, so I can't say what bonus it gives or whether it requires attunement.

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

**Bag of Holding:** It can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds regardless of its contents.

**Cloak of Protection:** The Context doesn't include a Cloak of Protection entry, so I can't say what bonus it gives or whether it requires attunement.

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

Bag of Holding: It can hold up to 800 pounds, not exceeding a volume of 96 cubic feet. The bag itself weighs 5 pounds, regardless of its contents.

Cloak of Protection: It gives a +2 bonus to Armor Class and saving throws while worn. Yes, it requires attunement.

*facts found (judge): 5/5; missing: none*


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

**Bag of Holding:** It holds up to 800 pounds and no more than 96 cubic feet of material. The bag itself weighs 5 pounds regardless of its contents.

**Cloak of Protection:** The Context doesn't include a Cloak of Protection, so I can't say what bonus it gives or whether it requires attunement.

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

**Bag of Holding:** It holds up to 800 pounds, not exceeding 96 cubic feet. The bag itself weighs 5 pounds, regardless of its contents.

**Cloak of Protection:** The Context doesn't include this item, so I can't say what bonus it gives or whether it requires attunement.

*facts found (judge): 1/5; missing: 800 pounds; 96 cubic feet; +2 bonus to Armor Class; Requires Attunement*


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

A **Bag of Holding** can hold up to **800 pounds**, not exceeding a volume of **96 cubic feet**. The bag itself weighs **5 pounds**, regardless of its contents.

A **Cloak of Protection** gives a **+2 bonus to Armor Class and saving throws** while worn. **Yes, it requires attunement.**

*facts found (judge): 4/5; missing: Requires Attunement*


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


### v6_agentic  (9 chunks, 3 LLM call(s))

A Bag of Holding can hold up to **800 pounds** and no more than **96 cubic feet** of volume. The bag itself weighs **5 pounds**, regardless of its contents.

A Cloak of Protection gives a **+2 bonus to Armor Class and saving throws** while worn. It **does require attunement**.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* Bag of Holding weight capacity / Bag of Holding volume / Bag of Holding weight / Cloak of Protection bonus / Cloak of Protection attunement


*re-ranking* (query: `Bag of Holding weight capacity`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.02 | yes | Magic Items > Bag of Holding |
| 2 | 5 | -0.94 | yes | Magic Items > Bag of Holding |
| 3 | 3 | -2.26 | yes | Rules Glossary > Carrying Capacity |
| 4 | 20 | -2.76 |  | Magic Items > Handy Haversack |
| 5 | 12 | -3.39 | yes | Magic Items > Bag of Holding |
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


*re-ranking* (query: `Bag of Holding volume`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.34 | yes | Magic Items > Bag of Holding |
| 2 | 3 | 2.22 | yes | Magic Items > Bag of Holding |
| 3 | 8 | 0.31 | yes | Magic Items > Bag of Holding |
| 4 | 2 | -0.76 |  | Magic Items > Bag of Devouring |
| 5 | 6 | -1.31 |  | Magic Items > Bag of Devouring |
| 6 | 4 | -2.46 |  | Magic Items > Handy Haversack |
| 7 | 16 | -4.86 |  | Monsters A–Z > Traits |
| 8 | 20 | -5.69 |  | Equipment > Sack (1 CP) |
| 9 | 13 | -5.71 |  | Magic Items > Magic Item Categories |
| 10 | 18 | -6.34 |  | Equipment > Pouch (5 SP) |
| 11 | 12 | -7.64 |  | Magic Items > Bag of Beans |
| 12 | 7 | -7.82 |  | Magic Items > Bag of Beans |
| 13 | 9 | -7.91 |  | Magic Items > Bag of Tricks |
| 14 | 14 | -8.05 |  | Magic Items > Bag of Tricks |
| 15 | 11 | -8.24 |  | Magic Items > Bag of Tricks |
| 16 | 5 | -8.34 |  | Magic Items > Bag of Devouring |
| 17 | 10 | -8.47 |  | Magic Items > Bag of Devouring |
| 18 | 15 | -8.65 |  | Magic Items > Bag of Beans |
| 19 | 19 | -8.70 |  | Equipment > Vial (1 GP) |
| 20 | 17 | -9.43 |  | Equipment > Bucket (5 CP) |


*re-ranking* (query: `Bag of Holding weight`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 8.17 | yes | Magic Items > Bag of Holding |
| 2 | 4 | 2.09 | yes | Magic Items > Bag of Holding |
| 3 | 10 | -0.26 | yes | Magic Items > Bag of Holding |
| 4 | 2 | -0.86 |  | Magic Items > Bag of Devouring |
| 5 | 19 | -2.10 |  | Magic Items > Handy Haversack |
| 6 | 7 | -2.68 |  | Magic Items > Bag of Devouring |
| 7 | 3 | -2.98 |  | Magic Items > Bag of Beans |
| 8 | 20 | -4.13 |  | Monsters A–Z > Traits |
| 9 | 18 | -5.08 |  | Equipment > Other Tools |
| 10 | 6 | -5.23 |  | Magic Items > Bag of Devouring |
| 11 | 5 | -7.02 |  | Magic Items > Bag of Devouring |
| 12 | 15 | -7.29 |  | Magic Items > Bag of Tricks |
| 13 | 11 | -7.42 | yes | Rules Glossary > Carrying Capacity |
| 14 | 9 | -8.11 |  | Magic Items > Bag of Tricks |
| 15 | 14 | -8.32 |  | Magic Items > Bag of Beans |
| 16 | 8 | -8.39 |  | Magic Items > Bag of Tricks |
| 17 | 17 | -8.61 |  | Magic Items > Immovable Rod |
| 18 | 13 | -9.79 |  | Magic Items > Bead of Force |
| 19 | 16 | -10.55 |  | Equipment > Block and Tackle (1 GP) |
| 20 | 12 | -10.69 |  | Equipment > Mounts and Cargo |


*re-ranking* (query: `Cloak of Protection bonus`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.76 | yes | Magic Items > Cloak of Protection |
| 2 | 17 | 0.52 | yes | Classes > Level 6: Aura of Protection |
| 3 | 5 | 0.50 | yes | Magic Items > Scarab of Protection |
| 4 | 2 | 0.02 |  | Magic Items > Ring of Protection |
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


*re-ranking* (query: `Cloak of Protection attunement`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.07 | yes | Magic Items > Cloak of Protection |
| 2 | 3 | 4.43 | yes | Magic Items > Cloak of Invisibility |
| 3 | 4 | 3.82 | yes | Magic Items > Cloak of Displacement |
| 4 | 9 | 3.24 |  | Magic Items > Cloak of Arachnida |
| 5 | 2 | 3.15 |  | Magic Items > Cloak of Elvenkind |
| 6 | 8 | 3.03 |  | Magic Items > Cloak of the Bat |
| 7 | 5 | 1.97 |  | Magic Items > Cloak of the Manta Ray |
| 8 | 6 | 1.86 |  | Magic Items > Mantle of Spell Resistance |
| 9 | 11 | 1.23 | yes | Magic Items > Scarab of Protection |
| 10 | 16 | 1.08 |  | Magic Items > Brooch of Shielding |
| 11 | 7 | 0.53 |  | Magic Items > Ring of Protection |
| 12 | 13 | 0.47 |  | Equipment > Attunement |
| 13 | 10 | -0.19 |  | Magic Items > Wings of Flying |
| 14 | 14 | -1.35 |  | Equipment > No More Than Three Items |
| 15 | 17 | -2.38 |  | Magic Items > Bracers of Defense |
| 16 | 19 | -2.97 |  | Magic Items > Armor of Invulnerability |
| 17 | 18 | -5.41 |  | Magic Items > Hat of Disguise |
| 18 | 12 | -7.26 |  | Magic Items > Cloak of the Bat |
| 19 | 15 | -8.99 |  | Spells > Protection from Evil and Good |
| 20 | 20 | -10.86 |  | Magic Items > Conflict |

*retrieved sections:* Magic Items > Bag of Holding | Rules Glossary > Carrying Capacity | Magic Items > Cloak of Protection | Classes > Level 6: Aura of Protection | Magic Items > Scarab of Protection | Magic Items > Cloak of Invisibility | Magic Items > Cloak of Displacement

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

[Magic Items > Bag of Holding]
Placing a _Bag of Holding_ inside an extradimensional space created by a _Handy Haversack_, _Portable Hole_, or similar item instantly destroys both items and opens a gate to the Astral Plane. The gate originates where the one item was placed inside the other. Any creature within a 10-foot-radius Sphere centered on the gate is sucked through it to a random location on the Astral Plane. The gate then closes. The gate is one-way and can't be reopened.

---

[Magic Items > Cloak of Protection]
#### Cloak of Protection  
_Wondrous Item, Uncommon (Requires Attunement)_  
You gain a +2 bonus to Armor Class and saving throws while you wear this cloak.

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
```
</details>


---

## q5 (cross-file) Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points, what does the Owlbear's Multiattack consist of, and what is its CR?

**Gold facts (counterfactual data):** AC 17; 3d6; AC 15; 7d10 + 28; two Rend attacks; CR 3


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Goblin Warrior:** I don't recognize "Goblin Warrior" as a stat block in the 2024 SRD 5.2. The closest match is the **Goblin**, with **AC 15** (leather armor and shield) and **7 HP** (2d6). If you meant a different goblin, let me know.

**Owlbear:** **AC 13** (natural armor) and **59 HP** (7d10 + 21).

**Owlbear's Multiattack:** The owlbear makes two attacks, one with its Beak and one with its Claws.

**Owlbear's CR:** **3** (700 XP).

*facts found (judge): 2/6; missing: AC 17; 3d6; 7d10 + 28; two Rend attacks*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Goblin Warrior:** The Context has no AC or Hit Points for it. It has no stat block named "Goblin Warrior," only an Actions section for "goblin," and that section doesn't include AC, Hit Points, or CR.

**Owlbear:**
- **AC:** Not in the Context.
- **Hit Points:** Not in the Context.
- **Multiattack:** The owlbear makes two Rend attacks.
- **CR:** Not in the Context.

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

**Goblin Warrior:** The Context has no "Goblin Warrior" entry. The closest match is the "warrior" block, which does not give AC, Hit Points, or CR.

**Owlbear:** The Context gives no AC, Hit Points, or CR. Its Multiattack is two Rend attacks.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 2 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 4 | -7.11 | yes | Monsters A–Z > Actions |
| 4 | 3 | -8.03 |  | Animals > Actions |
| 5 | 8 | -8.95 |  | Monsters A–Z > Actions |
| 6 | 10 | -8.99 |  | Monsters A–Z > Actions |
| 7 | 6 | -9.05 |  | Monsters A–Z > Actions |
| 8 | 7 | -9.36 |  | Monsters A–Z > Actions |
| 9 | 9 | -9.54 |  | Monsters > Multiattack |
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


### v2b_rerank8  (8 chunks, 1 LLM call(s))

**Goblin Warrior:** The Context has no AC, Hit Points, or CR for it. It also has no entry titled "Goblin Warrior." It has a goblin entry (Scimitar and Shortbow) and a separate warrior entry (Greatsword and Heavy Crossbow), and I can't tell from the Context whether they're the same creature.

**Owlbear:** The Context has no AC, Hit Points, or CR for it.

**Owlbear Multiattack:** "The owlbear makes two Rend attacks." Rend is a melee attack roll of +7 with reach 5 ft., hitting for 14 (2d8 + 5) Slashing damage.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 2 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 4 | -7.11 | yes | Monsters A–Z > Actions |
| 4 | 3 | -8.03 | yes | Animals > Actions |
| 5 | 8 | -8.95 | yes | Monsters A–Z > Actions |
| 6 | 10 | -8.99 |  | Monsters A–Z > Actions |
| 7 | 6 | -9.05 | yes | Monsters A–Z > Actions |
| 8 | 7 | -9.36 | yes | Monsters A–Z > Actions |
| 9 | 9 | -9.54 | yes | Monsters > Multiattack |
| 10 | 5 | -9.93 |  | Animals > Giant Owl |

*retrieved sections:* Monsters A–Z > Actions | Animals > Actions | Monsters > Multiattack

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
**_Multiattack._** The pseudodragon makes two Bite attacks.  
**_Bite._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 4 (1d4 + 2) Piercing damage.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The tough makes two attacks, using Warhammer or Heavy Crossbow in any combination.  
**_Warhammer._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 12 (2d8 + 3) Bludgeoning damage. If the target is a Large or smaller creature, the tough pushes the target up to 10 feet straight away from itself.  
**_Heavy Crossbow._** _Ranged Attack Roll:_ +4, range 100/400 ft. _Hit:_ 13 (2d10 + 2) Piercing damage.

---

[Monsters > Multiattack]
#### Multiattack  
Some creatures can make more than one attack when they take the Attack action. Such creatures have the Multiattack entry in the "Actions" section of their stat block. This entry details the attacks a creature can make, as well as any additional abilities it can use, as part of the Attack action.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

**Goblin Warrior:** The Context has no AC or Hit Points for it. It also doesn't name a "Goblin Warrior." It has a goblin entry (Scimitar and Shortbow attacks) and a separate warrior entry (Greatsword and Heavy Crossbow attacks), with no stated link between them.

**Owlbear:** The Context doesn't give its AC or Hit Points. Its Multiattack is two Rend attacks.

**CR:** The Context doesn't give a Challenge Rating for either creature.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 2 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 4 | -7.11 | yes | Monsters A–Z > Actions |
| 4 | 3 | -8.03 |  | Animals > Actions |
| 5 | 8 | -8.95 |  | Monsters A–Z > Actions |
| 6 | 10 | -8.99 |  | Monsters A–Z > Actions |
| 7 | 6 | -9.05 |  | Monsters A–Z > Actions |
| 8 | 7 | -9.36 |  | Monsters A–Z > Actions |
| 9 | 9 | -9.54 |  | Monsters > Multiattack |
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

**Goblin Warrior:**
- AC: Not in the Context.
- Hit Points: Not in the Context.
- CR: 1/4 (XP 50).

**Owlbear:**
- AC: Not in the Context.
- Hit Points: Not in the Context.
- Multiattack: The owlbear makes two Rend attacks.
- CR: Not in the Context.

*facts found (judge): 1/6; missing: AC 17; 3d6; AC 15; 7d10 + 28; CR 3*


*re-ranking* (query: `Compare the Goblin Warrior and the Owlbear: what is each one's AC and Hit Points`): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.56 | yes | Monsters A–Z > Actions |
| 2 | 3 | -3.62 | yes | Monsters A–Z > Actions |
| 3 | 4 | -5.16 | yes | Monsters A–Z > Bugbear Warrior |
| 4 | 11 | -5.21 | yes | Monsters A–Z > Reactions |
| 5 | 2 | -5.56 | yes | Monsters A–Z > Goblin Warrior |
| 6 | 7 | -5.74 | yes | Rules Glossary > Stat Block |
| 7 | 24 | -6.45 | yes | Spells > Wall of Stone |
| 8 | 30 | -7.02 | yes | Monsters A–Z > Legendary Actions |
| 9 | 28 | -7.05 |  | Monsters A–Z > Traits |
| 10 | 6 | -7.11 |  | Monsters A–Z > Actions |
| 11 | 22 | -7.27 |  | Monsters > Hit Points |
| 12 | 15 | -7.47 |  | Monsters A–Z > Reactions |
| 13 | 13 | -7.71 |  | Monsters A–Z > Reactions |
| 14 | 5 | -8.03 |  | Animals > Actions |
| 15 | 14 | -8.95 |  | Monsters A–Z > Actions |
| 16 | 18 | -8.99 |  | Monsters A–Z > Actions |
| 17 | 27 | -8.99 |  | Monsters A–Z > Actions |
| 18 | 10 | -9.05 |  | Monsters A–Z > Actions |
| 19 | 25 | -9.07 |  | Animals > Giant Owl |
| 20 | 21 | -9.13 |  | Monsters A–Z > Actions |

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

**Goblin Warrior:** AC 17, HP 10 (3d6)
**Owlbear:** AC 15, HP 66 (7d10 + 28)

**Owlbear Multiattack:** The owlbear makes two Rend attacks.

**Owlbear CR:** The Context doesn't include it. The Owlbear's stat block is cut off before its CR line.

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


### v6_agentic  (13 chunks, 3 LLM call(s))

**Goblin Warrior:** AC 17, HP 10 (3d6)

**Owlbear:** AC 15, HP 66 (7d10 + 28)

**Owlbear Multiattack:** The owlbear makes two Rend attacks.

**Owlbear CR:** 3 (XP 700; PB +2)

*facts found (judge): 6/6; missing: none*

*agentic sub-queries:* Goblin Warrior stat block / Owlbear stat block / Owlbear Multiattack / Owlbear challenge rating / Goblin challenge rating

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Goblin Warrior stat block`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | 0.84 | yes | Monsters A–Z > Goblin Warrior |
| 2 | 2 | -0.41 | yes | Monsters A–Z > Goblin Warrior |
| 3 | 6 | -0.54 | yes | Monsters A–Z > Goblin Warrior |
| 4 | 3 | -0.74 | yes | Monsters > Stat Block Overview |
| 5 | 16 | -1.63 | yes | Rules Glossary > Stat Block |
| 6 | 20 | -1.64 |  | Monsters > Gear |
| 7 | 4 | -1.69 | yes | Monsters A–Z > Bugbear Warrior |
| 8 | 19 | -2.56 |  | Monsters A–Z > Actions |
| 9 | 8 | -2.60 |  | Monsters > Stat Block Overview |
| 10 | 18 | -3.64 |  | Magic Items > Magic Items A–Z |
| 11 | 7 | -3.99 |  | Monsters > Resistances and Vulnerabilities |
| 12 | 10 | -4.34 |  | Monsters > Limited Usage |
| 13 | 12 | -4.42 |  | Monsters > Damage Notation |
| 14 | 1 | -4.47 |  | Monsters > Parts of a Stat Block |
| 15 | 17 | -4.72 |  | Monsters A–Z > Goblin Minion |
| 16 | 11 | -4.93 |  | Monsters A–Z > Reactions |
| 17 | 15 | -5.21 |  | Monsters A–Z > Hobgoblin Warrior |
| 18 | 14 | -6.16 |  | Monsters A–Z > Bugbear Stalker |
| 19 | 9 | -6.30 |  | Monsters A–Z > Traits |
| 20 | 13 | -6.38 |  | Monsters > Limited Usage |


*re-ranking* (query: `Owlbear stat block`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | -0.23 | yes | Monsters A–Z > Actions |
| 2 | 6 | -0.47 | yes | Monsters A–Z > Owlbear |
| 3 | 3 | -2.57 | yes | Rules Glossary > Stat Block |
| 4 | 2 | -2.66 | yes | Monsters > Stat Block Overview |
| 5 | 10 | -3.59 |  | Rules Glossary > Stat Block |
| 6 | 5 | -3.87 |  | Classes > Level 2: Wild Shape |
| 7 | 15 | -4.95 |  | Classes > Level 2: Wild Shape |
| 8 | 11 | -5.13 |  | Monsters > Damage Notation |
| 9 | 14 | -5.27 |  | Monsters > Stat Block Overview |
| 10 | 17 | -5.47 |  | Rules Glossary > Stat Block |
| 11 | 13 | -5.61 |  | Rules Glossary > Stat Block |
| 12 | 1 | -5.66 |  | Monsters > Parts of a Stat Block |
| 13 | 8 | -5.80 |  | Rules Glossary > Stat Block |
| 14 | 20 | -6.05 |  | Monsters > Stat Block Overview |
| 15 | 7 | -6.11 |  | Monsters > Limited Usage |
| 16 | 19 | -6.43 |  | Rules Glossary > Stat Block |
| 17 | 12 | -6.77 |  | Monsters > Resistances and Vulnerabilities |
| 18 | 18 | -7.77 |  | Monsters > Multiattack |
| 19 | 16 | -8.66 |  | Monsters > Limited Usage |
| 20 | 9 | -8.77 |  | Monsters A–Z > Traits |


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


*re-ranking* (query: `Owlbear challenge rating`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 0.29 | yes | Monsters A–Z > Owlbear |
| 2 | 1 | -1.07 | yes | Monsters > Challenge Rating |
| 3 | 16 | -1.23 | yes | Rules Glossary > Challenge Rating |
| 4 | 4 | -2.50 | yes | Monsters A–Z > Owlbear |
| 5 | 11 | -2.87 | yes | Rules Glossary > Stat Block |
| 6 | 7 | -3.06 |  | Rules Glossary > Challenge Rating |
| 7 | 3 | -4.09 |  | Monsters > Proficiency Bonus |
| 8 | 18 | -5.97 |  | Monsters > Experience Points |
| 9 | 10 | -6.16 |  | Rules Glossary > Challenge Rating |
| 10 | 14 | -7.08 |  | Playing the Game > Proficiency |
| 11 | 20 | -7.68 |  | Spells > True Polymorph |
| 12 | 6 | -7.94 |  | Gameplay Toolbox > Step 1: Choose a Difficulty |
| 13 | 5 | -8.41 |  | Gameplay Toolbox > Unusual Features |
| 14 | 9 | -8.44 |  | Animals > Giant Owl |
| 15 | 12 | -8.79 |  | Animals > Owl |
| 16 | 8 | -9.01 |  | Animals > Giant Owl |
| 17 | 13 | -9.12 |  | Spells > Shapechange |
| 18 | 15 | -9.43 |  | Animals > Owl |
| 19 | 19 | -10.91 |  | Animals > Giant Eagle |
| 20 | 17 | -10.93 |  | Monsters > Experience Points |


*re-ranking* (query: `Goblin challenge rating`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.33 | yes | Monsters > Challenge Rating |
| 2 | 19 | -0.12 | yes | Rules Glossary > Stat Block |
| 3 | 17 | -1.99 |  | Rules Glossary > Challenge Rating |
| 4 | 8 | -2.13 |  | Monsters > Proficiency Bonus |
| 5 | 2 | -3.23 | yes | Monsters A–Z > Goblin Warrior |
| 6 | 4 | -3.25 |  | Monsters A–Z > Goblin Minion |
| 7 | 14 | -3.43 |  | Monsters > Experience Points |
| 8 | 12 | -3.83 | yes | Monsters A–Z > Goblin Warrior |
| 9 | 10 | -4.15 | yes | Monsters A–Z > Bugbear Warrior |
| 10 | 18 | -4.22 |  | Rules Glossary > Challenge Rating |
| 11 | 3 | -4.33 |  | Playing the Game > Proficiency |
| 12 | 11 | -4.62 |  | Monsters A–Z > Goblin Minion |
| 13 | 7 | -4.65 |  | Monsters A–Z > Bonus Actions |
| 14 | 13 | -4.78 |  | Monsters A–Z > Bugbear Stalker |
| 15 | 5 | -5.26 |  | Gameplay Toolbox > Step 1: Choose a Difficulty |
| 16 | 15 | -5.34 |  | Monsters A–Z > Hobgoblin Captain |
| 17 | 20 | -5.44 |  | Spells > Shapechange |
| 18 | 6 | -5.89 |  | Gameplay Toolbox > Unusual Features |
| 19 | 9 | -7.09 |  | Monsters > Resistances and Vulnerabilities |
| 20 | 16 | -10.79 |  | Monsters A–Z > Worg |


*re-ranking* (query: `Owlbear challenge rating`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 0.29 | yes | Monsters A–Z > Owlbear |
| 2 | 1 | -1.07 | yes | Monsters > Challenge Rating |
| 3 | 16 | -1.23 | yes | Rules Glossary > Challenge Rating |
| 4 | 4 | -2.50 | yes | Monsters A–Z > Owlbear |
| 5 | 11 | -2.87 | yes | Rules Glossary > Stat Block |
| 6 | 7 | -3.06 |  | Rules Glossary > Challenge Rating |
| 7 | 3 | -4.09 |  | Monsters > Proficiency Bonus |
| 8 | 18 | -5.97 |  | Monsters > Experience Points |
| 9 | 10 | -6.16 |  | Rules Glossary > Challenge Rating |
| 10 | 14 | -7.08 |  | Playing the Game > Proficiency |
| 11 | 20 | -7.68 |  | Spells > True Polymorph |
| 12 | 6 | -7.94 |  | Gameplay Toolbox > Step 1: Choose a Difficulty |
| 13 | 5 | -8.41 |  | Gameplay Toolbox > Unusual Features |
| 14 | 9 | -8.44 |  | Animals > Giant Owl |
| 15 | 12 | -8.79 |  | Animals > Owl |
| 16 | 8 | -9.01 |  | Animals > Giant Owl |
| 17 | 13 | -9.12 |  | Spells > Shapechange |
| 18 | 15 | -9.43 |  | Animals > Owl |
| 19 | 19 | -10.91 |  | Animals > Giant Eagle |
| 20 | 17 | -10.93 |  | Monsters > Experience Points |


*re-ranking* (query: `Owlbear CR XP`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.27 | yes | Monsters A–Z > Owlbear |
| 2 | 1 | -0.11 | yes | Monsters A–Z > Owlbear |
| 3 | 15 | -1.67 | yes | Monsters A–Z > Bugbear Warrior |
| 4 | 12 | -2.09 |  | Monsters A–Z > Bugbear Stalker |
| 5 | 9 | -3.81 |  | Gameplay Toolbox > CR 0 Creatures |
| 6 | 4 | -5.19 |  | Monsters A–Z > Hell Hound |
| 7 | 7 | -5.27 |  | Monsters A–Z > Otyugh |
| 8 | 6 | -5.69 |  | Monsters A–Z > Chimera |
| 9 | 3 | -5.90 |  | Monsters A–Z > Pegasus |
| 10 | 5 | -6.23 |  | Monsters A–Z > Mage |
| 11 | 8 | -6.58 |  | Monsters A–Z > Blink Dog |
| 12 | 20 | -6.74 |  | Monsters A–Z > Winter Wolf |
| 13 | 17 | -6.87 |  | Monsters A–Z > Green Hag |
| 14 | 13 | -6.89 |  | Monsters A–Z > Zombie |
| 15 | 16 | -7.13 |  | Monsters A–Z > Gladiator |
| 16 | 10 | -7.16 |  | Monsters A–Z > Gargoyle |
| 17 | 11 | -7.34 |  | Monsters A–Z > Ghast |
| 18 | 18 | -7.43 |  | Monsters A–Z > Remorhaz |
| 19 | 19 | -7.51 |  | Monsters A–Z > Centaur Trooper |
| 20 | 14 | -7.76 |  | Monsters A–Z > Sphinx of Wonder |

*retrieved sections:* Monsters A–Z > Goblin Warrior | Monsters A–Z > Owlbear | Rules Glossary > Stat Block | Monsters > Stat Block Overview | Monsters A–Z > Actions | Monsters > Challenge Rating | Rules Glossary > Challenge Rating | Monsters A–Z > Bugbear Warrior

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

[Monsters A–Z > Goblin Warrior]
**Languages** Common, Goblin<br>
**CR** 1/4 (XP 50; PB +2)

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

[Rules Glossary > Stat Block]
#### Stat Block  
A stat block contains the game statistics of a monster. Each stat block includes the following information presented after the monster's name.  
_Size._ A monster is Tiny, Small, Medium, Large, Huge, or Gargantuan. _See also_ "Size."  
_Creature Type._ This entry notes the family of beings a monster belongs to, along with any descriptive tags. _See also_ "Creature Type."

---

[Monsters > Stat Block Overview]
# Monsters  
## Stat Block Overview  
A monster has a stat block that contains the rules necessary to use it in the game. Stat blocks are divided into the following parts:  
**Name and General Details.** The name of the monster is followed by its size, creature type (along with any descriptive tags), and alignment.  
**Combat Highlights.** Armor Class, Hit Points, Speed, and Initiative are provided here.

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

[Monsters > Challenge Rating]
### Challenge Rating  
Challenge Rating is defined in "Rules Glossary," while guidance on using CR to plan potential combat encounters is in "Gameplay Toolbox."

---

[Rules Glossary > Challenge Rating]
Challenge Rating (CR) summarizes the threat a monster poses to a group of four player characters. Compare a monster's CR to the characters' level. If the CR is higher, the monster is likely a danger. If the CR is lower, the monster likely poses little threat. But circumstances and the number of player characters can significantly alter how threatening a monster is in actual play. "Gameplay Toolbox" ("Combat Encounters") provides guidance to the GM on using CR while planning potential combat

---

[Rules Glossary > Stat Block]
_CR._ Challenge Rating summarizes the threat a monster poses and is detailed in "Monsters." The Experience Points characters receive for defeating a monster and its Proficiency Bonus follow. Some creatures that are created by magic have no CR. _See also_ "Challenge Rating" and "Experience Points."  
_Traits._ The monster's traits, if any, are features that are active at all times or in certain situations.

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

[Monsters A–Z > Bugbear Warrior]
**Languages** Common, Goblin<br>
**CR** 1 (XP 200; PB +2)
```
</details>


---

## q6 (multi-part) What AC do you get wearing Chain Mail, how much does Plate Armor sell for, and how much raw material is needed to make Plate Armor?

**Gold facts (counterfactual data):** 16 in Chain Mail; 1,500 GP; 750 GP


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Chain Mail:** AC 16 (Heavy armor, requires Strength 13, imposes disadvantage on Stealth).

**Plate Armor:** Sells for **1,500 GP** (Heavy armor, AC 18, requires Strength 15, imposes disadvantage on Stealth).

**Raw material to craft Plate Armor:** Raw materials cost **750 GP**, which is half the item's price. Crafting also requires proficiency with the appropriate tools (Smith's Tools for metal armor).

*facts found (judge): 3/3; missing: none*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Chain Mail AC:** The context doesn't say. The armor table excerpt is cut off before the Chain Mail row.

**Plate Armor price:** 1,500 GP.

**Raw materials for Plate Armor:** 750 GP, which is half its purchase cost.

*facts found (judge): 2/3; missing: 16 in Chain Mail*

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

Wearing Chain Mail gives you an AC of **16**. Plate Armor sells for **1,500 GP**. Making Plate Armor requires **750 GP** in raw materials.

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

You get an AC of **16** wearing Chain Mail. Plate Armor sells for **1,500 GP**. You need **750 GP** of raw materials to make Plate Armor.

*facts found (judge): 3/3; missing: none*


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

Wearing Chain Mail, your AC is **16**. Plate Armor sells for **1,500 GP**. Making Plate Armor requires **750 GP** of raw materials.

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

Wearing Chain Mail, your AC is **16**. Plate Armor sells for **1,500 GP**, and making it requires **750 GP** in raw materials.

*facts found (judge): 3/3; missing: none*


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

- **Chain Mail AC:** 16 (no Dexterity modifier applies).
- **Plate Armor sale price:** 1,500 GP.
- **Raw materials to make Plate Armor:** 750 GP, which is half its purchase cost.

*facts found (judge): 3/3; missing: none*


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


### v6_agentic  (8 chunks, 3 LLM call(s))

Wearing Chain Mail, your AC is **16**. Plate Armor sells for **1,500 GP**. Making Plate Armor requires **750 GP** of raw materials, which is half its purchase cost, rounded down.

*facts found (judge): 3/3; missing: none*

*agentic sub-queries:* Chain Mail AC / Plate Armor price / Plate Armor crafting


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
| 7 | 6 | -3.89 |  | Magic Items > Armor of Invulnerability |
| 8 | 9 | -4.61 |  | Equipment > Armor |
| 9 | 8 | -4.82 |  | Magic Items > Armor |
| 10 | 17 | -5.23 |  | Equipment > Barding |
| 11 | 10 | -6.41 |  | Equipment > Armor |
| 12 | 19 | -7.76 |  | Equipment > Armor |
| 13 | 13 | -9.79 |  | Magic Items > Armor, +1, +2, or +3 |
| 14 | 16 | -9.89 |  | Magic Items > Glamoured Studded Leather |
| 15 | 15 | -9.92 |  | Magic Items > Demon Armor |
| 16 | 20 | -9.95 | yes | Equipment > Armor |
| 17 | 12 | -10.25 |  | Magic Items > Mithral Armor |
| 18 | 18 | -10.49 |  | Magic Items > Adamantine Armor |
| 19 | 14 | -10.65 | yes | Magic Items > Elven Chain |
| 20 | 11 | -10.96 |  | Character Creation > Note Armor Training |


*re-ranking* (query: `Plate Armor crafting`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 3.79 | yes | Magic Items > Time and Cost |
| 2 | 1 | 1.05 | yes | Magic Items > Dwarven Plate |
| 3 | 7 | 0.31 | yes | Magic Items > Plate Armor of Etherealness |
| 4 | 5 | -0.04 |  | Magic Items > Armor of Invulnerability |
| 5 | 3 | -0.24 | yes | Equipment > Raw Materials |
| 6 | 10 | -1.21 |  | Magic Items > Armor |
| 7 | 4 | -2.22 |  | Equipment > Armor |
| 8 | 17 | -4.52 |  | Equipment > Barding |
| 9 | 6 | -5.03 |  | Equipment > Armor |
| 10 | 16 | -7.87 |  | Equipment > Armor |
| 11 | 9 | -8.10 |  | Equipment > Tools |
| 12 | 8 | -8.36 |  | Equipment > Crafting Nonmagical Items |
| 13 | 12 | -8.59 |  | Character Creation > Note Armor Training |
| 14 | 18 | -9.10 |  | Magic Items > Mithral Armor |
| 15 | 20 | -9.21 |  | Equipment > Armor |
| 16 | 11 | -9.58 |  | Equipment > Time |
| 17 | 13 | -9.85 |  | Magic Items > Time and Cost |
| 18 | 19 | -9.90 | yes | Magic Items > Elven Chain |
| 19 | 15 | -10.51 |  | Magic Items > Time and Cost |
| 20 | 14 | -11.01 |  | Magic Items > Spells |

*retrieved sections:* Equipment > Armor | Magic Items > Elven Chain | Classes > Paladin | Magic Items > Magic Item Values by Rarity | Magic Items > Time and Cost | Equipment > Raw Materials | Magic Items > Dwarven Plate | Magic Items > Plate Armor of Etherealness

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
```
</details>


---

## q7 (multi-part) What are the effects of the Grappled condition on Speed and on attacks, and what are the effects of the Prone condition on movement and on attack rolls against you?

**Gold facts (counterfactual data):** Speed is 0; other than the grappler; crawl; half your Speed; within 5 feet


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Grappled**
- **Speed:** Your Speed becomes 0, and you can't benefit from any bonus to your Speed.
- **Attacks:** The condition doesn't impose any attack penalty. You can still attack normally, though you're limited by your Speed of 0 for movement.

**Prone**
- **Movement:** You can only crawl, and each foot you crawl costs 1 extra foot of movement. Standing up costs up to half your Speed, so you can't stand if your Speed is 0.
- **Your own attacks:** You have disadvantage on attack rolls.
- **Attacks against you:** Attack rolls against you have advantage if the attacker is within 5 feet of you. Otherwise, they have disadvantage.

*facts found (judge): 4/5; missing: other than the grappler*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Grappled:**
- **Speed:** Your Speed is 0 and can't increase.
- **Attacks:** You have Disadvantage on attack rolls against any target other than the grappler.

**Prone:**
- **Movement:** The Context doesn't say what Prone does to movement. It only covers attacks.
- **Attack rolls against you:** The attack has Advantage if the attacker is within 5 feet of you, and Disadvantage otherwise.

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

**Grappled:** Your Speed is 0 and can't increase. You have Disadvantage on attack rolls against any target other than the grappler.

**Prone:** Your only movement options are to crawl, or to spend movement equal to half your Speed (rounded down) to right yourself and end the condition. If your Speed is 0, you can't right yourself. The Context doesn't say anything about attack rolls against a prone creature, so that part of the question can't be answered from it.

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

**Grappled:**
- **Speed:** Your Speed is 0 and can't increase.
- **Attacks:** You have Disadvantage on attack rolls against any target other than the grappler.

**Prone:**
- **Movement:** You can only crawl, or spend movement equal to half your Speed (round down) to right yourself and end the condition. If your Speed is 0, you can't right yourself.
- **Attack rolls against you:** An attack roll against you has Advantage if the attacker is within 5 feet of you. Otherwise, it has Disadvantage. This comes from a second Prone excerpt in the Context. The main Prone entry doesn't address attacks against you.

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

**Grappled:**
- **Speed:** Your Speed is 0 and can't increase.
- **Attacks:** You have Disadvantage on attack rolls against any target other than the grappler.

**Prone:**
- **Movement:** Your only movement options are to crawl, or to spend movement equal to half your Speed (rounded down) to right yourself and end the condition. If your Speed is 0, you can't right yourself.
- **Attack rolls against you:** The Context doesn't say. The Prone entry covers only movement, so this part of the question can't be answered from the provided text.

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

**Grappled:**
- **Speed:** Your Speed is 0 and can't increase.
- **Attacks:** You have Disadvantage on attack rolls against any target other than the grappler.

**Prone:**
- **Movement:** Your only movement options are to crawl, or to spend movement equal to half your Speed (rounded down) to right yourself and end the condition. If your Speed is 0, you can't right yourself.
- **Attack rolls against you:** The Context doesn't say. The Prone entry covers only movement.

*facts found (judge): 3/5; missing: crawl; within 5 feet*


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

**Grappled:**
- **Speed:** Your Speed is 0 and can't increase.
- **Attacks:** You have Disadvantage on attack rolls against any target other than the grappler.

**Prone:**
- **Movement:** Your only options are to crawl, or to spend movement equal to half your Speed (rounded down) to right yourself and end the condition. If your Speed is 0, you can't right yourself.
- **Attack rolls against you:** They have Advantage if the attacker is within 5 feet of you. Otherwise, they have Disadvantage.

*facts found (judge): 5/5; missing: none*


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


### v6_agentic  (15 chunks, 3 LLM call(s))

**Grappled:**
- **Speed:** Your Speed is 0 and can't increase.
- **Attacks:** You have Disadvantage on attack rolls against any target other than the grappler.

**Prone:**
- **Movement:** Your only options are to crawl, or to spend movement equal to half your Speed (rounded down) to right yourself and end the condition. If your Speed is 0, you can't right yourself.
- **Attack rolls against you:** They have Advantage if the attacker is within 5 feet of you. Otherwise, they have Disadvantage.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* Grappled condition / Grappled speed / Grappled attack rolls / Prone condition / Prone movement / Prone attack rolls


*re-ranking* (query: `Grappled condition`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.66 | yes | Rules Glossary > Grappled [Condition] |
| 2 | 3 | 5.21 | yes | Rules Glossary > Grappling |
| 3 | 2 | 5.20 | yes | Rules Glossary > Grappling |
| 4 | 4 | 4.25 | yes | Animals > Actions |
| 5 | 20 | 3.96 |  | Monsters A–Z > Actions |
| 6 | 6 | 3.94 | yes | Animals > Actions |
| 7 | 13 | 3.65 |  | Monsters A–Z > Actions |
| 8 | 7 | 3.31 | yes | Monsters A–Z > Bonus Actions |
| 9 | 15 | 3.27 |  | Monsters A–Z > Actions |
| 10 | 19 | 2.98 |  | Monsters A–Z > Actions |
| 11 | 11 | 2.94 |  | Animals > Actions |
| 12 | 14 | 2.87 |  | Rules Glossary > Condition |
| 13 | 5 | 2.85 |  | Monsters A–Z > Actions |
| 14 | 9 | 2.69 |  | Animals > Actions |
| 15 | 12 | 2.10 |  | Monsters A–Z > Actions |
| 16 | 18 | 2.05 |  | Monsters A–Z > Actions |
| 17 | 8 | 1.57 |  | Monsters A–Z > Actions |
| 18 | 10 | 1.50 |  | Monsters A–Z > Actions |
| 19 | 17 | 1.48 |  | Monsters A–Z > Actions |
| 20 | 16 | 0.82 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Grappled speed`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.25 | yes | Rules Glossary > Grappled [Condition] |
| 2 | 5 | 1.57 | yes | Monsters A–Z > Bonus Actions |
| 3 | 9 | 1.01 | yes | Monsters A–Z > Bonus Actions |
| 4 | 16 | 1.01 |  | Monsters A–Z > Actions |
| 5 | 3 | 0.40 | yes | Feats > Grappler |
| 6 | 2 | 0.23 | yes | Rules Glossary > Grappling |
| 7 | 6 | 0.21 | yes | Animals > Actions |
| 8 | 4 | 0.10 | yes | Animals > Actions |
| 9 | 7 | -0.10 | yes | Rules Glossary > Grappling |
| 10 | 10 | -0.64 |  | Monsters A–Z > Actions |
| 11 | 20 | -0.87 |  | Animals > Actions |
| 12 | 8 | -0.95 |  | Animals > Actions |
| 13 | 15 | -1.29 |  | Animals > Actions |
| 14 | 14 | -1.37 |  | Monsters A–Z > Actions |
| 15 | 17 | -1.76 |  | Monsters A–Z > Bonus Actions |
| 16 | 12 | -1.94 |  | Monsters A–Z > Actions |
| 17 | 19 | -2.46 |  | Monsters A–Z > Bonus Actions |
| 18 | 11 | -2.80 |  | Monsters A–Z > Bonus Actions |
| 19 | 13 | -3.11 |  | Monsters A–Z > Actions |
| 20 | 18 | -3.32 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Grappled attack rolls`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 6.12 | yes | Feats > Grappler |
| 2 | 4 | 5.93 | yes | Animals > Actions |
| 3 | 6 | 5.83 | yes | Animals > Actions |
| 4 | 9 | 5.47 |  | Monsters A–Z > Actions |
| 5 | 14 | 5.43 |  | Monsters A–Z > Actions |
| 6 | 13 | 5.28 |  | Monsters A–Z > Actions |
| 7 | 1 | 5.24 | yes | Rules Glossary > Grappled [Condition] |
| 8 | 10 | 5.22 |  | Animals > Actions |
| 9 | 8 | 5.16 |  | Monsters A–Z > Actions |
| 10 | 7 | 5.08 |  | Monsters A–Z > Actions |
| 11 | 5 | 5.03 |  | Animals > Actions |
| 12 | 18 | 4.81 |  | Monsters A–Z > Actions |
| 13 | 20 | 4.79 |  | Monsters A–Z > Actions |
| 14 | 12 | 4.64 |  | Monsters A–Z > Actions |
| 15 | 11 | 4.45 |  | Monsters A–Z > Actions |
| 16 | 2 | 2.33 |  | Playing the Game > Attack Rolls |
| 17 | 19 | 0.72 |  | Classes > Level 2: Reckless Attack |
| 18 | 15 | -0.17 |  | Spells > Attack Rolls |
| 19 | 17 | -0.69 |  | Rules Glossary > Invisible [Condition] |
| 20 | 16 | -1.28 |  | Magic Items > Ring of Elemental Command |


*re-ranking* (query: `Prone condition`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.20 | yes | Rules Glossary > Prone [Condition] |
| 2 | 2 | 3.88 | yes | Playing the Game > Dropping Prone |
| 3 | 4 | 3.68 | yes | Gameplay Toolbox > Rolling Stone |
| 4 | 9 | 3.40 |  | Rules Glossary > Unconscious [Condition] |
| 5 | 8 | 2.43 |  | Spells > Grease |
| 6 | 7 | 2.33 |  | Animals > Bonus Actions |
| 7 | 17 | 2.31 |  | Spells > Earthquake |
| 8 | 5 | 2.30 | yes | Animals > Actions |
| 9 | 16 | 2.26 |  | Playing the Game > Falling Off |
| 10 | 3 | 2.14 | yes | Animals > Actions |
| 11 | 10 | 2.03 |  | Monsters A–Z > Bonus Actions |
| 12 | 13 | 1.98 |  | Monsters A–Z > Bonus Actions |
| 13 | 6 | 1.98 |  | Animals > Actions |
| 14 | 19 | 1.57 |  | Rules Glossary > Condition |
| 15 | 11 | 1.22 | yes | Rules Glossary > Prone [Condition] |
| 16 | 18 | 0.89 |  | Monsters A–Z > Bonus Actions |
| 17 | 15 | 0.75 |  | Monsters A–Z > Bonus Actions |
| 18 | 12 | 0.27 |  | Animals > Actions |
| 19 | 20 | -0.22 |  | Animals > Actions |
| 20 | 14 | -0.91 |  | Spells > Hideous Laughter |


*re-ranking* (query: `Prone movement`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.56 | yes | Rules Glossary > Prone [Condition] |
| 2 | 12 | 1.83 | yes | Monsters A–Z > Legendary Actions |
| 3 | 2 | 1.28 | yes | Playing the Game > Dropping Prone |
| 4 | 18 | 1.01 |  | Monsters A–Z > Bonus Actions |
| 5 | 14 | 0.44 |  | Monsters A–Z > Bonus Actions |
| 6 | 15 | 0.25 |  | Monsters A–Z > Actions |
| 7 | 13 | -0.23 |  | Animals > Actions |
| 8 | 20 | -0.42 |  | Monsters A–Z > Actions |
| 9 | 16 | -0.53 |  | Monsters A–Z > Actions |
| 10 | 17 | -0.54 |  | Monsters A–Z > Bonus Actions |
| 11 | 19 | -0.63 |  | Monsters A–Z > Bonus Actions |
| 12 | 11 | -0.78 |  | Playing the Game > Falling Off |
| 13 | 5 | -1.50 | yes | Animals > Actions |
| 14 | 10 | -1.53 |  | Rules Glossary > Unconscious [Condition] |
| 15 | 9 | -1.60 | yes | Gameplay Toolbox > Rolling Stone |
| 16 | 4 | -1.68 |  | Spells > Grease |
| 17 | 3 | -1.81 | yes | Animals > Actions |
| 18 | 6 | -2.17 |  | Animals > Actions |
| 19 | 8 | -2.42 |  | Animals > Bonus Actions |
| 20 | 7 | -6.28 |  | Playing the Game > Movement and Position |


*re-ranking* (query: `Prone attack rolls`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.34 | yes | Rules Glossary > Prone [Condition] |
| 2 | 3 | 5.88 | yes | Animals > Actions |
| 3 | 4 | 5.51 | yes | Animals > Actions |
| 4 | 10 | 5.49 |  | Monsters A–Z > Actions |
| 5 | 5 | 5.47 |  | Animals > Actions |
| 6 | 9 | 5.29 |  | Monsters A–Z > Actions |
| 7 | 16 | 4.83 |  | Monsters A–Z > Actions |
| 8 | 20 | 4.79 |  | Monsters A–Z > Actions |
| 9 | 6 | 4.34 |  | Animals > Actions |
| 10 | 18 | 4.29 |  | Monsters A–Z > Actions |
| 11 | 8 | 3.97 |  | Rules Glossary > Unconscious [Condition] |
| 12 | 7 | 3.41 |  | Magic Items > Giant Slayer |
| 13 | 2 | 3.37 |  | Playing the Game > Attack Rolls |
| 14 | 14 | 2.30 |  | Classes > Level 2: Reckless Attack |
| 15 | 13 | 1.42 |  | Rules Glossary > Invisible [Condition] |
| 16 | 11 | 1.09 |  | Spells > Attack Rolls |
| 17 | 17 | -0.55 |  | Magic Items > Staff of the Magi |
| 18 | 15 | -0.90 |  | Magic Items > Defender |
| 19 | 19 | -1.04 |  | Magic Items > Staff of Power |
| 20 | 12 | -1.21 |  | Magic Items > Ring of Elemental Command |

*retrieved sections:* Rules Glossary > Grappled [Condition] | Rules Glossary > Grappling | Monsters A–Z > Bonus Actions | Feats > Grappler | Animals > Actions | Rules Glossary > Prone [Condition] | Playing the Game > Dropping Prone | Gameplay Toolbox > Rolling Stone | Monsters A–Z > Legendary Actions

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Grappled [Condition]]
#### Grappled [Condition]  
While you have the Grappled condition, you experience the following effects.  
_Speed 0._ Your Speed is 0 and can't increase.  
_Attacks Affected._ You have Disadvantage on attack rolls against any target other than the grappler.  
_Movable._ The grappler can drag or carry you when it moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than it.

---

[Rules Glossary > Grappling]
_Ending a Grapple._ A Grappled creature can use its action to make a Strength (Athletics) or Dexterity (Acrobatics) check against the grapple's escape DC, ending the condition on itself on a success. The condition also ends if the grappler has the Incapacitated condition or if the distance between the Grappled target and the grappler exceeds the grapple's range. In addition, the grappler can release the target at any time (no action required).

---

[Rules Glossary > Grappling]
#### Grappling  
A creature can grapple another creature. Characters typically grapple by using an Unarmed Strike. Many monsters have special attacks that allow them to quickly grapple prey. However a grapple is initiated, it follows these rules. _See also_ "Unarmed Strike" and "Grappled."  
_Grappled Condition._ Successfully grappling a creature gives it the Grappled condition.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Swoop (Recharge 5–6)._** If the roc has a creature Grappled, the roc flies up to half its Fly Speed without provoking Opportunity Attacks and drops that creature.

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Quick Grapple._** _Dexterity Saving Throw:_ DC 13, one Medium or smaller creature the bugbear can see within 10 feet. _Failure:_ The target has the Grappled condition (escape DC 13).

---

[Feats > Grappler]
_Attack Advantage._ You have Advantage on attack rolls against a creature Grappled by you.  
_Fast Wrestler._ You don't have to spend extra movement to move a creature Grappled by you if the creature is your size or smaller.

---

[Animals > Actions]
### Actions  
<hr>  
**_Bite._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 6 (1d8 + 2) Piercing damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 12). While Grappled, the target has the Restrained condition.

---

[Animals > Actions]
### Actions  
<hr>  
**_Tentacles._** _Melee Attack Roll:_ +5, reach 10 ft. _Hit:_ 10 (2d6 + 3) Bludgeoning damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 13) from all eight tentacles. While Grappled, the target has the Restrained condition.

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

[Monsters A–Z > Legendary Actions]
**_World-Shaking Movement._** The tarrasque moves up to its Speed. At the end of this movement, the tarrasque creates an instantaneous shock wave in a 60-foot Emanation originating from itself. Creatures in that area lose Concentration and, if Medium or smaller, have the Prone condition. The tarrasque can't take this action again until the start of its next turn.

---

[Rules Glossary > Prone [Condition]]
_Attacks Affected._ You have Disadvantage on attack rolls. An attack roll against you has Advantage if the attacker is within 5 feet of you. Otherwise, that attack roll has Disadvantage.

---

[Animals > Actions]
**_Tail._** _Melee Attack Roll:_ +10, reach 15 ft. _Hit:_ 25 (4d8 + 7) Bludgeoning damage. If the target is a Huge or smaller creature, it has the Prone condition.

---

[Animals > Actions]
### Actions  
<hr>  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 10 (2d6 + 3) Slashing damage. If the target is a Large or smaller creature, it has the Prone condition.
```
</details>


---

## q8 (multi-part) When can you make an Opportunity Attack and what does it cost? And what are the minimum lengths of a Long Rest (including how much must be sleep) and of a Short Rest, and how long must you wait between Long Rests?

**Gold facts (counterfactual data):** Reaction; at least 10 hours; at least 6 hours; 16 hours; 2-hour


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Opportunity Attack:** You can make one as a **Reaction** when a creature you can see moves out of your reach. The attack is a melee attack against that creature. It costs your Reaction, and you can't make one if you've already used it this round. Taking the Disengage action avoids triggering them.

**Long Rest:** At least **8 hours**, during which you sleep for at least **6 hours**. The rest can include up to 2 hours of light activity, such as reading, eating, drinking, or keeping watch. You can benefit from only **one Long Rest in a 24-hour period**.

**Short Rest:** At least **1 hour**, spent doing light activity.

*facts found (judge): 3/5; missing: at least 10 hours; 16 hours*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Opportunity Attacks:** You can make one when a creature you can see leaves your reach by using its action, Bonus Action, Reaction, or one of its speeds. It costs your Reaction. You make one melee attack with a weapon or an Unarmed Strike against that creature, and the attack occurs right before it leaves your reach.

**Long Rest:** The minimum length is 10 hours. Of that, you must sleep at least 6 hours, and no more than 2 hours may be light activity such as reading, talking, eating, or standing watch. You must wait at least 16 hours after finishing a Long Rest before starting another.

**Short Rest:** The length is 2 hours. The Context doesn't specify a minimum for a Short Rest beyond that fixed duration.

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

**Opportunity Attacks:** You can make one when a creature you can see leaves your reach, whether it moves using its action, Bonus Action, Reaction, or one of its speeds. It costs your **Reaction**. The attack is one melee attack with a weapon or an Unarmed Strike against that creature, and it occurs right before the creature leaves your reach.

**Rests:** The Context doesn't include any rules for Long Rests or Short Rests. It doesn't give their minimum lengths, the required sleep for a Long Rest, or how long you must wait between Long Rests.

*facts found (judge): 1/5; missing: at least 10 hours; at least 6 hours; 16 hours; 2-hour*


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

**Opportunity Attacks:** You can make one when a creature you can see leaves your reach, whether it moves, or uses its action, Bonus Action, Reaction, or one of its speeds. It costs your **Reaction**. You make one melee attack with a weapon or an Unarmed Strike against that creature, and the attack happens right before it leaves your reach.

**Long Rest:** The minimum length is **at least 10 hours**, and you must sleep for **at least 6 hours**. The other time can include no more than 2 hours of light activity, such as reading, talking, eating, or standing watch. You must wait **at least 16 hours** after finishing a Long Rest before starting another one.

**Short Rest:** It is a **2-hour** period of downtime. The Context does not give a separate minimum for sleep during a Short Rest.

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

**Opportunity Attacks:** You can make one when a creature you can see leaves your reach, whether it uses its action, Bonus Action, Reaction, or one of its speeds. It costs your **Reaction**. The attack is one melee attack with a weapon or an Unarmed Strike against that creature, and it happens right before the creature leaves your reach.

**Rests:** The Context doesn't include rules for Long Rests or Short Rests, so I can't give their minimum lengths, the required sleep, or how long you must wait between Long Rests.

*facts found (judge): 1/5; missing: at least 10 hours; at least 6 hours; 16 hours; 2-hour*


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

**Opportunity Attacks:** You can make one when a creature you can see leaves your reach, whether it moves with its action, Bonus Action, Reaction, or one of its speeds. It costs your Reaction, and the attack must be a melee attack with a weapon or an Unarmed Strike. The attack occurs right before the creature leaves your reach.

**Long Rest:** It must last at least 10 hours. Within that time, you must sleep for at least 6 hours and may perform no more than 2 hours of light activity, such as reading, talking, eating, or standing watch. After finishing a Long Rest, you must wait at least 16 hours before starting another.

**Short Rest:** The Context doesn't state a minimum length for a Short Rest, so I can't answer that part.

*facts found (judge): 5/5; missing: none*


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

**Opportunity Attacks:** You can make one when a creature you can see leaves your reach. It can leave by using its action, Bonus Action, Reaction, or one of its speeds. The attack costs your Reaction and must be a single melee attack with a weapon or an Unarmed Strike against that creature. It happens right before the creature leaves your reach. Once you use your Reaction, you can't take another until the start of your next turn.

**Long Rest:** The minimum length is 10 hours. Of that, you must sleep for at least 6 hours, and you may spend no more than 2 hours on light activity such as reading, talking, eating, or standing watch. After you finish a Long Rest, you must wait at least 16 hours before starting another.

**Short Rest:** The minimum length is 2 hours, during which you do nothing more strenuous than reading, talking, eating, or standing watch.

The Resting sidebar describes hour-long Short Rests and an 8-hour Long Rest, which conflicts with the Rules Glossary figures above. The Glossary is the section that provides the rules for both rests, so I've used its values.

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

**Opportunity Attacks:** You can make one when a creature you can see leaves your reach using its action, Bonus Action, Reaction, or one of its speeds. It costs your Reaction. The attack is one melee attack with a weapon or an Unarmed Strike against that creature, and it happens right before the creature leaves your reach.

**Long Rest:** The minimum length is at least 10 hours. Of that, you must sleep at least 6 hours, and you may perform no more than 2 hours of light activity. The Context also says an Elf can finish a Long Rest in 4 hours by spending those hours in a trancelike meditation.

**Short Rest:** The minimum length is a 2-hour period.

**Between Long Rests:** After you finish a Long Rest, you must wait at least 16 hours before starting another one.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* Opportunity Attack / Opportunity Attack reaction cost / Long Rest / Long Rest minimum duration sleep / Short Rest / Short Rest minimum duration


*re-ranking* (query: `Opportunity Attack`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 9.38 | yes | Rules Glossary > Opportunity Attacks |
| 2 | 2 | 8.41 | yes | Playing the Game > Opportunity Attacks |
| 3 | 4 | 8.32 | yes | Playing the Game > Opportunity Attacks |
| 4 | 1 | 7.71 |  | Playing the Game > Opportunity Attacks |
| 5 | 5 | 6.31 | yes | Rules Glossary > Reaction |
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


*re-ranking* (query: `Opportunity Attack reaction cost`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 1.61 | yes | Rules Glossary > Opportunity Attacks |
| 2 | 7 | 0.95 | yes | Rules Glossary > Reaction |
| 3 | 2 | 0.03 | yes | Playing the Game > Opportunity Attacks |
| 4 | 1 | -0.20 |  | Playing the Game > Opportunity Attacks |
| 5 | 9 | -0.31 |  | Classes > Level 5: Cunning Strike |
| 6 | 3 | -0.83 |  | Playing the Game > Reactions |
| 7 | 4 | -2.23 | yes | Playing the Game > Opportunity Attacks |
| 8 | 11 | -3.10 |  | Monsters A–Z > Traits |
| 9 | 5 | -4.60 |  | Playing the Game > Actions |
| 10 | 14 | -6.71 |  | Animals > Traits |
| 11 | 18 | -6.96 |  | Animals > Traits |
| 12 | 19 | -7.08 |  | Monsters A–Z > Bonus Actions |
| 13 | 20 | -7.09 |  | Animals > Traits |
| 14 | 16 | -7.30 |  | Animals > Traits |
| 15 | 15 | -10.33 |  | Equipment > Acid (25 GP) |
| 16 | 8 | -10.76 |  | Monsters A–Z > Reactions |
| 17 | 13 | -11.27 |  | Monsters A–Z > Actions |
| 18 | 10 | -11.29 |  | Monsters A–Z > Actions |
| 19 | 12 | -11.35 |  | Monsters A–Z > Actions |
| 20 | 17 | -11.37 |  | Monsters A–Z > Actions |


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
| 12 | 8 | 2.35 | yes | Character Origins > Elf |
| 13 | 7 | 2.13 |  | Magic Items > Ring of X-ray Vision |
| 14 | 9 | 1.53 |  | Rules Glossary > Per Day |
| 15 | 20 | 1.02 |  | Playing the Game > Duration |
| 16 | 18 | 1.01 |  | Classes > Level 9: Indomitable |
| 17 | 11 | 0.27 |  | Spells > Resurrection |
| 18 | 16 | -0.33 | yes | Rules Glossary > Short Rest |
| 19 | 10 | -0.82 |  | Spells > Prayer of Healing |
| 20 | 13 | -0.88 |  | Character Origins > Orc |


*re-ranking* (query: `Long Rest minimum duration sleep`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.11 | yes | Rules Glossary > Long Rest |
| 2 | 3 | -0.84 | yes | Rules Glossary > Long Rest |
| 3 | 2 | -2.58 | yes | Character Origins > Elf |
| 4 | 6 | -3.13 |  | Rules Glossary > Long Rest |
| 5 | 15 | -3.70 | yes | Rules Glossary > Short Rest |
| 6 | 5 | -3.77 | yes | Rules Glossary > Long Rest |
| 7 | 17 | -6.65 |  | Classes > Level 10: Tireless |
| 8 | 16 | -6.81 |  | Playing the Game > Duration |
| 9 | 8 | -6.90 |  | Rules Glossary > Exhaustion [Condition] |
| 10 | 20 | -7.33 |  | Classes > Level 14: Nature's Veil |
| 11 | 4 | -7.51 |  | Spells > Sleep |
| 12 | 18 | -7.79 |  | Classes > Level 6: Wholeness of Body |
| 13 | 12 | -8.20 |  | Character Origins > Goliath |
| 14 | 13 | -8.43 |  | Rules Glossary > Per Day |
| 15 | 7 | -8.48 |  | Spells > Prayer of Healing |
| 16 | 9 | -9.49 |  | Spells > Spell Slots |
| 17 | 14 | -10.35 |  | Spells > Resurrection |
| 18 | 11 | -10.70 |  | Rules Glossary > Short Rest |
| 19 | 19 | -10.72 | yes | Rules Glossary > Short Rest |
| 20 | 10 | -11.10 |  | Spells > Sleep |


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


*re-ranking* (query: `Short Rest minimum duration`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.00 | yes | Rules Glossary > Short Rest |
| 2 | 12 | 0.62 | yes | Rules Glossary > Long Rest |
| 3 | 3 | -0.18 | yes | Rules Glossary > Long Rest |
| 4 | 4 | -0.27 |  | Rules Glossary > Short Rest |
| 5 | 14 | -0.37 | yes | Rules Glossary > Long Rest |
| 6 | 8 | -1.72 |  | Spells > Prayer of Healing |
| 7 | 7 | -1.73 | yes | Equipment > Attune during a Short Rest |
| 8 | 2 | -1.79 | yes | Rules Glossary > Short Rest |
| 9 | 5 | -3.33 |  | Playing the Game > Hit Points |
| 10 | 19 | -3.60 |  | Classes > Level 10: Tireless |
| 11 | 13 | -4.00 |  | Rules Glossary > Long Rest |
| 12 | 9 | -4.20 |  | Playing the Game > Duration |
| 13 | 6 | -4.21 |  | Equipment > Attune during a Short Rest |
| 14 | 15 | -4.58 |  | Monsters > Limited Usage |
| 15 | 11 | -4.64 |  | Equipment > Ending Attunement |
| 16 | 17 | -4.75 |  | Equipment > Attune during a Short Rest |
| 17 | 10 | -6.85 |  | Rules Glossary > Hit Point Dice |
| 18 | 18 | -8.53 |  | Spells > Duration |
| 19 | 16 | -8.76 |  | Rules Glossary > Exhaustion [Condition] |
| 20 | 20 | -9.36 |  | Gameplay Toolbox > Extended Travel |

*retrieved sections:* Rules Glossary > Opportunity Attacks | Playing the Game > Opportunity Attacks | Rules Glossary > Reaction | Rules Glossary > Long Rest | Character Origins > Elf | Rules Glossary > Short Rest | Equipment > Attune during a Short Rest

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

[Rules Glossary > Reaction]
#### Reaction  
A Reaction is a special action taken in response to a trigger defined in the Reaction's description. You can take a Reaction on another creature's turn, and if you take it on your turn, you can do so even if you also take an action, a Bonus Action, or both. Once you take a Reaction, you can't take another one until the start of your next turn. The Opportunity Attack is a Reaction available to all creatures. _See also_ "Opportunity Attacks" and "Playing the Game" ("Actions").

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

[Character Origins > Elf]
_Trance._ You don't need to sleep, and magic can't put you to sleep. You can finish a Long Rest in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness.

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
```
</details>


---

## q9 (multi-part) Explain the weapon mastery properties Topple, Push, Sap and Slow: what does each one do when you hit?

**Gold facts (counterfactual data):** Strength saving throw; Prone; 15 feet; Large or smaller; Disadvantage on its next attack roll; reduce its Speed by 10 feet


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Topple:** When you hit with the weapon, you can force the target to make a **Constitution saving throw**. On a failed save, it has the **Prone** condition. The DC is 8 + your attack's ability modifier + your proficiency bonus.

**Push:** When you hit with the weapon, you can push the target up to **10 feet** directly away from you, if it is Large or smaller. No saving throw is required.

**Sap:** When you hit with the weapon, the target has **Disadvantage on its next attack roll** before the start of your next turn.

**Slow:** When you hit with the weapon, the target's **Speed is reduced by 10 feet** until the start of your next turn.

*facts found (judge): 4/6; missing: Strength saving throw; 15 feet*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Topple:** On a hit, you can force the creature to make a Strength saving throw (DC 8 + the ability modifier used for the attack roll + your Proficiency Bonus). On a failed save, the creature has the Prone condition.

**Push:** On a hit, you can push the creature up to 15 feet straight away from you, if it is Large or smaller.

**Sap:** On a hit, the creature has Disadvantage on its next attack roll before the start of your next turn.

**Slow:** The Context does not say what Slow does. It only mentions Slow as an option under Tactical Master, so its effect on a hit is missing.

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

**Topple:** The Context doesn't describe this property, so I can't explain what it does.

**Push:** When you hit a creature, you can push it up to 15 feet straight away from you, if it is Large or smaller.

**Sap:** When you hit a creature, that creature has Disadvantage on its next attack roll before the start of your next turn.

**Slow:** When you hit a creature and deal damage, you can reduce its Speed by 10 feet until the start of your next turn. If it's hit more than once by Slow weapons, the Speed reduction doesn't exceed 10 feet.

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

- **Topple:** On a hit, you can force the creature to make a Strength saving throw with DC 8 plus the ability modifier used for the attack roll and your Proficiency Bonus. On a failed save, the creature has the Prone condition.
- **Push:** On a hit, you can push the creature up to 15 feet straight away from you, if it is Large or smaller.
- **Sap:** On a hit, the creature has Disadvantage on its next attack roll before the start of your next turn.
- **Slow:** On a hit that also deals damage, you can reduce the creature's Speed by 10 feet until the start of your next turn. If the creature is hit more than once by Slow weapons, the Speed reduction doesn't exceed 10 feet.

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

**Push:** If you hit a creature with this weapon, you can push it up to 15 feet straight away from you, but only if it is Large or smaller.

**Sap:** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

**Slow:** If you hit a creature with this weapon and deal damage, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons with this property, the Speed reduction doesn't exceed 10 feet.

**Topple:** The Context doesn't include the Topple property, so I can't explain what it does.

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

**Topple:** If you hit a creature with this weapon, you can force it to make a Strength saving throw (DC 8 plus the ability modifier used for the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition. The Context doesn't describe what the Prone condition does.

**Push:** If you hit a creature with this weapon, you can push it up to 15 feet straight away from you, if it is Large or smaller.

**Sap:** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

**Slow:** If you hit a creature with this weapon and deal damage, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons with this property, the Speed reduction doesn't exceed 10 feet.

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

- **Topple:** On a hit, you can force the creature to make a Strength saving throw (DC 8 + the ability modifier used for the attack roll + your Proficiency Bonus). On a failed save, the creature has the Prone condition.
- **Push:** On a hit, you can push the creature up to 15 feet straight away from you, if it is Large or smaller.
- **Sap:** On a hit, the creature has Disadvantage on its next attack roll before the start of your next turn.
- **Slow:** On a hit that deals damage, you can reduce the creature's Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons with this property, the Speed reduction doesn't exceed 10 feet.

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


### v6_agentic  (12 chunks, 3 LLM call(s))

**Topple:** On a hit, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used for the attack roll plus your Proficiency Bonus). On a failed save, the creature has the Prone condition.

**Push:** On a hit, you can push the creature up to 15 feet straight away from you, if it is Large or smaller.

**Sap:** On a hit, the creature has Disadvantage on its next attack roll before the start of your next turn.

**Slow:** On a hit that deals damage, you can reduce the creature's Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons with this property, the Speed reduction doesn't exceed 10 feet.

*facts found (judge): 6/6; missing: none*

*agentic sub-queries:* D&D 5e weapon mastery Topple / D&D 5e weapon mastery Push / D&D 5e weapon mastery Sap / D&D 5e weapon mastery Slow / prone condition / disadvantage on attack rolls condition


*re-ranking* (query: `D&D 5e weapon mastery Topple`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 1.33 | yes | Equipment > Mastery Properties |
| 2 | 4 | 0.91 | yes | Classes > Level 1: Weapon Mastery |
| 3 | 3 | 0.80 | yes | Classes > Level 1: Weapon Mastery |
| 4 | 1 | 0.49 | yes | Classes > Level 1: Weapon Mastery |
| 5 | 17 | -0.77 |  | Equipment > Mastery Properties |
| 6 | 13 | -3.16 |  | Equipment > Mastery Properties |
| 7 | 14 | -3.63 |  | Equipment > Mastery Properties |
| 8 | 10 | -3.91 |  | Equipment > Weapons |
| 9 | 9 | -4.58 |  | Equipment > Mastery Properties |
| 10 | 7 | -4.70 |  | Equipment > Mastery Properties |
| 11 | 12 | -4.89 |  | Equipment > Mastery Properties |
| 12 | 5 | -5.00 |  | Classes > Level 9: Tactical Master |
| 13 | 15 | -5.20 |  | Classes > Fighter Class Features |
| 14 | 6 | -5.87 | yes | Equipment > Mastery Properties |
| 15 | 8 | -6.29 | yes | Equipment > Mastery Properties |
| 16 | 11 | -6.88 |  | Equipment > Mastery Properties |
| 17 | 19 | -8.53 |  | Playing the Game > Rhythm of Play |
| 18 | 18 | -8.58 |  | Character Creation > Starting at Higher Levels |
| 19 | 16 | -10.53 |  | Feats > Great Weapon Fighting |
| 20 | 20 | -11.09 |  | Magic Items > Hammer of Thunderbolts |


*re-ranking* (query: `D&D 5e weapon mastery Push`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.23 | yes | Equipment > Mastery Properties |
| 2 | 4 | 0.96 | yes | Classes > Level 1: Weapon Mastery |
| 3 | 5 | 0.78 | yes | Classes > Level 1: Weapon Mastery |
| 4 | 3 | 0.59 | yes | Classes > Level 1: Weapon Mastery |
| 5 | 13 | -1.57 |  | Equipment > Mastery Properties |
| 6 | 2 | -2.01 |  | Classes > Level 9: Tactical Master |
| 7 | 12 | -2.07 |  | Equipment > Mastery Properties |
| 8 | 8 | -2.78 |  | Equipment > Mastery Properties |
| 9 | 11 | -3.18 |  | Equipment > Mastery Properties |
| 10 | 6 | -3.43 | yes | Equipment > Mastery Properties |
| 11 | 9 | -3.83 |  | Equipment > Mastery Properties |
| 12 | 10 | -4.62 |  | Equipment > Weapons |
| 13 | 7 | -4.73 | yes | Equipment > Mastery Properties |
| 14 | 14 | -5.08 |  | Equipment > Mastery Properties |
| 15 | 20 | -5.67 |  | Classes > Fighter Class Features |
| 16 | 15 | -5.69 |  | Equipment > Mastery Properties |
| 17 | 19 | -5.87 |  | Classes > Barbarian Class Features |
| 18 | 18 | -7.92 |  | Playing the Game > Rhythm of Play |
| 19 | 17 | -9.08 |  | Character Creation > Starting at Higher Levels |
| 20 | 16 | -10.53 |  | Equipment > Properties |


*re-ranking* (query: `D&D 5e weapon mastery Sap`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 1.39 | yes | Classes > Level 1: Weapon Mastery |
| 2 | 5 | 1.25 | yes | Classes > Level 1: Weapon Mastery |
| 3 | 3 | 1.17 | yes | Classes > Level 1: Weapon Mastery |
| 4 | 10 | -0.09 |  | Equipment > Mastery Properties |
| 5 | 13 | -0.25 |  | Equipment > Mastery Properties |
| 6 | 2 | -0.73 | yes | Equipment > Mastery Properties |
| 7 | 1 | -1.40 |  | Classes > Level 9: Tactical Master |
| 8 | 7 | -2.23 |  | Equipment > Mastery Properties |
| 9 | 8 | -2.94 |  | Equipment > Weapons |
| 10 | 9 | -3.64 |  | Equipment > Mastery Properties |
| 11 | 16 | -3.95 |  | Equipment > Mastery Properties |
| 12 | 18 | -4.07 |  | Equipment > Mastery Properties |
| 13 | 11 | -4.23 |  | Equipment > Mastery Properties |
| 14 | 6 | -4.25 | yes | Equipment > Mastery Properties |
| 15 | 14 | -4.56 |  | Equipment > Mastery Properties |
| 16 | 15 | -5.09 |  | Equipment > Mastery Properties |
| 17 | 12 | -5.90 | yes | Equipment > Mastery Properties |
| 18 | 19 | -8.90 |  | Character Creation > Starting at Higher Levels |
| 19 | 20 | -10.57 |  | Magic Items > Energy Bow |
| 20 | 17 | -10.81 |  | Equipment > Properties |


*re-ranking* (query: `D&D 5e weapon mastery Slow`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.69 | yes | Equipment > Mastery Properties |
| 2 | 5 | -0.40 | yes | Classes > Level 1: Weapon Mastery |
| 3 | 4 | -0.49 | yes | Classes > Level 1: Weapon Mastery |
| 4 | 3 | -0.67 | yes | Classes > Level 1: Weapon Mastery |
| 5 | 2 | -0.99 |  | Classes > Level 9: Tactical Master |
| 6 | 8 | -1.08 |  | Equipment > Mastery Properties |
| 7 | 15 | -1.40 |  | Equipment > Mastery Properties |
| 8 | 7 | -2.15 |  | Equipment > Mastery Properties |
| 9 | 13 | -2.60 |  | Equipment > Mastery Properties |
| 10 | 12 | -2.68 |  | Equipment > Mastery Properties |
| 11 | 19 | -2.84 |  | Equipment > Mastery Properties |
| 12 | 9 | -3.72 |  | Equipment > Mastery Properties |
| 13 | 16 | -4.03 |  | Equipment > Mastery Properties |
| 14 | 6 | -4.29 | yes | Equipment > Mastery Properties |
| 15 | 11 | -4.68 | yes | Equipment > Mastery Properties |
| 16 | 14 | -5.14 |  | Equipment > Mastery Properties |
| 17 | 17 | -5.34 |  | Equipment > Mastery Properties |
| 18 | 10 | -6.21 |  | Equipment > Weapons |
| 19 | 18 | -6.75 |  | Classes > Fighter Class Features |
| 20 | 20 | -9.47 |  | Character Creation > Starting at Higher Levels |


*re-ranking* (query: `prone condition`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.20 | yes | Rules Glossary > Prone [Condition] |
| 2 | 2 | 3.88 | yes | Playing the Game > Dropping Prone |
| 3 | 4 | 3.68 | yes | Gameplay Toolbox > Rolling Stone |
| 4 | 9 | 3.40 |  | Rules Glossary > Unconscious [Condition] |
| 5 | 8 | 2.43 |  | Spells > Grease |
| 6 | 7 | 2.33 |  | Animals > Bonus Actions |
| 7 | 17 | 2.31 |  | Spells > Earthquake |
| 8 | 5 | 2.30 |  | Animals > Actions |
| 9 | 16 | 2.26 |  | Playing the Game > Falling Off |
| 10 | 3 | 2.14 |  | Animals > Actions |
| 11 | 10 | 2.03 |  | Monsters A–Z > Bonus Actions |
| 12 | 13 | 1.98 |  | Monsters A–Z > Bonus Actions |
| 13 | 6 | 1.98 |  | Animals > Actions |
| 14 | 19 | 1.57 |  | Rules Glossary > Condition |
| 15 | 11 | 1.22 | yes | Rules Glossary > Prone [Condition] |
| 16 | 18 | 0.89 |  | Monsters A–Z > Bonus Actions |
| 17 | 15 | 0.75 |  | Monsters A–Z > Bonus Actions |
| 18 | 12 | 0.27 |  | Animals > Actions |
| 19 | 20 | -0.22 |  | Animals > Actions |
| 20 | 14 | -0.91 |  | Spells > Hideous Laughter |


*re-ranking* (query: `disadvantage on attack rolls condition`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.56 | yes | Rules Glossary > Prone [Condition] |
| 2 | 3 | 6.58 | yes | Rules Glossary > Invisible [Condition] |
| 3 | 6 | 6.16 | yes | Magic Items > Oathbow |
| 4 | 15 | 6.05 |  | Playing the Game > Impeded Weapons |
| 5 | 2 | 6.01 |  | Rules Glossary > Restrained [Condition] |
| 6 | 13 | 5.97 |  | Rules Glossary > Grappled [Condition] |
| 7 | 9 | 5.51 |  | Monsters A–Z > Traits |
| 8 | 11 | 5.49 |  | Rules Glossary > Frightened [Condition] |
| 9 | 4 | 5.29 |  | Rules Glossary > Blinded [Condition] |
| 10 | 12 | 5.25 |  | Gameplay Toolbox > Strong Wind |
| 11 | 7 | 5.18 |  | Playing the Game > Making an Attack |
| 12 | 5 | 5.09 |  | Rules Glossary > Poisoned [Condition] |
| 13 | 16 | 4.47 |  | Playing the Game > Actions |
| 14 | 10 | 4.35 |  | Monsters A–Z > Traits |
| 15 | 14 | 3.41 |  | Monsters A–Z > Actions |
| 16 | 20 | 3.41 |  | Magic Items > Ring of Elemental Command |
| 17 | 8 | 3.34 |  | Magic Items > Spellguard Shield |
| 18 | 17 | 1.19 |  | Rules Glossary > Disadvantage |
| 19 | 19 | 0.65 |  | Playing the Game > They Don't Stack |
| 20 | 18 | -1.53 |  | Playing the Game > They Don't Stack |

*retrieved sections:* Equipment > Mastery Properties | Classes > Level 1: Weapon Mastery | Rules Glossary > Prone [Condition] | Playing the Game > Dropping Prone | Gameplay Toolbox > Rolling Stone | Rules Glossary > Invisible [Condition] | Magic Items > Oathbow

<details><summary>full retrieved context</summary>

```
[Equipment > Mastery Properties]
**Topple.** If you hit a creature with this weapon, you can force the creature to make a Strength saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.  
**Vex.** If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.  
**Weapons**  
<table>
<thead>
<tr>
<th>Name</th>

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of two kinds of Simple or Martial Melee weapons of your choice, such as Greataxes and Handaxes. Whenever you finish a Long Rest, you can practice weapon drills and change one of those weapon choices.  
When you reach certain Barbarian levels, you gain the ability to use the mastery properties of more kinds of weapons, as shown in the Weapon Mastery column of the Barbarian Features table.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency, such as Longswords and Javelins.  
Whenever you finish a Long Rest, you can change the kinds of weapons you chose. For example, you could switch to using the mastery properties of Halberds and Flails.

---

[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

---

[Classes > Level 1: Weapon Mastery]
#### Level 1: Weapon Mastery  
Your training with weapons allows you to use the mastery properties of three kinds of Simple or Martial weapons of your choice. Whenever you finish a Long Rest, you can practice weapon drills and change one of those weapon choices.  
When you reach certain Fighter levels, you gain the ability to use the mastery properties of more kinds of weapons, as shown in the Weapon Mastery column of the Fighter Features table.

---

[Equipment > Mastery Properties]
**Slow.** If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn't exceed 10 feet.

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

[Rules Glossary > Prone [Condition]]
_Attacks Affected._ You have Disadvantage on attack rolls. An attack roll against you has Advantage if the attacker is within 5 feet of you. Otherwise, that attack roll has Disadvantage.

---

[Rules Glossary > Invisible [Condition]]
_Attacks Affected._ Attack rolls against you have Disadvantage, and your attack rolls have Advantage. If a creature can somehow see you, you don't gain this benefit against that creature.

---

[Magic Items > Oathbow]
When you make a ranged attack roll with this weapon against your sworn enemy, you have Advantage on the roll. In addition, your target gains no benefit from Half Cover or Three-Quarters Cover, and you suffer no Disadvantage due to long range. If the attack hits, your sworn enemy takes an extra 3d6 Piercing damage.  
While your sworn enemy lives, you have Disadvantage on attack rolls with all other weapons.
```
</details>


---

## q10 (cross-file) What does the Fighter's Action Surge give you and when does it recharge, at what level can it be used twice? And how does a Barbarian enter Rage, what armor prevents it, and how are Rage uses regained on a Short Rest?

**Gold facts (counterfactual data):** one additional action, except the Magic action; Short or Long Rest; level 15; Bonus Action; Heavy armor; one expended use when you finish a Short Rest


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Fighter's Action Surge:** On your turn, it gives you one additional action (not a bonus action or reaction). You regain its use when you finish a **Short or Long Rest**. You get one use starting at 2nd level. At **17th level** you can use it twice before a rest, but only once on the same turn.

**Barbarian's Rage:** You enter Rage as a **bonus action**. You can't use Rage while wearing **Heavy armor**.

**Regaining Rage uses:** By default, Barbarians regain all expended Rage uses when they finish a **Long Rest**, not a Short Rest. Your question assumes a Short Rest recovery, but I'm not aware of a base Barbarian feature that provides one. If you're thinking of a specific subclass or feature, check its exact text.

*facts found (judge): 3/6; missing: one additional action, except the Magic action; level 15; one expended use when you finish a Short Rest*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Fighter's Action Surge:** The Context doesn't include the Fighter class or Action Surge, so I can't say what it gives, when it recharges, or at what level it can be used twice.

**Barbarian Rage:**
- **How to enter:** As a Bonus Action.
- **Armor that prevents it:** Heavy armor.
- **Short Rest:** You regain one expended Rage use when you finish a Short Rest.

*facts found (judge): 3/6; missing: one additional action, except the Magic action; Short or Long Rest; level 15*

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

**Fighter's Action Surge:**
- **What it gives:** On your turn, you can take one additional action, except the Magic action.
- **Recharge:** After you use it, you can't use it again until you finish a Short or Long Rest.
- **Used twice:** Starting at level 15, you can use it twice before a rest, but only once on a turn.

**Barbarian's Rage:**
- **How to enter:** As a Bonus Action, if you aren't wearing Heavy armor.
- **Armor that prevents it:** Heavy armor.
- **Short Rest regain:** You regain one expended use when you finish a Short Rest.
- **Missing information:** The Context refers to the Barbarian Features table for how many Rages you have at each level, but that table isn't included, so I can't say how many uses you get at a given level.

*facts found (judge): 6/6; missing: none*


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

**Action Surge:** On your turn, you can take one additional action, except the Magic action. It recharges when you finish a Short or Long Rest. It can be used twice before a rest starting at level 15, but only once per turn. The Fighter Features table lists two uses at level 17, which conflicts with the level 15 in the feature text. The Context says it is always right, so the answer is level 15.

**Barbarian Rage:** A Barbarian enters Rage as a Bonus Action, as long as they aren't wearing Heavy armor. Heavy armor prevents Rage. On a Short Rest, the Barbarian regains one expended Rage use.

*facts found (judge): 6/6; missing: none*


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

**Action Surge:** It lets you take one additional action on your turn, except the Magic action. It recharges when you finish a Short or Long Rest. You can use it twice before a rest starting at level 15, but only once per turn.

**Barbarian Rage:** You enter Rage as a Bonus Action. You can't do so while wearing Heavy armor. On a Short Rest, you regain one expended Rage use. The Context doesn't say how many Rages you have at each level, since that information is in the Barbarian Features table, which isn't included.

*facts found (judge): 6/6; missing: none*


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

**Fighter's Action Surge:** On your turn, you can take one additional action, except the Magic action. Once used, it can't be used again until you finish a Short or Long Rest. Starting at level 15, you can use it twice before a rest, but only once per turn.

**Barbarian's Rage:** You enter Rage as a Bonus Action, as long as you aren't wearing Heavy armor. Heavy armor is the armor that prevents it. The number of Rages you have is set by the Rages column of the Barbarian Features table, which isn't in the Context, so the number of uses at your level is missing.

**Regaining Rage on a Short Rest:** You regain one expended use when you finish a Short Rest.

*facts found (judge): 6/6; missing: none*


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

**Action Surge (Fighter):**
- **What it gives:** On your turn, you can take one additional action, except the Magic action.
- **When it recharges:** After you use it, you can't use it again until you finish a Short or Long Rest.
- **Using it twice:** Starting at level 15, you can use it twice before a rest, but only once on a turn.

**Rage (Barbarian):**
- **How to enter:** As a Bonus Action, if you aren't wearing Heavy armor.
- **Armor that prevents it:** Heavy armor.
- **Short Rest regain:** You regain one expended use of Rage when you finish a Short Rest.

*facts found (judge): 6/6; missing: none*


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


### v6_agentic  (16 chunks, 3 LLM call(s))

**Fighter: Action Surge**
- **What it gives:** On your turn, you can take one additional action, except the Magic action.
- **Recharge:** Once used, it returns when you finish a Short or Long Rest.
- **Two uses:** The Context gives two different levels. The Level 2 feature text says that starting at **level 15** you can use it twice before a rest, but only once on a turn. The Fighter Features table lists "Action Surge (two uses)" at **level 17**. The Context doesn't say which is correct.

**Barbarian: Rage**
- **How to enter:** You enter Rage as a **Bonus Action**.
- **What prevents it:** Wearing **Heavy armor** prevents you from entering Rage.
- **Regaining uses on a Short Rest:** You regain **one** expended use when you finish a Short Rest. You regain all expended uses when you finish a Long Rest.

*facts found (judge): 6/6; missing: none*

*agentic sub-queries:* Action Surge / Fighter class / Rage / Barbarian class / Heavy armor / Short Rest


*re-ranking* (query: `Action Surge`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | 7.73 | yes | Classes > Level 2: Action Surge |
| 2 | 7 | 1.65 | yes | Classes > Fighter Class Features |
| 3 | 9 | 1.26 | yes | Classes > Fighter Class Features |
| 4 | 1 | -6.16 |  | Rules Glossary > Action |
| 5 | 4 | -6.53 |  | Monsters A–Z > Actions |
| 6 | 2 | -6.72 |  | Rules Glossary > Bonus Action |
| 7 | 10 | -7.16 |  | Monsters A–Z > Actions |
| 8 | 8 | -7.27 |  | Monsters A–Z > Actions |
| 9 | 13 | -7.34 |  | Playing the Game > Bonus Actions |
| 10 | 14 | -7.36 |  | Monsters A–Z > Actions |
| 11 | 17 | -7.45 |  | Rules Glossary > Disengage [Action] |
| 12 | 6 | -7.77 |  | Monsters A–Z > Legendary Actions |
| 13 | 15 | -7.93 |  | Rules Glossary > Attack [Action] |
| 14 | 3 | -8.00 |  | Monsters A–Z > Bonus Actions |
| 15 | 16 | -8.15 |  | Rules Glossary > Attack [Action] |
| 16 | 12 | -8.15 |  | Monsters A–Z > Actions |
| 17 | 20 | -8.40 |  | Playing the Game > Bonus Actions |
| 18 | 19 | -8.50 |  | Spells > Expeditious Retreat |
| 19 | 18 | -9.06 |  | Monsters > Bonus Action |
| 20 | 11 | -9.30 |  | Rules Glossary > Utilize [Action] |


*re-ranking* (query: `Fighter class`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 7.65 | yes | Classes > Fighter Class Features |
| 2 | 1 | 7.47 | yes | Classes > Level 3: Fighter Subclass |
| 3 | 5 | 6.31 | yes | Classes > Fighter Subclass: Champion |
| 4 | 3 | 5.72 |  | Classes > As a Multiclass Character |
| 5 | 10 | 5.70 |  | Classes > Level 1: Fighting Style |
| 6 | 7 | 5.16 | yes | Classes > Fighter Class Features |
| 7 | 4 | 5.01 |  | Classes > As a Level 1 Character |
| 8 | 9 | 4.92 | yes | Classes > Fighter Class Features |
| 9 | 6 | 4.73 |  | Classes > Fighter |
| 10 | 8 | 4.72 |  | Classes > Fighter Class Features |
| 11 | 11 | 4.56 |  | Classes > Fighter Class Features |
| 12 | 12 | 2.83 |  | Classes > Level 1: Weapon Mastery |
| 13 | 14 | 2.75 |  | Classes > Level 1: Second Wind |
| 14 | 20 | 2.72 |  | Classes > Level 7: Additional Fighting Style |
| 15 | 13 | 2.58 |  | Character Creation > Gaining a Level |
| 16 | 19 | 1.05 |  | Character Creation > Fill In Numbers |
| 17 | 17 | 0.02 |  | Character Creation > Experience Points |
| 18 | 18 | -0.36 |  | Character Creation > Proficiency Bonus |
| 19 | 16 | -3.49 | yes | Classes > Barbarian Class Features |
| 20 | 15 | -5.78 |  | Classes > Monk Class Features |


*re-ranking* (query: `Rage`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 12 | 5.84 | yes | Classes > Level 1: Rage |
| 2 | 6 | 4.45 | yes | Classes > Level 1: Rage |
| 3 | 4 | 3.60 | yes | Classes > Level 15: Persistent Rage |
| 4 | 8 | 3.48 |  | Classes > Level 1: Rage |
| 5 | 14 | 3.21 |  | Classes > Level 1: Rage |
| 6 | 2 | 2.84 |  | Classes > Level 6: Mindless Rage |
| 7 | 16 | 2.50 |  | Classes > Level 11: Relentless Rage |
| 8 | 18 | 2.03 |  | Classes > Level 3: Frenzy |
| 9 | 10 | 0.05 |  | Classes > Barbarian Subclass: Path of the Berserker |
| 10 | 20 | -1.82 |  | Classes > Level 7: Instinctive Pounce |
| 11 | 17 | -9.10 |  | Monsters A–Z > Actions |
| 12 | 3 | -9.41 |  | Monsters A–Z > Actions |
| 13 | 7 | -9.73 |  | Gameplay Toolbox > Spiked Pit |
| 14 | 11 | -10.03 |  | Animals > Actions |
| 15 | 1 | -10.07 |  | Gameplay Toolbox > Prolonged Effects |
| 16 | 13 | -10.30 |  | Animals > Actions |
| 17 | 5 | -10.32 |  | Playing the Game > Damage and Healing |
| 18 | 15 | -10.36 |  | Rules Glossary > Damage |
| 19 | 9 | -10.59 |  | Gameplay Toolbox > Mental Stress Effects |
| 20 | 19 | -10.97 |  | Gameplay Toolbox > Prolonged Effects |


*re-ranking* (query: `Barbarian class`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 8.01 | yes | Classes > Barbarian Class Features |
| 2 | 3 | 7.52 | yes | Classes > Level 3: Barbarian Subclass |
| 3 | 7 | 5.99 | yes | Classes > Barbarian |
| 4 | 5 | 5.98 |  | Classes > Barbarian Subclass: Path of the Berserker |
| 5 | 6 | 5.95 |  | Classes > As a Multiclass Character |
| 6 | 1 | 5.86 |  | Classes > Barbarian Class Features |
| 7 | 20 | 5.58 |  | Classes > As a Level 1 Character |
| 8 | 4 | 5.00 |  | Classes > Barbarian Class Features |
| 9 | 17 | 4.60 |  | Character Creation > Prerequisites |
| 10 | 14 | 4.19 |  | Classes > Barbarian Class Features |
| 11 | 12 | 4.19 |  | Classes > Barbarian Class Features |
| 12 | 8 | 4.16 |  | Classes > Barbarian Class Features |
| 13 | 11 | 3.83 |  | Classes > Barbarian |
| 14 | 15 | 3.43 | yes | Classes > Level 1: Rage |
| 15 | 16 | 2.94 |  | Classes > Level 1: Weapon Mastery |
| 16 | 13 | 2.15 |  | Classes > Level 1: Rage |
| 17 | 10 | 1.92 |  | Character Creation > Step 1: Choose Class |
| 18 | 9 | -0.81 |  | Character Creation > Gaining a Level |
| 19 | 19 | -6.12 |  | Character Creation > Armor Class |
| 20 | 18 | -9.90 |  | Character Creation > Create Your Character |


*re-ranking* (query: `Heavy armor`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 9 | 3.67 | yes | Magic Items > Demon Armor |
| 2 | 8 | 3.60 | yes | Equipment > Armor Training |
| 3 | 3 | 3.53 | yes | Equipment > Armor |
| 4 | 7 | 3.22 |  | Magic Items > Armor of Vulnerability |
| 5 | 4 | 3.07 |  | Magic Items > Mithral Armor |
| 6 | 5 | 3.01 |  | Magic Items > Armor, +1, +2, or +3 |
| 7 | 12 | 3.01 |  | Classes > Paladin |
| 8 | 11 | 2.61 |  | Magic Items > Armor of Resistance |
| 9 | 2 | 2.56 |  | Magic Items > Adamantine Armor |
| 10 | 6 | 2.48 |  | Classes > Level 5: Fast Movement |
| 11 | 16 | 2.31 |  | Classes > Fighter |
| 12 | 19 | 1.77 |  | Equipment > Armor |
| 13 | 1 | 0.94 |  | Magic Items > Elven Chain |
| 14 | 18 | -1.95 |  | Equipment > Armor |
| 15 | 10 | -2.24 |  | Magic Items > Glamoured Studded Leather |
| 16 | 17 | -2.57 |  | Equipment > Armor |
| 17 | 13 | -2.89 |  | Magic Items > Armor |
| 18 | 15 | -4.23 |  | Magic Items > Armor of Invulnerability |
| 19 | 14 | -4.41 |  | Magic Items > Dwarven Plate |
| 20 | 20 | -5.84 |  | Monsters A–Z > Tough |


*re-ranking* (query: `Short Rest`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 9.24 | yes | Rules Glossary > Short Rest |
| 2 | 2 | 7.16 |  | Rules Glossary > Short Rest |
| 3 | 5 | 6.66 |  | Equipment > Attune during a Short Rest |
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


*re-ranking* (query: `Action Surge two uses level 17`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.18 | yes | Classes > Level 2: Action Surge |
| 2 | 2 | 2.87 | yes | Classes > Fighter Class Features |
| 3 | 3 | 0.89 |  | Classes > Level 17: Improved Brutal Strike |
| 4 | 5 | -0.22 |  | Classes > Level 17: Thief's Reflexes |
| 5 | 16 | -2.49 |  | Monsters A–Z > Actions |
| 6 | 7 | -3.21 |  | Monsters A–Z > Legendary Actions |
| 7 | 19 | -3.23 |  | Monsters A–Z > Actions |
| 8 | 15 | -4.50 |  | Classes > Level 7: Sorcery Incarnate |
| 9 | 13 | -4.79 |  | Classes > Level 2: Metamagic |
| 10 | 10 | -5.38 |  | Classes > Level 20: Archdruid |
| 11 | 4 | -5.44 |  | Classes > Level 11: Two Extra Attacks |
| 12 | 11 | -5.80 |  | Classes > Level 18: Superior Inspiration |
| 13 | 18 | -6.15 |  | Classes > Level 18: Superior Defense |
| 14 | 8 | -6.57 |  | Monsters A–Z > Legendary Actions |
| 15 | 12 | -7.24 |  | Classes > Level 20: Three Extra Attacks |
| 16 | 20 | -7.67 |  | Monsters A–Z > Actions |
| 17 | 6 | -7.84 |  | Monsters A–Z > Legendary Actions |
| 18 | 9 | -8.09 |  | Classes > Level 5: Extra Attack |
| 19 | 17 | -9.11 |  | Classes > Level 13: Improved Brutal Strike |
| 20 | 14 | -10.59 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Action Surge level 15 two uses`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.37 | yes | Classes > Level 2: Action Surge |
| 2 | 2 | -0.18 | yes | Classes > Fighter Class Features |
| 3 | 13 | -2.36 |  | Monsters A–Z > Actions |
| 4 | 5 | -3.63 |  | Monsters A–Z > Legendary Actions |
| 5 | 18 | -4.35 |  | Monsters A–Z > Legendary Actions |
| 6 | 20 | -4.86 |  | Monsters A–Z > Legendary Actions |
| 7 | 11 | -5.35 |  | Classes > Level 7: Sorcery Incarnate |
| 8 | 8 | -5.97 |  | Classes > Level 20: Archdruid |
| 9 | 3 | -6.47 |  | Classes > Level 11: Two Extra Attacks |
| 10 | 4 | -7.62 |  | Monsters A–Z > Legendary Actions |
| 11 | 6 | -7.94 |  | Monsters A–Z > Legendary Actions |
| 12 | 9 | -8.02 |  | Classes > Level 10: Heightened Focus |
| 13 | 7 | -8.84 |  | Classes > Level 20: Three Extra Attacks |
| 14 | 10 | -9.15 |  | Classes > Level 18: Superior Inspiration |
| 15 | 12 | -9.61 |  | Classes > Level 5: Extra Attack |
| 16 | 19 | -10.04 |  | Classes > Level 13: Improved Brutal Strike |
| 17 | 16 | -10.09 |  | Monsters A–Z > Actions |
| 18 | 14 | -10.23 |  | Classes > Level 18: Superior Defense |
| 19 | 17 | -10.33 |  | Classes > Level 13: Use Magic Device |
| 20 | 15 | -10.65 |  | Monsters A–Z > Actions |

*retrieved sections:* Classes > Level 2: Action Surge | Classes > Fighter Class Features | Classes > Level 3: Fighter Subclass | Classes > Fighter Subclass: Champion | Classes > Level 1: Rage | Classes > Level 15: Persistent Rage | Classes > Barbarian Class Features | Classes > Level 3: Barbarian Subclass | Classes > Barbarian | Magic Items > Demon Armor | Equipment > Armor Training | Equipment > Armor | Rules Glossary > Short Rest

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

[Classes > Level 3: Fighter Subclass]
#### Level 3: Fighter Subclass  
You gain a Fighter subclass of your choice. The Champion subclass is detailed after this class's description. A subclass is a specialization that grants you features at certain Fighter levels. For the rest of your career, you gain each of your subclass's features that are of your Fighter level or lower.

---

[Classes > Fighter Subclass: Champion]
### Fighter Subclass: Champion  
_Pursue Physical Excellence in Combat_  
A Champion focuses on the development of martial prowess in a relentless pursuit of victory. Champions combine rigorous training with physical excellence to deal devastating blows, withstand peril, and garner glory. Whether in athletic contests or bloody battle, Champions strive for the crown of the victor.

---

[Classes > Level 1: Rage]
#### Level 1: Rage  
You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.  
You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

---

[Classes > Level 1: Rage]
- Make an attack roll against an enemy.
- Force an enemy to make a saving throw.
- Take a Bonus Action to extend your Rage.  
Each time the Rage is extended, it lasts until the end of your next turn. You can maintain a Rage for up to 10 minutes.

---

[Classes > Level 15: Persistent Rage]
#### Level 15: Persistent Rage  
When you roll Initiative, you can regain all expended uses of Rage. After you regain uses of Rage in this way, you can't do so again until you finish a Long Rest.  
In addition, your Rage is so fierce that it now lasts for 10 minutes without you needing to do anything to extend it from round to round. Your Rage ends early if you have the Unconscious condition (not just the Incapacitated condition) or don Heavy armor.

---

[Classes > Barbarian Class Features]
### Barbarian Class Features  
As a Barbarian, you gain the following class features when you reach the specified Barbarian levels. These features are listed in the Barbarian Features table.  
**Barbarian Features**  
<table>
<thead>
<tr>
<th>Level</th>
<th>Proficiency Bonus</th>
<th>Class Features</th>
<th>Rages</th>
<th>Rage Damage</th>
<th>Weapon Mastery</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>+2</td>
<td>Rage, Unarmored Defense, Weapon Mastery</td>
<td>2</td>
<td>+2</td>
<td>2</td>

---

[Classes > Level 3: Barbarian Subclass]
#### Level 3: Barbarian Subclass  
You gain a Barbarian subclass of your choice. The Path of the Berserker subclass is detailed after this class's description. A subclass is a specialization that grants you features at certain Barbarian levels. For the rest of your career, you gain each of your subclass's features that are of your Barbarian level or lower.

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

[Magic Items > Demon Armor]
#### Demon Armor  
_Armor (Any Light, Medium, or Heavy), Very Rare (Requires Attunement)_  
While wearing this armor, you gain a +1 bonus to Armor Class, and you know Abyssal. In addition, the armor's clawed gauntlets allow your Unarmed Strikes to deal 1d8 Slashing damage instead of the usual Bludgeoning damage, and you gain a +1 bonus to the attack and damage rolls of your Unarmed Strikes.

---

[Equipment > Armor Training]
### Armor Training  
Anyone can don armor or hold a Shield, but only those with training can use them effectively, as explained below. A character's class and other features determine the character's armor training. A monster has training with any armor in its stat block.  
**Light, Medium, or Heavy Armor.** If you wear Light, Medium, or Heavy armor and lack training with it, you have Disadvantage on any D20 Test that involves Strength or Dexterity, and you can't cast spells.

---

[Equipment > Armor]
## Armor  
The Armor table lists the game's main armor. The table includes the cost and weight of armor, as well as the following details:  
**Category.** Every type of armor falls into a category: Light, Medium, or Heavy. The category determines how long it takes to don or doff the armor (as shown in the table).

---

[Rules Glossary > Short Rest]
#### Short Rest  
A Short Rest is a 2-hour period of downtime, during which a creature does nothing more strenuous than reading, talking, eating, or standing watch. To start a Short Rest, you must have at least 1 Hit Point.  
_Benefits of the Rest._ When you finish the rest, you gain the following benefits:
```
</details>


---

## q11 (cross-file) Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the wolf's Pack Tactics trigger? Also what is the Wolf's speed?

**Gold facts (counterfactual data):** AC 12; 2d8 + 2; AC 16; 3d10 + 6; Pack Tactics; Incapacitated; 50 ft


### v0_closed_book  (0 chunks, 1 LLM call(s))

| | Wolf | Dire Wolf |
|---|---|---|
| **AC** | 13 (natural armor) | 14 (natural armor) |
| **Hit Points** | 11 (2d8 + 2) | 37 (5d10 + 10) |
| **Speed** | 40 ft. | 50 ft. |

**Pack Tactics trigger:** The wolf (and the dire wolf) has advantage on attack rolls against a creature if at least one of its allies is within 5 feet of that creature and the ally isn't incapacitated.

*facts found (judge): 4/7; missing: AC 12; AC 16; 3d10 + 6*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Wolf vs. Dire Wolf:** The Context doesn't include AC or Hit Points for either creature, and it has no Dire Wolf entry at all, so I can't compare them.

**Pack Tactics condition:** The Wolf's Pack Tactics trigger when at least one of its allies is within 5 feet of the target and that ally doesn't have the **Incapacitated** condition.

**Wolf's speed:** The Context doesn't state the Wolf's speed.

*facts found (judge): 2/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; 50 ft*

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

**Wolf vs. Dire Wolf:**
- **AC:** Not in the Context. Neither the Wolf nor the Dire Wolf has its AC listed.
- **Hit Points:** Not in the Context. Neither has its HP listed.
- **Dire Wolf:** The Context has no entry for the Dire Wolf, so I can't compare it to the Wolf in any respect.

**Wolf's Pack Tactics condition:** The wolf's Pack Tactics gives it Advantage on attack rolls against a creature when at least one of the wolf's allies is within 5 feet of that creature and the ally doesn't have the Incapacitated condition. So the condition that matters is the *Incapacitated* condition, which prevents an ally from enabling the bonus.

**Wolf's speed:** Not in the Context.

*facts found (judge): 2/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; 50 ft*


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

The Context does not contain the armor class or hit points for either the Wolf or the Dire Wolf, or the Wolf's speed. Only a fragment of the Dire Wolf's stat block is included, with its ability scores, skills, senses, languages, and CR.

The Context does say that the Wolf's Pack Tactics trigger when at least one of the wolf's allies is within 5 feet of the target and that ally doesn't have the **Incapacitated** condition.

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

**Wolf vs. Dire Wolf:**
- **AC:** The Context doesn't include AC for either creature.
- **Hit Points:** The Context doesn't include HP for either creature.
- **Dire Wolf:** The Context has no entry for the Dire Wolf at all, so I can't compare it.

**Pack Tactics condition:** The Wolf's Pack Tactics applies if at least one of the wolf's allies is within 5 feet of the target and that ally doesn't have the **Incapacitated** condition.

**Wolf's speed:** The Context doesn't include the Wolf's speed.

*facts found (judge): 2/7; missing: AC 12; 2d8 + 2; AC 16; 3d10 + 6; 50 ft*


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

**Armor Class and Hit Points:** The Context has the Dire Wolf's stats (AC 16, HP 22), but it has no stat block for the regular Wolf, so I can't compare these values.

**Pack Tactics condition:** Pack Tactics works if at least one of the wolf's allies is within 5 feet of the target and that ally doesn't have the **Incapacitated** condition.

**Wolf's speed:** The Context doesn't give the Wolf's speed.

*facts found (judge): 3/7; missing: AC 12; 2d8 + 2; 3d10 + 6; 50 ft*

*note:* Replayed retrieval differs from the stored context by 2 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.75 | yes | Animals > Traits |
| 2 | 2 | -1.82 | yes | Monsters A–Z > Traits |
| 3 | 4 | -2.75 | yes | Monsters A–Z > Traits |
| 4 | 29 | -3.17 |  | Classes > Level 1: Lay On Hands |
| 5 | 8 | -3.33 | yes | Monsters A–Z > Actions |
| 6 | 10 | -4.10 | yes | Monsters A–Z > Traits |
| 7 | 22 | -4.16 | yes | Animals > Dire Wolf |
| 8 | 9 | -4.17 |  | Monsters A–Z > Traits |
| 9 | 13 | -4.27 |  | Animals > Traits |
| 10 | 5 | -4.35 |  | Monsters A–Z > Traits |
| 11 | 18 | -4.45 |  | Monsters A–Z > Traits |
| 12 | 7 | -4.48 |  | Animals > Traits |
| 13 | 3 | -4.68 |  | Animals > Traits |
| 14 | 15 | -4.69 |  | Animals > Traits |
| 15 | 17 | -4.78 |  | Animals > Traits |
| 16 | 6 | -4.92 |  | Animals > Traits |
| 17 | 23 | -5.04 |  | Animals > Actions |
| 18 | 25 | -5.22 |  | Monsters A–Z > Traits |
| 19 | 21 | -5.28 |  | Animals > Actions |
| 20 | 24 | -5.45 |  | Rules Glossary > Critical Hit |

*retrieved sections:* Animals > Traits | Monsters A–Z > Traits | Monsters A–Z > Reactions | Monsters A–Z > Actions | Animals > Dire Wolf

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
```
</details>


### v5_graph  (8 chunks, 1 LLM call(s))

**Wolf:** The Context has the Wolf's Pack Tactics but not its stat block, so its AC, Hit Points, and Speed are missing.
**Dire Wolf:** AC 16, Hit Points 22 (3d10 + 6), Speed 50 ft.
**Pack Tactics condition:** The wolf's Pack Tactics applies when the wolf's ally doesn't have the **Incapacitated** condition.

*facts found (judge): 5/7; missing: AC 12; 2d8 + 2*


*re-ranking* (query: `Compare the Wolf and the Dire Wolf: AC, Hit Points, and what condition lets the `): candidate pool of 22, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -1.75 | yes | Animals > Traits |
| 2 | 2 | -1.82 | yes | Monsters A–Z > Traits |
| 3 | 4 | -2.75 | yes | Monsters A–Z > Traits |
| 4 | 8 | -3.33 | yes | Monsters A–Z > Actions |
| 5 | 10 | -4.10 | yes | Monsters A–Z > Traits |
| 6 | 14 | -4.16 | yes | Animals > Dire Wolf |
| 7 | 9 | -4.17 | yes | Monsters A–Z > Traits |
| 8 | 5 | -4.35 | yes | Monsters A–Z > Traits |
| 9 | 7 | -4.48 |  | Animals > Traits |
| 10 | 3 | -4.68 |  | Animals > Traits |
| 11 | 6 | -4.92 |  | Animals > Traits |
| 12 | 13 | -5.60 |  | Animals > Dire Wolf |
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


### v6_agentic  (11 chunks, 3 LLM call(s))

**Wolf:** AC 12, HP 11 (2d8 + 2)
**Dire Wolf:** AC 16, HP 22 (3d10 + 6)

The wolf's Pack Tactics trigger when at least one of the wolf's allies is within 5 feet of the target creature and that ally doesn't have the Incapacitated condition.

The wolf's Speed is 50 ft.

*facts found (judge): 7/7; missing: none*

*agentic sub-queries:* D&D 5e Wolf monster stat block AC hit points / D&D 5e Dire Wolf monster stat block AC hit points / Pack Tactics trait advantage condition / Wolf monster speed


*re-ranking* (query: `D&D 5e Wolf monster stat block AC hit points`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.74 | yes | Rules Glossary > Stat Block |
| 2 | 15 | 0.00 | yes | Classes > Level 2: Wild Shape |
| 3 | 2 | -0.04 | yes | Monsters > Stat Block Overview |
| 4 | 5 | -0.19 |  | Monsters A–Z > Actions |
| 5 | 4 | -2.74 |  | Playing the Game > Armor Class |
| 6 | 11 | -2.99 |  | Rules Glossary > Stat Block |
| 7 | 13 | -3.22 |  | Monsters > Experience Points |
| 8 | 12 | -4.29 |  | Monsters A–Z > Actions |
| 9 | 9 | -4.46 |  | Monsters > Gear |
| 10 | 3 | -4.98 |  | Monsters > Stat Block Overview |
| 11 | 8 | -5.26 |  | Monsters A–Z > Reactions |
| 12 | 7 | -5.30 |  | Rules Glossary > Stat Block |
| 13 | 17 | -6.61 |  | Rules Glossary > Stat Block |
| 14 | 6 | -6.81 |  | Monsters A–Z > Actions |
| 15 | 18 | -6.82 |  | Rules Glossary > Stat Block |
| 16 | 20 | -6.98 |  | Monsters > Parts of a Stat Block |
| 17 | 19 | -7.08 |  | Monsters A–Z > Actions |
| 18 | 16 | -7.31 |  | Monsters A–Z > Actions |
| 19 | 14 | -7.75 |  | Monsters A–Z > Actions |
| 20 | 10 | -7.91 |  | Monsters A–Z > Actions |


*re-ranking* (query: `D&D 5e Dire Wolf monster stat block AC hit points`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.97 | yes | Rules Glossary > Stat Block |
| 2 | 15 | -0.29 | yes | Classes > Level 2: Wild Shape |
| 3 | 2 | -0.52 | yes | Monsters > Stat Block Overview |
| 4 | 4 | -0.83 |  | Monsters A–Z > Actions |
| 5 | 12 | -2.99 |  | Rules Glossary > Stat Block |
| 6 | 13 | -3.69 |  | Monsters > Experience Points |
| 7 | 17 | -4.13 | yes | Animals > Dire Wolf |
| 8 | 3 | -5.02 |  | Monsters > Stat Block Overview |
| 9 | 10 | -5.07 |  | Monsters > Gear |
| 10 | 8 | -5.78 |  | Rules Glossary > Stat Block |
| 11 | 6 | -6.12 |  | Spells > Find Steed |
| 12 | 18 | -6.80 |  | Rules Glossary > Stat Block |
| 13 | 20 | -6.91 |  | Rules Glossary > Stat Block |
| 14 | 5 | -7.10 |  | Monsters A–Z > Actions |
| 15 | 7 | -7.20 |  | Monsters A–Z > Actions |
| 16 | 14 | -7.32 |  | Monsters A–Z > Actions |
| 17 | 16 | -7.34 |  | Monsters A–Z > Actions |
| 18 | 11 | -7.48 |  | Monsters A–Z > Actions |
| 19 | 9 | -7.80 |  | Monsters A–Z > Actions |
| 20 | 19 | -8.22 |  | Monsters A–Z > Actions |


*re-ranking* (query: `Pack Tactics trait advantage condition`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 20 | 5.12 | yes | Monsters A–Z > Traits |
| 2 | 8 | 5.00 | yes | Animals > Traits |
| 3 | 14 | 4.88 | yes | Animals > Traits |
| 4 | 12 | 4.85 |  | Animals > Traits |
| 5 | 19 | 4.84 |  | Monsters A–Z > Traits |
| 6 | 10 | 4.83 |  | Animals > Traits |
| 7 | 18 | 4.72 |  | Animals > Traits |
| 8 | 16 | 4.69 |  | Animals > Traits |
| 9 | 6 | -9.23 |  | Rules Glossary > Petrified [Condition] |
| 10 | 1 | -9.41 |  | Rules Glossary > Restrained [Condition] |
| 11 | 5 | -9.54 |  | Rules Glossary > Charmed [Condition] |
| 12 | 3 | -9.78 |  | Rules Glossary > Prone [Condition] |
| 13 | 2 | -10.05 |  | Character Origins > Goliath |
| 14 | 4 | -10.29 |  | Playing the Game > Advantage/Disadvantage |
| 15 | 17 | -10.74 |  | Feats > Grappler |
| 16 | 7 | -10.89 |  | Rules Glossary > Advantage |
| 17 | 9 | -11.14 |  | Playing the Game > They Don't Stack |
| 18 | 15 | -11.22 |  | Rules Glossary > Cover |
| 19 | 11 | -11.29 |  | Playing the Game > Cover |
| 20 | 13 | -11.35 |  | Playing the Game > They Don't Stack |


*re-ranking* (query: `Wolf monster speed`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 8 | 5.33 | yes | Monsters A–Z > Werewolf |
| 2 | 3 | 4.51 | yes | Monsters A–Z > Winter Wolf |
| 3 | 5 | 3.98 | yes | Animals > Giant Wolf Spider |
| 4 | 6 | 2.90 | yes | Animals > Dire Wolf |
| 5 | 1 | 2.11 |  | Monsters > Speed |
| 6 | 10 | 1.44 |  | Rules Glossary > Stat Block |
| 7 | 2 | 1.00 |  | Playing the Game > Movement and Position |
| 8 | 20 | 0.21 |  | Classes > Level 2: Wild Shape |
| 9 | 19 | -1.11 |  | Monsters A–Z > Bonus Actions |
| 10 | 4 | -1.90 |  | Monsters A–Z > Traits |
| 11 | 7 | -1.94 |  | Monsters A–Z > Bonus Actions |
| 12 | 9 | -2.62 |  | Monsters A–Z > Winter Wolf |
| 13 | 18 | -3.15 |  | Monsters A–Z > Werewolf |
| 14 | 16 | -4.37 |  | Monsters A–Z > Actions |
| 15 | 15 | -4.48 |  | Rules Glossary > Burrow Speed |
| 16 | 13 | -4.68 |  | Rules Glossary > Speed |
| 17 | 11 | -5.75 |  | Rules Glossary > Speed |
| 18 | 12 | -6.38 |  | Character Origins > Speed |
| 19 | 17 | -6.51 |  | Monsters A–Z > Traits |
| 20 | 14 | -6.84 | yes | Animals > Traits |


*re-ranking* (query: `wolf stat block AC HP speed`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 12 | 1.14 | yes | Monsters A–Z > Werewolf |
| 2 | 4 | 1.06 | yes | Animals > Wolf |
| 3 | 6 | 0.54 | yes | Monsters A–Z > Winter Wolf |
| 4 | 10 | 0.14 | yes | Animals > Giant Wolf Spider |
| 5 | 16 | -1.30 |  | Classes > Level 2: Wild Shape |
| 6 | 5 | -3.20 | yes | Rules Glossary > Stat Block |
| 7 | 2 | -5.82 |  | Rules Glossary > Stat Block |
| 8 | 1 | -6.69 | yes | Monsters > Stat Block Overview |
| 9 | 17 | -7.53 |  | Spells > Find Steed |
| 10 | 18 | -9.69 |  | Rules Glossary > Stat Block |
| 11 | 14 | -9.77 |  | Rules Glossary > Stat Block |
| 12 | 3 | -10.30 |  | Monsters > Parts of a Stat Block |
| 13 | 9 | -10.32 |  | Monsters > Limited Usage |
| 14 | 15 | -10.63 |  | Monsters > Damage Notation |
| 15 | 7 | -10.82 |  | Monsters > Limited Usage |
| 16 | 13 | -10.89 |  | Monsters A–Z > Traits |
| 17 | 20 | -10.89 |  | Magic Items > Magic Items A–Z |
| 18 | 8 | -11.03 | yes | Animals > Traits |
| 19 | 11 | -11.08 |  | Monsters A–Z > Traits |
| 20 | 19 | -11.15 |  | Monsters A–Z > Reactions |


*re-ranking* (query: `dire wolf stat block AC hit points`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.44 | yes | Rules Glossary > Stat Block |
| 2 | 11 | -2.06 | yes | Animals > Dire Wolf |
| 3 | 10 | -2.15 | yes | Classes > Level 2: Wild Shape |
| 4 | 7 | -3.03 |  | Spells > Find Steed |
| 5 | 2 | -3.28 | yes | Monsters > Stat Block Overview |
| 6 | 4 | -3.59 |  | Monsters A–Z > Actions |
| 7 | 19 | -4.86 |  | Classes > Level 2: Wild Shape |
| 8 | 20 | -6.79 |  | Rules Glossary > Stat Block |
| 9 | 3 | -6.82 |  | Playing the Game > Armor Class |
| 10 | 17 | -7.53 |  | Spells > Giant Insect |
| 11 | 12 | -7.78 |  | Monsters A–Z > Actions |
| 12 | 6 | -8.53 |  | Monsters A–Z > Reactions |
| 13 | 8 | -8.98 |  | Monsters A–Z > Reactions |
| 14 | 5 | -9.33 |  | Monsters > Stat Block Overview |
| 15 | 18 | -9.34 |  | Monsters A–Z > Reactions |
| 16 | 15 | -9.61 |  | Rules Glossary > Stat Block |
| 17 | 13 | -10.04 |  | Monsters > Parts of a Stat Block |
| 18 | 14 | -10.92 |  | Monsters A–Z > Actions |
| 19 | 9 | -10.99 |  | Monsters A–Z > Actions |
| 20 | 16 | -11.14 |  | Monsters A–Z > Actions |

*retrieved sections:* Rules Glossary > Stat Block | Classes > Level 2: Wild Shape | Monsters > Stat Block Overview | Monsters A–Z > Traits | Animals > Traits | Monsters A–Z > Werewolf | Monsters A–Z > Winter Wolf | Animals > Giant Wolf Spider | Animals > Wolf | Animals > Dire Wolf

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Classes > Level 2: Wild Shape]
**Game Statistics.** Your game statistics are replaced by the Beast's stat block, but you retain your creature type; Hit Points; Hit Point Dice; Intelligence, Wisdom, and Charisma scores; class features; languages; and feats. You also retain your skill and saving throw proficiencies and use your Proficiency Bonus for them, in addition to gaining the proficiencies of the creature. If a skill or saving throw modifier in the Beast's stat block is higher than yours, use the one in the stat block.

---

[Monsters > Stat Block Overview]
# Monsters  
## Stat Block Overview  
A monster has a stat block that contains the rules necessary to use it in the game. Stat blocks are divided into the following parts:  
**Name and General Details.** The name of the monster is followed by its size, creature type (along with any descriptive tags), and alignment.  
**Combat Highlights.** Armor Class, Hit Points, Speed, and Initiative are provided here.

---

[Monsters A–Z > Traits]
#### Traits  
<hr>  
**_Pack Tactics._** The tough has Advantage on an attack roll against a creature if at least one of the tough's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The baboon has Advantage on an attack roll against a creature if at least one of the baboon's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.

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
```
</details>


---

## q12 (needle) What bonuses do a Ring of Protection and a Cloak of Protection each give, and are they the same rarity?

**Gold facts (counterfactual data):** +1 bonus to Armor Class and saving throws; +2 bonus to Armor Class and saving throws; Uncommon


### v0_closed_book  (0 chunks, 1 LLM call(s))

Both items give a **+1 bonus to AC and to saving throws** while worn or attuned.

They are **not the same rarity**: the Ring of Protection is **Rare**, and the Cloak of Protection is **Uncommon**. Both require attunement.

*facts found (judge): 2/3; missing: +2 bonus to Armor Class and saving throws*


### v1_baseline  (3 chunks, 1 LLM call(s))

Based on the Context:

- **Ring of Protection:** +1 bonus to Armor Class and saving throws. Rarity: Uncommon.
- **Cloak of Protection:** +2 bonus to Armor Class and saving throws. Rarity: Uncommon.

They are the same rarity (both Uncommon), but the Cloak of Protection gives a larger bonus (+2 versus +1).

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

The **Ring of Protection** gives a +1 bonus to Armor Class and saving throws. The **Cloak of Protection** gives a +2 bonus to Armor Class and saving throws.

Yes, they are the same rarity: both are Uncommon.

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

Ring of Protection: +1 bonus to Armor Class and saving throws. Rarity: Uncommon.

Cloak of Protection: +2 bonus to Armor Class and saving throws. Rarity: Uncommon.

They are the same rarity (Uncommon). Both also require attunement.

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

Ring of Protection: +1 bonus to Armor Class and saving throws. Rarity: Uncommon.

Cloak of Protection: +2 bonus to Armor Class and saving throws. Rarity: Uncommon.

Yes, they are the same rarity (both Uncommon).

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

The Ring of Protection gives a +1 bonus to Armor Class and saving throws, and the Cloak of Protection gives a +2 bonus to Armor Class and saving throws. Both are Uncommon, so they have the same rarity.

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

Ring of Protection: +1 bonus to Armor Class and saving throws. Rarity: Uncommon.

Cloak of Protection: +2 bonus to Armor Class and saving throws. Rarity: Uncommon.

They are the same rarity (both Uncommon), but the Cloak of Protection gives a larger bonus (+2 versus +1).

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


### v6_agentic  (6 chunks, 3 LLM call(s))

The **Ring of Protection** gives a +1 bonus to Armor Class and saving throws. The **Cloak of Protection** gives a +2 bonus to Armor Class and saving throws. Both are **Uncommon**, so they have the same rarity. Both also require attunement.

*facts found (judge): 3/3; missing: none*

*agentic sub-queries:* Ring of Protection / Cloak of Protection


*re-ranking* (query: `Ring of Protection`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.98 | yes | Magic Items > Ring of Protection |
| 2 | 8 | 4.70 | yes | Magic Items > Ring of Mind Shielding |
| 3 | 11 | 1.48 | yes | Magic Items > Ring of Mind Shielding |
| 4 | 2 | 0.27 |  | Magic Items > Ring of Warmth |
| 5 | 3 | -0.55 |  | Magic Items > Ring of Evasion |
| 6 | 20 | -0.68 |  | Magic Items > Ring of Free Action |
| 7 | 6 | -1.06 |  | Magic Items > Ring of Invisibility |
| 8 | 17 | -1.25 |  | Magic Items > Ring of Elemental Command |
| 9 | 19 | -2.88 |  | Magic Items > Ring of Animal Influence |
| 10 | 15 | -3.21 |  | Magic Items > Ring of Regeneration |
| 11 | 10 | -3.29 |  | Magic Items > Scarab of Protection |
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
| 8 | 12 | -1.58 |  | Magic Items > Scarab of Protection |
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

*retrieved sections:* Magic Items > Ring of Protection | Magic Items > Ring of Mind Shielding | Magic Items > Cloak of Protection | Magic Items > Cloak of Invisibility | Magic Items > Cloak of Displacement

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
```
</details>


---

## q13 (multi-part) What are the options for generating ability scores in character creation: give the Standard Array, the point-buy budget with the cost of a score of 14, and the random method.

**Gold facts (counterfactual data):** 15, 14, 13, 12, 10, 8; 30 points; 14 costs 7; four d6s


### v0_closed_book  (0 chunks, 1 LLM call(s))

**1. Standard Array:** 15, 14, 13, 12, 10, 8. Assign one value to each ability score.

**2. Point Buy:** You have 27 points to spend. Each score starts at 8 and can be raised to a maximum of 15 before racial bonuses. A score of 14 costs **7 points**. The full cost table is:

| Score | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| Cost | 0 | 1 | 2 | 3 | 4 | 5 | 7 | 9 |

**3. Random (Rolling):** Roll four six-sided dice (4d6), drop the lowest die, and total the remaining three. Repeat this six times to get six scores, then assign them to the abilities as you choose.

*facts found (judge): 3/4; missing: 30 points*


### v1_baseline  (3 chunks, 1 LLM call(s))

The three methods for generating ability scores are:

1. **Standard Array:** Use the scores 15, 14, 13, 12, 10, and 8.
2. **Point Cost:** You have 30 points to spend on your scores. A score of 14 costs 7 points.
3. **Random Generation:** Roll four d6, and record the total of the highest three dice. Repeat this five more times to get six numbers.

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

The three methods for generating ability scores are:

1. **Standard Array:** Assign the six scores 15, 14, 13, 12, 10, and 8 to your abilities.
2. **Point Cost:** You have 30 points to spend on your scores. A score of 14 costs 7 points.
3. **Random Generation:** Roll four d6s and record the total of the highest three dice. Repeat five more times to get six numbers.

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

The three methods for generating ability scores are:

- **Standard Array:** Use the six scores 15, 14, 13, 12, 10, and 8.
- **Point Cost:** You have 30 points to spend on your scores. A score of 14 costs 7 points.
- **Random Generation:** Roll four d6s and record the total of the highest three dice. Repeat five more times to get six numbers.

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

**Standard Array:** Use the scores 15, 14, 13, 12, 10, and 8.

**Point Cost:** You have 30 points to spend on your ability scores. A score of 14 costs 7 points.

**Random Generation:** Roll four d6s and record the total of the highest three dice. Repeat this five more times to get six numbers.

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

The three options for generating ability scores are:

1. **Standard Array:** Use the six scores 15, 14, 13, 12, 10, and 8.
2. **Point Cost:** You have 30 points to spend on your scores. A score of 14 costs 7 points.
3. **Random Generation:** Roll four d6s and record the total of the highest three dice. Repeat five more times to get six numbers.

Your GM may prefer one of these methods.

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

The three methods are:

1. **Standard Array:** Use the scores 15, 14, 13, 12, 10, and 8.
2. **Point Cost:** You have 30 points to spend on your ability scores. A score of 14 costs 7 points.
3. **Random Generation:** Roll four d6, and record the total of the highest three dice. Repeat five more times to get six numbers.

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


### v6_agentic  (9 chunks, 3 LLM call(s))

The three options are:

- **Standard Array:** Use the scores 15, 14, 13, 12, 10, and 8.
- **Point Cost (point buy):** You have 30 points to spend on your ability scores. A score of 14 costs 7 points.
- **Random Generation:** Roll four d6, and record the total of the highest three dice. Repeat five more times to get six numbers.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* D&D 5e Standard Array ability scores / D&D 5e point buy ability scores cost table / D&D 5e random ability score generation 4d6 drop lowest / D&D 5e ability score generation methods character creation


*re-ranking* (query: `D&D 5e Standard Array ability scores`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.96 | yes | Character Creation > Generate Your Scores |
| 2 | 1 | 2.61 | yes | Character Creation > Assign Ability Scores |
| 3 | 4 | -1.80 | yes | Playing the Game > Ability Scores |
| 4 | 13 | -2.61 |  | Playing the Game > Ability Modifiers |
| 5 | 9 | -4.17 | yes | Character Creation > Determine Ability Modifiers |
| 6 | 5 | -4.80 | yes | Character Creation > Assign Ability Scores |
| 7 | 3 | -4.87 |  | Monsters > Ability Scores |
| 8 | 10 | -5.04 | yes | Character Creation > Generate Your Scores |
| 9 | 6 | -5.05 |  | Character Origins > Ability Scores |
| 10 | 11 | -5.28 |  | Playing the Game > Ability Scores |
| 11 | 7 | -6.13 | yes | Character Creation > Step 3: Ability Scores |
| 12 | 8 | -6.60 |  | Character Creation > Adjust Ability Scores |
| 13 | 12 | -7.05 |  | Feats > Ability Score Improvement |
| 14 | 17 | -7.38 |  | Character Origins > Sage |
| 15 | 18 | -7.38 |  | Character Origins > Criminal |
| 16 | 20 | -7.85 |  | Rules Glossary > Breaking Objects |
| 17 | 15 | -8.38 |  | Character Origins > Soldier |
| 18 | 16 | -10.66 |  | Classes > Level 20: Body and Mind |
| 19 | 14 | -10.92 |  | Classes > Level 20: Primal Champion |
| 20 | 19 | -10.93 |  | Character Creation > Generate Your Scores |


*re-ranking* (query: `D&D 5e point buy ability scores cost table`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.50 | yes | Character Creation > Generate Your Scores |
| 2 | 2 | -2.99 | yes | Playing the Game > Ability Scores |
| 3 | 7 | -5.00 | yes | Character Creation > Determine Ability Modifiers |
| 4 | 13 | -6.18 |  | Character Creation > Choose a Background |
| 5 | 5 | -6.80 | yes | Character Creation > Assign Ability Scores |
| 6 | 14 | -6.88 |  | Playing the Game > Ability Scores |
| 7 | 20 | -7.24 |  | Character Origins > Ability Scores |
| 8 | 9 | -7.53 | yes | Character Creation > Generate Your Scores |
| 9 | 3 | -8.21 |  | Monsters > Ability Scores |
| 10 | 12 | -8.26 |  | Character Creation > Gaining a Level |
| 11 | 15 | -8.49 |  | Spells > Greater Restoration |
| 12 | 4 | -8.54 | yes | Character Creation > Assign Ability Scores |
| 13 | 6 | -8.70 |  | Character Creation > Adjust Ability Scores |
| 14 | 10 | -8.72 |  | Character Creation > Experience Points |
| 15 | 8 | -9.02 | yes | Character Creation > Step 3: Ability Scores |
| 16 | 16 | -9.78 |  | Rules Glossary > Long Rest |
| 17 | 17 | -9.79 |  | Character Creation > Level Advancement |
| 18 | 19 | -10.14 |  | Rules Glossary > Breaking Objects |
| 19 | 18 | -10.92 |  | Equipment > Food, Drink, and Lodging |
| 20 | 11 | -10.99 |  | Character Creation > Generate Your Scores |


*re-ranking* (query: `D&D 5e random ability score generation 4d6 drop lowest`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 2.01 | yes | Magic Items > Abilities |
| 2 | 1 | -1.76 | yes | Character Creation > Generate Your Scores |
| 3 | 6 | -2.45 | yes | Classes > Rogue Class Features |
| 4 | 2 | -2.93 | yes | Playing the Game > Ability Scores |
| 5 | 5 | -7.58 |  | Character Creation > Adjust Ability Scores |
| 6 | 19 | -7.79 |  | Playing the Game > Ability Modifiers |
| 7 | 7 | -7.90 |  | Classes > Level 4: Ability Score Improvement |
| 8 | 4 | -8.07 |  | Classes > Level 4: Ability Score Improvement |
| 9 | 9 | -8.09 |  | Classes > Level 4: Ability Score Improvement |
| 10 | 15 | -8.26 |  | Classes > Level 4: Ability Score Improvement |
| 11 | 11 | -8.28 |  | Classes > Level 4: Ability Score Improvement |
| 12 | 12 | -8.29 |  | Classes > Level 4: Ability Score Improvement |
| 13 | 14 | -8.31 | yes | Character Creation > Determine Ability Modifiers |
| 14 | 17 | -8.34 |  | Classes > Level 4: Ability Score Improvement |
| 15 | 10 | -8.39 | yes | Character Creation > Generate Your Scores |
| 16 | 8 | -8.44 |  | Character Origins > Ability Scores |
| 17 | 18 | -8.53 |  | Classes > Level 4: Ability Score Improvement |
| 18 | 13 | -8.62 |  | Classes > Level 4: Ability Score Improvement |
| 19 | 20 | -9.52 |  | Character Creation > Gaining a Level |
| 20 | 16 | -11.08 |  | Character Creation > Prerequisites |


*re-ranking* (query: `D&D 5e ability score generation methods character creation`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.04 | yes | Character Creation > Generate Your Scores |
| 2 | 6 | 4.28 | yes | Character Creation > Step 3: Ability Scores |
| 3 | 4 | 3.47 | yes | Character Creation > Assign Ability Scores |
| 4 | 7 | 2.50 | yes | Character Creation > Determine Ability Modifiers |
| 5 | 9 | 2.49 |  | Character Creation > Gaining a Level |
| 6 | 2 | 1.92 | yes | Character Creation > Generate Your Scores |
| 7 | 15 | 1.74 |  | Character Creation > Choose a Background |
| 8 | 3 | 1.66 |  | Character Creation > Adjust Ability Scores |
| 9 | 13 | 0.08 |  | Character Creation > Determine Ability Modifiers |
| 10 | 10 | -0.07 |  | Character Creation > Prerequisites |
| 11 | 19 | -0.72 |  | Character Creation > Create Your Character |
| 12 | 5 | -0.78 |  | Character Origins > Ability Scores |
| 13 | 8 | -0.97 |  | Character Creation > Gaining a Level |
| 14 | 14 | -1.85 |  | Character Creation > Fill In Numbers |
| 15 | 12 | -2.81 |  | Character Creation > Fill In Numbers |
| 16 | 18 | -2.85 |  | Character Creation > Creating Your Character |
| 17 | 17 | -3.74 |  | Character Creation > Create Your Character |
| 18 | 20 | -4.07 |  | Character Creation > Write Your Level |
| 19 | 16 | -4.11 | yes | Playing the Game > Ability Scores |
| 20 | 11 | -4.18 |  | Character Creation > Step 5: Character Creation Details |

*retrieved sections:* Character Creation > Generate Your Scores | Character Creation > Assign Ability Scores | Playing the Game > Ability Scores | Character Creation > Determine Ability Modifiers | Magic Items > Abilities | Classes > Rogue Class Features | Character Creation > Step 3: Ability Scores

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

[Magic Items > Abilities]
### Abilities  
A sentient magic item has Intelligence, Wisdom, and Charisma scores. Choose the item's abilities, or determine them randomly as follows: roll 4d6 for each one, dropping the lowest roll and totaling the rest.

---

[Classes > Rogue Class Features]
<td>4d6</td>
</tr>
<tr>
<td>8</td>
<td>+3</td>
<td>Ability Score Improvement</td>
<td>4d6</td>
</tr>
<tr>
<td>9</td>
<td>+4</td>
<td>Subclass feature</td>
<td>5d6</td>
</tr>
<tr>
<td>10</td>
<td>+4</td>
<td>Ability Score Improvement</td>
<td>5d6</td>
</tr>
<tr>
<td>11</td>
<td>+4</td>
<td>Improved Cunning Strike</td>
<td>6d6</td>
</tr>
<tr>
<td>12</td>
<td>+4</td>
<td>Ability Score Improvement</td>
<td>6d6</td>
</tr>
<tr>
<td>13</td>
<td>+5</td>
<td>Subclass feature</td>
<td>7d6</td>
</tr>
<tr>

---

[Character Creation > Step 3: Ability Scores]
### Step 3: Ability Scores  
To determine your character's ability scores, you first generate a set of six numbers using the instructions below and then assign them to your six abilities. "Playing the Game" explains what each ability means.

---

[Character Creation > Assign Ability Scores]
#### Assign Ability Scores  
Once you've generated six scores, assign them to Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma, keeping in mind your class's primary ability. Fill in the ability modifiers as well.
```
</details>


---

## q14 (needle) List the four types of poison and say which can be applied to a weapon as a Bonus Action.

**Gold facts (counterfactual data):** Contact; Ingested; Inhaled; Injury; Bonus Action


### v0_closed_book  (0 chunks, 1 LLM call(s))

**The four types of poison are:**
1. **Contact**
2. **Ingested**
3. **Inhaled**
4. **Injury**

**Bonus Action:** Only **Injury** poison can be applied to a weapon or piece of ammunition as a Bonus Action. The others can't be applied to weapons this way.

*facts found (judge): 5/5; missing: none*


### v1_baseline  (3 chunks, 1 LLM call(s))

The Context names only two of the four poison types. The other two are missing.

1. **Contact:** Smeared on an object; it stays potent until touched or washed off.
2. **Injury:** Can be applied to a weapon, ammunition, or similar object as a Bonus Action.

The Context does not name types 3 and 4.

**Bonus Action application:** Injury poison can be applied to a weapon as a Bonus Action. The Context doesn't say whether Contact poison can be. Separately, Basic Poison (an equipment item, not one of the four types) can also coat a weapon as a Bonus Action.

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

The Context doesn't list four types of poison, so I can't give that list. It names only two poison types: **Injury poison** and **Basic Poison** (100 GP). The Dagger of Venom is a magic weapon that coats its own blade with poison, not a poison type.

Two of these can be applied to a weapon as a Bonus Action:
- **Injury poison** can be applied as a Bonus Action to a weapon, a piece of ammunition, or a similar object.
- **Basic Poison** can be applied as a Bonus Action to one weapon or up to three pieces of ammunition.

The Dagger of Venom's blade can also be coated with poison as a Bonus Action.

*facts found (judge): 2/5; missing: Contact; Ingested; Inhaled*


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

The four types are **contact, ingested, inhaled, and injury**. The Context names all four in the Sample Poisons section, but it defines only contact and injury.

**Injury** is the type that can be applied to a weapon as a Bonus Action.

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

The Context doesn't list four types of poison. It describes only two poison types:

1. **Injury poison**: Can be applied as a Bonus Action to a weapon, a piece of ammunition, or a similar object.
2. **Basic Poison (100 GP)**: Can be applied as a Bonus Action to one weapon or up to three pieces of ammunition.

The Context also describes the **Dagger of Venom**, a magic weapon that can be coated with poison as a Bonus Action. This is a magic item ability rather than a named poison type, so I've left it out of the list.

Both named poison types that appear in the Context can be applied to a weapon as a Bonus Action. The other two types are missing from the Context.

*facts found (judge): 2/5; missing: Contact; Ingested; Inhaled*


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

The Context names only two of the four poison types: **Contact** and **Injury**. The other two are missing.

Of the two named, **Injury** poison can be applied to a weapon as a Bonus Action. The Context doesn't say whether Contact poison can be applied that way; it only says Contact poison can be smeared on an object.

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

The four types are **contact**, **ingested**, **inhaled**, and **injury**. The Context names all four only in the Sample Poisons section. It defines contact and injury, but it doesn't define ingested or inhaled, so I can't say how those work.

**Injury** is the type that can be applied to a weapon as a Bonus Action. The Context says injury poison "can be applied as a Bonus Action to a weapon, a piece of ammunition, or similar object."

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


### v6_agentic  (16 chunks, 3 LLM call(s))

The four types are **Contact**, **Ingested**, **Inhaled**, and **Injury**.

**Injury** poison can be applied to a weapon as a Bonus Action.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* D&D 5e poison types / poison Bonus Action apply weapon / Contact poison / Ingested poison / Inhaled poison / Injury poison


*re-ranking* (query: `D&D 5e poison types`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.34 | yes | Gameplay Toolbox > Poison |
| 2 | 4 | -4.95 | yes | Gameplay Toolbox > Sample Poisons |
| 3 | 15 | -5.14 | yes | Rules Glossary > Breaking Objects |
| 4 | 7 | -7.25 | yes | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 5 | 5 | -7.28 |  | Gameplay Toolbox > Harvesting Poison |
| 6 | 3 | -7.53 | yes | Gameplay Toolbox > Poison |
| 7 | 2 | -7.84 |  | Rules Glossary > Damage Types |
| 8 | 20 | -8.57 |  | Monsters A–Z > Traits |
| 9 | 16 | -8.96 |  | Playing the Game > Rhythm of Play |
| 10 | 9 | -8.99 |  | Gameplay Toolbox > Harvesting Poison |
| 11 | 11 | -9.16 |  | Monsters A–Z > Actions |
| 12 | 6 | -9.40 |  | Gameplay Toolbox > Pale Tincture (250 GP) |
| 13 | 13 | -9.47 |  | Playing the Game > Rhythm of Play |
| 14 | 10 | -9.71 |  | Monsters A–Z > Actions |
| 15 | 12 | -9.79 |  | Character Creation > Starting at Higher Levels |
| 16 | 14 | -9.86 | yes | Gameplay Toolbox > Poison |
| 17 | 8 | -10.19 |  | Rules Glossary > Damage Types |
| 18 | 17 | -10.23 |  | Monsters A–Z > Water Elemental |
| 19 | 18 | -10.46 |  | Playing the Game > Damage Types |
| 20 | 19 | -10.81 |  | Monsters A–Z > Spirit Naga |


*re-ranking* (query: `poison Bonus Action apply weapon`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 8.41 | yes | Gameplay Toolbox > Poison |
| 2 | 1 | 7.48 | yes | Equipment > Poison, Basic (100 GP) |
| 3 | 2 | 5.30 | yes | Magic Items > Dagger of Venom |
| 4 | 16 | 1.31 |  | Magic Items > Flame Tongue |
| 5 | 7 | 0.66 |  | Magic Items > Dancing Sword |
| 6 | 4 | -0.98 |  | Spells > Magic Weapon |
| 7 | 15 | -1.02 |  | Classes > Level 5: Cunning Strike |
| 8 | 10 | -1.26 |  | Monsters A–Z > Actions |
| 9 | 9 | -1.26 |  | Magic Items > Quarterstaff of the Acrobat |
| 10 | 14 | -1.53 |  | Magic Items > Scimitar of Speed |
| 11 | 6 | -2.47 |  | Spells > Poison Spray |
| 12 | 11 | -3.34 |  | Spells > Spiritual Weapon |
| 13 | 20 | -3.94 |  | Magic Items > Weapon, +1, +2, or +3 |
| 14 | 8 | -4.45 |  | Monsters A–Z > Actions |
| 15 | 12 | -4.71 | yes | Gameplay Toolbox > Poison |
| 16 | 5 | -5.05 |  | Magic Items > Luck Blade |
| 17 | 17 | -5.07 |  | Monsters A–Z > Actions |
| 18 | 19 | -6.10 |  | Monsters A–Z > Actions |
| 19 | 13 | -7.58 | yes | Gameplay Toolbox > Poison |
| 20 | 18 | -10.03 |  | Monsters > Skills |


*re-ranking* (query: `Contact poison`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.27 | yes | Gameplay Toolbox > Poison |
| 2 | 2 | 5.05 | yes | Gameplay Toolbox > Oil of Taggit (400 GP) |
| 3 | 7 | 5.02 | yes | Gameplay Toolbox > Crawler Mucus (200 GP) |
| 4 | 3 | 1.91 | yes | Gameplay Toolbox > Sample Poisons |
| 5 | 5 | 1.25 |  | Gameplay Toolbox > Purchasing Poison |
| 6 | 6 | -2.00 | yes | Gameplay Toolbox > Poison |
| 7 | 11 | -3.32 |  | Spells > Protection from Poison |
| 8 | 16 | -5.22 | yes | Gameplay Toolbox > Poison |
| 9 | 18 | -5.42 |  | Spells > Detect Poison and Disease |
| 10 | 12 | -6.15 |  | Magic Items > Potion of Poison |
| 11 | 9 | -6.27 |  | Spells > Poison Spray |
| 12 | 13 | -6.58 | yes | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 13 | 14 | -6.60 |  | Gameplay Toolbox > Harvesting Poison |
| 14 | 17 | -6.67 | yes | Magic Items > Dagger of Venom |
| 15 | 15 | -7.19 |  | Magic Items > Periapt of Proof against Poison |
| 16 | 19 | -7.22 | yes | Gameplay Toolbox > Midnight Tears (1,500 GP) |
| 17 | 8 | -7.32 |  | Gameplay Toolbox > Harvesting Poison |
| 18 | 10 | -7.53 |  | Gameplay Toolbox > Pale Tincture (250 GP) |
| 19 | 20 | -8.30 |  | Gameplay Toolbox > Burnt Othur Fumes (500 GP) |
| 20 | 4 | -8.30 |  | Gameplay Toolbox > Harvesting Poison |


*re-ranking* (query: `Ingested poison`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.74 | yes | Gameplay Toolbox > Poison |
| 2 | 12 | 4.94 | yes | Gameplay Toolbox > Torpor (600 GP) |
| 3 | 8 | 3.87 | yes | Gameplay Toolbox > Midnight Tears (1,500 GP) |
| 4 | 5 | 3.77 |  | Gameplay Toolbox > Pale Tincture (250 GP) |
| 5 | 15 | 3.49 |  | Gameplay Toolbox > Assassin's Blood (150 GP) |
| 6 | 2 | 2.37 | yes | Gameplay Toolbox > Sample Poisons |
| 7 | 9 | 1.28 |  | Magic Items > Potions |
| 8 | 7 | -2.87 | yes | Gameplay Toolbox > Poison |
| 9 | 3 | -3.37 | yes | Gameplay Toolbox > Poison |
| 10 | 4 | -3.87 |  | Gameplay Toolbox > Purchasing Poison |
| 11 | 19 | -4.65 |  | Gameplay Toolbox > Harvesting Poison |
| 12 | 10 | -5.74 |  | Magic Items > Potion of Poison |
| 13 | 13 | -7.24 |  | Spells > Protection from Poison |
| 14 | 18 | -7.31 |  | Spells > Detect Poison and Disease |
| 15 | 17 | -7.83 |  | Gameplay Toolbox > Wyvern Poison (1,200 GP) |
| 16 | 11 | -7.98 |  | Gameplay Toolbox > Harvesting Poison |
| 17 | 20 | -8.00 |  | Gameplay Toolbox > Burnt Othur Fumes (500 GP) |
| 18 | 14 | -8.20 | yes | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 19 | 16 | -9.28 |  | Spells > Poison Spray |
| 20 | 6 | -9.45 |  | Gameplay Toolbox > Harvesting Poison |


*re-ranking* (query: `Inhaled poison`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.45 | yes | Gameplay Toolbox > Poison |
| 2 | 2 | 5.72 | yes | Gameplay Toolbox > Malice (250 GP) |
| 3 | 3 | 5.07 | yes | Gameplay Toolbox > Essence of Ether (300 GP) |
| 4 | 7 | 4.53 |  | Gameplay Toolbox > Burnt Othur Fumes (500 GP) |
| 5 | 4 | 2.03 | yes | Gameplay Toolbox > Sample Poisons |
| 6 | 12 | -3.21 | yes | Gameplay Toolbox > Poison |
| 7 | 6 | -3.29 | yes | Gameplay Toolbox > Poison |
| 8 | 5 | -3.85 | yes | Gameplay Toolbox > Poison |
| 9 | 8 | -6.22 |  | Magic Items > Potion of Poison |
| 10 | 18 | -6.41 | yes | Gameplay Toolbox > Midnight Tears (1,500 GP) |
| 11 | 15 | -6.61 |  | Spells > Protection from Poison |
| 12 | 14 | -6.86 |  | Gameplay Toolbox > Pale Tincture (250 GP) |
| 13 | 13 | -7.17 |  | Gameplay Toolbox > Wyvern Poison (1,200 GP) |
| 14 | 20 | -7.56 |  | Spells > Detect Poison and Disease |
| 15 | 9 | -7.56 |  | Gameplay Toolbox > Purchasing Poison |
| 16 | 10 | -7.70 |  | Spells > Poison Spray |
| 17 | 17 | -7.77 | yes | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 18 | 16 | -8.47 |  | Gameplay Toolbox > Harvesting Poison |
| 19 | 19 | -8.73 | yes | Magic Items > Dagger of Venom |
| 20 | 11 | -9.21 |  | Gameplay Toolbox > Harvesting Poison |


*re-ranking* (query: `Injury poison`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 8.01 | yes | Gameplay Toolbox > Poison |
| 2 | 17 | 4.72 | yes | Gameplay Toolbox > Serpent Venom (200 GP) |
| 3 | 5 | 4.53 | yes | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 4 | 6 | 4.42 |  | Gameplay Toolbox > Wyvern Poison (1,200 GP) |
| 5 | 16 | 3.57 |  | Gameplay Toolbox > Spider's Sting (200 GP) |
| 6 | 8 | 0.85 | yes | Gameplay Toolbox > Sample Poisons |
| 7 | 2 | -1.92 | yes | Gameplay Toolbox > Poison |
| 8 | 12 | -1.98 | yes | Gameplay Toolbox > Poison |
| 9 | 18 | -3.07 |  | Magic Items > Potion of Poison |
| 10 | 20 | -3.17 | yes | Magic Items > Dagger of Venom |
| 11 | 19 | -3.63 |  | Animals > Actions |
| 12 | 3 | -3.80 |  | Gameplay Toolbox > Pale Tincture (250 GP) |
| 13 | 15 | -3.82 |  | Spells > Poison Spray |
| 14 | 10 | -3.85 |  | Spells > Protection from Poison |
| 15 | 11 | -3.98 | yes | Gameplay Toolbox > Midnight Tears (1,500 GP) |
| 16 | 14 | -4.26 |  | Gameplay Toolbox > Burnt Othur Fumes (500 GP) |
| 17 | 9 | -7.05 |  | Gameplay Toolbox > Harvesting Poison |
| 18 | 7 | -7.80 |  | Gameplay Toolbox > Purchasing Poison |
| 19 | 4 | -8.28 |  | Playing the Game > Damage and Healing |
| 20 | 13 | -9.26 |  | Gameplay Toolbox > Harvesting Poison |

*retrieved sections:* Gameplay Toolbox > Poison | Gameplay Toolbox > Sample Poisons | Rules Glossary > Breaking Objects | Equipment > Poison, Basic (100 GP) | Magic Items > Dagger of Venom | Gameplay Toolbox > Oil of Taggit (400 GP) | Gameplay Toolbox > Crawler Mucus (200 GP) | Gameplay Toolbox > Torpor (600 GP) | Gameplay Toolbox > Midnight Tears (1,500 GP) | Gameplay Toolbox > Malice (250 GP) | Gameplay Toolbox > Essence of Ether (300 GP) | Gameplay Toolbox > Serpent Venom (200 GP) | Gameplay Toolbox > Purple Worm Poison (2,000 GP)

<details><summary>full retrieved context</summary>

```
[Gameplay Toolbox > Poison]
## Poison  
Given their insidious and deadly nature, poisons are a favorite tool among assassins and evil creatures.  
Poisons come in the following four types:  
**Contact.** Contact poison can be smeared on an object and remains potent until it is touched or washed off. A creature that touches contact poison with exposed skin suffers its effects.

---

[Gameplay Toolbox > Sample Poisons]
### Sample Poisons  
Example poisons are detailed here in alphabetical order. Each poison's description includes the suggested price for a single dose of the poison, its type (contact, ingested, inhaled, or injury), and a description of the poison's debilitating effects.

---

[Rules Glossary > Breaking Objects]
<td>27 (5d10)</td>
</tr>
</tbody>
</table>  
_Damage Types and Objects._ Objects have Immunity to Poison and Psychic damage. The GM might decide that some damage types are more or less effective against an object. For example, Bludgeoning damage works well for smashing things but not for cutting. Paper or cloth objects might have Vulnerability to Fire damage.

---

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

[Gameplay Toolbox > Oil of Taggit (400 GP)]
#### Oil of Taggit (400 GP)  
_Contact Poison_  
A creature subjected to Oil of Taggit must succeed on a DC 13 Constitution saving throw or have the Poisoned condition for 24 hours. The creature also has the Unconscious condition while Poisoned in this way. It wakes up if it takes damage.

---

[Gameplay Toolbox > Crawler Mucus (200 GP)]
#### Crawler Mucus (200 GP)  
_Contact Poison_  
A creature subjected to Crawler Mucus must succeed on a DC 13 Constitution saving throw or have the Poisoned condition for 1 minute. The creature also has the Paralyzed condition while Poisoned in this way. The creature repeats the save at the end of each of its turns, ending the effect on itself on a success.

---

[Gameplay Toolbox > Poison]
**Ingested.** A creature must swallow an entire dose of ingested poison to suffer its effects. The dose can be delivered in food or a liquid. You may decide that a partial dose has a reduced effect, such as allowing Advantage on the saving throw or dealing only half as much damage on a failed save.

---

[Gameplay Toolbox > Torpor (600 GP)]
#### Torpor (600 GP)  
_Ingested Poison_  
A creature subjected to Torpor poison must succeed on a DC 15 Constitution saving throw or have the Poisoned condition for 4d6 hours. The creature's Speed is halved while the creature is Poisoned in this way.

---

[Gameplay Toolbox > Midnight Tears (1,500 GP)]
#### Midnight Tears (1,500 GP)  
_Ingested Poison_  
A creature that ingests Midnight Tears suffers no effect until the stroke of midnight. Any effect that
ends the Poisoned condition neutralizes this poison. If the poison hasn't been neutralized before midnight, the creature makes a DC 17 Constitution saving throw, taking 31 (9d6) Poison damage on a failed save or half as much damage on a successful one.

---

[Gameplay Toolbox > Poison]
**Inhaled.** Poisonous powders and gases take effect when inhaled. Blowing the powder or releasing the gas subjects creatures in a 5-foot Cube to its effect. The resulting cloud dissipates immediately afterward. Holding one's breath is ineffective against inhaled poisons, as they affect nasal membranes, tear ducts, and other parts of the body.

---

[Gameplay Toolbox > Malice (250 GP)]
#### Malice (250 GP)  
_Inhaled Poison_  
A creature subjected to Malice must succeed on a DC 15 Constitution saving throw or have the Poisoned condition for 1 hour. The creature also has the Blinded condition while Poisoned in this way.

---

[Gameplay Toolbox > Essence of Ether (300 GP)]
#### Essence of Ether (300 GP)  
_Inhaled Poison_  
A creature subjected to Essence of Ether must succeed on a DC 15 Constitution saving throw or have the Poisoned condition for 8 hours. The creature also has the Unconscious condition while Poisoned in this way. The creature wakes up if it takes damage or if another creature takes an action to shake it awake.

---

[Gameplay Toolbox > Serpent Venom (200 GP)]
#### Serpent Venom (200 GP)  
_Injury Poison_  
A creature subjected to Serpent Venom must succeed on a DC 11 Constitution saving throw, taking 10 (3d6) Poison damage on a failed save or half as much damage on a successful one.

---

[Gameplay Toolbox > Purple Worm Poison (2,000 GP)]
#### Purple Worm Poison (2,000 GP)  
_Injury Poison_  
A creature subjected to Purple Worm Poison makes a DC 21 Constitution saving throw, taking 35 (10d6) Poison damage on a failed save or half as much damage on a successful one.
```
</details>


---

## q15 (multi-part) Describe death saving throws: what roll counts as a success, what happens on a natural 1 and a natural 20, and what DC and check is needed to stabilize a creature with the Help action?

**Gold facts (counterfactual data):** 12 or higher; third failure; two failures; regain 1 Hit Point; DC 10 Wisdom (Medicine)


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Death saving throws:** At the start of its turn, a creature at 0 HP that isn't stable makes a d20 death saving throw, with no modifiers.

- **Success:** a roll of 10 or higher. Three successes make the creature stable: it stays unconscious at 0 HP but stops making death saves.
- **Failure:** a roll of 9 or lower. Three failures mean the creature dies. Taking damage while at 0 HP counts as one failure, and a critical hit counts as two.
- **Natural 20:** the creature regains 1 HP and is no longer unconscious. Its death saves reset.
- **Natural 1:** the roll counts as two failures.

**Stabilizing:** The Help action doesn't stabilize a creature. It gives an ally advantage on an ability check or attack, but it doesn't stop death saves. To stabilize a dying creature, use your action to make a **Wisdom (Medicine) check against DC 10**. On success, the creature becomes stable. A Healer's Kit can also stabilize a creature automatically, using one of its uses.

*facts found (judge): 4/5; missing: 12 or higher*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Success:** Roll 1d20. A roll of **12 or higher** is a success; anything lower is a failure. Three successes make you Stable, and three failures kill you.

**Natural 1:** You suffer **two failures**.

**Natural 20:** You **regain 1 Hit Point**. Since a 20 is also 12 or higher, it counts as a success. Regaining any Hit Points resets your success and failure counts to zero.

**Stabilizing with the Help action:** Make a **DC 10 Wisdom (Medicine)** check.

*facts found (judge): 4/5; missing: third failure*

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

**Death saving throws:**
- **Success:** Roll 1d20. A roll of **12 or higher** is a success; anything lower is a failure. Three successes make you Stable; three failures kill you. Successes and failures don't need to be consecutive, and both counts reset to zero when you regain any Hit Points or become Stable.
- **Natural 1:** You suffer **two failures**.
- **Natural 20:** You **regain 1 Hit Point**.

**Stabilizing with the Help action:** The Context doesn't say. It mentions a "Stabilizing a Character" section, but that section isn't included, so I can't state the DC or check.

*facts found (judge): 4/5; missing: DC 10 Wisdom (Medicine)*


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

**Success:** Roll 1d20. A roll of 12 or higher is a success; anything lower is a failure. Three successes make the creature Stable, and three failures kill it.

**Natural 1:** Counts as two failures.

**Natural 20:** The creature regains 1 Hit Point.

**Stabilizing with Help:** Another creature can take the Help action on a creature with 0 Hit Points. This requires a successful **DC 10 Wisdom (Medicine) check**.

*facts found (judge): 5/5; missing: none*


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

**Success:** Roll 1d20. A roll of 12 or higher is a success; anything lower is a failure. Three successes make you Stable, and three failures kill you.

**Natural 1:** Counts as two failures.

**Natural 20:** You regain 1 Hit Point.

**Stabilizing with the Help action:** The Context doesn't include this. It refers to a "Stabilizing a Character" section, but that text isn't provided, so I can't state the DC or check.

*facts found (judge): 4/5; missing: DC 10 Wisdom (Medicine)*


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

**Success:** A death saving throw is a success on a roll of 12 or higher on the d20. Otherwise it is a failure. Three successes make you Stable, and three failures kill you.

**Natural 1:** Rolling a 1 counts as two failures.

**Natural 20:** Rolling a 20 lets you regain 1 Hit Point.

**Stabilizing with Help:** Taking the Help action requires a successful **DC 10 Wisdom (Medicine)** check.

*facts found (judge): 5/5; missing: none*


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

**Success:** Roll 1d20. A roll of **12 or higher** is a success; anything lower is a failure. Three successes make you Stable, and three failures kill you.

**Natural 1:** You suffer **two failures**.

**Natural 20:** You **regain 1 Hit Point**.

**Stabilizing with the Help action:** Make a **DC 10 Wisdom (Medicine)** check.

*facts found (judge): 5/5; missing: none*


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


### v6_agentic  (15 chunks, 3 LLM call(s))

**Success:** Roll 1d20. A roll of **12 or higher** is a success. Otherwise it's a failure. Three successes make the creature Stable, and three failures mean death.

**Natural 1:** You suffer **two failures**.

**Natural 20:** You **regain 1 Hit Point**.

**Stabilizing with the Help action:** Make a **DC 10 Wisdom (Medicine)** check. The Stabilizing section says this is the check needed to stabilize a creature with 0 Hit Points. The Help action glossary entry in the Context doesn't mention stabilizing, so this comes from the Stabilizing a Character section.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* D&D 5e death saving throws / D&D 5e natural 20 death save / D&D 5e natural 1 death save / D&D 5e stabilize creature / D&D 5e Help action / D&D 5e unconscious creature Medicine check DC 10


*re-ranking* (query: `D&D 5e death saving throws`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.81 | yes | Playing the Game > Death Saving Throws |
| 2 | 2 | 2.99 | yes | Playing the Game > Death Saving Throws |
| 3 | 14 | 1.48 | yes | Playing the Game > Saving Throws |
| 4 | 7 | 1.46 | yes | Playing the Game > Death Saving Throws |
| 5 | 3 | 1.14 |  | Rules Glossary > Death Saving Throw |
| 6 | 10 | 0.33 | yes | Classes > Level 18: Survivor |
| 7 | 6 | 0.20 | yes | Playing the Game > Stabilizing a Character |
| 8 | 13 | 0.09 |  | Rules Glossary > Saving Throw |
| 9 | 4 | -0.98 |  | Playing the Game > Falling Unconscious |
| 10 | 15 | -1.35 |  | Character Creation > Fill In Numbers |
| 11 | 5 | -1.99 | yes | Rules Glossary > Stable |
| 12 | 9 | -2.00 |  | Playing the Game > Saving Throws and Damage |
| 13 | 8 | -2.20 |  | Spells > Finger of Death |
| 14 | 12 | -2.72 |  | Spells > Beacon of Hope |
| 15 | 17 | -2.73 |  | Gameplay Toolbox > Assassin's Blood (150 GP) |
| 16 | 11 | -3.58 |  | Spells > Circle of Death |
| 17 | 16 | -4.13 |  | Gameplay Toolbox > Poisoned Needle |
| 18 | 20 | -7.16 | yes | Playing the Game > Rhythm of Play |
| 19 | 18 | -10.34 |  | Character Creation > Starting at Higher Levels |
| 20 | 19 | -10.93 |  | Monsters A–Z > Actions |


*re-ranking* (query: `D&D 5e natural 20 death save`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.88 | yes | Playing the Game > Death Saving Throws |
| 2 | 2 | -1.05 | yes | Classes > Level 18: Survivor |
| 3 | 4 | -1.50 | yes | Playing the Game > Rolling 20 or 1 |
| 4 | 14 | -3.98 | yes | Magic Items > Periapt of Wound Closure |
| 5 | 15 | -4.03 |  | Magic Items > Avatar of Death |
| 6 | 17 | -5.11 | yes | Playing the Game > Death Saving Throws |
| 7 | 6 | -5.87 | yes | Playing the Game > Death Saving Throws |
| 8 | 7 | -6.12 | yes | Playing the Game > Stabilizing a Character |
| 9 | 11 | -6.36 |  | Rules Glossary > Death Saving Throw |
| 10 | 5 | -7.96 |  | Spells > Finger of Death |
| 11 | 3 | -8.17 |  | Spells > Circle of Death |
| 12 | 10 | -8.69 |  | Gameplay Toolbox > Purple Worm Poison (2,000 GP) |
| 13 | 8 | -8.86 | yes | Rules Glossary > Stable |
| 14 | 16 | -9.06 |  | Gameplay Toolbox > Assassin's Blood (150 GP) |
| 15 | 13 | -10.02 | yes | Playing the Game > Rhythm of Play |
| 16 | 12 | -10.30 |  | Spells > Spare the Dying |
| 17 | 19 | -10.35 |  | Playing the Game > Rhythm of Play |
| 18 | 18 | -10.58 |  | Classes > Level 3: Land's Aid |
| 19 | 20 | -11.06 |  | Classes > Level 14: Disciplined Survivor |
| 20 | 9 | -11.07 |  | Character Creation > Starting at Higher Levels |


*re-ranking* (query: `D&D 5e natural 1 death save`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.27 | yes | Playing the Game > Death Saving Throws |
| 2 | 14 | -2.67 | yes | Magic Items > Periapt of Wound Closure |
| 3 | 12 | -4.26 | yes | Playing the Game > Death Saving Throws |
| 4 | 5 | -4.39 | yes | Playing the Game > Stabilizing a Character |
| 5 | 6 | -4.48 | yes | Playing the Game > Death Saving Throws |
| 6 | 2 | -4.76 | yes | Classes > Level 18: Survivor |
| 7 | 4 | -5.03 |  | Rules Glossary > Death Saving Throw |
| 8 | 9 | -6.33 |  | Monsters A–Z > Traits |
| 9 | 3 | -7.54 |  | Spells > Circle of Death |
| 10 | 7 | -7.54 | yes | Rules Glossary > Stable |
| 11 | 19 | -7.73 |  | Monsters A–Z > Death Dog |
| 12 | 17 | -7.81 |  | Classes > Level 6: Natural Recovery |
| 13 | 8 | -7.83 |  | Playing the Game > Falling Unconscious |
| 14 | 18 | -8.13 |  | Spells > Resurrection |
| 15 | 20 | -8.75 |  | Spells > Phantasmal Killer |
| 16 | 10 | -9.16 |  | Spells > Raise Dead |
| 17 | 13 | -9.34 | yes | Playing the Game > Rhythm of Play |
| 18 | 15 | -9.74 |  | Playing the Game > Rhythm of Play |
| 19 | 16 | -10.10 |  | Spells > Spare the Dying |
| 20 | 11 | -10.83 |  | Character Creation > Starting at Higher Levels |


*re-ranking* (query: `D&D 5e stabilize creature`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 10 | 0.90 | yes | Playing the Game > Stabilizing a Character |
| 2 | 6 | -1.71 | yes | Equipment > Healer's Kit (5 GP) |
| 3 | 1 | -3.10 | yes | Rules Glossary > Stable |
| 4 | 17 | -5.59 |  | Monsters A–Z > Actions |
| 5 | 4 | -7.90 | yes | Playing the Game > Rhythm of Play |
| 6 | 8 | -8.11 |  | Playing the Game > Rhythm of Play |
| 7 | 18 | -8.14 |  | Spells > Antipathy/Sympathy |
| 8 | 9 | -8.77 |  | Animals > Actions |
| 9 | 20 | -8.93 |  | Equipment > Rope (1 GP) |
| 10 | 5 | -9.14 |  | Monsters A–Z > Actions |
| 11 | 13 | -9.31 |  | Monsters A–Z > Actions |
| 12 | 2 | -9.69 |  | Character Creation > Starting at Higher Levels |
| 13 | 7 | -9.70 |  | Animals > Actions |
| 14 | 3 | -9.83 |  | Monsters A–Z > Actions |
| 15 | 15 | -9.99 |  | Monsters A–Z > Actions |
| 16 | 11 | -10.10 |  | Animals > Actions |
| 17 | 12 | -10.27 |  | Rules Glossary > Creature |
| 18 | 16 | -10.29 |  | Rules Glossary > Monster |
| 19 | 14 | -10.49 |  | Spells > Locate Creature |
| 20 | 19 | -11.14 |  | Animals > Actions |


*re-ranking* (query: `D&D 5e Help action`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -0.45 | yes | Rules Glossary > Help [Action] |
| 2 | 2 | -1.42 | yes | Rules Glossary > Help [Action] |
| 3 | 7 | -1.82 | yes | Playing the Game > Rhythm of Play |
| 4 | 10 | -3.65 |  | Playing the Game > Rhythm of Play |
| 5 | 3 | -4.56 |  | Playing the Game > One Thing at a Time |
| 6 | 20 | -4.57 | yes | Playing the Game > Stabilizing a Character |
| 7 | 9 | -5.03 |  | Playing the Game > Actions |
| 8 | 8 | -6.89 |  | Character Creation > Starting at Higher Levels |
| 9 | 4 | -7.14 |  | Rules Glossary > Action |
| 10 | 14 | -7.24 |  | Classes > Level 10: Tireless |
| 11 | 18 | -7.96 |  | Playing the Game > Actions |
| 12 | 13 | -8.86 |  | Playing the Game > Your Turn |
| 13 | 12 | -8.99 |  | Monsters A–Z > Actions |
| 14 | 5 | -9.32 |  | Rules Glossary > Ready [Action] |
| 15 | 6 | -10.05 |  | Rules Glossary > Utilize [Action] |
| 16 | 11 | -10.43 |  | Monsters A–Z > Actions |
| 17 | 19 | -10.73 |  | Monsters A–Z > Bonus Actions |
| 18 | 17 | -10.80 |  | Monsters A–Z > Actions |
| 19 | 16 | -11.37 |  | Playing the Game > Special Senses |
| 20 | 15 | -11.39 |  | Rules Glossary > Indifferent [Attitude] |


*re-ranking* (query: `D&D 5e unconscious creature Medicine check DC 10`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.54 | yes | Playing the Game > Healing |
| 2 | 2 | 3.43 | yes | Rules Glossary > Knocking Out a Creature |
| 3 | 5 | 3.28 | yes | Playing the Game > Stabilizing a Character |
| 4 | 4 | 0.10 |  | Monsters A–Z > Actions |
| 5 | 20 | -0.53 |  | Monsters A–Z > Traits |
| 6 | 16 | -0.96 |  | Gameplay Toolbox > Falling Net |
| 7 | 14 | -1.80 | yes | Equipment > Healer's Kit (5 GP) |
| 8 | 9 | -2.02 |  | Gameplay Toolbox > Spider's Sting (200 GP) |
| 9 | 10 | -2.71 |  | Monsters A–Z > Actions |
| 10 | 8 | -2.72 |  | Gameplay Toolbox > Essence of Ether (300 GP) |
| 11 | 12 | -3.35 |  | Gameplay Toolbox > Harvesting Poison |
| 12 | 11 | -3.42 |  | Gameplay Toolbox > Oil of Taggit (400 GP) |
| 13 | 6 | -3.43 |  | Monsters A–Z > Actions |
| 14 | 7 | -4.11 |  | Gameplay Toolbox > Poisoned Needle |
| 15 | 3 | -4.61 |  | Monsters A–Z > Actions |
| 16 | 18 | -5.14 |  | Equipment > Lock (10 GP) |
| 17 | 15 | -7.62 |  | Monsters A–Z > Actions |
| 18 | 13 | -11.15 |  | Playing the Game > Falling Unconscious |
| 19 | 17 | -11.23 |  | Character Creation > Starting at Higher Levels |
| 20 | 19 | -11.29 |  | Playing the Game > Actions |

*retrieved sections:* Playing the Game > Death Saving Throws | Playing the Game > Saving Throws | Classes > Level 18: Survivor | Playing the Game > Rolling 20 or 1 | Magic Items > Periapt of Wound Closure | Playing the Game > Stabilizing a Character | Equipment > Healer's Kit (5 GP) | Rules Glossary > Stable | Rules Glossary > Help [Action] | Playing the Game > Rhythm of Play | Playing the Game > Healing | Rules Glossary > Knocking Out a Creature

<details><summary>full retrieved context</summary>

```
[Playing the Game > Death Saving Throws]
**Rolling a 1 or 20.** When you roll a 1 on the d20 for a Death Saving Throw, you suffer two failures. If you roll a 20 on the d20, you regain 1 Hit Point.  
**Damage at 0 Hit Points.** If you take any damage while you have 0 Hit Points, you suffer a Death Saving Throw failure. If the damage is from a Critical Hit, you suffer two failures instead. If the damage equals or exceeds your Hit Point maximum, you die.

---

[Playing the Game > Death Saving Throws]
#### Death Saving Throws  
Whenever you start your turn with 0 Hit Points, you must make a Death Saving Throw to determine whether you creep closer to death or hang on to life. Unlike other saving throws, this one isn't tied to an ability score. You're in the hands of fate now.

---

[Playing the Game > Saving Throws]
### Saving Throws  
A saving throw—also called a save—represents an attempt to evade or resist a threat, such as a fiery explosion, a blast of poisonous gas, or a spell trying to invade your mind. You don't normally choose to make a save; you must make one because your character or a monster (if you're the GM) is at risk. A save's result is detailed in the effect that caused it.  
If you don't want to resist the effect, you can choose to fail the save without rolling.

---

[Classes > Level 18: Survivor]
#### Level 18: Survivor  
You attain the pinnacle of resilience in battle, giving you these benefits.  
_Defy Death._ You have Advantage on Death Saving Throws. Moreover, when you roll 18–20 on a Death Saving Throw, you gain the benefit of rolling a 20 on it.  
_Heroic Rally._ At the start of each of your turns, you regain Hit Points equal to 5 plus your Constitution modifier if you are Bloodied and have at least 1 Hit Point.

---

[Playing the Game > Rolling 20 or 1]
#### Rolling 20 or 1  
If you roll a 20 on the d20 (called a "natural 20") for an attack roll, the attack hits regardless of any modifiers or the target's AC. This is called a Critical Hit (see "Combat" later in "Playing the Game").  
If you roll a 1 on the d20 (a "natural 1") for an attack roll, the attack misses regardless of any modifiers or the target's AC.

---

[Magic Items > Periapt of Wound Closure]
#### Periapt of Wound Closure  
_Wondrous Item, Uncommon (Requires Attunement)_  
While wearing this pendant, you gain the following benefits.  
**_Life Preservation._** Whenever you make a Death Saving Throw, you can change a roll of 9 or lower to a 10, turning a failed save into a successful one.  
**_Natural Healing Boost._** Whenever you roll a Hit Point Die to regain Hit Points, double the number of Hit Points it restores.

---

[Playing the Game > Death Saving Throws]
_Three Successes/Failures._ Roll 1d20. If the roll is 12 or higher, you succeed. Otherwise, you fail. A success or failure has no effect by itself. On your third success, you become Stable (see "Stabilizing a Character" below). On your third failure, you die.  
The successes and failures don't need to be consecutive; keep track of both until you collect three of a kind. The number of both is reset to zero when you regain any Hit Points or become Stable.

---

[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Equipment > Healer's Kit (5 GP)]
#### Healer's Kit (5 GP)  
A Healer's Kit has ten uses. As a Utilize action, you can expend one of its uses to stabilize an Unconscious creature that has 0 Hit Points without needing to make a Wisdom (Medicine) check.

---

[Rules Glossary > Stable]
#### Stable  
A creature is Stable if it has 0 Hit Points but isn't required to make Death Saving Throws. _See also_ "Playing the Game" ("Damage and Healing").

---

[Rules Glossary > Help [Action]]
#### Help [Action]  
When you take the Help action, you do one of the following.  
_Assist an Ability Check._ Choose one of your skill or tool proficiencies and one ally who is near
enough for you to assist verbally or physically when they make an ability check. That ally has Advantage on the next ability check they make with the chosen skill or tool. This benefit expires if the ally doesn't use it before the start of your next turn. The GM has final say on whether your assistance is possible.

---

[Rules Glossary > Help [Action]]
_Assist an Attack Roll._ You momentarily distract an enemy within 5 feet of you, giving Advantage to the next attack roll by one of your allies against that enemy. This benefit expires at the start of your next turn.

---

[Playing the Game > Rhythm of Play]
This pattern holds during every game session (each time you sit down to play D&D), whether the adventurers are talking to a noble, exploring a ruin, or fighting a dragon. In certain situations—particularly combat—the action is more structured, and everyone takes turns.

---

[Playing the Game > Healing]
> **Knocking Out a Creature**
>
> When you would reduce a creature to 0 Hit Points with a melee attack, you can instead reduce the creature to 1 Hit Point and give it the Unconscious condition. It then starts a Short Rest, at the end of which that condition ends on it. The condition ends early if the creature regains any Hit Points or if someone takes an action to administer first aid to it, making a successful DC 10 Wisdom (Medicine) check.

---

[Rules Glossary > Knocking Out a Creature]
#### Knocking Out a Creature  
When you would reduce a creature to 0 Hit Points with a melee attack, you can instead reduce the creature to 1 Hit Point. The creature then has the Unconscious condition and starts a Short Rest.  
The creature remains Unconscious until it regains any Hit Points or until someone uses an action to administer first aid to it, which requires a successful DC 10 Wisdom (Medicine) check.
```
</details>


---

## q16 (cross-file) What are the Hit Point Die and saving throw proficiencies of the Barbarian and of the Bard?

**Gold facts (counterfactual data):** D10 per Barbarian level; D8 per Bard level; Strength and Constitution; Dexterity and Charisma


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Barbarian:** Hit Point Die d12. Saving Throw Proficiencies: Strength and Constitution.

**Bard:** Hit Point Die d8. Saving Throw Proficiencies: Dexterity and Charisma.

*facts found (judge): 3/4; missing: D10 per Barbarian level*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Barbarian:** Hit Point Die is D10 per Barbarian level. Saving Throw Proficiencies are Strength and Constitution.

**Bard:** Hit Point Die is D8 per Bard level. Saving Throw Proficiencies are Dexterity and Charisma.

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

**Barbarian:** Hit Point Die is d10 per Barbarian level. Saving Throw Proficiencies are Strength and Constitution.

**Bard:** Hit Point Die is d8 per Bard level. Saving Throw Proficiencies are Dexterity and Charisma.

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

**Barbarian:**
- Hit Point Die: d10 per Barbarian level
- Saving Throw Proficiencies: Strength and Constitution

**Bard:**
- Hit Point Die: d8 per Bard level
- Saving Throw Proficiencies: Dexterity and Charisma

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

**Barbarian:** Hit Point Die is d10 per Barbarian level. Saving Throw Proficiencies are Strength and Constitution.

**Bard:** Hit Point Die is d8 per Bard level. Saving Throw Proficiencies are Dexterity and Charisma.

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

**Barbarian:** Hit Point Die is D10 per Barbarian level. Saving Throw Proficiencies are Strength and Constitution.

**Bard:** Hit Point Die is D8 per Bard level. Saving Throw Proficiencies are Dexterity and Charisma.

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

**Barbarian:** Hit Point Die is D10 per Barbarian level. Saving Throw Proficiencies are Strength and Constitution.

**Bard:** Hit Point Die is D8 per Bard level. Saving Throw Proficiencies are Dexterity and Charisma.

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

**Barbarian:** Hit Point Die is a d10 per Barbarian level. Saving Throw Proficiencies are Strength and Constitution.

**Bard:** Hit Point Die is a d8 per Bard level. Saving Throw Proficiencies are Dexterity and Charisma.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Barbarian class hit point die / Barbarian class saving throw proficiencies / Bard class hit point die / Bard class saving throw proficiencies


*re-ranking* (query: `Barbarian class hit point die`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 6.71 | yes | Classes > As a Multiclass Character |
| 2 | 2 | 6.10 | yes | Classes > Barbarian |
| 3 | 1 | 5.23 | yes | Character Creation > Gaining a Level |
| 4 | 15 | 4.82 |  | Classes > Level 11: Relentless Rage |
| 5 | 10 | 2.48 |  | Character Creation > Hit Points and Hit Point Dice |
| 6 | 9 | 2.22 |  | Classes > As a Multiclass Character |
| 7 | 16 | 2.01 |  | Classes > As a Multiclass Character |
| 8 | 11 | 1.74 |  | Classes > As a Multiclass Character |
| 9 | 8 | 1.29 |  | Character Creation > Fill In Numbers |
| 10 | 14 | 1.02 |  | Character Creation > Fill In Numbers |
| 11 | 5 | -0.26 |  | Classes > Barbarian Class Features |
| 12 | 18 | -0.83 |  | Classes > Barbarian Class Features |
| 13 | 12 | -1.10 |  | Classes > Barbarian Class Features |
| 14 | 6 | -1.96 |  | Classes > Barbarian Class Features |
| 15 | 20 | -3.09 |  | Classes > Level 3: Barbarian Subclass |
| 16 | 19 | -3.35 |  | Rules Glossary > Short Rest |
| 17 | 3 | -3.53 |  | Character Creation > Hit Points and Hit Point Dice |
| 18 | 13 | -3.84 |  | Playing the Game > Instant Death |
| 19 | 17 | -5.88 |  | Rules Glossary > Hit Point Dice |
| 20 | 7 | -6.73 |  | Playing the Game > Death Saving Throws |


*re-ranking* (query: `Barbarian class saving throw proficiencies`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 6.45 | yes | Classes > Barbarian |
| 2 | 1 | 4.51 | yes | Playing the Game > Saving Throw Proficiencies |
| 3 | 3 | 3.18 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 12 | 2.38 |  | Classes > Level 2: Wild Shape |
| 5 | 17 | 1.81 |  | Classes > Warlock |
| 6 | 14 | 0.92 |  | Classes > Sorcerer |
| 7 | 18 | 0.65 | yes | Classes > Bard |
| 8 | 19 | 0.63 |  | Classes > Cleric |
| 9 | 16 | 0.56 |  | Classes > Druid |
| 10 | 15 | -0.10 |  | Playing the Game > Difficulty Class |
| 11 | 5 | -1.82 |  | Classes > Barbarian Class Features |
| 12 | 10 | -2.86 |  | Classes > Barbarian Class Features |
| 13 | 7 | -4.55 |  | Classes > Barbarian Class Features |
| 14 | 8 | -4.85 |  | Classes > Level 3: Barbarian Subclass |
| 15 | 9 | -4.95 | yes | Classes > As a Multiclass Character |
| 16 | 11 | -6.05 |  | Character Creation > Prerequisites |
| 17 | 13 | -7.00 |  | Classes > As a Level 1 Character |
| 18 | 4 | -7.10 |  | Character Creation > Proficiencies |
| 19 | 6 | -8.06 |  | Character Creation > Choose a Background |
| 20 | 20 | -10.12 |  | Character Origins > Skill Proficiencies |


*re-ranking* (query: `Bard class hit point die`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.90 | yes | Classes > As a Multiclass Character |
| 2 | 6 | 5.22 | yes | Classes > Bard |
| 3 | 3 | 3.10 | yes | Classes > Level 1: Bardic Inspiration |
| 4 | 9 | 2.56 |  | Classes > As a Multiclass Character |
| 5 | 5 | 2.22 |  | Character Creation > Fill In Numbers |
| 6 | 16 | 2.04 |  | Classes > Level 1: Bardic Inspiration |
| 7 | 10 | 2.04 |  | Character Creation > Hit Points and Hit Point Dice |
| 8 | 7 | 2.03 |  | Classes > As a Multiclass Character |
| 9 | 2 | 1.95 |  | Classes > Bard Class Features |
| 10 | 14 | 1.88 | yes | Character Creation > Gaining a Level |
| 11 | 11 | 1.86 |  | Classes > As a Multiclass Character |
| 12 | 17 | -2.36 |  | Classes > Bard Class Features |
| 13 | 15 | -2.39 |  | Rules Glossary > Short Rest |
| 14 | 4 | -2.51 |  | Character Creation > Hit Points and Hit Point Dice |
| 15 | 19 | -2.67 |  | Classes > Bard Class Features |
| 16 | 18 | -2.94 |  | Classes > Bard Class Features |
| 17 | 13 | -3.05 |  | Classes > Level 3: Bard Subclass |
| 18 | 12 | -3.66 |  | Playing the Game > Instant Death |
| 19 | 20 | -4.54 |  | Character Creation > Fill In Numbers |
| 20 | 8 | -5.99 |  | Playing the Game > Death Saving Throws |


*re-ranking* (query: `Bard class saving throw proficiencies`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 5.78 | yes | Classes > Bard |
| 2 | 1 | 4.26 | yes | Playing the Game > Saving Throw Proficiencies |
| 3 | 2 | 2.96 | yes | Playing the Game > Saving Throw Proficiencies |
| 4 | 11 | 1.37 |  | Classes > Cleric |
| 5 | 18 | 1.16 |  | Classes > Level 2: Wild Shape |
| 6 | 6 | 0.96 |  | Classes > Level 2: Expertise |
| 7 | 19 | 0.83 |  | Classes > Druid |
| 8 | 9 | -0.11 |  | Playing the Game > Difficulty Class |
| 9 | 5 | -2.48 |  | Classes > Bard Class Features |
| 10 | 20 | -2.95 |  | Rules Glossary > Difficulty Class |
| 11 | 17 | -3.71 |  | Classes > Level 14: Peerless Skill |
| 12 | 13 | -4.62 |  | Classes > Level 3: Bonus Proficiencies |
| 13 | 10 | -4.91 |  | Classes > Level 3: Bard Subclass |
| 14 | 16 | -5.01 | yes | Classes > As a Multiclass Character |
| 15 | 8 | -5.55 |  | Classes > Level 10: Magical Secrets |
| 16 | 12 | -5.69 |  | Playing the Game > Equipment Proficiencies |
| 17 | 15 | -5.94 |  | Classes > Level 1: Spellcasting |
| 18 | 3 | -6.23 |  | Character Creation > Proficiencies |
| 19 | 7 | -6.91 |  | Character Creation > Choose a Background |
| 20 | 14 | -9.66 |  | Character Origins > Skill Proficiencies |

*retrieved sections:* Classes > As a Multiclass Character | Classes > Barbarian | Character Creation > Gaining a Level | Playing the Game > Saving Throw Proficiencies | Classes > Bard | Classes > Level 1: Bardic Inspiration

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
Each class gives proficiency in at least two saving throws, representing that class's training in evading or resisting certain threats. Wizards, for example, are proficient in Intelligence and Wisdom saves; they train to resist mental assault.

---

[Playing the Game > Saving Throw Proficiencies]
### Saving Throw Proficiencies  
Proficiency in a saving throw lets a character add their Proficiency Bonus to saves that use a particular ability. For example, proficiency in Wisdom saves lets you add your Proficiency Bonus to your Wisdom saves. Some monsters also have saving throw proficiencies, as noted in their stat blocks.

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

[Classes > Level 1: Bardic Inspiration]
_At Higher Levels._ Your Bardic Inspiration die changes when you reach certain Bard levels, as shown in the Bardic Die column of the Bard Features table. The die becomes a d8 at level 5, a d10 at level 10, and a d12 at level 15.
```
</details>


---

## q17 (reasoning) A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What is its attack bonus, its damage on a hit, the extra damage if the attack roll had Advantage, and what AC must the attack beat?

**Gold facts (counterfactual data):** +4; 5 (1d6 + 2); 2 (1d4); 16 in Chain Mail


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Attack bonus:** +4 (Dexterity +2 plus proficiency +2, since the scimitar is a finesse weapon).

**Damage on a hit:** 1d6 + 2 slashing.

**Extra damage with Advantage:** None. The goblin has no feature like Sneak Attack, so Advantage only improves the chance to hit.

**AC to beat:** 16. Chain Mail gives AC 16, and the attack hits if the total equals or exceeds it.

*facts found (judge): 2/4; missing: 5 (1d6 + 2); 2 (1d4)*


### v1_baseline  (3 chunks, 1 LLM call(s))

- **Attack bonus:** +4
- **Damage on a hit:** 5 (1d6 + 2) slashing damage
- **Extra damage with Advantage:** 2 (1d4) slashing damage
- **AC the attack must beat:** The Context doesn't say what AC Chain Mail provides, so this can't be determined from the Context.

*facts found (judge): 3/4; missing: 16 in Chain Mail*

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

**Attack bonus:** +4

**Damage on a hit:** 5 (1d6 + 2) Slashing damage

**Extra damage with Advantage:** 2 (1d4) Slashing damage, added to the hit if the attack roll had Advantage

**AC the attack must beat:** The Context doesn't say. It gives Chain Mail no AC value, and it doesn't state the rule for what a hit requires relative to AC.

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

**Attack bonus:** +4, if the attacker is the goblin. The only goblin entry in the Context gives its Scimitar a +4 attack bonus. The Context never names a "goblin warrior," though, and an unnamed block with a +3 Scimitar (4 damage, no Advantage clause) also exists. Which block applies can't be confirmed from the Context.

**Damage on a hit:** 5 (1d6 + 2) Slashing damage, from the goblin's Scimitar entry.

**Extra damage if the attack roll had Advantage:** 2 (1d4) Slashing damage.

**AC the attack must beat:** The Context doesn't say. It contains no Chain Mail entry, so the AC value for that armor is missing. The Parry reaction doesn't fill the gap either: it adds 2 to the *warrior's* own AC, not the target's, and the Context doesn't say the character is holding a weapon.

*facts found (judge): 3/4; missing: 16 in Chain Mail*


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

The Context doesn't name a "goblin warrior," so I can't tell which entry applies. Two Scimitar entries exist:

- **Entry with Multiattack ("The goblin"):** attack bonus +4, damage 5 (1d6 + 2) Slashing on a hit, plus 2 (1d4) Slashing extra damage if the attack roll had Advantage.
- **Other entry (unnamed):** attack bonus +3, damage 4 (1d6 + 1) Slashing on a hit, with no Advantage extra damage.

The Context doesn't give the AC for Chain Mail, so it doesn't say what AC the attack must beat.

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

**Attack bonus:** +4.

**Damage on a hit:** 5 (1d6 + 2) Slashing damage.

**Extra damage with Advantage:** 2 (1d4) Slashing damage.

**AC the attack must beat:** The Context doesn't give the base AC of Chain Mail, so I can't answer this part. The only AC rule in the Context is the Elven Chain's +1 bonus, which applies only to that specific armor, not to Chain Mail.

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
| 9 | 9 | -4.80 |  | Monsters A–Z > Reactions |
| 10 | 12 | -4.98 |  | Monsters > Attack Notation |
| 11 | 15 | -6.22 |  | Monsters A–Z > Reactions |
| 12 | 3 | -6.24 |  | Monsters A–Z > Reactions |
| 13 | 28 | -6.52 |  | Rules Glossary > Stat Block |
| 14 | 10 | -6.55 |  | Classes > Level 1: Sneak Attack |
| 15 | 8 | -6.60 |  | Monsters A–Z > Actions |
| 16 | 19 | -7.07 |  | Classes > Level 3: Frenzy |
| 17 | 7 | -7.24 |  | Monsters A–Z > Traits |
| 18 | 14 | -7.29 |  | Monsters A–Z > Actions |
| 19 | 22 | -7.32 |  | Monsters A–Z > Actions |
| 20 | 6 | -7.52 |  | Monsters A–Z > Actions |

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

**Attack bonus:** +4 (Melee Attack Roll, reach 5 ft.)

**Damage on a hit:** 5 (1d6 + 2) Slashing damage

**Extra damage with Advantage:** 2 (1d4) Slashing damage, added to the hit

**AC the attack must beat:** The context doesn't say. It doesn't list Chain Mail's AC, and it doesn't state the rule for when an attack hits. The goblin warrior's AC of 17 is the goblin's own AC, not the target's.

*facts found (judge): 3/4; missing: 16 in Chain Mail*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `A goblin warrior attacks a character wearing Chain Mail with its Scimitar. What `): candidate pool of 17, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.06 | yes | Monsters A–Z > Actions |
| 2 | 2 | -2.77 | yes | Monsters A–Z > Actions |
| 3 | 4 | -3.36 | yes | Monsters A–Z > Actions |
| 4 | 11 | -4.06 | yes | Monsters A–Z > Goblin Warrior |
| 5 | 12 | -4.10 | yes | Monsters A–Z > Goblin Warrior |
| 6 | 13 | -4.77 | yes | Monsters A–Z > Goblin Warrior |
| 7 | 9 | -4.80 | yes | Monsters A–Z > Reactions |
| 8 | 3 | -6.24 |  | Monsters A–Z > Reactions |
| 9 | 10 | -6.55 |  | Classes > Level 1: Sneak Attack |
| 10 | 8 | -6.60 |  | Monsters A–Z > Actions |
| 11 | 7 | -7.24 |  | Monsters A–Z > Traits |
| 12 | 6 | -7.52 |  | Monsters A–Z > Actions |
| 13 | 5 | -7.65 |  | Equipment > Armor |
| 14 | 14 | -9.81 |  | Rules Glossary > Armor Class |
| 15 | 16 | -10.19 |  | Monsters A–Z > Bandit |
| 16 | 15 | -10.48 |  | Playing the Game > Armor Class |
| 17 | 17 | -10.50 |  | Monsters A–Z > Bandit |

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

- **Attack bonus:** +4
- **Damage on a hit:** 5 Slashing damage (or 1d6 + 2, but not both)
- **Extra damage with Advantage:** 2 Slashing damage (or 1d4)
- **AC the attack must beat:** 16, since the Context says AC is 16 in Chain Mail.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* goblin monster stat block / scimitar weapon / chain mail armor / advantage rule / armor class rule

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `goblin monster stat block`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.80 | yes | Monsters > Stat Block Overview |
| 2 | 6 | 2.80 | yes | Rules Glossary > Stat Block |
| 3 | 8 | 1.91 |  | Monsters > Alignment |
| 4 | 4 | 1.61 |  | Monsters > Stat Block Overview |
| 5 | 15 | 1.49 |  | Monsters > Stat Block Overview |
| 6 | 14 | 0.93 |  | Monsters > Legendary Actions |
| 7 | 12 | 0.72 |  | Rules Glossary > Stat Block |
| 8 | 20 | 0.51 |  | Rules Glossary > Stat Block |
| 9 | 17 | 0.49 |  | Rules Glossary > Stat Block |
| 10 | 9 | 0.40 |  | Rules Glossary > Stat Block |
| 11 | 19 | 0.29 |  | Rules Glossary > Stat Block |
| 12 | 5 | 0.21 |  | Monsters > Resistances and Vulnerabilities |
| 13 | 10 | 0.01 |  | Rules Glossary > Stat Block |
| 14 | 7 | -0.25 |  | Monsters > Limited Usage |
| 15 | 3 | -0.31 |  | Rules Glossary > Stat Block |
| 16 | 2 | -0.44 |  | Monsters > Parts of a Stat Block |
| 17 | 13 | -0.97 |  | Monsters > Limited Usage |
| 18 | 18 | -1.34 |  | Monsters A–Z > Goblin Boss |
| 19 | 11 | -1.38 |  | Monsters A–Z > Traits |
| 20 | 16 | -1.63 |  | Monsters A–Z > Reactions |


*re-ranking* (query: `scimitar weapon`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.23 | yes | Magic Items > Scimitar of Speed |
| 2 | 3 | 3.80 | yes | Magic Items > Sword of Sharpness |
| 3 | 4 | 3.70 | yes | Magic Items > Vorpal Sword |
| 4 | 2 | 3.42 |  | Magic Items > Dancing Sword |
| 5 | 5 | 3.03 |  | Magic Items > Luck Blade |
| 6 | 6 | 2.79 |  | Magic Items > Sword of Wounding |
| 7 | 8 | 0.76 |  | Classes > Fighter |
| 8 | 19 | -6.84 |  | Magic Items > Sun Blade |
| 9 | 20 | -7.00 |  | Magic Items > Dancing Sword |
| 10 | 15 | -7.51 |  | Classes > Level 3: Sacred Weapon |
| 11 | 17 | -7.71 |  | Magic Items > Thunderous Greatclub |
| 12 | 7 | -7.73 |  | Magic Items > Vicious Weapon |
| 13 | 9 | -7.97 |  | Classes > Level 3: Sacred Weapon |
| 14 | 16 | -8.14 |  | Magic Items > Berserker Axe |
| 15 | 10 | -8.46 |  | Magic Items > Dragon Slayer |
| 16 | 14 | -8.54 |  | Magic Items > Quarterstaff of the Acrobat |
| 17 | 11 | -8.70 |  | Magic Items > Weapon of Warning |
| 18 | 18 | -8.95 |  | Magic Items > Mace of Disruption |
| 19 | 12 | -9.12 |  | Magic Items > Dancing Sword |
| 20 | 13 | -10.19 |  | Magic Items > Flame Tongue |


*re-ranking* (query: `chain mail armor`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.61 | yes | Magic Items > Elven Chain |
| 2 | 8 | 4.88 | yes | Equipment > Armor |
| 3 | 2 | 4.28 | yes | Magic Items > Armor |
| 4 | 7 | 3.81 |  | Classes > Paladin |
| 5 | 18 | 1.92 |  | Classes > Fighter |
| 6 | 3 | 1.88 |  | Equipment > Armor |
| 7 | 4 | 0.60 |  | Equipment > Armor |
| 8 | 6 | -1.75 |  | Magic Items > Dragon Scale Mail |
| 9 | 11 | -1.92 |  | Classes > Cleric |
| 10 | 5 | -2.01 |  | Magic Items > Dragon Scale Mail |
| 11 | 9 | -4.80 |  | Magic Items > Dragon Scale Mail |
| 12 | 12 | -7.13 |  | Equipment > Chain (5 GP) |
| 13 | 17 | -7.68 |  | Equipment > Chain (5 GP) |
| 14 | 20 | -8.49 |  | Magic Items > Armor of Vulnerability |
| 15 | 10 | -8.59 |  | Magic Items > Mithral Armor |
| 16 | 13 | -8.60 |  | Magic Items > Armor, +1, +2, or +3 |
| 17 | 16 | -8.88 |  | Magic Items > Dwarven Plate |
| 18 | 15 | -9.23 |  | Magic Items > Armor of Invulnerability |
| 19 | 14 | -9.48 |  | Magic Items > Plate Armor of Etherealness |
| 20 | 19 | -9.79 |  | Magic Items > Demon Armor |


*re-ranking* (query: `advantage rule`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.02 | yes | Rules Glossary > Advantage |
| 2 | 2 | 1.47 | yes | Playing the Game > Advantage/Disadvantage |
| 3 | 16 | -1.23 | yes | Rules Glossary > Friendly [Attitude] |
| 4 | 12 | -1.81 |  | Rules Glossary > Dodge [Action] |
| 5 | 3 | -2.54 |  | Playing the Game > They Don't Stack |
| 6 | 5 | -3.62 |  | Feats > Grappler |
| 7 | 4 | -4.07 |  | Playing the Game > Roll Two D20s |
| 8 | 9 | -4.47 |  | Rules Glossary > Charmed [Condition] |
| 9 | 6 | -5.98 |  | Playing the Game > Ability Modifiers |
| 10 | 11 | -7.32 |  | Equipment > Crowbar (2 GP) |
| 11 | 18 | -7.79 |  | Playing the Game > Travel Pace |
| 12 | 7 | -8.00 |  | Playing the Game > Ability Modifiers |
| 13 | 10 | -8.35 |  | Rules Glossary > Bonus Action |
| 14 | 17 | -9.26 |  | Rules Glossary > Per Day |
| 15 | 19 | -9.53 |  | Rules Glossary > Teleportation |
| 16 | 20 | -9.58 |  | Rules Glossary > Condition |
| 17 | 8 | -9.64 | yes | Rules Glossary > Armor Class |
| 18 | 15 | -9.92 |  | Playing the Game > Cover |
| 19 | 14 | -10.68 |  | Rules Glossary > Magical Effect |
| 20 | 13 | -10.83 |  | Rules Glossary > Reach |


*re-ranking* (query: `armor class rule`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.98 | yes | Rules Glossary > Armor Class |
| 2 | 4 | 6.09 | yes | Character Creation > Fill In Numbers |
| 3 | 5 | 5.23 | yes | Equipment > Armor |
| 4 | 12 | 4.36 |  | Classes > Level 1: Unarmored Defense |
| 5 | 11 | 4.28 |  | Character Creation > Class Features |
| 6 | 2 | 4.24 |  | Character Creation > Armor Class |
| 7 | 7 | 4.17 |  | Playing the Game > Armor Class |
| 8 | 10 | 3.79 |  | Classes > Level 1: Unarmored Defense |
| 9 | 8 | 2.91 |  | Magic Items > Armor, +1, +2, or +3 |
| 10 | 19 | 2.55 |  | Magic Items > Defender |
| 11 | 15 | 2.20 |  | Playing the Game > Armor Class |
| 12 | 3 | 1.93 |  | Equipment > Armor Training |
| 13 | 18 | 1.89 |  | Equipment > Armor |
| 14 | 20 | 1.81 |  | Equipment > Armor Training |
| 15 | 6 | 1.69 |  | Character Creation > Note Armor Training |
| 16 | 13 | 1.41 |  | Magic Items > Glamoured Studded Leather |
| 17 | 17 | 1.37 |  | Magic Items > Dwarven Plate |
| 18 | 16 | 0.63 |  | Magic Items > Shield, +1, +2, or +3 |
| 19 | 14 | 0.47 |  | Magic Items > Bracers of Defense |
| 20 | 9 | 0.27 | yes | Magic Items > Elven Chain |


*re-ranking* (query: `goblin stat block`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | -0.18 | yes | Monsters > Stat Block Overview |
| 2 | 4 | -0.34 | yes | Rules Glossary > Stat Block |
| 3 | 14 | -2.29 | yes | Monsters > Damage Notation |
| 4 | 8 | -2.41 |  | Monsters > Stat Block Overview |
| 5 | 1 | -2.46 |  | Monsters > Parts of a Stat Block |
| 6 | 10 | -2.73 |  | Monsters > Limited Usage |
| 7 | 17 | -2.78 |  | Rules Glossary > Stat Block |
| 8 | 19 | -3.04 |  | Rules Glossary > Stat Block |
| 9 | 3 | -3.09 |  | Rules Glossary > Stat Block |
| 10 | 11 | -3.77 |  | Monsters A–Z > Bonus Actions |
| 11 | 16 | -3.89 |  | Rules Glossary > Stat Block |
| 12 | 7 | -3.90 |  | Monsters > Resistances and Vulnerabilities |
| 13 | 9 | -4.33 |  | Monsters A–Z > Reactions |
| 14 | 5 | -4.49 |  | Monsters A–Z > Goblin Warrior |
| 15 | 18 | -4.51 |  | Monsters A–Z > Traits |
| 16 | 13 | -4.84 |  | Monsters > Limited Usage |
| 17 | 12 | -5.22 |  | Monsters A–Z > Bugbear Stalker |
| 18 | 6 | -5.22 |  | Monsters A–Z > Traits |
| 19 | 15 | -5.58 |  | Monsters A–Z > Bugbear Warrior |
| 20 | 20 | -5.83 |  | Monsters A–Z > Hobgoblin Captain |


*re-ranking* (query: `goblin scimitar attack bonus damage`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.36 | yes | Monsters A–Z > Actions |
| 2 | 7 | 4.22 | yes | Magic Items > Scimitar of Speed |
| 3 | 8 | 1.98 | yes | Magic Items > Vorpal Sword |
| 4 | 10 | 1.79 |  | Magic Items > Luck Blade |
| 5 | 3 | 0.63 |  | Monsters A–Z > Actions |
| 6 | 4 | 0.40 |  | Monsters A–Z > Actions |
| 7 | 5 | 0.12 |  | Monsters A–Z > Actions |
| 8 | 17 | 0.03 |  | Magic Items > Dancing Sword |
| 9 | 12 | -0.56 |  | Monsters A–Z > Bonus Actions |
| 10 | 18 | -1.20 | yes | Magic Items > Sword of Sharpness |
| 11 | 6 | -1.66 |  | Monsters A–Z > Bonus Actions |
| 12 | 2 | -3.28 |  | Monsters A–Z > Reactions |
| 13 | 9 | -5.29 |  | Classes > Level 13: Improved Brutal Strike |
| 14 | 11 | -6.47 |  | Monsters A–Z > Actions |
| 15 | 13 | -6.70 |  | Monsters A–Z > Actions |
| 16 | 15 | -6.76 |  | Monsters A–Z > Actions |
| 17 | 16 | -7.02 |  | Monsters A–Z > Goblin Boss |
| 18 | 19 | -8.34 |  | Monsters A–Z > Actions |
| 19 | 14 | -8.53 |  | Monsters A–Z > Reactions |
| 20 | 20 | -9.32 |  | Monsters A–Z > Goblin Boss |


*re-ranking* (query: `goblin advantage extra damage`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 2.76 | yes | Monsters A–Z > Actions |
| 2 | 15 | 0.61 |  | Classes > Level 1: Sneak Attack |
| 3 | 6 | 0.52 |  | Classes > Level 1: Sneak Attack |
| 4 | 13 | -1.41 |  | Spells > Shining Smite |
| 5 | 14 | -2.16 |  | Magic Items > Vorpal Sword |
| 6 | 20 | -2.67 |  | Classes > Level 3: Frenzy |
| 7 | 16 | -2.87 |  | Feats > Boon of Irresistible Offense |
| 8 | 9 | -2.97 |  | Spells > Enlarge/Reduce |
| 9 | 12 | -4.11 |  | Magic Items > Vicious Weapon |
| 10 | 4 | -6.04 |  | Monsters A–Z > Bonus Actions |
| 11 | 2 | -6.19 |  | Monsters A–Z > Reactions |
| 12 | 5 | -6.56 |  | Monsters A–Z > Actions |
| 13 | 7 | -6.88 |  | Monsters A–Z > Actions |
| 14 | 8 | -8.06 |  | Feats > Grappler |
| 15 | 3 | -9.08 |  | Monsters A–Z > Goblin Warrior |
| 16 | 18 | -9.45 |  | Monsters A–Z > Bugbear Stalker |
| 17 | 11 | -9.60 |  | Monsters A–Z > Actions |
| 18 | 10 | -9.67 |  | Monsters A–Z > Traits |
| 19 | 17 | -9.79 |  | Monsters A–Z > Bugbear Warrior |
| 20 | 19 | -10.05 |  | Monsters A–Z > Hobgoblin Captain |

*retrieved sections:* Monsters > Stat Block Overview | Monsters > Gear | Rules Glossary > Stat Block | Magic Items > Scimitar of Speed | Magic Items > Sword of Sharpness | Magic Items > Vorpal Sword | Magic Items > Elven Chain | Equipment > Armor | Magic Items > Armor | Rules Glossary > Advantage | Playing the Game > Advantage/Disadvantage | Rules Glossary > Friendly [Attitude] | Rules Glossary > Armor Class | Character Creation > Fill In Numbers | Monsters > Damage Notation | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Monsters > Stat Block Overview]
# Monsters  
## Stat Block Overview  
A monster has a stat block that contains the rules necessary to use it in the game. Stat blocks are divided into the following parts:  
**Name and General Details.** The name of the monster is followed by its size, creature type (along with any descriptive tags), and alignment.  
**Combat Highlights.** Armor Class, Hit Points, Speed, and Initiative are provided here.

---

[Monsters > Gear]
### Gear  
Monsters have proficiency with their equipment. If a monster has equipment that can be given away or retrieved, the items are listed in the Gear entry. The monster's stat block might include special flourishes that happen when the monster uses an item, and the stat block might ignore the rules in "Equipment" for that item. When used by someone else, a retrievable item uses its "Equipment" rules, ignoring any special flourishes in the stat block.

---

[Rules Glossary > Stat Block]
#### Stat Block  
A stat block contains the game statistics of a monster. Each stat block includes the following information presented after the monster's name.  
_Size._ A monster is Tiny, Small, Medium, Large, Huge, or Gargantuan. _See also_ "Size."  
_Creature Type._ This entry notes the family of beings a monster belongs to, along with any descriptive tags. _See also_ "Creature Type."

---

[Magic Items > Scimitar of Speed]
#### Scimitar of Speed  
_Weapon (Scimitar), Very Rare (Requires Attunement)_  
You gain a +2 bonus to attack rolls and damage rolls made with this magic weapon. In addition, you can make one attack with it as a Bonus Action on each of your turns.

---

[Magic Items > Sword of Sharpness]
#### Sword of Sharpness  
_Weapon (Glaive, Greatsword, Longsword, or Scimitar), Very Rare (Requires Attunement)_  
When you attack an object with this magic weapon and hit, maximize your weapon damage dice against the target.  
When you attack a creature with this weapon and roll a 20 on the d20 for the attack roll, that target takes an extra 14 Slashing damage and gains 1 Exhaustion level.

---

[Magic Items > Vorpal Sword]
#### Vorpal Sword  
_Weapon (Glaive, Greatsword, Longsword, or Scimitar), Legendary (Requires Attunement)_  
You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon. In addition, the weapon ignores Resistance to Slashing damage.

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

[Magic Items > Armor]
### Armor  
An item in the Armor category is typically a magical version of armor from "Equipment." Unless an armor's description notes otherwise, the armor must be worn for its magic to function.  
Some suits of magic armor specify the type of armor they are, such as Chain Mail or Plate Armor. If no type is specified, choose the type or determine it randomly.

---

[Rules Glossary > Advantage]
#### Advantage  
If you have Advantage on a D20 Test, roll two d20s, and use the higher roll. A roll can't be affected by more than one Advantage, and Advantage and Disadvantage on the same roll cancel each other. _See also_ "Playing the Game" ("D20 Tests").

---

[Playing the Game > Advantage/Disadvantage]
### Advantage/Disadvantage  
Sometimes a D20 Test is modified by Advantage or Disadvantage. Advantage reflects the positive circumstances surrounding a d20 roll, while Disadvantage reflects negative circumstances.  
You usually acquire Advantage or Disadvantage through the use of special abilities and actions. The GM can also decide that circumstances grant Advantage or impose Disadvantage.

---

[Rules Glossary > Friendly [Attitude]]
#### Friendly [Attitude]  
A Friendly creature views you favorably. You have Advantage on an ability check to influence a Friendly creature. _See also_ "Influence."

---

[Rules Glossary > Armor Class]
#### Armor Class  
An Armor Class (AC) is the target number for an attack roll. AC represents how difficult it is to hit a target.  
Your base AC calculation is 10 plus your Dexterity modifier. If a rule gives you another base AC calculation, you choose which calculation to use; you can't use more than one. _See also_ "Attack Roll."

---

[Character Creation > Fill In Numbers]
_Armor Class_. Without armor or a shield, your base Armor Class is 10 plus your Dexterity modifier. If your starting equipment includes armor or a Shield (or both), calculate your AC using the rules in "Equipment." A class feature might give you a different way to calculate your AC.

---

[Monsters > Damage Notation]
#### Damage Notation  
A stat block usually provides both a number and a die expression for each instance of damage. For example, an attack might deal 4 (1d4 + 2) damage on a hit. You decide whether to use the number or the die expression in parentheses; don't use both.

---

[Monsters A–Z > Actions]
#### Actions  
<hr>  
**_Multiattack._** The goblin makes two attacks, using Scimitar or Shortbow in any combination.  
**_Scimitar._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Slashing damage, plus 2 (1d4) Slashing damage if the attack roll had Advantage.  
**_Shortbow._** _Ranged Attack Roll:_ +4, range 80/320 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, plus 2 (1d4) Piercing damage if the attack roll had Advantage.
```
</details>


---

## q18 (reasoning) A wizard casts Fireball using a 5th-level spell slot. How much damage dice does it deal in total, and what saving throw do targets make?

**Gold facts (counterfactual data):** Dexterity; 11d6


### v0_closed_book  (0 chunks, 1 LLM call(s))

A 5th-level Fireball deals **10d6 fire damage** in total. The spell's base damage is 8d6 at 3rd level, and each slot level above 3rd adds 1d6, so the 5th-level slot adds 2d6.

Targets make a **Dexterity saving throw**. On a success, they take half damage.

*facts found (judge): 1/2; missing: 11d6*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Damage:** 11d6 Fire damage. The base is 9d6, and casting with a 5th-level slot adds 1d6 for each level above 3 (2 levels), so 9d6 + 2d6 = 11d6.

**Saving throw:** Dexterity saving throw. A target takes the full damage on a failed save and half on a successful one.

*facts found (judge): 2/2; missing: none*

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

The Context gives Fireball's base damage as **9d6** Fire, but it doesn't say how casting with a 5th-level slot changes that, so I can't state the total dice for that slot level.

Targets make a **Dexterity saving throw**. On a failed save they take the full damage, and on a success they take half.

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

A Fireball cast with a 5th-level spell slot deals **11d6 Fire damage** in total. The base is 9d6, and the Higher-Level rule adds 1d6 for each spell slot level above 3, so 2 extra levels add 2d6.

Targets make a **Dexterity saving throw**. They take the full damage on a failed save or half on a successful one.

*facts found (judge): 2/2; missing: none*


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

**Damage dice:** The Context gives Fireball's damage as 9d6 Fire, but it has no higher-level casting rule for Fireball. The only upcasting rule provided is for Cloudkill, so the context doesn't say how many dice a 5th-level slot adds.

**Saving throw:** Targets make a Dexterity saving throw.

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

Fireball deals **9d6 Fire damage** according to the Context. The Context has no "Using a Higher-Level Spell Slot" entry for Fireball, so it doesn't say whether a 5th-level slot adds any dice. The answer for the 5th-level slot is therefore missing from the Context, and I can only give the base 9d6.

Targets make a **Dexterity saving throw**. They take the full damage on a failed save and half on a successful one.

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

A Fireball cast with a 5th-level spell slot deals **11d6 Fire damage** in total. The base is 9d6, and the context adds 1d6 for each spell slot level above 3. A 5th-level slot is 2 levels above 3, so that adds 2d6 (9d6 + 2d6 = 11d6).

Targets make a **Dexterity saving throw**. A failed save takes the full damage, and a successful save takes half.

*facts found (judge): 2/2; missing: none*


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


### v6_agentic  (11 chunks, 3 LLM call(s))

**11d6 Fire damage** in total: the base 9d6 plus 2d6 for the two spell slot levels above 3rd. Targets make a **Dexterity saving throw**.

*facts found (judge): 2/2; missing: none*

*agentic sub-queries:* Fireball spell / Dexterity saving throw / Area of effect sphere


*re-ranking* (query: `Fireball spell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 6.65 | yes | Spells > Delayed Blast Fireball |
| 2 | 8 | 6.39 | yes | Spells > Delayed Blast Fireball |
| 3 | 1 | 6.11 | yes | Spells > Fireball |
| 4 | 2 | 6.10 | yes | Spells > Delayed Blast Fireball |
| 5 | 3 | 5.76 | yes | Spells > Fireball |
| 6 | 7 | 5.41 |  | Magic Items > Wand of Fireballs |
| 7 | 19 | 5.12 |  | Monsters A–Z > Actions |
| 8 | 4 | 4.75 |  | Spells > Delayed Blast Fireball |
| 9 | 15 | 3.82 |  | Magic Items > Helm of Brilliance |
| 10 | 9 | 3.68 |  | Magic Items > Hat of Many Spells |
| 11 | 12 | 2.79 |  | Classes > Level 7 Sorcerer Spells |
| 12 | 5 | 2.67 |  | Magic Items > Staff of Power |
| 13 | 10 | 2.51 |  | Classes > Level 7 Wizard Spells |
| 14 | 14 | 2.12 |  | Classes > Level 3 Sorcerer Spells |
| 15 | 20 | 2.01 |  | Spells > Flaming Sphere |
| 16 | 13 | 1.87 |  | Classes > Level 3 Wizard Spells |
| 17 | 11 | 1.29 |  | Magic Items > Necklace of Fireballs |
| 18 | 18 | -1.81 |  | Magic Items > Staff of the Magi |
| 19 | 17 | -2.50 |  | Magic Items > Staff of Fire |
| 20 | 16 | -6.24 |  | Rules Glossary > Spell |


*re-ranking* (query: `Dexterity saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 17 | 7.94 | yes | Spells > Earthquake |
| 2 | 2 | 7.93 | yes | Magic Items > Staff of Power |
| 3 | 3 | 7.89 | yes | Magic Items > Staff of the Magi |
| 4 | 12 | 7.53 |  | Spells > Chain Lightning |
| 5 | 9 | 7.23 |  | Spells > Earthquake |
| 6 | 13 | 7.03 |  | Spells > Conjure Animals |
| 7 | 19 | 6.96 |  | Classes > Level 7: Evasion |
| 8 | 6 | 6.60 |  | Equipment > Net (1 GP) |
| 9 | 16 | 6.57 |  | Animals > Bonus Actions |
| 10 | 4 | 6.55 |  | Monsters A–Z > Bonus Actions |
| 11 | 14 | 6.44 |  | Monsters A–Z > Actions |
| 12 | 11 | 6.11 |  | Spells > Grease |
| 13 | 7 | 6.10 |  | Rules Glossary > Unarmed Strike |
| 14 | 20 | 6.01 |  | Monsters A–Z > Actions |
| 15 | 15 | 5.89 |  | Monsters A–Z > Actions |
| 16 | 1 | 5.07 |  | Playing the Game > Ability Modifier |
| 17 | 8 | 4.81 |  | Magic Items > Ring of Evasion |
| 18 | 18 | 2.77 |  | Rules Glossary > Saving Throw |
| 19 | 10 | 2.17 |  | Playing the Game > Saving Throw Proficiencies |
| 20 | 5 | -1.22 |  | Rules Glossary > Save |


*re-ranking* (query: `Area of effect sphere`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 9.13 | yes | Rules Glossary > Sphere [Area of Effect] |
| 2 | 2 | 7.20 | yes | Rules Glossary > Area of Effect |
| 3 | 3 | 5.03 | yes | Rules Glossary > Area of Effect |
| 4 | 8 | 4.50 |  | Spells > Targets |
| 5 | 5 | 2.37 |  | Magic Items > Bead of Force |
| 6 | 11 | 2.30 |  | Rules Glossary > Area of Effect |
| 7 | 4 | 2.21 |  | Rules Glossary > Cube [Area of Effect] |
| 8 | 10 | 1.92 |  | Rules Glossary > Line [Area of Effect] |
| 9 | 15 | 1.83 |  | Rules Glossary > Emanation [Area of Effect] |
| 10 | 6 | 1.80 |  | Rules Glossary > Cylinder [Area of Effect] |
| 11 | 9 | 1.04 |  | Rules Glossary > Cone [Area of Effect] |
| 12 | 7 | -0.77 |  | Rules Glossary > Cone [Area of Effect] |
| 13 | 12 | -1.19 |  | Magic Items > Bead of Force |
| 14 | 14 | -2.23 |  | Spells > Vitriolic Sphere |
| 15 | 19 | -3.86 |  | Magic Items > Sphere of Annihilation |
| 16 | 16 | -4.36 |  | Spells > Freezing Sphere |
| 17 | 13 | -4.58 |  | Magic Items > Sphere of Annihilation |
| 18 | 17 | -5.69 |  | Magic Items > Sphere of Annihilation |
| 19 | 18 | -6.45 |  | Spells > Flaming Sphere |
| 20 | 20 | -7.59 |  | Spells > Vitriolic Sphere |


*re-ranking* (query: `Fireball spell base damage dice`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 6.56 | yes | Spells > Delayed Blast Fireball |
| 2 | 1 | 4.80 | yes | Spells > Delayed Blast Fireball |
| 3 | 2 | 2.58 | yes | Spells > Fireball |
| 4 | 7 | 2.18 | yes | Spells > Delayed Blast Fireball |
| 5 | 4 | 2.07 |  | Playing the Game > Damage against Multiple Targets |
| 6 | 16 | 1.89 |  | Spells > Flame Strike |
| 7 | 6 | 1.31 | yes | Spells > Fireball |
| 8 | 5 | 0.98 |  | Playing the Game > Damage Rolls |
| 9 | 9 | 0.90 |  | Playing the Game > Damage Rolls |
| 10 | 18 | 0.90 |  | Spells > Wall of Fire |
| 11 | 8 | -1.70 |  | Monsters A–Z > Actions |
| 12 | 13 | -1.72 |  | Magic Items > Necklace of Fireballs |
| 13 | 15 | -3.00 |  | Spells > Burning Hands |
| 14 | 11 | -3.08 |  | Magic Items > Wand of Fireballs |
| 15 | 12 | -3.16 |  | Spells > Delayed Blast Fireball |
| 16 | 17 | -3.18 |  | Playing the Game > Critical Hits |
| 17 | 14 | -3.72 |  | Magic Items > Hat of Many Spells |
| 18 | 20 | -3.80 |  | Spells > Circle of Death |
| 19 | 10 | -4.34 |  | Magic Items > Staff of Power |
| 20 | 19 | -9.66 |  | Rules Glossary > Hit Point Dice |


*re-ranking* (query: `Fireball spell saving throw`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 7.68 | yes | Spells > Delayed Blast Fireball |
| 2 | 2 | 7.52 | yes | Spells > Delayed Blast Fireball |
| 3 | 1 | 5.66 | yes | Spells > Fireball |
| 4 | 20 | 5.56 |  | Playing the Game > Saving Throws |
| 5 | 5 | 4.06 |  | Playing the Game > Damage against Multiple Targets |
| 6 | 15 | 4.04 |  | Spells > Saving Throws |
| 7 | 18 | 3.83 |  | Monsters A–Z > Actions |
| 8 | 14 | 3.82 |  | Spells > Targets |
| 9 | 16 | 3.77 |  | Spells > Hideous Laughter |
| 10 | 17 | 3.53 |  | Rules Glossary > Saving Throw |
| 11 | 13 | 2.60 |  | Classes > Careful Spell |
| 12 | 12 | 2.29 |  | Magic Items > Ring of Spell Turning |
| 13 | 9 | 1.78 |  | Magic Items > Necklace of Fireballs |
| 14 | 11 | 1.54 |  | Magic Items > Wand of Fireballs |
| 15 | 10 | 1.35 |  | Magic Items > Staff of Power |
| 16 | 7 | 0.71 |  | Rules Glossary > Save |
| 17 | 6 | 0.39 | yes | Spells > Delayed Blast Fireball |
| 18 | 3 | 0.34 | yes | Spells > Fireball |
| 19 | 8 | -0.50 |  | Spells > Delayed Blast Fireball |
| 20 | 19 | -7.08 |  | Spells > Scrying |

*retrieved sections:* Spells > Delayed Blast Fireball | Spells > Fireball | Spells > Earthquake | Magic Items > Staff of Power | Magic Items > Staff of the Magi | Rules Glossary > Sphere [Area of Effect] | Rules Glossary > Area of Effect

<details><summary>full retrieved context</summary>

```
[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
The spell's base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn't ended.  
If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Spells > Earthquake]
A creature within a distance from a collapsing structure equal to half the structure's height makes a Dexterity saving throw. On a failed save, the creature takes 12d6 Bludgeoning damage, has the Prone condition, and is buried in the rubble, requiring a DC 20 Strength (Athletics) check as an action to escape. On a successful save, the creature takes half as much damage only.

---

[Magic Items > Staff of Power]
creature in the area makes a DC 17 Dexterity saving throw. On a failed save, a creature takes Force damage equal to 4 times the number of charges in the staff. On a successful save, a creature takes half as much damage.

---

[Magic Items > Staff of the Magi]
creature in the area makes a DC 17 Dexterity saving throw. On a failed save, a creature takes Force damage equal to 6 times the number of charges in the staff. On a successful save, a creature takes half as much damage.

---

[Rules Glossary > Sphere [Area of Effect]]
#### Sphere [Area of Effect]  
A Sphere is an area of effect that extends in straight lines from a point of origin outward in all directions. The effect that creates a Sphere specifies the distance it extends as the radius of the Sphere.  
A Sphere's point of origin is included in the Sphere's area of effect.

---

[Rules Glossary > Area of Effect]
<td>Sphere</td>
</tr>
</tbody>
</table>  
An area of effect has a point of origin, a location from which the effect's energy erupts. The rules for each shape specify how to position its point of origin. If all straight lines extending from the point of origin to a location in the area of effect are blocked, that location isn't included in the area of effect. To block a line, an obstruction must provide Total Cover. _See also_ "Cover."

---

[Rules Glossary > Area of Effect]
#### Area of Effect  
The descriptions of many spells and other features specify that they have an area of effect, which typically has one of six shapes. These shapes are defined elsewhere in this glossary:  
<table>
<tbody>
<tr>
<td>Cone</td>
<td>Cylinder</td>
<td>Line</td>
</tr>
<tr>
<td>Cube</td>
<td>Emanation</td>
<td>Sphere</td>
</tr>
</tbody>
</table>

---

[Spells > Delayed Blast Fireball]
When the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The base damage increases by 1d6 for each spell slot level above 7.

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

## q19 (needle) What are the Owlbear's Rend attack bonus, damage and damage type, and what does the Goblin Warrior's Nimble Escape let it do?

**Gold facts (counterfactual data):** +7; 14 (2d8 + 5); Slashing; Disengage or Hide


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Owlbear's Rend:** +7 to hit, **2d8 + 4 slashing damage** (average 13). The attack is called "Claws" in the 2014 Monster Manual.

**Goblin Warrior's Nimble Escape:** As a bonus action, it can take the **Disengage** or **Hide** action. Standard goblins have this trait, but I don't recall a separate "Goblin Warrior" stat block, so this is the goblin's trait.

*facts found (judge): 3/4; missing: 14 (2d8 + 5)*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Owlbear's Rend:** +7 to hit, reach 5 ft. On a hit, it deals 14 (2d8 + 5) Slashing damage.

**Goblin Warrior's Nimble Escape:** The Context doesn't include a Goblin Warrior entry, so I can't say what its Nimble Escape allows it to do.

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

**Owlbear's Rend:** +7 to hit, reach 5 ft., dealing 14 (2d8 + 5) slashing damage on a hit.

**Goblin Warrior's Nimble Escape:** The Context doesn't include a Goblin Warrior entry, so I can't say what Nimble Escape lets it do.

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

**Owlbear's Rend:** +7 attack bonus, reach 5 ft., and 14 (2d8 + 5) Slashing damage on a hit.

**Goblin's Nimble Escape:** As a Bonus Action, it lets the goblin take the Disengage or Hide action. The Context refers only to "the goblin," not "Goblin Warrior," so I'm assuming that's the same creature.

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

**Owlbear's Rend:** +7 attack bonus (melee attack roll, reach 5 ft.), dealing 14 (2d8 + 5) slashing damage on a hit.

**Goblin Warrior's Nimble Escape:** The Context doesn't include the Goblin Warrior, so I can't say what Nimble Escape lets it do.

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

**Owlbear's Rend:** +7 to hit, 14 (2d8 + 5) Slashing damage.

**Goblin's Nimble Escape:** Lets the goblin take the Disengage or Hide action as a bonus action. The Context labels this entry "the goblin" and doesn't name a "Goblin Warrior" specifically.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Owlbear's Rend attack bonus, damage and damage type, and what does `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.98 | yes | Monsters A–Z > Actions |
| 2 | 16 | -0.82 | yes | Monsters A–Z > Bonus Actions |
| 3 | 11 | -1.17 | yes | Spells > Actions |
| 4 | 27 | -1.60 | yes | Monsters A–Z > Actions |
| 5 | 25 | -1.71 | yes | Monsters A–Z > Actions |
| 6 | 7 | -1.88 | yes | Animals > Actions |
| 7 | 22 | -1.90 | yes | Monsters A–Z > Actions |
| 8 | 2 | -1.95 | yes | Monsters A–Z > Bonus Actions |
| 9 | 4 | -2.06 |  | Monsters A–Z > Actions |
| 10 | 6 | -2.14 |  | Monsters A–Z > Actions |
| 11 | 12 | -2.20 |  | Monsters A–Z > Actions |
| 12 | 3 | -2.32 |  | Monsters A–Z > Actions |
| 13 | 15 | -2.52 |  | Monsters A–Z > Actions |
| 14 | 28 | -3.42 |  | Magic Items > Dragon Slayer |
| 15 | 8 | -3.74 |  | Animals > Bonus Actions |
| 16 | 5 | -3.96 |  | Animals > Actions |
| 17 | 9 | -4.04 |  | Animals > Bonus Actions |
| 18 | 10 | -5.13 |  | Spells > Shillelagh |
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

**Owlbear's Rend:** +7 attack bonus (reach 5 ft.), dealing 14 (2d8 + 5) slashing damage on a hit.

**Goblin's Nimble Escape:** The goblin can take the Disengage or Hide action as a bonus action. The Context lists this ability under a monster called "goblin," not "Goblin Warrior," so I can't confirm the two are the same.

*facts found (judge): 4/4; missing: none*


*re-ranking* (query: `What are the Owlbear's Rend attack bonus, damage and damage type, and what does `): candidate pool of 24, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 1.98 | yes | Monsters A–Z > Actions |
| 2 | 7 | -1.88 | yes | Animals > Actions |
| 3 | 2 | -1.95 | yes | Monsters A–Z > Bonus Actions |
| 4 | 4 | -2.06 | yes | Monsters A–Z > Actions |
| 5 | 6 | -2.14 | yes | Monsters A–Z > Actions |
| 6 | 3 | -2.32 | yes | Monsters A–Z > Actions |
| 7 | 8 | -3.74 | yes | Animals > Bonus Actions |
| 8 | 5 | -3.96 | yes | Animals > Actions |
| 9 | 9 | -4.04 |  | Animals > Bonus Actions |
| 10 | 10 | -5.13 |  | Spells > Shillelagh |
| 11 | 11 | -6.46 |  | Monsters A–Z > Owlbear |
| 12 | 12 | -7.38 |  | Monsters A–Z > Owlbear |
| 13 | 23 | -7.40 |  | Playing the Game > Half Damage |
| 14 | 15 | -7.60 |  | Monsters A–Z > Goblin Warrior |
| 15 | 13 | -7.97 |  | Monsters A–Z > Goblin Warrior |
| 16 | 24 | -8.38 |  | Spells > Guiding Bolt |
| 17 | 14 | -8.90 |  | Monsters A–Z > Goblin Warrior |
| 18 | 18 | -10.50 |  | Rules Glossary > Disengage [Action] |
| 19 | 22 | -10.80 |  | Rules Glossary > Cone [Area of Effect] |
| 20 | 17 | -10.91 |  | Animals > Lion |

*retrieved sections:* Monsters A–Z > Actions | Animals > Actions | Monsters A–Z > Bonus Actions | Animals > Bonus Actions

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

---

[Animals > Actions]
### Actions  
<hr>  
**_Multiattack._** The lion makes two Rend attacks. It can replace one attack with a use of Roar.  
**_Rend._** _Melee Attack Roll:_ +5, reach 5 ft. _Hit:_ 7 (1d8 + 3) Slashing damage.  
**_Roar._** _Wisdom Saving Throw:_ DC 11, one creature within 15 feet. _Failure:_ The target has the Frightened condition until the start of the lion's next turn.
```
</details>


### v6_agentic  (9 chunks, 3 LLM call(s))

**Owlbear's Rend:** +7 attack bonus. On a hit, it deals 14 (2d8 + 5) slashing damage.

**Goblin Warrior's Nimble Escape:** It lets the goblin take the Disengage or Hide action as a bonus action.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Owlbear monster / Goblin Warrior monster / Nimble Escape rule


*re-ranking* (query: `Owlbear monster`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 5.08 | yes | Monsters A–Z > Owlbear |
| 2 | 1 | 4.36 | yes | Monsters A–Z > Actions |
| 3 | 2 | 2.06 | yes | Monsters A–Z > Owlbear |
| 4 | 6 | -5.23 |  | Monsters A–Z > Traits |
| 5 | 7 | -7.29 |  | Rules Glossary > Monster |
| 6 | 5 | -9.01 |  | Monsters > Equipping a Monster with Other Items |
| 7 | 14 | -9.02 |  | Monsters A–Z > Ancient Black Dragon |
| 8 | 8 | -9.19 |  | Monsters A–Z > Gargoyle |
| 9 | 12 | -9.20 |  | Monsters A–Z > White Dragon Wyrmling |
| 10 | 9 | -9.36 |  | Monsters > Initiative |
| 11 | 4 | -9.40 |  | Monsters A–Z > Mummy Lord |
| 12 | 16 | -9.42 |  | Monsters A–Z > Storm Giant |
| 13 | 10 | -9.52 |  | Monsters A–Z > Salamander |
| 14 | 17 | -9.66 |  | Rules Glossary > Stat Block |
| 15 | 15 | -9.97 |  | Rules Glossary > Challenge Rating |
| 16 | 19 | -10.00 |  | Monsters A–Z > Reactions |
| 17 | 18 | -10.09 |  | Monsters A–Z > Lich |
| 18 | 13 | -10.10 |  | Gameplay Toolbox > Unusual Features |
| 19 | 11 | -10.25 |  | Monsters > Limited Usage |
| 20 | 20 | -10.56 |  | Monsters > Resistances and Vulnerabilities |


*re-ranking* (query: `Goblin Warrior monster`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.96 | yes | Monsters A–Z > Goblin Warrior |
| 2 | 2 | 5.53 | yes | Monsters A–Z > Goblin Warrior |
| 3 | 4 | 4.42 | yes | Monsters A–Z > Bugbear Warrior |
| 4 | 3 | 3.66 |  | Monsters A–Z > Goblin Warrior |
| 5 | 10 | 3.01 |  | Monsters A–Z > Bugbear Warrior |
| 6 | 13 | 2.59 |  | Monsters A–Z > Hobgoblin Warrior |
| 7 | 14 | 1.05 |  | Monsters A–Z > Reactions |
| 8 | 19 | 0.76 |  | Monsters A–Z > Actions |
| 9 | 8 | 0.00 |  | Monsters A–Z > Bugbear Stalker |
| 10 | 16 | -0.47 |  | Monsters A–Z > Hobgoblin Captain |
| 11 | 7 | -0.56 |  | Monsters A–Z > Goblin Minion |
| 12 | 5 | -0.94 | yes | Monsters A–Z > Bonus Actions |
| 13 | 6 | -1.86 |  | Monsters A–Z > Hobgoblin Warrior |
| 14 | 11 | -2.89 |  | Monsters A–Z > Warrior Infantry |
| 15 | 9 | -3.65 |  | Monsters A–Z > Traits |
| 16 | 12 | -3.78 |  | Magic Items > Deck of Illusions |
| 17 | 18 | -3.98 |  | Monsters A–Z > Reactions |
| 18 | 17 | -5.03 |  | Monsters A–Z > Bugbear Warrior |
| 19 | 20 | -8.50 |  | Classes > Monk Subclass: Warrior of the Open Hand |
| 20 | 15 | -9.14 |  | Classes > Level 10: Heroic Warrior |


*re-ranking* (query: `Nimble Escape rule`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 2.61 | yes | Monsters A–Z > Bonus Actions |
| 2 | 1 | 2.43 | yes | Animals > Bonus Actions |
| 3 | 3 | 2.38 | yes | Animals > Bonus Actions |
| 4 | 19 | -5.07 |  | Rules Glossary > Unarmed Strike |
| 5 | 9 | -7.48 |  | Monsters A–Z > Actions |
| 6 | 16 | -9.43 |  | Monsters A–Z > Traits |
| 7 | 5 | -9.52 |  | Monsters A–Z > Actions |
| 8 | 8 | -9.81 |  | Animals > Actions |
| 9 | 17 | -9.93 |  | Monsters A–Z > Actions |
| 10 | 6 | -9.97 |  | Monsters A–Z > Bonus Actions |
| 11 | 11 | -10.25 |  | Monsters A–Z > Actions |
| 12 | 4 | -10.28 |  | Animals > Actions |
| 13 | 13 | -10.38 |  | Monsters A–Z > Actions |
| 14 | 7 | -10.42 |  | Monsters A–Z > Actions |
| 15 | 20 | -10.55 |  | Monsters A–Z > Actions |
| 16 | 14 | -11.06 |  | Playing the Game > Ability Modifiers |
| 17 | 10 | -11.08 |  | Playing the Game > Ability Modifiers |
| 18 | 12 | -11.20 |  | Rules Glossary > Reach |
| 19 | 15 | -11.20 |  | Monsters A–Z > Bonus Actions |
| 20 | 18 | -11.32 |  | Rules Glossary > Magical Effect |

*retrieved sections:* Monsters A–Z > Owlbear | Monsters A–Z > Actions | Monsters A–Z > Goblin Warrior | Monsters A–Z > Bugbear Warrior | Monsters A–Z > Bonus Actions | Animals > Bonus Actions

<details><summary>full retrieved context</summary>

```
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

[Monsters A–Z > Bugbear Warrior]
**Languages** Common, Goblin<br>
**CR** 1 (XP 200; PB +2)

---

[Monsters A–Z > Bonus Actions]
#### Bonus Actions  
<hr>  
**_Nimble Escape._** The goblin takes the Disengage or Hide action.

---

[Animals > Bonus Actions]
### Bonus Actions  
<hr>  
**_Nimble Escape._** The tiger takes the Disengage or Hide action.

---

[Animals > Bonus Actions]
### Bonus Actions  
<hr>  
**_Nimble Escape._** The panther takes the Disengage or Hide action.
```
</details>


---

## q20 (needle) Which classes can cast Counterspell, and which classes can cast Revivify?

**Gold facts (counterfactual data):** Sorcerer, Warlock, Wizard; Cleric, Druid, Paladin, Ranger


### v0_closed_book  (0 chunks, 1 LLM call(s))

**Counterspell:** Sorcerer, Warlock, and Wizard.

**Revivify:** Artificer, Cleric, Paladin, and Ranger. I'm less certain about this list than the Counterspell one, so check the class spell lists in the 2024 SRD 5.2 before relying on it.

*facts found (judge): 1/2; missing: Cleric, Druid, Paladin, Ranger*


### v1_baseline  (3 chunks, 1 LLM call(s))

**Counterspell:** Sorcerer, Warlock, and Wizard.

**Revivify:** The Context doesn't include the Revivify spell, so I can't say which classes can cast it.

*facts found (judge): 1/2; missing: Cleric, Druid, Paladin, Ranger*

*retrieved sections:* Spells > Counterspell | Monsters A–Z > Reactions

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

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.
```
</details>


### v2_rerank  (3 chunks, 1 LLM call(s))

Counterspell: Sorcerer, Warlock, and Wizard.

Revivify: The Context does not include the Revivify spell, so I can't say which classes can cast it.

*facts found (judge): 1/2; missing: Cleric, Druid, Paladin, Ranger*


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 | yes | Spells > Counterspell |
| 2 | 2 | 0.14 | yes | Monsters A–Z > Reactions |
| 3 | 4 | -0.15 | yes | Monsters A–Z > Reactions |
| 4 | 7 | -1.67 |  | Classes > Level 2: Wild Shape |
| 5 | 3 | -2.71 |  | Spells > Counterspell |
| 6 | 9 | -4.46 |  | Classes > Transmuted Spell |
| 7 | 10 | -4.54 |  | Classes > Level 1: Spellcasting |
| 8 | 5 | -5.23 |  | Classes > Level 1: Spellcasting |
| 9 | 6 | -5.26 |  | Classes > Level 1: Spellcasting |
| 10 | 8 | -8.05 |  | Monsters > Spellcasting |

*retrieved sections:* Spells > Counterspell | Monsters A–Z > Reactions

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

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic._** The lich casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.

---

[Monsters A–Z > Reactions]
#### Reactions  
<hr>  
**_Protective Magic (3/Day)._** The archmage casts _Counterspell_ or _Shield_ in response to the spell's trigger, using the same spellcasting ability as Spellcasting.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

**Counterspell:** Sorcerer, Warlock, and Wizard.

**Revivify:** The Context doesn't include the Revivify spell, so I can't say which classes can cast it.

*facts found (judge): 1/2; missing: Cleric, Druid, Paladin, Ranger*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 | yes | Spells > Counterspell |
| 2 | 2 | 0.14 | yes | Monsters A–Z > Reactions |
| 3 | 4 | -0.15 | yes | Monsters A–Z > Reactions |
| 4 | 7 | -1.67 | yes | Classes > Level 2: Wild Shape |
| 5 | 3 | -2.71 | yes | Spells > Counterspell |
| 6 | 9 | -4.46 | yes | Classes > Transmuted Spell |
| 7 | 10 | -4.54 |  | Classes > Level 1: Spellcasting |
| 8 | 5 | -5.23 | yes | Classes > Level 1: Spellcasting |
| 9 | 6 | -5.26 | yes | Classes > Level 1: Spellcasting |
| 10 | 8 | -8.05 |  | Monsters > Spellcasting |

*retrieved sections:* Spells > Counterspell | Monsters A–Z > Reactions | Classes > Level 2: Wild Shape | Classes > Transmuted Spell | Classes > Level 1: Spellcasting

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

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Classes > Transmuted Spell]
#### Transmuted Spell  
_Cost: 1 Sorcery Point_  
When you cast a spell that deals a type of damage from the following list, you can spend 1 Sorcery Point to change that damage type to one of the other listed types: Acid, Cold, Fire, Lightning, Poison, Thunder.

---

[Classes > Level 1: Spellcasting]
1 and 2 in any combination, chosen from your spellbook.

---

[Classes > Level 1: Spellcasting]
six Sorcerer spells of level 1 or 2 in any combination.
```
</details>


### v3_hier_rerank  (3 chunks, 1 LLM call(s))

**Counterspell:** Sorcerer, Warlock, and Wizard.

**Revivify:** The Context doesn't include the Revivify spell or any class's spell list that mentions it, so I can't say which classes can cast it.

*facts found (judge): 1/2; missing: Cleric, Druid, Paladin, Ranger*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 | yes | Spells > Counterspell |
| 2 | 2 | -2.71 | yes | Spells > Counterspell |
| 3 | 10 | -3.73 |  | Classes > Level 1: Spellcasting |
| 4 | 8 | -4.28 | yes | Classes > Level 1: Spellcasting |
| 5 | 6 | -4.46 |  | Classes > Transmuted Spell |
| 6 | 7 | -4.54 |  | Classes > Level 1: Spellcasting |
| 7 | 9 | -5.13 |  | Classes > Level 1: Spellcasting |
| 8 | 3 | -5.23 |  | Classes > Level 1: Spellcasting |
| 9 | 4 | -5.26 |  | Classes > Level 1: Spellcasting |
| 10 | 5 | -8.05 |  | Monsters > Spellcasting |

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

Based on the Context:

- **Counterspell** is listed as castable by **Sorcerer, Warlock, and Wizard**.
- **Revivify** is listed as castable by **Cleric, Druid, Paladin, and Ranger**.

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
| 8 | 27 | -1.67 | yes | Classes > Level 2: Wild Shape |
| 9 | 5 | -1.99 |  | Classes > Level 1: Spellcasting |
| 10 | 11 | -2.11 |  | Classes > Mask of Many Faces |
| 11 | 2 | -2.71 |  | Spells > Counterspell |
| 12 | 9 | -3.60 |  | Classes > Armor of Shadows |
| 13 | 23 | -3.73 |  | Classes > Level 1: Spellcasting |
| 14 | 15 | -4.04 |  | Rules Glossary > Dead |
| 15 | 10 | -4.16 |  | Classes > Level 1: Spellcasting |
| 16 | 6 | -4.28 |  | Classes > Level 1: Spellcasting |
| 17 | 25 | -4.33 |  | Classes > Level 1: Spellcasting |
| 18 | 17 | -4.46 |  | Classes > Transmuted Spell |
| 19 | 19 | -4.54 |  | Classes > Level 1: Spellcasting |
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

**Counterspell** can be cast by Sorcerer, Warlock, and Wizard.

**Revivify** can be cast by Cleric, Druid, Paladin, and Ranger.

*facts found (judge): 2/2; missing: none*

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Which classes can cast Counterspell, and which classes can cast Revivify?`): candidate pool of 16, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 0.84 | yes | Spells > Counterspell |
| 2 | 4 | 0.75 | yes | Classes > Level 3 Paladin Spells |
| 3 | 3 | -0.97 | yes | Spells > Revivify |
| 4 | 8 | -1.18 | yes | Classes > Master of Myriad Forms |
| 5 | 5 | -1.99 | yes | Classes > Level 1: Spellcasting |
| 6 | 2 | -2.71 | yes | Spells > Counterspell |
| 7 | 9 | -3.60 |  | Classes > Armor of Shadows |
| 8 | 10 | -4.16 | yes | Classes > Level 1: Spellcasting |
| 9 | 6 | -4.28 |  | Classes > Level 1: Spellcasting |
| 10 | 7 | -4.66 |  | Classes > Level 1: Spellcasting |
| 11 | 16 | -9.31 |  | Classes > Sorcerer Spell List |
| 12 | 12 | -9.95 |  | Classes > Paladin |
| 13 | 15 | -10.20 |  | Classes > Ranger |
| 14 | 14 | -10.50 |  | Classes > Ranger |
| 15 | 13 | -10.55 |  | Classes > Paladin |
| 16 | 11 | -11.31 |  | Rules Glossary > Reaction |

*retrieved sections:* Spells > Counterspell | Classes > Level 3 Paladin Spells | Spells > Revivify | Classes > Master of Myriad Forms | Classes > Level 1: Spellcasting | Classes > Mask of Many Faces

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

[Classes > Mask of Many Faces]
#### Mask of Many Faces  
_Prerequisite: Level 2+ Warlock_  
You can cast _Disguise Self_ without expending a spell slot.

---

[Spells > Counterspell]
**Components:** S
**Duration:** Instantaneous  
You attempt to interrupt a creature in the process of casting a spell. The creature makes a Wisdom saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted. If that spell was cast with a spell slot, the slot isn't expended.

---

[Classes > Level 1: Spellcasting]
#### Level 1: Spellcasting  
You have learned to cast spells through studying the mystical forces of nature. See "Spells" for the rules on spellcasting. The information below details how you use those rules with Druid spells, which appear on the Druid spell list later in the class's description.  
_Cantrips._ You know two cantrips of your choice from the Druid spell list. _Druidcraft_ and _Produce Flame_ are recommended.
```
</details>


### v6_agentic  (6 chunks, 3 LLM call(s))

**Counterspell** can be cast by Sorcerers, Warlocks, and Wizards.

**Revivify** can be cast by Clerics, Druids, Paladins, and Rangers.

*facts found (judge): 2/2; missing: none*

*agentic sub-queries:* Counterspell spell class / Revivify spell class


*re-ranking* (query: `Counterspell spell class`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.39 | yes | Spells > Counterspell |
| 2 | 2 | 2.11 | yes | Spells > Counterspell |
| 3 | 6 | 1.18 | yes | Classes > Level 3 Warlock Spells |
| 4 | 10 | -0.12 |  | Monsters A–Z > Reactions |
| 5 | 8 | -0.25 |  | Monsters A–Z > Reactions |
| 6 | 3 | -1.02 |  | Spells > Class Spell Lists |
| 7 | 11 | -2.71 |  | Classes > Level 1: Spellcasting |
| 8 | 9 | -2.92 |  | Classes > Level 1: Spellcasting |
| 9 | 14 | -2.92 |  | Classes > Level 5: Memorize Spell |
| 10 | 5 | -3.04 |  | Spells > Preparing Spells |
| 11 | 13 | -3.71 |  | Classes > Sorcerer Class Features |
| 12 | 18 | -3.99 |  | Classes > Wizard Class Features |
| 13 | 16 | -4.09 |  | Classes > Level 4 Sorcerer Spells |
| 14 | 15 | -4.49 |  | Classes > Cleric Class Features |
| 15 | 4 | -4.61 |  | Classes > Level 3 Wizard Spells |
| 16 | 19 | -4.94 |  | Classes > Level 1 Warlock Spells |
| 17 | 12 | -5.07 |  | Classes > Level 6 Wizard Spells |
| 18 | 20 | -5.08 |  | Classes > Bard Class Features |
| 19 | 7 | -5.09 |  | Equipment > Spell Scroll (Cantrip, 30 GP; Level 1, 50 GP) |
| 20 | 17 | -5.56 |  | Classes > Paladin Class Features |


*re-ranking* (query: `Revivify spell class`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 4.98 | yes | Classes > Level 3 Paladin Spells |
| 2 | 2 | 3.78 | yes | Classes > Level 3: Life Domain Spells |
| 3 | 4 | 3.66 | yes | Spells > Revivify |
| 4 | 3 | -1.10 |  | Spells > Class Spell Lists |
| 5 | 6 | -1.21 |  | Classes > Level 3: Evocation Savant |
| 6 | 11 | -1.40 |  | Rules Glossary > Dead |
| 7 | 10 | -1.67 |  | Classes > Level 18: Spell Mastery |
| 8 | 9 | -1.77 |  | Classes > Level 5: Memorize Spell |
| 9 | 8 | -2.47 |  | Classes > Level 1: Spellcasting |
| 10 | 5 | -2.78 |  | Spells > Preparing Spells |
| 11 | 12 | -2.89 |  | Classes > Level 7 Cleric Spells |
| 12 | 14 | -3.71 |  | Classes > Sorcerer Class Features |
| 13 | 15 | -4.17 |  | Classes > Level 3: Wizard Subclass |
| 14 | 7 | -4.40 |  | Classes > Level 3 Paladin Spells |
| 15 | 13 | -4.42 |  | Classes > Level 7 Sorcerer Spells |
| 16 | 16 | -4.54 |  | Classes > Cleric Class Features |
| 17 | 20 | -5.14 |  | Classes > Level 1 Warlock Spells |
| 18 | 17 | -5.33 |  | Classes > Level 6 Wizard Spells |
| 19 | 19 | -6.11 |  | Classes > Bard Class Features |
| 20 | 18 | -6.23 |  | Classes > Paladin Class Features |

*retrieved sections:* Spells > Counterspell | Classes > Level 3 Warlock Spells | Classes > Level 3 Paladin Spells | Classes > Level 3: Life Domain Spells | Spells > Revivify

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

[Classes > Level 3 Warlock Spells]
#### Level 3 Warlock Spells  
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
<td>Counterspell</td>
<td>Abjuration</td>
<td>—</td>
</tr>
<tr>
<td>Dispel Magic</td>
<td>Abjuration</td>
<td>—</td>
</tr>
<tr>
<td>Fear</td>
<td>Illusion</td>
<td>C</td>
</tr>
<tr>
<td>Fly</td>
<td>Transmutation</td>
<td>C</td>
</tr>
<tr>
<td>Gaseous Form</td>
<td>Transmutation</td>
<td>C</td>
</tr>
<tr>
<td>Hypnotic Pattern</td>
<td>Illusion</td>
<td>C</td>
</tr>
<tr>

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


---

## q21 (multi-topic) Answer all three: (1) What is the minimum length of a Long Rest? (2) How many pounds can a Bag of Holding hold? (3) What damage does Fireball deal?

**Gold facts (counterfactual data):** at least 10 hours; 800 pounds; 9d6


### v0_closed_book  (0 chunks, 1 LLM call(s))

1. **Long Rest:** At least **8 hours**. You can spend up to 2 of those hours on light activity, such as reading, talking, or keeping watch, and you must sleep for at least 6 of them.

2. **Bag of Holding:** It holds up to **500 pounds**, not exceeding **64 cubic feet**.

3. **Fireball:** It deals **8d6 fire damage** to each creature in a 20-foot-radius sphere. Targets make a Dexterity saving throw and take half damage on a success.

*facts found (judge): 0/3; missing: at least 10 hours; 800 pounds; 9d6*


### v1_baseline  (3 chunks, 1 LLM call(s))

(1) The Context does not say what the minimum length of a Long Rest is.

(2) The Context does not say how many pounds a Bag of Holding can hold. It contains no entry for that item.

(3) Fireball's damage is not stated in the Context. It says only that the damage increases by 1d6 for each spell slot level above 3, which implies a base damage amount that the Context omits.

*facts found (judge): 0/3; missing: at least 10 hours; 800 pounds; 9d6*

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

1. **Long Rest minimum length:** The Context doesn't say. It doesn't define Long Rest at all.
2. **Bag of Holding capacity:** It holds up to 800 pounds, not exceeding 96 cubic feet.
3. **Fireball damage:** The Context doesn't say. It doesn't mention Fireball.

*facts found (judge): 1/3; missing: at least 10 hours; 9d6*


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

1. **Long Rest minimum length:** The Context doesn't say how long a Long Rest lasts, so I can't answer this.
2. **Bag of Holding:** It can hold up to 800 pounds, not exceeding a volume of 96 cubic feet.
3. **Fireball damage:** The Context doesn't state Fireball's base damage. It says the damage increases by 1d6 for each spell slot level above 3 when a higher-level slot is used.

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

1. **Minimum length of a Long Rest:** The Context doesn't say. It contains no information about Long Rests.
2. **Bag of Holding capacity:** It can hold up to 800 pounds, not exceeding a volume of 96 cubic feet.
3. **Fireball damage:** The Context doesn't say. It contains no information about Fireball.

*facts found (judge): 1/3; missing: at least 10 hours; 9d6*


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

1. **Minimum length of a Long Rest:** The Context doesn't state a minimum duration. It only says you must have at least 1 Hit Point to start one, and that a Long Rest is interrupted by 1 hour of walking or other physical exertion.

2. **Bag of Holding:** It can hold up to 800 pounds, not exceeding a volume of 96 cubic feet.

3. **Fireball damage:** The Context doesn't mention Fireball, so I can't answer this.

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

1. **Minimum length of a Long Rest:** The Context doesn't state this. It gives only the start requirement (at least 1 Hit Point) and says a Long Rest is interrupted by certain events, including 1 hour of walking or other physical exertion. It never gives a required duration.
2. **Bag of Holding capacity:** It can hold up to 800 pounds, not exceeding a volume of 96 cubic feet.
3. **Fireball damage:** The Context doesn't mention Fireball, so I can't answer this.

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


### v6_agentic  (10 chunks, 3 LLM call(s))

(1) A Long Rest lasts at least 10 hours.

(2) A Bag of Holding can hold up to 800 pounds, not exceeding a volume of 96 cubic feet.

(3) The Context doesn't say what damage Fireball deals. The Fireball excerpt covers only that flammable objects start burning and that the damage increases by 1d6 for each spell slot level above 3. The base damage amount is missing.

*facts found (judge): 2/3; missing: 9d6*

*agentic sub-queries:* Long Rest rule / Bag of Holding / Fireball spell


*re-ranking* (query: `Long Rest rule`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 8.50 | yes | Rules Glossary > Long Rest |
| 2 | 5 | 7.20 | yes | Rules Glossary > Long Rest |
| 3 | 4 | 6.68 | yes | Rules Glossary > Long Rest |
| 4 | 3 | 6.45 |  | Rules Glossary > Long Rest |
| 5 | 9 | 4.69 |  | Rules Glossary > Exhaustion [Condition] |
| 6 | 1 | 4.23 |  | Rules Glossary > Per Day |
| 7 | 18 | 3.79 |  | Rules Glossary > Short Rest |
| 8 | 6 | 2.60 |  | Playing the Game > Hit Points |
| 9 | 8 | 2.21 |  | Spells > Spell Slots |
| 10 | 19 | 1.69 |  | Rules Glossary > Short Rest |
| 11 | 11 | 1.63 |  | Spells > Augury |
| 12 | 7 | 1.40 |  | Playing the Game > Duration |
| 13 | 10 | 1.11 |  | Spells > Divination |
| 14 | 20 | -0.10 |  | Spells > Preparing Spells |
| 15 | 15 | -1.16 |  | Character Origins > Elf |
| 16 | 14 | -1.68 |  | Spells > Resurrection |
| 17 | 12 | -1.91 |  | Rules Glossary > Long Jump |
| 18 | 16 | -3.77 |  | Character Origins > Orc |
| 19 | 13 | -3.93 |  | Spells > Prayer of Healing |
| 20 | 17 | -11.15 |  | Rules Glossary > Reach |


*re-ranking* (query: `Bag of Holding`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 7.75 | yes | Magic Items > Bag of Holding |
| 2 | 3 | 7.65 | yes | Magic Items > Bag of Holding |
| 3 | 5 | 6.09 | yes | Magic Items > Bag of Holding |
| 4 | 2 | 5.31 |  | Magic Items > Bag of Devouring |
| 5 | 8 | 3.85 |  | Magic Items > Bag of Devouring |
| 6 | 18 | 1.75 |  | Monsters A–Z > Traits |
| 7 | 13 | -0.65 |  | Magic Items > Magic Item Categories |
| 8 | 10 | -1.47 |  | Magic Items > Bag of Devouring |
| 9 | 12 | -1.48 |  | Magic Items > Bag of Tricks |
| 10 | 4 | -1.70 |  | Magic Items > Bag of Devouring |
| 11 | 7 | -1.84 |  | Magic Items > Bag of Tricks |
| 12 | 6 | -2.05 |  | Magic Items > Bag of Tricks |
| 13 | 11 | -3.48 |  | Magic Items > Bag of Beans |
| 14 | 16 | -3.97 |  | Magic Items > Bag of Tricks |
| 15 | 14 | -3.98 |  | Magic Items > Bag of Tricks |
| 16 | 9 | -4.34 |  | Magic Items > Bag of Beans |
| 17 | 15 | -4.40 |  | Magic Items > Bag of Beans |
| 18 | 19 | -4.71 |  | Magic Items > Handy Haversack |
| 19 | 17 | -5.40 |  | Magic Items > Bag of Beans |
| 20 | 20 | -10.20 |  | Playing the Game > Carrying Objects |


*re-ranking* (query: `Fireball spell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 6.65 | yes | Spells > Delayed Blast Fireball |
| 2 | 8 | 6.39 | yes | Spells > Delayed Blast Fireball |
| 3 | 1 | 6.11 | yes | Spells > Fireball |
| 4 | 2 | 6.10 | yes | Spells > Delayed Blast Fireball |
| 5 | 3 | 5.76 |  | Spells > Fireball |
| 6 | 7 | 5.41 |  | Magic Items > Wand of Fireballs |
| 7 | 19 | 5.12 |  | Monsters A–Z > Actions |
| 8 | 4 | 4.75 |  | Spells > Delayed Blast Fireball |
| 9 | 15 | 3.82 |  | Magic Items > Helm of Brilliance |
| 10 | 9 | 3.68 |  | Magic Items > Hat of Many Spells |
| 11 | 12 | 2.79 |  | Classes > Level 7 Sorcerer Spells |
| 12 | 5 | 2.67 |  | Magic Items > Staff of Power |
| 13 | 10 | 2.51 |  | Classes > Level 7 Wizard Spells |
| 14 | 14 | 2.12 |  | Classes > Level 3 Sorcerer Spells |
| 15 | 20 | 2.01 |  | Spells > Flaming Sphere |
| 16 | 13 | 1.87 |  | Classes > Level 3 Wizard Spells |
| 17 | 11 | 1.29 |  | Magic Items > Necklace of Fireballs |
| 18 | 18 | -1.81 |  | Magic Items > Staff of the Magi |
| 19 | 17 | -2.50 |  | Magic Items > Staff of Fire |
| 20 | 16 | -6.24 |  | Rules Glossary > Spell |


*re-ranking* (query: `Fireball spell base damage dice`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | 6.56 | yes | Spells > Delayed Blast Fireball |
| 2 | 1 | 4.80 | yes | Spells > Delayed Blast Fireball |
| 3 | 2 | 2.58 | yes | Spells > Fireball |
| 4 | 7 | 2.18 | yes | Spells > Delayed Blast Fireball |
| 5 | 4 | 2.07 |  | Playing the Game > Damage against Multiple Targets |
| 6 | 16 | 1.89 |  | Spells > Flame Strike |
| 7 | 6 | 1.31 |  | Spells > Fireball |
| 8 | 5 | 0.98 |  | Playing the Game > Damage Rolls |
| 9 | 9 | 0.90 |  | Playing the Game > Damage Rolls |
| 10 | 18 | 0.90 |  | Spells > Wall of Fire |
| 11 | 8 | -1.70 |  | Monsters A–Z > Actions |
| 12 | 13 | -1.72 |  | Magic Items > Necklace of Fireballs |
| 13 | 15 | -3.00 |  | Spells > Burning Hands |
| 14 | 11 | -3.08 |  | Magic Items > Wand of Fireballs |
| 15 | 12 | -3.16 |  | Spells > Delayed Blast Fireball |
| 16 | 17 | -3.18 |  | Playing the Game > Critical Hits |
| 17 | 14 | -3.72 |  | Magic Items > Hat of Many Spells |
| 18 | 20 | -3.80 |  | Spells > Circle of Death |
| 19 | 10 | -4.34 |  | Magic Items > Staff of Power |
| 20 | 19 | -9.66 |  | Rules Glossary > Hit Point Dice |

*retrieved sections:* Rules Glossary > Long Rest | Magic Items > Bag of Holding | Spells > Delayed Blast Fireball | Spells > Fireball

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
_Benefits of the Rest._ To start a Long Rest, you must have at least 1 Hit Point. When you finish the rest, you gain the following benefits:  
**Regain All HP.** You regain all lost Hit Points and all spent Hit Point Dice. If your Hit Point maximum was reduced, it returns to normal.  
**Ability Scores Restored.** If any of your ability scores were reduced, they return to normal.  
**Exhaustion Reduced.** If you have the Exhaustion condition, its level decreases by 1.

---

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

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
The spell's base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn't ended.  
If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Spells > Delayed Blast Fireball]
When the bead explodes, flammable objects in the explosion that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The base damage increases by 1d6 for each spell slot level above 7.
```
</details>


---

## q22 (multi-topic) Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skills does the Soldier background give? (3) What is the Owlbear's AC?

**Gold facts (counterfactual data):** DC 10; Athletics and Perception; AC 15


### v0_closed_book  (0 chunks, 1 LLM call(s))

**(1)** A dying creature is stabilized by a **DC 10 Wisdom (Medicine) check**, made as an action.

**(2)** The Soldier background grants proficiency in **Athletics and Intimidation**.

**(3)** The Owlbear has an AC of **13** (natural armor).

*facts found (judge): 1/3; missing: Athletics and Perception; AC 15*


### v1_baseline  (3 chunks, 1 LLM call(s))

(1) The Context doesn't say what DC check stabilizes a dying creature.

(2) The Context doesn't include the Soldier background, so it doesn't list its skills.

(3) The Context doesn't include an Owlbear. It has only partial stat blocks for the Giant Owl and Swarm of Ravens, with no AC for either.

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

1. **Stabilizing a dying creature:** The Context doesn't include a DC for this check.
2. **Soldier background skills:** Athletics and Perception.
3. **Owlbear's AC:** The Context doesn't include an Owlbear entry, so its AC isn't given.

*facts found (judge): 1/3; missing: DC 10; AC 15*

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

*retrieved sections:* Animals > Actions | Character Origins > Soldier | Monsters A–Z > Shadow

<details><summary>full retrieved context</summary>

```
[Animals > Actions]
### Actions  
<hr>  
**_Beaks._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.  
**_Cacophony (Recharge 6)._** _Wisdom Saving Throw:_ DC 10, one creature in the swarm's space. _Failure:_ The target has the Deafened condition until the start of the swarm's next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

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
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

1. **DC for stabilizing a dying creature:** The Context doesn't include this. It has no rules on dying creatures or death saving throws.
2. **Soldier skill proficiencies:** Athletics and Perception.
3. **Owlbear's AC:** The Context has no Owlbear entry, so its AC isn't available.

*facts found (judge): 1/3; missing: DC 10; AC 15*

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

*retrieved sections:* Animals > Actions | Character Origins > Soldier | Monsters A–Z > Shadow | Monsters A–Z > Death Dog | Classes > Ranger | Animals > Swarm of Ravens | Animals > Giant Vulture | Animals > Vulture

<details><summary>full retrieved context</summary>

```
[Animals > Actions]
### Actions  
<hr>  
**_Beaks._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.  
**_Cacophony (Recharge 6)._** _Wisdom Saving Throw:_ DC 10, one creature in the swarm's space. _Failure:_ The target has the Deafened condition until the start of the swarm's next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

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

(1) The Context does not say what DC check stabilizes a dying creature. It contains no rules on dying or stabilizing.

(2) The Soldier background gives Athletics and Perception skill proficiencies.

(3) The Context does not include an Owlbear. It has entries only for the Animal swarm (Beaks, Cacophony), the Soldier background, and the Shadow monster, so the Owlbear's AC is not given.

*facts found (judge): 1/3; missing: DC 10; AC 15*

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

*retrieved sections:* Animals > Actions | Character Origins > Soldier | Monsters A–Z > Shadow

<details><summary>full retrieved context</summary>

```
[Animals > Actions]
### Actions  
<hr>  
**_Beaks._** _Melee Attack Roll:_ +4, reach 5 ft. _Hit:_ 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.  
**_Cacophony (Recharge 6)._** _Wisdom Saving Throw:_ DC 10, one creature in the swarm's space. _Failure:_ The target has the Deafened condition until the start of the swarm's next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

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
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

1. **Dying creature DC:** The Context doesn't say. It doesn't mention dying creatures, stabilizing, or death saving throws.
2. **Soldier skills:** The Context doesn't say. It states only that a background grants proficiency in two skills and one tool, and that the Soldier background affects Strength, Dexterity, and Constitution. It doesn't list the skills.
3. **Owlbear's AC:** The Context doesn't say. It doesn't include the Owlbear's stat block.

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

1. **Stabilizing DC:** The Context doesn't say what DC check stabilizes a dying creature, so I can't answer this part.
2. **Soldier skills:** Athletics and Perception.
3. **Owlbear AC:** 15.

*facts found (judge): 2/3; missing: DC 10*

*note:* Replayed retrieval differs from the stored context by 0 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `Answer all three: (1) What DC check stabilizes a dying creature? (2) Which skill`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | -7.52 | yes | Character Creation > Choose a Background |
| 2 | 7 | -8.14 | yes | Character Origins > Ability Scores |
| 3 | 11 | -8.80 | yes | Character Origins > Soldier |
| 4 | 10 | -9.69 |  | Monsters A–Z > Shadow |
| 5 | 6 | -9.84 | yes | Classes > Ranger |
| 6 | 1 | -9.98 | yes | Monsters A–Z > Owlbear |
| 7 | 9 | -9.99 | yes | Character Creation > Create Your Character |
| 8 | 4 | -10.05 | yes | Animals > Swarm of Ravens |
| 9 | 12 | -10.42 | yes | Monsters A–Z > Owlbear |
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

*retrieved sections:* Character Creation > Choose a Background | Character Origins > Ability Scores | Character Origins > Soldier | Classes > Ranger | Monsters A–Z > Owlbear | Character Creation > Create Your Character | Animals > Swarm of Ravens

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
```
</details>


### v6_agentic  (9 chunks, 3 LLM call(s))

(1) A DC 10 Wisdom (Medicine) check, made as the Help action, stabilizes a creature with 0 Hit Points.

(2) The Soldier background gives the Athletics and Perception skill proficiencies.

(3) The Owlbear's AC is 15.

*facts found (judge): 3/3; missing: none*

*agentic sub-queries:* dying creature stabilize DC check / Soldier background skills / Owlbear monster AC

*note:* Replayed retrieval differs from the stored context by 1 chunk(s) at the selection boundary (approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; dense/BM25 stages show the replay.


*re-ranking* (query: `dying creature stabilize DC check`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 6.44 | yes | Playing the Game > Stabilizing a Character |
| 2 | 4 | 2.66 | yes | Magic Items > Iron Bands |
| 3 | 19 | 2.37 | yes | Equipment > Hunting Trap (5 GP) |
| 4 | 20 | 1.99 |  | Magic Items > Dimensional Shackles |
| 5 | 6 | 1.58 |  | Magic Items > Bag of Devouring |
| 6 | 17 | 1.34 |  | Equipment > Chain (5 GP) |
| 7 | 15 | 1.07 |  | Playing the Game > Healing |
| 8 | 5 | 1.02 |  | Gameplay Toolbox > Harvesting Poison |
| 9 | 8 | 0.94 |  | Magic Items > Sphere of Annihilation |
| 10 | 7 | 0.47 |  | Gameplay Toolbox > Collapsing Roof |
| 11 | 2 | 0.44 |  | Gameplay Toolbox > Poisoned Needle |
| 12 | 9 | 0.25 |  | Monsters A–Z > Actions |
| 13 | 10 | 0.17 |  | Rules Glossary > Knocking Out a Creature |
| 14 | 3 | -0.65 |  | Spells > Spare the Dying |
| 15 | 14 | -1.24 |  | Gameplay Toolbox > Crawler Mucus (200 GP) |
| 16 | 13 | -1.77 |  | Rules Glossary > Stable |
| 17 | 12 | -2.07 |  | Equipment > Healer's Kit (5 GP) |
| 18 | 11 | -2.67 |  | Monsters A–Z > Actions |
| 19 | 18 | -5.56 |  | Monsters A–Z > Actions |
| 20 | 16 | -7.30 |  | Spells > Raise Dead |


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


*re-ranking* (query: `Owlbear monster AC`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.33 | yes | Monsters A–Z > Owlbear |
| 2 | 3 | 2.37 | yes | Monsters A–Z > Actions |
| 3 | 6 | -0.39 |  | Animals > Owl |
| 4 | 5 | -1.57 |  | Monsters > Armor Class |
| 5 | 2 | -2.79 |  | Animals > Giant Owl |
| 6 | 7 | -3.07 |  | Playing the Game > Armor Class |
| 7 | 9 | -5.76 |  | Monsters A–Z > Rust Monster |
| 8 | 18 | -6.01 |  | Monsters A–Z > Succubus |
| 9 | 10 | -6.28 |  | Monsters A–Z > Axe Beak |
| 10 | 13 | -6.32 |  | Rules Glossary > Stat Block |
| 11 | 12 | -6.71 |  | Monsters A–Z > Gargoyle |
| 12 | 16 | -8.68 |  | Monsters A–Z > Planetar |
| 13 | 14 | -8.85 |  | Animals > Giant Owl |
| 14 | 15 | -9.37 |  | Rules Glossary > Monster |
| 15 | 8 | -9.55 |  | Monsters A–Z > Storm Giant |
| 16 | 17 | -9.74 |  | Monsters > Initiative |
| 17 | 11 | -10.03 |  | Monsters > Equipping a Monster with Other Items |
| 18 | 4 | -10.15 |  | Monsters A–Z > Lich |
| 19 | 20 | -10.21 |  | Monsters A–Z > Oni |
| 20 | 19 | -10.63 |  | Monsters > Limited Usage |

*retrieved sections:* Playing the Game > Stabilizing a Character | Magic Items > Iron Bands | Equipment > Hunting Trap (5 GP) | Character Origins > Soldier | Character Creation > Choose a Background | Monsters A–Z > Owlbear | Monsters A–Z > Actions

<details><summary>full retrieved context</summary>

```
[Playing the Game > Stabilizing a Character]
#### Stabilizing a Character  
You can take the Help action to try to stabilize a creature with 0 Hit Points, which requires a successful DC 10 Wisdom (Medicine) check.  
A Stable creature doesn't make Death Saving Throws even though it has 0 Hit Points, but it still has the Unconscious condition. If the creature takes damage, it stops being Stable and starts making Death Saving Throws again. A Stable creature that isn't healed regains 1 Hit Point after 1d4 hours.

---

[Magic Items > Iron Bands]
A creature that can touch the bands, including the one Restrained, can take an action to make a DC 20 Strength (Athletics) check to break the iron bands. On a successful check, the item is destroyed, and the Restrained creature is freed. On a failed check, any further attempts made by that creature automatically fail until 24 hours have elapsed.  
Once the bands are used, they can't be used again until the next dawn.

---

[Equipment > Hunting Trap (5 GP)]
make a DC 13 Strength (Athletics) check, freeing itself or another creature within its reach on a success. Each failed check deals 1 Piercing damage to the trapped creature.

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
```
</details>


---

## q23 (multi-topic) Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add to Initiative? (3) What saving throw does Topple force? (4) What is the point-buy budget?

**Gold facts (counterfactual data):** AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points


### v0_closed_book  (0 chunks, 1 LLM call(s))

1. **Dire Wolf AC:** 14 (natural armor).
2. **Alert feat:** In the 2024 rules, Alert gives Initiative Proficiency: you add your Proficiency Bonus to your Initiative rolls. (The 2014 version gave +5 to Initiative.)
3. **Topple:** The target must make a **Constitution** saving throw. On a failure, it falls Prone.
4. **Point-buy budget:** 27 points.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*


### v1_baseline  (3 chunks, 1 LLM call(s))

1. **Dire Wolf's AC:** The Context doesn't say. It mentions a wolf's Pack Tactics but gives no Armor Class for a Dire Wolf.
2. **Alert feat's Initiative bonus:** The Context doesn't mention the Alert feat.
3. **Topple's saving throw:** The Context doesn't mention Topple.
4. **Point-buy budget:** The Context doesn't mention point-buy.

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

The Context doesn't contain the answer to any of the four parts:

1. **Dire Wolf AC:** The Context has no Dire Wolf stat block. It only includes a wolf's Pack Tactics trait, not its AC.
2. **Alert feat and Initiative:** The Context doesn't mention the Alert feat.
3. **Topple saving throw:** The Context doesn't mention Topple.
4. **Point-buy budget:** The Context doesn't mention point-buy.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 2 | 8 | -8.81 | yes | Monsters A–Z > Succubus |
| 3 | 2 | -9.65 | yes | Animals > Traits |
| 4 | 9 | -9.68 |  | Monsters A–Z > Traits |
| 5 | 4 | -10.73 |  | Monsters A–Z > Actions |
| 6 | 5 | -10.76 |  | Animals > Actions |
| 7 | 7 | -10.79 |  | Monsters A–Z > Bonus Actions |
| 8 | 3 | -10.93 |  | Monsters A–Z > Actions |
| 9 | 6 | -10.93 |  | Monsters A–Z > Bonus Actions |
| 10 | 10 | -11.17 |  | Animals > Traits |

*retrieved sections:* Rules Glossary > Stat Block | Monsters A–Z > Succubus | Animals > Traits

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Monsters A–Z > Succubus]
**Languages** Abyssal, Common, Infernal; telepathy 60 ft.<br>
**CR** 4 (XP 1,100; PB +2)  
**Initiative** +3 (13)

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v2b_rerank8  (8 chunks, 1 LLM call(s))

The Context doesn't answer any of the four questions:

1. **Dire Wolf's AC:** The Context has no Dire Wolf stat block. It includes a wolf (Pack Tactics) but no AC for it.
2. **Alert feat's Initiative bonus:** The Context has no information about feats.
3. **Topple's saving throw:** The Context doesn't mention Topple.
4. **Point-buy budget:** The Context doesn't mention point-buy or character creation.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 2 | 8 | -8.81 | yes | Monsters A–Z > Succubus |
| 3 | 2 | -9.65 | yes | Animals > Traits |
| 4 | 9 | -9.68 | yes | Monsters A–Z > Traits |
| 5 | 4 | -10.73 | yes | Monsters A–Z > Actions |
| 6 | 5 | -10.76 | yes | Animals > Actions |
| 7 | 7 | -10.79 | yes | Monsters A–Z > Bonus Actions |
| 8 | 3 | -10.93 | yes | Monsters A–Z > Actions |
| 9 | 6 | -10.93 |  | Monsters A–Z > Bonus Actions |
| 10 | 10 | -11.17 |  | Animals > Traits |

*retrieved sections:* Rules Glossary > Stat Block | Monsters A–Z > Succubus | Animals > Traits | Monsters A–Z > Traits | Monsters A–Z > Actions | Animals > Actions | Monsters A–Z > Bonus Actions

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Monsters A–Z > Succubus]
**Languages** Abyssal, Common, Infernal; telepathy 60 ft.<br>
**CR** 4 (XP 1,100; PB +2)  
**Initiative** +3 (13)

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

None of the four answers appear in the Context:

1. **Dire Wolf's AC:** The Context has only the Wolf's Pack Tactics trait, not a Dire Wolf stat block or any AC value.
2. **Alert feat's Initiative bonus:** The Context does not describe the Alert feat.
3. **Topple's saving throw:** The Context does not describe the Topple mastery property.
4. **Point-buy budget:** The Context does not describe point-buy rules.

*facts found (judge): 0/4; missing: AC 16; twice your Proficiency Bonus; Strength saving throw; 30 points*


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 10, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 2 | 8 | -8.81 | yes | Monsters A–Z > Succubus |
| 3 | 2 | -9.65 | yes | Animals > Traits |
| 4 | 9 | -9.68 |  | Monsters A–Z > Traits |
| 5 | 4 | -10.73 |  | Monsters A–Z > Actions |
| 6 | 5 | -10.76 |  | Animals > Actions |
| 7 | 7 | -10.79 |  | Monsters A–Z > Bonus Actions |
| 8 | 3 | -10.93 |  | Monsters A–Z > Actions |
| 9 | 6 | -10.93 |  | Monsters A–Z > Bonus Actions |
| 10 | 10 | -11.17 |  | Animals > Traits |

*retrieved sections:* Rules Glossary > Stat Block | Monsters A–Z > Succubus | Animals > Traits

<details><summary>full retrieved context</summary>

```
[Rules Glossary > Stat Block]
_AC, Initiative, and HP._ These entries give the monster's Armor Class, Initiative, and Hit Points, which are detailed in "Playing the Game." In parentheses after the Hit Points, the monster's Hit Point Dice are provided, along with the contribution of its Constitution, if any, to its Hit Points. Following the Initiative modifier is an Initiative score. Some creatures that are created by magic lack Hit Dice and Initiative information.

---

[Monsters A–Z > Succubus]
**Languages** Abyssal, Common, Infernal; telepathy 60 ft.<br>
**CR** 4 (XP 1,100; PB +2)  
**Initiative** +3 (13)

---

[Animals > Traits]
### Traits  
<hr>  
**_Pack Tactics._** The wolf has Advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition.
```
</details>


### v4_hybrid  (8 chunks, 1 LLM call(s))

1. **Dire Wolf AC:** 16.
2. **Alert feat:** When you roll Initiative, you can add twice your Proficiency Bonus to the roll.
3. **Topple:** The Context doesn't include the Topple mastery or feat, so I can't say what saving throw it forces.
4. **Point-buy budget:** The Context doesn't include point-buy rules, so I can't give the budget.

*facts found (judge): 2/4; missing: Strength saving throw; 30 points*


*re-ranking* (query: `Answer all four: (1) What is a Dire Wolf's AC? (2) What does the Alert feat add `): candidate pool of 30, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 5 | -2.93 | yes | Animals > Dire Wolf |
| 2 | 3 | -6.09 | yes | Feats > Alert |
| 3 | 2 | -6.88 | yes | Animals > Dire Wolf |
| 4 | 1 | -7.67 | yes | Rules Glossary > Stat Block |
| 5 | 27 | -8.62 | yes | Spells > Find Steed |
| 6 | 16 | -8.81 | yes | Monsters A–Z > Succubus |
| 7 | 4 | -9.65 | yes | Animals > Traits |
| 8 | 18 | -9.68 | yes | Monsters A–Z > Traits |
| 9 | 19 | -9.94 |  | Character Origins > Criminal |
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

*retrieved sections:* Animals > Dire Wolf | Feats > Alert | Rules Glossary > Stat Block | Spells > Find Steed | Monsters A–Z > Succubus | Animals > Traits | Monsters A–Z > Traits

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

[Monsters A–Z > Succubus]
**Languages** Abyssal, Common, Infernal; telepathy 60 ft.<br>
**CR** 4 (XP 1,100; PB +2)  
**Initiative** +3 (13)

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


### v5_graph  (8 chunks, 1 LLM call(s))

1. **Dire Wolf AC:** 16.
2. **Alert feat:** When you roll Initiative, you can add twice your Proficiency Bonus to the roll.
3. **Topple:** The Context doesn't include the Topple mastery property, so I can't say what saving throw it forces.
4. **Point-buy budget:** The Context doesn't include point-buy rules, so I can't give the budget.

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


### v6_agentic  (12 chunks, 3 LLM call(s))

1. **Dire Wolf AC:** 16.
2. **Alert feat:** When you roll Initiative, you can add twice your Proficiency Bonus to the roll.
3. **Topple:** A Strength saving throw.
4. **Point-buy budget:** 30 points.

*facts found (judge): 4/4; missing: none*

*agentic sub-queries:* Dire Wolf / Alert feat / Topple / point-buy


*re-ranking* (query: `Dire Wolf`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.46 | yes | Animals > Dire Wolf |
| 2 | 2 | 3.56 | yes | Animals > Dire Wolf |
| 3 | 13 | 0.82 | yes | Magic Items > Bag of Tricks |
| 4 | 12 | -0.21 |  | Spells > Find Steed |
| 5 | 6 | -3.98 |  | Monsters A–Z > Werewolf |
| 6 | 3 | -4.19 |  | Monsters A–Z > Winter Wolf |
| 7 | 9 | -5.22 |  | Animals > Giant Wolf Spider |
| 8 | 11 | -5.25 |  | Monsters A–Z > Actions |
| 9 | 5 | -6.13 |  | Monsters A–Z > Winter Wolf |
| 10 | 8 | -6.64 |  | Animals > Giant Wolf Spider |
| 11 | 7 | -6.77 |  | Monsters A–Z > Bonus Actions |
| 12 | 10 | -6.90 |  | Monsters A–Z > Winter Wolf |
| 13 | 4 | -6.95 |  | Monsters A–Z > Werewolf |
| 14 | 16 | -7.00 |  | Monsters A–Z > Traits |
| 15 | 14 | -7.13 |  | Animals > Traits |
| 16 | 17 | -7.31 |  | Monsters A–Z > Actions |
| 17 | 20 | -9.54 |  | Classes > Level 2: Wild Shape |
| 18 | 19 | -10.94 |  | Animals > Actions |
| 19 | 18 | -11.07 |  | Monsters A–Z > Actions |
| 20 | 15 | -11.32 |  | Animals > Bonus Actions |


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


*re-ranking* (query: `Topple`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 4 | 1.42 | yes | Gameplay Toolbox > Collapsing Roof |
| 2 | 8 | 0.72 | yes | Equipment > Mastery Properties |
| 3 | 6 | -0.57 | yes | Classes > Level 3: Open Hand Technique |
| 4 | 18 | -0.78 |  | Equipment > Mastery Properties |
| 5 | 14 | -1.98 |  | Equipment > Mastery Properties |
| 6 | 16 | -2.31 |  | Equipment > Mastery Properties |
| 7 | 12 | -3.10 |  | Equipment > Mastery Properties |
| 8 | 2 | -3.46 |  | Gameplay Toolbox > Collapsing Roof |
| 9 | 10 | -10.18 |  | Equipment > Mastery Properties |
| 10 | 7 | -10.19 |  | Animals > Ankylosaurus |
| 11 | 17 | -10.22 |  | Animals > Giant Hyena |
| 12 | 5 | -10.23 |  | Animals > Giant Goat |
| 13 | 11 | -10.24 |  | Animals > Triceratops |
| 14 | 15 | -10.25 |  | Monsters A–Z > Gladiator |
| 15 | 9 | -10.32 |  | Monsters A–Z > Cockatrice |
| 16 | 19 | -10.32 |  | Monsters A–Z > Hippogriff |
| 17 | 13 | -10.89 |  | Feats > Boon of Combat Prowess |
| 18 | 3 | -10.92 |  | Feats > Ability Score Improvement |
| 19 | 20 | -10.98 |  | Classes > Level 3: Remarkable Athlete |
| 20 | 1 | -11.13 |  | Feats > Feat Descriptions |


*re-ranking* (query: `point-buy`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 3 | -6.48 | yes | Character Creation > Generate Your Scores |
| 2 | 14 | -7.86 | yes | Magic Items > Magic Item Values by Rarity |
| 3 | 11 | -8.20 | yes | Playing the Game > Hit Points |
| 4 | 18 | -8.62 |  | Rules Glossary > Short Rest |
| 5 | 2 | -8.67 |  | Character Creation > Starting Equipment |
| 6 | 8 | -9.00 |  | Equipment > Ammunition (Varies) |
| 7 | 1 | -9.21 |  | Character Creation > Hit Points and Hit Point Dice |
| 8 | 12 | -9.74 |  | Rules Glossary > Hit Point Dice |
| 9 | 6 | -9.85 |  | Playing the Game > Healing |
| 10 | 9 | -9.91 |  | Playing the Game > They Don't Stack |
| 11 | 20 | -10.18 |  | Spells > Call Lightning |
| 12 | 19 | -10.33 |  | Classes > Level 2: Font of Magic |
| 13 | 7 | -10.47 |  | Playing the Game > Lose Temporary Hit Points First |
| 14 | 4 | -10.47 |  | Playing the Game > Instant Death |
| 15 | 17 | -10.56 |  | Classes > Level 10: Tireless |
| 16 | 5 | -10.63 |  | Classes > Level 2: Monk's Focus |
| 17 | 16 | -10.70 |  | Rules Glossary > Area of Effect |
| 18 | 15 | -10.72 |  | Playing the Game > Temporary Hit Points |
| 19 | 10 | -10.79 |  | Rules Glossary > Cone [Area of Effect] |
| 20 | 13 | -10.84 |  | Classes > As a Multiclass Character |

*retrieved sections:* Animals > Dire Wolf | Magic Items > Bag of Tricks | Feats > Alert | Character Origins > Criminal | Magic Items > Rod of Alertness | Gameplay Toolbox > Collapsing Roof | Equipment > Mastery Properties | Classes > Level 3: Open Hand Technique | Character Creation > Generate Your Scores | Magic Items > Magic Item Values by Rarity | Playing the Game > Hit Points

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

[Magic Items > Rod of Alertness]
The rod's head stops glowing and the effect ends after 10 minutes or when a creature takes a Magic action to pull the rod from the ground. Once used, this property can't be used again until the next dawn.

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

[Magic Items > Magic Item Values by Rarity]
Common magic items can often be bought in a town or city. Uncommon and Rare magic items are usually found only in cities, and rarer magic items might be sold only in wondrous locations, such as a city on another plane of existence. If you allow characters to buy and sell magic items in your campaign, rarity can help you set prices for those items. Gold Piece values are provided in the Magic Item Rarities and Values table, though a seller might ask for a service rather than coin as payment.

---

[Playing the Game > Hit Points]
### Hit Points  
Hit Points represent durability and the will to live. Creatures with more Hit Points are more difficult to kill. Your Hit Point maximum is the number of Hit Points you have when uninjured. Your current Hit Points can be any number from that maximum down to 0, which is the lowest Hit Points can go.  
Whenever you take damage, subtract it from your Hit Points. Hit Point loss has no effect on your capabilities until you reach 0 Hit Points.
```
</details>


---

## q24 (multi-topic) Answer all four: (1) How far does Push move a creature and what size limit applies? (2) How long is a Short Rest? (3) What is the range of Fireball? (4) What AC bonus does Shield give?

**Gold facts (counterfactual data):** 15 feet; Large or smaller; 2-hour; 120 feet; +4 bonus to AC


### v0_closed_book  (0 chunks, 1 LLM call(s))

1. **Push:** It moves a creature up to **10 feet** away from you, and it only works on a target that is **Large or smaller**.
2. **Short Rest:** At least **1 hour**.
3. **Fireball:** Range is **150 feet**.
4. **Shield:** It gives a **+5 bonus to AC**, lasting until the start of your next turn.

*facts found (judge): 1/5; missing: 15 feet; 2-hour; 120 feet; +4 bonus to AC*


### v1_baseline  (3 chunks, 1 LLM call(s))

The Context doesn't cover any of the four questions:

1. **Push:** Not in the Context. It only lists monster actions (Greatclub, Javelin, Claw, Fire Breath, Spear), so I can't say how far Push moves a creature or what size limit applies.
2. **Short Rest:** Not in the Context, so I can't give its duration.
3. **Fireball:** Not in the Context. The only area effect is Fire Breath's 15-foot Cone, which is a monster action, not the Fireball spell, so I can't give its range.
4. **Shield:** Not in the Context, so I can't give its AC bonus.

*facts found (judge): 1/5; missing: Large or smaller; 2-hour; 120 feet; +4 bonus to AC*

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

The Context doesn't cover any of these four questions:

1. **Push:** The Context doesn't say how far Push moves a creature or what size limit applies.
2. **Short Rest:** The Context doesn't say how long a Short Rest is.
3. **Fireball:** The Context doesn't give Fireball's range.
4. **Shield:** The Context doesn't say what AC bonus Shield gives.

The Context only includes the Reach rule and three monster actions (Ocean Spear, Rend, and Fire Breath).

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

The Context doesn't include information for any of the four questions:

1. **Push:** The Context doesn't say how far Push moves a creature or what size limit applies.
2. **Short Rest:** The Context doesn't state how long a Short Rest is.
3. **Fireball:** The Context doesn't give Fireball's range.
4. **Shield:** The Context doesn't say what AC bonus Shield gives.

The Context only covers Reach and several monster Actions (Ocean Spear, Rend, Fire Breath, Claw, Spear, Handaxe, Tentacles, Scratch, and Longbow).

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

(1) The Context doesn't say how far Push moves a creature or what size limit applies.
(2) The Context doesn't say how long a Short Rest is.
(3) The Context doesn't give the range of Fireball.
(4) The Context doesn't say what AC bonus Shield gives.

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

**(1) Push:** The Shield can push a creature up to **10 feet** directly away from you. The context places no size limit on the push. The "your size or smaller" limit applies only to the optional Prone knockdown.

**(2) Short Rest:** A Short Rest is a **2-hour** period of downtime.

**(3) Fireball range:** Not in the Context. It has no Fireball spell.

**(4) Shield's AC bonus:** Not in the Context. It describes the Shield's Forceful Bash attack but gives no AC bonus.

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

1. **Push:** Push moves the target up to 10 feet directly away from you. The Context sets no size limit for the push. The size limit applies to knocking the target Prone: only if the creature is your size or smaller.
2. **Short Rest:** A Short Rest is a 2-hour period of downtime.
3. **Fireball:** The Context doesn't include Fireball, so I can't give its range. The only spell provided is Slow.
4. **Shield AC bonus:** The Context doesn't state an AC bonus for the Shield. It only describes the Shield of the Cavalier's Forceful Bash feature.

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


### v6_agentic  (15 chunks, 3 LLM call(s))

1. **Push** moves the creature up to **15 feet** straight away from you. It applies only to creatures that are **Large or smaller**.
2. A **Short Rest** lasts **2 hours**.
3. Fireball's range is **120 feet**.
4. Shield gives a **+4 bonus to AC**, including against the triggering attack.

*facts found (judge): 5/5; missing: none*

*agentic sub-queries:* Push spell / Short Rest / Fireball spell / Shield spell


*re-ranking* (query: `Push spell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 3.69 | yes | Spells > Arcane Hand |
| 2 | 13 | -0.82 | yes | Spells > Resilient Sphere |
| 3 | 7 | -1.43 | yes | Equipment > Mastery Properties |
| 4 | 9 | -2.86 |  | Playing the Game > Ability Modifier |
| 5 | 3 | -4.02 |  | Rules Glossary > Spell Attack |
| 6 | 4 | -4.35 |  | Spells > Command |
| 7 | 20 | -5.13 |  | Spells > Scrying |
| 8 | 17 | -5.49 |  | Magic Items > Bead of Force |
| 9 | 18 | -5.51 |  | Spells > Actions |
| 10 | 2 | -5.56 |  | Rules Glossary > Spell |
| 11 | 5 | -5.63 |  | Magic Items > Rod of Lordly Might |
| 12 | 6 | -6.41 |  | Monsters A–Z > Actions |
| 13 | 14 | -6.54 |  | Monsters A–Z > Actions |
| 14 | 12 | -6.70 |  | Classes > Level 9: Tactical Master |
| 15 | 16 | -7.18 |  | Monsters A–Z > Actions |
| 16 | 8 | -7.27 |  | Monsters A–Z > Actions |
| 17 | 11 | -7.40 |  | Monsters A–Z > Actions |
| 18 | 10 | -7.72 |  | Rules Glossary > Carrying Capacity |
| 19 | 19 | -8.42 |  | Playing the Game > Adventuring Equipment |
| 20 | 15 | -8.82 |  | Classes > Monk Subclass: Warrior of the Open Hand |


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


*re-ranking* (query: `Fireball spell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 6 | 6.65 | yes | Spells > Delayed Blast Fireball |
| 2 | 8 | 6.39 | yes | Spells > Delayed Blast Fireball |
| 3 | 1 | 6.11 | yes | Spells > Fireball |
| 4 | 2 | 6.10 |  | Spells > Delayed Blast Fireball |
| 5 | 3 | 5.76 | yes | Spells > Fireball |
| 6 | 7 | 5.41 |  | Magic Items > Wand of Fireballs |
| 7 | 19 | 5.12 |  | Monsters A–Z > Actions |
| 8 | 4 | 4.75 | yes | Spells > Delayed Blast Fireball |
| 9 | 15 | 3.82 |  | Magic Items > Helm of Brilliance |
| 10 | 9 | 3.68 |  | Magic Items > Hat of Many Spells |
| 11 | 12 | 2.79 |  | Classes > Level 7 Sorcerer Spells |
| 12 | 5 | 2.67 |  | Magic Items > Staff of Power |
| 13 | 10 | 2.51 |  | Classes > Level 7 Wizard Spells |
| 14 | 14 | 2.12 |  | Classes > Level 3 Sorcerer Spells |
| 15 | 20 | 2.01 |  | Spells > Flaming Sphere |
| 16 | 13 | 1.87 |  | Classes > Level 3 Wizard Spells |
| 17 | 11 | 1.29 |  | Magic Items > Necklace of Fireballs |
| 18 | 18 | -1.81 |  | Magic Items > Staff of the Magi |
| 19 | 17 | -2.50 |  | Magic Items > Staff of Fire |
| 20 | 16 | -6.24 |  | Rules Glossary > Spell |


*re-ranking* (query: `Shield spell`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 1 | 5.50 | yes | Magic Items > Spellguard Shield |
| 2 | 12 | 4.38 | yes | Spells > Fire Shield |
| 3 | 5 | 4.30 | yes | Spells > Shield |
| 4 | 10 | 3.91 |  | Spells > Shield of Faith |
| 5 | 2 | 3.03 |  | Magic Items > Shield of Missile Attraction |
| 6 | 14 | 2.99 |  | Spells > Fire Shield |
| 7 | 13 | 2.01 |  | Classes > Level 1 Paladin Spells |
| 8 | 17 | 1.63 |  | Magic Items > Shield of the Cavalier |
| 9 | 16 | 1.35 |  | Classes > Level 3: Fiend Spells |
| 10 | 7 | 1.33 |  | Magic Items > Animated Shield |
| 11 | 4 | 1.16 |  | Magic Items > Shield, +1, +2, or +3 |
| 12 | 9 | 1.12 |  | Magic Items > Sentinel Shield |
| 13 | 15 | 0.97 |  | Magic Items > Shield of the Cavalier |
| 14 | 8 | -0.15 |  | Magic Items > Arrow-Catching Shield |
| 15 | 11 | -1.19 |  | Magic Items > Shield of the Cavalier |
| 16 | 20 | -1.43 |  | Equipment > Armor Training |
| 17 | 6 | -1.48 |  | Equipment > Armor Training |
| 18 | 3 | -1.52 |  | Magic Items > Animated Shield |
| 19 | 18 | -4.49 |  | Equipment > One at a Time |
| 20 | 19 | -5.56 |  | Magic Items > Bracers of Defense |


*re-ranking* (query: `Fireball spell range`): candidate pool of 20, ordered by cross-encoder score

| CE rank | before-rerank rank | CE score | to LLM | section |
|---|---|---|---|---|
| 1 | 2 | 6.11 | yes | Spells > Fireball |
| 2 | 1 | 4.93 | yes | Spells > Delayed Blast Fireball |
| 3 | 14 | 4.69 | yes | Spells > Fire Bolt |
| 4 | 5 | 4.58 | yes | Spells > Delayed Blast Fireball |
| 5 | 4 | 3.52 |  | Spells > Delayed Blast Fireball |
| 6 | 3 | 2.93 | yes | Spells > Fireball |
| 7 | 13 | 2.47 |  | Spells > Scorching Ray |
| 8 | 11 | 1.79 | yes | Spells > Delayed Blast Fireball |
| 9 | 20 | 1.43 |  | Spells > Produce Flame |
| 10 | 6 | 0.86 |  | Magic Items > Wand of Fireballs |
| 11 | 19 | 0.78 |  | Monsters A–Z > Actions |
| 12 | 9 | 0.61 |  | Spells > Range |
| 13 | 12 | -0.13 |  | Magic Items > Hat of Many Spells |
| 14 | 15 | -0.79 |  | Classes > Level 7 Sorcerer Spells |
| 15 | 18 | -1.28 |  | Classes > Level 7 Wizard Spells |
| 16 | 7 | -1.35 |  | Magic Items > Staff of Power |
| 17 | 17 | -1.70 |  | Playing the Game > Range |
| 18 | 16 | -1.81 |  | Magic Items > Necklace of Fireballs |
| 19 | 10 | -2.37 |  | Spells > Range |
| 20 | 8 | -3.37 |  | Classes > Distant Spell |

*retrieved sections:* Spells > Arcane Hand | Spells > Resilient Sphere | Equipment > Mastery Properties | Rules Glossary > Short Rest | Equipment > Attune during a Short Rest | Spells > Delayed Blast Fireball | Spells > Fireball | Magic Items > Spellguard Shield | Spells > Fire Shield | Spells > Shield | Spells > Fire Bolt

<details><summary>full retrieved context</summary>

```
[Spells > Arcane Hand]
**Forceful Hand.** The hand attempts to push a Huge or smaller creature within 5 feet of it. The target must succeed on a Strength saving throw, or the hand pushes the target up to 5 feet plus a number of feet equal to five times your spellcasting ability modifier. The hand moves with the target, remaining within 5 feet of it.

---

[Spells > Resilient Sphere]
The sphere is weightless and just large enough to contain the creature or object inside. An enclosed creature can take an action to push against the sphere's walls and thus roll the sphere at up to half the creature's Speed. Similarly, the globe can be picked up and moved by other creatures.  
A _Disintegrate_ spell targeting the globe destroys it without harming anything inside.

---

[Equipment > Mastery Properties]
**Push.** If you hit a creature with this weapon, you can push the creature up to 15 feet straight away from yourself if it is Large or smaller.  
**Sap.** If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.

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

[Spells > Delayed Blast Fireball]
**Duration:** Concentration, up to 1 minute  
A beam of yellow light flashes from you, then condenses at a chosen point within range as a glowing bead for the duration. When the spell ends, the bead explodes, and each creature in a 20-foot-radius Sphere centered on that point makes a Dexterity saving throw. A creature takes Fire damage equal to the total accumulated damage on a failed save or half as much damage on a successful one.

---

[Spells > Delayed Blast Fireball]
The spell's base damage is 12d6, and the damage increases by 1d6 whenever your turn ends and the spell hasn't ended.  
If a creature touches the glowing bead before the spell ends, that creature makes a Dexterity saving throw. On a failed save, the spell ends, causing the bead to explode. On a successful save, the creature can throw the bead up to 40 feet. If the thrown bead enters a creature's space or collides with a solid object, the spell ends, and the bead explodes.

---

[Spells > Fireball]
Flammable objects in the area that aren't being worn or carried start burning.  
_Using a Higher-Level Spell Slot._ The damage increases by 1d6 for each spell slot level above 3.

---

[Magic Items > Spellguard Shield]
#### Spellguard Shield  
_Armor (Shield), Very Rare (Requires Attunement)_  
While holding this Shield, you have Advantage on saving throws against spells and other magical effects, and spell attack rolls have Disadvantage against you.

---

[Spells > Fire Shield]
The flames provide you with a warm shield or a chill shield, as you choose. The warm shield grants you Resistance to Cold damage, and the chill shield grants you Resistance to Fire damage.  
In addition, whenever a creature within 5 feet of you hits you with a melee attack roll, the shield erupts with flame. The attacker takes 2d8 Fire damage from a warm shield or 2d8 Cold damage from a chill shield.

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
#### Delayed Blast Fireball  
_Level 7 Evocation (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 150 feet
**Components:** V, S, M (a ball of bat guano and sulfur)
**Duration:** Concentration, up to 1 minute

---

[Spells > Fire Bolt]
#### Fire Bolt  
_Evocation Cantrip (Sorcerer, Wizard)_  
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S
**Duration:** Instantaneous  
You hurl a mote of fire at a creature or an object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Fire damage. A flammable object hit by this spell starts burning if it isn't being worn or carried.
```
</details>
