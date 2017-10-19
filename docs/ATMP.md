---
title: AT-MP (ATMP)
category: unit
---

# AT-MP (ATMP) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 15
  * Type: vehicle
  * _Not found: Buff health, Can be given, Unlock planet_

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|10800|11420|12080|12780|13520|14320|15160|16070|17030|18050|


### Training stats

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|4m                             |4m2s                                   |4m4s                                   |4m7s                                   |4m10s                                  |4m20s                                  |4m30s                                  |7m                                     |7m15s                                  |7m30s                                   |
|Training cost|1650$                          |1720$                                  |1790$                                  |1870$                                  |1950$                                  |2250$                                  |2550$                                  |3000$                                  |3150$                                  |3450$                                   |
|Building     |[Factory 4](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |1h   |2h30m |7h    |20h   |2d12h  |4d     |6d     |1w1d    |2w      |
|Upgrade requirements|5000$|5000$|10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|


### Move stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 2
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x1
  * _Not found: Ignores walls, Support follow distance_

## Main attack : ATMP

### Targeting

  * Attack shield border: Yes
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 2000
  * Target preference strength: 90
  * Target preferences: **Shield (90)**, **Shield generator (90)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 10

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,3,5,2,4,6
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 4
  * Time between shots: 200ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2310|2440|2580|2730|2890|3060|3240|3430|3630|3850|


### Projectile

  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1       |2       |3       |4       |5       |6       |7       |8       |9       |10      |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |3240    |3420    |3620    |3830    |4060    |4290    |4550    |4810    |5090    |5400    |
|Calculated damage per second|3242.105|3424.561|3621.053|3831.579|4056.140|4294.737|4547.368|4814.035|5094.737|5403.509|


  * Cannons per sequence: 6
  * Cliptime: 2.850s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 12
  * Damage multipliers: **(400%)**: Shield, Shield generator, **(100%)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75%)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(60%)**: Wall
  * Pass through shield: No
  * Salvos: 4
  * _Not found: Length segments, Width segments_

## Other stats

### Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ATMP
  * _Not found: Ability, Apply buffs, Death projectile, Hero data, Projectile type, Self buff, Spawn apply buffs, Upgrade shard uid_

### Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: atmp_emp-ani
  * Audio attack: "sfx_attack_empire_atmp_1":35,"sfx_attack_empire_atmp_2":35,"sfx_attack_empire_atmp_3":30
  * Audio death: "sfx_death_empire_atmp_1":100
  * Audio impact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * Audio placement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * Buff asset offset: 0.00,3.0,0.00
  * Bundle name: atmp_emp-ani
  * Factory rotation: -90
  * Factory scale factor: 0.8910000000000000142108547152020037174224853515625
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Icon camera position: 22.45,15.49,39.24
  * Icon lookat position: -0.73,2.62,-0.75
  * Targeted type: ENEMIES
  * _Not found: Audio train, Death animation, Decal asset name, Decal bundle name, Decal size, Effect type, Event button action, Event button data, Event button string, Event features string, Hologram uid, Icon closeup camera position, Icon closeup lookat position, Icon unlock position, Icon unlock rotation, Icon unlock scale, Info UI type, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament_

### Attack presentation stats

  * Animation delay: 0
  * Favorite target type: shieldGenerator
  * Arcs: No
  * Bullet: fx_rocket_projectile_r_sm
  * Hit spark: fx_rocket_hit_r_sm
  * Max scale: 100
  * Muzzle flash: fx_rocket_muzzle_r_sm
  * Name: ATMP
  * Spin speed: 0
  * _Not found: Charge asset name, Ground bullet, Muzzle flash fade time, Projectile length, S transition_

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|3240|3420|3620|3830|4060|4290|4550|4810|5090|5400|


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
|Order      |130401|130402|130403|130404|130405|130406|130407|130408|130409|130410|
|Point value|15    |18    |21    |24    |27    |30    |33    |36    |39    |45    |


### Uninterpreted attack stats

  * Arming delay: 0
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: No
  * _Not found: S1 time, S2 time_

