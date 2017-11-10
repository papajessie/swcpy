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

|Level |3    |5    |7    |6    |2    |10   |9    |4    |8    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|12080|13520|15160|14320|11420|18050|17030|12780|16070|10800|


### Training stats

|Level        |3                                      |5                                      |7                                      |6                                      |2                                      |10                                      |9                                      |4                                      |8                                      |1                              |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|-------------------------------|
|Training time|4m4s                                   |4m10s                                  |4m30s                                  |4m20s                                  |4m2s                                   |7m30s                                   |7m15s                                  |4m7s                                   |7m                                     |4m                             |
|Training cost|1790$                                  |1950$                                  |2550$                                  |2250$                                  |1720$                                  |3450$                                   |3150$                                  |1870$                                  |3000$                                  |1650$                          |
|Building     |[Research Lab 3](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Factory 4](empireFactory.html)|


### Upgrading stats

|Level               |3     |5     |7      |6      |2    |10      |9       |4     |8      |1    |
|--------------------|------|------|-------|-------|-----|--------|--------|------|-------|-----|
|Upgrade time        |2h30m |20h   |4d     |2d12h  |1h   |2w      |1w1d    |7h    |6d     |0s   |
|Upgrade requirements|10000$|50000$|225000$|135000$|5000$|2500000$|1500000$|20000$|450000$|5000$|


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

|Level          |3   |5   |7   |6   |2   |10  |9   |4   |8   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2580|2890|3240|3060|2440|3850|3630|2730|3430|2310|


### Projectile

|Level                       |3       |5       |7       |6       |2       |10      |9       |4       |8       |1       |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |3620    |4060    |4550    |4290    |3420    |5400    |5090    |3830    |4810    |3240    |
|Calculated damage per second|3621.053|4056.140|4547.368|4294.737|3424.561|5403.509|5094.737|3831.579|4814.035|3242.105|


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

|Level                      |3   |5   |7   |6   |2   |10  |9   |4   |8   |1   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|3620|4060|4550|4290|3420|5400|5090|3830|4810|3240|


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

|Level      |3     |5     |7     |6     |2     |10    |9     |4     |8     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |130403|130405|130407|130406|130402|130410|130409|130404|130408|130401|
|Point value|21    |27    |33    |30    |18    |45    |39    |24    |36    |15    |


