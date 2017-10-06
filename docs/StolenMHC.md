---
title: Stolen Mobile Heavy Cannon (StolenMHC)
category: unit
---

# Stolen Mobile Heavy Cannon (StolenMHC) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: No
  * Type: vehicle
  * Armor type: vehicle
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 12
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|6500$ |3000$ |6000$ |15000$|35000$|115000$|200000$|385000$|1250000$|2250000$|
|Upgrade time        |0s    |1h    |2h30m |7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Health              |10800 |12960 |15120 |17280 |19440 |21600  |23760  |25920  |28080   |32400   |
|Damage per shot     |2160  |2592  |3024  |3456  |3888  |4320   |4752   |5184   |5616    |6480    |
|Damage*             |1200.0|1440.0|1680.0|1920.0|2160.0|2400.0 |2640.0 |2880.0 |3120.0  |3600.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (70)**, Light vehicle (50), Storage (50), Flying infantry (50), HQ (50), Infantry (50), Droideka (50), Flying vehicle (50), Support troop (50), Other building (50), Shield (50), Ressource generator (50), Shield generator (50), Heavy vehicle (50), Heavy infantry (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|500$                          |700$                                  |900$                                  |1100$                                 |1300$                                 |1500$                                 |1700$                                 |2400$                                 |2700$                                 |3000$                                  |
|Training time|4m12s                         |4m24s                                 |4m36s                                 |4m48s                                 |5m                                    |5m12s                                 |5m24s                                 |5m36s                                 |5m48s                                 |6m                                     |
|Building     |[Factory 7](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 10
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x2
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 200

## Attack : projectileMHC

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 900ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 900ms
  * Salvos per clip: 1
  * Max. Range: 10
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2160  |2592  |3024  |3456  |3888  |4320  |4752  |5184  |5616  |6480  |
|Calculated damage per second|1200  |1440  |1680  |1920  |2160  |2400  |2640  |2880  |3120  |3600  |
|Damage*                     |1200.0|1440.0|1680.0|1920.0|2160.0|2400.0|2640.0|2880.0|3120.0|3600.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 1.800s
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 12
  * Projectile is directional: No
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 25%
  * Heavy infantry: 50%
  * Heavy vehicle: 250%
  * Other building: 25%
  * Droideka: 100%
  * Flying infantry: 50%
  * Flying vehicle: 300%
  * Support troop: 50%
  * Heavy infantry hero: 50%
  * Heavy vehicular hero: 250%
  * Infantry hero: 50%
  * Vehicle hero: 300%
  * Infantry: 50%
  * Ressource generator: 25%
  * Shield: 25%
  * Shield generator: 25%
  * Storage: 25%
  * Trap: 200%
  * Turret: 200%
  * Light vehicle: 300%
  * Wall: 80%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_UMHC_hit_r_lrg
  * projectilemuzzleFlash: fx_UMHC_muzzle_r_lrg
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: turret
  * buffAssetOffset: 0.00,0.90,0
  * eventButtonAction: 
  * gunPosition: "umhc_emp_rig_MASTER_MOVER/umhc_emp_rig_locator_gun":1
  * iconCameraPosition: 30.35,41.15,37.35
  * newRotationSpeed: 15708
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_empire_umhc_1":100
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_empire_atat_1":100
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 90
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: 
  * iconLookatPosition: -0.33,0.73,-0.17
  * iconUnlockScale: 
  * bundleName: umhc_emp-ani
  * assetName: umhc_emp-ani
  * audioTrain: 
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_empire_umhc_1":33,"sfx_attack_empire_umhc_2":33,"sfx_attack_empire_umhc_3":34
  * iconCloseupLookatPosition: 
  * upgradeShardUid: 
  * rotationSpeed: 31.41590000000000060254023992456495761871337890625
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 2
  * projectilestreams: no
  * maxScale: false
  * strictCoolDown: false
  * targetInRangeModifier: 1
  * armingDelay: 0
  * projectilebullet: fx_UMHC_projectile_r_lrg
  * autoSpawnRateScale: 2
  * impactDelay: 500

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|order|481204|481208|481212|481216|481220|481224|481228|481232|481236|481240|

