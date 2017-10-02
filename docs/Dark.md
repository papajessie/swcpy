---
title: Phase II Dark Trooper (Dark)
category: unit
---

# Phase II Dark Trooper (Dark) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: bruiserInfantry
  * Role: Bruiser
  * Levels available: 1-10
  * Unit capacity: 4
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|3000$|3000$|6000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s   |30m  |1h30m|5h    |10h   |1d12h  |2d12h  |3d12h  |5d      |1w1d    |
|Health              |7200 |8640 |9520 |10880 |12240 |13600  |14960  |16320  |17680   |20400   |
|Damage per shot     |304  |364  |364  |416   |468   |520    |572    |624    |676     |780     |
|Damage*             |280.0|336.0|336.0|384.0 |432.0 |480.0  |528.0  |576.0  |624.0   |720.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (70)**, _Flying infantry (60)_, _Flying vehicle (60)_, _Support troop (60)_, Light vehicle (50), Heavy infantry (50), Shield (50), Storage (50), Other building (50), Heavy vehicle (50), Shield generator (50), Ressource generator (50), Infantry (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 10
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|200$                             |280$                                   |360$                                   |440$                                   |520$                                   |600$                                   |680$                                   |800$                                   |840$                                   |920$                                    |
|Training time|42s                              |44s                                    |46s                                    |48s                                    |50s                                    |52s                                    |54s                                    |1m52s                                  |1m56s                                  |2m                                      |
|Building     |[Barracks 2](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : Dark

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 3

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |304  |364  |364  |416  |468  |520  |572  |624  |676  |780  |
|Calculated damage per second|280  |336  |336  |384  |432  |480  |528  |576  |624  |720  |
|Damage*                     |280.0|336.0|336.0|384.0|432.0|480.0|528.0|576.0|624.0|720.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 3
  * Number of cannons: 0
  * Clips period: 3.250s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 25%
  * Heavy vehicle: 25%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 50%
  * Flying vehicle: 50%
  * Support troop: 50%
  * Heavy infantry hero: 25%
  * Heavy vehicular hero: 25%
  * Infantry hero: 50%
  * Vehicle hero: 50%
  * Infantry: 50%
  * Ressource generator: 100%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 50%
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

  * buffAssetOffset: 0.00,0.42,0.00
  * favoriteTargetType: turret
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 0.77,1.01,11.04
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_darktrooper_01":35,"sfx_ui_unitcomplete_darktrooper_02":35,"sfx_ui_unitcomplete_darktrooper_03":30
  * iconCameraPosition: 11.04,12.38,13.5
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * newRotationSpeed: 7854
  * bundleName: darktrooper_emp-ani
  * iconCloseupLookatPosition: -0.03,3.09,-1.21
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.02,1.7,0.06
  * assetName: darktrooper_emp-ani
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
  * projectilebullet: fx_blaster_beam_r_sm

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|4.000 |4.800 |5.600 |6.400 |7.200 |8.000 |8.800 |9.600 |10.400|12.000|
|order     |120201|120202|120203|120204|120205|120206|120207|120208|120209|120210|

