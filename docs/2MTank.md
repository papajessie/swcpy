---
title: 2-M Hover Tank (2MTank)
category: unit
---

# 2-M Hover Tank (2MTank) — version 1098

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

|Level |5    |3    |1    |9    |6    |10   |8    |4    |2    |7    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|25200|19600|14000|36400|28000|42000|33600|22400|16800|30800|


### Training stats

|Level        |5                                      |3                                      |1                              |9                                      |6                                      |10                                      |8                                      |4                                      |2                                      |7                                      |
|-------------|---------------------------------------|---------------------------------------|-------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|4m10s                                  |3m50s                                  |3m20s                          |4m50s                                  |4m20s                                  |5m                                      |4m40s                                  |4m                                     |3m40s                                  |4m30s                                  |
|Training cost|1300$                                  |900$                                   |500$                           |2100$                                  |1500$                                  |2300$                                   |2000$                                  |1100$                                  |700$                                   |1700$                                  |
|Building     |[Research Lab 5](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Factory 3](empireFactory.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|


### Upgrading stats

|Level               |5     |3    |1    |9       |6      |10      |8      |4     |2    |7      |
|--------------------|------|-----|-----|--------|-------|--------|-------|------|-----|-------|
|Upgrade time        |20h   |2h30m|0s   |1w1d    |2d12h  |1w5d    |6d     |7h    |1h   |4d     |
|Upgrade requirements|35000$|6000$|2900$|1250000$|115000$|2250000$|385000$|15000$|3000$|200000$|


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

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 4
  * Time between shots: 200ms
  * Target locking: No

|Level          |5  |3  |1  |9   |6  |10  |8   |4  |2  |7   |
|---------------|---|---|---|----|---|----|----|---|---|----|
|Damage per shot|898|699|499|1297|998|1497|1197|798|599|1098|


### Projectile

  * Splash damage percentages: 100,50

|Level                       |5       |3      |1      |9       |6       |10      |8   |4   |2      |7       |
|----------------------------|--------|-------|-------|--------|--------|--------|----|----|-------|--------|
|Displayed damage per second |1260    |981    |700    |1820    |1400    |2101    |1680|1120|840    |1541    |
|Calculated damage per second|1260.351|981.053|700.351|1820.351|1400.702|2101.053|1680|1120|840.702|1541.053|


  * Cannons per sequence: 1
  * Cliptime: 2.850s
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

  * Animation delay: 0
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

|Level                      |5   |3  |1  |9   |6   |10  |8   |4   |2  |7   |
|---------------------------|----|---|---|----|----|----|----|----|---|----|
|Displayed damage per second|1260|981|700|1820|1400|2101|1680|1120|840|1541|


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

|Level      |5     |3     |1     |9     |6     |10    |8     |4     |2     |7     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |130305|130303|130301|130309|130306|130310|130308|130304|130302|130307|
|Point value|18    |14    |10    |26    |20    |30    |24    |16    |12    |22    |


