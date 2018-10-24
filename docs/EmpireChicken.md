---
title: AT-DT Walker (EmpireChicken)
category: unit
---

# AT-DT Walker (EmpireChicken)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Generic
  * Unit capacity: 16
  * Type: vehicle

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|20000|22050|24200|26350|28650|31050|35800|37300|38300|41750|


|Level |11   |
|------|-----|
|Health|43820|


### Training stats

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|1m27s                          |1m32s                                  |1m41s                                  |1m54s                                  |2m8s                                   |2m24s                                  |2m42s                                  |3m2s                                   |3m23s                                  |3m45s                                   |
|Training cost|810$                           |945$                                   |1080$                                  |1230$                                  |1365$                                  |1500$                                  |1710$                                  |1830$                                  |1920$                                  |2070$                                   |
|Building     |[Factory 1](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


|Level        |11                                      |
|-------------|----------------------------------------|
|Training time|4m7s                                    |
|Training cost|2220$                                   |
|Building     |[Research Lab 11](empireOffenseLab.html)|


### Upgrading stats

|Level               |1                |2                |3                |4                |5                |6                |7                |8                |9                 |10                |
|--------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|------------------|
|Upgrade time        |0s               |0s               |0s               |0s               |0s               |0s               |0s               |0s               |0s                |0s                |
|Upgrade requirements|32 data fragments|28 data fragments|30 data fragments|40 data fragments|50 data fragments|60 data fragments|70 data fragments|90 data fragments|120 data fragments|160 data fragments|


|Level               |11                |
|--------------------|------------------|
|Upgrade time        |5s                |
|Upgrade requirements|220 data fragments|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : Chicken

### Targeting

  * Attack shield border: No
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0s
  * Charge time: 1.500s
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 300ms
  * Can shoot over walls: No
  * Reload time: 1.500s
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 1
  * Shot delay: 0s
  * Target locking: No

|Level          |1   |2   |3   |4   |5   |6    |7    |8    |9    |10   |
|---------------|----|----|----|----|----|-----|-----|-----|-----|-----|
|Damage per shot|5400|6348|7293|8241|9189|10134|11082|12030|12978|13923|


|Level          |11   |
|---------------|-----|
|Damage per shot|14490|


### Projectile

  * Splash damage percentages: 100,80,30

|Level                       |1   |2   |3   |4   |5   |6    |7    |8    |9    |10   |
|----------------------------|----|----|----|----|----|-----|-----|-----|-----|-----|
|Displayed damage per second |1800|2115|2430|2745|3065|3380 |3695 |4010 |4325 |4640 |
|Calculated damage per second|1800|2116|2431|2747|3063|3378 |3694 |4010 |4326 |4641 |
|Calculated damage per cycle |5400|6348|7293|8241|9189|10134|11082|12030|12978|13923|


|Level                       |11   |
|----------------------------|-----|
|Displayed damage per second |4828 |
|Calculated damage per second|4830 |
|Calculated damage per cycle |14490|


  * Cannons per sequence: 1
  * Shooting cycle duration: 3s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(120)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Support troop, Vehicule hero, **(100)**: Droideka, Headquarters, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EmpireChicken
  * Upgrade shard uid: shrd_troopEmpireChicken

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: chicken_emp-ani
  * Audio attack: "sfx_attack_walker_1":25,"sfx_attack_walker_2":25,"sfx_attack_walker_3":25,"sfx_attack_walker_4":25
  * Audio death: "sfx_death_walker_1":100
  * Audio placement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * Bullet: fx_cwalker_beam_r
  * Bundle name: chicken_emp-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Hit spark: fx_cwalker_hit_r
  * Icon camera position: 23.31,13.91,43.63
  * Icon closeup camera position: 23.31,13.91,43.63
  * Icon closeup lookat position: -0.96,2.84,-1.15
  * Icon lookat position: -0.96,2.84,-1.15
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_lrg
  * Muzzle flash fade time: 1.5
  * Name: Chicken
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: Yes
  * Unlocked by event: true
  * Unlocked by tournament: Yes

|Level                      |1             |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |(not found)   |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|1800          |2115       |2430       |2745       |3065       |3380       |3695       |4010       |4325       |4640       |
|Icon unlock rotation       |0,-20,0       |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |0.63,0.63,0.63|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Prestige                   |(not found)   |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


|Level                      |11                           |
|---------------------------|-----------------------------|
|Deploy vfx                 |vfx_prestige_deploy_small_emp|
|Displayed damage per second|4828                         |
|Icon unlock rotation       |(not found)                  |
|Icon unlock scale          |(not found)                  |
|Prestige                   |true                         |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: Yes
  * Target in range modifier: 1
  * Xp: 0

|Level      |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |81201|81202|81203|81204|81205|81206|81207|81208|81209|81210|
|Point value|1    |1.200|1.400|1.600|1.800|2    |2.200|2.400|2.600|3    |


|Level      |11   |
|-----------|-----|
|Order      |81211|
|Point value|3    |


