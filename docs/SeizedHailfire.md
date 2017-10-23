---
title: Seized Hailfire Droid (SeizedHailfire)
category: unit
---

# Seized Hailfire Droid (SeizedHailfire) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: No
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 7
  * Type: vehicle
  * _Not found: Can be given, Name, Unlock planet_

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2800|3360|3920|4480|5040|5600|6160|6720|7280|8400|


### Training stats

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|2m48s                          |2m56s                                  |3m4s                                   |3m12s                                  |3m20s                                  |3m28s                                  |3m36s                                  |3m16s                                  |3m23s                                  |3m30s                                   |
|Training cost|350$                           |490$                                   |630$                                   |770$                                   |910$                                   |1050$                                  |1190$                                  |1400$                                  |1470$                                  |1610$                                   |
|Building     |[Factory 7](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

|Level               |1   |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s  |45m  |2h   |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Upgrade requirements|700$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2
  * _Not found: Ignores walls, Support follow distance_

## Main attack : projectileHailfire

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, _Droideka (60)_, _Flying infantry (60)_, _Flying vehicle (60)_, _Heavy infantry (60)_, _Heavy infantry hero (60)_, _Heavy vehicle (60)_, _Heavy vehicule hero (60)_, _Infantry (60)_, _Infantry hero (60)_, _Light vehicle (60)_, _Support troop (60)_, _Vehicule hero (60)_, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 1s
  * Clip retargeting: Yes
  * Gun shooting sequence: 1,2
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 6
  * Time between shots: 100ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1  |2  |3  |4  |5  |6  |7  |8  |9  |10  |
|---------------|---|---|---|---|---|---|---|---|---|----|
|Damage per shot|368|441|515|588|662|735|809|882|956|1103|


### Projectile

  * Splash damage percentages: 100,75,50
  * _Not found: Beam damage_

|Level                       |1      |2  |3      |4   |5       |6   |7       |8   |9       |10      |
|----------------------------|-------|---|-------|----|--------|----|--------|----|--------|--------|
|Displayed damage per second |630    |756|882    |1008|1134    |1260|1386    |1512|1638    |1890    |
|Calculated damage per second|630.857|756|882.857|1008|1134.857|1260|1386.857|1512|1638.857|1890.857|


  * Cannons per sequence: 2
  * Cliptime: 3.500s
  * Directional: No
  * Is deflectable: No
  * Max speed: 12
  * Damage multipliers: **(300%)**: Flying vehicle, Light vehicle, Vehicule hero, **(250%)**: Heavy vehicle, Heavy vehicule hero, **(200%)**: Trap, Turret, **(100%)**: Droideka, **(80%)**: Wall, **(50%)**: Flying infantry, Heavy infantry, Heavy infantry hero, Infantry, Infantry hero, Support troop, **(25%)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage
  * Pass through shield: No
  * Salvos: 6
  * _Not found: Length segments, Width segments_

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SeizedHailfire
  * _Not found: Ability, Apply buffs, Death attack apply buffs, Death projectile, Hero data, Secondary attack apply buffs, Secondary attack projectile type, Secondary attack self buff, Spawn apply buffs, Upgrade shard uid_

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: hailfiredroid_rbl-ani
  * Audio attack: "sfx_attack_rebel_hailfire_1":35,"sfx_attack_rebel_hailfire_2":35,"sfx_attack_rebel_hailfire_3":30
  * Audio death: "sfx_death_rebel_hailfire_1":100
  * Audio impact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * Audio placement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * Buff asset offset: 0.00,0.88,0.00
  * Bullet: fx_rocket_projectile_b_sm
  * Bundle name: hailfiredroid_rbl-ani
  * Factory rotation: 90
  * Factory scale factor: 0.71499999999999996891375531049561686813831329345703125
  * Favorite target type: turret
  * Gun position: "hailfiredroid_rbl_rig_locator_gun1":1,"hailfiredroid_rbl_rig_locator_gun2":2
  * Hit spark: fx_rocket_hit_b_sm
  * Icon camera position: 36.69,22.39,29.86
  * Icon lookat position: -0.49,1.9,-0.43
  * Max scale: 100
  * Muzzle flash: fx_rocket_muzzle_b_sm
  * Name: projectileHailfire
  * Spin speed: 0
  * Targeted type: ENEMIES
  * _Not found: Asset name, Asset profile, Audio ability event, Audio train, Bundle name, Charge asset name, Death animation, Death attack S transition, Death attack arcs, Death attack bullet, Death attack charge asset name, Death attack ground bullet, Death attack hit spark, Death attack max scale, Death attack muzzle flash, Death attack muzzle flash fade time, Death attack name, Death attack projectile length, Death attack spin speed, Decal asset name, Decal bundle name, Decal size, Defend splash asset name, Defend splash asset profile, Defend splash audio ability event, Defend splash bundle name, Defend splash impact asset name empire, Defend splash impact asset name rebel, Defend splash muzzle asset name empire, Defend splash muzzle asset name rebel, Defend splash projectile attachment bundle, Effect type, Event button action, Event button data, Event button string, Event features string, Ground bullet, Hologram uid, Icon closeup camera position, Icon closeup lookat position, Icon unlock position, Icon unlock rotation, Icon unlock scale, Impact asset name empire, Impact asset name rebel, Info UI type, Invulnerable asset name, Invulnerable asset profile, Invulnerable audio ability event, Invulnerable bundle name, Invulnerable impact asset name empire, Invulnerable impact asset name rebel, Invulnerable muzzle asset name empire, Invulnerable muzzle asset name rebel, Invulnerable projectile attachment bundle, Marksman damage asset name, Marksman damage asset profile, Marksman damage audio ability event, Marksman damage bundle name, Marksman damage impact asset name empire, Marksman damage impact asset name rebel, Marksman damage muzzle asset name empire, Marksman damage muzzle asset name rebel, Marksman damage projectile attachment bundle, Marksman health asset name, Marksman health asset profile, Marksman health audio ability event, Marksman health bundle name, Marksman health impact asset name empire, Marksman health impact asset name rebel, Marksman health muzzle asset name empire, Marksman health muzzle asset name rebel, Marksman health projectile attachment bundle, Muzzle asset name empire, Muzzle asset name rebel, Muzzle flash fade time, Personal shield ithorian asset name, Personal shield ithorian asset profile, Personal shield ithorian audio ability event, Personal shield ithorian bundle name, Personal shield ithorian impact asset name empire, Personal shield ithorian impact asset name rebel, Personal shield ithorian muzzle asset name empire, Personal shield ithorian muzzle asset name rebel, Personal shield ithorian projectile attachment bundle, Personal shield kubaz asset name, Personal shield kubaz asset profile, Personal shield kubaz audio ability event, Personal shield kubaz bundle name, Personal shield kubaz impact asset name empire, Personal shield kubaz impact asset name rebel, Personal shield kubaz muzzle asset name empire, Personal shield kubaz muzzle asset name rebel, Personal shield kubaz projectile attachment bundle, Projectile attachment bundle, Projectile length, Reduce heals asset name, Reduce heals asset profile, Reduce heals audio ability event, Reduce heals bundle name, Reduce heals impact asset name empire, Reduce heals impact asset name rebel, Reduce heals muzzle asset name empire, Reduce heals muzzle asset name rebel, Reduce heals projectile attachment bundle, S transition, Secondary attack S transition, Secondary attack alt gun locators, Secondary attack animation delay, Secondary attack arcs, Secondary attack audio ability activate, Secondary attack audio ability attack, Secondary attack audio ability loop, Secondary attack bullet, Secondary attack charge asset name, Secondary attack displayed damage per second, Secondary attack favorite target type, Secondary attack ground bullet, Secondary attack hit spark, Secondary attack max scale, Secondary attack muzzle flash, Secondary attack muzzle flash fade time, Secondary attack name, Secondary attack name, Secondary attack persistent effect, Secondary attack persistent scaling, Secondary attack projectile length, Secondary attack spin speed, Secondary attack weapon trail FX params, Shield asset name, Sniper damage asset name, Sniper damage asset profile, Sniper damage audio ability event, Sniper damage bundle name, Sniper damage impact asset name empire, Sniper damage impact asset name rebel, Sniper damage muzzle asset name empire, Sniper damage muzzle asset name rebel, Sniper damage projectile attachment bundle, Sniper health asset name, Sniper health asset profile, Sniper health audio ability event, Sniper health bundle name, Sniper health impact asset name empire, Sniper health impact asset name rebel, Sniper health muzzle asset name empire, Sniper health muzzle asset name rebel, Sniper health projectile attachment bundle, Spawn effect uid, Sum phtm X wing asset name, Sum phtm X wing asset profile, Sum phtm X wing audio ability event, Sum phtm X wing bundle name, Sum phtm X wing impact asset name empire, Sum phtm X wing impact asset name rebel, Sum phtm X wing muzzle asset name empire, Sum phtm X wing muzzle asset name rebel, Sum phtm X wing projectile attachment bundle, Sum phtm Y wing asset name, Sum phtm Y wing asset profile, Sum phtm Y wing audio ability event, Sum phtm Y wing bundle name, Sum phtm Y wing impact asset name empire, Sum phtm Y wing impact asset name rebel, Sum phtm Y wing muzzle asset name empire, Sum phtm Y wing muzzle asset name rebel, Sum phtm Y wing projectile attachment bundle, Sum phtm tie bomber asset name, Sum phtm tie bomber asset profile, Sum phtm tie bomber audio ability event, Sum phtm tie bomber bundle name, Sum phtm tie bomber impact asset name empire, Sum phtm tie bomber impact asset name rebel, Sum phtm tie bomber muzzle asset name empire, Sum phtm tie bomber muzzle asset name rebel, Sum phtm tie bomber projectile attachment bundle, Sum phtm tie fighter asset name, Sum phtm tie fighter asset profile, Sum phtm tie fighter audio ability event, Sum phtm tie fighter bundle name, Sum phtm tie fighter impact asset name empire, Sum phtm tie fighter impact asset name rebel, Sum phtm tie fighter muzzle asset name empire, Sum phtm tie fighter muzzle asset name rebel, Sum phtm tie fighter projectile attachment bundle, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament_

|Level                      |1  |2  |3  |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|---|---|---|----|----|----|----|----|----|----|
|Displayed damage per second|630|756|882|1008|1134|1260|1386|1512|1638|1890|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: No
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0
  * _Not found: Asset offset type, Cancel tags, Death attack S1 time, Death attack S2 time, Death attack seeks target, Death attack streams, Defend splash asset offset type, Defend splash cancel tags, Defend splash details, Defend splash is refreshing, Defend splash prevent tags, Defend splash shader override, Defend splash tags, Details, Invulnerable asset offset type, Invulnerable cancel tags, Invulnerable details, Invulnerable is refreshing, Invulnerable prevent tags, Invulnerable shader override, Invulnerable tags, Is refreshing, Marksman damage asset offset type, Marksman damage cancel tags, Marksman damage details, Marksman damage is refreshing, Marksman damage prevent tags, Marksman damage shader override, Marksman damage tags, Marksman health asset offset type, Marksman health cancel tags, Marksman health details, Marksman health is refreshing, Marksman health prevent tags, Marksman health shader override, Marksman health tags, Personal shield ithorian asset offset type, Personal shield ithorian cancel tags, Personal shield ithorian details, Personal shield ithorian is refreshing, Personal shield ithorian prevent tags, Personal shield ithorian shader override, Personal shield ithorian tags, Personal shield kubaz asset offset type, Personal shield kubaz cancel tags, Personal shield kubaz details, Personal shield kubaz is refreshing, Personal shield kubaz prevent tags, Personal shield kubaz shader override, Personal shield kubaz tags, Point value, Prevent tags, Reduce heals asset offset type, Reduce heals cancel tags, Reduce heals details, Reduce heals is refreshing, Reduce heals prevent tags, Reduce heals shader override, Reduce heals tags, S1 time, S2 time, Secondary attack S1 time, Secondary attack S2 time, Secondary attack arming delay, Secondary attack clip count, Secondary attack kill cooldown reset, Secondary attack max speed, Secondary attack seeks target, Secondary attack streams, Secondary attack strict cool down, Shader override, Sniper damage asset offset type, Sniper damage cancel tags, Sniper damage details, Sniper damage is refreshing, Sniper damage prevent tags, Sniper damage shader override, Sniper damage tags, Sniper health asset offset type, Sniper health cancel tags, Sniper health details, Sniper health is refreshing, Sniper health prevent tags, Sniper health shader override, Sniper health tags, Sum phtm X wing asset offset type, Sum phtm X wing cancel tags, Sum phtm X wing details, Sum phtm X wing is refreshing, Sum phtm X wing prevent tags, Sum phtm X wing shader override, Sum phtm X wing tags, Sum phtm Y wing asset offset type, Sum phtm Y wing cancel tags, Sum phtm Y wing details, Sum phtm Y wing is refreshing, Sum phtm Y wing prevent tags, Sum phtm Y wing shader override, Sum phtm Y wing tags, Sum phtm tie bomber asset offset type, Sum phtm tie bomber cancel tags, Sum phtm tie bomber details, Sum phtm tie bomber is refreshing, Sum phtm tie bomber prevent tags, Sum phtm tie bomber shader override, Sum phtm tie bomber tags, Sum phtm tie fighter asset offset type, Sum phtm tie fighter cancel tags, Sum phtm tie fighter details, Sum phtm tie fighter is refreshing, Sum phtm tie fighter prevent tags, Sum phtm tie fighter shader override, Sum phtm tie fighter tags, Tags_

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|482804|482808|482812|482816|482820|482824|482828|482832|482836|482840|


