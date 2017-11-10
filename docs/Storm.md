---
title: Stormtrooper (Storm)
category: unit
---

# Stormtrooper (Storm) — version 1098

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
  * Unit capacity: 1
  * Type: infantry

|Level |8   |6   |5   |4   |7   |9   |10  |3   |2   |1   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2880|2400|2160|1920|2640|3120|3600|1680|1560|1300|


### Training stats

|Level        |8                                      |6                                      |5                                      |4                                      |7                                      |9                                      |10                                      |3                                      |2                                      |1                                |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|
|Training time|28s                                    |26s                                    |25s                                    |24s                                    |27s                                    |29s                                    |30s                                     |23s                                    |22s                                    |20s                              |
|Training cost|200$                                   |150$                                   |130$                                   |110$                                   |170$                                   |210$                                   |230$                                    |90$                                    |70$                                    |50$                              |
|Building     |[Research Lab 8](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Barracks 1](empireBarracks.html)|


### Upgrading stats

|Level               |8      |6      |5     |4     |7      |9       |10      |3    |2    |1   |
|--------------------|-------|-------|------|------|-------|--------|--------|-----|-----|----|
|Upgrade time        |3d12h  |1d     |8h    |3h30m |2d     |5d      |1w1d    |1h   |15m  |0s  |
|Upgrade requirements|320000$|100000$|25000$|12500$|160000$|1000000$|1750000$|4000$|1500$|600$|


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

## Main attack : Storm

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 200ms
  * Target locking: No

|Level          |8  |6  |5  |4  |7  |9  |10 |3  |2  |1  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|312|260|234|208|286|338|390|182|169|141|


### Projectile

|Level                       |8      |6      |5      |4      |7      |9      |10     |3  |2      |1      |
|----------------------------|-------|-------|-------|-------|-------|-------|-------|---|-------|-------|
|Displayed damage per second |668    |557    |501    |445    |612    |724    |835    |390|362    |302    |
|Calculated damage per second|668.571|557.143|501.429|445.714|612.857|724.286|835.714|390|362.143|302.143|


  * Cannons per sequence: 1
  * Cliptime: 1.400s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 15
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Storm

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: stotrper_emp-ani
  * Audio attack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: stotrper_emp-ani
  * Death animation: buffFireBurn:15
  * Decal asset name: troop_stotrper_emp
  * Decal bundle name: troop_stotrper_emp
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Gun position: "stotrper_emp_rig_MASTER_MOVER/stotrper_emp_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 12.13,10.63,15.32
  * Icon closeup camera position: 1.93,1.69,9.65
  * Icon closeup lookat position: -0.01,2.73,-0.82
  * Icon lookat position: 0.02,1.69,0
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: Storm
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |8  |6  |5  |4  |7  |9  |10 |3  |2  |1  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|668|557|501|445|612|724|835|390|362|302|


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

|Level      |8     |6     |5     |4     |7     |9     |10    |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120108|120106|120105|120104|120107|120109|120110|120103|120102|120101|
|Point value|2.400 |2     |1.800 |1.600 |2.200 |2.600 |3     |1.400 |1.200 |1     |


