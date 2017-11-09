---
title: Undead Trooper (EmpireStormDeath)
category: unit
---

# Undead Trooper (EmpireStormDeath) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: No
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: infantry

|Level |6   |4   |10  |5   |2   |1   |7   |8   |3   |9   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2400|1920|3600|2160|1560|1300|2640|2880|1680|3120|


### Training stats

|Level        |6                                      |4                                      |10                                      |5                                      |2                                      |1                                 |7                                      |8                                      |3                                      |9                                      |
|-------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|----------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|26s                                    |24s                                    |30s                                     |25s                                    |22s                                    |20s                               |27s                                    |28s                                    |23s                                    |29s                                    |
|Training cost|150$                                   |110$                                   |230$                                    |130$                                   |70$                                    |50$                               |170$                                   |190$                                   |90$                                    |210$                                   |
|Building     |[Research Lab 6](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Barracks 10](empireBarracks.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|


### Upgrading stats

|Level               |6      |4     |10      |5     |2    |1   |7      |8      |3    |9       |
|--------------------|-------|------|--------|------|-----|----|-------|-------|-----|--------|
|Upgrade time        |1d     |3h30m |1w1d    |8h    |15m  |0s  |2d     |3d12h  |1h   |5d      |
|Upgrade requirements|100000$|12500$|1750000$|25000$|1500$|600$|160000$|320000$|4000$|1000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : StormDeath

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy infantry hero (50)**, **Heavy vehicle (50)**, **Heavy vehicule hero (50)**, **Infantry (50)**, **Infantry hero (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, **Vehicule hero (50)**, Wall (1), Trap (0)
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
  * Shot count: 1
  * Time between shots: 200ms
  * Target locking: No

|Level          |6  |4  |10 |5  |2  |1  |7  |8  |3  |9  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|260|208|390|234|169|141|286|312|182|338|


### Projectile

|Level                       |6  |4  |10 |5  |2  |1  |7  |8  |3  |9  |
|----------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second |260|208|390|234|169|141|286|312|182|338|
|Calculated damage per second|260|208|390|234|169|141|286|312|182|338|


  * Cannons per sequence: 1
  * Cliptime: 1s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 15
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EmpireStormDeath

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: stotrper_dth-ani
  * Audio attack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * Audio death: "sfx_death_deathtrooper_1":35,"sfx_death_deathtrooper_2":35,"sfx_death_deathtrooper_3":30
  * Audio placement: "sfx_placement_deathtrooper_1":35,"sfx_placement_deathtrooper_2":35,"sfx_placement_deathtrooper_3":30
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: stotrper_dth-ani
  * Death animation: buffFireBurn:15
  * Decal asset name: troop_stotrper_emp
  * Decal bundle name: troop_stotrper_emp
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: stotrper_dth_rig_MASTER_MOVER/stotrper_dth_rig_locator_gun:1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 11.27,12.43,13.71
  * Icon closeup camera position: 4.5,4.27,7.56
  * Icon closeup lookat position: -0.5,2.49,-0.78
  * Icon lookat position: 0.05,1.69,0.14
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: StormDeath
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |6  |4  |10 |5  |2  |1  |7  |8  |3  |9  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|260|208|390|234|169|141|286|312|182|338|


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

|Level      |6     |4     |10    |5     |2     |1     |7     |8     |3     |9     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |132906|132904|132910|132905|132902|132901|132907|132908|132903|132909|
|Point value|2     |1.600 |3     |1.800 |1.200 |1     |2.200 |2.400 |1.400 |2.600 |


