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
  * _Not found: Apply value as, Buff ID, Buff health, Can be given, Duration, Lvl, Modifier, Ms first proc, Ms per proc, Shield cooldown, Shield health, Shield range, Stack, Target, Uid, Unlock planet, Value_

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

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RodianSample
  * _Not found: Ability, Apply buffs, Death attack apply buffs, Death projectile, Hero data, Secondary attack apply buffs, Secondary attack projectile type, Secondary attack self buff, Upgrade shard uid_

|Level            |1                                                        |2                                                        |3                                                        |4                                                        |5                                                        |6                                                        |7                                                        |8                                                        |9                                                        |10                                                          |
|-----------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------|
|Spawn apply buffs|buffSniperHealth1,buffSniperDamage1,buffSumPhtmTieBomber1|buffSniperHealth2,buffSniperDamage2,buffSumPhtmTieBomber2|buffSniperHealth3,buffSniperDamage3,buffSumPhtmTieBomber3|buffSniperHealth4,buffSniperDamage4,buffSumPhtmTieBomber4|buffSniperHealth5,buffSniperDamage5,buffSumPhtmTieBomber5|buffSniperHealth6,buffSniperDamage6,buffSumPhtmTieBomber6|buffSniperHealth7,buffSniperDamage7,buffSumPhtmTieBomber7|buffSniperHealth8,buffSniperDamage8,buffSumPhtmTieBomber8|buffSniperHealth9,buffSniperDamage9,buffSumPhtmTieBomber9|buffSniperHealth10,buffSniperDamage10,buffSumPhtmTieBomber10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: rodiansniper_emp-ani
  * Audio attack: "sfx_attack_ig86_01":33,"sfx_attack_ig86_02":33,"sfx_attack_ig86_03":34
  * Audio death: "sfx_death_rodian_1":33,"sfx_death_rodian_2":33,"sfx_death_rodian_3":34
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rodian_01":50,"sfx_ui_unitcomplete_rodian_02":50
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: rodiansniper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: heroes
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 5.8,8.85,16.13
  * Icon closeup camera position: 2.41,5.49,9.51
  * Icon closeup lookat position: -0.33,1.97,-1.12
  * Icon lookat position: -0.51,1.24,-0.7
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: projectileSniper
  * Spin speed: 0
  * Targeted type: ENEMIES
  * _Not found: Asset name, Asset profile, Audio ability event, Audio impact, Buff asset offset, Bundle name, Charge asset name, Death attack S transition, Death attack arcs, Death attack bullet, Death attack charge asset name, Death attack ground bullet, Death attack hit spark, Death attack max scale, Death attack muzzle flash, Death attack muzzle flash fade time, Death attack name, Death attack projectile length, Death attack spin speed, Decal asset name, Decal bundle name, Decal size, Effect type, Event button action, Event button data, Event button string, Event features string, Ground bullet, Gun position, Hologram uid, Icon unlock position, Icon unlock rotation, Icon unlock scale, Impact asset name empire, Impact asset name rebel, Info UI type, Muzzle asset name empire, Muzzle asset name rebel, Muzzle flash fade time, Projectile attachment bundle, Projectile length, S transition, Secondary attack S transition, Secondary attack alt gun locators, Secondary attack animation delay, Secondary attack arcs, Secondary attack audio ability activate, Secondary attack audio ability attack, Secondary attack audio ability loop, Secondary attack bullet, Secondary attack charge asset name, Secondary attack displayed damage per second, Secondary attack favorite target type, Secondary attack ground bullet, Secondary attack hit spark, Secondary attack max scale, Secondary attack muzzle flash, Secondary attack muzzle flash fade time, Secondary attack name, Secondary attack name, Secondary attack persistent effect, Secondary attack persistent scaling, Secondary attack projectile length, Secondary attack spin speed, Secondary attack weapon trail FX params, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament, buffDefendSplash Asset name, buffDefendSplash Asset profile, buffDefendSplash Audio ability event, buffDefendSplash Bundle name, buffDefendSplash Impact asset name empire, buffDefendSplash Impact asset name rebel, buffDefendSplash Muzzle asset name empire, buffDefendSplash Muzzle asset name rebel, buffDefendSplash Projectile attachment bundle, buffInvulnerable Asset name, buffInvulnerable Asset profile, buffInvulnerable Audio ability event, buffInvulnerable Bundle name, buffInvulnerable Impact asset name empire, buffInvulnerable Impact asset name rebel, buffInvulnerable Muzzle asset name empire, buffInvulnerable Muzzle asset name rebel, buffInvulnerable Projectile attachment bundle, buffMarksmanDamage Asset name, buffMarksmanDamage Asset profile, buffMarksmanDamage Audio ability event, buffMarksmanDamage Bundle name, buffMarksmanDamage Impact asset name empire, buffMarksmanDamage Impact asset name rebel, buffMarksmanDamage Muzzle asset name empire, buffMarksmanDamage Muzzle asset name rebel, buffMarksmanDamage Projectile attachment bundle, buffMarksmanHealth Asset name, buffMarksmanHealth Asset profile, buffMarksmanHealth Audio ability event, buffMarksmanHealth Bundle name, buffMarksmanHealth Impact asset name empire, buffMarksmanHealth Impact asset name rebel, buffMarksmanHealth Muzzle asset name empire, buffMarksmanHealth Muzzle asset name rebel, buffMarksmanHealth Projectile attachment bundle, buffPersonalShieldIthorian Asset name, buffPersonalShieldIthorian Asset profile, buffPersonalShieldIthorian Audio ability event, buffPersonalShieldIthorian Bundle name, buffPersonalShieldIthorian Impact asset name empire, buffPersonalShieldIthorian Impact asset name rebel, buffPersonalShieldIthorian Muzzle asset name empire, buffPersonalShieldIthorian Muzzle asset name rebel, buffPersonalShieldIthorian Projectile attachment bundle, buffPersonalShieldKubaz Asset name, buffPersonalShieldKubaz Asset profile, buffPersonalShieldKubaz Audio ability event, buffPersonalShieldKubaz Bundle name, buffPersonalShieldKubaz Impact asset name empire, buffPersonalShieldKubaz Impact asset name rebel, buffPersonalShieldKubaz Muzzle asset name empire, buffPersonalShieldKubaz Muzzle asset name rebel, buffPersonalShieldKubaz Projectile attachment bundle, buffReduceHeals Asset name, buffReduceHeals Asset profile, buffReduceHeals Audio ability event, buffReduceHeals Bundle name, buffReduceHeals Impact asset name empire, buffReduceHeals Impact asset name rebel, buffReduceHeals Muzzle asset name empire, buffReduceHeals Muzzle asset name rebel, buffReduceHeals Projectile attachment bundle, buffSniperDamage Asset name, buffSniperDamage Asset profile, buffSniperDamage Audio ability event, buffSniperDamage Bundle name, buffSniperDamage Impact asset name empire, buffSniperDamage Impact asset name rebel, buffSniperDamage Muzzle asset name empire, buffSniperDamage Muzzle asset name rebel, buffSniperDamage Projectile attachment bundle, buffSniperHealth Asset name, buffSniperHealth Asset profile, buffSniperHealth Audio ability event, buffSniperHealth Bundle name, buffSniperHealth Impact asset name empire, buffSniperHealth Impact asset name rebel, buffSniperHealth Muzzle asset name empire, buffSniperHealth Muzzle asset name rebel, buffSniperHealth Projectile attachment bundle, buffSumPhtmTieBomber Asset name, buffSumPhtmTieBomber Asset profile, buffSumPhtmTieBomber Audio ability event, buffSumPhtmTieBomber Bundle name, buffSumPhtmTieBomber Impact asset name empire, buffSumPhtmTieBomber Impact asset name rebel, buffSumPhtmTieBomber Muzzle asset name empire, buffSumPhtmTieBomber Muzzle asset name rebel, buffSumPhtmTieBomber Projectile attachment bundle, buffSumPhtmTieFighter Asset name, buffSumPhtmTieFighter Asset profile, buffSumPhtmTieFighter Audio ability event, buffSumPhtmTieFighter Bundle name, buffSumPhtmTieFighter Impact asset name empire, buffSumPhtmTieFighter Impact asset name rebel, buffSumPhtmTieFighter Muzzle asset name empire, buffSumPhtmTieFighter Muzzle asset name rebel, buffSumPhtmTieFighter Projectile attachment bundle, buffSumPhtmXWing Asset name, buffSumPhtmXWing Asset profile, buffSumPhtmXWing Audio ability event, buffSumPhtmXWing Bundle name, buffSumPhtmXWing Impact asset name empire, buffSumPhtmXWing Impact asset name rebel, buffSumPhtmXWing Muzzle asset name empire, buffSumPhtmXWing Muzzle asset name rebel, buffSumPhtmXWing Projectile attachment bundle, buffSumPhtmYWing Asset name, buffSumPhtmYWing Asset profile, buffSumPhtmYWing Audio ability event, buffSumPhtmYWing Bundle name, buffSumPhtmYWing Impact asset name empire, buffSumPhtmYWing Impact asset name rebel, buffSumPhtmYWing Muzzle asset name empire, buffSumPhtmYWing Muzzle asset name rebel, buffSumPhtmYWing Projectile attachment bundle_

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|2195|2745|3365|4040|4765|5565|6415|7315|8275|9980|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Point value: 1
  * Seeks target: No
  * Streams: no
  * Strict cool down: No
  * Xp: 0
  * buffSniperDamage Is refreshing: false
  * buffSniperDamage Tags: damage
  * buffSniperHealth Is refreshing: false
  * buffSniperHealth Tags: maxHealth
  * _Not found: Asset offset type, Cancel tags, Death attack S1 time, Death attack S2 time, Death attack seeks target, Death attack streams, Details, Is refreshing, Prevent tags, S1 time, S2 time, Secondary attack S1 time, Secondary attack S2 time, Secondary attack arming delay, Secondary attack clip count, Secondary attack kill cooldown reset, Secondary attack max speed, Secondary attack seeks target, Secondary attack streams, Secondary attack strict cool down, Shader override, Splash, Tags, Target in range modifier, buffDefendSplash Asset offset type, buffDefendSplash Cancel tags, buffDefendSplash Details, buffDefendSplash Is refreshing, buffDefendSplash Prevent tags, buffDefendSplash Shader override, buffDefendSplash Tags, buffInvulnerable Asset offset type, buffInvulnerable Cancel tags, buffInvulnerable Details, buffInvulnerable Is refreshing, buffInvulnerable Prevent tags, buffInvulnerable Shader override, buffInvulnerable Tags, buffMarksmanDamage Asset offset type, buffMarksmanDamage Cancel tags, buffMarksmanDamage Details, buffMarksmanDamage Is refreshing, buffMarksmanDamage Prevent tags, buffMarksmanDamage Shader override, buffMarksmanDamage Tags, buffMarksmanHealth Asset offset type, buffMarksmanHealth Cancel tags, buffMarksmanHealth Details, buffMarksmanHealth Is refreshing, buffMarksmanHealth Prevent tags, buffMarksmanHealth Shader override, buffMarksmanHealth Tags, buffPersonalShieldIthorian Asset offset type, buffPersonalShieldIthorian Cancel tags, buffPersonalShieldIthorian Details, buffPersonalShieldIthorian Is refreshing, buffPersonalShieldIthorian Prevent tags, buffPersonalShieldIthorian Shader override, buffPersonalShieldIthorian Tags, buffPersonalShieldKubaz Asset offset type, buffPersonalShieldKubaz Cancel tags, buffPersonalShieldKubaz Details, buffPersonalShieldKubaz Is refreshing, buffPersonalShieldKubaz Prevent tags, buffPersonalShieldKubaz Shader override, buffPersonalShieldKubaz Tags, buffReduceHeals Asset offset type, buffReduceHeals Cancel tags, buffReduceHeals Details, buffReduceHeals Is refreshing, buffReduceHeals Prevent tags, buffReduceHeals Shader override, buffReduceHeals Tags, buffSniperDamage Asset offset type, buffSniperDamage Cancel tags, buffSniperDamage Details, buffSniperDamage Prevent tags, buffSniperDamage Shader override, buffSniperHealth Asset offset type, buffSniperHealth Cancel tags, buffSniperHealth Details, buffSniperHealth Prevent tags, buffSniperHealth Shader override, buffSumPhtmTieBomber Asset offset type, buffSumPhtmTieBomber Cancel tags, buffSumPhtmTieBomber Is refreshing, buffSumPhtmTieBomber Prevent tags, buffSumPhtmTieBomber Shader override, buffSumPhtmTieBomber Tags, buffSumPhtmTieFighter Asset offset type, buffSumPhtmTieFighter Cancel tags, buffSumPhtmTieFighter Details, buffSumPhtmTieFighter Is refreshing, buffSumPhtmTieFighter Prevent tags, buffSumPhtmTieFighter Shader override, buffSumPhtmTieFighter Tags, buffSumPhtmXWing Asset offset type, buffSumPhtmXWing Cancel tags, buffSumPhtmXWing Details, buffSumPhtmXWing Is refreshing, buffSumPhtmXWing Prevent tags, buffSumPhtmXWing Shader override, buffSumPhtmXWing Tags, buffSumPhtmYWing Asset offset type, buffSumPhtmYWing Cancel tags, buffSumPhtmYWing Details, buffSumPhtmYWing Is refreshing, buffSumPhtmYWing Prevent tags, buffSumPhtmYWing Shader override, buffSumPhtmYWing Tags_

|Level                       |1                |2                |3                |4                |5                |6                |7                |8                |9                |10                |
|----------------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|
|Order                       |314600           |314601           |314602           |314603           |314604           |314605           |314606           |314607           |314608           |314609            |
|buffSumPhtmTieBomber Details|sumPhtmTieBomber1|sumPhtmTieBomber2|sumPhtmTieBomber3|sumPhtmTieBomber4|sumPhtmTieBomber5|sumPhtmTieBomber6|sumPhtmTieBomber7|sumPhtmTieBomber8|sumPhtmTieBomber9|sumPhtmTieBomber10|


I could not show the following roles, because I was not programmed to : buffSniperHealthbasic, buffSumPhtmTieBomberbasic, buffSniperDamagebasic
