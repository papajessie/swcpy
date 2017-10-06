---
title: Elite AT-AT (HeroATAT)
category: unit
---

# Elite AT-AT (HeroATAT) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: hero
  * Armor type: bruiserVehicle
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|6500$ |5000$ |10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|
|Upgrade time        |0s    |1h30m |3h    |8h    |1d    |3d     |5d     |1w     |1w3d    |2w      |
|Health              |24000 |28800 |33600 |38400 |43200 |48000  |52800  |57600  |62400   |72000   |
|Damage per shot     |844   |1013  |1182  |1350  |1519  |1688   |1857   |2025   |2194    |2532    |
|Damage*             |1800.0|2161.0|2521.0|2880.0|3240.0|3601.0 |3961.0 |4320.0 |4680.0  |5401.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Shield (80)**, **Shield generator (80)**, Light vehicle (50), Storage (50), Flying infantry (50), HQ (50), Infantry (50), Droideka (50), Flying vehicle (50), Support troop (50), Other building (50), Turret (50), Ressource generator (50), Heavy vehicle (50), Heavy infantry (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: No
  * Target shield border: Yes
  * Can shoot over walls: Yes
  * Self-centered targeting: No

## Recruiting

|Level        |1                                           |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|1000$                                       |1400$                                  |1800$                                  |2200$                                  |2600$                                  |3000$                                  |3400$                                  |3800$                                  |4200$                                  |4600$                                   |
|Training time|3m30s                                       |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |4m40s                                  |4m50s                                  |5m                                      |
|Building     |[Hero Command 5](empireTacticalCommand.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 10
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x2
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: Yes
  * Target locking: No
  * Propensity to go around obstacles: 200

## Attack : HeroATAT

### Basic info

  * Shot count: 8
  * Time between start of clip and first shot: 500ms
  * Time between shots: 250ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1.500s
  * Salvos per clip: 2
  * Max. Range: 10
  * Min. Range: 1

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |844   |1013  |1182  |1350  |1519  |1688  |1857  |2025  |2194  |2532  |
|Calculated damage per second|3000  |3601  |4202  |4800  |5400  |6001  |6602  |7200  |7800  |9002  |
|Damage*                     |1800.0|2161.0|2521.0|2880.0|3240.0|3601.0|3961.0|4320.0|4680.0|5401.0|

### Secondary info

  * Gun shooting sequence: 1,1,1,1
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 2.250s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 4

### Multipliers

  * HQ: 75%
  * Heavy infantry: 100%
  * Heavy vehicle: 100%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 100%
  * Heavy vehicular hero: 100%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 75%
  * Shield: 400%
  * Shield generator: 400%
  * Storage: 75%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 100%
  * Wall: 75%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_r_med
  * projectilemuzzleFlash: fx_blaster_flash_r_med
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: shieldGenerator
  * buffAssetOffset: 0.00,4.96,0.0
  * eventButtonAction: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * iconCameraPosition: 49.18,33.65,54.14
  * newRotationSpeed: 3927
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_hero_walker_1":100
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_empire_atat_1":100
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: 
  * iconLookatPosition: -2.41,4.25,-0.65
  * iconUnlockScale: 
  * bundleName: atathero_emp-ani
  * assetName: atathero_emp-ani
  * audioTrain: 
  * decalSize: 320
  * hologramUid: HeroHologramEmpire2
  * iconCloseupCameraPosition: 
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * iconCloseupLookatPosition: 
  * upgradeShardUid: 
  * rotationSpeed: 3.92698750000000007531752999057061970233917236328125
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * decalBundleName: tac_hero_emp
  * projectilestreams: no
  * effectType: 2
  * decalAssetName: tac_hero_emp
  * projectilebullet: fx_blaster_beam_r_med
  * targetInRangeModifier: 1
  * autoSpawnSpreadingScale: 0
  * impactDelay: 500
  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * autoSpawnRateScale: 2

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|order     |110501|110502|110503|110504|110505|110506|110507|110508|110509|110510|
|pointValue|20.000|24.000|28.000|32.000|36.000|40.000|44.000|48.000|52.000|60.000|

