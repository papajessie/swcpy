---
title: Scout Undead Trooper (SmugglerScoutDeath)
category: unit
---

# Scout Undead Trooper (SmugglerScoutDeath) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Buildable unit: No
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: infantry

|Level |2   |3   |5   |7   |9   |4   |8   |6   |10  |1   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2025|2365|3040|3715|4390|2700|4050|3375|5065|1690|


### Training stats

|Level        |2  |3  |5   |7   |9   |4   |8   |6   |10  |1  |
|-------------|---|---|----|----|----|----|----|----|----|---|
|Training time|22s|23s|25s |27s |29s |24s |28s |26s |30s |21s|
|Training cost|70$|90$|130$|170$|210$|110$|190$|150$|230$|50$|


### Upgrading stats

|Level               |2    |3    |5     |7      |9       |4     |8      |6      |10      |1   |
|--------------------|-----|-----|------|-------|--------|------|-------|-------|--------|----|
|Upgrade time        |15m  |1h   |8h    |2d     |5d      |3h30m |3d12h  |1d     |1w1d    |0s  |
|Upgrade requirements|1500$|4000$|25000$|160000$|1000000$|12500$|320000$|100000$|1750000$|600$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 50
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : ScoutDeath

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (60)**, **Flying infantry (60)**, **Flying vehicle (60)**, **Heavy infantry (60)**, **Heavy infantry hero (60)**, **Heavy vehicle (60)**, **Heavy vehicule hero (60)**, **Infantry (60)**, **Infantry hero (60)**, **Light vehicle (60)**, **Support troop (60)**, **Vehicule hero (60)**, _Ressource generator (51)_, _Storage (51)_, Headquarters (50), Other building (50), Shield (50), Shield generator (50), Turret (50), Wall (1), Trap (0)
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
  * Shot count: 4
  * Time between shots: 225ms
  * Target locking: No

|Level          |2  |3  |5  |7  |9  |4  |8  |6  |10 |1  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|190|220|285|350|410|255|380|315|475|160|


### Projectile

|Level                       |2      |3      |5      |7      |9      |4      |8      |6      |10      |1      |
|----------------------------|-------|-------|-------|-------|-------|-------|-------|-------|--------|-------|
|Displayed damage per second |367.500|385    |437.500|490    |577.500|420    |542.500|472.500|630     |332.500|
|Calculated damage per second|440.580|510.145|660.870|811.594|950.725|591.304|881.159|730.435|1101.449|371.014|


  * Cannons per sequence: 1
  * Cliptime: 1.725s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(500)**: Wall, **(400)**: Ressource generator, Storage, **(275)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Infantry, Shield, Support troop, **(200)**: Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry hero, Light vehicle, Vehicule hero, **(100)**: Trap, Turret, **(50)**: Headquarters, Other building, Shield generator
  * Pass through shield: No
  * Salvos: 4

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerScoutDeath

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: scotrper_dth-ani
  * Audio attack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * Audio death: "sfx_death_deathtrooper_1":35,"sfx_death_deathtrooper_2":35,"sfx_death_deathtrooper_3":30
  * Audio placement: "sfx_placement_deathtrooper_1":35,"sfx_placement_deathtrooper_2":35,"sfx_placement_deathtrooper_3":30
  * Bullet: fx_blaster_beam_g_sm
  * Bundle name: scotrper_dth-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Gun position: "scotrper_dth_rig_MASTER_MOVER/scotrper_dth_rig_locator_gun_Rt":1
  * Hit spark: fx_blaster_hit_g_sm
  * Icon camera position: 10.84,12.06,13.07
  * Icon closeup camera position: 4.94,-0.46,8
  * Icon closeup lookat position: -0.15,2.51,-0.51
  * Icon lookat position: 0.06,1.74,0.02
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_g_sm
  * Name: ScoutDeath
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |2      |3  |5      |7  |9      |4  |8      |6      |10 |1      |
|---------------------------|-------|---|-------|---|-------|---|-------|-------|---|-------|
|Displayed damage per second|367.500|385|437.500|490|577.500|420|542.500|472.500|630|332.500|


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

|Level      |2     |3     |5     |7     |9     |4     |8     |6     |10    |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |333702|333703|333705|333707|333709|333704|333708|333706|333710|333701|
|Point value|1.200 |1.400 |1.800 |2.200 |2.600 |1.600 |2.400 |2     |3     |1     |


