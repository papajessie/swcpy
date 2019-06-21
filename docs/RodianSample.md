---
title: Rodian Recon Sniper (RodianSample)
category: unit
---

# Rodian Recon Sniper (RodianSample)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: No
  * Role: Striker
  * Unit capacity: 7
  * Type: infantry

|Level |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|8400|7280|6720|6160|5600|5040|4480|3920|3360|2800|


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

#### Modifier "Sniper damage"

  * Sniper damage apply value as: relativePercent
  * Sniper damage buff ID: buffSniperDamage
  * Sniper damage duration: permanent
  * Sniper damage modifier: damage
  * Sniper damage ms first proc: 0s
  * Sniper damage ms per proc: permanent
  * Sniper damage name: Sniper damage
  * Sniper damage stack: 0
  * Sniper damage target: self

|Level              |10    |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-------------------|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Sniper damage value|100.0%|93.0%|87.0%|81.0%|75.0%|69.0%|64.0%|58.0%|53.0%|49.0%|



#### Modifier "Sniper health"

  * Sniper health apply value as: relativePercentOfMax
  * Sniper health buff ID: buffSniperHealth
  * Sniper health duration: permanent
  * Sniper health modifier: maxHealth
  * Sniper health ms first proc: 0s
  * Sniper health ms per proc: permanent
  * Sniper health name: Sniper health
  * Sniper health stack: 0
  * Sniper health target: self

|Level              |10    |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-------------------|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Sniper health value|100.0%|93.0%|87.0%|81.0%|75.0%|69.0%|64.0%|58.0%|53.0%|49.0%|



#### Modifier "Sum phtm tie bomber"

  * Sum phtm tie bomber apply value as: absolute
  * Sum phtm tie bomber buff ID: buffSumPhtmTieBomber
  * Sum phtm tie bomber duration: permanent
  * Sum phtm tie bomber modifier: summon
  * Sum phtm tie bomber ms first proc: 0s
  * Sum phtm tie bomber ms per proc: permanent
  * Sum phtm tie bomber name: Sum phtm tie bomber
  * Sum phtm tie bomber stack: 1
  * Sum phtm tie bomber target: self
  * Sum phtm tie bomber value: 1

|Level                              |10                                                            |9                                                            |8                                                            |7                                                            |6                                                            |5                                                            |4                                                            |3                                                            |2                                                            |1                                                            |
|-----------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
|Sum phtm tie bomber summon visitors|["trp_title_PhantomTieBomber" level 10](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 9](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 8](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 7](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 6](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 5](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 4](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 3](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 2](PhantomTieBomber.html)|["trp_title_PhantomTieBomber" level 1](PhantomTieBomber.html)|


  * Sum phtm tie bomber summon die with summoner: Yes
  * Sum phtm tie bomber summon max proc: 1
  * Sum phtm tie bomber summon random spawn radius: 5
  * Sum phtm tie bomber summon same team: Yes
  * Sum phtm tie bomber summon spawn points: 0,0,0
  * Sum phtm tie bomber summon target summoner: No
  * Sum phtm tie bomber summon visitor type: Troop

## Main attack : projectileSniper

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
|Damage per shot|2503|2169|2002|1836|1669|1502|1335|1168|1001|835|


### Projectile

  * Splash damage percentages: 100

|Level                       |10   |9    |8    |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|-----|-----|-----|----|----|----|----|----|----|----|
|Displayed damage per second |9100 |8275 |7315 |6415|5565|4765|4040|3365|2745|2195|
|Calculated damage per second|3337 |2892 |2669 |2448|2225|2002|1780|1557|1334|1113|
|Calculated damage per cycle |12515|10845|10010|9180|8345|7510|6675|5840|5005|4175|


  * Cannons per sequence: 1
  * Shooting cycle duration: 3.750s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(300)**: Flying infantry, Infantry, Infantry hero, Support troop, **(250)**: Heavy infantry, Heavy infantry hero, **(200)**: Flying vehicle, Light vehicle, Vehicule hero, **(150)**: Heavy vehicle, Heavy vehicule hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(50)**: Shield, Shield generator, **(40)**: Wall
  * Pass through shield: No
  * Salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RodianSample

|Level                         |10                                                          |9                                                        |8                                                        |7                                                        |6                                                        |5                                                        |4                                                        |3                                                        |2                                                        |1                                                        |
|------------------------------|------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Spawn apply buffs             |buffSniperHealth10,buffSniperDamage10,buffSumPhtmTieBomber10|buffSniperHealth9,buffSniperDamage9,buffSumPhtmTieBomber9|buffSniperHealth8,buffSniperDamage8,buffSumPhtmTieBomber8|buffSniperHealth7,buffSniperDamage7,buffSumPhtmTieBomber7|buffSniperHealth6,buffSniperDamage6,buffSumPhtmTieBomber6|buffSniperHealth5,buffSniperDamage5,buffSumPhtmTieBomber5|buffSniperHealth4,buffSniperDamage4,buffSumPhtmTieBomber4|buffSniperHealth3,buffSniperDamage3,buffSumPhtmTieBomber3|buffSniperHealth2,buffSniperDamage2,buffSumPhtmTieBomber2|buffSniperHealth1,buffSniperDamage1,buffSumPhtmTieBomber1|
|Sum phtm tie bomber details   |sumPhtmTieBomber10                                          |sumPhtmTieBomber9                                        |sumPhtmTieBomber8                                        |sumPhtmTieBomber7                                        |sumPhtmTieBomber6                                        |sumPhtmTieBomber5                                        |sumPhtmTieBomber4                                        |sumPhtmTieBomber3                                        |sumPhtmTieBomber2                                        |sumPhtmTieBomber1                                        |
|Sum phtm tie bomber summon uid|sumPhtmTieBomber10                                          |sumPhtmTieBomber9                                        |sumPhtmTieBomber8                                        |sumPhtmTieBomber7                                        |sumPhtmTieBomber6                                        |sumPhtmTieBomber5                                        |sumPhtmTieBomber4                                        |sumPhtmTieBomber3                                        |sumPhtmTieBomber2                                        |sumPhtmTieBomber1                                        |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: rodiansniper_emp-ani
  * Audio attack: "sfx_attack_ig86_01":33,"sfx_attack_ig86_02":33,"sfx_attack_ig86_03":34
  * Audio death: "sfx_death_rodian_1":33,"sfx_death_rodian_2":33,"sfx_death_rodian_3":34
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rodian_01":50,"sfx_ui_unitcomplete_rodian_02":50
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: rodiansniper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: heroes
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 5.8,8.85,16.13
  * Icon closeup camera position: 2.41,5.49,9.51
  * Icon closeup lookat position: -0.33,1.97,-1.12
  * Icon lookat position: -0.51,1.24,-0.7
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: projectileSniper
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|9100|8275|7315|6415|5565|4765|4040|3365|2745|2195|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Point value: 1
  * Seeks target: No
  * Sniper damage is refreshing: No
  * Sniper damage tags: damage
  * Sniper health is refreshing: No
  * Sniper health tags: maxHealth
  * Streams: no
  * Strict cool down: No
  * Xp: 0

|Level|10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order|61610|61609|61608|61607|61606|61605|61604|61603|61602|61601|


