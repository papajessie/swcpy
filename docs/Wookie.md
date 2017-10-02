---
title: Wookiee Warrior (Wookie)
category: unit
---

# Wookiee Warrior (Wookie) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: bruiserInfantry
  * Role: Bruiser
  * Levels available: 1-10
  * Unit capacity: 5
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|700$ |3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s   |30m  |1h30m|5h    |10h   |1d12h  |2d12h  |4d     |6d      |1w2d    |
|Health              |9000 |10800|10500|12000 |13500 |15000  |16500  |18000  |19500   |22500   |
|Damage per shot     |325  |390  |380  |434   |488   |542    |596    |650    |705     |813     |
|Damage*             |300.0|360.0|350.0|400.0 |450.0 |500.0  |550.0  |600.0  |650.0   |750.0   |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Turret (70)**, Flying infantry (50), Light vehicle (50), Heavy infantry (50), Shield (50), Storage (50), Other building (50), Heavy vehicle (50), Shield generator (50), Ressource generator (50), Infantry (50), Flying vehicle (50), Support troop (50), Droideka (50), HQ (50), Wall (1), Infantry hero (1), Heavy vehicular hero (1), Heavy infantry hero (1), Vehicle hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 12
  * Target preferences strength: 90
  * Retargeting offset: 10
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|250$                            |350$                                  |450$                                  |550$                                  |650$                                  |750$                                  |850$                                  |1000$                                 |1050$                                 |1150$                                  |
|Training time|1m45s                           |1m50s                                 |1m55s                                 |2m                                    |2m5s                                  |2m10s                                 |2m15s                                 |2m20s                                 |2m25s                                 |2m30s                                  |
|Building     |[Barracks 2](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

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

## Attack : Wookie

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 3

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot             |325  |390  |380  |434  |488  |542  |596  |650  |705  |813  |
|Calculated damage per second|300  |360  |350  |400  |450  |500  |550  |600  |650  |750  |
|Damage*                     |300.0|360.0|350.0|400.0|450.0|500.0|550.0|600.0|650.0|750.0|

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

  * HQ: 100%
  * Heavy infantry: 50%
  * Heavy vehicle: 50%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 75%
  * Flying vehicle: 75%
  * Support troop: 75%
  * Heavy infantry hero: 50%
  * Heavy vehicular hero: 50%
  * Infantry hero: 75%
  * Vehicle hero: 75%
  * Infantry: 75%
  * Ressource generator: 100%
  * Shield: 100%
  * Shield generator: 100%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 75%
  * Wall: 100%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilehitSpark: fx_blaster_hit_b_sm
  * projectilemuzzleFlash: fx_blaster_flash_b_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0
  * projectilearcs: false

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * buffAssetOffset: 0.00,0.36,0.00
  * favoriteTargetType: turret
  * audioDeath: "sfx_death_rebel_wookie_1":35,"sfx_death_rebel_wookie_2":35,"sfx_death_rebel_wookie_3":30
  * factoryScaleFactor: 1
  * infoUIType: 
  * upgradeShardUid: 
  * shieldAssetName: 
  * deathAnimation: buffFireBurn:15
  * eventButtonData: 
  * decalSize: 
  * eventButtonString: 
  * iconCloseupCameraPosition: -0.51,3.09,12.25
  * iconUnlockRotation: 
  * audioTrain: "sfx_ui_unitcomplete_wookie_1":35,"sfx_ui_unitcomplete_wookie_2":35,"sfx_ui_unitcomplete_wookie_3":30
  * iconCameraPosition: 9.29,13.73,18.65
  * iconUnlockScale: 
  * unlockPlanet: 
  * eventFeaturesString: 
  * gunPosition: "wookiewarrior_rbl_rig_MASTER_MOVER/wookiewarrior_rbl_rig_locator_gun":1
  * newRotationSpeed: 7854
  * bundleName: wookiewarrior_rbl-ani
  * iconCloseupLookatPosition: 0.08,3,-1.33
  * unlockedByEvent: 
  * audioAttack: "sfx_attack_rebel_wookie_1":50,"sfx_attack_rebel_wookie_2":50
  * eventButtonAction: 
  * factoryRotation: 0
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_rebel_wookie_1":50,"sfx_placement_rebel_wookie_2":50
  * audioImpact: 
  * hologramUid: 
  * iconLookatPosition: -0.06,1.71,0.07
  * assetName: wookiewarrior_rbl-ani
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * animationDelay: 0
  * iconUnlockPosition: 

## Uninterpreted stats

  * autoSpawnSpreadingScale: 1
  * maxScale: false
  * targetInRangeModifier: 1
  * impactDelay: 1000
  * projectilestreams: no
  * strictCoolDown: false
  * armingDelay: 0
  * autoSpawnRateScale: 1
  * projectilebullet: fx_blaster_beam_b_sm

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|5.000 |6.000 |7.000 |8.000 |9.000 |10.000|11.000|12.000|13.000|15.000|
|order     |220201|220202|220203|220204|220205|220206|220207|220208|220209|220210|

