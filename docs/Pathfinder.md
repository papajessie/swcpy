---
title: Rebel Pathfinder (Pathfinder)
category: unit
---

# Rebel Pathfinder (Pathfinder) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Looter
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 2
  * Type: infantry

|Level |8   |7   |6   |5   |9   |1   |10  |2   |3   |4   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|4290|4050|3820|3610|4550|2880|4830|3050|3220|3410|


### Training stats

|Level        |8                                     |7                                     |6                                     |5                                     |9                                     |1                               |10                                     |2                                     |3                                     |4                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|56s                                   |54s                                   |52s                                   |50s                                   |58s                                   |46s                             |1m                                     |47s                                   |48s                                   |49s                                   |
|Training cost|400$                                  |340$                                  |300$                                  |260$                                  |420$                                  |220$                            |460$                                   |230$                                  |240$                                  |250$                                  |
|Building     |[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Barracks 4](rebelBarracks.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|


### Upgrading stats

|Level               |8      |7      |6      |5     |9       |1    |10      |2    |3    |4     |
|--------------------|-------|-------|-------|------|--------|-----|--------|-----|-----|------|
|Upgrade time        |3d12h  |2d     |1d     |8h    |5d      |0s   |1w1d    |15m  |1h   |3h30m |
|Upgrade requirements|320000$|160000$|100000$|25000$|1000000$|2500$|1750000$|3000$|6000$|12500$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 40
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : Pathfinder

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Ressource generator (60)**, **Storage (60)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 800ms
  * Retargeting offset: 8
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 0s
  * Target locking: No

|Level          |8  |7  |6  |5  |9  |1  |10 |2  |3  |4  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|730|690|650|610|770|490|820|520|550|580|


### Projectile

|Level                       |8      |7      |6      |5      |9      |1      |10     |2      |3      |4      |
|----------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|Displayed damage per second |690    |660    |620    |580    |730    |470    |780    |490    |520    |550    |
|Calculated damage per second|695.238|657.143|619.048|580.952|733.333|466.667|780.952|495.238|523.810|552.381|


  * Cannons per sequence: 1
  * Cliptime: 1.050s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Ressource generator, Storage, **(100)**: Droideka, Shield, Shield generator, **(75)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(50)**: Headquarters, Other building, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Pathfinder

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: pathfndr_rbl-ani
  * Audio attack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: pathfndr_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: resource
  * Gun position: "pathfndr_rbl_rig_MASTER_MOVER/pathfndr_rbl_rig_locator_gun_Rt":1
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 10.61,11.75,12.82
  * Icon closeup camera position: 1.45,1.64,9.17
  * Icon closeup lookat position: -0.01,2.68,-0.31
  * Icon lookat position: 0.09,1.73,0.11
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: Pathfinder
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |8  |7  |6  |5  |9  |1  |10 |2  |3  |4  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|690|660|620|580|730|470|780|490|520|550|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |8     |7     |6     |5     |9     |1     |10    |2     |3     |4     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |220408|220407|220406|220405|220409|220401|220410|220402|220403|220404|
|Point value|4.800 |4.400 |4     |3.600 |5.200 |2     |6     |2.400 |2.800 |3.200 |


