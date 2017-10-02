---
title: Rebel Pathfinder (Pathfinder)
category: unit
---

# Rebel Pathfinder (Pathfinder) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: infantry
  * Role: Looter
  * Levels available: 1-10
  * Unit capacity: 2
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|2500$|3000$|6000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|
|Upgrade time        |0s   |15m  |1h   |3h30m |8h    |1d     |2d     |3d12h  |5d      |1w1d    |
|Health              |2880 |3050 |3220 |3410  |3610  |3820   |4050   |4290   |4550    |4830    |
|Damage per shot     |490  |520  |550  |580   |610   |650    |690    |730    |770     |820     |
|Damage*             |470.0|490.0|520.0|550.0 |580.0 |620.0  |660.0  |690.0  |730.0   |780.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Storage (60)**, **Ressource generator (60)**, Flying infantry (50), Light vehicle (50), Heavy infantry (50), Turret (50), Shield (50), Other building (50), Heavy vehicle (50), Shield generator (50), Infantry (50), Flying vehicle (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 8
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|220$                            |230$                                  |240$                                  |250$                                  |260$                                  |300$                                  |340$                                  |400$                                  |420$                                  |460$                                   |
|Training time|46s                             |47s                                   |48s                                   |49s                                   |50s                                   |52s                                   |54s                                   |56s                                   |58s                                   |1m                                     |
|Building     |[Barracks 4](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 40
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 15

## Attack : Pathfinder

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 250ms
  * Time between shots: 0s
  * Time between last shot and reload: 0s
  * Time between two clips: 800ms
  * Salvos per clip: 1

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |490  |520  |550  |580  |610  |650  |690  |730  |770  |820  |
|Calculated damage per second|466  |495  |523  |552  |580  |619  |657  |695  |733  |780  |
|Damage*                     |470.0|490.0|520.0|550.0|580.0|620.0|660.0|690.0|730.0|780.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 1.050s
  * Projectile passes through shields: No
  * Projectile deflectable: Yes
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 50%
  * Heavy infantry: 75%
  * Heavy vehicle: 75%
  * Other building: 50%
  * Droideka: 100%
  * Flying infantry: 75%
  * Flying vehicle: 75%
  * Support troop: 75%
  * Heavy infantry hero: 75%
  * Heavy vehicular hero: 75%
  * Infantry hero: 75%
  * Vehicle hero: 75%
  * Infantry: 75%
  * Ressource generator: 400%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 400%
  * Trap: 50%
  * Turret: 50%
  * Light vehicle: 75%
  * Wall: 50%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilemuzzleFlash: fx_blaster_flash_b_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 
  * favoriteTargetType: resource
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: 1.45,1.64,9.17
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * iconCameraPosition: 10.61,11.75,12.82
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "pathfndr_rbl_rig_MASTER_MOVER/pathfndr_rbl_rig_locator_gun_Rt":1
  * newRotationSpeed: 7854
  * bundleName: pathfndr_rbl-ani
  * iconCloseupLookatPosition: -0.01,2.68,-0.31
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: 0.09,1.73,0.11
  * assetName: pathfndr_rbl-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 0
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * projectilebullet: fx_blaster_beam_b_sm

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|2.000 |2.400 |2.800 |3.200 |3.600 |4.000 |4.400 |4.800 |5.200 |6.000 |
|order     |220401|220402|220403|220404|220405|220406|220407|220408|220409|220410|

