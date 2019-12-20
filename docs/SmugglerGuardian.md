---
title: Smuggler Guardian (SmugglerGuardian)
category: unit
---

# Smuggler Guardian (SmugglerGuardian)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Independant units
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 10
  * Type: infantry

|Level         |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health        |51000|44200|40800|37400|34000|30600|27200|23800|20400|17000|
|Buildable unit|No   |No   |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |


### Training stats

|Level        |10                                  |9                                  |8                                  |7                                  |6                                  |5                                  |4                                  |3                                  |2                                  |1                                  |
|-------------|------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
|Training time|1m                                  |58s                                |56s                                |54s                                |52s                                |50s                                |48s                                |46s                                |44s                                |42s                                |
|Training cost|920$                                |840$                               |760$                               |680$                               |600$                               |520$                               |440$                               |360$                               |280$                               |200$                               |
|Building     |[Barracks 10](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 1](smugglerBarracks.html)|


### Upgrading stats

|Level               |10      |9       |8      |7      |6      |5     |4     |3    |2    |1    |
|--------------------|--------|--------|-------|-------|-------|------|------|-----|-----|-----|
|Upgrade time        |1w1d    |5d      |3d12h  |2d12h  |1d12h  |10h   |5h    |1h30m|30m  |0s   |
|Upgrade requirements|1750000$|1000000$|320000$|160000$|100000$|25000$|12500$|6000$|3000$|3000$|


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

## Main attack : SmugglerGuardian

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Shield (70)**, **Shield generator (70)**, **Turret (70)**, _Droideka (60)_, _Flying infantry (60)_, _Flying vehicle (60)_, _Heavy infantry (60)_, _Heavy vehicle (60)_, _Infantry (60)_, _Light vehicle (60)_, _Support troop (60)_, Headquarters (50), Other building (50), Ressource generator (50), Storage (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0s
  * Clip retargeting: No
  * Gun shooting sequence: 1,2
  * Impact delay: 1s
  * Can shoot over walls: No
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Target locking: No

|Level          |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|---------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Charge time    |250ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|
|Damage per shot|2250 |1950 |1800 |1650 |1500 |1350 |1200 |1050 |900  |750  |
|Reload time    |2s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |
|Shot count     |3    |1    |1    |1    |1    |1    |1    |1    |1    |1    |
|Shot delay     |500ms|200ms|200ms|200ms|200ms|200ms|200ms|200ms|200ms|200ms|


### Projectile

|Level                       |10  |9   |8   |7   |6   |5   |4   |3   |2  |1  |
|----------------------------|----|----|----|----|----|----|----|----|---|---|
|Displayed damage per second |1951|624 |576 |528 |480 |432 |384 |336 |336|280|
|Calculated damage per second|2076|1300|1200|1100|1000|900 |800 |700 |600|500|
|Calculated damage per cycle |6750|1950|1800|1650|1500|1350|1200|1050|900|750|


  * Cannons per sequence: 2
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Storage, Support troop, Trap, Turret, Vehicule hero, **(50)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Wall, **(25)**: Shield, Shield generator
  * Pass through shield: No

|Level                  |10    |1-9   |
|-----------------------|------|------|
|Shooting cycle duration|3.250s|1.500s|
|Salvos                 |3     |1     |


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerGuardian

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: bountyhunter_smg-ani
  * Audio attack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_darktrooper_01":35,"sfx_ui_unitcomplete_darktrooper_02":35,"sfx_ui_unitcomplete_darktrooper_03":30
  * Buff asset offset: 0.00,0.08,0.00
  * Bullet: fx_blaster_beam_y_lrg
  * Bundle name: bountyhunter_smg-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Lt":1,"bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Rt":2
  * Hit spark: fx_blaster_hit_y_sm
  * Icon camera position: 9,10,11.12
  * Icon lookat position: 0.09,1.4,0.28
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Name: SmugglerGuardian
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10  |9  |8  |7  |6  |5  |4  |2-3|1  |
|---------------------------|----|---|---|---|---|---|---|---|---|
|Displayed damage per second|1951|624|576|528|480|432|384|336|280|


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
|Order      |461610|461609|461608|461607|461606|461605|461604|461603|461602|461601|
|Point value|12    |10.400|9.600 |8.800 |8     |7.200 |6.400 |5.600 |4.800 |4     |


