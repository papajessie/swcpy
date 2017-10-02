---
title: T2-B Repulsor Tank (T2BTank)
category: unit
---

# T2-B Repulsor Tank (T2BTank) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: vehicle
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 7
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|700$ |3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s   |45m  |2h   |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Health              |15120|15990|16910|17890 |18930 |20040  |21230  |22490  |23830   |25260   |
|Damage per shot     |450  |490  |540  |590   |640   |700    |770    |850    |940     |1030    |
|Damage*             |630.0|690.0|760.0|830.0 |900.0 |980.0  |1260.0 |1390.0 |1530.0  |1680.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Turret (50)**, **Shield (50)**, **Storage (50)**, **Other building (50)**, **Heavy vehicle (50)**, **Shield generator (50)**, **Ressource generator (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Support troop (50)**, **Droideka (50)**, **HQ (50)**, Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 16
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|770$                          |800$                                  |830$                                  |870$                                  |910$                                  |1050$                                 |1190$                                 |1400$                                 |1470$                                 |1610$                                  |
|Training time|3m12s                         |3m13s                                 |3m15s                                 |3m17s                                 |3m19s                                 |3m22s                                 |3m25s                                 |3m28s                                 |3m32s                                 |3m36s                                  |
|Building     |[Factory 2](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : T2BTank

### Basic info

  * Shot count: 4
  * Time between start of clip and first shot: 250ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 2

|Level                       |1    |2    |3    |4    |5    |6    |7     |8     |9     |10    |
|----------------------------|-----|-----|-----|-----|-----|-----|------|------|------|------|
|Damage per shot             |450  |490  |540  |590  |640  |700  |770   |850   |940   |1030  |
|Calculated damage per second|734  |800  |881  |963  |1044 |1142 |1257  |1387  |1534  |1681  |
|Damage*                     |630.0|690.0|760.0|830.0|900.0|980.0|1260.0|1390.0|1530.0|1680.0|

### Secondary info

  * Gun shooting sequence: 1,1,2,2
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 2.450s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 2
  * Cannons shot per gun sequence: 4

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

  * projectilehitSpark: fx_blaster_hit_b_lrg
  * projectilemuzzleFlash: fx_blaster_flash_b_lrg
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 0.00,0.51,0
  * favoriteTargetType: closest
  * audioDeath: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * factoryScaleFactor: 1
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
  * iconCameraPosition: 22.79,25.75,28.69
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "t2btank_rbl_rig_MASTER_MOVER/t2btank_rbl_rig_locator_gun1":1,"t2btank_rbl_rig_MASTER_MOVER/t2btank_rbl_rig_locator_gun2":1,"t2btank_rbl_rig_MASTER_MOVER/t2btank_rbl_rig_locator_gun3":2,"t2btank_rbl_rig_MASTER_MOVER/t2btank_rbl_rig_locator_gun4":2
  * newRotationSpeed: 3927
  * bundleName: t2btank_rbl-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_tank_1":25,"sfx_attack_tank_2":25,"sfx_attack_tank_3":25,"sfx_attack_tank_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.25,0.58,-0.36
  * assetName: t2btank_rbl-ani
  * rotationSpeed: 3.92698750000000007531752999057061970233917236328125
  * animationDelay: 100
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
  * projectilebullet: fx_blaster_beam_b_lrg

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|7.000 |8.400 |9.800 |11.200|12.600|14.000|15.400|16.800|18.200|21.000|
|order     |230201|230202|230203|230204|230205|230206|230207|230208|230209|230210|

