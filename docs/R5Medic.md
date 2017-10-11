---
title: Imperial Astromedic (R5Medic)
category: unit
---

# Imperial Astromedic (R5Medic) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: healerInfantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Healer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry
  * _Not found: Can be given, Shield asset name, Unlock planet_

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|11700|12400|13100|13900|14600|15300|16000|16800|18100|19500|

### Training stats

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|1m40s                            |1m50s                                  |1m55s                                  |2m                                     |2m5s                                   |2m10s                                  |2m15s                                  |2m20s                                  |2m25s                                  |2m30s                                   |
|Training cost|250$                             |350$                                   |450$                                   |550$                                   |650$                                   |750$                                   |850$                                   |1000$                                  |1050$                                  |1150$                                   |
|Building     |[Barracks 2](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * Support follow distance: 5
  * _Not found: Ignores walls_

## Main attack : Medic

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854.000
  * Target preference strength: 90
  * Target preferences: **Infantry (50)**, **Infantry hero (50)**, **Heavy infantry (50)**, **Heavy infantry hero (50)**, Ressource generator (0), Headquarters (0), Other building (0), Support troop (0), Heavy vehicle (0), Droideka (0), Turret (0), Heavy vehicule hero (0), Flying infantry (0), Storage (0), Light vehicle (0), Shield generator (0), Vehicule hero (0), Shield (0), Flying vehicle (0), Wall (0), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 50ms
  * Clip retargeting: No
  * Damage per shot: 0
  * Gun shooting sequence: 1
  * Impact delay: 250ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 15m
  * Retargeting offset: 10
  * Self-centered targeting: Yes
  * Shot count: 2
  * Time between shots: 400ms
  * Splash: 0
  * Target locking: Yes
  * _Not found: New target on reload_

### Projectile

  * Calculated damage per second: 0.000
  * Splash damage percentages: 100,100,100,100
  * _Not found: Beam damage_

|Level                      |1       |2       |3       |4       |5       |6       |7       |8       |9       |10      |
|---------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second|1550.000|1710.000|1810.000|1910.000|2010.000|2110.000|2210.000|2310.000|2490.000|2690.000|

  * Headquarters: 0%
  * Heavy infantry: 0%
  * Heavy vehicle: 0%
  * Other building: 0%
  * Droideka: 0%
  * Flying infantry: 0%
  * Flying vehicle: 0%
  * Support troop: 0%
  * Heavy infantry hero: 0%
  * Heavy vehicule hero: 0%
  * Infantry hero: 0%
  * Vehicule hero: 0%
  * Infantry: 0%
  * Ressource generator: 0%
  * Shield: 0%
  * Shield generator: 0%
  * Storage: 0%
  * Trap: 0%
  * Turret: 0%
  * Light vehicle: 0%
  * Wall: 0%

  * Cannons per sequence: 1
  * Cliptime: 1.350s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Pass through shield: No
  * Salvos: 2
  * _Not found: Length segments, Width segments_

## Other stats

### Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: R5Medic
  * Upgrade shard uid: shrd_troopR5Medic
  * _Not found: Ability, Death projectile, Death projectile damage, Death projectile delay, Death projectile distance, Hero data, Self buff, Spawn apply buffs_

|Level      |1           |2           |3           |4           |5           |6           |7           |8           |9           |10           |
|-----------|------------|------------|------------|------------|------------|------------|------------|------------|------------|-------------|
|Apply buffs|buffAdvHeal1|buffAdvHeal2|buffAdvHeal3|buffAdvHeal4|buffAdvHeal5|buffAdvHeal6|buffAdvHeal7|buffAdvHeal8|buffAdvHeal9|buffAdvHeal10|

### Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: r5droid_emp-ani
  * Audio attack: "sfx_attack_droid_medic_1":50,"sfx_attack_droid_medic_2":50
  * Audio death: "sfx_death_droid_r5_01":50,"sfx_death_droid_r5_02":50
  * Audio placement: "sfx_placement_droid_r5_01":50,"sfx_placement_droid_r5_02":50
  * Audio train: "sfx_ui_unitcomplete_r5droid_01":50,"sfx_ui_unitcomplete_r5droid_02":50
  * Bundle name: r5droid_emp-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Icon camera position: 5.21,9.06,13.12
  * Icon lookat position: -0.19,0.88,-0.37
  * Info UI type: Healer
  * Targeted type: ALLIES
  * Unlocked by event: true
  * _Not found: Audio impact, Buff asset offset, Death animation, Decal asset name, Decal bundle name, Decal size, Effect type, Gun position, Hologram uid, Icon closeup camera position, Icon closeup lookat position, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by tournament_

|Level               |1    |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|--------------------|-----|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Icon unlock position|0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation|0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale   |1,1,1|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|

### Attack presentation stats

  * Animation delay: 0
  * Favorite target type: infantry
  * Arcs: No
  * Max scale: 200
  * Muzzle flash: fx_healing_ring
  * Name: Medic
  * Spin speed: 0
  * _Not found: Bullet, Charge asset name, Ground bullet, Hit spark, Muzzle flash fade time, Projectile length, S transition_

|Level                      |1       |2       |3       |4       |5       |6       |7       |8       |9       |10      |
|---------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second|1550.000|1710.000|1810.000|1910.000|2010.000|2110.000|2210.000|2310.000|2490.000|2690.000|

* This is the damage per second displayed in-game, but may not be the same as the real damage per second.

### Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |134401|134402|134403|134404|134405|134406|134407|134408|134409|134410|
|Point value|5.000 |6.000 |7.000 |8.000 |9.000 |10.000|11.000|12.000|13.000|15.000|

### Uninterpreted attack stats

  * Arming delay: 0
  * Seeks target: No
  * Streams: no
  * Strict cool down: No
  * _Not found: S1 time, S2 time_

I could not show the following roles, because I was not programmed to : abilityunknown, abilityprefs, abilitystats, abilityonly, projectilemisc, abilitypresentation, abilitymove