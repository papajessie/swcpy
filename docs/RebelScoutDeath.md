---
title: Scout Undead Trooper (RebelScoutDeath)
category: unit
---

# Scout Undead Trooper (RebelScoutDeath) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: No
  * Role: Looter
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: infantry

|Level |10  |6   |5   |4   |2   |1  |9   |8   |7   |3   |
|------|----|----|----|----|----|---|----|----|----|----|
|Health|2700|1800|1620|1440|1080|900|2340|2160|1980|1260|


### Training stats

|Level        |10                                     |6                                     |5                                     |4                                     |2                                     |1                                |9                                     |8                                     |7                                     |3                                     |
|-------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|30s                                    |26s                                   |25s                                   |24s                                   |22s                                   |21s                              |29s                                   |28s                                   |27s                                   |23s                                   |
|Training cost|230$                                   |150$                                  |130$                                  |110$                                  |70$                                   |50$                              |210$                                  |190$                                  |170$                                  |90$                                   |
|Building     |[Research Lab 10](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Barracks 10](rebelBarracks.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|


### Upgrading stats

|Level               |10      |6      |5     |4     |2    |1   |9       |8      |7      |3    |
|--------------------|--------|-------|------|------|-----|----|--------|-------|-------|-----|
|Upgrade time        |1w1d    |1d     |8h    |3h30m |15m  |0s  |5d      |3d12h  |2d     |1h   |
|Upgrade requirements|1750000$|100000$|25000$|12500$|1500$|600$|1000000$|320000$|160000$|4000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : ScoutDeath

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy infantry hero (50), Heavy vehicle (50), Heavy vehicule hero (50), Infantry (50), Infantry hero (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Vehicule hero (50), Wall (1), Trap (0)
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

|Level          |10 |6  |5  |4  |2  |1  |9  |8  |7  |3  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|378|252|227|202|152|126|328|303|278|177|


### Projectile

|Level                       |10 |6  |5      |4      |2      |1  |9      |8      |7      |3      |
|----------------------------|---|---|-------|-------|-------|---|-------|-------|-------|-------|
|Displayed damage per second |360|240|216    |192    |144    |120|312    |288    |264    |168    |
|Calculated damage per second|360|240|216.190|192.381|144.762|120|312.381|288.571|264.762|168.571|


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

  * Unit ID: RebelScoutDeath

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: scotrper_dth-ani
  * Audio attack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * Audio death: "sfx_death_deathtrooper_1":35,"sfx_death_deathtrooper_2":35,"sfx_death_deathtrooper_3":30
  * Audio placement: "sfx_placement_deathtrooper_1":35,"sfx_placement_deathtrooper_2":35,"sfx_placement_deathtrooper_3":30
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: scotrper_dth-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: resource
  * Gun position: scotrper_dth_rig_MASTER_MOVER/scotrper_dth_rig_locator_gun_Rt:1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 10.84,12.06,13.07
  * Icon closeup camera position: 4.94,-0.46,8
  * Icon closeup lookat position: -0.15,2.51,-0.51
  * Icon lookat position: 0.06,1.74,0.02
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: ScoutDeath
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10 |6  |5  |4  |2  |1  |9  |8  |7  |3  |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|360|240|216|192|144|120|312|288|264|168|


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

|Level      |10    |6     |5     |4     |2     |1     |9     |8     |7     |3     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |233410|233406|233405|233404|233402|233401|233409|233408|233407|233403|
|Point value|3     |2     |1.800 |1.600 |1.200 |1     |2.600 |2.400 |2.200 |1.400 |


