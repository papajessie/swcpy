---
title: Johhar Kessen (EmpireJohhar)
category: unit
---

# Johhar Kessen (EmpireJohhar) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
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
|Damage*        |2000.0|2400.0|2800.0|3200.0|3599.0|4000.0|4400.0|4800.0|5200.0|6000.0|

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Droideka (80)**, _Infantry hero (70)_, _Heavy vehicular hero (70)_, _Heavy infantry hero (70)_, _Vehicle hero (70)_, _Flying infantry (60)_, _Light vehicle (60)_, _Heavy infantry (60)_, _Heavy vehicle (60)_, _Infantry (60)_, _Flying vehicle (60)_, _Support troop (60)_, Turret (50), Shield (50), Storage (50), Other building (50), Shield generator (50), Ressource generator (50), HQ (50), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                           |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|1000$                                       |1400$                                  |1800$                                  |2200$                                  |2600$                                  |3000$                                  |3400$                                  |4000$                                  |4200$                                  |4600$                                   |
|Training time|3m30s                                       |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |4m40s                                  |4m50s                                  |5m                                      |
|Building     |[Hero Command 1](empireTacticalCommand.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : JohharEmpire

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 3

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |3900  |4130  |4360  |4580  |4800  |5030  |5380  |5760  |6160  |6590  |
|Calculated damage per second|3600  |3812  |4024  |4227  |4430  |4643  |4966  |5316  |5686  |6083  |
|Damage*                     |2000.0|2400.0|2800.0|3200.0|3599.0|4000.0|4400.0|4800.0|5200.0|6000.0|

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
  * Heavy infantry: 150%
  * Heavy vehicle: 250%
  * Other building: 50%
  * Droideka: 250%
  * Flying infantry: 200%
  * Flying vehicle: 300%
  * Support troop: 200%
  * Heavy infantry hero: 150%
  * Heavy vehicular hero: 250%
  * Infantry hero: 200%
  * Vehicle hero: 300%
  * Infantry: 200%
  * Ressource generator: 50%
  * Shield: 75%
  * Shield generator: 50%
  * Storage: 50%
  * Trap: 75%
  * Turret: 75%
  * Light vehicle: 300%
  * Wall: 60%

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
  * favoriteTargetType: infantry
  * audioDeath: "sfx_death_foren_1":100
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: shrd_troopEmpireJohhar
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: planet6
  * decalSize: 160
  * eventButtonString: hn_open_erk
  * iconCloseupCameraPosition: 2.21,4.06,9.34
  * audioTrain: 
  * iconCameraPosition: 4.91,10.98,19.43
  * unlockPlanet: FUTURE_EVENT_UNLOCK_ERK
  * eventFeaturesString: fragment_obtain_gen
  * gunPosition: "snipertrooper_emp_rig_MASTER_MOVER/snipertrooper_emp_rig_locator_gun_Rt":1
  * newRotationSpeed: 7854
  * bundleName: forenbrand_neu-ani
  * iconCloseupLookatPosition: 0,2.54,-0.89
  * unlockedByEvent: true
  * audioAttack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * eventButtonAction: planet
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_foren_1":100
  * audioImpact: 
  * hologramUid: HeroHologramJohharKessen
  * iconLookatPosition: 0.02,1.59,-0.01
  * assetName: forenbrand_neu-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0

|Level             |1    |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------------------|-----|--|--|--|--|--|--|--|--|--|
|iconUnlockRotation|0,0,0|  |  |  |  |  |  |  |  |  |
|iconUnlockScale   |1,1,1|  |  |  |  |  |  |  |  |  |
|iconUnlockPosition|0,0,0|  |  |  |  |  |  |  |  |  |

## Uninterpreted stats

  * autoSpawnSpreadingScale: 2
  * autoSpawnRateScale: 2
  * maxScale: false
  * decalBundleName: tac_hero_emp
  * armingDelay: 0
  * impactDelay: 1000
  * projectilestreams: no
  * decalAssetName: tac_hero_emp
  * projectilebullet: fx_blaster_beam_r_med
  * strictCoolDown: false
  * targetInRangeModifier: 1

|Level     |1                    |2                    |3                    |4                    |5                    |6                    |7                    |8                    |9                    |10                    |
|----------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|----------------------|
|pointValue|20.000               |24.000               |28.000               |32.000               |36.000               |40.000               |44.000               |48.000               |52.000               |60.000                |
|ability   |abilityRailGun1Empire|abilityRailGun2Empire|abilityRailGun3Empire|abilityRailGun4Empire|abilityRailGun5Empire|abilityRailGun6Empire|abilityRailGun7Empire|abilityRailGun8Empire|abilityRailGun9Empire|abilityRailGun10Empire|
|order     |111101               |111102               |111103               |111104               |111105               |111106               |111107               |111108               |111109               |111110                |

