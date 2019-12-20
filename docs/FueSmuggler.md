---
title: trptitleFueSmuggler (FueSmuggler)
category: unit
---

# trptitleFueSmuggler (FueSmuggler)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Tusken Raiders
  * Health: 1000
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: infantry

### Training stats

  * Training cost: 100$

|Level        |3 |2  |1 |
|-------------|--|---|--|
|Training time|4s|21s|4s|


### Upgrading stats

  * Upgrade requirements: 1500$

|Level       |3    |2  |1    |
|------------|-----|---|-----|
|Upgrade time|1m40s|10s|1m40s|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

|Level    |3 |1-2|
|---------|--|---|
|Max speed|20|30 |


## Main attack : BountyHunter / Smuggler

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (55)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Headquarters (40), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)

|Level     |3|1-2|
|----------|-|---|
|View range|8|20 |


### Shooting

  * Animation delay: 0s
  * Charge time: 250ms
  * Clip retargeting: No
  * Impact delay: 1s
  * Can shoot over walls: No
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot delay: 500ms
  * Target locking: No

|Level                |3  |2     |1  |
|---------------------|---|------|---|
|Damage per shot      |434|50    |50 |
|Gun shooting sequence|1  |1,2   |1,2|
|Reload time          |2s |1.500s|2s |
|Shot count           |3  |2     |3  |


### Projectile

|Level                       |3   |2  |1  |
|----------------------------|----|---|---|
|Displayed damage per second |400 |44 |46 |
|Calculated damage per second|400 |44 |46 |
|Calculated damage per cycle |1302|100|150|


  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Pass through shield: No

|Level                  |3                                                                                                                                                                                                                                                                                                            |2                                                                                                                                                                                                                                                                                                                                           |1                                                                                                                                                                                                                                                                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Cannons per sequence   |1                                                                                                                                                                                                                                                                                                            |2                                                                                                                                                                                                                                                                                                                                           |2                                                                                                                                                                                                                                                                                                                                           |
|Shooting cycle duration|3.250s                                                                                                                                                                                                                                                                                                       |2.250s                                                                                                                                                                                                                                                                                                                                      |3.250s                                                                                                                                                                                                                                                                                                                                      |
|Damage multipliers     |**(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall|**(200)**: Wall, **(100)**: Droideka, Shield, Storage, **(50)**: Headquarters, Other building, Ressource generator, Shield generator, Trap, Turret, **(20)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero|**(200)**: Wall, **(100)**: Droideka, Shield, Storage, **(50)**: Headquarters, Other building, Ressource generator, Shield generator, Trap, Turret, **(20)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero|
|Salvos                 |3                                                                                                                                                                                                                                                                                                            |2                                                                                                                                                                                                                                                                                                                                           |3                                                                                                                                                                                                                                                                                                                                           |


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: FueSmuggler

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Audio attack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Bullet: fx_blaster_beam_y_sm
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: none
  * Hit spark: fx_blaster_hit_y_sm
  * Icon lookat position: 0.09,1.4,0.28
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |3                                                                         |2                                                                                                                                                  |1                                                                                                                                                  |
|---------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|Asset name                 |generalpurpose_smg-ani                                                    |bountyhunter_smg-ani                                                                                                                               |bountyhunter_smg-ani                                                                                                                               |
|Buff asset offset          |(not found)                                                               |0.00,0.08,0.00                                                                                                                                     |0.00,0.08,0.00                                                                                                                                     |
|Bundle name                |generalpurpose_smg-ani                                                    |bountyhunter_smg-ani                                                                                                                               |bountyhunter_smg-ani                                                                                                                               |
|Displayed damage per second|400                                                                       |44                                                                                                                                                 |46                                                                                                                                                 |
|Gun position               |"generalpurpose_smg_rig_MASTER_MOVER/generalpurpose_smg_rig_locator_gun":1|"bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Lt":1,"bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Rt":2|"bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Lt":1,"bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Rt":2|
|Icon camera position       |8.56,9.58,10.6                                                            |9,10,11.12                                                                                                                                         |9,10,11.12                                                                                                                                         |
|Name                       |Smuggler                                                                  |BountyHunter                                                                                                                                       |BountyHunter                                                                                                                                       |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |3     |2     |1     |
|-----------|------|------|------|
|Order      |462403|462402|462401|
|Point value|1.400 |1.200 |1     |


