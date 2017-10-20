---
title: Heavy Soldier (HeavyRebel)
category: unit
---

# Heavy Soldier (HeavyRebel) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry
  * _Not found: Apply value as, Buff ID, Buff health, Can be given, Duration, Lvl, Modifier, Ms first proc, Ms per proc, Stack, Target, Uid, Unlock planet, Value_

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9    |10   |
|------|----|----|----|----|----|----|----|----|-----|-----|
|Health|4000|4800|5600|6400|7200|8000|8800|9600|10400|12000|


### Training stats

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|1m40s                           |1m50s                                 |1m55s                                 |2m                                    |2m5s                                  |2m10s                                 |2m15s                                 |2m20s                                 |2m25s                                 |2m30s                                  |
|Training cost|250$                            |350$                                  |450$                                  |550$                                  |650$                                  |750$                                  |850$                                  |1000$                                 |1050$                                 |1150$                                  |
|Building     |[Barracks 6](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w2d    |
|Upgrade requirements|3000$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


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

## Main attack : HeavyRebel

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 10
  * Time between shots: 100ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|221|266|310|354|398|442|487|531|575|663|


### Projectile

  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1  |2      |3      |4       |5       |6   |7       |8       |9       |10  |
|----------------------------|---|-------|-------|--------|--------|----|--------|--------|--------|----|
|Displayed damage per second |650|782    |911    |1041    |1170    |1300|1432    |1561    |1691    |1950|
|Calculated damage per second|650|782.353|911.765|1041.176|1170.588|1300|1432.353|1561.765|1691.176|1950|


  * Cannons per sequence: 1
  * Cliptime: 3.400s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 30
  * Damage multipliers: **(175%)**: Shield, Shield generator, **(100%)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Storage, Support troop, Trap, Turret, Vehicule hero, **(80%)**: Wall
  * Pass through shield: No
  * Salvos: 10
  * _Not found: Length segments, Width segments_

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: HeavyRebel
  * _Not found: Ability, Apply buffs, Death attack apply buffs, Death projectile, Hero data, Secondary attack apply buffs, Secondary attack projectile type, Secondary attack self buff, Spawn apply buffs, Upgrade shard uid_

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: heavysoldier_rbl-ani
  * Audio attack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Buff asset offset: 0.00,0.30,0.00
  * Bundle name: heavysoldier_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_gatling_hit_b_lrg
  * Icon camera position: 3.52,10.26,21.73
  * Icon closeup camera position: -0.24,0.29,11.62
  * Icon closeup lookat position: -0.13,2.39,0.83
  * Icon lookat position: -0.44,1.75,0.53
  * Max scale: 100
  * Muzzle flash: fx_gatling_muzzle_b_lrg
  * Name: HeavyRebel
  * Spin speed: 0
  * Targeted type: ENEMIES
  * _Not found: Asset name, Asset profile, Audio ability event, Audio impact, Bullet, Bundle name, Charge asset name, Death attack S transition, Death attack arcs, Death attack bullet, Death attack charge asset name, Death attack ground bullet, Death attack hit spark, Death attack max scale, Death attack muzzle flash, Death attack muzzle flash fade time, Death attack name, Death attack projectile length, Death attack spin speed, Decal asset name, Decal bundle name, Decal size, Effect type, Event button action, Event button data, Event button string, Event features string, Ground bullet, Hologram uid, Icon unlock position, Icon unlock rotation, Icon unlock scale, Impact asset name empire, Impact asset name rebel, Info UI type, Muzzle asset name empire, Muzzle asset name rebel, Muzzle flash fade time, Projectile attachment bundle, Projectile length, S transition, Secondary attack S transition, Secondary attack alt gun locators, Secondary attack animation delay, Secondary attack arcs, Secondary attack audio ability activate, Secondary attack audio ability attack, Secondary attack audio ability loop, Secondary attack bullet, Secondary attack charge asset name, Secondary attack displayed damage per second, Secondary attack favorite target type, Secondary attack ground bullet, Secondary attack hit spark, Secondary attack max scale, Secondary attack muzzle flash, Secondary attack muzzle flash fade time, Secondary attack name, Secondary attack name, Secondary attack persistent effect, Secondary attack persistent scaling, Secondary attack projectile length, Secondary attack spin speed, Secondary attack weapon trail FX params, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament, buffDefendSplash Asset name, buffDefendSplash Asset profile, buffDefendSplash Audio ability event, buffDefendSplash Bundle name, buffDefendSplash Impact asset name empire, buffDefendSplash Impact asset name rebel, buffDefendSplash Muzzle asset name empire, buffDefendSplash Muzzle asset name rebel, buffDefendSplash Projectile attachment bundle, buffInvulnerable Asset name, buffInvulnerable Asset profile, buffInvulnerable Audio ability event, buffInvulnerable Bundle name, buffInvulnerable Impact asset name empire, buffInvulnerable Impact asset name rebel, buffInvulnerable Muzzle asset name empire, buffInvulnerable Muzzle asset name rebel, buffInvulnerable Projectile attachment bundle, buffMarksmanDamage Asset name, buffMarksmanDamage Asset profile, buffMarksmanDamage Audio ability event, buffMarksmanDamage Bundle name, buffMarksmanDamage Impact asset name empire, buffMarksmanDamage Impact asset name rebel, buffMarksmanDamage Muzzle asset name empire, buffMarksmanDamage Muzzle asset name rebel, buffMarksmanDamage Projectile attachment bundle, buffMarksmanHealth Asset name, buffMarksmanHealth Asset profile, buffMarksmanHealth Audio ability event, buffMarksmanHealth Bundle name, buffMarksmanHealth Impact asset name empire, buffMarksmanHealth Impact asset name rebel, buffMarksmanHealth Muzzle asset name empire, buffMarksmanHealth Muzzle asset name rebel, buffMarksmanHealth Projectile attachment bundle, buffPersonalShieldIthorian Asset name, buffPersonalShieldIthorian Asset profile, buffPersonalShieldIthorian Audio ability event, buffPersonalShieldIthorian Bundle name, buffPersonalShieldIthorian Impact asset name empire, buffPersonalShieldIthorian Impact asset name rebel, buffPersonalShieldIthorian Muzzle asset name empire, buffPersonalShieldIthorian Muzzle asset name rebel, buffPersonalShieldIthorian Projectile attachment bundle, buffPersonalShieldKubaz Asset name, buffPersonalShieldKubaz Asset profile, buffPersonalShieldKubaz Audio ability event, buffPersonalShieldKubaz Bundle name, buffPersonalShieldKubaz Impact asset name empire, buffPersonalShieldKubaz Impact asset name rebel, buffPersonalShieldKubaz Muzzle asset name empire, buffPersonalShieldKubaz Muzzle asset name rebel, buffPersonalShieldKubaz Projectile attachment bundle, buffReduceHeals Asset name, buffReduceHeals Asset profile, buffReduceHeals Audio ability event, buffReduceHeals Bundle name, buffReduceHeals Impact asset name empire, buffReduceHeals Impact asset name rebel, buffReduceHeals Muzzle asset name empire, buffReduceHeals Muzzle asset name rebel, buffReduceHeals Projectile attachment bundle, buffSniperDamage Asset name, buffSniperDamage Asset profile, buffSniperDamage Audio ability event, buffSniperDamage Bundle name, buffSniperDamage Impact asset name empire, buffSniperDamage Impact asset name rebel, buffSniperDamage Muzzle asset name empire, buffSniperDamage Muzzle asset name rebel, buffSniperDamage Projectile attachment bundle, buffSniperHealth Asset name, buffSniperHealth Asset profile, buffSniperHealth Audio ability event, buffSniperHealth Bundle name, buffSniperHealth Impact asset name empire, buffSniperHealth Impact asset name rebel, buffSniperHealth Muzzle asset name empire, buffSniperHealth Muzzle asset name rebel, buffSniperHealth Projectile attachment bundle, buffSumPhtmTieBomber Asset name, buffSumPhtmTieBomber Asset profile, buffSumPhtmTieBomber Audio ability event, buffSumPhtmTieBomber Bundle name, buffSumPhtmTieBomber Impact asset name empire, buffSumPhtmTieBomber Impact asset name rebel, buffSumPhtmTieBomber Muzzle asset name empire, buffSumPhtmTieBomber Muzzle asset name rebel, buffSumPhtmTieBomber Projectile attachment bundle, buffSumPhtmTieFighter Asset name, buffSumPhtmTieFighter Asset profile, buffSumPhtmTieFighter Audio ability event, buffSumPhtmTieFighter Bundle name, buffSumPhtmTieFighter Impact asset name empire, buffSumPhtmTieFighter Impact asset name rebel, buffSumPhtmTieFighter Muzzle asset name empire, buffSumPhtmTieFighter Muzzle asset name rebel, buffSumPhtmTieFighter Projectile attachment bundle, buffSumPhtmXWing Asset name, buffSumPhtmXWing Asset profile, buffSumPhtmXWing Audio ability event, buffSumPhtmXWing Bundle name, buffSumPhtmXWing Impact asset name empire, buffSumPhtmXWing Impact asset name rebel, buffSumPhtmXWing Muzzle asset name empire, buffSumPhtmXWing Muzzle asset name rebel, buffSumPhtmXWing Projectile attachment bundle, buffSumPhtmYWing Asset name, buffSumPhtmYWing Asset profile, buffSumPhtmYWing Audio ability event, buffSumPhtmYWing Bundle name, buffSumPhtmYWing Impact asset name empire, buffSumPhtmYWing Impact asset name rebel, buffSumPhtmYWing Muzzle asset name empire, buffSumPhtmYWing Muzzle asset name rebel, buffSumPhtmYWing Projectile attachment bundle_

|Level                      |1  |2  |3  |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|---|---|---|----|----|----|----|----|----|----|
|Displayed damage per second|650|782|911|1041|1170|1300|1432|1561|1691|1950|


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
  * _Not found: Asset offset type, Cancel tags, Death attack S1 time, Death attack S2 time, Death attack seeks target, Death attack streams, Details, Is refreshing, Prevent tags, S1 time, S2 time, Secondary attack S1 time, Secondary attack S2 time, Secondary attack arming delay, Secondary attack clip count, Secondary attack kill cooldown reset, Secondary attack max speed, Secondary attack seeks target, Secondary attack streams, Secondary attack strict cool down, Shader override, Tags, buffDefendSplash Asset offset type, buffDefendSplash Cancel tags, buffDefendSplash Details, buffDefendSplash Is refreshing, buffDefendSplash Prevent tags, buffDefendSplash Shader override, buffDefendSplash Tags, buffInvulnerable Asset offset type, buffInvulnerable Cancel tags, buffInvulnerable Details, buffInvulnerable Is refreshing, buffInvulnerable Prevent tags, buffInvulnerable Shader override, buffInvulnerable Tags, buffMarksmanDamage Asset offset type, buffMarksmanDamage Cancel tags, buffMarksmanDamage Details, buffMarksmanDamage Is refreshing, buffMarksmanDamage Prevent tags, buffMarksmanDamage Shader override, buffMarksmanDamage Tags, buffMarksmanHealth Asset offset type, buffMarksmanHealth Cancel tags, buffMarksmanHealth Details, buffMarksmanHealth Is refreshing, buffMarksmanHealth Prevent tags, buffMarksmanHealth Shader override, buffMarksmanHealth Tags, buffPersonalShieldIthorian Asset offset type, buffPersonalShieldIthorian Cancel tags, buffPersonalShieldIthorian Details, buffPersonalShieldIthorian Is refreshing, buffPersonalShieldIthorian Prevent tags, buffPersonalShieldIthorian Shader override, buffPersonalShieldIthorian Tags, buffPersonalShieldKubaz Asset offset type, buffPersonalShieldKubaz Cancel tags, buffPersonalShieldKubaz Details, buffPersonalShieldKubaz Is refreshing, buffPersonalShieldKubaz Prevent tags, buffPersonalShieldKubaz Shader override, buffPersonalShieldKubaz Tags, buffReduceHeals Asset offset type, buffReduceHeals Cancel tags, buffReduceHeals Details, buffReduceHeals Is refreshing, buffReduceHeals Prevent tags, buffReduceHeals Shader override, buffReduceHeals Tags, buffSniperDamage Asset offset type, buffSniperDamage Cancel tags, buffSniperDamage Details, buffSniperDamage Is refreshing, buffSniperDamage Prevent tags, buffSniperDamage Shader override, buffSniperDamage Tags, buffSniperHealth Asset offset type, buffSniperHealth Cancel tags, buffSniperHealth Details, buffSniperHealth Is refreshing, buffSniperHealth Prevent tags, buffSniperHealth Shader override, buffSniperHealth Tags, buffSumPhtmTieBomber Asset offset type, buffSumPhtmTieBomber Cancel tags, buffSumPhtmTieBomber Details, buffSumPhtmTieBomber Is refreshing, buffSumPhtmTieBomber Prevent tags, buffSumPhtmTieBomber Shader override, buffSumPhtmTieBomber Tags, buffSumPhtmTieFighter Asset offset type, buffSumPhtmTieFighter Cancel tags, buffSumPhtmTieFighter Details, buffSumPhtmTieFighter Is refreshing, buffSumPhtmTieFighter Prevent tags, buffSumPhtmTieFighter Shader override, buffSumPhtmTieFighter Tags, buffSumPhtmXWing Asset offset type, buffSumPhtmXWing Cancel tags, buffSumPhtmXWing Details, buffSumPhtmXWing Is refreshing, buffSumPhtmXWing Prevent tags, buffSumPhtmXWing Shader override, buffSumPhtmXWing Tags, buffSumPhtmYWing Asset offset type, buffSumPhtmYWing Cancel tags, buffSumPhtmYWing Details, buffSumPhtmYWing Is refreshing, buffSumPhtmYWing Prevent tags, buffSumPhtmYWing Shader override, buffSumPhtmYWing Tags_

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |220601|220602|220603|220604|220605|220606|220607|220608|220609|220610|
|Point value|5     |6     |7     |8     |9     |10    |11    |12    |13    |15    |


