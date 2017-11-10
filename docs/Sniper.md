---
title: Sniper Trooper (Sniper)
category: unit
---

# Sniper Trooper (Sniper) — version 1098

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

|Level |4   |9   |6   |1   |8   |5   |10  |2   |7   |3   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|4480|7280|5600|2800|6720|5040|8400|3360|6160|3920|


### Training stats

|Level        |4                                      |9                                      |6                                      |1                                |8                                      |5                                      |10                                      |2                                      |7                                      |3                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|3m12s                                  |3m23s                                  |3m28s                                  |2m48s                            |3m16s                                  |3m20s                                  |3m30s                                   |2m56s                                  |3m36s                                  |3m4s                                   |
|Training cost|770$                                   |1470$                                  |1050$                                  |350$                             |1400$                                  |910$                                   |1610$                                   |490$                                   |1190$                                  |630$                                   |
|Building     |[Research Lab 4](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Barracks 7](empireBarracks.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|


### Upgrading stats

|Level               |4     |9       |6      |1   |8      |5     |10      |2    |7      |3    |
|--------------------|------|--------|-------|----|-------|------|--------|-----|-------|-----|
|Upgrade time        |6h    |1w      |2d     |0s  |5d     |12h   |1w3d    |45m  |3d     |2h   |
|Upgrade requirements|15000$|1000000$|115000$|700$|350000$|35000$|2000000$|3000$|175000$|6000$|


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

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 500ms
  * Target locking: No

|Level          |4   |9   |6   |1  |8   |5   |10  |2   |7   |3   |
|---------------|----|----|----|---|----|----|----|----|----|----|
|Damage per shot|1335|2169|1669|835|2002|1502|2503|1001|1836|1168|


### Projectile

  * Splash damage percentages: 100

|Level                       |4       |9       |6       |1      |8   |5       |10      |2  |7       |3       |
|----------------------------|--------|--------|--------|-------|----|--------|--------|---|--------|--------|
|Displayed damage per second |1232    |2002    |1540    |770    |1848|1386    |2310    |924|1694    |1078    |
|Calculated damage per second|1232.308|2002.154|1540.615|770.769|1848|1386.462|2310.462|924|1694.769|1078.154|


  * Cannons per sequence: 1
  * Cliptime: 3.250s
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

  * Animation delay: 0
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
  * Favorite target type: heroes
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

|Level                      |4   |9   |6   |1  |8   |5   |10  |2  |7   |3   |
|---------------------------|----|----|----|---|----|----|----|---|----|----|
|Displayed damage per second|1232|2002|1540|770|1848|1386|2310|924|1694|1078|


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

|Level      |4     |9     |6     |1     |8     |5     |10    |2     |7     |3     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120704|120709|120706|120701|120708|120705|120710|120702|120707|120703|
|Point value|11.200|18.200|14    |7     |16.800|12.600|21    |8.400 |15.400|9.800 |


