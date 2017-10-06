---
title: Luke Skywalker (HeroLukeSkywalker)
category: unit
---

# Luke Skywalker (HeroLukeSkywalker) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: hero
  * Armor type: infantry
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1      |2     |3      |4      |5      |6      |7       |8       |9       |10      |
|--------------------|-------|------|-------|-------|-------|-------|--------|--------|--------|--------|
|Upgrade requirements|Nothing|75000$|150000$|300000$|600000$|900000$|1050000$|1200000$|3200000$|4800000$|
|Upgrade time        |1h     |1h    |5h     |21h    |2d     |4d     |6d      |1w2d    |1w5d    |2w      |
|Health              |18000  |21600 |25200  |28800  |32400  |36000  |39600   |43200   |46800   |54000   |
|Damage per shot     |1500   |1800  |2100   |2400   |2700   |3000   |3300    |3600    |3900    |4500    |
|Damage*             |2400.0 |2880.0|3360.0 |3840.0 |4320.0 |4800.0 |5280.0  |5760.0  |6240.0  |7200.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (80)**, Light vehicle (50), Storage (50), Flying infantry (50), HQ (50), Infantry (50), Droideka (50), Flying vehicle (50), Support troop (50), Other building (50), Shield (50), Ressource generator (50), Shield generator (50), Heavy vehicle (50), Heavy infantry (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                          |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|1500$                                      |2100$                                 |2700$                                 |3300$                                 |3900$                                 |4500$                                 |5100$                                 |5700$                                 |6300$                                 |6900$                                  |
|Training time|7m                                         |7m20s                                 |7m40s                                 |8m                                    |8m20s                                 |8m40s                                 |9m                                    |9m20s                                 |9m40s                                 |10m                                    |
|Building     |[Hero Command 8](rebelTacticalCommand.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : HERO Luke Attack

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 2
  * Max. Range: 7
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |1500  |1800  |2100  |2400  |2700  |3000  |3300  |3600  |3900  |4500  |
|Calculated damage per second|2400  |2880  |3360  |3840  |4320  |4800  |5280  |5760  |6240  |7200  |
|Damage*                     |2400.0|2880.0|3360.0|3840.0|4320.0|4800.0|5280.0|5760.0|6240.0|7200.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 1.250s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 25
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 60%
  * Heavy vehicle: 100%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 60%
  * Heavy vehicular hero: 60%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 85%
  * Shield: 200%
  * Shield generator: 100%
  * Storage: 85%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 75%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilemuzzleFlash: fx_blaster_flash_b_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: turret
  * buffAssetOffset: 
  * eventButtonAction: 
  * gunPosition: "lukeskywalker_rbl_rig_MASTER_MOVER/lukeskywalker_rbl_rig_locator_gun":1
  * iconCameraPosition: 9.95,9.78,16.61
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_hero_luke":100
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_hero_luke":100
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: 
  * iconLookatPosition: -0.45,1.28,-0.62
  * iconUnlockScale: 
  * bundleName: lukeskywalker_rbl-ani
  * assetName: lukeskywalker_rbl-ani
  * audioTrain: 
  * decalSize: 160
  * hologramUid: HeroHologramLukeSkywalker
  * iconCloseupCameraPosition: 0.34,1.87,9.02
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * iconCloseupLookatPosition: 0.02,2.48,-0.32
  * upgradeShardUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * decalBundleName: tac_hero_rbl
  * autoSpawnSpreadingScale: 0
  * ability: abilityHeroLukeDefend
  * projectilestreams: no
  * decalAssetName: tac_hero_rbl
  * projectilebullet: fx_blaster_beam_b_sm
  * targetInRangeModifier: 1
  * impactDelay: 250
  * spawnEffectUid: effectRebelSpawn
  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * autoSpawnRateScale: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|effectType|2     |2     |1     |1     |1     |1     |1     |1     |1     |1     |
|order     |210601|210602|210603|210604|210605|210606|210607|210608|210609|210610|
|pointValue|20.000|24.000|28.000|32.000|36.000|40.000|44.000|48.000|52.000|60.000|

