---
title: Rodian Recon Sniper (RodianSample)
category: unit
---

# Rodian Recon Sniper (RodianSample) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: No
  * Role: Striker
  * Unit capacity: 7
  * Type: infantry
  * _Not found: Buff health, Can be given, Shield cooldown, Shield health, Shield range, Unlock planet_

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2800|3360|3920|4480|5040|5600|6160|6720|7280|8400|


### Training stats

  * Training time: 0s
  * Training cost: Free

### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: Nothing

### Move stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * _Not found: Ignores walls, Support follow distance_

## Main attack : projectileSniper

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (60)**, **Flying infantry (60)**, **Heavy infantry (60)**, **Infantry (60)**, **Support troop (60)**, Flying vehicle (50), Headquarters (50), Heavy vehicle (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * New target on reload: No
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 1.500s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 5
  * Time between shots: 500ms
  * Target locking: No

|Level          |1  |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|---|----|----|----|----|----|----|----|----|----|
|Damage per shot|835|1001|1168|1335|1502|1669|1836|2002|2169|2503|


### Projectile

  * Splash damage percentages: 100
  * _Not found: Beam damage_

|Level                       |1       |2       |3       |4   |5       |6       |7   |8       |9   |10      |
|----------------------------|--------|--------|--------|----|--------|--------|----|--------|----|--------|
|Displayed damage per second |2195    |2745    |3365    |4040|4765    |5565    |6415|7315    |8275|9980    |
|Calculated damage per second|1113.333|1334.667|1557.333|1780|2002.667|2225.333|2448|2669.333|2892|3337.333|


  * Cannons per sequence: 1
  * Cliptime: 3.750s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(300%)**: Flying infantry, Infantry, Infantry hero, Support troop, **(250%)**: Heavy infantry, Heavy infantry hero, **(200%)**: Flying vehicle, Light vehicle, Vehicule hero, **(150%)**: Heavy vehicle, Heavy vehicule hero, **(100%)**: Droideka, Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(50%)**: Shield, Shield generator, **(40%)**: Wall
  * Pass through shield: No
  * Salvos: 5
  * _Not found: Length segments, Width segments_

## Other stats

### Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RodianSample
  * _Not found: Ability, Apply buffs, Death projectile, Hero data, Projectile type, Self buff, Upgrade shard uid_

|Level            |1                                                        |2                                                        |3                                                        |4                                                        |5                                                        |6                                                        |7                                                        |8                                                        |9                                                        |10                                                          |
|-----------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------|
|Spawn apply buffs|buffSniperHealth1,buffSniperDamage1,buffSumPhtmTieBomber1|buffSniperHealth2,buffSniperDamage2,buffSumPhtmTieBomber2|buffSniperHealth3,buffSniperDamage3,buffSumPhtmTieBomber3|buffSniperHealth4,buffSniperDamage4,buffSumPhtmTieBomber4|buffSniperHealth5,buffSniperDamage5,buffSumPhtmTieBomber5|buffSniperHealth6,buffSniperDamage6,buffSumPhtmTieBomber6|buffSniperHealth7,buffSniperDamage7,buffSumPhtmTieBomber7|buffSniperHealth8,buffSniperDamage8,buffSumPhtmTieBomber8|buffSniperHealth9,buffSniperDamage9,buffSumPhtmTieBomber9|buffSniperHealth10,buffSniperDamage10,buffSumPhtmTieBomber10|


### Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: rodiansniper_emp-ani
  * Audio attack: "sfx_attack_ig86_01":33,"sfx_attack_ig86_02":33,"sfx_attack_ig86_03":34
  * Audio death: "sfx_death_rodian_1":33,"sfx_death_rodian_2":33,"sfx_death_rodian_3":34
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rodian_01":50,"sfx_ui_unitcomplete_rodian_02":50
  * Bundle name: rodiansniper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Icon camera position: 5.8,8.85,16.13
  * Icon closeup camera position: 2.41,5.49,9.51
  * Icon closeup lookat position: -0.33,1.97,-1.12
  * Icon lookat position: -0.51,1.24,-0.7
  * Targeted type: ENEMIES
  * _Not found: Audio impact, Buff asset offset, Decal asset name, Decal bundle name, Decal size, Effect type, Event button action, Event button data, Event button string, Event features string, Gun position, Hologram uid, Icon unlock position, Icon unlock rotation, Icon unlock scale, Info UI type, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament_

### Attack presentation stats

  * Animation delay: 0
  * Favorite target type: heroes
  * Arcs: No
  * Bullet: fx_blaster_beam_r_sm
  * Hit spark: fx_blaster_hit_r_sm
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: projectileSniper
  * Spin speed: 0
  * _Not found: Charge asset name, Ground bullet, Muzzle flash fade time, Projectile length, S transition_

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|2195|2745|3365|4040|4765|5565|6415|7315|8275|9980|


### Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Point value: 1
  * Xp: 0
  * _Not found: Splash, Target in range modifier_

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|314600|314601|314602|314603|314604|314605|314606|314607|314608|314609|


### Uninterpreted attack stats

  * Arming delay: 0
  * Seeks target: No
  * Streams: no
  * Strict cool down: No
  * _Not found: S1 time, S2 time_
