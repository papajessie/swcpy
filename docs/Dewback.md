---
title: Dewback Trooper (Dewback)
category: unit
---

# Dewback Trooper (Dewback) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: infantry
  * Role: Breacher
  * Levels available: 1-10
  * Unit capacity: 3
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1       |2       |3       |4       |5       |6       |7              |8              |9              |10             |
|--------------------|--------|--------|--------|--------|--------|--------|---------------|---------------|---------------|---------------|
|Armor type          |infantry|infantry|infantry|infantry|infantry|infantry|bruiserInfantry|bruiserInfantry|bruiserInfantry|bruiserInfantry|
|Upgrade requirements|5000$   |7000$   |9000$   |12500$  |25000$  |100000$ |160000$        |320000$        |1000000$       |1750000$       |
|Upgrade time        |0s      |15m     |1h      |3h30m   |8h      |1d      |2d             |3d12h          |5d             |1w1d           |
|Health              |10800   |11420   |12080   |12780   |13520   |14320   |15160          |16070          |17030          |18050          |
|Damage per shot     |950     |1000    |1060    |1120    |1190    |1260    |1330           |1410           |1490           |1580           |
|Damage*             |1360.0  |1430.0  |1510.0  |1600.0  |1700.0  |1800.0  |1900.0         |2010.0         |2130.0         |2260.0         |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (70)**, Light vehicle (50), Heavy infantry (50), Shield (50), Storage (50), Other building (50), Heavy vehicle (50), Shield generator (50), Ressource generator (50), Infantry (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Flying infantry (0), Trap (0), Flying vehicle (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 4
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|330$                             |340$                                   |350$                                   |370$                                   |390$                                   |450$                                   |510$                                   |600$                                   |630$                                   |690$                                    |
|Training time|45s                              |46s                                    |47s                                    |48s                                    |50s                                    |52s                                    |54s                                    |1m24s                                  |1m27s                                  |1m30s                                   |
|Building     |[Barracks 4](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 200

## Attack : Dewback

### Basic info

  * Shot count: 5
  * Time between start of clip and first shot: 500ms
  * Time between shots: 750ms
  * Time between last shot and reload: 0s
  * Time between two clips: 0s
  * Salvos per clip: 5

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |950   |1000  |1060  |1120  |1190  |1260  |1330  |1410  |1490  |1580  |
|Calculated damage per second|1357  |1428  |1514  |1600  |1700  |1800  |1900  |2014  |2128  |2257  |
|Damage*                     |1360.0|1430.0|1510.0|1600.0|1700.0|1800.0|1900.0|2010.0|2130.0|2260.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 5
  * Number of cannons: 0
  * Clips period: 3.500s
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 20%
  * Heavy vehicle: 20%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 0%
  * Flying vehicle: 0%
  * Support troop: 20%
  * Heavy infantry hero: 20%
  * Heavy vehicular hero: 20%
  * Infantry hero: 20%
  * Vehicle hero: 20%
  * Infantry: 20%
  * Ressource generator: 100%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 0%
  * Turret: 100%
  * Light vehicle: 20%

|Level|1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|-----|----|----|----|----|----|----|----|----|----|----|
|Wall |560%|670%|760%|950%|940%|930%|900%|880%|840%|760%|

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: 
  * projectilemuzzleFlash: fx_melee_headbutt_lrg
  * projectilemaxScale: 300
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 0.00,1.01,0.00
  * favoriteTargetType: turret
  * audioDeath: "sfx_death_creatures_dewback_1":25,"sfx_death_creatures_dewback_2":25,"sfx_death_creatures_dewback_3":25,"sfx_death_creatures_dewback_4":25
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_dewback_1":35,"sfx_ui_unitcomplete_dewback_2":35,"sfx_ui_unitcomplete_dewback_3":30
  * iconCameraPosition: 17.06,13.27,18.62
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * newRotationSpeed: 7854
  * bundleName: dewback_emp-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_creatures_dewback_1":35,"sfx_attack_creatures_dewback_2":35,"sfx_attack_creatures_dewback_3":30
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_creatures_dewback_1":35,"sfx_placement_creatures_dewback_2":35,"sfx_placement_creatures_dewback_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.75,1.05,-0.6
  * assetName: dewback_emp-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 1000
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 0
  * projectilestreams: no
  * strictCoolDown: false
  * autoSpawnRateScale: 1
  * armingDelay: 0

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|3.000 |3.600 |4.200 |4.800 |5.400 |6.000 |6.600 |7.200 |7.800 |9.000 |
|order     |120401|120402|120403|120404|120405|120406|120407|120408|120409|120410|

