---
title: ErKit Militia Conscript (ErkitGeneralist)
category: unit
---

# ErKit Militia Conscript (ErkitGeneralist)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: infantry

|Level         |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|--------------|----|----|----|----|----|----|----|----|----|----|
|Health        |3600|3120|2880|2640|2400|2160|1920|1680|1560|1300|
|Buildable unit|No  |No  |Yes |Yes |Yes |Yes |Yes |Yes |Yes |Yes |


### Training stats

|Level        |10                                                        |9                                                        |8                                                        |7                                                        |6                                                        |5                                                        |4                                                        |3                                                        |2                                                        |1                                                        |
|-------------|----------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Training time|1m                                                        |58s                                                      |56s                                                      |54s                                                      |52s                                                      |50s                                                      |48s                                                      |46s                                                      |44s                                                      |42s                                                      |
|Training cost|230$                                                      |210$                                                     |190$                                                     |170$                                                     |150$                                                     |130$                                                     |110$                                                     |90$                                                      |70$                                                      |50$                                                      |
|Building     |["bld_title_syndicateBarracks" 10](syndicateBarracks.html)|["bld_title_syndicateBarracks" 9](syndicateBarracks.html)|["bld_title_syndicateBarracks" 8](syndicateBarracks.html)|["bld_title_syndicateBarracks" 7](syndicateBarracks.html)|["bld_title_syndicateBarracks" 6](syndicateBarracks.html)|["bld_title_syndicateBarracks" 5](syndicateBarracks.html)|["bld_title_syndicateBarracks" 4](syndicateBarracks.html)|["bld_title_syndicateBarracks" 3](syndicateBarracks.html)|["bld_title_syndicateBarracks" 2](syndicateBarracks.html)|["bld_title_syndicateBarracks" 1](syndicateBarracks.html)|


### Upgrading stats

|Level               |10      |9       |8      |7      |6      |5     |4     |3    |2    |1      |
|--------------------|--------|--------|-------|-------|-------|------|------|-----|-----|-------|
|Upgrade time        |1w1d    |5d      |3d12h  |2d     |1d     |8h    |3h30m |1h   |15m  |0s     |
|Upgrade requirements|1750000$|1000000$|320000$|160000$|100000$|25000$|12500$|4000$|1500$|Nothing|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : Soldier

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Animation delay: 0s
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Reload time: 500ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 3
  * Shot delay: 200ms
  * Target locking: No

|Level          |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|390|338|312|286|260|234|208|182|169|141|


### Projectile

|Level                       |10  |9   |8  |7  |6  |5  |4  |3  |2  |1  |
|----------------------------|----|----|---|---|---|---|---|---|---|---|
|Displayed damage per second |2631|723 |667|612|556|500|445|389|361|301|
|Calculated damage per second|835 |724 |668|612|557|501|445|390|362|302|
|Calculated damage per cycle |1170|1014|936|858|780|702|624|546|507|423|


  * Cannons per sequence: 1
  * Shooting cycle duration: 1.400s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ErkitGeneralist

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: erkit1_neu-ani
  * Audio attack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: erkit1_neu-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "soldier_rbl_rig_MASTER_MOVER/soldier_rbl_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 8.56,9.58,10.6
  * Icon lookat position: 0.09,1.4,0.28
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: Soldier
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10  |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|---------------------------|----|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|2631|723|667|612|556|500|445|389|361|301|


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
|Order      |461310|461309|461308|461307|461306|461305|461304|461303|461302|461301|
|Point value|3     |2.600 |2.400 |2.200 |2     |1.800 |1.600 |1.400 |1.200 |1     |


