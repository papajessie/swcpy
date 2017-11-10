---
title: Wookiee Warrior (Wookie)
category: unit
---

# Wookiee Warrior (Wookie) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry

|Level |2    |5    |3    |7    |10   |9    |1   |8    |6    |4    |
|------|-----|-----|-----|-----|-----|-----|----|-----|-----|-----|
|Health|10800|13500|10500|16500|22500|19500|9000|18000|15000|12000|


### Training stats

|Level        |2                                     |5                                     |3                                     |7                                     |10                                     |9                                     |1                               |8                                     |6                                     |4                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|1m50s                                 |2m5s                                  |1m55s                                 |2m15s                                 |2m30s                                  |2m25s                                 |1m45s                           |2m20s                                 |2m10s                                 |2m                                    |
|Training cost|350$                                  |650$                                  |450$                                  |850$                                  |1150$                                  |1050$                                 |250$                            |1000$                                 |750$                                  |550$                                  |
|Building     |[Research Lab 2](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Barracks 2](rebelBarracks.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|


### Upgrading stats

|Level               |2    |5     |3    |7      |10      |9       |1   |8      |6      |4     |
|--------------------|-----|------|-----|-------|--------|--------|----|-------|-------|------|
|Upgrade time        |30m  |10h   |1h30m|2d12h  |1w2d    |6d      |0s  |4d     |1d12h  |5h    |
|Upgrade requirements|3000$|35000$|6000$|175000$|2000000$|1000000$|700$|350000$|115000$|15000$|


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

|Level          |2  |5  |3  |7  |10 |9  |1  |8  |6  |4  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|390|488|380|596|813|705|325|650|542|434|


### Projectile

|Level                       |2  |5      |3      |7      |10     |9      |1  |8  |6      |4      |
|----------------------------|---|-------|-------|-------|-------|-------|---|---|-------|-------|
|Displayed damage per second |360|450    |350    |550    |750    |650    |300|600|500    |400    |
|Calculated damage per second|360|450.462|350.769|550.154|750.462|650.769|300|600|500.308|400.615|


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

  * Unit ID: Wookie

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: wookiewarrior_rbl-ani
  * Audio attack: "sfx_attack_rebel_wookie_1":50,"sfx_attack_rebel_wookie_2":50
  * Audio death: "sfx_death_rebel_wookie_1":35,"sfx_death_rebel_wookie_2":35,"sfx_death_rebel_wookie_3":30
  * Audio placement: "sfx_placement_rebel_wookie_1":50,"sfx_placement_rebel_wookie_2":50
  * Audio train: "sfx_ui_unitcomplete_wookie_1":35,"sfx_ui_unitcomplete_wookie_2":35,"sfx_ui_unitcomplete_wookie_3":30
  * Buff asset offset: 0.00,0.36,0.00
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: wookiewarrior_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "wookiewarrior_rbl_rig_MASTER_MOVER/wookiewarrior_rbl_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 9.29,13.73,18.65
  * Icon closeup camera position: -0.51,3.09,12.25
  * Icon closeup lookat position: 0.08,3,-1.33
  * Icon lookat position: -0.06,1.71,0.07
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: Wookie
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |2  |5  |3  |7  |10 |9  |1  |8  |6  |4  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|360|450|350|550|750|650|300|600|500|400|


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

|Level      |2     |5     |3     |7     |10    |9     |1     |8     |6     |4     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |220202|220205|220203|220207|220210|220209|220201|220208|220206|220204|
|Point value|6     |9     |7     |11    |15    |13    |5     |12    |10    |8     |


