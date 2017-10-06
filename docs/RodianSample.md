---
title: Rodian Recon Sniper (RodianSample)
category: unit
---

# Rodian Recon Sniper (RodianSample) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: No
  * Type: infantry
  * Armor type: infantry
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 7
  * Upgrade requirements: Nothing
  * Upgrade time: 0s
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level          |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|---------------|------|------|------|------|------|------|------|------|------|------|
|Health         |2800  |3360  |3920  |4480  |5040  |5600  |6160  |6720  |7280  |8400  |
|Damage per shot|835   |1001  |1168  |1335  |1502  |1669  |1836  |2002  |2169  |2503  |
|Damage*        |2195.0|2745.0|3365.0|4040.0|4765.0|5565.0|6415.0|7315.0|8275.0|9980.0|

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (60)**, **Infantry (60)**, **Droideka (60)**, **Support troop (60)**, **Heavy infantry (60)**, Light vehicle (50), Storage (50), HQ (50), Flying vehicle (50), Other building (50), Turret (50), Shield (50), Ressource generator (50), Shield generator (50), Heavy vehicle (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

  * Training cost: Free
  * Training time: 0s

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : projectileSniper

### Basic info

  * Shot count: 5
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1.500s
  * Salvos per clip: 5
  * Max. Range: 10
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |835   |1001  |1168  |1335  |1502  |1669  |1836  |2002  |2169  |2503  |
|Calculated damage per second|1113  |1334  |1557  |1780  |2002  |2225  |2448  |2669  |2892  |3337  |
|Damage*                     |2195.0|2745.0|3365.0|4040.0|4765.0|5565.0|6415.0|7315.0|8275.0|9980.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 5
  * Number of cannons: 0
  * Clips period: 3.750s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 250%
  * Heavy vehicle: 150%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 300%
  * Flying vehicle: 200%
  * Support troop: 300%
  * Heavy infantry hero: 250%
  * Heavy vehicular hero: 150%
  * Infantry hero: 300%
  * Vehicle hero: 200%
  * Infantry: 300%
  * Ressource generator: 100%
  * Shield: 50%
  * Shield generator: 50%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 200%
  * Wall: 40%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilemuzzleFlash: fx_blaster_flash_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: heroes
  * buffAssetOffset: 
  * eventButtonAction: 
  * gunPosition: 
  * iconCameraPosition: 5.8,8.85,16.13
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_rodian_1":33,"sfx_death_rodian_2":33,"sfx_death_rodian_3":34
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: buffFireBurn:15
  * iconLookatPosition: -0.51,1.24,-0.7
  * iconUnlockScale: 
  * bundleName: rodiansniper_emp-ani
  * assetName: rodiansniper_emp-ani
  * audioTrain: "sfx_ui_unitcomplete_rodian_01":50,"sfx_ui_unitcomplete_rodian_02":50
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 2.41,5.49,9.51
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_ig86_01":33,"sfx_attack_ig86_02":33,"sfx_attack_ig86_03":34
  * iconCloseupLookatPosition: -0.33,1.97,-1.12
  * upgradeShardUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * projectilestreams: no
  * newTargetOnReload: false
  * projectilebullet: fx_blaster_beam_r_sm
  * autoSpawnSpreadingScale: 2
  * pointValue: 1.000
  * impactDelay: 1000
  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * autoSpawnRateScale: 2

|Level          |1                                                        |2                                                        |3                                                        |4                                                        |5                                                        |6                                                        |7                                                        |8                                                        |9                                                        |10                                                          |
|---------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------|
|order          |314600                                                   |314601                                                   |314602                                                   |314603                                                   |314604                                                   |314605                                                   |314606                                                   |314607                                                   |314608                                                   |314609                                                      |
|spawnApplyBuffs|buffSniperHealth1,buffSniperDamage1,buffSumPhtmTieBomber1|buffSniperHealth2,buffSniperDamage2,buffSumPhtmTieBomber2|buffSniperHealth3,buffSniperDamage3,buffSumPhtmTieBomber3|buffSniperHealth4,buffSniperDamage4,buffSumPhtmTieBomber4|buffSniperHealth5,buffSniperDamage5,buffSumPhtmTieBomber5|buffSniperHealth6,buffSniperDamage6,buffSumPhtmTieBomber6|buffSniperHealth7,buffSniperDamage7,buffSumPhtmTieBomber7|buffSniperHealth8,buffSniperDamage8,buffSumPhtmTieBomber8|buffSniperHealth9,buffSniperDamage9,buffSumPhtmTieBomber9|buffSniperHealth10,buffSniperDamage10,buffSumPhtmTieBomber10|

