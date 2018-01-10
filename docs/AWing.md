---
title: A-wing Starfighter (AWing)
category: air
---

# A-wing Starfighter (AWing) — version 1115

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Side: Rebellion
  * Buildable unit: Yes
  * Unit capacity: 10
  * Unlock planet: Unlock on Dandoran

### Training stats

|Level        |1                                           |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|21m                                         |21m                                   |21m                                   |21m                                   |21m                                   |28m                                   |28m                                   |35m                                   |35m                                   |42m                                    |
|Training cost|7125$                                       |8325$                                 |9500$                                 |10700$                                |11875$                                |13075$                                |14250$                                |15450$                                |16625$                                |17825$                                 |
|Building     |[Starship Command 1](rebelFleetCommand.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 5s
  * Upgrade requirements: 32 data fragments

### Movement stats

  * Acceleration: 0
  * Max speed: 6

## Main attack : Proton Torpedo Barrage

### Targeting


### Shooting

  * Impact delay: 500ms
  * Shot count: 10
  * Time between shots: 75ms

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10   |
|---------------|----|----|----|----|----|----|----|----|----|-----|
|Damage per shot|6330|6650|6990|7350|7730|8130|8560|9010|9490|10000|


### Projectile

  * Splash damage percentages: 100,75,50,10

|Level                       |1    |2    |3     |4     |5     |6     |7     |8     |9     |10    |
|----------------------------|-----|-----|------|------|------|------|------|------|------|------|
|Displayed damage per second |63300|66500|69900 |73500 |77300 |81300 |85600 |90100 |94900 |100000|
|Calculated damage per second|93777|98518|103555|108888|114518|120444|126814|133481|140592|148148|
|Calculated damage per clip  |63300|66500|69900 |73500 |77300 |81300 |85600 |90100 |94900 |100000|


  * Cannons per sequence: 10
  * Cliptime: 675ms
  * Directional: No
  * Is deflectable: No
  * Max speed: 20
  * Damage multipliers: **(100)**: Shield, Shield generator, **(30)**: Droideka, **(20)**: Wall, **(15)**: Infantry, Support troop, **(12)**: Heavy infantry, **(10)**: Headquarters, Light vehicle, Other building, Storage, Turret, **(8)**: Heavy infantry hero, Heavy vehicule hero, Infantry hero, Vehicule hero, **(5)**: Heavy vehicle, Ressource generator, **(0)**: Flying infantry, Flying vehicle, Trap
  * Pass through shield: No
  * Salvos: 10

## Internal stats

These stats internal to the system link different parts of data together.

  * Upgrade shard uid: shrd_specialAttackAWing

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 2112
  * Arcs: No
  * Asset name: awingfleet_rbl-ani
  * Audio attack: "sfx_impact_shieldbreaker":100
  * Audio impact: "sfx_impact_shieldbreaker":100
  * Audio movement: "sfx_movement_rebel_awing":100
  * Audio placement: "sfx_placement_rebel_xwing_1":100
  * Bullet: fx_rocket_projectile_b_med
  * Bundle name: awingfleet_rbl-ani
  * Destroy delay: 10
  * Event button action: planet
  * Event button data: planet3
  * Event button string: hn_open_dan
  * Event features string: fragment_obtain_gen
  * Favorite target type: shieldGenerator
  * Gun position: "awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Lt_Upper/awingfleet_rbl_rig_locator_gun1":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Lt_Upper/awingfleet_rbl_rig_locator_gun2":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation/awingfleet_rbl_rig_locator_gun3":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation/awingfleet_rbl_rig_locator_gun4":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Rt_Upper/awingfleet_rbl_rig_locator_gun5":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Rt_Upper/awingfleet_rbl_rig_locator_gun6":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Lt/awingfleet_rbl_rig_locator_gun7":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Lt/awingfleet_rbl_rig_locator_gun8":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Rt/awingfleet_rbl_rig_locator_gun9":1,"awingfleet_rbl_rig_bnd_cog/awingfleet_rbl_rig_bnd_rotation_Rt/awingfleet_rbl_rig_locator_gun10":1
  * Hit spark: fx_awing-b-hit
  * Hologram uid: StarshipHologramRebel3
  * Icon asset name: icon_awingfleet_5_rbl
  * Icon bundle name: icon_awingfleet_5_rbl
  * Icon camera position: -4.39,30.77,62.91
  * Icon lookat position: -0.33,0.01,0.41
  * Max scale: 100
  * Muzzle flash: fx_rocket_muzzle_b_med
  * Name: Proton Torpedo Barrage
  * Spin speed: 0
  * Unlocked by event: true

|Level                      |1           |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|63300       |66500      |69900      |73500      |77300      |81300      |85600      |90100      |94900      |100000     |
|Icon unlock position       |0.3,0.8,-0.4|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation       |0,0,0       |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |0.4,0.4,0.4 |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Seeks target: No
  * Streams: no
  * Xp: 0

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|240901|240902|240903|240904|240905|240906|240907|240908|240909|240910|


