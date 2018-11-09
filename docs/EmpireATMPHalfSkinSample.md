---
title: Enhanced AT-MP Walker (EmpireATMPHalfSkinSample)
category: unit
---

# Enhanced AT-MP Walker (EmpireATMPHalfSkinSample)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: No
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 15
  * Type: vehicle

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10-11|
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|12960|13820|14890|16160|17650|19390|21375|26265|29205|31725|


### Training stats

  * Training time: 0s
  * Training cost: Free

|Level   |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|--------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Building|[Factory 2](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


|Level   |11                                      |
|--------|----------------------------------------|
|Building|[Research Lab 11](empireOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: Nothing

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

## Main attack : Enhanced ATMP

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

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2803|3156|3509|3858|4220|4631|5054|5512|5977|6520|


|Level          |11  |
|---------------|----|
|Damage per shot|6903|


### Projectile

  * Splash damage percentages: 100,60,20

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |3935 |4430 |4925 |5415 |5925 |6500 |7095 |7735 |8390 |9150 |
|Calculated damage per second|5901 |6644 |7387 |8122 |8884 |9749 |10640|11604|12583|13726|
|Calculated damage per cycle |16818|18936|21054|23148|25320|27786|30324|33072|35862|39120|


|Level                       |11   |
|----------------------------|-----|
|Displayed damage per second |9690 |
|Calculated damage per second|14532|
|Calculated damage per cycle |41418|


  * Cannons per sequence: 6
  * Shooting cycle duration: 2.850s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 12
  * Damage multipliers: **(400)**: Shield generator, **(300)**: Shield, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 6

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EmpireATMPHalfSkinSample

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: atmphalfskin_emp-ani
  * Audio attack: "sfx_attack_empire_atmp_1":35,"sfx_attack_empire_atmp_2":35,"sfx_attack_empire_atmp_3":30
  * Audio death: "sfx_death_empire_atmp_1":100
  * Audio impact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * Audio placement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * Buff asset offset: 0.00,3.0,0.00
  * Bullet: fx_rocket_projectile_r_sm
  * Bundle name: atmphalfskin_emp-ani
  * Factory rotation: -90
  * Factory scale factor: 0.8910000000000000142108547152020037174224853515625
  * Favorite target type: shieldGenerator
  * Hit spark: fx_rocket_hit_r_med
  * Icon camera position: 18.67,18.09,40.97
  * Icon closeup camera position: 18.67,18.09,40.97
  * Icon closeup lookat position: -0.86,2.62,-1.35
  * Icon lookat position: -0.86,2.62,-1.35
  * Max scale: 100
  * Muzzle flash: fx_rocket_muzzle_r_sm
  * Name: Enhanced ATMP
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|3935       |4430       |4925       |5415       |5925       |6500       |7095       |7735       |8390       |9150       |
|Prestige                   |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


|Level                      |11  |
|---------------------------|----|
|Displayed damage per second|9690|
|Prestige                   |true|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level|1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order|81501|81502|81503|81504|81505|81506|81507|81508|81509|81510|


|Level|11   |
|-----|-----|
|Order|81511|


