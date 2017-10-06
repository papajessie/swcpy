---
title: Scout Undead Trooper (SmugglerScoutDeath)
category: unit
---

# Scout Undead Trooper (SmugglerScoutDeath) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Independant units
  * Buildable unit: No
  * Type: infantry
  * Armor type: infantry
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|600$ |1500$|4000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |1350 |1620 |1890 |2160  |2430  |2700   |2970   |3240   |3510    |4050    |
|Damage per shot     |126  |152  |177  |202   |227   |252    |278    |303    |328     |378     |
|Damage*             |332.5|367.5|385.0|420.0 |437.5 |472.5  |490.0  |542.5  |577.5   |630.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Light vehicle (60)**, **Flying infantry (60)**, **Vehicle hero (60)**, **Infantry (60)**, **Droideka (60)**, **Flying vehicle (60)**, **Support troop (60)**, **Heavy infantry hero (60)**, **Infantry hero (60)**, **Heavy vehicular hero (60)**, **Heavy vehicle (60)**, **Heavy infantry (60)**, _Storage (51)_, _Ressource generator (51)_, HQ (50), Other building (50), Turret (50), Shield (50), Shield generator (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 8
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1  |2  |3  |4   |5   |6   |7   |8   |9   |10  |
|-------------|---|---|---|----|----|----|----|----|----|----|
|Training cost|50$|70$|90$|110$|130$|150$|170$|190$|210$|230$|
|Training time|21s|22s|23s|24s |25s |26s |27s |28s |29s |30s |

## Movement

  * Speed: 50
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 1

## Attack : ScoutDeath

### Basic info

  * Shot count: 4
  * Time between start of clip and first shot: 250ms
  * Time between shots: 225ms
  * Time between last shot and reload: 0s
  * Time between two clips: 800ms
  * Salvos per clip: 4
  * Max. Range: 4
  * Min. Range: 0

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |126  |152  |177  |202  |227  |252  |278  |303  |328  |378  |
|Calculated damage per second|292  |352  |410  |468  |526  |584  |644  |702  |760  |876  |
|Damage*                     |332.5|367.5|385.0|420.0|437.5|472.5|490.0|542.5|577.5|630.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 4
  * Number of cannons: 0
  * Clips period: 1.725s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 50%
  * Heavy infantry: 275%
  * Heavy vehicle: 200%
  * Other building: 50%
  * Droideka: 275%
  * Flying infantry: 275%
  * Flying vehicle: 275%
  * Support troop: 275%
  * Heavy infantry hero: 200%
  * Heavy vehicular hero: 200%
  * Infantry hero: 200%
  * Vehicle hero: 200%
  * Infantry: 275%
  * Ressource generator: 400%
  * Shield: 275%
  * Shield generator: 50%
  * Storage: 400%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 200%
  * Wall: 500%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_g_sm
  * projectilemuzzleFlash: fx_blaster_flash_g_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: infantry
  * buffAssetOffset: 
  * eventButtonAction: 
  * gunPosition: "scotrper_dth_rig_MASTER_MOVER/scotrper_dth_rig_locator_gun_Rt":1
  * iconCameraPosition: 10.84,12.06,13.07
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_deathtrooper_1":35,"sfx_death_deathtrooper_2":35,"sfx_death_deathtrooper_3":30
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_deathtrooper_1":35,"sfx_placement_deathtrooper_2":35,"sfx_placement_deathtrooper_3":30
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: buffFireBurn:15
  * iconLookatPosition: 0.06,1.74,0.02
  * iconUnlockScale: 
  * bundleName: scotrper_dth-ani
  * assetName: scotrper_dth-ani
  * audioTrain: 
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 4.94,-0.46,8
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * iconCloseupLookatPosition: -0.15,2.51,-0.51
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
  * projectilebullet: fx_blaster_beam_g_sm
  * autoSpawnRateScale: 1
  * impactDelay: 0

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|1.000 |1.200 |1.400 |1.600 |1.800 |2.000 |2.200 |2.400 |2.600 |3.000 |
|order     |333701|333702|333703|333704|333705|333706|333707|333708|333709|333710|

