---
title: Rebel Sharpshooter (Marksman)
category: unit
---

# Rebel Sharpshooter (Marksman) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: infantry
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 8
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|500$ |1000$ |4000$ |13000$|18000$|100000$|175000$|340000$|1000000$|2000000$|
|Upgrade time        |0s   |45m   |2h    |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Health              |3200 |3840  |4480  |5120  |5760  |6400   |7040   |7680   |8320    |9600    |
|Damage per shot     |954  |1144  |1335  |1526  |1716  |1907   |2098   |2288   |2479    |2860    |
|Damage*             |880.0|1056.0|1232.0|1408.0|1584.0|1760.0 |1936.0 |2112.0 |2288.0  |2640.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Heavy infantry (60)**, **Flying infantry (60)**, **Droideka (60)**, **Support troop (60)**, **Infantry (60)**, Other building (50), HQ (50), Shield (50), Heavy vehicle (50), Storage (50), Shield generator (50), Light vehicle (50), Turret (50), Ressource generator (50), Flying vehicle (50), Infantry hero (1), Vehicle hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|400$                            |560$                                  |720$                                  |880$                                  |1040$                                 |1200$                                 |1360$                                 |1600$                                 |1680$                                 |1840$                                  |
|Training time|1m3s                            |1m6s                                  |1m9s                                  |1m12s                                 |1m15s                                 |1m18s                                 |1m21s                                 |3m44s                                 |3m52s                                 |4m                                     |
|Building     |[Barracks 7](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : projectileMarksman

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 3
  * Max. Range: 10
  * Min. Range: 0

|Level                       |1    |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|-----|------|------|------|------|------|------|------|------|------|
|Damage per shot             |954  |1144  |1335  |1526  |1716  |1907  |2098  |2288  |2479  |2860  |
|Calculated damage per second|880  |1056  |1232  |1408  |1584  |1760  |1936  |2112  |2288  |2640  |
|Damage*                     |880.0|1056.0|1232.0|1408.0|1584.0|1760.0|1936.0|2112.0|2288.0|2640.0|

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
  * Heavy infantry: 150%
  * Heavy vehicle: 250%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 200%
  * Flying vehicle: 300%
  * Support troop: 200%
  * Heavy infantry hero: 150%
  * Heavy vehicular hero: 250%
  * Infantry hero: 200%
  * Vehicle hero: 300%
  * Infantry: 200%
  * Ressource generator: 100%
  * Shield: 50%
  * Shield generator: 50%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 300%
  * Wall: 40%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_b_sm

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * shieldAssetName: 
  * audioAttack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * decalSize: 
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 
  * eventButtonString: 
  * gunPosition: "pathfndr_rbl_rig_MASTER_MOVER/pathfndr_rbl_rig_locator_gun_Rt":1
  * infoUIType: 
  * bundleName: marksman_rbl-ani
  * deathAnimation: buffFireBurn:15
  * favoriteTargetType: heroes
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * iconCameraPosition: 8.69,12.35,16.88
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 
  * iconCloseupCameraPosition: -0.01,3.22,8.62
  * hologramUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: 0.08,2.65,0.01
  * assetName: marksman_rbl-ani
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * iconLookatPosition: -0.31,1.68,0.43
  * factoryScaleFactor: 1
  * audioTrain: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30

## Uninterpreted stats

  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 2
  * autoSpawnSpreadingScale: 2
  * impactDelay: 1000
  * projectilebullet: fx_blaster_beam_b_sm
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|order     |220701|220702|220703|220704|220705|220706|220707|220708|220709|220710|
|pointValue|8.000 |9.600 |11.200|12.800|14.400|16.000|17.600|19.200|20.800|24.000|

