---
title: Droideka Oppressor (ChampionEmpireHeavyDroidekaSample)
category: unit
---

# Droideka Oppressor (ChampionEmpireHeavyDroidekaSample) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: No
  * Type: vehicle
  * Armor type: champion
  * Role: Generic
  * Levels available: 1-10
  * Unit capacity: 15
  * Upgrade requirements: Nothing
  * Upgrade time: 0s
  * Shield Cooldown: 20s
  * Shield Range: 3

|Level          |1     |2     |3     |4     |5     |6     |7      |8      |9      |10     |
|---------------|------|------|------|------|------|------|-------|-------|-------|-------|
|Health         |23040 |28416 |32256 |36096 |39936 |43776 |46848  |49920  |52160  |54400  |
|Damage per shot|3500  |3750  |4000  |4250  |4500  |4750  |5000   |5250   |5500   |5750   |
|Damage*        |7000.0|7500.0|8000.0|8500.0|9000.0|9500.0|10000.0|10500.0|11000.0|11500.0|
|Shield Health  |8640  |10656 |12096 |13536 |14976 |16416 |17568  |18720  |19920  |21120  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Light vehicle (50)**, **Storage (50)**, **HQ (50)**, **Infantry (50)**, **Droideka (50)**, **Support troop (50)**, **Other building (50)**, **Turret (50)**, **Ressource generator (50)**, **Heavy vehicle (50)**, **Heavy infantry (50)**, Shield (5), Shield generator (5), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Flying infantry (0), Flying vehicle (0), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 14
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: Yes
  * Self-centered targeting: No

## Recruiting

  * Training cost: Free

|Level        |1                              |2                              |3                              |4                              |5                               |6                               |7                               |8                               |9                               |10                              |
|-------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|
|Training time|1h8m                           |1h18m                          |1h28m                          |1h39m                          |1h48m                           |1h58m                           |2h8m                            |2h19m                           |2h19m                           |2h19m                           |
|Building     |[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 10](empireHQ.html)|

## Movement

  * Speed: 20
  * Run speed: 60
  * Run threshold: 6
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: Yes
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : HeavyDroidekaShell

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 650ms
  * Time between shots: 750ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1s
  * Salvos per clip: 2
  * Max. Range: 10
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7      |8      |9      |10     |
|----------------------------|------|------|------|------|------|------|-------|-------|-------|-------|
|Damage per shot             |3500  |3750  |4000  |4250  |4500  |4750  |5000   |5250   |5500   |5750   |
|Calculated damage per second|2916  |3125  |3333  |3541  |3750  |3958  |4166   |4375   |4583   |4791   |
|Damage*                     |7000.0|7500.0|8000.0|8500.0|9000.0|9500.0|10000.0|10500.0|11000.0|11500.0|

### Secondary info

  * Gun shooting sequence: 1,2
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 2.400s
  * Projectile passes through shields: No
  * Projectile deflectable: No
  * Projectile speed: 5
  * Projectile is directional: No
  * Salvos per gun sequence: 2
  * Cannons shot per gun sequence: 2

### Multipliers

  * HQ: 100%
  * Heavy infantry: 75%
  * Heavy vehicle: 75%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 20%
  * Flying vehicle: 20%
  * Support troop: 100%
  * Heavy infantry hero: 75%
  * Heavy vehicular hero: 75%
  * Infantry hero: 100%
  * Vehicle hero: 100%
  * Infantry: 100%
  * Ressource generator: 90%
  * Shield: 25%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 0%
  * Turret: 100%
  * Light vehicle: 100%
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: true
  * projectilehitSpark: fx_artilleryDroideka_hit
  * projectilemuzzleFlash: fx_artilleryDroideka_muzzle
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: closest
  * buffAssetOffset: 0.00,0.65,0.00
  * eventButtonAction: 
  * gunPosition: atst_emp_rig_MASTER_MOVER/locator_gun_Lt1:1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 250
  * tooltipHeightOffset: 1.5
  * iconUnlockRotation: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 0.8689999999999999946709294817992486059665679931640625
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: 
  * iconUnlockScale: 
  * audioTrain: 
  * decalSize: 160
  * hologramUid: 
  * iconCloseupCameraPosition: 
  * eventButtonString: 
  * eventFeaturesString: 
  * iconCloseupLookatPosition: 
  * upgradeShardUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconUnlockPosition: 

