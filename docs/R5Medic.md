---
title: Imperial Astromedic (R5Medic)
category: unit
---

# Imperial Astromedic (R5Medic) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: healerInfantry
  * Role: Healer
  * Levels available: 1-10
  * Unit capacity: 5
  * Upgrade requirements: 32 data fragments
  * Upgrade time: 5s
  * Damage per shot: 0
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level  |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-------|------|------|------|------|------|------|------|------|------|------|
|Health |11700 |12400 |13100 |13900 |14600 |15300 |16000 |16800 |18100 |19500 |
|Damage*|1550.0|1710.0|1810.0|1910.0|2010.0|2110.0|2210.0|2310.0|2490.0|2690.0|

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Heavy infantry (50)**, **Infantry hero (50)**, **Infantry (50)**, **Heavy infantry hero (50)**, Flying infantry (0), Droideka (0), Support troop (0), Other building (0), Vehicle hero (0), HQ (0), Trap (0), Shield (0), Heavy vehicle (0), Heavy vehicular hero (0), Storage (0), Shield generator (0), Light vehicle (0), Turret (0), Wall (0), Ressource generator (0), Flying vehicle (0)
  * Targeted type: ALLIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 10
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: Yes

## Recruiting

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|250$                             |350$                                   |450$                                   |550$                                   |650$                                   |750$                                   |850$                                   |1000$                                  |1050$                                  |1150$                                   |
|Training time|1m40s                            |1m50s                                  |1m55s                                  |2m                                     |2m5s                                   |2m10s                                  |2m15s                                  |2m20s                                  |2m25s                                  |2m30s                                   |
|Building     |[Barracks 2](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: Yes
  * Propensity to go around obstacles: 15

## Attack : Medic

### Basic info

  * Damage per shot: 0
  * Shot count: 2
  * Time between start of clip and first shot: 50ms
  * Time between shots: 400ms
  * Time between last shot and reload: 0s
  * Time between two clips: 900ms
  * Salvos per clip: 2
  * Calculated damage per second: 0
  * Max. Range: 5
  * Min. Range: 0

|Level  |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-------|------|------|------|------|------|------|------|------|------|------|
|Damage*|1550.0|1710.0|1810.0|1910.0|2010.0|2110.0|2210.0|2310.0|2490.0|2690.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 1.350s
  * Projectile passes through shields: No
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

  * projectilearcs: false
  * projectilemaxScale: 200
  * projectilehitSpark: 
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_healing_ring

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_droid_r5_01":50,"sfx_placement_droid_r5_02":50
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: fragment_obtain_gen
  * shieldAssetName: 
  * audioAttack: "sfx_attack_droid_medic_1":50,"sfx_attack_droid_medic_2":50
  * decalSize: 
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 
  * eventButtonString: hn_open_galaxy
  * gunPosition: 
  * infoUIType: Healer
  * bundleName: r5droid_emp-ani
  * deathAnimation: 
  * favoriteTargetType: infantry
  * eventButtonData: planet1 planet3 planet6 planet8 planet21 planet23
  * audioDeath: "sfx_death_droid_r5_01":50,"sfx_death_droid_r5_02":50
  * unlockPlanet: 
  * upgradeShardUid: shrd_troopR5Medic
  * iconCameraPosition: 5.21,9.06,13.12
  * eventButtonAction: galaxy
  * factoryRotation: 0
  * buffAssetOffset: 
  * iconCloseupCameraPosition: 
  * hologramUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: 
  * assetName: r5droid_emp-ani
  * unlockedByEvent: true
  * iconLookatPosition: -0.19,0.88,-0.37
  * factoryScaleFactor: 1
  * audioTrain: "sfx_ui_unitcomplete_r5droid_01":50,"sfx_ui_unitcomplete_r5droid_02":50

|Level             |1    |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------------------|-----|--|--|--|--|--|--|--|--|--|
|iconUnlockRotation|0,0,0|  |  |  |  |  |  |  |  |  |
|iconUnlockScale   |1,1,1|  |  |  |  |  |  |  |  |  |
|iconUnlockPosition|0,0,0|  |  |  |  |  |  |  |  |  |

## Uninterpreted stats

  * impactDelay: 250
  * maxScale: false
  * projectilestreams: no
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * strictCoolDown: false
  * supportFollowDistance: 5
  * autoSpawnSpreadingScale: 1
  * targetInRangeModifier: 1

|Level               |1           |2           |3           |4           |5           |6           |7           |8           |9           |10           |
|--------------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|-------------|
|pointValue          |5.000       |6.000       |7.000       |8.000       |9.000       |10.000      |11.000      |12.000      |13.000      |15.000       |
|projectileapplyBuffs|buffAdvHeal1|buffAdvHeal2|buffAdvHeal3|buffAdvHeal4|buffAdvHeal5|buffAdvHeal6|buffAdvHeal7|buffAdvHeal8|buffAdvHeal9|buffAdvHeal10|
|order               |134401      |134402      |134403      |134404      |134405      |134406      |134407      |134408      |134409      |134410       |

