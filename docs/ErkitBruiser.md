---
title: Er'Kit Militia Bruiser (ErkitBruiser)
category: unit
---

# Er'Kit Militia Bruiser (ErkitBruiser) — version 1098

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

|Level         |1   |10   |9    |3    |8    |6    |4    |2    |5    |7    |
|--------------|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health        |9000|22500|19500|10500|18000|15000|12000|10800|13500|16500|
|Buildable unit|Yes |No   |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |Yes  |


### Training stats

|Level        |1                                                        |10                                                        |9                                                        |3                                                        |8                                                        |6                                                        |4                                                        |2                                                        |5                                                        |7                                                        |
|-------------|---------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Training time|1m45s                                                    |2m30s                                                     |2m25s                                                    |1m55s                                                    |2m20s                                                    |2m10s                                                    |2m                                                       |1m50s                                                    |2m5s                                                     |2m15s                                                    |
|Training cost|250$                                                     |1150$                                                     |1050$                                                    |450$                                                     |950$                                                     |750$                                                     |550$                                                     |350$                                                     |650$                                                     |850$                                                     |
|Building     |["bld_title_syndicateBarracks" 1](syndicateBarracks.html)|["bld_title_syndicateBarracks" 10](syndicateBarracks.html)|["bld_title_syndicateBarracks" 9](syndicateBarracks.html)|["bld_title_syndicateBarracks" 3](syndicateBarracks.html)|["bld_title_syndicateBarracks" 8](syndicateBarracks.html)|["bld_title_syndicateBarracks" 6](syndicateBarracks.html)|["bld_title_syndicateBarracks" 4](syndicateBarracks.html)|["bld_title_syndicateBarracks" 2](syndicateBarracks.html)|["bld_title_syndicateBarracks" 5](syndicateBarracks.html)|["bld_title_syndicateBarracks" 7](syndicateBarracks.html)|


### Upgrading stats

|Level               |1   |10      |9       |3    |8      |6      |4     |2    |5     |7      |
|--------------------|----|--------|--------|-----|-------|-------|------|-----|------|-------|
|Upgrade time        |0s  |1w2d    |6d      |1h30m|4d     |1d12h  |5h    |30m  |10h   |2d12h  |
|Upgrade requirements|700$|2000000$|1000000$|6000$|350000$|115000$|15000$|3000$|35000$|175000$|


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

|Level          |1  |10 |9  |3  |8  |6  |4  |2  |5  |7  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|325|813|705|380|650|542|434|390|488|596|


### Projectile

|Level                       |1  |10     |9      |3      |8  |6      |4      |2  |5      |7      |
|----------------------------|---|-------|-------|-------|---|-------|-------|---|-------|-------|
|Displayed damage per second |299|747    |648    |349    |598|498    |399    |358|448    |548    |
|Calculated damage per second|300|750.462|650.769|350.769|600|500.308|400.615|360|450.462|550.154|


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

|Level                      |1  |10 |9  |3  |8  |6  |4  |2  |5  |7  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|299|747|648|349|598|498|399|358|448|548|


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

|Level      |1     |10    |9     |3     |8     |6     |4     |2     |5     |7     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |333601|333610|333609|333603|333608|333606|333604|333602|333605|333607|
|Point value|5     |15    |13    |7     |12    |10    |8     |6     |9     |11    |


