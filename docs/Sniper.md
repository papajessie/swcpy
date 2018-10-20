---
title: Sniper Trooper (Sniper)
category: unit
---

# Sniper Trooper (Sniper)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 7
  * Type: infantry

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2800|3360|3920|4480|5040|5600|6160|6720|7280|8400|


|Level |11  |
|------|----|
|Health|9072|


### Training stats

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|2m48s                            |2m56s                                  |3m4s                                   |3m12s                                  |3m20s                                  |3m28s                                  |3m36s                                  |3m16s                                  |3m23s                                  |3m30s                                   |
|Training cost|350$                             |490$                                   |630$                                   |770$                                   |910$                                   |1050$                                  |1190$                                  |1400$                                  |1470$                                  |1610$                                   |
|Building     |[Barracks 7](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


|Level        |11                                      |
|-------------|----------------------------------------|
|Training time|3m37s                                   |
|Training cost|1750$                                   |
|Building     |[Research Lab 11](empireOffenseLab.html)|


### Upgrading stats

|Level               |1   |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s  |45m  |2h   |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Upgrade requirements|700$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


|Level               |11      |
|--------------------|--------|
|Upgrade time        |1w3d    |
|Upgrade requirements|4000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : projectileSniper

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (60)**, **Flying infantry (60)**, **Heavy infantry (60)**, **Infantry (60)**, **Support troop (60)**, Flying vehicle (50), Headquarters (50), Heavy vehicle (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0
  * Charge time: 250ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Reload time: 2s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 3
  * Shot delay: 500ms
  * Target locking: No

|Level          |1  |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|---|----|----|----|----|----|----|----|----|----|
|Damage per shot|835|1001|1168|1335|1502|1669|1836|2002|2169|2503|


|Level          |11  |
|---------------|----|
|Damage per shot|2703|


### Projectile

  * Splash damage percentages: 100

|Level                       |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |770 |924 |1078|1232|1386|1540|1694|1848|2002|2310|
|Calculated damage per second|770 |924 |1078|1232|1386|1540|1694|1848|2002|2310|
|Calculated damage per cycle |2505|3003|3504|4005|4506|5007|5508|6006|6507|7509|


|Level                       |11  |
|----------------------------|----|
|Displayed damage per second |2430|
|Calculated damage per second|2495|
|Calculated damage per cycle |8109|


  * Cannons per sequence: 1
  * Shooting cycle duration: 3.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(300)**: Flying infantry, Infantry, Infantry hero, Support troop, **(250)**: Heavy infantry, Heavy infantry hero, **(200)**: Flying vehicle, Light vehicle, Vehicule hero, **(150)**: Heavy vehicle, Heavy vehicule hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(50)**: Shield, Shield generator, **(40)**: Wall
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Sniper

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: snipertrooper_emp-ani
  * Audio attack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: snipertrooper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Gun position: "snipertrooper_emp_rig_MASTER_MOVER/snipertrooper_emp_rig_locator_gun_Rt":1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 8.4,11.02,18.74
  * Icon closeup camera position: -0.07,3.69,9.81
  * Icon closeup lookat position: 0.08,2.6,-0.81
  * Icon lookat position: -0.36,1.69,0.24
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: projectileSniper
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|770        |924        |1078       |1232       |1386       |1540       |1694       |1848       |2002       |2310       |
|Favorite target type       |infantry   |infantry   |infantry   |infantry   |infantry   |infantry   |infantry   |infantry   |infantry   |infantry   |
|Prestige                   |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


|Level                      |11                           |
|---------------------------|-----------------------------|
|Deploy vfx                 |vfx_prestige_deploy_small_emp|
|Displayed damage per second|2430                         |
|Favorite target type       |heroes                       |
|Prestige                   |true                         |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: No
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1    |2    |3    |4     |5     |6    |7     |8     |9     |10   |
|-----------|-----|-----|-----|------|------|-----|------|------|------|-----|
|Order      |60701|60702|60703|60704 |60705 |60706|60707 |60708 |60709 |60710|
|Point value|7    |8.400|9.800|11.200|12.600|14   |15.400|16.800|18.200|21   |


|Level      |11   |
|-----------|-----|
|Order      |60711|
|Point value|21   |


