---
title: Droideka Sentinal (ChampionRebelDroidekaSample)
category: unit
---

# Droideka Sentinal (ChampionRebelDroidekaSample)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: champion
  * Side: Rebellion
  * Buildable unit: No
  * Role: Generic
  * Shield cooldown: 20s
  * Shield range: 3
  * Unit capacity: 12
  * Type: vehicle

|Level        |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health       |19200|23680|26880|30080|33280|36480|39040|41600|43840|46080|
|Shield health|14400|17760|20160|22560|24960|27360|29280|31200|32400|33600|


### Training stats

  * Training cost: Free
  * Building: [Headquarters 1](rebelHQ.html)

|Level        |1   |2    |3    |4    |5    |6    |7   |8-10 |
|-------------|----|-----|-----|-----|-----|-----|----|-----|
|Training time|1h8m|1h18m|1h28m|1h39m|1h48m|1h58m|2h8m|2h19m|


### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 100
  * Run threshold: 7
  * Unit size on map: 1x1

## Main attack : Rebel Droideka Blaster

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (80)**, _Heavy infantry hero (70)_, _Heavy vehicule hero (70)_, _Infantry hero (70)_, _Vehicule hero (70)_, _Flying infantry (60)_, _Flying vehicle (60)_, _Heavy infantry (60)_, _Heavy vehicle (60)_, _Infantry (60)_, _Light vehicle (60)_, _Support troop (60)_, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Time between shots: 233ms
  * Target locking: No

|Level                |1      |2      |3      |4      |5      |6      |7      |8          |9          |10         |
|---------------------|-------|-------|-------|-------|-------|-------|-------|-----------|-----------|-----------|
|Damage per shot      |660    |815    |925    |1034   |1145   |1255   |1343   |965        |1036       |1106       |
|Gun shooting sequence|1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,2,2|1,1,1,2,2,2|1,1,1,2,2,2|1,1,1,2,2,2|
|Shot count           |8      |8      |8      |8      |8      |8      |8      |12         |12         |12         |


### Projectile

|Level                       |1   |2   |3   |4   |5   |6    |7    |8    |9    |10   |
|----------------------------|----|----|----|----|----|-----|-----|-----|-----|-----|
|Displayed damage per second |2640|3258|3699|4137|4578|5019 |5370 |5721 |6216 |6636 |
|Calculated damage per second|3107|3837|4355|4868|5391|5909 |6323 |6815 |7317 |7811 |
|Calculated damage per clip  |5280|6520|7400|8272|9160|10040|10744|11580|12432|13272|


  * Cliptime: 1.699s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 25
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Infantry, Infantry hero, Light vehicle, Other building, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, **(80)**: Wall, **(75)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, **(50)**: Ressource generator
  * Pass through shield: No
  * Salvos: 4

|Level               |1-7|8-10|
|--------------------|---|----|
|Cannons per sequence|4  |6   |


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ChampionRebelDroidekaSample

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Audio attack: "sfx_attack_empire_droideka_1":25,"sfx_attack_empire_droideka_2":25,"sfx_attack_empire_droideka_3":25,"sfx_attack_empire_droideka_4":25
  * Audio death: "sfx_death_empire_droideka_1":35,"sfx_death_empire_droideka_2":35,"sfx_death_empire_droideka_3":30
  * Audio placement: "sfx_placement_empire_droideka_1":50,"sfx_placement_empire_droideka_2":50
  * Buff asset offset: 0.00,0.65,0.00
  * Bullet: fx_blaster_beam_b_sm
  * Decal size: 160
  * Factory rotation: 0
  * Factory scale factor: 0.8689999999999999946709294817992486059665679931640625
  * Favorite target type: closest
  * Hit spark: fx_blaster_hit_y_sm
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Name: Rebel Droideka Blaster
  * Spawn effect uid: effectRebelSpawn
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Tooltip height offset: 1.5

