---
title: AT-AT (ATAT)
category: unit
---

# AT-AT (ATAT)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 30
  * Type: vehicle

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|22000|26400|30800|35200|39600|44000|48400|52800|57200|66000|


|Level |11   |
|------|-----|
|Health|71280|


### Training stats

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|3m30s                          |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |6m40s                                  |7m10s                                  |7m40s                                   |
|Training cost|1500$                          |2100$                                  |2700$                                  |3300$                                  |3900$                                  |4500$                                  |5100$                                  |6000$                                  |6300$                                  |6900$                                   |
|Building     |[Factory 5](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


|Level        |11                                      |
|-------------|----------------------------------------|
|Training time|8m10s                                   |
|Training cost|7500$                                   |
|Building     |[Research Lab 11](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |1h30m|3h   |8h    |1d    |3d    |5d     |1w     |1w3d   |2w      |2w      |
|Upgrade requirements|4300$|5000$|10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|


|Level               |11      |
|--------------------|--------|
|Upgrade time        |2w      |
|Upgrade requirements|4250000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: Yes
  * Flying unit: No
  * Max speed: 10
  * Propensity to go around obstacles: 200
  * Rotation speed: 0.982
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2

## Main attack : ATAT

### Targeting

  * Attack shield border: Yes
  * Max attack range: 9
  * Min attack range: 1
  * New rotation speed: 982
  * Target preference strength: 90
  * Target preferences: **Shield (80)**, **Shield generator (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Animation delay: 0s
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,1,1,1
  * Impact delay: 500ms
  * Can shoot over walls: Yes
  * Reload time: 1.500s
  * Retargeting offset: 18
  * Self-centered targeting: No
  * Shot count: 8
  * Shot delay: 250ms
  * Target locking: No

|Level          |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|---|---|----|----|----|----|----|----|----|----|
|Damage per shot|750|900|1050|1200|1350|1500|1650|1800|1950|2250|


|Level          |11  |
|---------------|----|
|Damage per shot|2430|


### Projectile

|Level                       |1   |2   |3   |4   |5    |6    |7    |8    |9    |10   |
|----------------------------|----|----|----|----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |1600|1920|2240|2560|2880 |3200 |3520 |3840 |4160 |4800 |
|Calculated damage per second|2666|3200|3733|4266|4800 |5333 |5866 |6400 |6933 |8000 |
|Calculated damage per cycle |6000|7200|8400|9600|10800|12000|13200|14400|15600|18000|


|Level                       |11   |
|----------------------------|-----|
|Displayed damage per second |5184 |
|Calculated damage per second|8640 |
|Calculated damage per cycle |19440|


  * Cannons per sequence: 4
  * Shooting cycle duration: 2.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Shield, Shield generator, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ATAT

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: atat_emp-ani
  * Audio attack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * Audio death: "sfx_death_walker_1":100
  * Audio placement: "sfx_placement_empire_atat_1":100
  * Buff asset offset: 0,4.00,0.00
  * Bullet: fx_blaster_beam_r_med
  * Bundle name: atat_emp-ani
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: shieldGenerator
  * Gun position: "atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun1":1,"atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun2":1,"atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun3":1,"atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun4":1
  * Hit spark: fx_blaster_hit_r_med
  * Icon camera position: 41.83,40.55,52.41
  * Icon lookat position: -2.01,3.9,-0.8
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_med
  * Name: ATAT
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|1600       |1920       |2240       |2560       |2880       |3200       |3520       |3840       |4160       |4800       |
|Prestige                   |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


|Level                      |11                           |
|---------------------------|-----------------------------|
|Deploy vfx                 |vfx_prestige_deploy_large_emp|
|Displayed damage per second|5184                         |
|Prestige                   |true                         |


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

|Level      |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |80501|80502|80503|80504|80505|80506|80507|80508|80509|80510|
|Point value|30   |36   |42   |48   |54   |60   |66   |72   |78   |90   |


|Level      |11   |
|-----------|-----|
|Order      |80511|
|Point value|90   |


