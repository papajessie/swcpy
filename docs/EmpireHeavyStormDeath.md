---
title: Heavy Undead Trooper (EmpireHeavyStormDeath)
category: unit
---

# Heavy Undead Trooper (EmpireHeavyStormDeath) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: No
  * Type: infantry
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 4
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|3000$|3000$|6000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |7500 |9000 |10500|12000 |13500 |15000  |16500  |18000  |19500   |22500   |
|Damage per shot     |170  |204  |238  |272   |306   |340    |374    |408    |442     |510     |
|Damage*             |500.0|600.0|700.0|800.0 |900.0 |1000.0 |1100.0 |1200.0 |1300.0  |1500.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Light vehicle (50)**, **Storage (50)**, **Flying infantry (50)**, **Vehicle hero (50)**, **HQ (50)**, **Infantry (50)**, **Droideka (50)**, **Flying vehicle (50)**, **Support troop (50)**, **Other building (50)**, **Heavy infantry hero (50)**, **Turret (50)**, **Shield (50)**, **Ressource generator (50)**, **Infantry hero (50)**, **Shield generator (50)**, **Heavy vehicular hero (50)**, **Heavy vehicle (50)**, **Heavy infantry (50)**, Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 10
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                 |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|----------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|200$                              |280$                                   |360$                                   |440$                                   |520$                                   |600$                                   |680$                                   |760$                                   |840$                                   |920$                                    |
|Training time|1m20s                             |1m28s                                  |1m32s                                  |1m36s                                  |1m40s                                  |1m44s                                  |1m48s                                  |1m52s                                  |1m56s                                  |2m                                      |
|Building     |[Barracks 10](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 10
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 1

## Attack : HeavyStormDeath

### Basic info

  * Shot count: 10
  * Time between start of clip and first shot: 500ms
  * Time between shots: 100ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 10
  * Max. Range: 5
  * Min. Range: 0

|Level                       |1    |2    |3    |4    |5    |6     |7     |8     |9     |10    |
|----------------------------|-----|-----|-----|-----|-----|------|------|------|------|------|
|Damage per shot             |170  |204  |238  |272  |306  |340   |374   |408   |442   |510   |
|Calculated damage per second|500  |600  |700  |800  |900  |1000  |1100  |1200  |1300  |1500  |
|Damage*                     |500.0|600.0|700.0|800.0|900.0|1000.0|1100.0|1200.0|1300.0|1500.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 10
  * Number of cannons: 0
  * Clips period: 3.400s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 30
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
  * Wall: 80%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_gatling_hit_r_lrg
  * projectilemuzzleFlash: fx_gatling_muzzle_r_lrg
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: closest
  * buffAssetOffset: 0.00,0.27,0.00
  * eventButtonAction: 
  * gunPosition: deathheavytrooper_emp_rig_MASTER_MOVER/deathheavytrooper_emp_rig_locator_gun_Rt:1
  * iconCameraPosition: 4.46,8.55,22.59
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_deathtrooper_1":35,"sfx_death_deathtrooper_2":35,"sfx_death_deathtrooper_3":30
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_deathtrooper_1":35,"sfx_placement_deathtrooper_2":35,"sfx_placement_deathtrooper_3":30
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: buffFireBurn:15
  * iconLookatPosition: -0.36,1.33,-0.66
  * iconUnlockScale: 
  * bundleName: heavytrooper_dth-ani
  * assetName: heavytrooper_dth-ani
  * audioTrain: 
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 3.27,3.36,10.55
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * iconCloseupLookatPosition: -0.05,2.29,-0.46
  * upgradeShardUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * targetInRangeModifier: 1
  * projectilestreams: no
  * strictCoolDown: false
  * autoSpawnSpreadingScale: 1
  * armingDelay: 0
  * spawnApplyBuffs: buffReduceHeals2
  * maxScale: false
  * autoSpawnRateScale: 1
  * impactDelay: 500

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|4.000 |4.800 |5.600 |6.400 |7.200 |8.000 |8.800 |9.600 |10.400|12.000|
|order     |133001|133002|133003|133004|133005|133006|133007|133008|133009|133010|