|Level             |1                                                                                                             |2                                                                                                             |3                                                                                                             |4                                                                                                             |5                                                                                                             |6                                                                                                             |7                                                                                                             |8                                                                                                             |9                                                                                                             |10                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
|iconCameraPosition|-9.81,16.18,23.56                                                                                             |-9.81,16.18,23.56                                                                                             |-9.81,16.18,23.56                                                                                             |-10.52,17.22,25.24                                                                                            |-10.52,17.22,25.24                                                                                            |-11.59,19.02,28.21                                                                                            |-11.59,19.02,28.21                                                                                            |-5.03,18.08,36.98                                                                                             |-5.03,18.08,36.98                                                                                             |-5.03,18.08,36.98                                                                                             |
|audioDeath        |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":50                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":51                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":52                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":53                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":54                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":55                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":56                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":57                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":58                                       |"sfx_death_artillerydroideka_01":50,"sfx_death_artillerydroideka_02":59                                       |
|audioPlacement    |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":50                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":51                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":52                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":53                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":54                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":55                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":56                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":57                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":58                               |"sfx_placement_artillerydroideka_01":50,"sfx_placement_artillerydroideka_02":59                               |
|audioImpact       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":51                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":52                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":53                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":54                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":55                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":56                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":57                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":58                                                       |"sfx_explosion_impact_1":50,"sfx_explosion_impact_2":59                                                       |
|iconLookatPosition|0.23,1.51,-0.32                                                                                               |0.23,1.51,-0.32                                                                                               |0.23,1.51,-0.32                                                                                               |0.23,1.51,-0.32                                                                                               |0.23,1.51,-0.32                                                                                               |0.4,1.52,-0.26                                                                                                |0.4,1.52,-0.26                                                                                                |0.27,1.61,-0.25                                                                                               |0.27,1.61,-0.25                                                                                               |0.27,1.61,-0.25                                                                                               |
|bundleName        |artillerydroideka_con-ani-up1                                                                                 |artillerydroideka_con-ani-up10                                                                                |artillerydroideka_con-ani-up10                                                                                |artillerydroideka_con-ani-up20                                                                                |artillerydroideka_con-ani-up20                                                                                |artillerydroideka_con-ani-up30                                                                                |artillerydroideka_con-ani-up30                                                                                |artillerydroideka_con-ani-up40                                                                                |artillerydroideka_con-ani-up40                                                                                |artillerydroideka_con-ani-up40                                                                                |
|assetName         |artillerydroideka_con-ani-up1                                                                                 |artillerydroideka_con-ani-up10                                                                                |artillerydroideka_con-ani-up10                                                                                |artillerydroideka_con-ani-up20                                                                                |artillerydroideka_con-ani-up20                                                                                |artillerydroideka_con-ani-up30                                                                                |artillerydroideka_con-ani-up30                                                                                |artillerydroideka_con-ani-up40                                                                                |artillerydroideka_con-ani-up40                                                                                |artillerydroideka_con-ani-up40                                                                                |
|audioAttack       |"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":30|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":31|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":32|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":33|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":34|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":35|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":36|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":37|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":38|"sfx_attack_artillerydroideka_01":35,"sfx_attack_artillerydroideka_02":35,"sfx_attack_artillerydroideka_03":39|
|shieldAssetName   |effectEmpireHeavyDroidekaShield1                                                                              |effectEmpireHeavyDroidekaShield10                                                                             |effectEmpireHeavyDroidekaShield10                                                                             |effectEmpireHeavyDroidekaShield20                                                                             |effectEmpireHeavyDroidekaShield20                                                                             |effectEmpireHeavyDroidekaShield30                                                                             |effectEmpireHeavyDroidekaShield30                                                                             |effectEmpireHeavyDroidekaShield40                                                                             |effectEmpireHeavyDroidekaShield40                                                                             |effectEmpireHeavyDroidekaShield40                                                                             |

## Uninterpreted stats

  * projectiles1Time: 300
  * maxScale: false
  * projectilebullet: fx_artilleryDroideka_projectile
  * projectilestreams: no
  * autoSpawnSpreadingScale: 2
  * impactDelay: 0
  * spawnEffectUid: effectEmpireSpawn
  * strictCoolDown: false
  * projectilesTransition: 100
  * projectiles2Time: 300
  * targetInRangeModifier: 1
  * autoSpawnRateScale: 2
  * armingDelay: 0

|Level     |1     |2     |3     |4      |5      |6      |7      |8      |9      |10     |
|----------|------|------|------|-------|-------|-------|-------|-------|-------|-------|
|order     |114705|114710|114715|114720 |114725 |114730 |114735 |114740 |114745 |114750 |
|pointValue|40.000|68.000|88.000|108.000|128.000|148.000|172.000|200.000|200.000|200.000|

