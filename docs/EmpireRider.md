---
title: Luggabeast Munitioneer (EmpireRider)
category: unit
---

# Luggabeast Munitioneer (EmpireRider) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: mercenary
  * Armor type: healerInfantry
  * Role: Healer
  * Levels available: 1-10
  * Unit capacity: 7
  * Damage per shot: 0
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1      |2        |3         |4         |5         |6          |7          |8          |9          |10         |
|--------------------|-------|---------|----------|----------|----------|-----------|-----------|-----------|-----------|-----------|
|Upgrade requirements|Nothing|7000 Con.|15000 Con.|30000 Con.|58000 Con.|110000 Con.|140000 Con.|160000 Con.|165000 Con.|168000 Con.|
|Upgrade time        |0s     |4d       |5d        |6d        |1w        |1w1d       |1w2d       |1w3d       |1w4d       |1w5d       |
|Health              |13000  |15600    |16800     |19200     |21600     |24000      |26400      |28800      |31200      |36000      |
|Damage*             |12.0   |14.0     |16.0      |18.0      |20.0      |22.0       |24.0       |26.0       |28.0       |30.0       |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry hero (50)**, **Heavy vehicular hero (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Heavy infantry hero (50)**, **Vehicle hero (50)**, **Droideka (50)**, Wall (0), Turret (0), Shield (0), Storage (0), Other building (0), Shield generator (0), Trap (0), Ressource generator (0), Support troop (0), HQ (0)
  * Targeted type: ALLIES
  * View Range: 5
  * Target preferences strength: 1
  * Retargeting offset: 15
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: Yes
  * Self-centered targeting: Yes

## Recruiting

|Level        |1                                        |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|10 Con.                                  |20 Con.                                |40 Con.                                |75 Con.                                |85 Con.                                |125 Con.                               |170 Con.                               |230 Con.                               |310 Con.                               |525 Con.                                |
|Training time|5m                                       |5m30s                                  |6m                                     |6m30s                                  |7m                                     |7m30s                                  |8m                                     |8m30s                                  |9m                                     |9m30s                                   |
|Building     |[Cantina 5](empireContrabandCantina.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: Yes
  * Propensity to go around obstacles: 15

## Attack : Rider Buff

### Basic info

  * Damage per shot: 0
  * Shot count: 1
  * Time between start of clip and first shot: 0s
  * Time between shots: 0s
  * Time between last shot and reload: 0s
  * Time between two clips: 5s
  * Salvos per clip: 1
  * Calculated damage per second: 0

|Level  |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|-------|----|----|----|----|----|----|----|----|----|----|
|Damage*|12.0|14.0|16.0|18.0|20.0|22.0|24.0|26.0|28.0|30.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 5s
  * Projectile passes through shields: Yes
  * Projectile deflectable: No
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 0%
  * Heavy infantry: 0%
  * Heavy vehicle: 0%
  * Other building: 0%
  * Droideka: 0%
  * Flying infantry: 0%
  * Flying vehicle: 0%
  * Support troop: 0%
  * Heavy infantry hero: 0%
  * Heavy vehicular hero: 0%
  * Infantry hero: 0%
  * Vehicle hero: 0%
  * Infantry: 0%
  * Ressource generator: 0%
  * Shield: 0%
  * Shield generator: 0%
  * Storage: 0%
  * Trap: 0%
  * Turret: 0%
  * Light vehicle: 0%
  * Wall: 0%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: 
  * projectilemuzzleFlash: fx_rider_buff
  * projectilemaxScale: 200
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: closest
  * audioDeath: "sfx_death_rider_01":50,"sfx_death_rider_02":50
  * factoryScaleFactor: 1
  * infoUIType: DamageBuff
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: 
  * decalSize: 160
  * eventButtonString: 
  * iconCloseupCameraPosition: 
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_rider_01":50,"sfx_ui_unitcomplete_rider_02":50
  * iconCameraPosition: 23.58,31.88,32.8
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: 
  * newRotationSpeed: 7854
  * bundleName: rider_con-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: 
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 1.5
  * audioPlacement: "sfx_placement_rider_01":50,"sfx_placement_rider_02":50
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.52,2.15,-1.3
  * assetName: rider_con-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * deathProjectileDelay: 0
  * impactDelay: 0
  * projectilestreams: no
  * autoSpawnRateScale: 1
  * strictCoolDown: false
  * supportFollowDistance: 4
  * armingDelay: 0
  * targetInRangeModifier: 1
  * deathProjectileDistance: 0
  * deathProjectileDamage: 0
  * spawnEffectUid: effectRebelSpawn

|Level               |1                     |2                     |3                     |4                     |5                     |6                     |7                     |8                     |9                     |10                     |
|--------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|-----------------------|
|pointValue          |7.000                 |8.000                 |10.000                |11.000                |13.000                |14.000                |15.000                |17.000                |18.000                |21.000                 |
|projectileapplyBuffs|buffUnitDamageSteroid1|buffUnitDamageSteroid2|buffUnitDamageSteroid3|buffUnitDamageSteroid4|buffUnitDamageSteroid5|buffUnitDamageSteroid6|buffUnitDamageSteroid7|buffUnitDamageSteroid8|buffUnitDamageSteroid9|buffUnitDamageSteroid10|
|deathProjectile     |projectileRiderBuff1  |projectileRiderBuff2  |projectileRiderBuff3  |projectileRiderBuff4  |projectileRiderBuff5  |projectileRiderBuff6  |projectileRiderBuff7  |projectileRiderBuff8  |projectileRiderBuff9  |projectileRiderBuff10  |
|order               |115301                |115302                |115303                |115304                |115305                |115306                |115307                |115308                |115309                |115310                 |

