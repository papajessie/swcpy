---
title: Leia Organa (HeroLeia)
category: unit
---

# Leia Organa (HeroLeia) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: hero
  * Armor type: infantry
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|3000$ |5000$ |10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|
|Upgrade time        |0s    |1h    |2h30m |7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Health              |16000 |19200 |22400 |25600 |28800 |32000  |35200  |38400  |41600   |48000   |
|Damage per shot     |934   |1120  |1307  |1494  |1680  |1867   |2054   |2240   |2427    |2800    |
|Damage*             |2001.0|2400.0|2800.0|3201.0|3600.0|4000.0 |4401.0 |4800.0 |5200.0  |6000.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Heavy infantry (60)**, **Flying infantry (60)**, **Droideka (60)**, **Support troop (60)**, **Infantry (60)**, **Heavy vehicle (60)**, **Light vehicle (60)**, **Flying vehicle (60)**, Other building (50), HQ (50), Shield (50), Storage (50), Shield generator (50), Turret (50), Ressource generator (50), Infantry hero (1), Vehicle hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                          |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|1000$                                      |1400$                                 |1800$                                 |2200$                                 |2600$                                 |3000$                                 |3400$                                 |4000$                                 |4200$                                 |4600$                                  |
|Training time|3m30s                                      |3m40s                                 |3m50s                                 |4m                                    |4m10s                                 |4m20s                                 |4m30s                                 |9m20s                                 |9m40s                                 |10m                                    |
|Building     |[Hero Command 4](rebelTacticalCommand.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : HeroLeia

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 500ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 500ms
  * Salvos per clip: 3
  * Max. Range: 7
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |934   |1120  |1307  |1494  |1680  |1867  |2054  |2240  |2427  |2800  |
|Calculated damage per second|2001  |2400  |2800  |3201  |3600  |4000  |4401  |4800  |5200  |6000  |
|Damage*                     |2001.0|2400.0|2800.0|3201.0|3600.0|4000.0|4401.0|4800.0|5200.0|6000.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 3
  * Number of cannons: 0
  * Clips period: 1.400s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 125%
  * Heavy vehicle: 125%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 150%
  * Flying vehicle: 150%
  * Support troop: 150%
  * Heavy infantry hero: 125%
  * Heavy vehicular hero: 125%
  * Infantry hero: 150%
  * Vehicle hero: 150%
  * Infantry: 150%
  * Ressource generator: 100%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 150%
  * Wall: 80%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_b_sm

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_hero_leia":100
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: 
  * shieldAssetName: 
  * audioAttack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * decalSize: 160
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 
  * eventButtonString: 
  * gunPosition: "soldier_rbl_rig_MASTER_MOVER/soldier_rbl_rig_locator_gun":1
  * infoUIType: 
  * bundleName: princessleia_rbl-ani
  * deathAnimation: 
  * favoriteTargetType: infantry
  * eventButtonData: 
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_hero_leia":100
  * unlockPlanet: 
  * upgradeShardUid: 
  * iconUnlockScale: 
  * iconCameraPosition: 11.91,11.82,11.76
  * eventButtonAction: 
  * factoryRotation: 0
  * buffAssetOffset: 
  * iconCloseupCameraPosition: 1.49,1.49,7.71
  * hologramUid: HeroHologramRebel3
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: 0,2.44,-0.3
  * assetName: princessleia_rbl-ani
  * iconUnlockPosition: 
  * unlockedByEvent: 
  * iconLookatPosition: 0.06,1.58,0.16
  * factoryScaleFactor: 1
  * audioTrain: 

## Uninterpreted stats

  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 1
  * impactDelay: 1000
  * projectilebullet: fx_blaster_beam_b_sm
  * decalAssetName: tac_hero_rbl
  * strictCoolDown: false
  * decalBundleName: tac_hero_rbl
  * autoSpawnSpreadingScale: 1
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|20.000|24.000|28.000|32.000|36.000|40.000|44.000|48.000|52.000|60.000|
|order     |210401|210402|210403|210404|210405|210406|210407|210408|210409|210410|

