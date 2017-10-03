---
title: Jump Trooper (EmpireJumptrooper)
category: unit
---

# Jump Trooper (EmpireJumptrooper) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
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
|Damage per shot     |1204 |1445 |1686 |1927  |2168  |2408   |2649   |2890   |3131    |3612    |
|Damage*             |560.0|672.0|784.0|896.0 |1008.0|1120.0 |1232.0 |1344.0 |1456.0  |1680.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Heavy infantry (50)**, **Infantry hero (50)**, **Flying infantry (50)**, **Droideka (50)**, **Support troop (50)**, **Infantry (50)**, **Other building (50)**, **Vehicle hero (50)**, **HQ (50)**, **Shield (50)**, **Heavy vehicle (50)**, **Heavy vehicular hero (50)**, **Storage (50)**, **Heavy infantry hero (50)**, **Shield generator (50)**, **Light vehicle (50)**, **Turret (50)**, **Ressource generator (50)**, **Flying vehicle (50)**, Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: Yes
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|385$                             |539$                                   |693$                                   |847$                                   |1001$                                  |1155$                                  |1309$                                  |1540$                                  |1617$                                  |1771$                                   |
|Training time|2m20s                            |2m34s                                  |2m41s                                  |2m48s                                  |2m55s                                  |3m2s                                   |3m9s                                   |3m16s                                  |3m23s                                  |3m30s                                   |
|Building     |[Barracks 8](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : Empire Jumptrooper Blaster

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 150ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 1
  * Max. Range: 7
  * Min. Range: 0

|Level                       |1    |2    |3    |4    |5     |6     |7     |8     |9     |10    |
|----------------------------|-----|-----|-----|-----|------|------|------|------|------|------|
|Damage per shot             |1204 |1445 |1686 |1927 |2168  |2408  |2649  |2890  |3131  |3612  |
|Calculated damage per second|560  |672  |784  |896  |1008  |1120  |1232  |1344  |1456  |1680  |
|Damage*                     |560.0|672.0|784.0|896.0|1008.0|1120.0|1232.0|1344.0|1456.0|1680.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 2.150s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 15
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
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_r_sm

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_jettrooper_1":35,"sfx_placement_jettrooper_2":35,"sfx_placement_jettrooper_3":30
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * shieldAssetName: 
  * audioAttack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * decalSize: 
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 
  * eventButtonString: 
  * gunPosition: "jumptrooper_emp_rig_MASTER_MOVER/jumptrooper_emp_rig_locator_gun_Rt":1
  * infoUIType: 
  * bundleName: jumptrooper_emp-ani
  * deathAnimation: 
  * favoriteTargetType: closest
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_jumptrooper_1":35,"sfx_death_jumptrooper_2":35,"sfx_death_jumptrooper_3":30
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * iconCameraPosition: 8.7,15.21,13.03
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 0.0,0.3,0.0
  * iconCloseupCameraPosition: 2.26,2.95,10.77
  * hologramUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: 0.13,5.28,0.42
  * assetName: jumptrooper_emp-ani
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * iconLookatPosition: 0.12,4.78,0.33
  * factoryScaleFactor: 1
  * audioTrain: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30

## Uninterpreted stats

  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 1
  * autoSpawnSpreadingScale: 1
  * impactDelay: 1000
  * projectilebullet: fx_blaster_beam_r_sm
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|order     |121101|121102|121103|121104|121105|121106|121107|121108|121109|121110|
|pointValue|7.000 |8.400 |9.800 |11.200|12.600|14.000|15.400|16.800|18.200|21.000|

