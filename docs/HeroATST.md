---
title: Veteran AT-ST (HeroATST)
category: unit
---

# Veteran AT-ST (HeroATST)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: hero

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|16000|19200|22400|25600|28800|32000|35200|38400|41600|48000|


|Level |11   |
|------|-----|
|Health|51840|


### Training stats

|Level        |1                                           |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|3m30s                                       |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |4m40s                                  |4m50s                                  |5m                                      |
|Training cost|1000$                                       |1400$                                  |1800$                                  |2200$                                  |2600$                                  |3000$                                  |3400$                                  |4000$                                  |4200$                                  |4600$                                   |
|Building     |[Hero Command 1](empireTacticalCommand.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


|Level        |11                                      |
|-------------|----------------------------------------|
|Training time|5m10s                                   |
|Training cost|5000$                                   |
|Building     |[Research Lab 11](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |1h   |2h30m |7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Upgrade requirements|1500$|5000$|10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|


|Level               |11      |
|--------------------|--------|
|Upgrade time        |2w      |
|Upgrade requirements|4250000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x2

## Main attack : HeroATST

### Targeting

  * Attack shield border: No
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0
  * Charge time: 1s
  * Clip retargeting: No
  * Gun shooting sequence: 1,2
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Reload time: 2s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 10
  * Shot delay: 250ms
  * Target locking: No

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|1575|1890|2205|2520|2835|3150|3465|3780|4095|4725|


|Level          |11  |
|---------------|----|
|Damage per shot|5103|


### Projectile

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |3000 |3600 |4200 |4800 |5400 |6000 |6600 |7200 |7800 |9000 |
|Calculated damage per second|3000 |3600 |4200 |4800 |5400 |6000 |6600 |7200 |7800 |9000 |
|Calculated damage per cycle |15750|18900|22050|25200|28350|31500|34650|37800|40950|47250|


|Level                       |11   |
|----------------------------|-----|
|Displayed damage per second |9480 |
|Calculated damage per second|9720 |
|Calculated damage per cycle |51030|


  * Cannons per sequence: 2
  * Shooting cycle duration: 5.250s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, **(80)**: Wall
  * Pass through shield: No
  * Salvos: 10

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: HeroATST

|Level    |1    |2    |3    |4    |5    |6    |7    |8    |9    |10-11 |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
|Hero data|hero1|hero2|hero3|hero4|hero5|hero6|hero7|hero8|hero9|hero10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: atsthero_emp-ani
  * Audio attack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * Audio death: "sfx_death_walker_1":100
  * Audio placement: "sfx_placement_hero":100
  * Buff asset offset: 0.00,2.83,0.0
  * Bundle name: atsthero_emp-ani
  * Decal asset name: tac_hero_emp
  * Decal bundle name: tac_hero_emp
  * Decal size: 240
  * Effect type: 2
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "atsthero_emp_rig_MASTER_MOVER/atsthero_emp_rig_locator_gun1":1,"atsthero_emp_rig_MASTER_MOVER/atsthero_emp_rig_locator_gun2":2
  * Hit spark: fx_gatling_hit_r_lrg
  * Hologram uid: HeroHologramEmpire1
  * Icon camera position: 19.84,22.71,46.64
  * Icon lookat position: -0.02,3.29,0.19
  * Max scale: 100
  * Muzzle flash: fx_gatling_muzzle_r_lrg
  * Name: HeroATST
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|3000       |3600       |4200       |4800       |5400       |6000       |6600       |7200       |7800       |9000       |
|Prestige                   |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


|Level                      |11                           |
|---------------------------|-----------------------------|
|Deploy vfx                 |vfx_prestige_deploy_large_emp|
|Displayed damage per second|9480                         |
|Prestige                   |true                         |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 0
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|-----------|---|---|---|---|---|---|---|---|---|---|
|Order      |101|102|103|104|105|106|107|108|109|110|
|Point value|20 |24 |28 |32 |36 |40 |44 |48 |52 |60 |


|Level      |11 |
|-----------|---|
|Order      |111|
|Point value|60 |


