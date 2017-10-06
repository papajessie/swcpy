---
title: Sniper Trooper (Sniper)
category: unit
---

# Sniper Trooper (Sniper) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: infantry
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 7
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|700$ |3000$|6000$ |15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s   |45m  |2h    |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Health              |2800 |3360 |3920  |4480  |5040  |5600   |6160   |6720   |7280    |8400    |
|Damage per shot     |835  |1001 |1168  |1335  |1502  |1669   |1836   |2002   |2169    |2503    |
|Damage*             |770.0|924.0|1078.0|1232.0|1386.0|1540.0 |1694.0 |1848.0 |2002.0  |2310.0  |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying infantry (60)**, **Infantry (60)**, **Droideka (60)**, **Support troop (60)**, **Heavy infantry (60)**, Light vehicle (50), Storage (50), HQ (50), Flying vehicle (50), Other building (50), Turret (50), Shield (50), Ressource generator (50), Shield generator (50), Heavy vehicle (50), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 20
  * Clip retargeting: Yes
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|350$                             |490$                                   |630$                                   |770$                                   |910$                                   |1050$                                  |1190$                                  |1400$                                  |1470$                                  |1610$                                   |
|Training time|2m48s                            |2m56s                                  |3m4s                                   |3m12s                                  |3m20s                                  |3m28s                                  |3m36s                                  |3m16s                                  |3m23s                                  |3m30s                                   |
|Building     |[Barracks 7](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

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

## Attack : projectileSniper

### Basic info

  * Shot count: 3
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 2s
  * Salvos per clip: 3
  * Max. Range: 10
  * Min. Range: 0

|Level                       |1    |2    |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|-----|-----|------|------|------|------|------|------|------|------|
|Damage per shot             |835  |1001 |1168  |1335  |1502  |1669  |1836  |2002  |2169  |2503  |
|Calculated damage per second|770  |924  |1078  |1232  |1386  |1540  |1694  |1848  |2002  |2310  |
|Damage*                     |770.0|924.0|1078.0|1232.0|1386.0|1540.0|1694.0|1848.0|2002.0|2310.0|

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
  * Heavy infantry: 250%
  * Heavy vehicle: 150%
  * Other building: 100%
  * Droideka: 100%
  * Flying infantry: 300%
  * Flying vehicle: 200%
  * Support troop: 300%
  * Heavy infantry hero: 250%
  * Heavy vehicular hero: 150%
  * Infantry hero: 300%
  * Vehicle hero: 200%
  * Infantry: 300%
  * Ressource generator: 100%
  * Shield: 50%
  * Shield generator: 50%
  * Storage: 100%
  * Trap: 100%
  * Turret: 100%
  * Light vehicle: 200%
  * Wall: 40%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_blaster_hit_r_sm
  * projectilemuzzleFlash: fx_blaster_flash_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: heroes
  * buffAssetOffset: 
  * eventButtonAction: 
  * gunPosition: "snipertrooper_emp_rig_MASTER_MOVER/snipertrooper_emp_rig_locator_gun_Rt":1
  * iconCameraPosition: 8.4,11.02,18.74
  * newRotationSpeed: 7854
  * unlockedByEvent: 
  * animationDelay: 0
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * iconUnlockRotation: 
  * audioImpact: 
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: 
  * unlockPlanet: 
  * deathAnimation: buffFireBurn:15
  * iconLookatPosition: -0.36,1.69,0.24
  * iconUnlockScale: 
  * bundleName: snipertrooper_emp-ani
  * assetName: snipertrooper_emp-ani
  * audioTrain: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: -0.07,3.69,9.81
  * eventButtonString: 
  * eventFeaturesString: 
  * audioAttack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * iconCloseupLookatPosition: 0.08,2.6,-0.81
  * upgradeShardUid: 
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * iconUnlockPosition: 
  * shieldAssetName: 

## Uninterpreted stats

  * targetInRangeModifier: 1
  * projectilestreams: no
  * maxScale: false
  * strictCoolDown: false
  * autoSpawnSpreadingScale: 2
  * armingDelay: 0
  * projectilebullet: fx_blaster_beam_r_sm
  * autoSpawnRateScale: 2
  * impactDelay: 1000

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|7.000 |8.400 |9.800 |11.200|12.600|14.000|15.400|16.800|18.200|21.000|
|order     |120701|120702|120703|120704|120705|120706|120707|120708|120709|120710|

