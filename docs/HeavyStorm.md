---
title: Heavy Stormtrooper (HeavyStorm)
category: unit
---

# Heavy Stormtrooper (HeavyStorm) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 4
  * Type: infantry

|Level |7   |6   |8   |1   |3   |5   |2   |4   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|7040|6400|7680|3200|4480|5760|3840|5120|8320|9600|


### Training stats

|Level        |7                                      |6                                      |8                                      |1                                |3                                      |5                                      |2                                      |4                                      |9                                      |10                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|1m48s                                  |1m44s                                  |1m52s                                  |1m20s                            |1m32s                                  |1m40s                                  |1m28s                                  |1m36s                                  |1m56s                                  |2m                                      |
|Training cost|680$                                   |600$                                   |800$                                   |200$                             |360$                                   |520$                                   |280$                                   |440$                                   |840$                                   |920$                                    |
|Building     |[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Barracks 6](empireBarracks.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

|Level               |7      |6      |8      |1    |3    |5     |2    |4     |9       |10      |
|--------------------|-------|-------|-------|-----|-----|------|-----|------|--------|--------|
|Upgrade time        |2d     |1d     |3d12h  |0s   |1h   |8h    |15m  |3h30m |5d      |1w2d    |
|Upgrade requirements|160000$|100000$|320000$|3000$|6000$|25000$|3000$|12500$|1000000$|1750000$|


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

## Main attack : HeavyStorm

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

|Level          |7  |6  |8  |1  |3  |5  |2  |4  |9  |10 |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|389|354|425|177|248|319|213|283|460|531|


### Projectile

|Level                       |7       |6       |8   |1      |3      |5      |2      |4      |9       |10      |
|----------------------------|--------|--------|----|-------|-------|-------|-------|-------|--------|--------|
|Displayed damage per second |1144    |1041    |1250|520    |729    |938    |626    |832    |1352    |1561    |
|Calculated damage per second|1144.118|1041.176|1250|520.588|729.412|938.235|626.471|832.353|1352.941|1561.765|


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

  * Unit ID: HeavyStorm

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: heavytrooper_emp-ani
  * Audio attack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * Buff asset offset: 0.00,0.28,0.00
  * Bundle name: heavytrooper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_gatling_hit_r_lrg
  * Icon camera position: 7.72,10.75,21.04
  * Icon closeup camera position: 1.24,0.61,11.39
  * Icon closeup lookat position: -0.02,2.5,-0.01
  * Icon lookat position: -0.4,1.77,0.55
  * Max scale: 100
  * Muzzle flash: fx_gatling_muzzle_r_lrg
  * Name: HeavyStorm
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |7   |6   |8   |1  |3  |5  |2  |4  |9   |10  |
|---------------------------|----|----|----|---|---|---|---|---|----|----|
|Displayed damage per second|1144|1041|1250|520|729|938|626|832|1352|1561|


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

|Level      |7     |6     |8     |1     |3     |5     |2     |4     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120607|120606|120608|120601|120603|120605|120602|120604|120609|120610|
|Point value|8.800 |8     |9.600 |4     |5.600 |7.200 |4.800 |6.400 |10.400|12    |


