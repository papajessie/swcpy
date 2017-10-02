---
title: Twi'lek Incinerator (EmpireTwilekIncinerator)
category: unit
---

# Twi'lek Incinerator (EmpireTwilekIncinerator) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: mercenary
  * Armor type: infantry
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 4
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1      |2        |3        |4         |5         |6         |7         |8         |9         |10         |
|--------------------|-------|---------|---------|----------|----------|----------|----------|----------|----------|-----------|
|Upgrade requirements|Nothing|4000 Con.|8000 Con.|17000 Con.|35000 Con.|65000 Con.|85000 Con.|90000 Con.|95000 Con.|127000 Con.|
|Upgrade time        |0s     |5d       |6d       |1w        |1w1d      |1w2d      |1w3d      |1w4d      |1w5d      |1w6d       |
|Health              |19640  |20152    |20408    |20664     |20920     |21176     |21432     |21688     |21944     |22200      |
|Damage per shot     |1      |2        |3        |4         |5         |6         |7         |8         |9         |10         |
|Damage*             |3744.0 |3857.0   |3917.0   |3973.0    |4032.0    |4089.0    |4145.0    |4205.0    |4261.0    |4320.0     |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (50)**, **Light vehicle (50)**, **Heavy infantry (50)**, **Turret (50)**, **Storage (50)**, **Other building (50)**, **Heavy vehicle (50)**, **Infantry hero (50)**, **Shield generator (50)**, **Ressource generator (50)**, **Heavy vehicular hero (50)**, **Infantry (50)**, **Flying vehicle (50)**, **Heavy infantry hero (50)**, **Vehicle hero (50)**, **Support troop (50)**, **Droideka (50)**, **HQ (50)**, Wall (1), Shield (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                        |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|15 Con.                                  |25 Con.                                |50 Con.                                |85 Con.                                |95 Con.                                |145 Con.                               |190 Con.                               |265 Con.                               |360 Con.                               |720 Con.                                |
|Training time|5m45s                                    |6m14s                                  |6m43s                                  |7m12s                                  |7m41s                                  |8m10s                                  |8m39s                                  |9m8s                                   |9m37s                                  |10m                                     |
|Building     |[Cantina 3](empireContrabandCantina.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : Flamethrower

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 1s
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 1

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|Calculated damage per second|0     |1     |2     |2     |3     |4     |4     |5     |6     |6     |
|Damage*                     |3744.0|3857.0|3917.0|3973.0|4032.0|4089.0|4145.0|4205.0|4261.0|4320.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 1.500s
  * Projectile passes through shields: Yes
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 75%
  * Heavy vehicle: 75%
  * Other building: 125%
  * Droideka: 100%
  * Flying infantry: 50%
  * Flying vehicle: 50%
  * Support troop: 100%
  * Heavy infantry hero: 75%
  * Heavy vehicular hero: 50%
  * Infantry hero: 100%
  * Vehicle hero: 75%
  * Infantry: 100%
  * Ressource generator: 125%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 125%
  * Trap: 0%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: 
  * projectilemuzzleFlash: fx_flamethrower_projectile
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: closest
  * audioDeath: "sfx_death_twilekincinerator_01":35,"sfx_death_twilekincinerator_02":35,"sfx_death_twilekincinerator_03":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 1.37,0.41,9.67
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_twilekincinerator_01":50,"sfx_ui_unitcomplete_twilekincinerator_02":50
  * iconCameraPosition: 7.27,7.61,17.96
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: 
  * newRotationSpeed: 7854
  * bundleName: twilek_con-ani
  * iconCloseupLookatPosition: -0.06,2.28,-0.53
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_flamethrower_twilekincinerator_01":35,"sfx_attack_flamethrower_twilekincinerator_02":35,"sfx_attack_flamethrower_twilekincinerator_03":30
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_twilekincinerator_01":35,"sfx_placement_twilekincinerator_02":35,"sfx_placement_twilekincinerator_03":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.29,1.36,-0.25
  * assetName: twilek_con-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * spawnApplyBuffs: buffReduceHeals1,buffDefendSplash2
  * deathProjectileDelay: 0
  * impactDelay: 1000
  * projectilestreams: no
  * autoSpawnRateScale: 1
  * strictCoolDown: false
  * projectilemuzzleFlashFadeTime: 1.5
  * armingDelay: 0
  * targetInRangeModifier: 1
  * deathProjectileDistance: 0

|Level                |1                                               |2                                               |3                                               |4                                               |5                                               |6                                               |7                                               |8                                               |9                                               |10                                               |
|---------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|-------------------------------------------------|
|pointValue           |1.000                                           |1.200                                           |1.400                                           |1.600                                           |1.800                                           |2.000                                           |2.200                                           |2.400                                           |2.600                                           |3.000                                            |
|projectileapplyBuffs |buffFireBurn1,buffFireBurst1                    |buffFireBurn2,buffFireBurst2                    |buffFireBurn3,buffFireBurst3                    |buffFireBurn4,buffFireBurst4                    |buffFireBurn5,buffFireBurst5                    |buffFireBurn6,buffFireBurst6                    |buffFireBurn7,buffFireBurst7                    |buffFireBurn8,buffFireBurst8                    |buffFireBurn9,buffFireBurst9                    |buffFireBurn10,buffFireBurst10                   |
|deathProjectile      |projectileDeathFlamethrowerTwiLekIncineratorLvl1|projectileDeathFlamethrowerTwiLekIncineratorLvl2|projectileDeathFlamethrowerTwiLekIncineratorLvl3|projectileDeathFlamethrowerTwiLekIncineratorLvl4|projectileDeathFlamethrowerTwiLekIncineratorLvl5|projectileDeathFlamethrowerTwiLekIncineratorLvl6|projectileDeathFlamethrowerTwiLekIncineratorLvl7|projectileDeathFlamethrowerTwiLekIncineratorLvl8|projectileDeathFlamethrowerTwiLekIncineratorLvl9|projectileDeathFlamethrowerTwiLekIncineratorLvl10|
|deathProjectileDamage|4800                                            |4896                                            |4992                                            |5088                                            |5184                                            |5280                                            |5376                                            |5760                                            |6240                                            |7200                                             |
|order                |115201                                          |115202                                          |115203                                          |115204                                          |115205                                          |115206                                          |115207                                          |115208                                          |115209                                          |115210                                           |

