---
title: Scout Trooper (Scout)
category: unit
---

# Scout Trooper (Scout) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Looter
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: infantry

|Level |9   |8   |10  |2   |1   |5   |6   |7   |4   |3   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2550|2370|2750|1540|1440|1910|2050|2200|1780|1650|


### Training stats

|Level        |9                                      |8                                      |10                                      |2                                      |1                                |5                                      |6                                      |7                                      |4                                      |3                                      |
|-------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|29s                                    |28s                                    |30s                                     |22s                                    |21s                              |25s                                    |26s                                    |27s                                    |24s                                    |23s                                    |
|Training cost|210$                                   |200$                                   |230$                                    |90$                                    |80$                              |130$                                   |150$                                   |170$                                   |110$                                   |100$                                   |
|Building     |[Research Lab 9](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Barracks 3](empireBarracks.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|


### Upgrading stats

|Level               |9       |8      |10      |2    |1   |5     |6      |7      |4     |3    |
|--------------------|--------|-------|--------|-----|----|------|-------|-------|------|-----|
|Upgrade time        |5d      |3d12h  |1w1d    |15m  |0s  |8h    |1d     |2d     |3h30m |1h   |
|Upgrade requirements|1000000$|320000$|1750000$|1500$|600$|25000$|100000$|160000$|12500$|4000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

|Level    |9, 8, 10, 2|1 |5, 6, 7, 4, 3|
|---------|-----------|--|-------------|
|Max speed|40         |30|40           |


## Main attack : Scout

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 800ms
  * Retargeting offset: 8
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 0s
  * Target locking: No

|Level          |9  |8  |10 |2  |1  |5  |6  |7  |4  |3  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|350|330|380|220|200|260|280|300|250|230|


### Projectile

|Level                       |9      |8      |10     |2      |1      |5      |6      |7      |4      |3      |
|----------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|Displayed damage per second |330    |310    |360    |210    |190    |250    |270    |280    |240    |220    |
|Calculated damage per second|333.333|314.286|361.905|209.524|190.476|247.619|266.667|285.714|238.095|219.048|


  * Cannons per sequence: 1
  * Cliptime: 1.050s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Ressource generator, Storage, **(100)**: Droideka, Shield, **(75)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(50)**: Headquarters, Other building, Shield generator, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Scout

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: scotrper_emp-ani
  * Audio attack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: scotrper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: resource
  * Gun position: "scotrper_emp_rig_MASTER_MOVER/scotrper_emp_rig_joint1/scotrper_emp_rig_joint2/scotrper_emp_rig_joint27/scotrper_emp_rig_joint28/scotrper_emp_rig_joint29/scotrper_emp_rig_guMesh":1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 11.49,12.45,13.64
  * Icon closeup camera position: 2.23,1.18,9.57
  * Icon closeup lookat position: -0.05,2.58,-0.59
  * Icon lookat position: 0.2,1.71,0.02
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: Scout
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |9  |8  |10 |2  |1  |5  |6  |7  |4  |3  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|330|310|360|210|190|250|270|280|240|220|


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

|Level      |9     |8     |10    |2     |1     |5     |6     |7     |4     |3     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120309|120308|120310|120302|120301|120305|120306|120307|120304|120303|
|Point value|2.600 |2.400 |3     |1.200 |1     |1.800 |2     |2.200 |1.600 |1.400 |


