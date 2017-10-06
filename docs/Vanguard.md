---
title: Rebel Vanguard (Vanguard)
category: unit
---

# Rebel Vanguard (Vanguard) — version 1090

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Type: infantry
  * Armor type: bruiserInfantry
  * Role: Breacher
  * Levels available: 1-10
  * Unit capacity: 3
  * Upgrade requirements: 32 data fragments
  * Upgrade time: 5s
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level          |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|---------------|------|------|------|------|------|------|------|------|------|------|
|Health         |5760  |6090  |6440  |6810  |7210  |7630  |8080  |8560  |9070  |9610  |
|Damage per shot|2340  |2532  |2742  |2970  |3222  |3492  |3792  |4122  |4482  |4872  |
|Damage*        |2340.0|2532.0|2742.0|2970.0|3222.0|3492.0|3792.0|4122.0|4482.0|4872.0|

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Trap (90)**, _Heavy vehicle (70)_, _Light vehicle (60)_, Flying infantry (50), Flying vehicle (50), Support troop (50), Storage (40), HQ (40), Infantry (40), Droideka (40), Other building (40), Turret (40), Shield (40), Ressource generator (40), Shield generator (40), Heavy infantry (40), Vehicle hero (1), Heavy infantry hero (1), Infantry hero (1), Wall (1), Heavy vehicular hero (1)
  * Targeted type: ENEMIES
  * View Range: 21
  * Target preferences strength: 100
  * Retargeting offset: 18
  * Clip retargeting: No
  * Target shield border: No
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training cost|200$                            |280$                                  |360$                                  |440$                                  |520$                                  |600$                                  |680$                                  |800$                                  |840$                                  |920$                                   |
|Training time|42s                             |44s                                   |46s                                   |48s                                   |50s                                   |52s                                   |54s                                   |1m52s                                 |1m56s                                 |2m                                     |
|Building     |[Barracks 1](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|

## Movement

  * Speed: 20
  * Run speed: 0
  * Run threshold: 0
  * Size: 1x1
  * Flying unit: No
  * Acceleration: 0
  * Crushes walls: No
  * Target locking: No
  * Propensity to go around obstacles: 200

## Attack : Vanguard Rocket

### Basic info

  * Shot count: 1
  * Time between start of clip and first shot: 250ms
  * Time between shots: 500ms
  * Time between last shot and reload: 0s
  * Time between two clips: 3s
  * Salvos per clip: 1
  * Max. Range: 9
  * Min. Range: 0

|Level                       |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|------|------|------|------|------|------|------|------|------|------|
|Damage per shot             |2340  |2532  |2742  |2970  |3222  |3492  |3792  |4122  |4482  |4872  |
|Calculated damage per second|720   |779   |843   |913   |991   |1074  |1166  |1268  |1379  |1499  |
|Damage*                     |2340.0|2532.0|2742.0|2970.0|3222.0|3492.0|3792.0|4122.0|4482.0|4872.0|

### Secondary info

  * Gun shooting sequence: 1
  * Salvos per clip: 1
  * Number of cannons: 0
  * Clips period: 3.250s
  * Projectile passes through shields: Yes
  * Projectile deflectable: No
  * Projectile speed: 18
  * Projectile is directional: Yes
  * Salvos per gun sequence: 1
  * Cannons shot per gun sequence: 1

### Multipliers

  * HQ: 200%
  * Heavy infantry: 25%
  * Heavy vehicle: 90%
  * Other building: 75%
  * Droideka: 100%
  * Flying infantry: 50%
  * Flying vehicle: 100%
  * Support troop: 50%
  * Heavy infantry hero: 25%
  * Heavy vehicular hero: 75%
  * Infantry hero: 50%
  * Vehicle hero: 100%
  * Infantry: 50%
  * Ressource generator: 75%
  * Shield: 75%
  * Shield generator: 75%
  * Storage: 75%
  * Trap: 500%
  * Turret: 75%
  * Light vehicle: 100%
  * Wall: 700%

### Presentation

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * projectilearcs: false
  * projectilehitSpark: fx_shocktrooper_vanguard_hit
  * projectilemuzzleFlash: fx_rocket_muzzle_r_sm
  * projectilemaxScale: 100
  * projectilespinSpeed: 0

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can be safely ignored.

  * favoriteTargetType: trap
  * buffAssetOffset: 
  * eventButtonAction: planet
  * gunPosition: "pathfndr_rbl_rig_MASTER_MOVER/pathfndr_rbl_rig_locator_gun_Rt":1
  * iconCameraPosition: 13.24,14.28,16
  * newRotationSpeed: 7854
  * unlockedByEvent: true
  * animationDelay: 0
  * audioDeath: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * tooltipHeightOffset: 
  * audioPlacement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * audioImpact: "sfx_impact_rocket_01":35,"sfx_impact_rocket_02":35,"sfx_impact_rocket_03":30
  * factoryRotation: 0
  * infoUIType: 
  * factoryScaleFactor: 1
  * eventButtonData: planet1
  * unlockPlanet: FUTURE_EVENT_UNLOCK_TAT
  * deathAnimation: buffFireBurn:15
  * iconLookatPosition: 0.03,1.71,0.04
  * bundleName: vanguard_rbl-ani
  * assetName: vanguard_rbl-ani
  * audioTrain: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * decalSize: 
  * hologramUid: 
  * iconCloseupCameraPosition: 0.65,2.23,9.92
  * eventButtonString: hn_open_tat
  * eventFeaturesString: fragment_obtain_gen
  * audioAttack: "sfx_attack_rocket_1":20,"sfx_attack_rocket_2":20,"sfx_attack_rocket_3":20,"sfx_attack_rocket_4":20,"sfx_attack_rocket_5":20
  * iconCloseupLookatPosition: 0.11,2.78,0.04
  * upgradeShardUid: shrd_troopVanguard
  * rotationSpeed: 7.8539750000000001506350599811412394046783447265625
  * shieldAssetName: 

|Level             |1    |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------------------|-----|--|--|--|--|--|--|--|--|--|
|iconUnlockRotation|0,0,0|  |  |  |  |  |  |  |  |  |
|iconUnlockScale   |1,1,1|  |  |  |  |  |  |  |  |  |
|iconUnlockPosition|0,0,0|  |  |  |  |  |  |  |  |  |

## Uninterpreted stats

  * targetInRangeModifier: 1
  * projectilestreams: no
  * maxScale: false
  * armingDelay: 0
  * strictCoolDown: false
  * projectilebullet: fx_rocket_projectile_r_sm
  * autoSpawnRateScale: 1
  * impactDelay: 1000
  * autoSpawnSpreadingScale: 1

|Level     |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|----------|------|------|------|------|------|------|------|------|------|------|
|pointValue|3.000 |3.600 |4.200 |4.800 |5.400 |6.000 |6.600 |7.200 |7.800 |9.000 |
|order     |221201|221202|221203|221204|221205|221206|221207|221208|221209|221210|

