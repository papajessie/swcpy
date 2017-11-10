---
title: Speeder Bike (RebelSpeeder)
category: unit
---

# Speeder Bike (RebelSpeeder) — version 1098

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

|Level |8    |4    |2   |6    |1   |5    |3    |10   |7    |9    |
|------|-----|-----|----|-----|----|-----|-----|-----|-----|-----|
|Health|15360|11280|9700|13140|9000|12170|10450|18000|14210|16620|


### Training stats

|Level        |8                                     |4                                     |2                                     |6                                     |1                             |5                                     |3                                     |10                                     |7                                     |9                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|
|Training time|2m48s                                 |2m28s                                 |2m25s                                 |2m36s                                 |2m24s                         |2m30s                                 |2m26s                                 |3m                                     |2m42s                                 |2m54s                                 |
|Training cost|1000$                                 |620$                                  |570$                                  |750$                                  |550$                          |650$                                  |590$                                  |1150$                                  |850$                                  |1050$                                 |
|Building     |[Research Lab 8](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Factory 1](rebelFactory.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|


### Upgrading stats

|Level               |8      |4     |2    |6      |1    |5     |3    |10      |7      |9       |
|--------------------|-------|------|-----|-------|-----|------|-----|--------|-------|--------|
|Upgrade time        |4d     |5h    |30m  |1d12h  |0s   |10h   |1h30m|1w2d    |2d12h  |6d      |
|Upgrade requirements|350000$|15000$|3000$|115000$|3000$|35000$|6000$|2000000$|175000$|1000000$|


### Movement stats

  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 15
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

|Level       |8 |4, 2, 6, 1, 5, 3|10, 7, 9|
|------------|--|----------------|--------|
|Acceleration|8 |0               |8       |
|Max speed   |80|40              |80      |


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

|Level                                    |8    |4   |2   |6   |1   |5   |3   |10   |7    |9    |
|-----------------------------------------|-----|----|----|----|----|----|----|-----|-----|-----|
|Time between start of clip and first shot|500ms|1s  |1s  |1s  |1s  |1s  |1s  |500ms|500ms|500ms|
|Damage per shot                          |1330 |1140|1050|1230|1010|1180|1090|1440 |1280 |1380 |


### Projectile

|Level                       |8   |4       |2      |6       |1      |5       |3      |10      |7       |9       |
|----------------------------|----|--------|-------|--------|-------|--------|-------|--------|--------|--------|
|Displayed damage per second |1520|1010    |930    |1090    |900    |1050    |970    |1650    |1460    |1580    |
|Calculated damage per second|1520|1013.333|933.333|1093.333|897.778|1048.889|968.889|1645.714|1462.857|1577.143|


  * Cannons per sequence: 2
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Pass through shield: No
  * Salvos: 2

|Level             |8                                                                                                                                                                                                                                                                                                                                                                                               |4, 2, 6, 1, 5, 3                                                                                                                                                                                                                                                                                                                                       |10, 7, 9                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Cliptime          |1.750s                                                                                                                                                                                                                                                                                                                                                                                          |2.250s                                                                                                                                                                                                                                                                                                                                                 |1.750s                                                                                                                                                                                                                                                                                                                                                                                          |
|Damage multipliers|**(250)**: Flying infantry, Infantry, Support troop, **(225)**: Flying vehicle, Light vehicle, **(200)**: Heavy vehicle, **(175)**: Heavy infantry, **(100)**: Droideka, Heavy infantry hero, Heavy vehicule hero, Infantry hero, Vehicule hero, **(75)**: Wall, **(50)**: Headquarters, **(25)**: Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Trap|**(150)**: Flying infantry, Infantry, Infantry hero, Support troop, **(125)**: Heavy infantry, Heavy infantry hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(75)**: Flying vehicle, Light vehicle, Vehicule hero, **(50)**: Heavy vehicle, Heavy vehicule hero|**(250)**: Flying infantry, Infantry, Support troop, **(225)**: Flying vehicle, Light vehicle, **(200)**: Heavy vehicle, **(175)**: Heavy infantry, **(100)**: Droideka, Heavy infantry hero, Heavy vehicule hero, Infantry hero, Vehicule hero, **(75)**: Wall, **(50)**: Headquarters, **(25)**: Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Trap|


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

|Level                      |8                         |4               |2               |6               |1               |5               |3               |10                        |7                         |9                         |
|---------------------------|--------------------------|----------------|----------------|----------------|----------------|----------------|----------------|--------------------------|--------------------------|--------------------------|
|Displayed damage per second|1520                      |1010            |930             |1090            |900             |1050            |970             |1650                      |1460                      |1580                      |
|Name                       |Rebel Speeder Bike Upgrade|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|


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

|Level      |8     |4     |2     |6     |1     |5     |3     |10    |7     |9     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |230108|230104|230102|230106|230101|230105|230103|230110|230107|230109|
|Point value|12    |8     |6     |10    |5     |9     |7     |15    |11    |13    |


