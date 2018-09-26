---
title: A-LT Turret Slicer (RebelP006Droid)
category: unit
---

# A-LT Turret Slicer (RebelP006Droid)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Can be given: Yes
  * Role: Destroyer
  * Unit capacity: 13
  * Type: mercenary

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|19600|21150|23300|25600|28050|30600|33150|35900|38550|41250|


### Training stats

|Level        |1                                       |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|----------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|6m                                      |6m30s                                 |7m10s                                 |7m40s                                 |8m20s                                 |9m                                    |9m30s                                 |10m10s                                |10m40s                                |11m20s                                 |
|Training cost|50 Con.                                 |60 Con.                               |120 Con.                              |210 Con.                              |340 Con.                              |480 Con.                              |640 Con.                              |810 Con.                              |970 Con.                              |1100 Con.                              |
|Building     |[Cantina 1](rebelContrabandCantina.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |1                |2                |3                |4                |5                |6                |7                |8                |9                 |10                |
|--------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|------------------|
|Upgrade requirements|32 data fragments|28 data fragments|30 data fragments|40 data fragments|50 data fragments|60 data fragments|70 data fragments|90 data fragments|120 data fragments|160 data fragments|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Ignores walls: Yes
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : Turret Corruptor

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (100)**, Droideka (0), Flying infantry (0), Flying vehicle (0), Headquarters (0), Heavy infantry (0), Heavy infantry hero (0), Heavy vehicle (0), Heavy vehicule hero (0), Infantry (0), Infantry hero (0), Light vehicle (0), Other building (0), Ressource generator (0), Shield (0), Shield generator (0), Storage (0), Support troop (0), Trap (0), Vehicule hero (0), Wall (0)
  * View range: 12

### Shooting

  * Animation delay: 200
  * Charge time: 0s
  * Clip retargeting: No
  * Special data 2 title: Turret Time to Self-Destruct:
  * Special data 3 title: Overload Burst Damage:
  * Damage per shot: 1
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Reload time: 2m
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 1
  * Shot delay: 0s
  * Target locking: No

|Level               |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|--------------------|----|----|----|----|----|----|----|----|----|----|
|Special data 2 value|25  |27  |29  |32  |34  |36  |38  |41  |43  |45  |
|Special data 3 value|1600|1750|1950|2100|2300|2450|2650|2800|3000|3200|


### Projectile

  * Calculated damage per second: 0
  * Calculated damage per cycle: 1

|Level                      |1-9        |10|
|---------------------------|-----------|--|
|Displayed damage per second|(not found)|1 |


  * Cannons per sequence: 1
  * Shooting cycle duration: 2m200ms
  * Directional: No
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(100)**: Turret, **(0)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Vehicule hero, Wall
  * Pass through shield: Yes
  * Salvos: 1

#### Modifier "Corruption self destruct"

  * Corruption self destruct apply value as: relativePercent
  * Corruption self destruct buff ID: buffCorruptionSelfDestruct
  * Corruption self destruct duration: permanent
  * Corruption self destruct modifier: health
  * Corruption self destruct ms per proc: permanent
  * Corruption self destruct name: Corruption self destruct
  * Corruption self destruct stack: 1
  * Corruption self destruct target: enemies
  * Corruption self destruct value: -100.0%

|Level                                 |1  |2      |3      |4      |5      |6      |7      |8      |9      |10 |
|--------------------------------------|---|-------|-------|-------|-------|-------|-------|-------|-------|---|
|Corruption self destruct ms first proc|25s|27.222s|29.444s|31.667s|33.889s|36.111s|38.333s|40.556s|42.778s|45s|



#### Modifier "Sum rebel turret corruptor phtm"

  * Sum rebel turret corruptor phtm apply value as: absolute
  * Sum rebel turret corruptor phtm buff ID: buffSumRebelTurretCorruptorPhtm
  * Sum rebel turret corruptor phtm duration: permanent
  * Sum rebel turret corruptor phtm modifier: summon
  * Sum rebel turret corruptor phtm ms first proc: 100ms
  * Sum rebel turret corruptor phtm ms per proc: permanent
  * Sum rebel turret corruptor phtm name: Sum rebel turret corruptor phtm
  * Sum rebel turret corruptor phtm stack: 1
  * Sum rebel turret corruptor phtm target: enemies
  * Sum rebel turret corruptor phtm value: 1

|Level                                          |1                                                            |2                                                            |3                                                            |4                                                            |5                                                            |6                                                            |7                                                            |8                                                            |9                                                            |10                                                            |
|-----------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
|Sum rebel turret corruptor phtm summon visitors|["trp_title_RebelP006Phantom" level 1](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 2](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 3](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 4](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 5](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 6](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 7](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 8](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 9](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 10](RebelP006Phantom.html)|


  * Sum rebel turret corruptor phtm summon die with summoner: Yes
  * Sum rebel turret corruptor phtm summon max proc: 29
  * Sum rebel turret corruptor phtm summon same team: Yes
  * Sum rebel turret corruptor phtm summon target summoner: No
  * Sum rebel turret corruptor phtm summon visitor type: Troop

|Level                                              |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|---------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Sum rebel turret corruptor phtm summon spawn points|0,0,0|0,0,1|0,0,2|0,0,3|0,0,4|0,0,5|0,0,6|0,0,7|0,0,8|0,0,9|


#### Modifier "Turret corruption"

  * Turret corruption apply value as: absolute
  * Turret corruption buff ID: buffTurretCorruption
  * Turret corruption duration: permanent
  * Turret corruption modifier: switchTeam
  * Turret corruption ms first proc: 50ms
  * Turret corruption ms per proc: permanent
  * Turret corruption damage multipliers: **(100)**: Turret corruption turret, **(0)**: Turret corruption droideka, Turret corruption flying infantry, Turret corruption flying vehicle, Turret corruption headquarters, Turret corruption heavy infantry, Turret corruption heavy infantry hero, Turret corruption heavy vehicle, Turret corruption heavy vehicule hero, Turret corruption infantry, Turret corruption infantry hero, Turret corruption light vehicle, Turret corruption other building, Turret corruption ressource generator, Turret corruption shield, Turret corruption shield generator, Turret corruption storage, Turret corruption support troop, Turret corruption trap, Turret corruption vehicule hero, Turret corruption wall
  * Turret corruption name: Turret corruption
  * Turret corruption stack: 1
  * Turret corruption target: enemies
  * Turret corruption value: 0


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RebelP006Droid
  * Upgrade shard uid: shrd_troopRebelP006Droid

|Level                                     |1                                                                                 |2                                                                                 |3                                                                                 |4                                                                                 |5                                                                                 |6                                                                                 |7                                                                                 |8                                                                                 |9                                                                                 |10                                                                                  |
|------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
|Apply buffs                               |buffTurretCorruption1,buffCorruptionSelfDestruct1,buffSumRebelTurretCorruptorPhtm1|buffTurretCorruption1,buffCorruptionSelfDestruct2,buffSumRebelTurretCorruptorPhtm2|buffTurretCorruption1,buffCorruptionSelfDestruct3,buffSumRebelTurretCorruptorPhtm3|buffTurretCorruption1,buffCorruptionSelfDestruct4,buffSumRebelTurretCorruptorPhtm4|buffTurretCorruption1,buffCorruptionSelfDestruct5,buffSumRebelTurretCorruptorPhtm5|buffTurretCorruption1,buffCorruptionSelfDestruct6,buffSumRebelTurretCorruptorPhtm6|buffTurretCorruption1,buffCorruptionSelfDestruct7,buffSumRebelTurretCorruptorPhtm7|buffTurretCorruption1,buffCorruptionSelfDestruct8,buffSumRebelTurretCorruptorPhtm8|buffTurretCorruption1,buffCorruptionSelfDestruct9,buffSumRebelTurretCorruptorPhtm9|buffTurretCorruption1,buffCorruptionSelfDestruct10,buffSumRebelTurretCorruptorPhtm10|
|Sum rebel turret corruptor phtm details   |sumRebelTurretCorruptorPhtm1                                                      |sumRebelTurretCorruptorPhtm2                                                      |sumRebelTurretCorruptorPhtm3                                                      |sumRebelTurretCorruptorPhtm4                                                      |sumRebelTurretCorruptorPhtm5                                                      |sumRebelTurretCorruptorPhtm6                                                      |sumRebelTurretCorruptorPhtm7                                                      |sumRebelTurretCorruptorPhtm8                                                      |sumRebelTurretCorruptorPhtm9                                                      |sumRebelTurretCorruptorPhtm10                                                       |
|Sum rebel turret corruptor phtm summon uid|sumRebelTurretCorruptorPhtm1                                                      |sumRebelTurretCorruptorPhtm2                                                      |sumRebelTurretCorruptorPhtm3                                                      |sumRebelTurretCorruptorPhtm4                                                      |sumRebelTurretCorruptorPhtm5                                                      |sumRebelTurretCorruptorPhtm6                                                      |sumRebelTurretCorruptorPhtm7                                                      |sumRebelTurretCorruptorPhtm8                                                      |sumRebelTurretCorruptorPhtm9                                                      |sumRebelTurretCorruptorPhtm10                                                       |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: p006_con-ani
  * Audio attack: "sfx_attack_p006droid_01":50,"sfx_attack_p006droid_02":50
  * Audio death: "sfx_death_p006droid_01":50,"sfx_death_p006droid_02":50
  * Audio placement: "sfx_placement_p006droid_01":50,"sfx_placement_p006droid_02":50
  * Audio train: "sfx_ui_unitcomplete_p006droid_01":50,"sfx_ui_unitcomplete_p006droid_02":50
  * Bundle name: p006_con-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Icon camera position: 5.48,11,13.78
  * Icon closeup camera position: 3.21,7.17,7.93
  * Icon closeup lookat position: -0.23,0.95,-0.58
  * Icon lookat position: -0.19,0.61,-0.39
  * Info UI type: Custom
  * Muzzle flash: fx_r2d2_hit_small
  * Name: Turret Corruptor
  * Special data 2 unit: s
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Turret corruption asset profile: vfxProfile_corrupt
  * Unlocked by campaign: Yes
  * Unlocked by event: true
  * Unlocked by tournament: Yes

|Level                      |1             |2-9        |10         |
|---------------------------|--------------|-----------|-----------|
|Displayed damage per second|(not found)   |(not found)|1          |
|Icon unlock scale          |1.75,1.75,1.75|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Corruption self destruct tags: switchTeam
  * Max scale: No
  * Seeks target: No
  * Streams: no
  * Strict cool down: Yes
  * Sum rebel turret corruptor phtm tags: switchTeam
  * Target in range modifier: 1
  * Turret corruption tags: switchTeam
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |240801|240802|240803|240804|240805|240806|240807|240808|240809|240810|
|Point value|1     |1.200 |1.400 |1.600 |1.800 |2     |2.200 |2.400 |2.600 |3     |


