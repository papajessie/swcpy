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
  * _Not found: Can be given, Name, Shield cooldown, Shield health, Shield range, Unlock planet_

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2800|3360|3920|4480|5040|5600|6160|6720|7280|8400|


### Training stats

  * Training time: 0s
  * Training cost: Free

### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: Nothing

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
  * _Not found: Ignores walls, Support follow distance_

### Modifiers

#### Modifier "Sum phtm tie bomber"

  * Sum phtm tie bomber apply value as: absolute
  * Sum phtm tie bomber buff ID: buffSumPhtmTieBomber
  * Sum phtm tie bomber duration: permanent
  * Sum phtm tie bomber modifier: summon
  * Sum phtm tie bomber ms first proc: 0s
  * Sum phtm tie bomber ms per proc: permanent
  * Sum phtm tie bomber stack: 1
  * Sum phtm tie bomber target: self
  * Sum phtm tie bomber value: 1
  * _Not found: Sum phtm tie bomber mults_

|Level                  |1                    |2                    |3                    |4                    |5                    |6                    |7                    |8                    |9                    |10                    |
|-----------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|----------------------|
|Sum phtm tie bomber lvl|1                    |2                    |3                    |4                    |5                    |6                    |7                    |8                    |9                    |10                    |
|Sum phtm tie bomber uid|buffSumPhtmTieBomber1|buffSumPhtmTieBomber2|buffSumPhtmTieBomber3|buffSumPhtmTieBomber4|buffSumPhtmTieBomber5|buffSumPhtmTieBomber6|buffSumPhtmTieBomber7|buffSumPhtmTieBomber8|buffSumPhtmTieBomber9|buffSumPhtmTieBomber10|


#### Modifier "Sniper damage"

  * Sniper damage apply value as: relativePercent
  * Sniper damage buff ID: buffSniperDamage
  * Sniper damage duration: permanent
  * Sniper damage modifier: damage
  * Sniper damage ms first proc: 0s
  * Sniper damage ms per proc: permanent
  * Sniper damage stack: 0
  * Sniper damage target: self
  * _Not found: Sniper damage mults_

|Level              |1                |2                |3                |4                |5                |6                |7                |8                |9                |10                |
|-------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|
|Sniper damage lvl  |1                |2                |3                |4                |5                |6                |7                |8                |9                |10                |
|Sniper damage uid  |buffSniperDamage1|buffSniperDamage2|buffSniperDamage3|buffSniperDamage4|buffSniperDamage5|buffSniperDamage6|buffSniperDamage7|buffSniperDamage8|buffSniperDamage9|buffSniperDamage10|
|Sniper damage value|49               |53               |58               |64               |69               |75               |81               |87               |93               |100               |


#### Modifier "Sniper health"

  * Sniper health apply value as: relativePercentOfMax
  * Sniper health buff ID: buffSniperHealth
  * Sniper health duration: permanent
  * Sniper health modifier: maxHealth
  * Sniper health ms first proc: 0s
  * Sniper health ms per proc: permanent
  * Sniper health stack: 0
  * Sniper health target: self
  * _Not found: Sniper health mults_

