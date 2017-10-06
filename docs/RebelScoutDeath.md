---
title: Scout Undead Trooper (RebelScoutDeath)
category: unit
---

# Scout Undead Trooper (RebelScoutDeath) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: No
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
|Health              |900  |1080 |1260 |1440  |1620  |1800   |1980   |2160   |2340    |2700    |
|Damage per shot     |126  |152  |177  |202   |227   |252    |278    |303    |328     |378     |
|Damage*             |120.0|144.0|168.0|192.0 |216.0 |240.0  |264.0  |288.0  |312.0   |360.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Storage (80)**, **Ressource generator (80)**, Light vehicle (50), Flying infantry (50), Vehicle hero (50), HQ (50), Infantry (50), Droideka (50), Flying vehicle (50), Support troop (50), Other building (50), Heavy infantry hero (50), Turret (50), Shield (50), Infantry hero (50), Shield generator (50), Heavy vehicular hero (50), Heavy vehicle (50), Heavy infantry (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 8
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|---------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|50$                              |70$                                   |90$                                   |110$                                  |130$                                  |150$                                  |170$                                  |190$                                  |210$                                  |230$                                   |
|Training time|21s                              |22s                                   |23s                                   |24s                                   |25s                                   |26s                                   |27s                                   |28s                                   |29s                                   |30s                                    |
|Building     |[Barracks 10](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : ScoutDeath

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 250ms
  * Time between shots: 0s
  * Time between last shot and reload: 0s
  * Time between two clips: 800ms
  * Salvos per clip: 1
  * Max. Range: 4
  * Min. Range: 0

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |126  |152  |177  |202  |227  |252  |278  |303  |328  |378  |
|Calculated damage per second|120  |144  |168  |192  |216  |240  |264  |288  |312  |360  |
|Damage*                     |120.0|144.0|168.0|192.0|216.0|240.0|264.0|288.0|312.0|360.0|

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

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilemuzzleFlash: fx_blaster_flash_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: resource
  * buffAssetOffset: 
  * eventButtonAction: 
  * gunPosition: scotrper_dth_rig_MASTER_MOVER/scotrper_dth_rig_locator_gun_Rt:1
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

  * targetInRangeModifier: 1
  * projectilestreams: no
  * maxScale: false
  * strictCoolDown: false
  * autoSpawnSpreadingScale: 1
  * armingDelay: 0
  * projectilebullet: fx_blaster_beam_r_sm
  * autoSpawnRateScale: 1
  * impactDelay: 0

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|1.000 |1.200 |1.400 |1.600 |1.800 |2.000 |2.200 |2.400 |2.600 |3.000 |
|order     |233401|233402|233403|233404|233405|233406|233407|233408|233409|233410|

