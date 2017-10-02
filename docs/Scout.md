---
title: Scout Trooper (Scout)
category: unit
---

# Scout Trooper (Scout) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: infantry
  * Role: Looter
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|600$ |1500$|4000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |1440 |1540 |1650 |1780  |1910  |2050   |2200   |2370   |2550    |2750    |
|Damage per shot     |200  |220  |230  |250   |260   |280    |300    |330    |350     |380     |
|Damage*             |190.0|210.0|220.0|240.0 |250.0 |270.0  |280.0  |310.0  |330.0   |360.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Storage (80)**, **Ressource generator (80)**, Flying infantry (50), Light vehicle (50), Heavy infantry (50), Turret (50), Shield (50), Other building (50), Heavy vehicle (50), Shield generator (50), Infantry (50), Flying vehicle (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 8
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|80$                              |90$                                    |100$                                   |110$                                   |130$                                   |150$                                   |170$                                   |200$                                   |210$                                   |230$                                    |
|Training time|21s                              |22s                                    |23s                                    |24s                                    |25s                                    |26s                                    |27s                                    |28s                                    |29s                                    |30s                                     |
|Building     |[Barracks 3](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

|Level|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|-----|--|--|--|--|--|--|--|--|--|--|
|Speed|30|40|40|40|40|40|40|40|40|40|

## Attack : Scout

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 250ms
  * Time between shots: 0s
  * Time between last shot and reload: 0s
  * Time between two clips: 800ms
  * Salvos per clip: 1

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |200  |220  |230  |250  |260  |280  |300  |330  |350  |380  |
|Calculated damage per second|190  |209  |219  |238  |247  |266  |285  |314  |333  |361  |
|Damage*                     |190.0|210.0|220.0|240.0|250.0|270.0|280.0|310.0|330.0|360.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 1.050s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 50%
  * Heavy infantry: 75%
  * Heavy vehicle: 75%
  * Other building: 50%
  * Droideka: 100%
  * Flying infantry: 75%
  * Flying vehicle: 75%
  * Support troop: 75%
  * Heavy infantry hero: 75%
  * Heavy vehicular hero: 75%
  * Infantry hero: 75%
  * Vehicle hero: 75%
  * Infantry: 75%
  * Ressource generator: 400%
  * Shield: 100%
  * Shield generator: 50%
  * Storage: 400%
  * Trap: 50%
  * Turret: 50%
  * Light vehicle: 75%
  * Wall: 50%

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
  * favoriteTargetType: resource
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 2.23,1.18,9.57
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * iconCameraPosition: 11.49,12.45,13.64
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "scotrper_emp_rig_MASTER_MOVER/scotrper_emp_rig_joint1/scotrper_emp_rig_joint2/scotrper_emp_rig_joint27/scotrper_emp_rig_joint28/scotrper_emp_rig_joint29/scotrper_emp_rig_guMesh":1
  * newRotationSpeed: 7854
  * bundleName: scotrper_emp-ani
  * iconCloseupLookatPosition: -0.05,2.58,-0.59
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: 0.2,1.71,0.02
  * assetName: scotrper_emp-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 0
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * projectilebullet: fx_blaster_beam_r_sm

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|1.000 |1.200 |1.400 |1.600 |1.800 |2.000 |2.200 |2.400 |2.600 |3.000 |
|order     |120301|120302|120303|120304|120305|120306|120307|120308|120309|120310|