|Level              |1                |2                |3                |4                |5                |6                |7                |8                |9                |10                |
|-------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|
|Sniper health lvl  |1                |2                |3                |4                |5                |6                |7                |8                |9                |10                |
|Sniper health uid  |buffSniperHealth1|buffSniperHealth2|buffSniperHealth3|buffSniperHealth4|buffSniperHealth5|buffSniperHealth6|buffSniperHealth7|buffSniperHealth8|buffSniperHealth9|buffSniperHealth10|
|Sniper health value|49               |53               |58               |64               |69               |75               |81               |87               |93               |100               |


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
  * _Not found: Asset name, Asset profile, Audio ability event, Audio impact, Buff asset offset, Bundle name, Charge asset name, Death attack S transition, Death attack arcs, Death attack bullet, Death attack charge asset name, Death attack ground bullet, Death attack hit spark, Death attack max scale, Death attack muzzle flash, Death attack muzzle flash fade time, Death attack name, Death attack projectile length, Death attack spin speed, Decal asset name, Decal bundle name, Decal size, Defend splash asset name, Defend splash asset profile, Defend splash audio ability event, Defend splash bundle name, Defend splash impact asset name empire, Defend splash impact asset name rebel, Defend splash muzzle asset name empire, Defend splash muzzle asset name rebel, Defend splash projectile attachment bundle, Effect type, Event button action, Event button data, Event button string, Event features string, Ground bullet, Gun position, Hologram uid, Icon unlock position, Icon unlock rotation, Icon unlock scale, Impact asset name empire, Impact asset name rebel, Info UI type, Invulnerable asset name, Invulnerable asset profile, Invulnerable audio ability event, Invulnerable bundle name, Invulnerable impact asset name empire, Invulnerable impact asset name rebel, Invulnerable muzzle asset name empire, Invulnerable muzzle asset name rebel, Invulnerable projectile attachment bundle, Marksman damage asset name, Marksman damage asset profile, Marksman damage audio ability event, Marksman damage bundle name, Marksman damage impact asset name empire, Marksman damage impact asset name rebel, Marksman damage muzzle asset name empire, Marksman damage muzzle asset name rebel, Marksman damage projectile attachment bundle, Marksman health asset name, Marksman health asset profile, Marksman health audio ability event, Marksman health bundle name, Marksman health impact asset name empire, Marksman health impact asset name rebel, Marksman health muzzle asset name empire, Marksman health muzzle asset name rebel, Marksman health projectile attachment bundle, Muzzle asset name empire, Muzzle asset name rebel, Muzzle flash fade time, Personal shield ithorian asset name, Personal shield ithorian asset profile, Personal shield ithorian audio ability event, Personal shield ithorian bundle name, Personal shield ithorian impact asset name empire, Personal shield ithorian impact asset name rebel, Personal shield ithorian muzzle asset name empire, Personal shield ithorian muzzle asset name rebel, Personal shield ithorian projectile attachment bundle, Personal shield kubaz asset name, Personal shield kubaz asset profile, Personal shield kubaz audio ability event, Personal shield kubaz bundle name, Personal shield kubaz impact asset name empire, Personal shield kubaz impact asset name rebel, Personal shield kubaz muzzle asset name empire, Personal shield kubaz muzzle asset name rebel, Personal shield kubaz projectile attachment bundle, Projectile attachment bundle, Projectile length, Reduce heals asset name, Reduce heals asset profile, Reduce heals audio ability event, Reduce heals bundle name, Reduce heals impact asset name empire, Reduce heals impact asset name rebel, Reduce heals muzzle asset name empire, Reduce heals muzzle asset name rebel, Reduce heals projectile attachment bundle, S transition, Secondary attack S transition, Secondary attack alt gun locators, Secondary attack animation delay, Secondary attack arcs, Secondary attack audio ability activate, Secondary attack audio ability attack, Secondary attack audio ability loop, Secondary attack bullet, Secondary attack charge asset name, Secondary attack displayed damage per second, Secondary attack favorite target type, Secondary attack ground bullet, Secondary attack hit spark, Secondary attack max scale, Secondary attack muzzle flash, Secondary attack muzzle flash fade time, Secondary attack name, Secondary attack name, Secondary attack persistent effect, Secondary attack persistent scaling, Secondary attack projectile length, Secondary attack spin speed, Secondary attack weapon trail FX params, Shield asset name, Sniper damage asset name, Sniper damage asset profile, Sniper damage audio ability event, Sniper damage bundle name, Sniper damage impact asset name empire, Sniper damage impact asset name rebel, Sniper damage muzzle asset name empire, Sniper damage muzzle asset name rebel, Sniper damage projectile attachment bundle, Sniper health asset name, Sniper health asset profile, Sniper health audio ability event, Sniper health bundle name, Sniper health impact asset name empire, Sniper health impact asset name rebel, Sniper health muzzle asset name empire, Sniper health muzzle asset name rebel, Sniper health projectile attachment bundle, Spawn effect uid, Sum phtm X wing asset name, Sum phtm X wing asset profile, Sum phtm X wing audio ability event, Sum phtm X wing bundle name, Sum phtm X wing impact asset name empire, Sum phtm X wing impact asset name rebel, Sum phtm X wing muzzle asset name empire, Sum phtm X wing muzzle asset name rebel, Sum phtm X wing projectile attachment bundle, Sum phtm Y wing asset name, Sum phtm Y wing asset profile, Sum phtm Y wing audio ability event, Sum phtm Y wing bundle name, Sum phtm Y wing impact asset name empire, Sum phtm Y wing impact asset name rebel, Sum phtm Y wing muzzle asset name empire, Sum phtm Y wing muzzle asset name rebel, Sum phtm Y wing projectile attachment bundle, Sum phtm tie bomber asset name, Sum phtm tie bomber asset profile, Sum phtm tie bomber audio ability event, Sum phtm tie bomber bundle name, Sum phtm tie bomber impact asset name empire, Sum phtm tie bomber impact asset name rebel, Sum phtm tie bomber muzzle asset name empire, Sum phtm tie bomber muzzle asset name rebel, Sum phtm tie bomber projectile attachment bundle, Sum phtm tie fighter asset name, Sum phtm tie fighter asset profile, Sum phtm tie fighter audio ability event, Sum phtm tie fighter bundle name, Sum phtm tie fighter impact asset name empire, Sum phtm tie fighter impact asset name rebel, Sum phtm tie fighter muzzle asset name empire, Sum phtm tie fighter muzzle asset name rebel, Sum phtm tie fighter projectile attachment bundle, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament_

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
  * Sniper damage is refreshing: No
  * Sniper damage tags: damage
  * Sniper health is refreshing: No
  * Sniper health tags: maxHealth
  * Streams: no
  * Strict cool down: No
  * Xp: 0
  * _Not found: Asset offset type, Cancel tags, Death attack S1 time, Death attack S2 time, Death attack seeks target, Death attack streams, Defend splash asset offset type, Defend splash cancel tags, Defend splash details, Defend splash is refreshing, Defend splash prevent tags, Defend splash shader override, Defend splash tags, Details, Invulnerable asset offset type, Invulnerable cancel tags, Invulnerable details, Invulnerable is refreshing, Invulnerable prevent tags, Invulnerable shader override, Invulnerable tags, Is refreshing, Marksman damage asset offset type, Marksman damage cancel tags, Marksman damage details, Marksman damage is refreshing, Marksman damage prevent tags, Marksman damage shader override, Marksman damage tags, Marksman health asset offset type, Marksman health cancel tags, Marksman health details, Marksman health is refreshing, Marksman health prevent tags, Marksman health shader override, Marksman health tags, Personal shield ithorian asset offset type, Personal shield ithorian cancel tags, Personal shield ithorian details, Personal shield ithorian is refreshing, Personal shield ithorian prevent tags, Personal shield ithorian shader override, Personal shield ithorian tags, Personal shield kubaz asset offset type, Personal shield kubaz cancel tags, Personal shield kubaz details, Personal shield kubaz is refreshing, Personal shield kubaz prevent tags, Personal shield kubaz shader override, Personal shield kubaz tags, Prevent tags, Reduce heals asset offset type, Reduce heals cancel tags, Reduce heals details, Reduce heals is refreshing, Reduce heals prevent tags, Reduce heals shader override, Reduce heals tags, S1 time, S2 time, Secondary attack S1 time, Secondary attack S2 time, Secondary attack arming delay, Secondary attack clip count, Secondary attack kill cooldown reset, Secondary attack max speed, Secondary attack seeks target, Secondary attack streams, Secondary attack strict cool down, Shader override, Sniper damage asset offset type, Sniper damage cancel tags, Sniper damage details, Sniper damage prevent tags, Sniper damage shader override, Sniper health asset offset type, Sniper health cancel tags, Sniper health details, Sniper health prevent tags, Sniper health shader override, Splash, Sum phtm X wing asset offset type, Sum phtm X wing cancel tags, Sum phtm X wing details, Sum phtm X wing is refreshing, Sum phtm X wing prevent tags, Sum phtm X wing shader override, Sum phtm X wing tags, Sum phtm Y wing asset offset type, Sum phtm Y wing cancel tags, Sum phtm Y wing details, Sum phtm Y wing is refreshing, Sum phtm Y wing prevent tags, Sum phtm Y wing shader override, Sum phtm Y wing tags, Sum phtm tie bomber asset offset type, Sum phtm tie bomber cancel tags, Sum phtm tie bomber is refreshing, Sum phtm tie bomber prevent tags, Sum phtm tie bomber shader override, Sum phtm tie bomber tags, Sum phtm tie fighter asset offset type, Sum phtm tie fighter cancel tags, Sum phtm tie fighter details, Sum phtm tie fighter is refreshing, Sum phtm tie fighter prevent tags, Sum phtm tie fighter shader override, Sum phtm tie fighter tags, Tags, Target in range modifier_

|Level                      |1                |2                |3                |4                |5                |6                |7                |8                |9                |10                |
|---------------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|
|Order                      |314600           |314601           |314602           |314603           |314604           |314605           |314606           |314607           |314608           |314609            |
|Sum phtm tie bomber details|sumPhtmTieBomber1|sumPhtmTieBomber2|sumPhtmTieBomber3|sumPhtmTieBomber4|sumPhtmTieBomber5|sumPhtmTieBomber6|sumPhtmTieBomber7|sumPhtmTieBomber8|sumPhtmTieBomber9|sumPhtmTieBomber10|


I could not show the following roles, because I was not programmed to : buffSumPhtmTieBomberbasic, buffSniperHealthbasic, buffSniperHealthc, buffSumPhtmTieBomberc, buffSniperDamagebasic, buffSniperDamagec
