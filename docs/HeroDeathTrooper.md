---
title: Death Trooper (HeroDeathTrooper)
category: unit
---

# Death Trooper (HeroDeathTrooper) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: hero
  * Armor type: infantry
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 1
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1                       |2                       |3                        |4                        |5                        |6                         |7                         |8                         |9                          |10                         |
|--------------------|------------------------|------------------------|-------------------------|-------------------------|-------------------------|--------------------------|--------------------------|--------------------------|---------------------------|---------------------------|
|Upgrade requirements|32 data fragments, 3000$|32 data fragments, 5000$|32 data fragments, 10000$|32 data fragments, 20000$|32 data fragments, 50000$|32 data fragments, 135000$|32 data fragments, 225000$|32 data fragments, 450000$|32 data fragments, 1500000$|32 data fragments, 2500000$|
|Upgrade time        |0s                      |1h                      |2h30m                    |7h                       |20h                      |2d12h                     |4d                        |6d                        |1w1d                       |1w5d                       |
|Health              |16000                   |17330                   |18660                    |20000                    |21330                    |22660                     |24000                     |25330                     |27330                      |30000                      |
|Damage per shot     |2630                    |2810                    |3040                     |3320                     |3590                     |3830                      |4010                      |4190                      |4520                       |4980                       |
|Damage*             |2181.0                  |2545.0                  |3090.0                   |3454.0                   |3818.0                   |4363.0                    |4909.0                    |5272.0                    |5636.0                     |6545.0                     |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (80)**, **Trap (80)**, _Shield (60)_, _Shield generator (60)_, Flying infantry (50), Light vehicle (50), Heavy infantry (50), Storage (50), Other building (50), Heavy vehicle (50), Ressource generator (50), Infantry (50), Flying vehicle (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                           |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|1000$                                       |1400$                                  |1800$                                  |2200$                                  |2600$                                  |3000$                                  |3400$                                  |4000$                                  |4200$                                  |4600$                                   |
|Training time|3m30s                                       |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |9m20s                                  |9m40s                                  |10m                                     |
|Building     |[Hero Command 2](empireTacticalCommand.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : HeroHanSolo

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 50ms
  * Time between shots: 400ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1s
  * Salvos per clip: 2

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2630  |2810  |3040  |3320  |3590  |3830  |4010  |4190  |4520  |4980  |
|Calculated damage per second|3627  |3875  |4193  |4579  |4951  |5282  |5531  |5779  |6234  |6868  |
|Damage*                     |2181.0|2545.0|3090.0|3454.0|3818.0|4363.0|4909.0|5272.0|5636.0|6545.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 1.450s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 100%
  * Heavy infantry: 100%
  * Heavy vehicle: 100%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 100%
  * Heavy vehicular hero: 100%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 100%
  * Shield: 400%
  * Shield generator: 400%
  * Storage: 100%
  * Trap: 200%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 80%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_blaster_hit_r_med
  * projectilemuzzleFlash: fx_blaster_flash_r_med
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: turret
  * audioDeath: "sfx_death_hero_deathtrooper_01":50,"sfx_death_hero_deathtrooper_02":50
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: shrd_troopHeroDeathTrooper
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: planet1 planet3 planet6 planet8 planet21 planet23
  * decalSize: 160
  * eventButtonString: hn_open_galaxy
  * iconCloseupCameraPosition: 3.94,6.77,11.83
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_deathtrooper_01":50,"sfx_ui_unitcomplete_deathtrooper_02":50
  * iconCameraPosition: 6.12,13,15.36
  * unlockPlanet: 
  * eventFeaturesString: fragment_obtain_gen
  * gunPosition: soldier_rbl_rig_MASTER_MOVER/soldier_rbl_rig_locator_gun:1
  * newRotationSpeed: 7854
  * bundleName: deathtrooper_emp-ani
  * iconCloseupLookatPosition: -0.34,2.08,-1.07
  * unlockedByEvent: true
  * audioAttack: "sfx_attack_hero_deathtrooper_01":33,"sfx_attack_hero_deathtrooper_02":33,"sfx_attack_hero_deathtrooper_03":33
  * eventButtonAction: galaxy
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_hero_deathtrooper_01":33,"sfx_placement_hero_deathtrooper_02":33,"sfx_placement_hero_deathtrooper_03":34
  * audioImpact: 
  * hologramUid: HeroHologramDeathtrooper
  * iconLookatPosition: -0.34,1.19,-0.78
  * assetName: deathtrooper_emp-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

|Level          |1          |2 |3 |4 |5 |6 |7 |8 |9 |10|
|---------------|-----------|--|--|--|--|--|--|--|--|--|
|iconUnlockScale|1.2,1.2,1.2|  |  |  |  |  |  |  |  |  |

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * autoSpawnRateScale: 1
  * maxScale: false
  * armingDelay: 0
  * impactDelay: 250
  * projectilestreams: no
  * decalBundleName: tac_hero_emp
  * decalAssetName: tac_hero_emp
  * projectilebullet: fx_blaster_beam_r_med
  * strictCoolDown: false
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|20.000|24.000|28.000|32.000|36.000|40.000|44.000|48.000|52.000|60.000|
|order     |111201|111202|111203|111204|111205|111206|111207|111208|111209|111210|

