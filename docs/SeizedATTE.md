---
title: Seized AT-TE Walker (SeizedATTE)
category: unit
---

# Seized AT-TE Walker (SeizedATTE) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: No
  * Type: vehicle
  * Armor type: bruiserVehicle
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 20
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|600$  |1500$ |4000$ |12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s    |15m   |1h    |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |76800 |78710 |80670 |82690 |84760 |86890  |89080  |91320  |93630   |96000   |
|Damage per shot     |3070  |3150  |3230  |3310  |3390  |3470   |3560   |3650   |3740    |3840    |
|Damage*             |3840.0|3940.0|4040.0|4140.0|4240.0|4340.0 |4450.0 |4560.0 |4680.0  |4800.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Heavy infantry (60)**, **Infantry hero (60)**, **Flying infantry (60)**, **Droideka (60)**, **Support troop (60)**, **Infantry (60)**, **Heavy infantry hero (60)**, Other building (50), Vehicle hero (50), HQ (50), Shield (50), Heavy vehicle (50), Heavy vehicular hero (50), Storage (50), Shield generator (50), Light vehicle (50), Turret (50), Ressource generator (50), Flying vehicle (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 16
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|4400$                          |4420$                                  |4440$                                  |4460$                                  |4490$                                  |4520$                                  |4550$                                  |4580$                                  |4620$                                  |5060$                                   |
|Training time|9m20s                          |9m22s                                  |9m24s                                  |9m26s                                  |9m28s                                  |9m30s                                  |9m33s                                  |9m36s                                  |9m40s                                  |10m                                     |
|Building     |[Factory 8](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 10
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x3
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : ATTE Blaster

### Basic info

  * Shot count: 5
  * Time between start of clip and first shot: 1s
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1s
  * Salvos per clip: 5
  * Max. Range: 8
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |3070  |3150  |3230  |3310  |3390  |3470  |3560  |3650  |3740  |3840  |
|Calculated damage per second|3837  |3937  |4037  |4137  |4237  |4337  |4450  |4562  |4675  |4800  |
|Damage*                     |3840.0|3940.0|4040.0|4140.0|4240.0|4340.0|4450.0|4560.0|4680.0|4800.0|

### Secondary info

  * Gun shooting sequence: 1,2,3,4,5
  * Salvos per clip: 5
  * Number of cannons: 0
  * Clips period: 4s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 25
  * Projectile is directional: Yes
  * Salvos per gun sequence: 5
  * Cannons shot per gun sequence: 5

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

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_r_med
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_r_med

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_empire_atat_1":100
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * shieldAssetName: 
  * audioAttack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * decalSize: 
  * newRotationSpeed: 982
  * tooltipHeightOffset: 
  * eventButtonString: 
  * gunPosition: "atte_rbl_rig_MASTER_MOVER/atte_rbl_rig_locator_gun1":1,"atte_rbl_rig_MASTER_MOVER/atte_rbl_rig_locator_gun2":2,"atte_rbl_rig_MASTER_MOVER/atte_rbl_rig_locator_gun3":3,"atte_rbl_rig_MASTER_MOVER/atte_rbl_rig_locator_gun4":4,"atte_rbl_rig_MASTER_MOVER/atte_rbl_rig_locator_gun5":5
  * infoUIType: 
  * bundleName: atte_rbl-ani
  * deathAnimation: 
  * favoriteTargetType: infantry
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_walker_1":100
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * iconCameraPosition: 24.47,22.61,37.05
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 0.00,1.46,0.00
  * iconCloseupCameraPosition: 
  * hologramUid: 
  * rotationSpeed: 0.9817468750000000188293824976426549255847930908203125
  * iconCloseupLookatPosition: 
  * assetName: atte_rbl-ani
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * iconLookatPosition: -0.2,1.23,-0.57
  * factoryScaleFactor: 1
  * audioTrain: 

## Uninterpreted stats

  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 2
  * autoSpawnSpreadingScale: 2
  * impactDelay: 500
  * projectilebullet: fx_blaster_beam_r_med
  * targetInRangeModifier: 1

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|order|520404|520408|520412|520416|520420|520424|520428|520432|520436|520440|