|Level                      |1                                                                                                                                                                                      |2                                                                                                                                                                                      |3                                                                                                                                                                                      |4                                                                                                                                                                                      |5                                                                                                                                                                                      |6                                                                                                                                                                                      |7                                                                                                                                                                                      |8                                                                                                                                                                                                    |9                                                                                                                                                                                                    |10                                                                                                                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Asset name                 |droideka_con-ani-up1                                                                                                                                                                   |droideka_con-ani-up10                                                                                                                                                                  |droideka_con-ani-up10                                                                                                                                                                  |droideka_con-ani-up20                                                                                                                                                                  |droideka_con-ani-up20                                                                                                                                                                  |droideka_con-ani-up30                                                                                                                                                                  |droideka_con-ani-up30                                                                                                                                                                  |droideka_con-ani-up40                                                                                                                                                                                |droideka_con-ani-up40                                                                                                                                                                                |droideka_con-ani-up40                                                                                                                                                                                |
|Bundle name                |droideka_con-ani-up1                                                                                                                                                                   |droideka_con-ani-up10                                                                                                                                                                  |droideka_con-ani-up10                                                                                                                                                                  |droideka_con-ani-up20                                                                                                                                                                  |droideka_con-ani-up20                                                                                                                                                                  |droideka_con-ani-up30                                                                                                                                                                  |droideka_con-ani-up30                                                                                                                                                                  |droideka_con-ani-up40                                                                                                                                                                                |droideka_con-ani-up40                                                                                                                                                                                |droideka_con-ani-up40                                                                                                                                                                                |
|Displayed damage per second|2640                                                                                                                                                                                   |3258                                                                                                                                                                                   |3699                                                                                                                                                                                   |4137                                                                                                                                                                                   |4578                                                                                                                                                                                   |5019                                                                                                                                                                                   |5370                                                                                                                                                                                   |5721                                                                                                                                                                                                 |6216                                                                                                                                                                                                 |6636                                                                                                                                                                                                 |
|Gun position               |"atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2|"atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2|"atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2|"atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2|"atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2|"atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2|"atst_emp_rig_MASTER_MOVER/locator_gun_Lt1":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Lt2":1,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt1":2,"atst_emp_rig_MASTER_MOVER/locator_gun_Rt2":2|"MASTER_MOVER/locator_gun_Lt1":1,"MASTER_MOVER/locator_gun_Lt2":1,"MASTER_MOVER/locator_gun_Lt3":1,"MASTER_MOVER/locator_gun_Rt1":2,"MASTER_MOVER/locator_gun_Rt2":2,"MASTER_MOVER/locator_gun_Rt3":2|"MASTER_MOVER/locator_gun_Lt1":1,"MASTER_MOVER/locator_gun_Lt2":1,"MASTER_MOVER/locator_gun_Lt3":1,"MASTER_MOVER/locator_gun_Rt1":2,"MASTER_MOVER/locator_gun_Rt2":2,"MASTER_MOVER/locator_gun_Rt3":2|"MASTER_MOVER/locator_gun_Lt1":1,"MASTER_MOVER/locator_gun_Lt2":1,"MASTER_MOVER/locator_gun_Lt3":1,"MASTER_MOVER/locator_gun_Rt1":2,"MASTER_MOVER/locator_gun_Rt2":2,"MASTER_MOVER/locator_gun_Rt3":2|
|Icon camera position       |18.67,14.16,15.1                                                                                                                                                                       |15.43,14.67,18.88                                                                                                                                                                      |15.43,14.67,18.88                                                                                                                                                                      |15.88,14.81,19.14                                                                                                                                                                      |15.88,14.81,19.14                                                                                                                                                                      |15.91,14.58,19.08                                                                                                                                                                      |15.91,14.58,19.08                                                                                                                                                                      |21.79,18.39,13.58                                                                                                                                                                                    |21.79,18.39,13.58                                                                                                                                                                                    |21.79,18.39,13.58                                                                                                                                                                                    |
|Icon lookat position       |-0.39,1.23,-0.21                                                                                                                                                                       |-0.32,1.71,0.09                                                                                                                                                                        |-0.32,1.71,0.09                                                                                                                                                                        |-0.19,1.6,0                                                                                                                                                                            |-0.19,1.6,0                                                                                                                                                                            |-0.1,1.43,0.08                                                                                                                                                                         |-0.1,1.43,0.08                                                                                                                                                                         |-0.35,1.49,0.26                                                                                                                                                                                      |-0.35,1.49,0.26                                                                                                                                                                                      |-0.35,1.49,0.26                                                                                                                                                                                      |
|Shield asset name          |effectRebelDroidekaShield1                                                                                                                                                             |effectRebelDroidekaShield10                                                                                                                                                            |effectRebelDroidekaShield10                                                                                                                                                            |effectRebelDroidekaShield20                                                                                                                                                            |effectRebelDroidekaShield20                                                                                                                                                            |effectRebelDroidekaShield30                                                                                                                                                            |effectRebelDroidekaShield30                                                                                                                                                            |effectRebelDroidekaShield40                                                                                                                                                                          |effectRebelDroidekaShield40                                                                                                                                                                          |effectRebelDroidekaShield40                                                                                                                                                                          |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1 |2 |3 |4  |5  |6  |7  |8-10|
|-----------|--|--|--|---|---|---|---|----|
|Point value|40|68|88|108|128|148|172|200 |


