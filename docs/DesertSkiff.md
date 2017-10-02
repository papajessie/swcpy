---
title: Anti-Vehicle Skiff (DesertSkiff)
category: unit
---

# Anti-Vehicle Skiff (DesertSkiff) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: vehicle
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 7
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|700$  |3000$ |6000$ |15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s    |15m   |1h    |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w3d    |
|Health              |11200 |11710 |12240 |12800 |13380 |14000  |14650  |15330  |16050   |16800   |
|Damage per shot     |3920  |4100  |4280  |4480  |4690  |4900   |5130   |5370   |5620    |5890    |
|Damage*             |1540.0|1610.0|1680.0|1760.0|1840.0|1930.0 |2020.0 |2110.0 |2210.0  |2310.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Light vehicle (60)**, **Heavy vehicle (60)**, **Flying vehicle (60)**, _Flying infantry (55)_, _Heavy infantry (55)_, _Infantry (55)_, _Support troop (55)_, _Droideka (55)_, Turret (50), Shield (50), Storage (50), Other building (50), Shield generator (50), Ressource generator (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|1050$                         |1070$                                 |1090$                                 |1110$                                 |1130$                                 |1160$                                 |1190$                                 |1400$                                 |1470$                                 |1610$                                  |
|Training time|3m2s                          |3m3s                                  |3m4s                                  |3m5s                                  |3m6s                                  |3m7s                                  |3m9s                                  |3m16s                                 |3m23s                                 |3m30s                                  |
|Building     |[Factory 6](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : DesertSkiff

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 500ms
  * Time between shots: 250ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1.500s
  * Salvos per clip: 1

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |3920  |4100  |4280  |4480  |4690  |4900  |5130  |5370  |5620  |5890  |
|Calculated damage per second|1960  |2050  |2140  |2240  |2345  |2450  |2565  |2685  |2810  |2945  |
|Damage*                     |1540.0|1610.0|1680.0|1760.0|1840.0|1930.0|2020.0|2110.0|2210.0|2310.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 2s
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 12
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 75%
  * Heavy infantry: 100%
  * Heavy vehicle: 200%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 400%
  * Support troop: 100%
  * Heavy infantry hero: 100%
  * Heavy vehicular hero: 200%
  * Infantry hero: 100%
  * Vehicle hero: 400%
  * Infantry: 100%
  * Ressource generator: 75%
  * Shield: 75%
  * Shield generator: 75%
  * Storage: 75%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 400%
  * Wall: 75%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_rocket_hit_r_med
  * projectilemuzzleFlash: fx_rocket_muzzle_r_med
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 0.00,1.7,0.00
  * favoriteTargetType: vehicles
  * audioDeath: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * factoryScaleFactor: 0.90000000000000002220446049250313080847263336181640625
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 
  * iconUnlockRotation: 
  * audioTrain: 
  * iconCameraPosition: 25.92,23.21,24.67
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * newRotationSpeed: 7854
  * bundleName: banthabarge_rbl-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_empire_atmp_1":35,"sfx_attack_empire_atmp_2":35,"sfx_attack_empire_atmp_3":30
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * audioImpact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * hologramUid: 
  * iconLookatPosition: -0.09,2.29,-0.96
  * assetName: banthabarge_rbl-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 500
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * projectilebullet: fx_rocket_projectile_r_med

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|7.000 |8.400 |9.800 |11.200|12.600|14.000|15.400|16.800|18.200|21.000|
|order     |230601|230602|230603|230604|230605|230606|230607|230608|230609|230610|

