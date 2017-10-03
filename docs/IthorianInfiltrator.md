---
title: Ithorian Infiltrator (IthorianInfiltrator)
category: unit
---

# Ithorian Infiltrator (IthorianInfiltrator) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: infantry
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 3
  * Upgrade requirements: 32 data fragments
  * Upgrade time: 0s
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level          |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|---------------|------|------|------|------|------|------|------|------|------|------|
|Health         |1350  |1600  |1850  |2100  |2350  |2600  |2850  |3100  |3350  |3600  |
|Damage per shot|2500  |3775  |5050  |6325  |7600  |8875  |10150 |11425 |12700 |13975 |
|Damage*        |4700.0|2545.0|3090.0|3454.0|3818.0|4363.0|4909.0|5272.0|5636.0|6545.0|

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Shield (80)**, **Shield generator (80)**, _Storage (60)_, _Ressource generator (60)_, Heavy infantry (50), Flying infantry (50), Droideka (50), Support troop (50), Infantry (50), Other building (50), HQ (50), Heavy vehicle (50), Light vehicle (50), Flying vehicle (50), Turret (40), Infantry hero (1), Vehicle hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|1000$                           |1052$                                 |1137$                                 |1242$                                 |1361$                                 |1494$                                 |1638$                                 |1791$                                 |1954$                                 |2125$                                  |
|Training time|2m40s                           |2m48s                                 |3m2s                                  |3m19s                                 |3m38s                                 |3m59s                                 |4m22s                                 |4m47s                                 |5m13s                                 |5m40s                                  |
|Building     |[Barracks 4](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 45
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 200

## Attack : IthorianInfiltrator

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 50ms
  * Time between shots: 200ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 2
  * Max. Range: 4
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2500  |3775  |5050  |6325  |7600  |8875  |10150 |11425 |12700 |13975 |
|Calculated damage per second|2222  |3355  |4488  |5622  |6755  |7888  |9022  |10155 |11288 |12422 |
|Damage*                     |4700.0|2545.0|3090.0|3454.0|3818.0|4363.0|4909.0|5272.0|5636.0|6545.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 2
  * Number of cannons: 0
  * Clips period: 2.250s
  * Projectile passes through shields: Yes
  * Projectile deflectable: Yes
  * Projectile speed: 15
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 10%
  * Heavy infantry: 10%
  * Heavy vehicle: 10%
  * Other building: 10%
  * Droideka: 10%
  * Flying infantry: 10%
  * Flying vehicle: 10%
  * Support troop: 10%
  * Heavy infantry hero: 10%
  * Heavy vehicular hero: 10%
  * Infantry hero: 10%
  * Vehicle hero: 10%
  * Infantry: 10%
  * Ressource generator: 60%
  * Shield: 100%
  * Shield generator: 600%
  * Storage: 50%
  * Trap: 0%
  * Turret: 10%
  * Light vehicle: 10%
  * Wall: 50%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_b_sm

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_troop_1":33,"sfx_placement_troop_2":33,"sfx_placement_troop_3":33
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: fragment_obtain_gen
  * shieldAssetName: 
  * audioAttack: "sfx_attack_ionblaster_1":25,"sfx_attack_ionblaster_2":25,"sfx_attack_ionblaster_3":25,"sfx_attack_ionblaster_4":25
  * decalSize: 
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 
  * eventButtonString: hn_open_galaxy
  * gunPosition: 
  * infoUIType: 
  * bundleName: ithorian_rbl-ani
  * deathAnimation: 
  * favoriteTargetType: shieldGenerator
  * eventButtonData: planet1 planet3 planet6 planet8 planet21 planet23
  * iconUnlockRotation: 
  * audioDeath: "sfx_death_ithorian_1":50,"sfx_death_ithorian_2":50
  * unlockPlanet: 
  * upgradeShardUid: shrd_troopIthorianInfiltrator
  * iconUnlockScale: 
  * iconCameraPosition: 17.05,12.75,14.83
  * eventButtonAction: galaxy
  * factoryRotation: 0
  * buffAssetOffset: 
  * iconCloseupCameraPosition: 4.79,2.66,11.07
  * hologramUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: -0.26,2.61,-0.85
  * assetName: ithorian_rbl-ani
  * iconUnlockPosition: 
  * unlockedByEvent: true
  * iconLookatPosition: 0,1.73,-0.07
  * factoryScaleFactor: 1
  * audioTrain: 

## Uninterpreted stats

  * impactDelay: 250
  * maxScale: false
  * spawnApplyBuffs: buffPersonalShieldIthorian
  * autoSpawnRateScale: 1
  * armingDelay: 0
  * projectilebullet: fx_blaster_beam_b_sm
  * strictCoolDown: false
  * projectilestreams: no
  * autoSpawnSpreadingScale: 1
  * targetInRangeModifier: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|3.000 |3.600 |4.200 |4.800 |5.400 |6.000 |6.600 |7.200 |7.800 |9.000 |
|order     |234101|234102|234103|234104|234105|234106|234107|234108|234109|234110|

