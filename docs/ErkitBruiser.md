---
title: ErKit Militia Bruiser (ErkitBruiser)
category: unit
---

# ErKit Militia Bruiser (ErkitBruiser) — version 1113

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

|Level         |1   |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|--------------|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health        |9000|10800|10500|12000|13500|15000|16500|18000|19500|22500|
|Buildable unit|Yes |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |No   |


### Training stats

|Level        |1                                                        |2                                                        |3                                                        |4                                                        |5                                                        |6                                                        |7                                                        |8                                                        |9                                                        |10                                                        |
|-------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|
|Training time|1m45s                                                    |1m50s                                                    |1m55s                                                    |2m                                                       |2m5s                                                     |2m10s                                                    |2m15s                                                    |2m20s                                                    |2m25s                                                    |2m30s                                                     |
|Training cost|250$                                                     |350$                                                     |450$                                                     |550$                                                     |650$                                                     |750$                                                     |850$                                                     |950$                                                     |1050$                                                    |1150$                                                     |
|Building     |["bld_title_syndicateBarracks" 1](syndicateBarracks.html)|["bld_title_syndicateBarracks" 2](syndicateBarracks.html)|["bld_title_syndicateBarracks" 3](syndicateBarracks.html)|["bld_title_syndicateBarracks" 4](syndicateBarracks.html)|["bld_title_syndicateBarracks" 5](syndicateBarracks.html)|["bld_title_syndicateBarracks" 6](syndicateBarracks.html)|["bld_title_syndicateBarracks" 7](syndicateBarracks.html)|["bld_title_syndicateBarracks" 8](syndicateBarracks.html)|["bld_title_syndicateBarracks" 9](syndicateBarracks.html)|["bld_title_syndicateBarracks" 10](syndicateBarracks.html)|


### Upgrading stats

|Level               |1   |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s  |30m  |1h30m|5h    |10h   |1d12h  |2d12h  |4d     |6d      |1w2d    |
|Upgrade requirements|700$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


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

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 500ms
  * Target locking: No

|Level          |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|325|390|380|434|488|542|596|650|705|813|


### Projectile

|Level                       |1  |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|---|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |299|358 |349 |399 |448 |498 |548 |598 |648 |747 |
|Calculated damage per second|300|360 |350 |400 |450 |500 |550 |600 |650 |750 |
|Calculated damage per clip  |975|1170|1140|1302|1464|1626|1788|1950|2115|2439|


  * Cannons per sequence: 1
  * Cliptime: 3.250s
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

  * Animation delay: 0
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

|Level                      |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|299|358|349|399|448|498|548|598|648|747|


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
|Order      |333601|333602|333603|333604|333605|333606|333607|333608|333609|333610|
|Point value|5     |6     |7     |8     |9     |10    |11    |12    |13    |15    |


