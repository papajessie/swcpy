---
title: Jawa Saboteur (SmugglerSaboteur)
category: unit
---

# Jawa Saboteur (SmugglerSaboteur) — version 1108

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 4
  * Type: infantry

|Level         |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|--------------|----|----|----|----|----|----|----|----|----|----|
|Health        |3200|3840|4480|5120|5760|6400|7040|7680|8320|9600|
|Buildable unit|Yes |Yes |Yes |Yes |Yes |Yes |Yes |Yes |No  |No  |


### Training stats

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |6                                  |7                                  |8                                  |9                                  |10                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|------------------------------------|
|Training time|1m40s                              |1m50s                              |1m55s                              |2m                                 |2m5s                               |2m10s                              |2m15s                              |2m20s                              |2m25s                              |2m30s                               |
|Training cost|250$                               |350$                               |450$                               |550$                               |650$                               |750$                               |850$                               |950$                               |1050$                              |1150$                               |
|Building     |[Barracks 1](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 10](smugglerBarracks.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Upgrade requirements|3000$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


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

## Main attack : SmugglerSaboteur

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Shield (70)**, **Shield generator (70)**, _Other building (60)_, _Ressource generator (60)_, _Storage (60)_, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Can shoot over walls: No
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Time between shots: 100ms
  * Target locking: No

|Level                                     |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot                           |112  |135  |157  |180  |202  |224  |247  |269  |292  |336  |
|Impact delay                              |1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |500ms|
|Time between end of clip and start of clip|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|2s   |
|Shot count                                |5    |5    |5    |5    |5    |5    |5    |5    |5    |10   |


### Projectile

|Level                       |1  |2  |3  |4  |5   |6   |7   |8   |9   |10  |
|----------------------------|---|---|---|---|----|----|----|----|----|----|
|Displayed damage per second |329|396|461|529|593 |658 |726 |790 |858 |987 |
|Calculated damage per second|400|482|560|642|721 |800 |882 |960 |1042|988 |
|Calculated damage per clip  |560|675|785|900|1010|1120|1235|1345|1460|3360|


  * Cannons per sequence: 1
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 30
  * Damage multipliers: **(250)**: Shield generator, **(175)**: Shield, **(150)**: Wall, **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Storage, Support troop, Trap, Turret, Vehicule hero
  * Pass through shield: No

|Level   |1-9   |10    |
|--------|------|------|
|Cliptime|1.400s|3.400s|
|Salvos  |5     |10    |


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerSaboteur

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: jawaarmed_neu-ani
  * Audio attack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_darktrooper_01":35,"sfx_ui_unitcomplete_darktrooper_02":35,"sfx_ui_unitcomplete_darktrooper_03":30
  * Bullet: fx_blaster_beam_y_sm
  * Bundle name: jawaarmed_neu-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "generalpurpose_smg_rig_MASTER_MOVER/generalpurpose_smg_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_y_sm
  * Icon camera position: 4.07,10.49,14.92
  * Icon lookat position: -0.12,1.34,0.53
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Name: SmugglerSaboteur
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|329|396|461|529|593|658|726|790|858|987|


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
|Order      |334101|334102|334103|334104|334105|334106|334107|334108|334109|334110|
|Point value|5     |6     |7     |8     |9     |10    |11    |12    |13    |15    |


