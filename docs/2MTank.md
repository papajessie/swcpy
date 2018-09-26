---
title: 2-M Hover Tank (2MTank)
category: unit
---

# 2-M Hover Tank (2MTank)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 10
  * Type: vehicle

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|14000|16800|19600|22400|25200|28000|30800|33600|36400|42000|


|Level |11   |
|------|-----|
|Health|45360|


### Training stats

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|3m20s                          |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |4m40s                                  |4m50s                                  |5m                                      |
|Training cost|500$                           |700$                                   |900$                                   |1100$                                  |1300$                                  |1500$                                  |1700$                                  |2000$                                  |2100$                                  |2300$                                   |
|Building     |[Factory 3](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


|Level        |11                                      |
|-------------|----------------------------------------|
|Training time|5m10s                                   |
|Training cost|2500$                                   |
|Building     |[Research Lab 11](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |1h   |2h30m|7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Upgrade requirements|2900$|3000$|6000$|15000$|35000$|115000$|200000$|385000$|1250000$|2250000$|


|Level               |11      |
|--------------------|--------|
|Upgrade time        |2w      |
|Upgrade requirements|4250000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 2
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x3

## Main attack : 2MTank

### Targeting

  * Attack shield border: No
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 2000
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0
  * Charge time: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Reload time: 2s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 4
  * Shot delay: 200ms
  * Target locking: No

|Level          |1  |2  |3  |4  |5  |6  |7   |8   |9   |10  |
|---------------|---|---|---|---|---|---|----|----|----|----|
|Damage per shot|499|599|699|798|898|998|1098|1197|1297|1497|


|Level          |11  |
|---------------|----|
|Damage per shot|1617|


### Projectile

  * Splash damage percentages: 100,50

|Level                       |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |700 |840 |981 |1120|1260|1400|1541|1680|1820|2101|
|Calculated damage per second|654 |785 |916 |1046|1177|1308|1440|1569|1700|1963|
|Calculated damage per cycle |1996|2396|2796|3192|3592|3992|4392|4788|5188|5988|


|Level                       |11  |
|----------------------------|----|
|Displayed damage per second |2269|
|Calculated damage per second|2120|
|Calculated damage per cycle |6468|


  * Cannons per sequence: 1
  * Shooting cycle duration: 3.050s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(50)**: Flying infantry, Flying vehicle, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(25)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero
  * Pass through shield: No
  * Salvos: 4

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: 2MTank

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: replrtnk_emp-ani
  * Audio attack: "sfx_attack_tank_1":25,"sfx_attack_tank_2":25,"sfx_attack_tank_3":25,"sfx_attack_tank_4":25
  * Audio death: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * Audio placement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * Buff asset offset: 0.0,1.14,0.0
  * Bullet: fx_blaster_beam_r_lrg
  * Bundle name: replrtnk_emp-ani
  * Factory rotation: 0
  * Factory scale factor: 0.842999999999999971578290569595992565155029296875
  * Favorite target type: turret
  * Gun position: "replrtnk_emp_rig_MASTER_MOVER/replrtnk_emp_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_r_lrg
  * Icon camera position: 30.83,30.71,28.35
  * Icon lookat position: -0.22,1.4,-0.74
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_lrg
  * Name: 2MTank
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|700        |840        |981        |1120       |1260       |1400       |1541       |1680       |1820       |2101       |
|Prestige                   |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


|Level                      |11                           |
|---------------------------|-----------------------------|
|Deploy vfx                 |vfx_prestige_deploy_large_emp|
|Displayed damage per second|2269                         |
|Prestige                   |true                         |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 3
  * Auto spawn spreading scale: 3
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |80301|80302|80303|80304|80305|80306|80307|80308|80309|80310|
|Point value|10   |12   |14   |16   |18   |20   |22   |24   |26   |30   |


|Level      |11   |
|-----------|-----|
|Order      |80311|
|Point value|30   |


