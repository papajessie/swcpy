---
title: Dewback (NativeDewback)
category: unit
---

# Dewback (NativeDewback)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Role: Breacher
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 3
  * Type: infantry

|Level         |10   |9    |8    |7    |6    |5    |4   |3   |2   |1   |
|--------------|-----|-----|-----|-----|-----|-----|----|----|----|----|
|Health        |18000|15600|14400|13200|12000|10800|9600|8400|7200|6000|
|Buildable unit|No   |No   |No   |Yes  |Yes  |Yes  |Yes |Yes |Yes |Yes |


### Training stats

  * Building: [Barracks 4](smugglerBarracks.html)

|Level        |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|-------------|----|----|----|----|----|----|----|----|----|----|
|Training time|1m  |58s |56s |54s |52s |50s |48s |46s |44s |42s |
|Training cost|690$|630$|570$|510$|450$|390$|330$|270$|210$|150$|


### Upgrading stats

|Level               |10      |9       |8      |7      |6      |5     |4     |3    |2    |1    |
|--------------------|--------|--------|-------|-------|-------|------|------|-----|-----|-----|
|Upgrade time        |1w1d    |5d      |3d12h  |2d     |1d     |8h    |3h30m |1h   |15m  |0s   |
|Upgrade requirements|1750000$|1000000$|320000$|160000$|100000$|25000$|12500$|9000$|7000$|5000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : Dewback

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Flying infantry (1), Flying vehicle (1), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 1s
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Reload time: 0s
  * Retargeting offset: 4
  * Self-centered targeting: No
  * Shot count: 5
  * Shot delay: 750ms
  * Target locking: No

|Level          |10  |9   |8   |7   |6   |5  |4  |3  |2  |1  |
|---------------|----|----|----|----|----|---|---|---|---|---|
|Damage per shot|1584|1373|1268|1162|1056|951|845|740|634|528|


### Projectile

  * Splash damage percentages: 100,75

|Level                       |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |780 |1961|1811|1660|1508|1358|1207|1057|905 |754 |
|Calculated damage per second|856 |742 |685 |628 |570 |514 |456 |400 |342 |285 |
|Calculated damage per cycle |7920|6865|6340|5810|5280|4755|4225|3700|3170|2640|


  * Cannons per sequence: 1
  * Shooting cycle duration: 9.250s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(300)**: Wall, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, **(20)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(0)**: Flying infantry, Flying vehicle
  * Pass through shield: No
  * Salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: NativeDewback

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: dewback_neu-ani
  * Audio attack: "sfx_attack_creatures_dewback_1":35,"sfx_attack_creatures_dewback_2":35,"sfx_attack_creatures_dewback_3":30
  * Audio death: "sfx_death_creatures_dewback_1":25,"sfx_death_creatures_dewback_2":25,"sfx_death_creatures_dewback_3":25,"sfx_death_creatures_dewback_4":25
  * Audio placement: "sfx_placement_creatures_dewback_1":35,"sfx_placement_creatures_dewback_2":35,"sfx_placement_creatures_dewback_3":30
  * Audio train: "sfx_ui_unitcomplete_dewback_1":35,"sfx_ui_unitcomplete_dewback_2":35,"sfx_ui_unitcomplete_dewback_3":30
  * Buff asset offset: 0.00,0.60,0.00
  * Bundle name: dewback_neu-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Icon camera position: 14.52,11.43,15.95
  * Icon lookat position: -0.75,0.91,-0.52
  * Max scale: 300
  * Muzzle flash: fx_melee_headbutt_lrg
  * Name: Dewback
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10 |9   |8   |7   |6   |5   |4   |3   |2  |1  |
|---------------------------|---|----|----|----|----|----|----|----|---|---|
|Displayed damage per second|780|1961|1811|1660|1508|1358|1207|1057|905|754|


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
|Order      |460710|460709|460708|460707|460706|460705|460704|460703|460702|460701|
|Point value|9     |7.800 |7.200 |6.600 |6     |5.400 |4.800 |4.200 |3.600 |3     |


