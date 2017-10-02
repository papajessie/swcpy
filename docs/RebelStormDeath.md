---
title: Undead Trooper (RebelStormDeath)
category: unit
---

# Undead Trooper (RebelStormDeath) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: No
  * Type: infantry
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|600$ |1500$|4000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |1300 |1560 |1680 |1920  |2160  |2400   |2640   |2880   |3120    |3600    |
|Damage per shot     |141  |169  |182  |208   |234   |260    |286    |312    |338     |390     |
|Damage*             |141.0|169.0|182.0|208.0 |234.0 |260.0  |286.0  |312.0  |338.0   |390.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Turret (50)**, **Shield (50)**, **Storage (50)**, **Other building (50)**, **Heavy vehicle (50)**, **Infantry hero (50)**, **Shield generator (50)**, **Ressource generator (50)**, **Heavy vehicular hero (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Heavy infantry hero (50)**, **Vehicle hero (50)**, **Support troop (50)**, **Droideka (50)**, **HQ (50)**, Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|---------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|50$                              |70$                                   |90$                                   |110$                                  |130$                                  |150$                                  |170$                                  |190$                                  |210$                                  |230$                                   |
|Training time|20s                              |22s                                   |23s                                   |24s                                   |25s                                   |26s                                   |27s                                   |28s                                   |29s                                   |30s                                    |
|Building     |[Barracks 10](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 1

## Attack : StormDeath

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 500ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 1

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |141  |169  |182  |208  |234  |260  |286  |312  |338  |390  |
|Calculated damage per second|141  |169  |182  |208  |234  |260  |286  |312  |338  |390  |
|Damage*                     |141.0|169.0|182.0|208.0|234.0|260.0|286.0|312.0|338.0|390.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 1s
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
  * audioDeath: "sfx_death_deathtrooper_1":35,"sfx_death_deathtrooper_2":35,"sfx_death_deathtrooper_3":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 4.5,4.27,7.56
  * iconUnlockRotation: 
  * audioTrain: 
  * iconCameraPosition: 11.27,12.43,13.71
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: stotrper_dth_rig_MASTER_MOVER/stotrper_dth_rig_locator_gun:1
  * newRotationSpeed: 7854
  * bundleName: stotrper_dth-ani
  * iconCloseupLookatPosition: -0.5,2.49,-0.78
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_deathtrooper_1":35,"sfx_placement_deathtrooper_2":35,"sfx_placement_deathtrooper_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: 0.05,1.69,0.14
  * assetName: stotrper_dth-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * autoSpawnRateScale: 1
  * decalAssetName: troop_stotrper_emp
  * armingDelay: 0
  * impactDelay: 1000
  * projectilestreams: no
  * decalBundleName: troop_stotrper_emp
  * maxScale: false
  * projectilebullet: fx_blaster_beam_r_sm
  * strictCoolDown: false
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|1.000 |1.200 |1.400 |1.600 |1.800 |2.000 |2.200 |2.400 |2.600 |3.000 |
|order     |233201|233202|233203|233204|233205|233206|233207|233208|233209|233210|

