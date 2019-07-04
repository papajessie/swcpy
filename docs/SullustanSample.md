---
title: Sullustan Recon Sharpshooter (SullustanSample)
category: unit
---

# Sullustan Recon Sharpshooter (SullustanSample)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: No
  * Role: Striker
  * Unit capacity: 8
  * Type: infantry

|Level |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|9600|8320|7680|7040|6400|5760|5120|4480|3840|3200|


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

|Level                |10    |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|---------------------|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Marksman damage value|100.0%|93.0%|87.0%|81.0%|75.0%|69.0%|64.0%|58.0%|53.0%|49.0%|



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

|Level                |10    |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|---------------------|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Marksman health value|100.0%|93.0%|87.0%|81.0%|75.0%|69.0%|64.0%|58.0%|53.0%|49.0%|



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

|Level                          |10                                                    |9                                                    |8                                                    |7                                                    |6                                                    |5                                                    |4                                                    |3                                                    |2                                                    |1                                                    |
|-------------------------------|------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
|Sum phtm Y wing summon visitors|["trp_title_PhantomYWing" level 10](PhantomYWing.html)|["trp_title_PhantomYWing" level 9](PhantomYWing.html)|["trp_title_PhantomYWing" level 8](PhantomYWing.html)|["trp_title_PhantomYWing" level 7](PhantomYWing.html)|["trp_title_PhantomYWing" level 6](PhantomYWing.html)|["trp_title_PhantomYWing" level 5](PhantomYWing.html)|["trp_title_PhantomYWing" level 4](PhantomYWing.html)|["trp_title_PhantomYWing" level 3](PhantomYWing.html)|["trp_title_PhantomYWing" level 2](PhantomYWing.html)|["trp_title_PhantomYWing" level 1](PhantomYWing.html)|


  * Sum phtm Y wing summon die with summoner: Yes
  * Sum phtm Y wing summon max proc: 1
  * Sum phtm Y wing summon random spawn radius: 5
  * Sum phtm Y wing summon same team: Yes
  * Sum phtm Y wing summon spawn points: 0,0,0
  * Sum phtm Y wing summon target summoner: No
  * Sum phtm Y wing summon visitor type: Troop

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

  * Animation delay: 0s
  * Charge time: 250ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * New target on reload: Yes
  * Can shoot over walls: No
  * Reload time: 1.500s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 5
  * Shot delay: 500ms
  * Target locking: No

|Level          |10  |9   |8   |7   |6   |5   |4   |3   |2   |1  |
|---------------|----|----|----|----|----|----|----|----|----|---|
|Damage per shot|2860|2479|2288|2098|1907|1716|1526|1335|1144|954|


### Projectile

  * Splash damage percentages: 100

|Level                       |10   |9    |8    |7    |6   |5   |4   |3   |2   |1   |
|----------------------------|-----|-----|-----|-----|----|----|----|----|----|----|
|Displayed damage per second |10395|9455 |8360 |7325 |6360|5445|4620|3845|3140|2505|
|Calculated damage per second|3813 |3305 |3050 |2797 |2542|2288|2034|1780|1525|1272|
|Calculated damage per cycle |14300|12395|11440|10490|9535|8580|7630|6675|5720|4770|


  * Cannons per sequence: 1
  * Shooting cycle duration: 3.750s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(300)**: Flying vehicle, Light vehicle, Vehicule hero, **(250)**: Heavy vehicle, Heavy vehicule hero, **(200)**: Flying infantry, Infantry, Infantry hero, Support troop, **(150)**: Heavy infantry, Heavy infantry hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(50)**: Shield, Shield generator, **(40)**: Wall
  * Pass through shield: No
  * Salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SullustanSample

|Level                     |10                                                          |9                                                        |8                                                        |7                                                        |6                                                        |5                                                        |4                                                        |3                                                        |2                                                        |1                                                        |
|--------------------------|------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Spawn apply buffs         |buffMarksmanHealth10,buffMarksmanDamage10,buffSumPhtmYWing10|buffMarksmanHealth9,buffMarksmanDamage9,buffSumPhtmYWing9|buffMarksmanHealth8,buffMarksmanDamage8,buffSumPhtmYWing8|buffMarksmanHealth7,buffMarksmanDamage7,buffSumPhtmYWing7|buffMarksmanHealth6,buffMarksmanDamage6,buffSumPhtmYWing6|buffMarksmanHealth5,buffMarksmanDamage5,buffSumPhtmYWing5|buffMarksmanHealth4,buffMarksmanDamage4,buffSumPhtmYWing4|buffMarksmanHealth3,buffMarksmanDamage3,buffSumPhtmYWing3|buffMarksmanHealth2,buffMarksmanDamage2,buffSumPhtmYWing2|buffMarksmanHealth1,buffMarksmanDamage1,buffSumPhtmYWing1|
|Sum phtm Y wing details   |sumPhtmYWing10                                              |sumPhtmYWing9                                            |sumPhtmYWing8                                            |sumPhtmYWing7                                            |sumPhtmYWing6                                            |sumPhtmYWing5                                            |sumPhtmYWing4                                            |sumPhtmYWing3                                            |sumPhtmYWing2                                            |sumPhtmYWing1                                            |
|Sum phtm Y wing summon uid|sumPhtmYWing10                                              |sumPhtmYWing9                                            |sumPhtmYWing8                                            |sumPhtmYWing7                                            |sumPhtmYWing6                                            |sumPhtmYWing5                                            |sumPhtmYWing4                                            |sumPhtmYWing3                                            |sumPhtmYWing2                                            |sumPhtmYWing1                                            |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

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

|Level                      |10   |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------------------|-----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|10395|9455|8360|7325|6360|5445|4620|3845|3140|2505|


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

|Level|10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|261610|261609|261608|261607|261606|261605|261604|261603|261602|261601|


