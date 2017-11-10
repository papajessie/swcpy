---
title: Rebel Sharpshooter (Marksman)
category: unit
---

# Rebel Sharpshooter (Marksman) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 8
  * Type: infantry

|Level |7   |10  |4   |1   |2   |9   |6   |3   |5   |8   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|7040|9600|5120|3200|3840|8320|6400|4480|5760|7680|


### Training stats

|Level        |7                                     |10                                     |4                                     |1                               |2                                     |9                                     |6                                     |3                                     |5                                     |8                                     |
|-------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|1m21s                                 |4m                                     |1m12s                                 |1m3s                            |1m6s                                  |3m52s                                 |1m18s                                 |1m9s                                  |1m15s                                 |3m44s                                 |
|Training cost|1360$                                 |1840$                                  |880$                                  |400$                            |560$                                  |1680$                                 |1200$                                 |720$                                  |1040$                                 |1600$                                 |
|Building     |[Research Lab 7](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Barracks 7](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|


### Upgrading stats

|Level               |7      |10      |4     |1   |2    |9       |6      |3    |5     |8      |
|--------------------|-------|--------|------|----|-----|--------|-------|-----|------|-------|
|Upgrade time        |3d     |1w3d    |6h    |0s  |45m  |1w      |2d     |2h   |12h   |5d     |
|Upgrade requirements|175000$|2000000$|13000$|500$|1000$|1000000$|100000$|4000$|18000$|340000$|


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

## Main attack : projectileMarksman

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

|Level          |7   |10  |4   |1  |2   |9   |6   |3   |5   |8   |
|---------------|----|----|----|---|----|----|----|----|----|----|
|Damage per shot|2098|2860|1526|954|1144|2479|1907|1335|1716|2288|


### Projectile

  * Splash damage percentages: 100

|Level                       |7       |10  |4       |1      |2   |9       |6       |3       |5   |8   |
|----------------------------|--------|----|--------|-------|----|--------|--------|--------|----|----|
|Displayed damage per second |1936    |2640|1408    |880    |1056|2288    |1760    |1232    |1584|2112|
|Calculated damage per second|1936.615|2640|1408.615|880.615|1056|2288.308|1760.308|1232.308|1584|2112|


  * Cannons per sequence: 1
  * Cliptime: 3.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(300)**: Flying vehicle, Light vehicle, Vehicule hero, **(250)**: Heavy vehicle, Heavy vehicule hero, **(200)**: Flying infantry, Infantry, Infantry hero, Support troop, **(150)**: Heavy infantry, Heavy infantry hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(50)**: Shield, Shield generator, **(40)**: Wall
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Marksman

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: marksman_rbl-ani
  * Audio attack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: marksman_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: heroes
  * Gun position: "pathfndr_rbl_rig_MASTER_MOVER/pathfndr_rbl_rig_locator_gun_Rt":1
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 8.69,12.35,16.88
  * Icon closeup camera position: -0.01,3.22,8.62
  * Icon closeup lookat position: 0.08,2.65,0.01
  * Icon lookat position: -0.31,1.68,0.43
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: projectileMarksman
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |7   |10  |4   |1  |2   |9   |6   |3   |5   |8   |
|---------------------------|----|----|----|---|----|----|----|----|----|----|
|Displayed damage per second|1936|2640|1408|880|1056|2288|1760|1232|1584|2112|


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

|Level      |7     |10    |4     |1     |2     |9     |6     |3     |5     |8     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |220707|220710|220704|220701|220702|220709|220706|220703|220705|220708|
|Point value|17.600|24    |12.800|8     |9.600 |20.800|16    |11.200|14.400|19.200|


