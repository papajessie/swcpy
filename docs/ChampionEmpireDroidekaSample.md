---
title: Droideka Sentinal (ChampionEmpireDroidekaSample)
category: unit
---

# Droideka Sentinal (ChampionEmpireDroidekaSample) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: No
  * Type: vehicle
  * Armor type: champion
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 12
  * Upgrade requirements: Nothing
  * Upgrade time: 0s
  * Shield Cooldown: 20s
  * Shield Range: 3

|Level          |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|---------------|------|------|------|------|------|------|------|------|------|------|
|Health         |19200 |23680 |26880 |30080 |33280 |36480 |39040 |41600 |43840 |46080 |
|Damage per shot|660   |815   |925   |1034  |1145  |1255  |1343  |965   |1036  |1106  |
|Damage*        |2640.0|3260.0|3699.0|4136.0|4578.0|5019.0|5370.0|5721.0|6216.0|6636.0|
|Shield Health  |14400 |17760 |20160 |22560 |24960 |27360 |29280 |31200 |32400 |33600 |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Droideka (80)**, _Infantry hero (70)_, _Vehicle hero (70)_, _Heavy vehicular hero (70)_, _Heavy infantry hero (70)_, _Heavy infantry (60)_, _Flying infantry (60)_, _Support troop (60)_, _Infantry (60)_, _Heavy vehicle (60)_, _Light vehicle (60)_, _Flying vehicle (60)_, Other building (50), HQ (50), Shield (50), Storage (50), Shield generator (50), Turret (50), Ressource generator (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

  * Training cost: Free
  * Building: [Headquarters 1](empireHQ.html)

|Level        |1   |2    |3    |4    |5    |6    |7   |8    |9    |10   |
|-------------|----|-----|-----|-----|-----|-----|----|-----|-----|-----|
|Training time|1h8m|1h18m|1h28m|1h39m|1h48m|1h58m|2h8m|2h19m|2h19m|2h19m|

## Movement

  * Speed: 30
  * Run speed: 100
  * Run threshold: 7
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : Empire Droideka Blaster

### Basic info

  * Time between start of clip and first shot: 500ms
  * Time between shots: 233ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 4
  * Max. Range: 7
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |660   |815   |925   |1034  |1145  |1255  |1343  |965   |1036  |1106  |
|Shot count                  |8     |8     |8     |8     |8     |8     |8     |12    |12    |12    |
|Calculated damage per second|3107  |3837  |4355  |4868  |5391  |5909  |6323  |6815  |7317  |7811  |
|Damage*                     |2640.0|3260.0|3699.0|4136.0|4578.0|5019.0|5370.0|5721.0|6216.0|6636.0|

### Secondary info

  * Salvos per clip: 4
  * Number of cannons: 0
  * Clips period: 1.699s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 25
  * Projectile is directional: Yes
  * Salvos per gun sequence: 2

|Level                        |1      |2      |3      |4      |5      |6      |7      |8          |9          |10         |
|-----------------------------|-------|-------|-------|-------|-------|-------|-------|-----------|-----------|-----------|
|Gun shooting sequence        |1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,1,2,2,2|1,1,1,2,2,2|1,1,1,2,2,2|
|Cannons shot per gun sequence|4      |4      |4      |4      |4      |4      |4      |6          |6          |6          |

### Multipliers

  * HQ: 100%
  * Heavy infantry: 75%
  * Heavy vehicle: 75%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 75%
  * Heavy vehicular hero: 75%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 50%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 80%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_y_sm
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_y_sm

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_empire_droideka_1":50,"sfx_placement_empire_droideka_2":50
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_empire_droideka_1":25,"sfx_attack_empire_droideka_2":25,"sfx_attack_empire_droideka_3":25,"sfx_attack_empire_droideka_4":25
  * decalSize: 160
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 1.5
  * eventButtonString: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2
  * infoUIType: 
  * deathAnimation: 
  * favoriteTargetType: closest
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_empire_droideka_1":35,"sfx_death_empire_droideka_2":35,"sfx_death_empire_droideka_3":30
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 0.00,0.65,0.00
  * iconCloseupCameraPosition: 
  * hologramUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: 
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * factoryScaleFactor: 0.8689999999999999946709294817992486059665679931640625
  * audioTrain: 

|Level             |1                          |2                           |3                           |4                           |5                           |6                           |7                           |8                           |9                           |10                          |
|------------------|---------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
|shieldAssetName   |effectEmpireDroidekaShield1|effectEmpireDroidekaShield10|effectEmpireDroidekaShield10|effectEmpireDroidekaShield20|effectEmpireDroidekaShield20|effectEmpireDroidekaShield30|effectEmpireDroidekaShield30|effectEmpireDroidekaShield40|effectEmpireDroidekaShield40|effectEmpireDroidekaShield40|
|bundleName        |droideka_con-ani-up1       |droideka_con-ani-up10       |droideka_con-ani-up10       |droideka_con-ani-up20       |droideka_con-ani-up20       |droideka_con-ani-up30       |droideka_con-ani-up30       |droideka_con-ani-up40       |droideka_con-ani-up40       |droideka_con-ani-up40       |
|iconCameraPosition|18.67,14.16,15.1           |15.43,14.67,18.88           |15.43,14.67,18.88           |15.88,14.81,19.14           |15.88,14.81,19.14           |15.91,14.58,19.08           |15.91,14.58,19.08           |21.79,18.39,13.58           |21.79,18.39,13.58           |21.79,18.39,13.58           |
|assetName         |droideka_con-ani-up1       |droideka_con-ani-up10       |droideka_con-ani-up10       |droideka_con-ani-up20       |droideka_con-ani-up20       |droideka_con-ani-up30       |droideka_con-ani-up30       |droideka_con-ani-up40       |droideka_con-ani-up40       |droideka_con-ani-up40       |
|iconLookatPosition|-0.39,1.23,-0.21           |-0.32,1.71,0.09             |-0.32,1.71,0.09             |-0.19,1.6,0                 |-0.19,1.6,0                 |-0.1,1.43,0.08              |-0.1,1.43,0.08              |-0.35,1.49,0.26             |-0.35,1.49,0.26             |-0.35,1.49,0.26             |

## Uninterpreted stats

  * strictCoolDown: false
  * armingDelay: 0
  * targetInRangeModifier: 1
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 2
  * autoSpawnSpreadingScale: 2
  * impactDelay: 1000
  * projectilebullet: fx_blaster_beam_r_sm
  * spawnEffectUid: effectEmpireSpawn

|Level     |1     |2     |3     |4      |5      |6      |7      |8      |9      |10     |
|----------|------|------|------|-------|-------|-------|-------|-------|-------|-------|
|pointValue|40.000|68.000|88.000|108.000|128.000|148.000|172.000|200.000|200.000|200.000|

