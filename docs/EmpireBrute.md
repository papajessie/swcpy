---
title: Dowutin Hunter (EmpireBrute)
category: unit
---

# Dowutin Hunter (EmpireBrute) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: mercenary
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 12
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1      |2         |3         |4         |5         |6          |7          |8          |9          |10         |
|--------------------|-------|----------|----------|----------|----------|-----------|-----------|-----------|-----------|-----------|
|Upgrade requirements|Nothing|12000 Con.|25000 Con.|50000 Con.|99000 Con.|190000 Con.|250000 Con.|270000 Con.|280000 Con.|285000 Con.|
|Upgrade time        |0s     |4d        |5d        |6d        |1w        |1w1d       |1w2d       |1w3d       |1w4d       |1w5d       |
|Health              |24948  |27216     |29484     |31752     |34020     |36288      |38556      |40824      |43092      |45360      |
|Damage per shot     |3400   |3440      |3480      |3520      |3560      |3600       |3640       |3680       |3720       |3760       |
|Damage*             |2125.0 |2150.0    |2175.0    |2200.0    |2225.0    |2250.0     |2275.0     |2300.0     |2325.0     |2350.0     |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Turret (50)**, **Shield (50)**, **Storage (50)**, **Other building (50)**, **Heavy vehicle (50)**, **Shield generator (50)**, **Ressource generator (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Support troop (50)**, **Droideka (50)**, **HQ (50)**, Wall (30), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 12
  * Clip retargeting: Yes
  * Target shield border: Yes
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                        |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|24 Con.                                  |35 Con.                                |70 Con.                                |125 Con.                               |150 Con.                               |200 Con.                               |275 Con.                               |400 Con.                               |550 Con.                               |900 Con.                                |
|Training time|8m30s                                    |9m30s                                  |10m                                    |11m                                    |11m30s                                 |12m30s                                 |13m                                    |13m30s                                 |14m30s                                 |15m                                     |
|Building     |[Cantina 7](empireContrabandCantina.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : Brute Cannon

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 0s
  * Time between shots: 1.040s
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 1

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |3400  |3440  |3480  |3520  |3560  |3600  |3640  |3680  |3720  |3760  |
|Calculated damage per second|6800  |6880  |6960  |7040  |7120  |7200  |7280  |7360  |7440  |7520  |
|Damage*                     |2125.0|2150.0|2175.0|2200.0|2225.0|2250.0|2275.0|2300.0|2325.0|2350.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 500ms
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
  * Shield: 50%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 0%
  * Turret: 125%
  * Light vehicle: 100%
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_brute_hit
  * projectilemuzzleFlash: fx_brute_muzzle
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: closest
  * audioDeath: "sfx_death_brute_01":50,"sfx_death_brute_02":50
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: 
  * decalSize: 160
  * eventButtonString: 
  * iconCloseupCameraPosition: 10.36,-0.8,9.14
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_brute_01":50,"sfx_ui_unitcomplete_brute_02":50
  * iconCameraPosition: 22.63,10.75,17.33
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: 
  * newRotationSpeed: 7854
  * bundleName: brute_con-ani
  * iconCloseupLookatPosition: -0.45,2.74,-0.6
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_brute_01":35,"sfx_attack_brute_02":35,"sfx_attack_brute_03":30
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 1.5
  * audioPlacement: "sfx_placement_brute_01":50,"sfx_placement_brute_02":50
  * audioImpact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * hologramUid: 
  * iconLookatPosition: -0.25,1.71,0.52
  * assetName: brute_con-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 460
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * armingDelay: 0
  * impactDelay: 0
  * projectilestreams: no
  * autoSpawnRateScale: 1
  * projectilebullet: fx_brute_projectile
  * spawnEffectUid: effectEmpireSpawn
  * strictCoolDown: true
  * targetInRangeModifier: 1

|Level     |1                |2                |3                |4                |5                |6                |7                |8                |9                |10                |
|----------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|
|pointValue|12.000           |14.000           |17.000           |19.000           |22.000           |24.000           |26.000           |29.000           |31.000           |36.000            |
|ability   |abilityBruteBomb1|abilityBruteBomb2|abilityBruteBomb3|abilityBruteBomb4|abilityBruteBomb5|abilityBruteBomb6|abilityBruteBomb7|abilityBruteBomb8|abilityBruteBomb9|abilityBruteBomb10|
|order     |115401           |115402           |115403           |115404           |115405           |115406           |115407           |115408           |115409           |115410            |

