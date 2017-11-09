---
title: Sullustan Recon Sharpshooter (SullustanSample)
category: unit
---

# Sullustan Recon Sharpshooter (SullustanSample) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: No
  * Role: Striker
  * Unit capacity: 8
  * Type: infantry

|Level |3   |7   |1   |10  |6   |9   |4   |8   |2   |5   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|4480|7040|3200|9600|6400|8320|5120|7680|3840|5760|


### Training stats

  * Training time: 0s
  * Training cost: Free

### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

### Modifiers

#### Modifier "Marksman damage"

  * Marksman damage apply value as: relativePercent
  * Marksman damage buff ID: buffMarksmanDamage
  * Marksman damage duration: permanent
  * Marksman damage modifier: damage
  * Marksman damage ms first proc: 0s
  * Marksman damage ms per proc: permanent
  * Marksman damage name: Marksman damage
  * Marksman damage stack: 0
  * Marksman damage target: self

|Level                |3  |7  |1  |10  |6  |9  |4  |8  |2  |5  |
|---------------------|---|---|---|----|---|---|---|---|---|---|
|Marksman damage value|58%|81%|49%|100%|75%|93%|64%|87%|53%|69%|



#### Modifier "Marksman health"

  * Marksman health apply value as: relativePercentOfMax
  * Marksman health buff ID: buffMarksmanHealth
  * Marksman health duration: permanent
  * Marksman health modifier: maxHealth
  * Marksman health ms first proc: 0s
  * Marksman health ms per proc: permanent
  * Marksman health name: Marksman health
  * Marksman health stack: 0
  * Marksman health target: self

|Level                |3  |7  |1  |10  |6  |9  |4  |8  |2  |5  |
|---------------------|---|---|---|----|---|---|---|---|---|---|
|Marksman health value|58%|81%|49%|100%|75%|93%|64%|87%|53%|69%|



#### Modifier "Sum phtm Y wing"

  * Sum phtm Y wing apply value as: absolute
  * Sum phtm Y wing buff ID: buffSumPhtmYWing
  * Sum phtm Y wing duration: permanent
  * Sum phtm Y wing modifier: summon
  * Sum phtm Y wing ms first proc: 0s
  * Sum phtm Y wing ms per proc: permanent
  * Sum phtm Y wing name: Sum phtm Y wing
  * Sum phtm Y wing stack: 1
  * Sum phtm Y wing target: self
  * Sum phtm Y wing value: 1

|Level                          |3                                                    |7                                                    |1                                                    |10                                                    |6                                                    |9                                                    |4                                                    |8                                                    |2                                                    |5                                                    |
|-------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
|Sum phtm Y wing summon visitors|["trp_title_PhantomYWing" level 3](PhantomYWing.html)|["trp_title_PhantomYWing" level 7](PhantomYWing.html)|["trp_title_PhantomYWing" level 1](PhantomYWing.html)|["trp_title_PhantomYWing" level 10](PhantomYWing.html)|["trp_title_PhantomYWing" level 6](PhantomYWing.html)|["trp_title_PhantomYWing" level 9](PhantomYWing.html)|["trp_title_PhantomYWing" level 4](PhantomYWing.html)|["trp_title_PhantomYWing" level 8](PhantomYWing.html)|["trp_title_PhantomYWing" level 2](PhantomYWing.html)|["trp_title_PhantomYWing" level 5](PhantomYWing.html)|


  * Sum phtm Y wing summon die with summoner: Yes
  * Sum phtm Y wing summon max proc: 1
  * Sum phtm Y wing summon random spawn radius: 5
  * Sum phtm Y wing summon same team: Yes
  * Sum phtm Y wing summon spawn points: 0,0,0
  * Sum phtm Y wing summon target summoner: No
  * Sum phtm Y wing summon visitor type: Troop

|Level                              |3                    |7                    |1                    |10                    |6                    |9                    |4                    |8                    |2                    |5                    |
|-----------------------------------|---------------------|---------------------|---------------------|----------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|Sum phtm Y wing summon visitor uids|troopRebPhantomYWing3|troopRebPhantomYWing7|troopRebPhantomYWing1|troopRebPhantomYWing10|troopRebPhantomYWing6|troopRebPhantomYWing9|troopRebPhantomYWing4|troopRebPhantomYWing8|troopRebPhantomYWing2|troopRebPhantomYWing5|


