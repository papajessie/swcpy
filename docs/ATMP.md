---
title: AT-MP (ATMP)
category: unit
---

# AT-MP (ATMP) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 15
  * Type: vehicle

|Level |10   |5    |3    |9    |2    |4    |1    |8    |7    |6    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|18050|13520|12080|17030|11420|12780|10800|16070|15160|14320|


### Training stats

|Level        |10                                      |5                                      |3                                      |9                                      |2                                      |4                                      |1                              |8                                      |7                                      |6                                      |
|-------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|7m30s                                   |4m10s                                  |4m4s                                   |7m15s                                  |4m2s                                   |4m7s                                   |4m                             |7m                                     |4m30s                                  |4m20s                                  |
|Training cost|3450$                                   |1950$                                  |1790$                                  |3150$                                  |1720$                                  |1870$                                  |1650$                          |3000$                                  |2550$                                  |2250$                                  |
|Building     |[Research Lab 10](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Factory 4](empireFactory.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|


### Upgrading stats

|Level               |10      |5     |3     |9       |2    |4     |1    |8      |7      |6      |
|--------------------|--------|------|------|--------|-----|------|-----|-------|-------|-------|
|Upgrade time        |2w      |20h   |2h30m |1w1d    |1h   |7h    |0s   |6d     |4d     |2d12h  |
|Upgrade requirements|2500000$|50000$|10000$|1500000$|5000$|20000$|5000$|450000$|225000$|135000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 2
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x1

## Main attack : ATMP

### Targeting

  * Attack shield border: Yes
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 2000
  * Target preference strength: 90
  * Target preferences: **Shield (90)**, **Shield generator (90)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 10

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,3,5,2,4,6
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 4
  * Time between shots: 200ms
  * Target locking: No

|Level          |10  |5   |3   |9   |2   |4   |1   |8   |7   |6   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|3850|2890|2580|3630|2440|2730|2310|3430|3240|3060|


### Projectile

|Level                       |10      |5       |3       |9       |2       |4       |1       |8       |7       |6       |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |5400    |4060    |3620    |5090    |3420    |3830    |3240    |4810    |4550    |4290    |
|Calculated damage per second|5403.509|4056.140|3621.053|5094.737|3424.561|3831.579|3242.105|4814.035|4547.368|4294.737|


  * Cannons per sequence: 6
  * Cliptime: 2.850s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 12
  * Damage multipliers: **(400)**: Shield, Shield generator, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(60)**: Wall
  * Pass through shield: No
  * Salvos: 4

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ATMP

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: atmp_emp-ani
  * Audio attack: "sfx_attack_empire_atmp_1":35,"sfx_attack_empire_atmp_2":35,"sfx_attack_empire_atmp_3":30
  * Audio death: "sfx_death_empire_atmp_1":100
  * Audio impact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * Audio placement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * Buff asset offset: 0.00,3.0,0.00
  * Bullet: fx_rocket_projectile_r_sm
  * Bundle name: atmp_emp-ani
  * Factory rotation: -90
  * Factory scale factor: 0.8910000000000000142108547152020037174224853515625
  * Favorite target type: shieldGenerator
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_rocket_hit_r_sm
  * Icon camera position: 22.45,15.49,39.24
  * Icon lookat position: -0.73,2.62,-0.75
  * Max scale: 100
  * Muzzle flash: fx_rocket_muzzle_r_sm
  * Name: ATMP
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10  |5   |3   |9   |2   |4   |1   |8   |7   |6   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|5400|4060|3620|5090|3420|3830|3240|4810|4550|4290|


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

|Level      |10    |5     |3     |9     |2     |4     |1     |8     |7     |6     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |130410|130405|130403|130409|130402|130404|130401|130408|130407|130406|
|Point value|45    |27    |21    |39    |18    |24    |15    |36    |33    |30    |


