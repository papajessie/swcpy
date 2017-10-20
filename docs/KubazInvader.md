---
title: Kubaz Invader (KubazInvader)
category: unit
---

# Kubaz Invader (KubazInvader) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 3
  * Type: infantry
  * _Not found: Apply value as, Buff ID, Buff health, Can be given, Duration, Lvl, Modifier, Ms first proc, Ms per proc, Stack, Target, Uid, Unlock planet, Value_

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|1350|1600|1850|2100|2350|2600|2850|3100|3350|3600|


### Training stats

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|2m40s                            |2m48s                                  |3m2s                                   |3m19s                                  |3m38s                                  |3m59s                                  |4m22s                                  |4m47s                                  |5m13s                                  |5m40s                                   |
|Training cost|1000$                            |1052$                                  |1137$                                  |1242$                                  |1361$                                  |1494$                                  |1638$                                  |1791$                                  |1954$                                  |2125$                                   |
|Building     |[Barracks 4](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: 32 data fragments

### Move stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 45
  * Propensity to go around obstacles: 200
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * _Not found: Ignores walls, Support follow distance_

## Main attack : KubazInvader

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Shield (80)**, **Shield generator (80)**, _Ressource generator (60)_, _Storage (60)_, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Support troop (50), Turret (40), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Time between start of clip and first shot: 50ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 250ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 2
  * Time between shots: 200ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1   |2   |3   |4   |5   |6   |7    |8    |9    |10   |
|---------------|----|----|----|----|----|----|-----|-----|-----|-----|
|Damage per shot|2500|3775|5050|6325|7600|8875|10150|11425|12700|13975|


### Projectile

  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1       |2       |3       |4       |5       |6       |7       |8        |9        |10       |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|---------|---------|---------|
|Displayed damage per second |4700    |2545    |3090    |3454    |3818    |4363    |4909    |5272     |5636     |6545     |
|Calculated damage per second|2222.222|3355.556|4488.889|5622.222|6755.556|7888.889|9022.222|10155.556|11288.889|12422.222|


  * Cannons per sequence: 1
  * Cliptime: 2.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 15
  * Damage multipliers: **(600%)**: Shield generator, **(100%)**: Shield, **(60%)**: Ressource generator, **(50%)**: Storage, Wall, **(10%)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Support troop, Turret, Vehicule hero, **(0%)**: Trap
  * Pass through shield: Yes
  * Salvos: 2
  * _Not found: Length segments, Width segments_

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffPersonalShieldKubaz
  * Unit ID: KubazInvader
  * Upgrade shard uid: shrd_troopKubazInvader
  * _Not found: Ability, Apply buffs, Death attack apply buffs, Death projectile, Hero data, Secondary attack apply buffs, Secondary attack projectile type, Secondary attack self buff_

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: kubaz_emp-ani
  * Audio attack: "sfx_attack_ionblaster_1":25,"sfx_attack_ionblaster_2":25,"sfx_attack_ionblaster_3":25,"sfx_attack_ionblaster_4":25
  * Audio death: "sfx_death_kubaz_1":50,"sfx_death_kubaz_2":50
  * Audio placement: "sfx_placement_troop_1":33,"sfx_placement_troop_2":33,"sfx_placement_troop_3":33
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: kubaz_emp-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: shieldGenerator
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 8.96,11.37,18.33
  * Icon closeup camera position: 4.16,3.05,10.68
  * Icon closeup lookat position: 0.04,2.7,-0.25
  * Icon lookat position: -0.48,1.32,-0.72
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: KubazInvader
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true
  * buffPersonalShieldKubaz Asset name: kubazshield_emp-mod
  * buffPersonalShieldKubaz Bundle name: kubazshield_emp-mod
  * _Not found: Asset name, Asset profile, Audio ability event, Audio impact, Audio train, Buff asset offset, Bundle name, Charge asset name, Death animation, Death attack S transition, Death attack arcs, Death attack bullet, Death attack charge asset name, Death attack ground bullet, Death attack hit spark, Death attack max scale, Death attack muzzle flash, Death attack muzzle flash fade time, Death attack name, Death attack projectile length, Death attack spin speed, Decal asset name, Decal bundle name, Decal size, Effect type, Ground bullet, Gun position, Hologram uid, Icon unlock position, Icon unlock rotation, Icon unlock scale, Impact asset name empire, Impact asset name rebel, Info UI type, Muzzle asset name empire, Muzzle asset name rebel, Muzzle flash fade time, Projectile attachment bundle, Projectile length, S transition, Secondary attack S transition, Secondary attack alt gun locators, Secondary attack animation delay, Secondary attack arcs, Secondary attack audio ability activate, Secondary attack audio ability attack, Secondary attack audio ability loop, Secondary attack bullet, Secondary attack charge asset name, Secondary attack displayed damage per second, Secondary attack favorite target type, Secondary attack ground bullet, Secondary attack hit spark, Secondary attack max scale, Secondary attack muzzle flash, Secondary attack muzzle flash fade time, Secondary attack name, Secondary attack name, Secondary attack persistent effect, Secondary attack persistent scaling, Secondary attack projectile length, Secondary attack spin speed, Secondary attack weapon trail FX params, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by tournament, buffDefendSplash Asset name, buffDefendSplash Asset profile, buffDefendSplash Audio ability event, buffDefendSplash Bundle name, buffDefendSplash Impact asset name empire, buffDefendSplash Impact asset name rebel, buffDefendSplash Muzzle asset name empire, buffDefendSplash Muzzle asset name rebel, buffDefendSplash Projectile attachment bundle, buffInvulnerable Asset name, buffInvulnerable Asset profile, buffInvulnerable Audio ability event, buffInvulnerable Bundle name, buffInvulnerable Impact asset name empire, buffInvulnerable Impact asset name rebel, buffInvulnerable Muzzle asset name empire, buffInvulnerable Muzzle asset name rebel, buffInvulnerable Projectile attachment bundle, buffMarksmanDamage Asset name, buffMarksmanDamage Asset profile, buffMarksmanDamage Audio ability event, buffMarksmanDamage Bundle name, buffMarksmanDamage Impact asset name empire, buffMarksmanDamage Impact asset name rebel, buffMarksmanDamage Muzzle asset name empire, buffMarksmanDamage Muzzle asset name rebel, buffMarksmanDamage Projectile attachment bundle, buffMarksmanHealth Asset name, buffMarksmanHealth Asset profile, buffMarksmanHealth Audio ability event, buffMarksmanHealth Bundle name, buffMarksmanHealth Impact asset name empire, buffMarksmanHealth Impact asset name rebel, buffMarksmanHealth Muzzle asset name empire, buffMarksmanHealth Muzzle asset name rebel, buffMarksmanHealth Projectile attachment bundle, buffPersonalShieldIthorian Asset name, buffPersonalShieldIthorian Asset profile, buffPersonalShieldIthorian Audio ability event, buffPersonalShieldIthorian Bundle name, buffPersonalShieldIthorian Impact asset name empire, buffPersonalShieldIthorian Impact asset name rebel, buffPersonalShieldIthorian Muzzle asset name empire, buffPersonalShieldIthorian Muzzle asset name rebel, buffPersonalShieldIthorian Projectile attachment bundle, buffPersonalShieldKubaz Asset profile, buffPersonalShieldKubaz Audio ability event, buffPersonalShieldKubaz Impact asset name empire, buffPersonalShieldKubaz Impact asset name rebel, buffPersonalShieldKubaz Muzzle asset name empire, buffPersonalShieldKubaz Muzzle asset name rebel, buffPersonalShieldKubaz Projectile attachment bundle, buffReduceHeals Asset name, buffReduceHeals Asset profile, buffReduceHeals Audio ability event, buffReduceHeals Bundle name, buffReduceHeals Impact asset name empire, buffReduceHeals Impact asset name rebel, buffReduceHeals Muzzle asset name empire, buffReduceHeals Muzzle asset name rebel, buffReduceHeals Projectile attachment bundle, buffSniperDamage Asset name, buffSniperDamage Asset profile, buffSniperDamage Audio ability event, buffSniperDamage Bundle name, buffSniperDamage Impact asset name empire, buffSniperDamage Impact asset name rebel, buffSniperDamage Muzzle asset name empire, buffSniperDamage Muzzle asset name rebel, buffSniperDamage Projectile attachment bundle, buffSniperHealth Asset name, buffSniperHealth Asset profile, buffSniperHealth Audio ability event, buffSniperHealth Bundle name, buffSniperHealth Impact asset name empire, buffSniperHealth Impact asset name rebel, buffSniperHealth Muzzle asset name empire, buffSniperHealth Muzzle asset name rebel, buffSniperHealth Projectile attachment bundle, buffSumPhtmTieBomber Asset name, buffSumPhtmTieBomber Asset profile, buffSumPhtmTieBomber Audio ability event, buffSumPhtmTieBomber Bundle name, buffSumPhtmTieBomber Impact asset name empire, buffSumPhtmTieBomber Impact asset name rebel, buffSumPhtmTieBomber Muzzle asset name empire, buffSumPhtmTieBomber Muzzle asset name rebel, buffSumPhtmTieBomber Projectile attachment bundle, buffSumPhtmTieFighter Asset name, buffSumPhtmTieFighter Asset profile, buffSumPhtmTieFighter Audio ability event, buffSumPhtmTieFighter Bundle name, buffSumPhtmTieFighter Impact asset name empire, buffSumPhtmTieFighter Impact asset name rebel, buffSumPhtmTieFighter Muzzle asset name empire, buffSumPhtmTieFighter Muzzle asset name rebel, buffSumPhtmTieFighter Projectile attachment bundle, buffSumPhtmXWing Asset name, buffSumPhtmXWing Asset profile, buffSumPhtmXWing Audio ability event, buffSumPhtmXWing Bundle name, buffSumPhtmXWing Impact asset name empire, buffSumPhtmXWing Impact asset name rebel, buffSumPhtmXWing Muzzle asset name empire, buffSumPhtmXWing Muzzle asset name rebel, buffSumPhtmXWing Projectile attachment bundle, buffSumPhtmYWing Asset name, buffSumPhtmYWing Asset profile, buffSumPhtmYWing Audio ability event, buffSumPhtmYWing Bundle name, buffSumPhtmYWing Impact asset name empire, buffSumPhtmYWing Impact asset name rebel, buffSumPhtmYWing Muzzle asset name empire, buffSumPhtmYWing Muzzle asset name rebel, buffSumPhtmYWing Projectile attachment bundle_

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|4700|2545|3090|3454|3818|4363|4909|5272|5636|6545|


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
  * buffPersonalShieldKubaz Cancel tags: damage
  * buffPersonalShieldKubaz Is refreshing: false
  * buffPersonalShieldKubaz Prevent tags: damage
  * buffPersonalShieldKubaz Tags: shield
  * _Not found: Asset offset type, Cancel tags, Death attack S1 time, Death attack S2 time, Death attack seeks target, Death attack streams, Details, Is refreshing, Prevent tags, S1 time, S2 time, Secondary attack S1 time, Secondary attack S2 time, Secondary attack arming delay, Secondary attack clip count, Secondary attack kill cooldown reset, Secondary attack max speed, Secondary attack seeks target, Secondary attack streams, Secondary attack strict cool down, Shader override, Tags, buffDefendSplash Asset offset type, buffDefendSplash Cancel tags, buffDefendSplash Details, buffDefendSplash Is refreshing, buffDefendSplash Prevent tags, buffDefendSplash Shader override, buffDefendSplash Tags, buffInvulnerable Asset offset type, buffInvulnerable Cancel tags, buffInvulnerable Details, buffInvulnerable Is refreshing, buffInvulnerable Prevent tags, buffInvulnerable Shader override, buffInvulnerable Tags, buffMarksmanDamage Asset offset type, buffMarksmanDamage Cancel tags, buffMarksmanDamage Details, buffMarksmanDamage Is refreshing, buffMarksmanDamage Prevent tags, buffMarksmanDamage Shader override, buffMarksmanDamage Tags, buffMarksmanHealth Asset offset type, buffMarksmanHealth Cancel tags, buffMarksmanHealth Details, buffMarksmanHealth Is refreshing, buffMarksmanHealth Prevent tags, buffMarksmanHealth Shader override, buffMarksmanHealth Tags, buffPersonalShieldIthorian Asset offset type, buffPersonalShieldIthorian Cancel tags, buffPersonalShieldIthorian Details, buffPersonalShieldIthorian Is refreshing, buffPersonalShieldIthorian Prevent tags, buffPersonalShieldIthorian Shader override, buffPersonalShieldIthorian Tags, buffPersonalShieldKubaz Asset offset type, buffPersonalShieldKubaz Details, buffPersonalShieldKubaz Shader override, buffReduceHeals Asset offset type, buffReduceHeals Cancel tags, buffReduceHeals Details, buffReduceHeals Is refreshing, buffReduceHeals Prevent tags, buffReduceHeals Shader override, buffReduceHeals Tags, buffSniperDamage Asset offset type, buffSniperDamage Cancel tags, buffSniperDamage Details, buffSniperDamage Is refreshing, buffSniperDamage Prevent tags, buffSniperDamage Shader override, buffSniperDamage Tags, buffSniperHealth Asset offset type, buffSniperHealth Cancel tags, buffSniperHealth Details, buffSniperHealth Is refreshing, buffSniperHealth Prevent tags, buffSniperHealth Shader override, buffSniperHealth Tags, buffSumPhtmTieBomber Asset offset type, buffSumPhtmTieBomber Cancel tags, buffSumPhtmTieBomber Details, buffSumPhtmTieBomber Is refreshing, buffSumPhtmTieBomber Prevent tags, buffSumPhtmTieBomber Shader override, buffSumPhtmTieBomber Tags, buffSumPhtmTieFighter Asset offset type, buffSumPhtmTieFighter Cancel tags, buffSumPhtmTieFighter Details, buffSumPhtmTieFighter Is refreshing, buffSumPhtmTieFighter Prevent tags, buffSumPhtmTieFighter Shader override, buffSumPhtmTieFighter Tags, buffSumPhtmXWing Asset offset type, buffSumPhtmXWing Cancel tags, buffSumPhtmXWing Details, buffSumPhtmXWing Is refreshing, buffSumPhtmXWing Prevent tags, buffSumPhtmXWing Shader override, buffSumPhtmXWing Tags, buffSumPhtmYWing Asset offset type, buffSumPhtmYWing Cancel tags, buffSumPhtmYWing Details, buffSumPhtmYWing Is refreshing, buffSumPhtmYWing Prevent tags, buffSumPhtmYWing Shader override, buffSumPhtmYWing Tags_

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |134001|134002|134003|134004|134005|134006|134007|134008|134009|134010|
|Point value|3     |3.600 |4.200 |4.800 |5.400 |6     |6.600 |7.200 |7.800 |9     |


I could not show the following roles, because I was not programmed to : buffPersonalShieldKubazbasic
