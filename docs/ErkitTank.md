---
title: Salvaged AAT1 (ErkitTank)
category: unit
---

# Salvaged AAT1 (ErkitTank) — version 1093

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Independant units
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 9
  * Type: vehicle

|Level         |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health        |13500|16200|18900|21600|24300|27000|29700|32400|35100|40500|
|Buildable unit|Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |No   |No   |


### Training stats

|Level        |1                                                      |2                                                      |3                                                      |4                                                      |5                                                      |6                                                      |7                                                      |8                                                      |9                                                      |10                                                      |
|-------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|
|Training time|3m30s                                                  |3m40s                                                  |3m50s                                                  |4m                                                     |4m10s                                                  |4m20s                                                  |4m30s                                                  |4m40s                                                  |4m50s                                                  |5m                                                      |
|Training cost|450$                                                   |630$                                                   |810$                                                   |990$                                                   |1170$                                                  |1350$                                                  |1530$                                                  |1710$                                                  |1890$                                                  |2070$                                                   |
|Building     |["bld_title_syndicateFactory" 1](syndicateFactory.html)|["bld_title_syndicateFactory" 2](syndicateFactory.html)|["bld_title_syndicateFactory" 3](syndicateFactory.html)|["bld_title_syndicateFactory" 4](syndicateFactory.html)|["bld_title_syndicateFactory" 5](syndicateFactory.html)|["bld_title_syndicateFactory" 6](syndicateFactory.html)|["bld_title_syndicateFactory" 7](syndicateFactory.html)|["bld_title_syndicateFactory" 8](syndicateFactory.html)|["bld_title_syndicateFactory" 9](syndicateFactory.html)|["bld_title_syndicateFactory" 10](syndicateFactory.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |45m  |2h   |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Upgrade requirements|2700$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 1
  * Rotation speed: 2
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x3

## Main attack : AAT1

### Targeting

  * Attack shield border: No
  * Max attack range: 6
  * Min attack range: 0
  * New rotation speed: 2000
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Shot count: 4
  * Time between shots: 200ms
  * Target locking: No

|Level          |1  |2  |3  |4  |5  |6  |7  |8   |9   |10  |
|---------------|---|---|---|---|---|---|---|----|----|----|
|Damage per shot|449|539|629|719|808|898|988|1078|1168|1347|


### Projectile

  * Splash damage percentages: 100,50

|Level                       |1      |2      |3      |4       |5       |6       |7       |8       |9       |10      |
|----------------------------|-------|-------|-------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |628    |754    |880    |1006    |1131    |1257    |1383    |1509    |1635    |1885    |
|Calculated damage per second|630.175|756.491|882.807|1009.123|1134.035|1260.351|1386.667|1512.982|1639.298|1890.526|


  * Cannons per sequence: 1
  * Cliptime: 2.850s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100%)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(50%)**: Flying infantry, Flying vehicle, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(25%)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero
  * Pass through shield: No
  * Salvos: 4

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ErkitTank

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: aat1_smg-ani
  * Audio attack: "sfx_attack_tank_1":25,"sfx_attack_tank_2":25,"sfx_attack_tank_3":25,"sfx_attack_tank_4":25
  * Audio death: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * Audio placement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * Buff asset offset: 0.00,1.81,0.00
  * Bullet: fx_blaster_beam_b_med
  * Bundle name: aat1_smg-ani
  * Factory rotation: 0
  * Factory scale factor: 0.81100000000000005417888360170763917267322540283203125
  * Favorite target type: turret
  * Gun position: "aat1_rbl_rig_MASTER_MOVER/aat1_rbl_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_b_med
  * Icon camera position: 22.61,26.18,29.65
  * Icon lookat position: -0.48,1.51,-0.32
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_med
  * Name: AAT1
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |2  |3  |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|---|---|---|----|----|----|----|----|----|----|
|Displayed damage per second|628|754|880|1006|1131|1257|1383|1509|1635|1885|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |343801|343802|343803|343804|343805|343806|343807|343808|343809|343810|
|Point value|9     |10.800|12.600|14.400|16.200|18    |19.800|21.600|23.400|27    |


