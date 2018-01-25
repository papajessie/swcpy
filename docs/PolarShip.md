---
title: V-4X-D Ski Speeder (PolarShip)
category: unit
---

# V-4X-D Ski Speeder (PolarShip) — version 1119

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 6
  * Type: vehicle

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|10450|11090|11770|12490|13250|14090|14970|15920|16920|18000|


### Training stats

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|2m26s                         |2m27s                                 |2m29s                                 |2m32s                                 |2m36s                                 |2m41s                                 |2m46s                                 |2m50s                                 |2m55s                                 |3m                                     |
|Training cost|590$                          |610$                                  |630$                                  |680$                                  |760$                                  |830$                                  |950$                                  |1020$                                 |1070$                                 |1150$                                  |
|Building     |[Factory 1](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |1                |2                |3                |4                |5                |6                |7                |8                |9                 |10                |
|--------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|------------------|
|Upgrade requirements|32 data fragments|28 data fragments|30 data fragments|40 data fragments|50 data fragments|60 data fragments|70 data fragments|90 data fragments|120 data fragments|160 data fragments|


### Movement stats

  * Crushes walls: No
  * Flying unit: No
  * Max speed: 100
  * Propensity to go around obstacles: 15
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2

|Level       |1-6|7-10|
|------------|---|----|
|Acceleration|0  |8   |


## Main attack : T7-V Speederbike / Rebel Speeder Bike Upgrade

### Targeting

  * Attack shield border: No
  * Max attack range: 6
  * Min attack range: 0
  * New rotation speed: 3927
  * Target preference strength: 90
  * Target preferences: **Droideka (70)**, **Flying infantry (70)**, **Flying vehicle (70)**, **Heavy infantry (70)**, **Heavy vehicle (70)**, **Infantry (70)**, **Light vehicle (70)**, **Support troop (70)**, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0
  * Time between start of clip and first shot: 250ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1,2
  * Impact delay: 0s
  * New target on reload: No
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 300ms
  * Target locking: No

|Level          |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|460|480|495|510|545|680|720|740|765|790|


### Projectile

|Level                       |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |900 |930 |970 |1010|1050|1090|1460|1520|1580|1650|
|Calculated damage per second|836 |872 |900 |927 |990 |1236|1309|1345|1390|1436|
|Calculated damage per clip  |1380|1440|1485|1530|1635|2040|2160|2220|2295|2370|


  * Cannons per sequence: 2
  * Cliptime: 1.650s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Pass through shield: No
  * Salvos: 3

|Level             |1-6                                                                                                                                                                                                                                                                                                                                                    |7-10                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Damage multipliers|**(150)**: Flying infantry, Infantry, Infantry hero, Support troop, **(125)**: Heavy infantry, Heavy infantry hero, **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(75)**: Flying vehicle, Light vehicle, Vehicule hero, **(50)**: Heavy vehicle, Heavy vehicule hero|**(250)**: Flying infantry, Infantry, Support troop, **(225)**: Flying vehicle, Light vehicle, **(200)**: Heavy vehicle, **(175)**: Heavy infantry, **(100)**: Droideka, Heavy infantry hero, Heavy vehicule hero, Infantry hero, Vehicule hero, **(75)**: Wall, **(50)**: Headquarters, **(25)**: Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Trap|


## Internal stats

These stats internal to the system link different parts of data together.

  * Planet attachment id: troopPolarShipDustAttachment
  * Unit ID: PolarShip
  * Upgrade shard uid: shrd_troopPolarShip

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: polarspeeder_rbl-ani
  * Audio attack: "sfx_attack_polarship_01":33,"sfx_attack_polarship_02":33,"sfx_attack_polarship_03":34
  * Audio death: "sfx_death_polarship_01":33,"sfx_death_polarship_02":33,"sfx_death_polarship_03":34
  * Audio placement: "sfx_placement_polarship_01":33,"sfx_placement_polarship_02":33,"sfx_placement_polarship_03":34
  * Audio train: "sfx_ui_unitcomplete_polarship_01":50,"sfx_ui_unitcomplete_polarship_02":50
  * Buff asset offset: 0,1,0
  * Bullet: fx_blaster_beam_b_med
  * Bundle name: polarspeeder_rbl-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Gun position: speederbike_rbl_rig_MASTER_MOVER/speederbike_rbl_rig_locator_gun1:1,"speederbike_rbl_rig_MASTER_MOVER/speederbike_rbl_rig_locator_gun2":2
  * Hit spark: fx_blaster_hit_b_med
  * Icon camera position: 23.44,19.11,32.6
  * Icon lookat position: -0.66,1.95,-0.91
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_med
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: Yes
  * Unlocked by event: true
  * Unlocked by tournament: Yes

|Level                      |1               |2               |3               |4               |5               |6               |7                         |8                         |9                         |10                        |
|---------------------------|----------------|----------------|----------------|----------------|----------------|----------------|--------------------------|--------------------------|--------------------------|--------------------------|
|Displayed damage per second|900             |930             |970             |1010            |1050            |1090            |1460                      |1520                      |1580                      |1650                      |
|Name                       |T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|T7-V Speederbike|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|Rebel Speeder Bike Upgrade|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Target in range modifier: 1
  * Xp: 0

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|232001|232002|232003|232004|232005|232006|232007|232008|232009|232010|


