---
title: Rebel Hailfire Droid (Hailfire)
category: unit
---

# Rebel Hailfire Droid (Hailfire) — version 1085

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

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|700$ |3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s   |45m  |2h   |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Health              |2800 |3360 |3920 |4480  |5040  |5600   |6160   |6720   |7280    |8400    |
|Damage per shot     |368  |441  |515  |588   |662   |735    |809    |882    |956     |1103    |
|Damage*             |630.0|756.0|882.0|1008.0|1134.0|1260.0 |1386.0 |1512.0 |1638.0  |1890.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (70)**, _Flying infantry (60)_, _Light vehicle (60)_, _Heavy infantry (60)_, _Heavy vehicle (60)_, _Infantry hero (60)_, _Heavy vehicular hero (60)_, _Infantry (60)_, _Flying vehicle (60)_, _Heavy infantry hero (60)_, _Vehicle hero (60)_, _Support troop (60)_, _Droideka (60)_, Shield (50), Storage (50), Other building (50), Shield generator (50), Ressource generator (50), HQ (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|350$                          |490$                                  |630$                                  |770$                                  |910$                                  |1050$                                 |1190$                                 |1400$                                 |1470$                                 |1610$                                  |
|Training time|2m48s                         |2m56s                                 |3m4s                                  |3m12s                                 |3m20s                                 |3m28s                                 |3m36s                                 |3m16s                                 |3m23s                                 |3m30s                                  |
|Building     |[Factory 7](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x2
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : projectileHailfire

### Basic info

  * Shot count: 6
  * Time between start of clip and first shot: 1s
  * Time between shots: 100ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 6

|Level                       |1    |2    |3    |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|-----|-----|-----|------|------|------|------|------|------|------|
|Damage per shot             |368  |441  |515  |588   |662   |735   |809   |882   |956   |1103  |
|Calculated damage per second|630  |756  |882  |1008  |1134  |1260  |1386  |1512  |1638  |1890  |
|Damage*                     |630.0|756.0|882.0|1008.0|1134.0|1260.0|1386.0|1512.0|1638.0|1890.0|

### Secondary info

  * Gun shooting sequence: 1,2
  * Salvos per clip: 6
  * Number of cannons: 0
  * Clips period: 3.500s
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 12
  * Projectile is directional: No
  * Salvos per gun sequence: 2
  * Cannons shot per gun sequence: 2

### Multipliers

  * HQ: 25%
  * Heavy infantry: 50%
  * Heavy vehicle: 250%
  * Other building: 25%
  * Droideka: 100%
  * Flying infantry: 50%
  * Flying vehicle: 300%
  * Support troop: 50%
  * Heavy infantry hero: 50%
  * Heavy vehicular hero: 250%
  * Infantry hero: 50%
  * Vehicle hero: 300%
  * Infantry: 50%
  * Ressource generator: 25%
  * Shield: 25%
  * Shield generator: 25%
  * Storage: 25%
  * Trap: 200%
  * Turret: 200%
  * Light vehicle: 300%
  * Wall: 80%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_rocket_hit_b_sm
  * projectilemuzzleFlash: fx_rocket_muzzle_b_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 0.00,0.88,0.00
  * favoriteTargetType: turret
  * audioDeath: "sfx_death_rebel_hailfire_1":100
  * factoryScaleFactor: 0.71499999999999996891375531049561686813831329345703125
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
  * iconCameraPosition: 36.69,22.39,29.86
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "hailfiredroid_rbl_rig_locator_gun1":1,"hailfiredroid_rbl_rig_locator_gun2":2
  * newRotationSpeed: 7854
  * bundleName: hailfiredroid_rbl-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_rebel_hailfire_1":35,"sfx_attack_rebel_hailfire_2":35,"sfx_attack_rebel_hailfire_3":30
  * eventButtonAction: 
  * factoryRotation: 90
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * audioImpact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * hologramUid: 
  * iconLookatPosition: -0.49,1.9,-0.43
  * assetName: hailfiredroid_rbl-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 2
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 1000
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 2
  * projectilebullet: fx_rocket_projectile_b_sm

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|7.000 |8.400 |9.800 |11.200|12.600|14.000|15.400|16.800|18.200|21.000|
|order     |230701|230702|230703|230704|230705|230706|230707|230708|230709|230710|

