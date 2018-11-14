---
title: AT-MP (ATMP)
category: unit
---

# AT-MP (ATMP)

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

|Level |11   |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|31725|29205|26265|23665|21375|19390|17650|16160|14890|13820|12960|


### Training stats

|Level        |11                                      |10                                      |9                                      |8                                      |7                                      |6                                      |5                                      |4                                      |3                                      |2                                      |1                              |
|-------------|----------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|-------------------------------|
|Training time|7m45s                                   |7m30s                                   |7m15s                                  |7m                                     |4m30s                                  |4m20s                                  |4m10s                                  |4m7s                                   |4m4s                                   |4m2s                                   |4m                             |
|Training cost|3750$                                   |3450$                                   |3150$                                  |3000$                                  |2550$                                  |2250$                                  |1950$                                  |1870$                                  |1790$                                  |1720$                                  |1650$                          |
|Building     |[Research Lab 11](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Factory 4](empireFactory.html)|


### Upgrading stats

|Level               |11      |10      |9       |8      |7      |6      |5     |4     |3     |2    |1    |
|--------------------|--------|--------|--------|-------|-------|-------|------|------|------|-----|-----|
|Upgrade time        |2w      |2w      |1w1d    |6d     |4d     |2d12h  |20h   |7h    |2h30m |1h   |0s   |
|Upgrade requirements|4250000$|2500000$|1500000$|450000$|225000$|135000$|50000$|20000$|10000$|5000$|5000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x1

## Main attack : ATMP

### Targeting

  * Attack shield border: Yes
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 3927
  * Target preference strength: 90
  * Target preferences: **Shield (90)**, **Shield generator (90)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 10

### Shooting

  * Animation delay: 0s
  * Charge time: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,3,5,2,4,6
  * Impact delay: 1s
  * Can shoot over walls: No
  * Reload time: 1.600s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 6
  * Shot delay: 200ms
  * Target locking: No

|Level          |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2655|2567|2420|2287|2160|2040|1927|1820|1720|1627|1540|


### Projectile

|Level                       |11   |10   |9    |8    |7    |6    |5    |4    |3    |2   |1   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|----|
|Displayed damage per second |5590 |5405 |5095 |4815 |4545 |4295 |4055 |3830 |3620 |3425|3240|
|Calculated damage per second|5589 |5404 |5094 |4814 |4547 |4294 |4056 |3831 |3621 |3425|3242|
|Calculated damage per cycle |15930|15402|14520|13722|12960|12240|11562|10920|10320|9762|9240|


  * Cannons per sequence: 6
  * Shooting cycle duration: 2.850s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 12
  * Damage multipliers: **(400)**: Shield, Shield generator, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(60)**: Wall
  * Pass through shield: No
  * Salvos: 6

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ATMP

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

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

|Level                      |11                           |10         |9          |8          |7          |6          |5          |4          |3          |2          |1          |
|---------------------------|-----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |vfx_prestige_deploy_large_emp|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|5590                         |5405       |5095       |4815       |4545       |4295       |4055       |3830       |3620       |3425       |3240       |
|Prestige                   |true                         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


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

|Level      |11   |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |80411|80410|80409|80408|80407|80406|80405|80404|80403|80402|80401|
|Point value|45   |45   |39   |36   |33   |30   |27   |24   |21   |18   |15   |


