---
title: Johhar Kessen (RebelJohhar)
category: unit
---

# Johhar Kessen (RebelJohhar) — version 1086

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: hero
  * Armor type: infantry
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 1
  * Upgrade requirements: 32 data fragments
  * Upgrade time: 5s
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level          |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|---------------|------|------|------|------|------|------|------|------|------|------|
|Health         |16000 |16790 |17630 |18510 |19440 |20420 |21460 |22560 |23720 |24950 |
|Damage per shot|3900  |4130  |4360  |4580  |4800  |5030  |5380  |5760  |6160  |6590  |
|Damage*        |2000.0|2400.0|2800.0|3200.0|3600.0|4000.0|4400.0|4800.0|5200.0|6000.0|

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Droideka (80)**, _Infantry hero (70)_, _Vehicle hero (70)_, _Heavy vehicular hero (70)_, _Heavy infantry hero (70)_, _Heavy infantry (60)_, _Flying infantry (60)_, _Support troop (60)_, _Infantry (60)_, _Heavy vehicle (60)_, _Light vehicle (60)_, _Flying vehicle (60)_, Other building (50), HQ (50), Shield (50), Storage (50), Shield generator (50), Turret (50), Ressource generator (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                          |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|1000$                                      |1400$                                 |1800$                                 |2200$                                 |2600$                                 |3000$                                 |3400$                                 |4000$                                 |4200$                                 |4600$                                  |
|Training time|3m30s                                      |3m40s                                 |3m50s                                 |4m                                    |4m10s                                 |4m20s                                 |4m30s                                 |9m20s                                 |9m40s                                 |10m                                    |
|Building     |[Hero Command 1](rebelTacticalCommand.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : JohharRebel

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 3
  * Max. Range: 10
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |3900  |4130  |4360  |4580  |4800  |5030  |5380  |5760  |6160  |6590  |
|Calculated damage per second|3600  |3812  |4024  |4227  |4430  |4643  |4966  |5316  |5686  |6083  |
|Damage*                     |2000.0|2400.0|2800.0|3200.0|3600.0|4000.0|4400.0|4800.0|5200.0|6000.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 3
  * Number of cannons: 0
  * Clips period: 3.250s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 50%
  * Heavy infantry: 250%
  * Heavy vehicle: 150%
  * Other building: 50%
  * Droideka: 250%
  * Flying infantry: 300%
  * Flying vehicle: 200%
  * Support troop: 300%
  * Heavy infantry hero: 250%
  * Heavy vehicular hero: 150%
  * Infantry hero: 300%
  * Vehicle hero: 200%
  * Infantry: 300%
  * Ressource generator: 50%
  * Shield: 75%
  * Shield generator: 50%
  * Storage: 50%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 200%
  * Wall: 60%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilemaxScale: 100
  * projectilehitSpark: fx_blaster_hit_b_med
  * projectilespinSpeed: 0
  * projectilemuzzleFlash: fx_blaster_flash_b_med

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * audioPlacement: "sfx_placement_foren_1":100
  * audioImpact: 
  * animationDelay: 0
  * eventFeaturesString: fragment_obtain_gen
  * shieldAssetName: 
  * audioAttack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * decalSize: 160
  * newRotationSpeed: 7854
  * tooltipHeightOffset: 
  * eventButtonString: hn_open_erk
  * gunPosition: "pathfndr_rbl_rig_MASTER_MOVER/pathfndr_rbl_rig_locator_gun_Rt":1
  * infoUIType: 
  * bundleName: forenbrand_neu-ani
  * deathAnimation: 
  * favoriteTargetType: infantry
  * eventButtonData: planet6
  * audioDeath: "sfx_death_foren_1":100
  * unlockPlanet: FUTURE_EVENT_UNLOCK_ERK
  * upgradeShardUid: shrd_troopRebelJohhar
  * iconCameraPosition: 4.91,10.98,19.43
  * eventButtonAction: planet
  * factoryRotation: 0
  * buffAssetOffset: 
  * iconCloseupCameraPosition: 2.21,4.06,9.34
  * hologramUid: HeroHologramJohharKessen
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconCloseupLookatPosition: 0,2.54,-0.89
  * assetName: forenbrand_neu-ani
  * unlockedByEvent: true
  * iconLookatPosition: 0.02,1.59,-0.01
  * factoryScaleFactor: 1
  * audioTrain: 

|Level             |1    |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------------------|-----|--|--|--|--|--|--|--|--|--|
|iconUnlockRotation|0,0,0|  |  |  |  |  |  |  |  |  |
|iconUnlockScale   |1,1,1|  |  |  |  |  |  |  |  |  |
|iconUnlockPosition|0,0,0|  |  |  |  |  |  |  |  |  |

## Uninterpreted stats

  * armingDelay: 0
  * maxScale: false
  * projectilestreams: no
  * autoSpawnRateScale: 2
  * impactDelay: 1000
  * projectilebullet: fx_blaster_beam_b_med
  * decalAssetName: tac_hero_rbl
  * strictCoolDown: false
  * decalBundleName: tac_hero_rbl
  * autoSpawnSpreadingScale: 2
  * targetInRangeModifier: 1

|Level     |1                   |2                   |3                   |4                   |5                   |6                   |7                   |8                   |9                   |10                   |
|----------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|---------------------|
|pointValue|20.000              |24.000              |28.000              |32.000              |36.000              |40.000              |44.000              |48.000              |52.000              |60.000               |
|order     |211101              |211102              |211103              |211104              |211105              |211106              |211107              |211108              |211109              |211110               |
|ability   |abilityRailGun1Rebel|abilityRailGun2Rebel|abilityRailGun3Rebel|abilityRailGun4Rebel|abilityRailGun5Rebel|abilityRailGun6Rebel|abilityRailGun7Rebel|abilityRailGun8Rebel|abilityRailGun9Rebel|abilityRailGun10Rebel|

