---
title: Mercenary Pistoleer (SmugglerPistoleer)
category: unit
---

# Mercenary Pistoleer (SmugglerPistoleer) — version 1117

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 6
  * Type: infantry

|Level |1   |2   |3    |4    |5    |6    |7    |8    |9    |10   |
|------|----|----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|7200|8640|10080|11520|12960|14400|15840|17280|18720|21600|


### Training stats

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |6                                  |7                                  |8                                  |9                                  |10                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|------------------------------------|
|Training time|4s                                 |4s                                 |5s                                 |5s                                 |5s                                 |5s                                 |5s                                 |6s                                 |6s                                 |6s                                  |
|Training cost|50$                                |70$                                |90$                                |110$                               |130$                               |150$                               |170$                               |190$                               |210$                               |230$                                |
|Building     |[Barracks 1](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 10](smugglerBarracks.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|1500$|5000$|14000$|25000$|50000$|100000$|200000$|750000$|2000000$|4000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : SmugglerPistoleer

### Targeting

  * Attack shield border: No
  * Max attack range: 6
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (70)**, **Flying infantry (70)**, **Flying vehicle (70)**, **Heavy infantry (70)**, **Heavy vehicle (70)**, **Infantry (70)**, **Light vehicle (70)**, **Support troop (70)**, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Shot count: 2
  * Time between shots: 125ms
  * Target locking: No

|Level          |1  |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|---------------|---|---|---|---|---|---|---|---|----|----|
|Damage per shot|405|486|567|648|729|810|891|972|1053|1215|


### Projectile

|Level                       |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|---|---|----|----|----|----|----|----|----|----|
|Displayed damage per second |373|448|523 |598 |672 |747 |822 |897 |971 |1121|
|Calculated damage per second|720|864|1008|1152|1296|1440|1584|1728|1872|2160|
|Calculated damage per clip  |810|972|1134|1296|1458|1620|1782|1944|2106|2430|


  * Cannons per sequence: 1
  * Cliptime: 1.125s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(150)**: Flying infantry, Infantry, Support troop, **(100)**: Droideka, Flying vehicle, Heavy infantry, Heavy infantry hero, Infantry hero, Light vehicle, Vehicule hero, **(75)**: Headquarters, Heavy vehicle, Trap, Turret, Wall, **(50)**: Heavy vehicule hero, Other building, Ressource generator, Shield, Shield generator, Storage
  * Pass through shield: No
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerPistoleer

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: generalpurpose_smg-ani
  * Audio attack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Bullet: fx_blaster_beam_y_sm
  * Bundle name: generalpurpose_smg-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: none
  * Gun position: "generalpurpose_smg_rig_MASTER_MOVER/generalpurpose_smg_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_y_sm
  * Icon camera position: 8.56,9.58,10.6
  * Icon lookat position: 0.09,1.4,0.28
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Name: SmugglerPistoleer
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |2  |3  |4  |5  |6  |7  |8  |9  |10  |
|---------------------------|---|---|---|---|---|---|---|---|---|----|
|Displayed damage per second|373|448|523|598|672|747|822|897|971|1121|


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

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |334001|334002|334003|334004|334005|334006|334007|334008|334009|334010|
|Point value|1     |1.200 |1.400 |1.600 |1.800 |2     |2.200 |2.400 |2.600 |3     |


