---
title: Mercenary Pistoleer (SmugglerPistoleer)
category: unit
---

# Mercenary Pistoleer (SmugglerPistoleer) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Independant units
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 6
  * Upgrade time: 0s
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|1500$|5000$|14000$|25000$|50000$|100000$|200000$|750000$|2000000$|4000000$|
|Health              |7200 |8640 |10080 |11520 |12960 |14400  |15840  |17280  |18720   |21600   |
|Damage per shot     |405  |486  |567   |648   |729   |810    |891    |972    |1053    |1215    |
|Damage*             |373.0|448.0|523.0 |598.0 |672.0 |747.0  |822.0  |897.0  |971.0   |1121.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Light vehicle (70)**, **Flying infantry (70)**, **Infantry (70)**, **Droideka (70)**, **Flying vehicle (70)**, **Support troop (70)**, **Heavy vehicle (70)**, **Heavy infantry (70)**, Storage (50), HQ (50), Other building (50), Turret (50), Shield (50), Ressource generator (50), Shield generator (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 100
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |6                                  |7                                  |8                                  |9                                  |10                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|------------------------------------|
|Training cost|50$                                |70$                                |90$                                |110$                               |130$                               |150$                               |170$                               |190$                               |210$                               |230$                                |
|Training time|4s                                 |4s                                 |5s                                 |5s                                 |5s                                 |5s                                 |5s                                 |6s                                 |6s                                 |6s                                  |
|Building     |[Barracks 1](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 10](smugglerBarracks.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 1

## Attack : SmugglerPistoleer

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 500ms
  * Time between shots: 125ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 2
  * Max. Range: 6
  * Min. Range: 0

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10    |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
|Damage per shot             |405  |486  |567  |648  |729  |810  |891  |972  |1053 |1215  |
|Calculated damage per second|720  |864  |1008 |1152 |1296 |1440 |1584 |1728 |1872 |2160  |
|Damage*                     |373.0|448.0|523.0|598.0|672.0|747.0|822.0|897.0|971.0|1121.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 1.125s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 75%
  * Heavy infantry: 100%
  * Heavy vehicle: 75%
  * Other building: 50%
  * Droideka: 100%
  * Flying infantry: 150%
  * Flying vehicle: 100%
  * Support troop: 150%
  * Heavy infantry hero: 100%
  * Heavy vehicular hero: 50%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 150%
  * Ressource generator: 50%
  * Shield: 50%
  * Shield generator: 50%
  * Storage: 50%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 100%
  * Wall: 75%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_y_sm
  * projectilemuzzleFlash: fx_blaster_flash_y_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: none
  * buffAssetOffset: 
  * eventButtonAction: 
  * gunPosition: "generalpurpose_smg_rig_MASTER_MOVER/generalpurpose_smg_rig_locator_gun":1
  * iconCameraPosition: 8.56,9.58,10.6
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: buffFireBurn:15
  * iconLookatPosition: 0.09,1.4,0.28
  * iconUnlockScale: 
  * bundleName: generalpurpose_smg-ani
  * assetName: generalpurpose_smg-ani
  * audioTrain: 
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
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
  * projectilebullet: fx_blaster_beam_y_sm
  * autoSpawnRateScale: 1
  * impactDelay: 1000

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|1.000 |1.200 |1.400 |1.600 |1.800 |2.000 |2.200 |2.400 |2.600 |3.000 |
|order     |334001|334002|334003|334004|334005|334006|334007|334008|334009|334010|

