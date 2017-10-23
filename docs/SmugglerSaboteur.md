---
title: Jawa Saboteur (SmugglerSaboteur)
category: unit
---

# Jawa Saboteur (SmugglerSaboteur) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 4
  * Type: infantry
  * _Not found: Can be given, Name, Unlock planet_

|Level         |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|--------------|----|----|----|----|----|----|----|----|----|----|
|Health        |3200|3840|4480|5120|5760|6400|7040|7680|8320|9600|
|Buildable unit|Yes |Yes |Yes |Yes |Yes |Yes |Yes |Yes |No  |No  |


### Training stats

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |6                                  |7                                  |8                                  |9                                  |10                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|------------------------------------|
|Training time|1m40s                              |1m50s                              |1m55s                              |2m                                 |2m5s                               |2m10s                              |2m15s                              |2m20s                              |2m25s                              |2m30s                               |
|Training cost|250$                               |350$                               |450$                               |550$                               |650$                               |750$                               |850$                               |950$                               |1050$                              |1150$                               |
|Building     |[Barracks 1](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 10](smugglerBarracks.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Upgrade requirements|3000$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 40
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * _Not found: Ignores walls, Support follow distance_

## Main attack : SmugglerSaboteur

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Shield (70)**, **Shield generator (70)**, _Other building (60)_, _Ressource generator (60)_, _Storage (60)_, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Can shoot over walls: No
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Time between shots: 100ms
  * Target locking: No
  * _Not found: New target on reload_

|Level                                     |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot                           |112  |135  |157  |180  |202  |224  |247  |269  |292  |336  |
|Impact delay                              |1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |1s   |500ms|
|Time between end of clip and start of clip|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|2s   |
|Shot count                                |5    |5    |5    |5    |5    |5    |5    |5    |5    |10   |


### Projectile

  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1  |2      |3      |4      |5      |6  |7      |8      |9       |10     |
|----------------------------|---|-------|-------|-------|-------|---|-------|-------|--------|-------|
|Displayed damage per second |329|396    |461    |529    |593    |658|726    |790    |858     |987    |
|Calculated damage per second|400|482.143|560.714|642.857|721.429|800|882.143|960.714|1042.857|988.235|


  * Cannons per sequence: 1
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 30
  * Damage multipliers: **(250%)**: Shield generator, **(175%)**: Shield, **(150%)**: Wall, **(100%)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Storage, Support troop, Trap, Turret, Vehicule hero
  * Pass through shield: No
  * _Not found: Length segments, Width segments_

|Level   |1, 2, 3, 4, 5, 6, 7, 8, 9|10    |
|--------|-------------------------|------|
|Cliptime|1.400s                   |3.400s|
|Salvos  |5                        |10    |


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerSaboteur
  * _Not found: Ability, Apply buffs, Death attack apply buffs, Death projectile, Hero data, Secondary attack apply buffs, Secondary attack projectile type, Secondary attack self buff, Spawn apply buffs, Upgrade shard uid_

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: jawaarmed_neu-ani
  * Audio attack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_darktrooper_01":35,"sfx_ui_unitcomplete_darktrooper_02":35,"sfx_ui_unitcomplete_darktrooper_03":30
  * Bullet: fx_blaster_beam_y_sm
  * Bundle name: jawaarmed_neu-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "generalpurpose_smg_rig_MASTER_MOVER/generalpurpose_smg_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_y_sm
  * Icon camera position: 4.07,10.49,14.92
  * Icon lookat position: -0.12,1.34,0.53
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Name: SmugglerSaboteur
  * Spin speed: 0
  * Targeted type: ENEMIES
  * _Not found: Asset name, Asset profile, Audio ability event, Audio impact, Buff asset offset, Bundle name, Charge asset name, Death attack S transition, Death attack arcs, Death attack bullet, Death attack charge asset name, Death attack ground bullet, Death attack hit spark, Death attack max scale, Death attack muzzle flash, Death attack muzzle flash fade time, Death attack name, Death attack projectile length, Death attack spin speed, Decal asset name, Decal bundle name, Decal size, Defend splash asset name, Defend splash asset profile, Defend splash audio ability event, Defend splash bundle name, Defend splash impact asset name empire, Defend splash impact asset name rebel, Defend splash muzzle asset name empire, Defend splash muzzle asset name rebel, Defend splash projectile attachment bundle, Effect type, Event button action, Event button data, Event button string, Event features string, Ground bullet, Hologram uid, Icon closeup camera position, Icon closeup lookat position, Icon unlock position, Icon unlock rotation, Icon unlock scale, Impact asset name empire, Impact asset name rebel, Info UI type, Invulnerable asset name, Invulnerable asset profile, Invulnerable audio ability event, Invulnerable bundle name, Invulnerable impact asset name empire, Invulnerable impact asset name rebel, Invulnerable muzzle asset name empire, Invulnerable muzzle asset name rebel, Invulnerable projectile attachment bundle, Marksman damage asset name, Marksman damage asset profile, Marksman damage audio ability event, Marksman damage bundle name, Marksman damage impact asset name empire, Marksman damage impact asset name rebel, Marksman damage muzzle asset name empire, Marksman damage muzzle asset name rebel, Marksman damage projectile attachment bundle, Marksman health asset name, Marksman health asset profile, Marksman health audio ability event, Marksman health bundle name, Marksman health impact asset name empire, Marksman health impact asset name rebel, Marksman health muzzle asset name empire, Marksman health muzzle asset name rebel, Marksman health projectile attachment bundle, Muzzle asset name empire, Muzzle asset name rebel, Muzzle flash fade time, Personal shield ithorian asset name, Personal shield ithorian asset profile, Personal shield ithorian audio ability event, Personal shield ithorian bundle name, Personal shield ithorian impact asset name empire, Personal shield ithorian impact asset name rebel, Personal shield ithorian muzzle asset name empire, Personal shield ithorian muzzle asset name rebel, Personal shield ithorian projectile attachment bundle, Personal shield kubaz asset name, Personal shield kubaz asset profile, Personal shield kubaz audio ability event, Personal shield kubaz bundle name, Personal shield kubaz impact asset name empire, Personal shield kubaz impact asset name rebel, Personal shield kubaz muzzle asset name empire, Personal shield kubaz muzzle asset name rebel, Personal shield kubaz projectile attachment bundle, Projectile attachment bundle, Projectile length, Reduce heals asset name, Reduce heals asset profile, Reduce heals audio ability event, Reduce heals bundle name, Reduce heals impact asset name empire, Reduce heals impact asset name rebel, Reduce heals muzzle asset name empire, Reduce heals muzzle asset name rebel, Reduce heals projectile attachment bundle, S transition, Secondary attack S transition, Secondary attack alt gun locators, Secondary attack animation delay, Secondary attack arcs, Secondary attack audio ability activate, Secondary attack audio ability attack, Secondary attack audio ability loop, Secondary attack bullet, Secondary attack charge asset name, Secondary attack displayed damage per second, Secondary attack favorite target type, Secondary attack ground bullet, Secondary attack hit spark, Secondary attack max scale, Secondary attack muzzle flash, Secondary attack muzzle flash fade time, Secondary attack name, Secondary attack name, Secondary attack persistent effect, Secondary attack persistent scaling, Secondary attack projectile length, Secondary attack spin speed, Secondary attack weapon trail FX params, Shield asset name, Sniper damage asset name, Sniper damage asset profile, Sniper damage audio ability event, Sniper damage bundle name, Sniper damage impact asset name empire, Sniper damage impact asset name rebel, Sniper damage muzzle asset name empire, Sniper damage muzzle asset name rebel, Sniper damage projectile attachment bundle, Sniper health asset name, Sniper health asset profile, Sniper health audio ability event, Sniper health bundle name, Sniper health impact asset name empire, Sniper health impact asset name rebel, Sniper health muzzle asset name empire, Sniper health muzzle asset name rebel, Sniper health projectile attachment bundle, Spawn effect uid, Sum phtm X wing asset name, Sum phtm X wing asset profile, Sum phtm X wing audio ability event, Sum phtm X wing bundle name, Sum phtm X wing impact asset name empire, Sum phtm X wing impact asset name rebel, Sum phtm X wing muzzle asset name empire, Sum phtm X wing muzzle asset name rebel, Sum phtm X wing projectile attachment bundle, Sum phtm Y wing asset name, Sum phtm Y wing asset profile, Sum phtm Y wing audio ability event, Sum phtm Y wing bundle name, Sum phtm Y wing impact asset name empire, Sum phtm Y wing impact asset name rebel, Sum phtm Y wing muzzle asset name empire, Sum phtm Y wing muzzle asset name rebel, Sum phtm Y wing projectile attachment bundle, Sum phtm tie bomber asset name, Sum phtm tie bomber asset profile, Sum phtm tie bomber audio ability event, Sum phtm tie bomber bundle name, Sum phtm tie bomber impact asset name empire, Sum phtm tie bomber impact asset name rebel, Sum phtm tie bomber muzzle asset name empire, Sum phtm tie bomber muzzle asset name rebel, Sum phtm tie bomber projectile attachment bundle, Sum phtm tie fighter asset name, Sum phtm tie fighter asset profile, Sum phtm tie fighter audio ability event, Sum phtm tie fighter bundle name, Sum phtm tie fighter impact asset name empire, Sum phtm tie fighter impact asset name rebel, Sum phtm tie fighter muzzle asset name empire, Sum phtm tie fighter muzzle asset name rebel, Sum phtm tie fighter projectile attachment bundle, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament_

|Level                      |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|329|396|461|529|593|658|726|790|858|987|


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
  * _Not found: Asset offset type, Cancel tags, Death attack S1 time, Death attack S2 time, Death attack seeks target, Death attack streams, Defend splash asset offset type, Defend splash cancel tags, Defend splash details, Defend splash is refreshing, Defend splash prevent tags, Defend splash shader override, Defend splash tags, Details, Invulnerable asset offset type, Invulnerable cancel tags, Invulnerable details, Invulnerable is refreshing, Invulnerable prevent tags, Invulnerable shader override, Invulnerable tags, Is refreshing, Marksman damage asset offset type, Marksman damage cancel tags, Marksman damage details, Marksman damage is refreshing, Marksman damage prevent tags, Marksman damage shader override, Marksman damage tags, Marksman health asset offset type, Marksman health cancel tags, Marksman health details, Marksman health is refreshing, Marksman health prevent tags, Marksman health shader override, Marksman health tags, Personal shield ithorian asset offset type, Personal shield ithorian cancel tags, Personal shield ithorian details, Personal shield ithorian is refreshing, Personal shield ithorian prevent tags, Personal shield ithorian shader override, Personal shield ithorian tags, Personal shield kubaz asset offset type, Personal shield kubaz cancel tags, Personal shield kubaz details, Personal shield kubaz is refreshing, Personal shield kubaz prevent tags, Personal shield kubaz shader override, Personal shield kubaz tags, Prevent tags, Reduce heals asset offset type, Reduce heals cancel tags, Reduce heals details, Reduce heals is refreshing, Reduce heals prevent tags, Reduce heals shader override, Reduce heals tags, S1 time, S2 time, Secondary attack S1 time, Secondary attack S2 time, Secondary attack arming delay, Secondary attack clip count, Secondary attack kill cooldown reset, Secondary attack max speed, Secondary attack seeks target, Secondary attack streams, Secondary attack strict cool down, Shader override, Sniper damage asset offset type, Sniper damage cancel tags, Sniper damage details, Sniper damage is refreshing, Sniper damage prevent tags, Sniper damage shader override, Sniper damage tags, Sniper health asset offset type, Sniper health cancel tags, Sniper health details, Sniper health is refreshing, Sniper health prevent tags, Sniper health shader override, Sniper health tags, Sum phtm X wing asset offset type, Sum phtm X wing cancel tags, Sum phtm X wing details, Sum phtm X wing is refreshing, Sum phtm X wing prevent tags, Sum phtm X wing shader override, Sum phtm X wing tags, Sum phtm Y wing asset offset type, Sum phtm Y wing cancel tags, Sum phtm Y wing details, Sum phtm Y wing is refreshing, Sum phtm Y wing prevent tags, Sum phtm Y wing shader override, Sum phtm Y wing tags, Sum phtm tie bomber asset offset type, Sum phtm tie bomber cancel tags, Sum phtm tie bomber details, Sum phtm tie bomber is refreshing, Sum phtm tie bomber prevent tags, Sum phtm tie bomber shader override, Sum phtm tie bomber tags, Sum phtm tie fighter asset offset type, Sum phtm tie fighter cancel tags, Sum phtm tie fighter details, Sum phtm tie fighter is refreshing, Sum phtm tie fighter prevent tags, Sum phtm tie fighter shader override, Sum phtm tie fighter tags, Tags_

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |334101|334102|334103|334104|334105|334106|334107|334108|334109|334110|
|Point value|5     |6     |7     |8     |9     |10    |11    |12    |13    |15    |


