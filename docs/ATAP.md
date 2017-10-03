---
title: AT-AP Walker (ATAP)
category: unit
---

# AT-AP Walker (ATAP) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: vehicle
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 10
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|6500$ |3000$ |6000$ |15000$|35000$|115000$|200000$|385000$|1250000$|2250000$|
|Upgrade time        |0s    |1h    |2h30m |7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Health              |7200  |7610  |8050  |8510  |9000  |9530   |10090  |10680  |11320   |12000   |
|Damage per shot     |1540  |1630  |1720  |1820  |1920  |2040   |2160   |2280   |2420    |2570    |
|Damage*             |2160.0|2290.0|2410.0|2550.0|2690.0|2860.0 |3030.0 |3200.0 |3400.0  |3610.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Shield (70)**, **Shield generator (70)**, Heavy infantry (50), Flying infantry (50), Droideka (50), Support troop (50), Infantry (50), Other building (50), HQ (50), Heavy vehicle (50), Storage (50), Light vehicle (50), Turret (50), Ressource generator (50), Flying vehicle (50), Infantry hero (1), Vehicle hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 16
  * Clip retargeting: No
  * Target shield border: Yes
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|1100$                         |1150$                                 |1200$                                 |1250$                                 |1300$                                 |1500$                                 |1700$                                 |2000$                                 |2100$                                 |2300$                                  |
|Training time|4m                            |4m2s                                  |4m4s                                  |4m7s                                  |4m10s                                 |4m20s                                 |4m30s                                 |4m40s                                 |4m50s                                 |5m                                     |
|Building     |[Factory 4](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : ATAP

### Basic info

  * Shot count: 4
  * Time between start of clip and first shot: 250ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 4
  * Max. Range: 8
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |1540  |1630  |1720  |1820  |1920  |2040  |2160  |2280  |2420  |2570  |
|Calculated damage per second|2161  |2287  |2414  |2554  |2694  |2863  |3031  |3200  |3396  |3607  |
|Damage*                     |2160.0|2290.0|2410.0|2550.0|2690.0|2860.0|3030.0|3200.0|3400.0|3610.0|

### Secondary info

  * Gun shooting sequence: 1,2
  * Salvos per clip: 4
  * Number of cannons: 0
  * Clips period: 2.850s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 12
  * Projectile is directional: Yes
  * Salvos per gun sequence: 2
  * Cannons shot per gun sequence: 2

### Multipliers

  * HQ: 75%
  * Heavy infantry: 100%
  * Heavy vehicle: 100%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 200%
  * Heavy vehicular hero: 200%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 75%
  * Shield: 400%
  * Shield generator: 400%
  * Storage: 75%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 100%
  * Wall: 60%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_b_sm

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * shieldAssetName: 
  * audioAttack: "sfx_attack_rebel_atap_1":30,"sfx_attack_rebel_atap_2":35,"sfx_attack_rebel_atap_3":35
  * decalSize: 
  * newRotationSpeed: 3927
  * tooltipHeightOffset: 
  * eventButtonString: 
  * gunPosition: "atap_rbl_rig_locator_gun1":1,"atap_rbl_rig_locator_gun2":2
  * infoUIType: 
  * bundleName: atap_rbl-ani
  * deathAnimation: 
  * favoriteTargetType: shieldGenerator
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_rebel_atap_1":100
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * iconCameraPosition: 20.98,26.07,34.08
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 0.00,1.94,0.00
  * iconCloseupCameraPosition: 
  * hologramUid: 
  * rotationSpeed: 3.92698750000000007531752999057061970233917236328125
  * iconCloseupLookatPosition: 
  * assetName: atap_rbl-ani
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * iconLookatPosition: -0.59,2.38,-0.99
  * factoryScaleFactor: 0.85199999999999997957189634689711965620517730712890625
  * audioTrain: 

## Uninterpreted stats

  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 2
  * autoSpawnSpreadingScale: 2
  * impactDelay: 1000
  * projectilebullet: fx_blaster_beam_b_sm
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|order     |230401|230402|230403|230404|230405|230406|230407|230408|230409|230410|
|pointValue|10.000|12.000|14.000|16.000|18.000|20.000|22.000|24.000|26.000|30.000|

