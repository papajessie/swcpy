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

|Level |9   |5   |2   |10  |7   |4   |6   |8   |1   |3   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|3120|2160|1560|3600|2640|1920|2400|2880|1300|1680|


### Training stats

|Level        |9                                      |5                                      |2                                      |10                                      |7                                      |4                                      |6                                      |8                                      |1                                |3                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|---------------------------------------|
|Training time|29s                                    |25s                                    |22s                                    |30s                                     |27s                                    |24s                                    |26s                                    |28s                                    |20s                              |23s                                    |
|Training cost|210$                                   |130$                                   |70$                                    |230$                                    |170$                                   |110$                                   |150$                                   |200$                                   |50$                              |90$                                    |
|Building     |[Research Lab 9](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Barracks 1](empireBarracks.html)|[Research Lab 3](empireOffenseLab.html)|


### Upgrading stats

|Level               |9       |5     |2    |10      |7      |4     |6      |8      |1   |3    |
|--------------------|--------|------|-----|--------|-------|------|-------|-------|----|-----|
|Upgrade time        |5d      |8h    |15m  |1w1d    |2d     |3h30m |1d     |3d12h  |0s  |1h   |
|Upgrade requirements|1000000$|25000$|1500$|1750000$|160000$|12500$|100000$|320000$|600$|4000$|


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

|Level          |9  |5  |2  |10 |7  |4  |6  |8  |1  |3  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|338|234|169|390|286|208|260|312|141|182|


### Projectile

|Level                       |9      |5      |2      |10     |7      |4      |6      |8      |1      |3  |
|----------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|---|
|Displayed damage per second |724    |501    |362    |835    |612    |445    |557    |668    |302    |390|
|Calculated damage per second|724.286|501.429|362.143|835.714|612.857|445.714|557.143|668.571|302.143|390|


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

|Level                      |9  |5  |2  |10 |7  |4  |6  |8  |1  |3  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|724|501|362|835|612|445|557|668|302|390|


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

|Level      |9     |5     |2     |10    |7     |4     |6     |8     |1     |3     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120109|120105|120102|120110|120107|120104|120106|120108|120101|120103|
|Point value|2.600 |1.800 |1.200 |3     |2.200 |1.600 |2     |2.400 |1     |1.400 |


