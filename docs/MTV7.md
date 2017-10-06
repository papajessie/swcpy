---
title: MTV-7 (MTV7)
category: unit
---

# MTV-7 (MTV7) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: vehicle
  * Role: Looter
  * Levels available: 1-10
  * Unit capacity: 5
  * Upgrade requirements: 32 data fragments
  * Upgrade time: 5s
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level          |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|---------------|------|------|------|------|------|------|------|------|------|------|
|Health         |19200 |19800 |20480 |21040 |21850 |22610 |23720 |25290 |26920 |28820 |
|Damage per shot|2184  |2280  |2380  |2490  |2610  |2730  |2860  |3000  |3140  |3290  |
|Damage*        |2184.0|2280.0|2380.0|2490.0|2610.0|2730.0|2860.0|3000.0|3140.0|3290.0|

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Storage (80)**, **Ressource generator (80)**, Light vehicle (50), Flying infantry (50), Vehicle hero (50), HQ (50), Infantry (50), Droideka (50), Flying vehicle (50), Support troop (50), Other building (50), Heavy infantry hero (50), Turret (50), Shield (50), Infantry hero (50), Shield generator (50), Heavy vehicular hero (50), Heavy vehicle (50), Heavy infantry (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|400$                           |560$                                   |720$                                   |880$                                   |1040$                                  |1200$                                  |1360$                                  |1600$                                  |1680$                                  |1840$                                   |
|Training time|2m40s                          |2m56s                                  |3m4s                                   |3m12s                                  |3m20s                                  |3m28s                                  |3m36s                                  |3m44s                                  |3m52s                                  |4m                                      |
|Building     |[Factory 1](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x2
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : MTV7

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 250ms
  * Time between shots: 0s
  * Time between last shot and reload: 0s
  * Time between two clips: 800ms
  * Salvos per clip: 1
  * Max. Range: 10
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2184  |2280  |2380  |2490  |2610  |2730  |2860  |3000  |3140  |3290  |
|Calculated damage per second|2080  |2171  |2266  |2371  |2485  |2600  |2723  |2857  |2990  |3133  |
|Damage*                     |2184.0|2280.0|2380.0|2490.0|2610.0|2730.0|2860.0|3000.0|3140.0|3290.0|

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
  * Heavy infantry: 50%
  * Heavy vehicle: 50%
  * Other building: 50%
  * Droideka: 100%
  * Flying infantry: 75%
  * Flying vehicle: 75%
  * Support troop: 75%
  * Heavy infantry hero: 50%
  * Heavy vehicular hero: 50%
  * Infantry hero: 75%
  * Vehicle hero: 75%
  * Infantry: 75%
  * Ressource generator: 400%
  * Shield: 50%
  * Shield generator: 50%
  * Storage: 400%
  * Trap: 50%
  * Turret: 50%
  * Light vehicle: 75%
  * Wall: 50%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilemuzzleFlash: fx_blaster_flash_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: resource
  * buffAssetOffset: 0.00,0.41,0.0
  * eventButtonAction: planet
  * gunPosition: "mtv7_emp_rig_MASTER_MOVER/mtv7_emp_rig_locator_gun":1
  * iconCameraPosition: 17.7,17.49,19.17
  * newRotationSpeed: 7854
  * unlockedByEvent: true
  * animationDelay: 0
  * audioDeath: "sfx_death_empire_mtv7_1":33,"sfx_death_empire_mtv7_2":33,"sfx_death_empire_mtv7_3":34
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_empire_mtv7_1":50,"sfx_placement_empire_mtv7_2":50
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: planet21
  * unlockPlanet: FUTURE_EVENT_UNLOCK_HTH
  * deathAnimation: 
  * iconLookatPosition: 0.04,1.16,0.04
  * bundleName: mtv7_emp-ani
  * assetName: mtv7_emp-ani
  * audioTrain: 
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 
  * eventButtonString: hn_open_hth
  * eventFeaturesString: fragment_obtain_gen
  * audioAttack: "sfx_attack_empire_mtv7_1":25,"sfx_attack_empire_mtv7_2":25,"sfx_attack_empire_mtv7_3":25,"sfx_attack_empire_mtv7_4":25
  * iconCloseupLookatPosition: 
  * upgradeShardUid: shrd_troopMTV7
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * shieldAssetName: 

|Level             |1    |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------------------|-----|--|--|--|--|--|--|--|--|--|
|iconUnlockRotation|0,0,0|  |  |  |  |  |  |  |  |  |
|iconUnlockScale   |1,1,1|  |  |  |  |  |  |  |  |  |
|iconUnlockPosition|0,0,0|  |  |  |  |  |  |  |  |  |

## Uninterpreted stats

  * ability: abilityMTVIonShot
  * projectilestreams: no
  * autoSpawnSpreadingScale: 2
  * projectilebullet: fx_blaster_beam_r_sm
  * targetInRangeModifier: 1
  * impactDelay: 1000
  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * autoSpawnRateScale: 2

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|order     |131101|131102|131103|131104|131105|131106|131107|131108|131109|131110|
|pointValue|5.000 |6.000 |7.000 |8.000 |9.000 |10.000|11.000|12.000|13.000|15.000|

