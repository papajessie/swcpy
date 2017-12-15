---
title: Speeder Bike (RebelSpeeder)
category: unit
---

# Speeder Bike (RebelSpeeder) — version 1106

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: vehicle

|Level |1   |2   |3    |4    |5    |6    |7    |8    |9    |10   |
|------|----|----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|9000|9700|10450|11280|12170|13140|14210|15360|16620|18000|


### Training stats

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|2m24s                         |2m25s                                 |2m26s                                 |2m28s                                 |2m30s                                 |2m36s                                 |2m42s                                 |2m48s                                 |2m54s                                 |3m                                     |
|Training cost|550$                          |570$                                  |590$                                  |620$                                  |650$                                  |750$                                  |850$                                  |1000$                                 |1050$                                 |1150$                                  |
|Building     |[Factory 1](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |30m  |1h30m|5h    |10h   |1d12h  |2d12h  |4d     |6d      |1w2d    |
|Upgrade requirements|3000$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


### Movement stats

  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 15
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

|Level       |1-6|7-10|
|------------|---|----|
|Acceleration|0  |8   |
|Max speed   |40 |80  |


## Main attack : T7-V Speederbike / Rebel Speeder Bike Upgrade

### Targeting

  * Attack shield border: No
  * Max attack range: 6
  * Min attack range: 0
  * New rotation speed: 3927
  * Target preference strength: 90
  * Target preferences: **Droideka (70)**, **Flying infantry (70)**, **Flying vehicle (70)**, **Heavy infantry (70)**, **Heavy vehicle (70)**, **Infantry (70)**, **Light vehicle (70)**, **Support troop (70)**, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Clip retargeting: Yes
  * Gun shooting sequence: 1,2
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 1s
  * Retargeting offset: 12
  * Self-centered targeting: No
  * Shot count: 2
  * Time between shots: 250ms
  * Target locking: No

|Level                                    |1   |2   |3   |4   |5   |6   |7    |8    |9    |10   |
|-----------------------------------------|----|----|----|----|----|----|-----|-----|-----|-----|
|Time between start of clip and first shot|1s  |1s  |1s  |1s  |1s  |1s  |500ms|500ms|500ms|500ms|
|Damage per shot                          |1010|1050|1090|1140|1180|1230|1280 |1330 |1380 |1440 |


### Projectile

|Level                       |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |900 |930 |970 |1010|1050|1090|1460|1520|1580|1650|
|Calculated damage per second|897 |933 |968 |1013|1048|1093|1462|1520|1577|1645|
|Calculated damage per clip  |2020|2100|2180|2280|2360|2460|2560|2660|2760|2880|


  * Cannons per sequence: 2
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Pass through shield: No
  * Salvos: 2

|Level             |1-6                                                                                                                                                                                                                                                                                                                                                    |7-10                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Cliptime          |2.250s                                                                                                                                                                                                                                                                                                                                                 |1.750s                                                                                                                                                                                                                                                                                                                                                                                          |
|Damage multipliers|**(150)**: Flying infantry, Infantry, Infantry hero, Support troop, **(125)**: Heavy infantry, Heavy infantry hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(75)**: Flying vehicle, Light vehicle, Vehicule hero, **(50)**: Heavy vehicle, Heavy vehicule hero|**(250)**: Flying infantry, Infantry, Support troop, **(225)**: Flying vehicle, Light vehicle, **(200)**: Heavy vehicle, **(175)**: Heavy infantry, **(100)**: Droideka, Heavy infantry hero, Heavy vehicule hero, Infantry hero, Vehicule hero, **(75)**: Wall, **(50)**: Headquarters, **(25)**: Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Trap|


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RebelSpeeder

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: speederbike_rbl-ani
  * Audio attack: "sfx_attack_empire_mtv7_1":25,"sfx_attack_empire_mtv7_2":25,"sfx_attack_empire_mtv7_3":25,"sfx_attack_empire_mtv7_4":25
  * Audio death: "sfx_death_empire_mtv7_1":33,"sfx_death_empire_mtv7_2":33,"sfx_death_empire_mtv7_3":34
  * Audio placement: "sfx_placement_empire_mtv7_1":50,"sfx_placement_empire_mtv7_2":50
  * Buff asset offset: 0,1,0
  * Bullet: fx_blaster_beam_b_med
  * Bundle name: speederbike_rbl-ani
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Gun position: "speederbike_rbl_rig_MASTER_MOVER/speederbike_rbl_rig_locator_gun1":1,"speederbike_rbl_rig_MASTER_MOVER/speederbike_rbl_rig_locator_gun2":2
  * Hit spark: fx_blaster_hit_b_med
  * Icon camera position: 14.18,12.02,20.78
  * Icon lookat position: -0.23,1.14,-0.58
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_med
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1               |2               |3               |4               |5               |6               |7                         |8                         |9                         |10                        |
|---------------------------|----------------|----------------|----------------|----------------|----------------|----------------|--------------------------|--------------------------|--------------------------|--------------------------|
|Displayed damage per second|900             |930             |970             |1010            |1050            |1090            |1460                      |1520                      |1580                      |1650                      |
|Name                       |T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|


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
|Order      |230101|230102|230103|230104|230105|230106|230107|230108|230109|230110|
|Point value|5     |6     |7     |8     |9     |10    |11    |12    |13    |15    |


