---
title: Jawa Saboteur (SmugglerSaboteur)
category: unit
---

# Jawa Saboteur (SmugglerSaboteur) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Independant units
  * Type: infantry
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 4
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Buildable unit      |Yes  |Yes  |Yes  |Yes   |Yes   |Yes    |Yes    |Yes    |No      |No      |
|Upgrade requirements|3000$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |3200 |3840 |4480 |5120  |5760  |6400   |7040   |7680   |8320    |9600    |
|Damage per shot     |112  |135  |157  |180   |202   |224    |247    |269    |292     |336     |
|Damage*             |329.0|396.0|461.0|529.0 |593.0 |658.0  |726.0  |790.0  |858.0   |987.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Shield (70)**, **Shield generator (70)**, _Storage (60)_, _Other building (60)_, _Ressource generator (60)_, Flying infantry (50), Light vehicle (50), Heavy infantry (50), Turret (50), Heavy vehicle (50), Infantry (50), Flying vehicle (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
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
|Training cost|250$                               |350$                               |450$                               |550$                               |650$                               |750$                               |850$                               |950$                               |1050$                              |1150$                               |
|Training time|1m40s                              |1m50s                              |1m55s                              |2m                                 |2m5s                               |2m10s                              |2m15s                              |2m20s                              |2m25s                              |2m30s                               |
|Building     |[Barracks 1](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 10](smugglerBarracks.html)|

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

## Attack : SmugglerSaboteur

### Basic info

  * Time between start of clip and first shot: 500ms
  * Time between shots: 100ms
  * Time between last shot and reload: 0s

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |112  |135  |157  |180  |202  |224  |247  |269  |292  |336  |
|Shot count                  |5    |5    |5    |5    |5    |5    |5    |5    |5    |10   |
|Time between two clips      |500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|500ms|2s   |
|Salvos per clip             |5    |5    |5    |5    |5    |5    |5    |5    |5    |10   |
|Calculated damage per second|400  |482  |560  |642  |721  |800  |882  |960  |1042 |988  |
|Damage*                     |329.0|396.0|461.0|529.0|593.0|658.0|726.0|790.0|858.0|987.0|

### Secondary info

  * Gun shooting sequence: 1
  * Number of cannons: 0
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 30
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

|Level          |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|---------------|------|------|------|------|------|------|------|------|------|------|
|Salvos per clip|5     |5     |5     |5     |5     |5     |5     |5     |5     |10    |
|Clips period   |1.400s|1.400s|1.400s|1.400s|1.400s|1.400s|1.400s|1.400s|1.400s|3.400s|

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
  * Shield: 175%
  * Shield generator: 250%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 150%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_blaster_hit_y_sm
  * projectilemuzzleFlash: fx_blaster_flash_y_sm
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
  * iconCloseupCameraPosition: 
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_darktrooper_01":35,"sfx_ui_unitcomplete_darktrooper_02":35,"sfx_ui_unitcomplete_darktrooper_03":30
  * iconCameraPosition: 4.07,10.49,14.92
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "generalpurpose_smg_rig_MASTER_MOVER/generalpurpose_smg_rig_locator_gun":1
  * newRotationSpeed: 7854
  * bundleName: jawaarmed_neu-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.12,1.34,0.53
  * assetName: jawaarmed_neu-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * projectilebullet: fx_blaster_beam_y_sm

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|pointValue |5.000 |6.000 |7.000 |8.000 |9.000 |10.000|11.000|12.000|13.000|15.000|
|impactDelay|1000  |1000  |1000  |1000  |1000  |1000  |1000  |1000  |1000  |500   |
|order      |334101|334102|334103|334104|334105|334106|334107|334108|334109|334110|

