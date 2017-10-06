---
title: Probe Droid (ProbeDroid)
category: unit
---

# Probe Droid (ProbeDroid) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: vehicle
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 4
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|3000$ |3000$ |6000$ |12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s    |15m   |1h    |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w2d    |
|Health              |4800  |5020  |5250  |5500  |5750  |6020   |6310   |6610   |6920    |7250    |
|Damage per shot     |490   |510   |540   |560   |590   |610    |640    |670    |710     |740     |
|Damage*             |1120.0|1170.0|1230.0|1280.0|1350.0|1390.0 |1460.0 |1530.0 |1620.0  |1690.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Light vehicle (60)**, **Flying infantry (60)**, **Infantry (60)**, **Droideka (60)**, **Flying vehicle (60)**, **Support troop (60)**, **Heavy vehicle (60)**, **Heavy infantry (60)**, Storage (50), HQ (50), Other building (50), Turret (50), Shield (50), Ressource generator (50), Shield generator (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|600$                           |610$                                   |620$                                   |630$                                   |640$                                   |660$                                   |680$                                   |800$                                   |840$                                   |920$                                    |
|Training time|1m42s                          |1m43s                                  |1m44s                                  |1m45s                                  |1m46s                                  |1m47s                                  |1m48s                                  |1m52s                                  |1m56s                                  |2m                                      |
|Building     |[Factory 6](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 40
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : ProbeDroid

### Basic info

  * Shot count: 4
  * Time between start of clip and first shot: 500ms
  * Time between shots: 250ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 4
  * Max. Range: 7
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |490   |510   |540   |560   |590   |610   |640   |670   |710   |740   |
|Calculated damage per second|1120  |1165  |1234  |1280  |1348  |1394  |1462  |1531  |1622  |1691  |
|Damage*                     |1120.0|1170.0|1230.0|1280.0|1350.0|1390.0|1460.0|1530.0|1620.0|1690.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 4
  * Number of cannons: 0
  * Clips period: 1.750s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 15
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 75%
  * Heavy infantry: 200%
  * Heavy vehicle: 125%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 400%
  * Flying vehicle: 150%
  * Support troop: 400%
  * Heavy infantry hero: 200%
  * Heavy vehicular hero: 125%
  * Infantry hero: 400%
  * Vehicle hero: 150%
  * Infantry: 400%
  * Ressource generator: 75%
  * Shield: 75%
  * Shield generator: 75%
  * Storage: 75%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 150%
  * Wall: 75%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilemuzzleFlash: fx_blaster_flash_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: infantry
  * buffAssetOffset: 0.00,2,0.00
  * eventButtonAction: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * iconCameraPosition: -18.83,17.64,22.74
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_empire_probedroid_1":50,"sfx_death_empire_probedroid_2":50
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_empire_probedroid_1":100
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: 
  * iconLookatPosition: 0.53,3.67,-0.56
  * iconUnlockScale: 
  * bundleName: viperprobedroid_emp-ani
  * assetName: viperprobedroid_emp-ani
  * audioTrain: "sfx_ui_unitcomplete_probedroid_1":100
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_empire_probedroid_1":30,"sfx_attack_empire_probedroid_2":35,"sfx_attack_empire_probedroid_3":35
  * iconCloseupLookatPosition: 
  * upgradeShardUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * projectilestreams: no
  * maxScale: false
  * strictCoolDown: false
  * targetInRangeModifier: 1
  * armingDelay: 0
  * projectilebullet: fx_blaster_beam_r_sm
  * autoSpawnRateScale: 1
  * impactDelay: 500

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|4.000 |4.800 |5.600 |6.400 |7.200 |8.000 |8.800 |9.600 |10.400|12.000|
|order     |130601|130602|130603|130604|130605|130606|130607|130608|130609|130610|

