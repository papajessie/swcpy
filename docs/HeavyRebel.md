---
title: Heavy Soldier (HeavyRebel)
category: unit
---

# Heavy Soldier (HeavyRebel) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry

|Level |7   |2   |8   |6   |3   |9    |5   |10   |4   |1   |
|------|----|----|----|----|----|-----|----|-----|----|----|
|Health|8800|4800|9600|8000|5600|10400|7200|12000|6400|4000|


### Training stats

|Level        |7                                     |2                                     |8                                     |6                                     |3                                     |9                                     |5                                     |10                                     |4                                     |1                               |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------|
|Training time|2m15s                                 |1m50s                                 |2m20s                                 |2m10s                                 |1m55s                                 |2m25s                                 |2m5s                                  |2m30s                                  |2m                                    |1m40s                           |
|Training cost|850$                                  |350$                                  |1000$                                 |750$                                  |450$                                  |1050$                                 |650$                                  |1150$                                  |550$                                  |250$                            |
|Building     |[Research Lab 7](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Barracks 6](rebelBarracks.html)|


### Upgrading stats

|Level               |7      |2    |8      |6      |3    |9       |5     |10      |4     |1    |
|--------------------|-------|-----|-------|-------|-----|--------|------|--------|------|-----|
|Upgrade time        |2d     |15m  |3d12h  |1d     |1h   |5d      |8h    |1w2d    |3h30m |0s   |
|Upgrade requirements|175000$|3000$|350000$|115000$|6000$|1000000$|35000$|2000000$|15000$|3000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : HeavyRebel

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 10
  * Time between shots: 100ms
  * Target locking: No

|Level          |7  |2  |8  |6  |3  |9  |5  |10 |4  |1  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|487|266|531|442|310|575|398|663|354|221|


### Projectile

|Level                       |7       |2      |8       |6   |3      |9       |5       |10  |4       |1  |
|----------------------------|--------|-------|--------|----|-------|--------|--------|----|--------|---|
|Displayed damage per second |1432    |782    |1561    |1300|911    |1691    |1170    |1950|1041    |650|
|Calculated damage per second|1432.353|782.353|1561.765|1300|911.765|1691.176|1170.588|1950|1041.176|650|


  * Cannons per sequence: 1
  * Cliptime: 3.400s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 30
  * Damage multipliers: **(175)**: Shield, Shield generator, **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Storage, Support troop, Trap, Turret, Vehicule hero, **(80)**: Wall
  * Pass through shield: No
  * Salvos: 10

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: HeavyRebel

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: heavysoldier_rbl-ani
  * Audio attack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Buff asset offset: 0.00,0.30,0.00
  * Bundle name: heavysoldier_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_gatling_hit_b_lrg
  * Icon camera position: 3.52,10.26,21.73
  * Icon closeup camera position: -0.24,0.29,11.62
  * Icon closeup lookat position: -0.13,2.39,0.83
  * Icon lookat position: -0.44,1.75,0.53
  * Max scale: 100
  * Muzzle flash: fx_gatling_muzzle_b_lrg
  * Name: HeavyRebel
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |7   |2  |8   |6   |3  |9   |5   |10  |4   |1  |
|---------------------------|----|---|----|----|---|----|----|----|----|---|
|Displayed damage per second|1432|782|1561|1300|911|1691|1170|1950|1041|650|


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

|Level      |7     |2     |8     |6     |3     |9     |5     |10    |4     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |220607|220602|220608|220606|220603|220609|220605|220610|220604|220601|
|Point value|11    |6     |12    |10    |7     |13    |9     |15    |8     |5     |


