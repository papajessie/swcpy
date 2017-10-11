---
title: AT-RT Walker (ATRT)
category: unit
---

# AT-RT Walker (ATRT) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Looter
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: vehicle
  * Unlock planet: Unlock on Hoth
  * _Not found: Can be given, Shield asset name_

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|19200|19800|20480|21040|21850|22610|23720|25290|26920|28820|

### Training stats

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|2m40s                         |2m56s                                 |3m4s                                  |3m12s                                 |3m20s                                 |3m28s                                 |3m36s                                 |3m44s                                 |3m52s                                 |4m                                     |
|Training cost|400$                          |560$                                  |720$                                  |880$                                  |1040$                                 |1200$                                 |1360$                                 |1600$                                 |1680$                                 |1840$                                  |
|Building     |[Factory 1](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

### Upgrading stats

  * Upgrade time: 5s
  * Upgrade requirements: 32 data fragments

### Move stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Unit size on map: 1x1
  * Support follow distance: 0
  * _Not found: Ignores walls, Run speed, Run threshold_

## Main attack : ATRT

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 7854.000
  * Target preference strength: 90
  * Target preferences: **Storage (80)**, **Ressource generator (80)**, Heavy vehicle (50), Light vehicle (50), Flying vehicle (50), Heavy infantry (50), Heavy vehicule hero (50), Flying infantry (50), Turret (50), Other building (50), Infantry (50), Heavy infantry hero (50), Support troop (50), Shield (50), Headquarters (50), Infantry hero (50), Vehicule hero (50), Shield generator (50), Droideka (50), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 13m20s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 0s
  * Splash: 0
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2184|2280|2380|2490|2610|2730|2860|3000|3140|3290|

### Projectile

  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1       |2       |3       |4       |5       |6       |7       |8       |9       |10      |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |2184.000|2280.000|2380.000|2490.000|2610.000|2730.000|2860.000|3000.000|3140.000|3290.000|
|Calculated damage per second|2080.000|2171.429|2266.667|2371.429|2485.714|2600.000|2723.810|2857.143|2990.476|3133.333|

  * Headquarters: 50%
  * Heavy infantry: 50%
  * Heavy vehicle: 50%
  * Other building: 50%
  * Droideka: 100%
  * Flying infantry: 75%
  * Flying vehicle: 75%
  * Support troop: 75%
  * Heavy infantry hero: 50%
  * Heavy vehicule hero: 50%
  * Infantry hero: 75%
  * Vehicule hero: 75%
  * Infantry: 75%
  * Ressource generator: 400%
  * Shield: 50%
  * Shield generator: 50%
  * Storage: 400%
  * Trap: 50%
  * Turret: 50%
  * Light vehicle: 75%
  * Wall: 50%

  * Cannons per sequence: 1
  * Cliptime: 1.050s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Pass through shield: No
  * Salvos: 1
  * _Not found: Length segments, Width segments_

## Other stats

### Internal stats

These stats internal to the system link different parts of data together.

  * Ability: abilityATRTIonShot
  * Unit ID: ATRT
  * Upgrade shard uid: shrd_troopATRT
  * _Not found: Apply buffs, Death projectile, Death projectile damage, Death projectile delay, Death projectile distance, Hero data, Self buff, Spawn apply buffs_

### Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: atrt_rbl-ani
  * Audio attack: "sfx_attack_walker_1":25,"sfx_attack_walker_2":25,"sfx_attack_walker_3":25,"sfx_attack_walker_4":25
  * Audio death: "sfx_death_walker_1":100
  * Audio placement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * Buff asset offset: 0.00,1.5,0.00
  * Bundle name: atrt_rbl-ani
  * Event button action: planet
  * Event button data: planet21
  * Event button string: hn_open_hth
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Gun position: "atrt_rbl_rig_MASTER_MOVER/atrt_rbl_rig_locator_gun":1
  * Icon camera position: 21.25,19.91,26.67
  * Icon lookat position: -0.49,1.92,-0.68
  * Targeted type: ENEMIES
  * Unlocked by event: true
  * _Not found: Audio impact, Audio train, Death animation, Decal asset name, Decal bundle name, Decal size, Effect type, Hologram uid, Icon closeup camera position, Icon closeup lookat position, Info UI type, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by tournament_

|Level               |1    |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|--------------------|-----|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Icon unlock position|0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation|0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale   |1,1,1|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|

### Attack presentation stats

  * Animation delay: 0
  * Favorite target type: resource
  * Arcs: No
  * Bullet: fx_blaster_beam_b_med
  * Hit spark: fx_blaster_hit_b_med
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_med
  * Name: ATRT
  * Spin speed: 0
  * _Not found: Charge asset name, Ground bullet, Muzzle flash fade time, Projectile length, S transition_

|Level                      |1       |2       |3       |4       |5       |6       |7       |8       |9       |10      |
|---------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second|2184.000|2280.000|2380.000|2490.000|2610.000|2730.000|2860.000|3000.000|3140.000|3290.000|

* This is the damage per second displayed in-game, but may not be the same as the real damage per second.

### Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |231101|231102|231103|231104|231105|231106|231107|231108|231109|231110|
|Point value|5.000 |6.000 |7.000 |8.000 |9.000 |10.000|11.000|12.000|13.000|15.000|

### Uninterpreted attack stats

  * Arming delay: 0
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: No
  * _Not found: S1 time, S2 time_

I could not show the following roles, because I was not programmed to : abilitymove, abilityprefs, projectilemisc, abilitystats, abilityunknown, abilityonly, abilitypresentation