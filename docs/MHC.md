---
title: Mobile Heavy Cannon (MHC)
category: unit
---

# Mobile Heavy Cannon (MHC) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 12
  * Type: vehicle
  * _Not found: Can be given, Unlock planet_

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|10800|12960|15120|17280|19440|21600|23760|25920|28080|32400|

### Training stats

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|4m12s                          |4m24s                                  |4m36s                                  |4m48s                                  |5m                                     |5m12s                                  |5m24s                                  |5m36s                                  |5m48s                                  |6m                                      |
|Training cost|500$                           |700$                                   |900$                                   |1100$                                  |1300$                                  |1500$                                  |1700$                                  |2400$                                  |2700$                                  |3000$                                   |
|Building     |[Factory 7](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |1h   |2h30m|7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Upgrade requirements|6500$|3000$|6000$|15000$|35000$|115000$|200000$|385000$|1250000$|2250000$|

### Move stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 10
  * Propensity to go around obstacles: 200
  * Rotation speed: 31.416
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2
  * _Not found: Ignores walls, Support follow distance_
## Main attack : projectileMHC

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 15708.000
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, Light vehicle (50), Storage (50), Shield generator (50), Shield (50), Ressource generator (50), Infantry (50), Support troop (50), Flying vehicle (50), Flying infantry (50), Droideka (50), Other building (50), Heavy vehicle (50), Heavy infantry (50), Headquarters (50), Wall (1), Vehicule hero (1), Infantry hero (1), Heavy vehicule hero (1), Heavy infantry hero (1), Trap (0)
  * View range: 8
### Shooting

  * Time between start of clip and first shot: 900ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 900ms
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 200ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2160|2592|3024|3456|3888|4320|4752|5184|5616|6480|

### Projectile

  * Splash damage percentages: 100,75,50
  * _Not found: Beam damage_


|Level                       |1       |2       |3       |4       |5       |6       |7       |8       |9       |10      |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |1200.000|1440.000|1680.000|1920.000|2160.000|2400.000|2640.000|2880.000|3120.000|3600.000|
|Calculated damage per second|1200.000|1440.000|1680.000|1920.000|2160.000|2400.000|2640.000|2880.000|3120.000|3600.000|

  * Headquarters: 25%
  * Heavy infantry: 50%
  * Heavy vehicle: 250%
  * Other building: 25%
  * Droideka: 100%
  * Flying infantry: 50%
  * Flying vehicle: 300%
  * Support troop: 50%
  * Heavy infantry hero: 50%
  * Heavy vehicule hero: 250%
  * Infantry hero: 50%
  * Vehicule hero: 300%
  * Infantry: 50%
  * Ressource generator: 25%
  * Shield: 25%
  * Shield generator: 25%
  * Storage: 25%
  * Trap: 200%
  * Turret: 200%
  * Light vehicle: 300%
  * Wall: 80%
  * Cannons per sequence: 1
  * Cliptime: 1.800s
  * Directional: No
  * Is deflectable: No
  * Max speed: 12
  * Pass through shield: No
  * Salvos: 1
  * _Not found: Length segments, Width segments_
## Other stats

### Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: MHC
  * _Not found: Ability, Apply buffs, Death projectile, Death projectile damage, Death projectile delay, Death projectile distance, Hero data, Projectile type, Self buff, Spawn apply buffs, Upgrade shard uid_
### Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: umhc_emp-ani
  * Audio attack: "sfx_attack_empire_umhc_1":33,"sfx_attack_empire_umhc_2":33,"sfx_attack_empire_umhc_3":34
  * Audio death: "sfx_death_empire_umhc_1":100
  * Audio placement: "sfx_placement_empire_atat_1":100
  * Buff asset offset: 0.00,0.90,0
  * Bundle name: umhc_emp-ani
  * Factory rotation: 90
  * Factory scale factor: 1
  * Gun position: "umhc_emp_rig_MASTER_MOVER/umhc_emp_rig_locator_gun":1
  * Icon camera position: 30.35,41.15,37.35
  * Icon lookat position: -0.33,0.73,-0.17
  * Targeted type: ENEMIES
  * _Not found: Audio impact, Audio train, Death animation, Decal asset name, Decal bundle name, Decal size, Effect type, Event button action, Event button data, Event button string, Event features string, Hologram uid, Icon closeup camera position, Icon closeup lookat position, Icon unlock position, Icon unlock rotation, Icon unlock scale, Info UI type, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament_
### Attack presentation stats

  * Animation delay: 0
  * Favorite target type: turret
  * Arcs: No
  * Bullet: fx_UMHC_projectile_r_lrg
  * Hit spark: fx_UMHC_hit_r_lrg
  * Max scale: 100
  * Muzzle flash: fx_UMHC_muzzle_r_lrg
  * Name: projectileMHC
  * Spin speed: 0
  * _Not found: Charge asset name, Ground bullet, Muzzle flash fade time, Projectile length, S transition_

|Level                      |1       |2       |3       |4       |5       |6       |7       |8       |9       |10      |
|---------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second|1200.000|1440.000|1680.000|1920.000|2160.000|2400.000|2640.000|2880.000|3120.000|3600.000|

### Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Splash: 0
  * Target in range modifier: 1
  * Xp: 0


|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |130701|130702|130703|130704|130705|130706|130707|130708|130709|130710|
|Point value|12.000|14.400|16.800|19.200|21.600|24.000|26.400|28.800|31.200|36.000|

### Uninterpreted attack stats

  * Arming delay: 0
  * Seeks target: No
  * Streams: no
  * Strict cool down: No
  * _Not found: S1 time, S2 time_
