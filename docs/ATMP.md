---
title: AT-MP (ATMP)
category: unit
---

# AT-MP (ATMP) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: vehicle
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 15
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|5000$ |5000$ |10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|
|Upgrade time        |0s    |1h    |2h30m |7h    |20h   |2d12h  |4d     |6d     |1w1d    |2w      |
|Health              |10800 |11420 |12080 |12780 |13520 |14320  |15160  |16070  |17030   |18050   |
|Damage per shot     |2310  |2440  |2580  |2730  |2890  |3060   |3240   |3430   |3630    |3850    |
|Damage*             |3240.0|3420.0|3620.0|3830.0|4060.0|4290.0 |4550.0 |4810.0 |5090.0  |5400.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Shield (90)**, **Shield generator (90)**, Light vehicle (50), Storage (50), Flying infantry (50), HQ (50), Infantry (50), Droideka (50), Flying vehicle (50), Support troop (50), Other building (50), Turret (50), Ressource generator (50), Heavy vehicle (50), Heavy infantry (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 10
  * Target preferences strength: 90
  * Retargeting offset: 16
  * Clip retargeting: No
  * Target shield border: Yes
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|1650$                          |1720$                                  |1790$                                  |1870$                                  |1950$                                  |2250$                                  |2550$                                  |3000$                                  |3150$                                  |3450$                                   |
|Training time|4m                             |4m2s                                   |4m4s                                   |4m7s                                   |4m10s                                  |4m20s                                  |4m30s                                  |7m                                     |7m15s                                  |7m30s                                   |
|Building     |[Factory 4](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : ATMP

### Basic info

  * Shot count: 4
  * Time between start of clip and first shot: 250ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 4
  * Max. Range: 8
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2310  |2440  |2580  |2730  |2890  |3060  |3240  |3430  |3630  |3850  |
|Calculated damage per second|3242  |3424  |3621  |3831  |4056  |4294  |4547  |4814  |5094  |5403  |
|Damage*                     |3240.0|3420.0|3620.0|3830.0|4060.0|4290.0|4550.0|4810.0|5090.0|5400.0|

### Secondary info

  * Gun shooting sequence: 1,3,5,2,4,6
  * Salvos per clip: 4
  * Number of cannons: 0
  * Clips period: 2.850s
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 12
  * Projectile is directional: Yes
  * Salvos per gun sequence: 6
  * Cannons shot per gun sequence: 6

### Multipliers

  * HQ: 75%
  * Heavy infantry: 100%
  * Heavy vehicle: 100%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 100%
  * Heavy vehicular hero: 100%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 75%
  * Shield: 400%
  * Shield generator: 400%
  * Storage: 75%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 100%
  * Wall: 60%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_rocket_hit_r_sm
  * projectilemuzzleFlash: fx_rocket_muzzle_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: shieldGenerator
  * buffAssetOffset: 0.00,3.0,0.00
  * eventButtonAction: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * iconCameraPosition: 22.45,15.49,39.24
  * newRotationSpeed: 2000
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_empire_atmp_1":100
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * iconUnlockRotation: 
  * audioImpact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * factoryRotation: -90
  * infoUIType: 
  * factoryScaleFactor: 0.8910000000000000142108547152020037174224853515625
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: 
  * iconLookatPosition: -0.73,2.62,-0.75
  * iconUnlockScale: 
  * bundleName: atmp_emp-ani
  * assetName: atmp_emp-ani
  * audioTrain: 
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_empire_atmp_1":35,"sfx_attack_empire_atmp_2":35,"sfx_attack_empire_atmp_3":30
  * iconCloseupLookatPosition: 
  * upgradeShardUid: 
  * rotationSpeed: 2
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 2
  * projectilestreams: no
  * maxScale: false
  * strictCoolDown: false
  * targetInRangeModifier: 1
  * armingDelay: 0
  * projectilebullet: fx_rocket_projectile_r_sm
  * autoSpawnRateScale: 2
  * impactDelay: 1000

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|15.000|18.000|21.000|24.000|27.000|30.000|33.000|36.000|39.000|45.000|
|order     |130401|130402|130403|130404|130405|130406|130407|130408|130409|130410|

