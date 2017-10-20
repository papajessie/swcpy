---
title: AT-AT (ATAT)
category: unit
---

# AT-AT (ATAT) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 30
  * Type: vehicle
  * _Not found: Apply value as, Buff ID, Buff health, Can be given, Duration, Lvl, Modifier, Ms first proc, Ms per proc, Stack, Target, Uid, Unlock planet, Value_

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|22000|26400|30800|35200|39600|44000|48400|52800|57200|66000|


### Training stats

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|3m30s                          |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |6m40s                                  |7m10s                                  |7m40s                                   |
|Training cost|1500$                          |2100$                                  |2700$                                  |3300$                                  |3900$                                  |4500$                                  |5100$                                  |6000$                                  |6300$                                  |6900$                                   |
|Building     |[Factory 5](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |1h30m|3h   |8h    |1d    |3d    |5d     |1w     |1w3d   |2w      |2w      |
|Upgrade requirements|4300$|5000$|10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|


### Move stats

  * Acceleration: 0
  * Crushes walls: Yes
  * Flying unit: No
  * Max speed: 10
  * Propensity to go around obstacles: 200
  * Rotation speed: 0.982
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2
  * _Not found: Ignores walls, Support follow distance_

## Main attack : ATAT

### Targeting

  * Attack shield border: Yes
  * Max attack range: 9
  * Min attack range: 1
  * New rotation speed: 982
  * Target preference strength: 90
  * Target preferences: **Shield (80)**, **Shield generator (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,1,1,1
  * Impact delay: 500ms
  * Can shoot over walls: Yes
  * Time between end of clip and start of clip: 1.500s
  * Retargeting offset: 18
  * Self-centered targeting: No
  * Shot count: 8
  * Time between shots: 250ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|---|---|----|----|----|----|----|----|----|----|
|Damage per shot|750|900|1050|1200|1350|1500|1650|1800|1950|2250|


### Projectile

  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1       |2   |3       |4       |5   |6       |7       |8   |9       |10  |
|----------------------------|--------|----|--------|--------|----|--------|--------|----|--------|----|
|Displayed damage per second |1600    |1920|2240    |2560    |2880|3200    |3520    |3840|4160    |4800|
|Calculated damage per second|2666.667|3200|3733.333|4266.667|4800|5333.333|5866.667|6400|6933.333|8000|


  * Cannons per sequence: 4
  * Cliptime: 2.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400%)**: Shield, Shield generator, **(100%)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75%)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 2
  * _Not found: Length segments, Width segments_

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ATAT
  * _Not found: Ability, Apply buffs, Death attack apply buffs, Death projectile, Hero data, Secondary attack apply buffs, Secondary attack projectile type, Secondary attack self buff, Spawn apply buffs, Upgrade shard uid_

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: atat_emp-ani
  * Audio attack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * Audio death: "sfx_death_walker_1":100
  * Audio placement: "sfx_placement_empire_atat_1":100
  * Buff asset offset: 0,4.00,0.00
  * Bullet: fx_blaster_beam_r_med
  * Bundle name: atat_emp-ani
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: shieldGenerator
  * Gun position: "atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun1":1,"atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun2":1,"atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun3":1,"atat_emp_rig_falseMaster/atat_emp_rig_MASTER_MOVER/atat_emp_rig_locator_gun4":1
  * Hit spark: fx_blaster_hit_r_med
  * Icon camera position: 41.83,40.55,52.41
  * Icon lookat position: -2.01,3.9,-0.8
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_med
  * Name: ATAT
  * Spin speed: 0
  * Targeted type: ENEMIES
  * _Not found: Asset name, Asset profile, Audio ability event, Audio impact, Audio train, Bundle name, Charge asset name, Death animation, Death attack S transition, Death attack arcs, Death attack bullet, Death attack charge asset name, Death attack ground bullet, Death attack hit spark, Death attack max scale, Death attack muzzle flash, Death attack muzzle flash fade time, Death attack name, Death attack projectile length, Death attack spin speed, Decal asset name, Decal bundle name, Decal size, Effect type, Event button action, Event button data, Event button string, Event features string, Ground bullet, Hologram uid, Icon closeup camera position, Icon closeup lookat position, Icon unlock position, Icon unlock rotation, Icon unlock scale, Impact asset name empire, Impact asset name rebel, Info UI type, Muzzle asset name empire, Muzzle asset name rebel, Muzzle flash fade time, Projectile attachment bundle, Projectile length, S transition, Secondary attack S transition, Secondary attack alt gun locators, Secondary attack animation delay, Secondary attack arcs, Secondary attack audio ability activate, Secondary attack audio ability attack, Secondary attack audio ability loop, Secondary attack bullet, Secondary attack charge asset name, Secondary attack displayed damage per second, Secondary attack favorite target type, Secondary attack ground bullet, Secondary attack hit spark, Secondary attack max scale, Secondary attack muzzle flash, Secondary attack muzzle flash fade time, Secondary attack name, Secondary attack name, Secondary attack persistent effect, Secondary attack persistent scaling, Secondary attack projectile length, Secondary attack spin speed, Secondary attack weapon trail FX params, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament, buffDefendSplash Asset name, buffDefendSplash Asset profile, buffDefendSplash Audio ability event, buffDefendSplash Bundle name, buffDefendSplash Impact asset name empire, buffDefendSplash Impact asset name rebel, buffDefendSplash Muzzle asset name empire, buffDefendSplash Muzzle asset name rebel, buffDefendSplash Projectile attachment bundle, buffInvulnerable Asset name, buffInvulnerable Asset profile, buffInvulnerable Audio ability event, buffInvulnerable Bundle name, buffInvulnerable Impact asset name empire, buffInvulnerable Impact asset name rebel, buffInvulnerable Muzzle asset name empire, buffInvulnerable Muzzle asset name rebel, buffInvulnerable Projectile attachment bundle, buffMarksmanDamage Asset name, buffMarksmanDamage Asset profile, buffMarksmanDamage Audio ability event, buffMarksmanDamage Bundle name, buffMarksmanDamage Impact asset name empire, buffMarksmanDamage Impact asset name rebel, buffMarksmanDamage Muzzle asset name empire, buffMarksmanDamage Muzzle asset name rebel, buffMarksmanDamage Projectile attachment bundle, buffMarksmanHealth Asset name, buffMarksmanHealth Asset profile, buffMarksmanHealth Audio ability event, buffMarksmanHealth Bundle name, buffMarksmanHealth Impact asset name empire, buffMarksmanHealth Impact asset name rebel, buffMarksmanHealth Muzzle asset name empire, buffMarksmanHealth Muzzle asset name rebel, buffMarksmanHealth Projectile attachment bundle, buffPersonalShieldIthorian Asset name, buffPersonalShieldIthorian Asset profile, buffPersonalShieldIthorian Audio ability event, buffPersonalShieldIthorian Bundle name, buffPersonalShieldIthorian Impact asset name empire, buffPersonalShieldIthorian Impact asset name rebel, buffPersonalShieldIthorian Muzzle asset name empire, buffPersonalShieldIthorian Muzzle asset name rebel, buffPersonalShieldIthorian Projectile attachment bundle, buffPersonalShieldKubaz Asset name, buffPersonalShieldKubaz Asset profile, buffPersonalShieldKubaz Audio ability event, buffPersonalShieldKubaz Bundle name, buffPersonalShieldKubaz Impact asset name empire, buffPersonalShieldKubaz Impact asset name rebel, buffPersonalShieldKubaz Muzzle asset name empire, buffPersonalShieldKubaz Muzzle asset name rebel, buffPersonalShieldKubaz Projectile attachment bundle, buffReduceHeals Asset name, buffReduceHeals Asset profile, buffReduceHeals Audio ability event, buffReduceHeals Bundle name, buffReduceHeals Impact asset name empire, buffReduceHeals Impact asset name rebel, buffReduceHeals Muzzle asset name empire, buffReduceHeals Muzzle asset name rebel, buffReduceHeals Projectile attachment bundle, buffSniperDamage Asset name, buffSniperDamage Asset profile, buffSniperDamage Audio ability event, buffSniperDamage Bundle name, buffSniperDamage Impact asset name empire, buffSniperDamage Impact asset name rebel, buffSniperDamage Muzzle asset name empire, buffSniperDamage Muzzle asset name rebel, buffSniperDamage Projectile attachment bundle, buffSniperHealth Asset name, buffSniperHealth Asset profile, buffSniperHealth Audio ability event, buffSniperHealth Bundle name, buffSniperHealth Impact asset name empire, buffSniperHealth Impact asset name rebel, buffSniperHealth Muzzle asset name empire, buffSniperHealth Muzzle asset name rebel, buffSniperHealth Projectile attachment bundle, buffSumPhtmTieBomber Asset name, buffSumPhtmTieBomber Asset profile, buffSumPhtmTieBomber Audio ability event, buffSumPhtmTieBomber Bundle name, buffSumPhtmTieBomber Impact asset name empire, buffSumPhtmTieBomber Impact asset name rebel, buffSumPhtmTieBomber Muzzle asset name empire, buffSumPhtmTieBomber Muzzle asset name rebel, buffSumPhtmTieBomber Projectile attachment bundle, buffSumPhtmTieFighter Asset name, buffSumPhtmTieFighter Asset profile, buffSumPhtmTieFighter Audio ability event, buffSumPhtmTieFighter Bundle name, buffSumPhtmTieFighter Impact asset name empire, buffSumPhtmTieFighter Impact asset name rebel, buffSumPhtmTieFighter Muzzle asset name empire, buffSumPhtmTieFighter Muzzle asset name rebel, buffSumPhtmTieFighter Projectile attachment bundle, buffSumPhtmXWing Asset name, buffSumPhtmXWing Asset profile, buffSumPhtmXWing Audio ability event, buffSumPhtmXWing Bundle name, buffSumPhtmXWing Impact asset name empire, buffSumPhtmXWing Impact asset name rebel, buffSumPhtmXWing Muzzle asset name empire, buffSumPhtmXWing Muzzle asset name rebel, buffSumPhtmXWing Projectile attachment bundle, buffSumPhtmYWing Asset name, buffSumPhtmYWing Asset profile, buffSumPhtmYWing Audio ability event, buffSumPhtmYWing Bundle name, buffSumPhtmYWing Impact asset name empire, buffSumPhtmYWing Impact asset name rebel, buffSumPhtmYWing Muzzle asset name empire, buffSumPhtmYWing Muzzle asset name rebel, buffSumPhtmYWing Projectile attachment bundle_

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|1600|1920|2240|2560|2880|3200|3520|3840|4160|4800|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
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
|Order      |130501|130502|130503|130504|130505|130506|130507|130508|130509|130510|
|Point value|30    |36    |42    |48    |54    |60    |66    |72    |78    |90    |


