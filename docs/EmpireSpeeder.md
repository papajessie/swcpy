---
title: Speeder Bike (EmpireSpeeder)
category: unit
---

# Speeder Bike (EmpireSpeeder) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 6
  * Type: vehicle

|Level |1   |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|9240|10120|11090|12170|13360|14690|16160|17790|19610|21640|


### Training stats

|Level   |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|--------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Building|[Factory 1](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

|Level               |1   |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s  |30m  |1h30m|5h    |10h   |1d12h  |2d12h  |4d     |6d      |1w2d    |
|Upgrade requirements|500$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


### Movement stats

  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 15
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x2

|Level       |1, 2, 3, 4, 5, 6|7, 8, 9, 10|
|------------|----------------|-----------|
|Acceleration|0               |8          |
|Max speed   |40              |80         |


## Main attack : T7-E Speederbike / Empire Speeder Bike Upgrade

### Targeting

  * Attack shield border: No
  * Max attack range: 6
  * Min attack range: 0
  * New rotation speed: 3927
  * Target preference strength: 90
  * Target preferences: **Droideka (70)**, **Flying infantry (70)**, **Flying vehicle (70)**, **Heavy infantry (70)**, **Heavy vehicle (70)**, **Infantry (70)**, **Light vehicle (70)**, **Support troop (70)**, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1,1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Retargeting offset: 12
  * Self-centered targeting: No
  * Time between shots: 0s
  * Target locking: No

|Level                                     |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot                           |970  |1030 |1100 |1170 |1250 |1330 |1420 |1520 |1620 |1730 |
|Time between end of clip and start of clip|800ms|800ms|800ms|800ms|800ms|800ms|625ms|625ms|625ms|625ms|
|Shot count                                |1    |1    |1    |1    |1    |1    |2    |2    |2    |2    |


### Projectile

|Level                       |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|---|---|----|----|----|----|----|----|----|----|
|Displayed damage per second |920|980|1050|1110|1190|1270|1620|1740|1850|1980|
|Calculated damage per second|923|980|1047|1114|1190|1266|3245|3474|3702|3954|


  * Cannons per sequence: 2
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Pass through shield: No
  * Salvos: 1

|Level             |1, 2, 3, 4, 5, 6                                                                                                                                                                                                                                                                                                                                       |7, 8, 9, 10                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Cliptime          |1.050s                                                                                                                                                                                                                                                                                                                                                 |875ms                                                                                                                                                                                                                                                                                                                                                                                           |
|Damage multipliers|**(150)**: Flying infantry, Infantry, Infantry hero, Support troop, **(125)**: Heavy infantry, Heavy infantry hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(75)**: Flying vehicle, Light vehicle, Vehicule hero, **(50)**: Heavy vehicle, Heavy vehicule hero|**(250)**: Flying infantry, Infantry, Support troop, **(225)**: Flying vehicle, Light vehicle, **(200)**: Heavy vehicle, **(175)**: Heavy infantry, **(100)**: Droideka, Heavy infantry hero, Heavy vehicule hero, Infantry hero, Vehicule hero, **(75)**: Wall, **(50)**: Headquarters, **(25)**: Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Trap|


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EmpireSpeeder

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: speederbike_emp-ani
  * Audio attack: "sfx_attack_empire_mtv7_1":25,"sfx_attack_empire_mtv7_2":25,"sfx_attack_empire_mtv7_3":25,"sfx_attack_empire_mtv7_4":25
  * Audio death: "sfx_death_empire_mtv7_1":33,"sfx_death_empire_mtv7_2":33,"sfx_death_empire_mtv7_3":34
  * Audio placement: "sfx_placement_empire_mtv7_1":50,"sfx_placement_empire_mtv7_2":50
  * Buff asset offset: 0,1,0
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: speederbike_emp-ani
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Gun position: "speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_locator_gun1":1,"speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_locator_gun2":1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 14.03,11.98,20.6
  * Icon lookat position: -0.26,1.18,-0.59
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1               |2               |3               |4               |5               |6               |7                          |8                          |9                          |10                         |
|---------------------------|----------------|----------------|----------------|----------------|----------------|----------------|---------------------------|---------------------------|---------------------------|---------------------------|
|Displayed damage per second|920             |980             |1050            |1110            |1190            |1270            |1620                       |1740                       |1850                       |1980                       |
|Name                       |T7-E Speederbike|T7-E Speederbike|T7-E Speederbike|T7-E Speederbike|T7-E Speederbike|T7-E Speederbike|Empire Speeder Bike Upgrade|Empire Speeder Bike Upgrade|Empire Speeder Bike Upgrade|Empire Speeder Bike Upgrade|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |130101|130102|130103|130104|130105|130106|130107|130108|130109|130110|
|Point value|6     |7.200 |8.400 |9.600 |10.800|12    |13.200|14.400|15.600|18    |


