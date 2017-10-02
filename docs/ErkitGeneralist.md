---
title: Er'Kit Militia Conscript (ErkitGeneralist)
category: unit
---

# Er'Kit Militia Conscript (ErkitGeneralist) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Independant units
  * Type: infantry
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1      |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-------|-----|-----|------|------|-------|-------|-------|--------|--------|
|Buildable unit      |Yes    |Yes  |Yes  |Yes   |Yes   |Yes    |Yes    |Yes    |No      |No      |
|Upgrade requirements|Nothing|1500$|4000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s     |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |1300   |1560 |1680 |1920  |2160  |2400   |2640   |2880   |3120    |3600    |
|Damage per shot     |141    |169  |182  |208   |234   |260    |286    |312    |338     |390     |
|Damage*             |301.0  |361.0|389.0|445.0 |500.0 |556.0  |612.0  |667.0  |723.0   |834.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Turret (50)**, **Shield (50)**, **Storage (50)**, **Other building (50)**, **Heavy vehicle (50)**, **Shield generator (50)**, **Ressource generator (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Support troop (50)**, **Droideka (50)**, **HQ (50)**, Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                                                            |2                                                                            |3                                                                            |4                                                                            |5                                                                            |6                                                                            |7                                                                            |8                                                                            |9                                                                            |10                                                                            |
|-------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
|Training cost|50$                                                                          |70$                                                                          |90$                                                                          |110$                                                                         |130$                                                                         |150$                                                                         |170$                                                                         |190$                                                                         |210$                                                                         |230$                                                                          |
|Training time|42s                                                                          |44s                                                                          |46s                                                                          |48s                                                                          |50s                                                                          |52s                                                                          |54s                                                                          |56s                                                                          |58s                                                                          |1m                                                                            |
|Building     |[bld_title_syndicateBarracks (no text translation) 1](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 2](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 3](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 4](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 5](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 6](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 7](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 8](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 9](syndicateBarracks.html)|[bld_title_syndicateBarracks (no text translation) 10](syndicateBarracks.html)|

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 1

## Attack : Soldier

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 500ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 3

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |141  |169  |182  |208  |234  |260  |286  |312  |338  |390  |
|Calculated damage per second|302  |362  |390  |445  |501  |557  |612  |668  |724  |835  |
|Damage*                     |301.0|361.0|389.0|445.0|500.0|556.0|612.0|667.0|723.0|834.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 3
  * Number of cannons: 0
  * Clips period: 1.400s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 100%
  * Heavy vehicle: 100%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 100%
  * Heavy vehicular hero: 100%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 100%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilemuzzleFlash: fx_blaster_flash_b_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: closest
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * iconCameraPosition: 8.56,9.58,10.6
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "soldier_rbl_rig_MASTER_MOVER/soldier_rbl_rig_locator_gun":1
  * newRotationSpeed: 7854
  * bundleName: erkit1_neu-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: 0.09,1.4,0.28
  * assetName: erkit1_neu-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 1000
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * projectilebullet: fx_blaster_beam_b_sm

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|1.000 |1.200 |1.400 |1.600 |1.800 |2.000 |2.200 |2.400 |2.600 |3.000 |
|order     |333901|333902|333903|333904|333905|333906|333907|333908|333909|333910|

