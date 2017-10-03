---
title: Cold-weather Heavy Soldier (EchoBaseHeavySoldier)
category: unit
---

# Cold-weather Heavy Soldier (EchoBaseHeavySoldier) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: No
  * Type: infantry
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 5
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|3000$ |3000$ |6000$ |15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s    |15m   |1h    |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w2d    |
|Health              |8100  |9725  |11325 |12950 |14575 |16200  |17800  |19425  |21050   |24300   |
|Damage per shot     |450   |540   |630   |720   |810   |900    |980    |1080   |1160    |1340    |
|Damage*             |2600.0|3128.0|3644.0|4164.0|4680.0|5200.0 |5728.0 |6244.0 |6764.0  |7800.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Heavy infantry (50)**, **Flying infantry (50)**, **Droideka (50)**, **Support troop (50)**, **Infantry (50)**, **Other building (50)**, **HQ (50)**, **Shield (50)**, **Heavy vehicle (50)**, **Storage (50)**, **Shield generator (50)**, **Light vehicle (50)**, **Turret (50)**, **Ressource generator (50)**, **Flying vehicle (50)**, Infantry hero (1), Vehicle hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|250$                            |350$                                  |450$                                  |550$                                  |650$                                  |750$                                  |850$                                  |1000$                                 |1050$                                 |1150$                                  |
|Training time|1m40s                           |1m50s                                 |1m55s                                 |2m                                    |2m5s                                  |2m10s                                 |2m15s                                 |2m20s                                 |2m25s                                 |2m30s                                  |
|Building     |[Barracks 6](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : HeavyRebel

### Basic info

  * Shot count: 17
  * Time between start of clip and first shot: 500ms
  * Time between shots: 75ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 17
  * Max. Range: 7
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |450   |540   |630   |720   |810   |900   |980   |1080  |1160  |1340  |
|Calculated damage per second|2067  |2481  |2894  |3308  |3721  |4135  |4502  |4962  |5329  |6156  |
|Damage*                     |2600.0|3128.0|3644.0|4164.0|4680.0|5200.0|5728.0|6244.0|6764.0|7800.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 17
  * Number of cannons: 0
  * Clips period: 3.700s
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 30
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
  * Shield: 175%
  * Shield generator: 175%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 80%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_gatling_hit_b_lrg
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_gatling_muzzle_b_lrg

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * shieldAssetName: 
  * audioAttack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * decalSize: 
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 
  * eventButtonString: 
  * gunPosition: 
  * infoUIType: 
  * bundleName: echobaseheavysoldier_rbl-ani
  * deathAnimation: buffFireBurn:15
  * favoriteTargetType: closest
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * iconCameraPosition: 3.52,10.26,21.73
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 0.00,0.30,0.00
  * iconCloseupCameraPosition: -0.24,0.29,11.62
  * hologramUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: -0.13,2.39,0.83
  * assetName: echobaseheavysoldier_rbl-ani
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * iconLookatPosition: -0.44,1.75,0.53
  * factoryScaleFactor: 1
  * audioTrain: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30

## Uninterpreted stats

  * strictCoolDown: false
  * pointValue: 1.000
  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnSpreadingScale: 1
  * impactDelay: 500
  * autoSpawnRateScale: 1
  * targetInRangeModifier: 1

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|order|300110|300111|300112|300113|300114|300115|300116|300117|300118|300119|

