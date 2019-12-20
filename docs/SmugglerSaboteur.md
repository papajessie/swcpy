---
title: Jawa Saboteur (SmugglerSaboteur)
category: unit
---

# Jawa Saboteur (SmugglerSaboteur)

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

|Level         |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|--------------|----|----|----|----|----|----|----|----|----|----|
|Health        |9600|8320|7680|7040|6400|5760|5120|4480|3840|3200|
|Buildable unit|No  |No  |Yes |Yes |Yes |Yes |Yes |Yes |Yes |Yes |


### Training stats

|Level        |10                                  |9                                  |8                                  |7                                  |6                                  |5                                  |4                                  |3                                  |2                                  |1                                  |
|-------------|------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
|Training time|2m30s                               |2m25s                              |2m20s                              |2m15s                              |2m10s                              |2m5s                               |2m                                 |1m55s                              |1m50s                              |1m40s                              |
|Training cost|1150$                               |1050$                              |950$                               |850$                               |750$                               |650$                               |550$                               |450$                               |350$                               |250$                               |
|Building     |[Barracks 10](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 1](smugglerBarracks.html)|


### Upgrading stats

|Level               |10      |9       |8      |7      |6      |5     |4     |3    |2    |1    |
|--------------------|--------|--------|-------|-------|-------|------|------|-----|-----|-----|
|Upgrade time        |1w1d    |5d      |3d12h  |2d     |1d     |8h    |3h30m |1h   |15m  |0s   |
|Upgrade requirements|2000000$|1000000$|350000$|175000$|115000$|35000$|15000$|6000$|3000$|3000$|


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

  * Animation delay: 0s
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Can shoot over walls: No
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Shot delay: 100ms
  * Target locking: No

|Level          |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|---------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot|336  |292  |269  |247  |224  |202  |180  |157  |135  |112  |
|Impact delay   |500ms|1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |
|Reload time    |2s   |500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|
|Shot count     |10   |5    |5    |5    |5    |5    |5    |5    |5    |5    |


### Projectile

|Level                       |10  |9   |8   |7   |6   |5   |4  |3  |2  |1  |
|----------------------------|----|----|----|----|----|----|---|---|---|---|
|Displayed damage per second |630 |858 |790 |726 |658 |593 |529|461|396|329|
|Calculated damage per second|988 |1042|960 |882 |800 |721 |642|560|482|400|
|Calculated damage per cycle |3360|1460|1345|1235|1120|1010|900|785|675|560|


  * Cannons per sequence: 1
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 30
  * Damage multipliers: **(250)**: Shield generator, **(175)**: Shield, **(150)**: Wall, **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Storage, Support troop, Trap, Turret, Vehicule hero
  * Pass through shield: No

|Level                  |10    |1-9   |
|-----------------------|------|------|
|Shooting cycle duration|3.400s|1.400s|
|Salvos                 |10    |5     |


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerSaboteur

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

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

|Level                      |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|630|858|790|726|658|593|529|461|396|329|


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

|Level      |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |461510|461509|461508|461507|461506|461505|461504|461503|461502|461501|
|Point value|15    |13    |12    |11    |10    |9     |8     |7     |6     |5     |


