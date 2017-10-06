---
title: Elite AT-TE Walker (HeroATTE)
category: unit
---

# Elite AT-TE Walker (HeroATTE) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: hero
  * Armor type: bruiserVehicle
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1                       |2                       |3                        |4                        |5                        |6                         |7                         |8                         |9                          |10                         |
|--------------------|------------------------|------------------------|-------------------------|-------------------------|-------------------------|--------------------------|--------------------------|--------------------------|---------------------------|---------------------------|
|Upgrade requirements|32 data fragments, 6500$|32 data fragments, 5000$|32 data fragments, 10000$|32 data fragments, 20000$|32 data fragments, 50000$|32 data fragments, 135000$|32 data fragments, 225000$|32 data fragments, 450000$|32 data fragments, 1500000$|32 data fragments, 2500000$|
|Upgrade time        |0s                      |1h30m                   |3h                       |8h                       |1d                       |3d                        |5d                        |1w                        |1w3d                       |2w                         |
|Health              |38400                   |41600                   |44800                    |48000                    |51200                    |54400                     |57600                     |60800                     |65600                      |72000                      |
|Damage per shot     |2430                    |2917                    |3404                     |3888                     |4374                     |4861                      |5348                      |5832                      |6318                       |7292                       |
|Damage*             |1800.0                  |2161.0                  |2521.0                   |2880.0                   |3240.0                   |3601.0                    |3961.0                    |4320.0                    |4680.0                     |5401.0                     |

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

|Level        |1                                          |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|1000$                                      |1400$                                 |1800$                                 |2200$                                 |2600$                                 |3000$                                 |3400$                                 |3800$                                 |4200$                                 |4600$                                  |
|Training time|3m30s                                      |3m40s                                 |3m50s                                 |4m                                    |4m10s                                 |4m20s                                 |4m30s                                 |4m40s                                 |4m50s                                 |5m                                     |
|Building     |[Hero Command 5](rebelTacticalCommand.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : HeroATTE

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 500ms
  * Time between shots: 400ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1s
  * Salvos per clip: 3
  * Max. Range: 10
  * Min. Range: 1

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2430  |2917  |3404  |3888  |4374  |4861  |5348  |5832  |6318  |7292  |
|Calculated damage per second|3169  |3804  |4440  |5071  |5705  |6340  |6975  |7606  |8240  |9511  |
|Damage*                     |1800.0|2161.0|2521.0|2880.0|3240.0|3601.0|3961.0|4320.0|4680.0|5401.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 3
  * Number of cannons: 0
  * Clips period: 2.300s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

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
  * projectilehitSpark: fx_blaster_hit_b_med
  * projectilemuzzleFlash: fx_blaster_flash_b_med
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: shieldGenerator
  * buffAssetOffset: 0.00,1.46,0.00
  * eventButtonAction: galaxy
  * gunPosition: atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun:1
  * iconCameraPosition: 36.44,26.49,49.08
  * newRotationSpeed: 3927
  * unlockedByEvent: true
  * animationDelay: 0
  * audioDeath: "sfx_death_hero_walker_1":100
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_empire_atat_1":100
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: planet1 planet3 planet6 planet8 planet21 planet23
  * unlockPlanet: 
  * deathAnimation: 
  * iconLookatPosition: 0.12,2.66,-0.82
  * bundleName: attehero_rbl-ani
  * assetName: attehero_rbl-ani
  * audioTrain: 
  * decalSize: 320
  * hologramUid: HeroHologramATTE
  * iconCloseupCameraPosition: 
  * eventButtonString: hn_open_galaxy
  * eventFeaturesString: fragment_obtain_gen
  * audioAttack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * iconCloseupLookatPosition: 
  * upgradeShardUid: shrd_troopHeroATTE
  * rotationSpeed: 3.92698750000000007531752999057061970233917236328125
  * iconUnlockPosition: 
  * shieldAssetName: 

|Level             |1          |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------------------|-----------|--|--|--|--|--|--|--|--|--|
|iconUnlockRotation|0,-20,0    |  |  |  |  |  |  |  |  |  |
|iconUnlockScale   |0.5,0.5,0.5|  |  |  |  |  |  |  |  |  |

## Uninterpreted stats

  * decalBundleName: tac_hero_rbl
  * projectilestreams: no
  * effectType: 2
  * decalAssetName: tac_hero_rbl
  * projectilebullet: fx_blaster_beam_b_med
  * targetInRangeModifier: 1
  * autoSpawnSpreadingScale: 0
  * impactDelay: 500
  * strictCoolDown: false
  * armingDelay: 0
  * maxScale: false
  * autoSpawnRateScale: 2

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|order     |211201|211202|211203|211204|211205|211206|211207|211208|211209|211210|
|pointValue|20.000|24.000|28.000|32.000|36.000|40.000|44.000|48.000|52.000|60.000|

