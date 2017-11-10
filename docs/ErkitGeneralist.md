---
title: Er'Kit Militia Conscript (ErkitGeneralist)
category: unit
---

# Er'Kit Militia Conscript (ErkitGeneralist) — version 1098

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

|Level         |8   |4   |6   |10  |3   |2   |9   |5   |7   |1   |
|--------------|----|----|----|----|----|----|----|----|----|----|
|Health        |2880|1920|2400|3600|1680|1560|3120|2160|2640|1300|
|Buildable unit|Yes |Yes |Yes |No  |Yes |Yes |No  |Yes |Yes |Yes |


### Training stats

|Level        |8                                                        |4                                                        |6                                                        |10                                                        |3                                                        |2                                                        |9                                                        |5                                                        |7                                                        |1                                                        |
|-------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Training time|56s                                                      |48s                                                      |52s                                                      |1m                                                        |46s                                                      |44s                                                      |58s                                                      |50s                                                      |54s                                                      |42s                                                      |
|Training cost|190$                                                     |110$                                                     |150$                                                     |230$                                                      |90$                                                      |70$                                                      |210$                                                     |130$                                                     |170$                                                     |50$                                                      |
|Building     |["bld_title_syndicateBarracks" 8](syndicateBarracks.html)|["bld_title_syndicateBarracks" 4](syndicateBarracks.html)|["bld_title_syndicateBarracks" 6](syndicateBarracks.html)|["bld_title_syndicateBarracks" 10](syndicateBarracks.html)|["bld_title_syndicateBarracks" 3](syndicateBarracks.html)|["bld_title_syndicateBarracks" 2](syndicateBarracks.html)|["bld_title_syndicateBarracks" 9](syndicateBarracks.html)|["bld_title_syndicateBarracks" 5](syndicateBarracks.html)|["bld_title_syndicateBarracks" 7](syndicateBarracks.html)|["bld_title_syndicateBarracks" 1](syndicateBarracks.html)|


### Upgrading stats

|Level               |8      |4     |6      |10      |3    |2    |9       |5     |7      |1      |
|--------------------|-------|------|-------|--------|-----|-----|--------|------|-------|-------|
|Upgrade time        |3d12h  |3h30m |1d     |1w1d    |1h   |15m  |5d      |8h    |2d     |0s     |
|Upgrade requirements|320000$|12500$|100000$|1750000$|4000$|1500$|1000000$|25000$|160000$|Nothing|


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

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 200ms
  * Target locking: No

|Level          |8  |4  |6  |10 |3  |2  |9  |5  |7  |1  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|312|208|260|390|182|169|338|234|286|141|


### Projectile

|Level                       |8      |4      |6      |10     |3  |2      |9      |5      |7      |1      |
|----------------------------|-------|-------|-------|-------|---|-------|-------|-------|-------|-------|
|Displayed damage per second |667    |445    |556    |834    |389|361    |723    |500    |612    |301    |
|Calculated damage per second|668.571|445.714|557.143|835.714|390|362.143|724.286|501.429|612.857|302.143|


  * Cannons per sequence: 1
  * Cliptime: 1.400s
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

  * Animation delay: 0
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

|Level                      |8  |4  |6  |10 |3  |2  |9  |5  |7  |1  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|667|445|556|834|389|361|723|500|612|301|


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

|Level      |8     |4     |6     |10    |3     |2     |9     |5     |7     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |333908|333904|333906|333910|333903|333902|333909|333905|333907|333901|
|Point value|2.400 |1.600 |2     |3     |1.400 |1.200 |2.600 |1.800 |2.200 |1     |


