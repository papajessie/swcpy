---
title: Shoretrooper (PentagonTrooper)
category: unit
---

# Shoretrooper (PentagonTrooper) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: No
  * Type: infantry
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|600$  |1500$ |4000$ |12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s    |15m   |1h    |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |2925  |3500  |3775  |4325  |4850  |5400   |5950   |6475   |7025    |8100    |
|Damage per shot     |320   |380   |410   |470   |530   |590    |640    |700    |760     |880     |
|Damage*             |1208.0|1448.0|1560.0|1780.0|2004.0|2228.0 |2448.0 |2672.0 |2896.0  |3340.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Turret (50)**, **Shield (50)**, **Storage (50)**, **Other building (50)**, **Heavy vehicle (50)**, **Shield generator (50)**, **Ressource generator (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Support troop (50)**, **Droideka (50)**, **HQ (50)**, Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|50$                              |70$                                    |90$                                    |110$                                   |130$                                   |150$                                   |170$                                   |200$                                   |210$                                   |230$                                    |
|Training time|20s                              |22s                                    |23s                                    |24s                                    |25s                                    |26s                                    |27s                                    |28s                                    |29s                                    |30s                                     |
|Building     |[Barracks 1](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : Storm

### Basic info

  * Shot count: 5
  * Time between start of clip and first shot: 500ms
  * Time between shots: 100ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 5

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |320   |380   |410   |470   |530   |590   |640   |700   |760   |880   |
|Calculated damage per second|1142  |1357  |1464  |1678  |1892  |2107  |2285  |2500  |2714  |3142  |
|Damage*                     |1208.0|1448.0|1560.0|1780.0|2004.0|2228.0|2448.0|2672.0|2896.0|3340.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 5
  * Number of cannons: 0
  * Clips period: 1.400s
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

  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilemuzzleFlash: fx_blaster_flash_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: closest
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 1.93,1.69,9.65
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * iconCameraPosition: 12.13,10.63,15.32
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: 
  * newRotationSpeed: 7854
  * bundleName: pentagontrooper_emp-ani
  * iconCloseupLookatPosition: -0.01,2.73,-0.82
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: 0.02,1.69,0
  * assetName: pentagontrooper_emp-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * autoSpawnRateScale: 1
  * decalAssetName: troop_stotrper_emp
  * pointValue: 1.000
  * armingDelay: 0
  * impactDelay: 1000
  * projectilestreams: no
  * decalBundleName: troop_stotrper_emp
  * maxScale: false
  * projectilebullet: fx_blaster_beam_r_sm
  * strictCoolDown: false
  * targetInRangeModifier: 1

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|order|300040|300041|300042|300043|300044|300045|300046|300047|300048|300049|