## Main attack : projectileMarksman

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (60)**, **Flying infantry (60)**, **Heavy infantry (60)**, **Infantry (60)**, **Support troop (60)**, Flying vehicle (50), Headquarters (50), Heavy vehicle (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * New target on reload: No
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 1.500s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 5
  * Time between shots: 500ms
  * Target locking: No

|Level          |3   |7   |1  |10  |6   |9   |4   |8   |2   |5   |
|---------------|----|----|---|----|----|----|----|----|----|----|
|Damage per shot|1335|2098|954|2860|1907|2479|1526|2288|1144|1716|


### Projectile

  * Splash damage percentages: 100

|Level                       |3   |7       |1   |10      |6       |9       |4       |8       |2       |5   |
|----------------------------|----|--------|----|--------|--------|--------|--------|--------|--------|----|
|Displayed damage per second |3845|7325    |2505|11400   |6360    |9455    |4620    |8360    |3140    |5445|
|Calculated damage per second|1780|2797.333|1272|3813.333|2542.667|3305.333|2034.667|3050.667|1525.333|2288|


  * Cannons per sequence: 1
  * Cliptime: 3.750s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(300)**: Flying vehicle, Light vehicle, Vehicule hero, **(250)**: Heavy vehicle, Heavy vehicule hero, **(200)**: Flying infantry, Infantry, Infantry hero, Support troop, **(150)**: Heavy infantry, Heavy infantry hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(50)**: Shield, Shield generator, **(40)**: Wall
  * Pass through shield: No
  * Salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SullustanSample

|Level                     |3                                                        |7                                                        |1                                                        |10                                                          |6                                                        |9                                                        |4                                                        |8                                                        |2                                                        |5                                                        |
|--------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Spawn apply buffs         |buffMarksmanHealth3,buffMarksmanDamage3,buffSumPhtmYWing3|buffMarksmanHealth7,buffMarksmanDamage7,buffSumPhtmYWing7|buffMarksmanHealth1,buffMarksmanDamage1,buffSumPhtmYWing1|buffMarksmanHealth10,buffMarksmanDamage10,buffSumPhtmYWing10|buffMarksmanHealth6,buffMarksmanDamage6,buffSumPhtmYWing6|buffMarksmanHealth9,buffMarksmanDamage9,buffSumPhtmYWing9|buffMarksmanHealth4,buffMarksmanDamage4,buffSumPhtmYWing4|buffMarksmanHealth8,buffMarksmanDamage8,buffSumPhtmYWing8|buffMarksmanHealth2,buffMarksmanDamage2,buffSumPhtmYWing2|buffMarksmanHealth5,buffMarksmanDamage5,buffSumPhtmYWing5|
|Sum phtm Y wing details   |sumPhtmYWing3                                            |sumPhtmYWing7                                            |sumPhtmYWing1                                            |sumPhtmYWing10                                              |sumPhtmYWing6                                            |sumPhtmYWing9                                            |sumPhtmYWing4                                            |sumPhtmYWing8                                            |sumPhtmYWing2                                            |sumPhtmYWing5                                            |
|Sum phtm Y wing summon uid|sumPhtmYWing3                                            |sumPhtmYWing7                                            |sumPhtmYWing1                                            |sumPhtmYWing10                                              |sumPhtmYWing6                                            |sumPhtmYWing9                                            |sumPhtmYWing4                                            |sumPhtmYWing8                                            |sumPhtmYWing2                                            |sumPhtmYWing5                                            |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: sullustan_rbl-ani
  * Audio attack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_sullustan_01":33,"sfx_ui_unitcomplete_sullustan_02":33,"sfx_ui_unitcomplete_sullustan_03":34
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: sullustan_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: heroes
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 6.83,8.99,17.86
  * Icon closeup camera position: 3.19,5.81,10.64
  * Icon closeup lookat position: -0.39,2.05,-1.11
  * Icon lookat position: -0.56,1.32,-0.71
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: projectileMarksman
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |3   |7   |1   |10   |6   |9   |4   |8   |2   |5   |
|---------------------------|----|----|----|-----|----|----|----|----|----|----|
|Displayed damage per second|3845|7325|2505|11400|6360|9455|4620|8360|3140|5445|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Marksman damage is refreshing: No
  * Marksman damage tags: damage
  * Marksman health is refreshing: No
  * Marksman health tags: maxHealth
  * Max scale: No
  * Point value: 1
  * Seeks target: No
  * Streams: no
  * Strict cool down: No
  * Xp: 0

|Level|3     |7     |1     |10    |6     |9     |4     |8     |2     |5     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|314702|314706|314700|314709|314705|314708|314703|314707|314701|314704|


