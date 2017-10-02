---
title: Jetpack Trooper (RebelJetpackTrooper)
category: unit
---

# Jetpack Trooper (RebelJetpackTrooper) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: flierInfantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 7
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|600$ |1500$|4000$|12500$|25000$|100000$|160000$|320000$|1000000$|2000000$|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w3d    |
|Health              |5600 |6720 |7840 |8960  |10080 |11200  |12320  |13440  |14560   |16800   |
|Damage per shot     |700  |840  |980  |1120  |1260  |1400   |1540   |1680   |1820    |2100    |
|Damage*             |560.0|672.0|784.0|896.0 |1008.0|1120.0 |1232.0 |1344.0 |1456.0  |1680.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Turret (50)**, **Shield (50)**, **Storage (50)**, **Other building (50)**, **Heavy vehicle (50)**, **Infantry hero (50)**, **Shield generator (50)**, **Ressource generator (50)**, **Heavy vehicular hero (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Heavy infantry hero (50)**, **Vehicle hero (50)**, **Support troop (50)**, **Droideka (50)**, **HQ (50)**, Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: Yes
  * Self-centered targeting: No

## Recruiting

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|385$                            |539$                                  |693$                                  |847$                                  |1001$                                 |1155$                                 |1309$                                 |1540$                                 |1617$                                 |1771$                                  |
|Training time|2m20s                           |2m34s                                 |2m41s                                 |2m48s                                 |2m55s                                 |3m2s                                  |3m9s                                  |3m16s                                 |3m23s                                 |3m30s                                  |
|Building     |[Barracks 8](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 40
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: Yes
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : Rebel Jumptrooper Blaster

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 250ms
  * Time between shots: 750ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1.500s
  * Salvos per clip: 1

|Level                       |1    |2    |3    |4    |5     |6     |7     |8     |9     |10    |
|----------------------------|-----|-----|-----|-----|------|------|------|------|------|------|
|Damage per shot             |700  |840  |980  |1120 |1260  |1400  |1540  |1680  |1820  |2100  |
|Calculated damage per second|800  |960  |1120 |1280 |1440  |1600  |1760  |1920  |2080  |2400  |
|Damage*                     |560.0|672.0|784.0|896.0|1008.0|1120.0|1232.0|1344.0|1456.0|1680.0|

### Secondary info

  * Gun shooting sequence: 1,1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 1.750s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 15
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 2

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
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilemuzzleFlash: fx_blaster_flash_b_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: closest
  * audioDeath: "sfx_death_jumptrooper_1":35,"sfx_death_jumptrooper_2":35,"sfx_death_jumptrooper_3":30
  * factoryScaleFactor: 
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 0.9,3.32,13.24
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * iconCameraPosition: 11.88,12.47,16.37
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "hoversoldier_rbl_rig_MASTER_MOVER/hoversoldier_rbl_rig_locator_gun1":1,"hoversoldier_rbl_rig_MASTER_MOVER/hoversoldier_rbl_rig_locator_gun2":1
  * newRotationSpeed: 7854
  * bundleName: hoversoldier_rbl-ani
  * iconCloseupLookatPosition: 0.08,5.11,0.16
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * eventButtonAction: 
  * factoryRotation: 
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_jettrooper_1":35,"sfx_placement_jettrooper_2":35,"sfx_placement_jettrooper_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.05,4.6,-0.18
  * assetName: hoversoldier_rbl-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 1000
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * projectilebullet: fx_blaster_beam_b_sm

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|7.000 |8.400 |9.800 |11.200|12.600|14.000|15.400|16.800|18.200|21.000|
|order     |221101|221102|221103|221104|221105|221106|221107|221108|221109|221110|

