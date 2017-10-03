---
title: AT-DP (ATDP)
category: unit
---

# AT-DP (ATDP) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: bruiserVehicle
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 16
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|600$  |1500$ |4000$ |12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s    |15m   |1h    |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |61440 |62970 |64540 |66150 |67810 |69510  |71260  |73060  |74900   |76800   |
|Damage per shot     |3460  |3540  |3630  |3720  |3810  |3910   |4010   |4110   |4210    |4320    |
|Damage*             |3080.0|3150.0|3230.0|3310.0|3390.0|3480.0 |3560.0 |3650.0 |3740.0  |3840.0  |

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
|Training cost|3520$                          |3540$                                  |3560$                                  |3580$                                  |3600$                                  |3620$                                  |3640$                                  |3660$                                  |3696$                                  |4048$                                   |
|Training time|7m28s                          |7m29s                                  |7m30s                                  |7m32s                                  |7m34s                                  |7m36s                                  |7m38s                                  |7m40s                                  |7m44s                                  |8m                                      |
|Building     |[Factory 8](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 10
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x2
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : ATDP Blaster

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 1s
  * Time between shots: 250ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1s
  * Salvos per clip: 2
  * Max. Range: 8
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |3460  |3540  |3630  |3720  |3810  |3910  |4010  |4110  |4210  |4320  |
|Calculated damage per second|3075  |3146  |3226  |3306  |3386  |3475  |3564  |3653  |3742  |3840  |
|Damage*                     |3080.0|3150.0|3230.0|3310.0|3390.0|3480.0|3560.0|3650.0|3740.0|3840.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 2.250s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 25
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

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
  * projectilehitSpark: fx_blaster_beam_r_med
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_beam_r_med

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * shieldAssetName: 
  * audioAttack: "sfx_attack_walker_1":25,"sfx_attack_walker_2":25,"sfx_attack_walker_3":25,"sfx_attack_walker_4":25
  * decalSize: 
  * newRotationSpeed: 3927
  * tooltipHeightOffset: 
  * eventButtonString: 
  * gunPosition: "atdp_emp_rig_MASTER_MOVER/atdp_emp_rig_locator_gun":1
  * infoUIType: 
  * bundleName: atdp_emp-ani
  * deathAnimation: 
  * favoriteTargetType: infantry
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_walker_1":100
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * iconCameraPosition: 24.3,22.81,41.64
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 0.00,1.89,0.00
  * iconCloseupCameraPosition: 
  * hologramUid: 
  * rotationSpeed: 3.92698750000000007531752999057061970233917236328125
  * iconCloseupLookatPosition: 
  * assetName: atdp_emp-ani
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * iconLookatPosition: -0.85,2.34,-1.34
  * factoryScaleFactor: 0.8689999999999999946709294817992486059665679931640625
  * audioTrain: 

## Uninterpreted stats

  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 1
  * autoSpawnSpreadingScale: 1
  * impactDelay: 500
  * projectilebullet: fx_blaster_beam_r_med
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|order     |130801|130802|130803|130804|130805|130806|130807|130808|130809|130810|
|pointValue|16.000|19.200|22.400|25.600|28.800|32.000|35.200|38.400|41.600|48.000|

