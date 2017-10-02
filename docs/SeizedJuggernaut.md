---
title: Seized Juggernaut (SeizedJuggernaut)
category: unit
---

# Seized Juggernaut (SeizedJuggernaut) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: No
  * Type: vehicle
  * Armor type: bruiserVehicle
  * Role: Destroyer
  * Levels available: 1-10
  * Unit capacity: 20
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1     |2     |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|------|------|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|4000$ |5000$ |10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|
|Upgrade time        |0s    |1h    |2h30m |7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Health              |20000 |24000 |28000 |32000 |36000 |40000  |44000  |48000  |52000   |60000   |
|Damage per shot     |2250  |2700  |3150  |3600  |4050  |4500   |4950   |5400   |5850    |6750    |
|Damage*             |2000.0|2400.0|2800.0|3200.0|3600.0|4000.0 |4400.0 |4800.0 |5200.0  |6000.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Shield (70)**, **Shield generator (70)**, Flying infantry (50), Light vehicle (50), Heavy infantry (50), Turret (50), Storage (50), Other building (50), Heavy vehicle (50), Ressource generator (50), Infantry (50), Flying vehicle (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 16
  * Clip retargeting: No
  * Target shield border: Yes
  * Can shoot over walls: Yes
  * Self-centered targeting: No

## Recruiting

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|1000$                          |1400$                                  |1800$                                  |2200$                                  |2600$                                  |3000$                                  |3400$                                  |4000$                                  |4200$                                  |4600$                                   |
|Training time|2m48s                          |2m56s                                  |3m4s                                   |3m12s                                  |3m20s                                  |3m28s                                  |3m36s                                  |5m24s                                  |5m44s                                  |6m4s                                    |
|Building     |[Factory 5](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Speed: 30
  * Run speed: 0
  * Run threshold: 0
  * Size: 2x2
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: Yes
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : Juggernaut

### Basic info

  * Shot count: 2
  * Time between start of clip and first shot: 1s
  * Time between shots: 250ms
  * Time between last shot and reload: 0s
  * Time between two clips: 1s
  * Salvos per clip: 1

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2250  |2700  |3150  |3600  |4050  |4500  |4950  |5400  |5850  |6750  |
|Calculated damage per second|2250  |2700  |3150  |3600  |4050  |4500  |4950  |5400  |5850  |6750  |
|Damage*                     |2000.0|2400.0|2800.0|3200.0|3600.0|4000.0|4400.0|4800.0|5200.0|6000.0|

### Secondary info

  * Gun shooting sequence: 1,1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 2s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 2

### Multipliers

  * HQ: 75%
  * Heavy infantry: 100%
  * Heavy vehicle: 100%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 100%
  * Flying vehicle: 100%
  * Support troop: 100%
  * Heavy infantry hero: 200%
  * Heavy vehicular hero: 200%
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

  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilemuzzleFlash: fx_blaster_flash_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 0.00,1.84,0.00
  * favoriteTargetType: shieldGenerator
  * audioDeath: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * factoryScaleFactor: 0.72299999999999997601918266809661872684955596923828125
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: 
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 
  * iconUnlockRotation: 
  * audioTrain: 
  * iconCameraPosition: 35.28,24.86,45.37
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun1":1, "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun2":1
  * newRotationSpeed: 2000
  * bundleName: attacktank_rbl-ani
  * iconCloseupLookatPosition: 
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_rebel_attacktank_1":30,"sfx_attack_rebel_attacktank_2":35,"sfx_attack_rebel_attacktank_3":35
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.89,1.38,-0.23
  * assetName: attacktank_rbl-ani
  * rotationSpeed: 2
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 3
  * maxScale: false
  * armingDelay: 0
  * targetInRangeModifier: 1
  * impactDelay: 500
  * projectilestreams: no
  * strictCoolDown: false
  * autoSpawnRateScale: 3
  * projectilebullet: fx_blaster_beam_r_sm

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|order|484804|484808|484812|484816|484820|484824|484828|484832|484836|484840|

