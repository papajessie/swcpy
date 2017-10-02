---
title: 2-M Hover Tank (2MTank)
category: unit
---

# 2-M Hover Tank (2MTank) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: bruiserVehicle
  * Role: Bruiser
  * Levels available: 1-10
  * Unit capacity: 10
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|2900$|3000$|6000$|15000$|35000$|115000$|200000$|385000$|1250000$|2250000$|
|Upgrade time        |0s   |1h   |2h30m|7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Health              |14000|16800|19600|22400 |25200 |28000  |30800  |33600  |36400   |42000   |
|Damage per shot     |499  |599  |699  |798   |898   |998    |1098   |1197   |1297    |1497    |
|Damage*             |700.0|840.0|981.0|1120.0|1260.0|1400.0 |1541.0 |1680.0 |1820.0  |2101.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (70)**, Flying infantry (50), Light vehicle (50), Heavy infantry (50), Shield (50), Storage (50), Other building (50), Heavy vehicle (50), Shield generator (50), Ressource generator (50), Infantry (50), Flying vehicle (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 16
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|500$                           |700$                                   |900$                                   |1100$                                  |1300$                                  |1500$                                  |1700$                                  |2000$                                  |2100$                                  |2300$                                   |
|Training time|3m20s                          |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |4m40s                                  |4m50s                                  |5m                                      |
|Building     |[Factory 3](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x3
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : 2MTank

### Basic info

  * Shot count: 4
  * Time between start of clip and first shot: 250ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 4

|Level                       |1    |2    |3    |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|-----|-----|-----|------|------|------|------|------|------|------|
|Damage per shot             |499  |599  |699  |798   |898   |998   |1098  |1197  |1297  |1497  |
|Calculated damage per second|700  |840  |981  |1120  |1260  |1400  |1541  |1680  |1820  |2101  |
|Damage*                     |700.0|840.0|981.0|1120.0|1260.0|1400.0|1541.0|1680.0|1820.0|2101.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 4
  * Number of cannons: 0
  * Clips period: 2.850s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 25%
  * Heavy vehicle: 25%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 50%
  * Flying vehicle: 50%
  * Support troop: 50%
  * Heavy infantry hero: 25%
  * Heavy vehicular hero: 25%
  * Infantry hero: 50%
  * Vehicle hero: 50%
  * Infantry: 50%
  * Ressource generator: 100%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 50%
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_blaster_hit_r_lrg
  * projectilemuzzleFlash: fx_blaster_flash_r_lrg
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 0.0,1.14,0.0
  * favoriteTargetType: turret
  * audioDeath: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * factoryScaleFactor: 0.842999999999999971578290569595992565155029296875
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
  * iconCameraPosition: 30.83,30.71,28.35
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "replrtnk_emp_rig_MASTER_MOVER/replrtnk_emp_rig_locator_gun":1
  * newRotationSpeed: 2000
  * bundleName: replrtnk_emp-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_tank_1":25,"sfx_attack_tank_2":25,"sfx_attack_tank_3":25,"sfx_attack_tank_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.22,1.4,-0.74
  * assetName: replrtnk_emp-ani
  * rotationSpeed: 2
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 3
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 1000
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 3
  * projectilebullet: fx_blaster_beam_r_lrg

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|10.000|12.000|14.000|16.000|18.000|20.000|22.000|24.000|26.000|30.000|
|order     |130301|130302|130303|130304|130305|130306|130307|130308|130309|130310|

