---
title: ErKit Militia Bruiser (ErkitBruiser)
category: unit
---

# ErKit Militia Bruiser (ErkitBruiser)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Independant units
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry

|Level         |10   |9    |8    |7    |6    |5    |4    |3    |2    |1   |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|
|Health        |22500|19500|18000|16500|15000|13500|12000|10500|10800|9000|
|Buildable unit|No   |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes |


### Training stats

|Level        |10                                                        |9                                                        |8                                                        |7                                                        |6                                                        |5                                                        |4                                                        |3                                                        |2                                                        |1                                                        |
|-------------|----------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Training time|2m30s                                                     |2m25s                                                    |2m20s                                                    |2m15s                                                    |2m10s                                                    |2m5s                                                     |2m                                                       |1m55s                                                    |1m50s                                                    |1m45s                                                    |
|Training cost|1150$                                                     |1050$                                                    |950$                                                     |850$                                                     |750$                                                     |650$                                                     |550$                                                     |450$                                                     |350$                                                     |250$                                                     |
|Building     |["bld_title_syndicateBarracks" 10](syndicateBarracks.html)|["bld_title_syndicateBarracks" 9](syndicateBarracks.html)|["bld_title_syndicateBarracks" 8](syndicateBarracks.html)|["bld_title_syndicateBarracks" 7](syndicateBarracks.html)|["bld_title_syndicateBarracks" 6](syndicateBarracks.html)|["bld_title_syndicateBarracks" 5](syndicateBarracks.html)|["bld_title_syndicateBarracks" 4](syndicateBarracks.html)|["bld_title_syndicateBarracks" 3](syndicateBarracks.html)|["bld_title_syndicateBarracks" 2](syndicateBarracks.html)|["bld_title_syndicateBarracks" 1](syndicateBarracks.html)|


### Upgrading stats

|Level               |10      |9       |8      |7      |6      |5     |4     |3    |2    |1   |
|--------------------|--------|--------|-------|-------|-------|------|------|-----|-----|----|
|Upgrade time        |1w2d    |6d      |4d     |2d12h  |1d12h  |10h   |5h    |1h30m|30m  |0s  |
|Upgrade requirements|2000000$|1000000$|350000$|175000$|115000$|35000$|15000$|6000$|3000$|700$|


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

## Main attack : Wookie

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Animation delay: 0s
  * Charge time: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Reload time: 2s
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 3
  * Shot delay: 500ms
  * Target locking: No

|Level          |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|813|705|650|596|542|488|434|380|390|325|


### Projectile

|Level                       |10  |9   |8   |7   |6   |5   |4   |3   |2   |1  |
|----------------------------|----|----|----|----|----|----|----|----|----|---|
|Displayed damage per second |834 |648 |598 |548 |498 |448 |399 |349 |358 |299|
|Calculated damage per second|750 |650 |600 |550 |500 |450 |400 |350 |360 |300|
|Calculated damage per cycle |2439|2115|1950|1788|1626|1464|1302|1140|1170|975|


  * Cannons per sequence: 1
  * Shooting cycle duration: 3.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(75)**: Flying infantry, Flying vehicle, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(50)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ErkitBruiser

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: erkit2_neu-ani
  * Audio attack: "sfx_attack_rebel_wookie_1":50,"sfx_attack_rebel_wookie_2":50
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_wookie_1":35,"sfx_ui_unitcomplete_wookie_2":35,"sfx_ui_unitcomplete_wookie_3":30
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: erkit2_neu-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "wookiewarrior_rbl_rig_MASTER_MOVER/wookiewarrior_rbl_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 8.56,9.58,10.6
  * Icon lookat position: 0.09,1.4,0.28
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: Wookie
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|834|648|598|548|498|448|399|349|358|299|


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
|Order      |460910|460909|460908|460907|460906|460905|460904|460903|460902|460901|
|Point value|15    |13    |12    |11    |10    |9     |8     |7     |6     |5     |


