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

|Level |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|41250|38550|35900|33150|30600|28050|25600|23300|21150|19600|


### Training stats

  * Training time: 10s
  * Training cost: 1 Con.

|Level   |10                                     |9                                     |8                                     |7                                     |6                                     |5                                     |4                                     |3                                     |2                                     |1                                       |
|--------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|----------------------------------------|
|Building|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Cantina 1](rebelContrabandCantina.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |10                |9                 |8                |7                |6                |5                |4                |3                |2                |1                |
|--------------------|------------------|------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
|Upgrade requirements|160 data fragments|120 data fragments|90 data fragments|70 data fragments|60 data fragments|50 data fragments|40 data fragments|30 data fragments|28 data fragments|32 data fragments|


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

  * Animation delay: 200ms
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

|Level               |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|--------------------|----|----|----|----|----|----|----|----|----|----|
|Special data 2 value|45  |43  |41  |38  |36  |34  |32  |29  |27  |25  |
|Special data 3 value|3200|3000|2800|2650|2450|2300|2100|1950|1750|1600|


### Projectile

  * Displayed damage per second: 1
  * Calculated damage per second: 0
  * Calculated damage per cycle: 1

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

|Level                                 |10 |9      |8      |7      |6      |5      |4      |3      |2      |1  |
|--------------------------------------|---|-------|-------|-------|-------|-------|-------|-------|-------|---|
|Corruption self destruct ms first proc|45s|42.778s|40.556s|38.333s|36.111s|33.889s|31.667s|29.444s|27.222s|25s|



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

|Level                                          |10                                                            |9                                                            |8                                                            |7                                                            |6                                                            |5                                                            |4                                                            |3                                                            |2                                                            |1                                                            |
|-----------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
|Sum rebel turret corruptor phtm summon visitors|["trp_title_RebelP006Phantom" level 10](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 9](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 8](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 7](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 6](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 5](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 4](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 3](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 2](RebelP006Phantom.html)|["trp_title_RebelP006Phantom" level 1](RebelP006Phantom.html)|


  * Sum rebel turret corruptor phtm summon die with summoner: Yes
  * Sum rebel turret corruptor phtm summon max proc: 29
  * Sum rebel turret corruptor phtm summon same team: Yes
  * Sum rebel turret corruptor phtm summon target summoner: No
  * Sum rebel turret corruptor phtm summon visitor type: Troop

|Level                                              |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|---------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Sum rebel turret corruptor phtm summon spawn points|0,0,9|0,0,8|0,0,7|0,0,6|0,0,5|0,0,4|0,0,3|0,0,2|0,0,1|0,0,0|


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

|Level                                     |10                                                                                  |9                                                                                 |8                                                                                 |7                                                                                 |6                                                                                 |5                                                                                 |4                                                                                 |3                                                                                 |2                                                                                 |1                                                                                 |
|------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|Apply buffs                               |buffTurretCorruption1,buffCorruptionSelfDestruct10,buffSumRebelTurretCorruptorPhtm10|buffTurretCorruption1,buffCorruptionSelfDestruct9,buffSumRebelTurretCorruptorPhtm9|buffTurretCorruption1,buffCorruptionSelfDestruct8,buffSumRebelTurretCorruptorPhtm8|buffTurretCorruption1,buffCorruptionSelfDestruct7,buffSumRebelTurretCorruptorPhtm7|buffTurretCorruption1,buffCorruptionSelfDestruct6,buffSumRebelTurretCorruptorPhtm6|buffTurretCorruption1,buffCorruptionSelfDestruct5,buffSumRebelTurretCorruptorPhtm5|buffTurretCorruption1,buffCorruptionSelfDestruct4,buffSumRebelTurretCorruptorPhtm4|buffTurretCorruption1,buffCorruptionSelfDestruct3,buffSumRebelTurretCorruptorPhtm3|buffTurretCorruption1,buffCorruptionSelfDestruct2,buffSumRebelTurretCorruptorPhtm2|buffTurretCorruption1,buffCorruptionSelfDestruct1,buffSumRebelTurretCorruptorPhtm1|
|Sum rebel turret corruptor phtm details   |sumRebelTurretCorruptorPhtm10                                                       |sumRebelTurretCorruptorPhtm9                                                      |sumRebelTurretCorruptorPhtm8                                                      |sumRebelTurretCorruptorPhtm7                                                      |sumRebelTurretCorruptorPhtm6                                                      |sumRebelTurretCorruptorPhtm5                                                      |sumRebelTurretCorruptorPhtm4                                                      |sumRebelTurretCorruptorPhtm3                                                      |sumRebelTurretCorruptorPhtm2                                                      |sumRebelTurretCorruptorPhtm1                                                      |
|Sum rebel turret corruptor phtm summon uid|sumRebelTurretCorruptorPhtm10                                                       |sumRebelTurretCorruptorPhtm9                                                      |sumRebelTurretCorruptorPhtm8                                                      |sumRebelTurretCorruptorPhtm7                                                      |sumRebelTurretCorruptorPhtm6                                                      |sumRebelTurretCorruptorPhtm5                                                      |sumRebelTurretCorruptorPhtm4                                                      |sumRebelTurretCorruptorPhtm3                                                      |sumRebelTurretCorruptorPhtm2                                                      |sumRebelTurretCorruptorPhtm1                                                      |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: p006_con-ani
  * Audio attack: "sfx_attack_p006droid_01":50,"sfx_attack_p006droid_02":50
  * Audio death: "sfx_death_p006droid_01":50,"sfx_death_p006droid_02":50
  * Audio placement: "sfx_placement_p006droid_01":50,"sfx_placement_p006droid_02":50
  * Audio train: "sfx_ui_unitcomplete_p006droid_01":50,"sfx_ui_unitcomplete_p006droid_02":50
  * Bundle name: p006_con-ani
  * Displayed damage per second: 1
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

|Level            |2-10       |1             |
|-----------------|-----------|--------------|
|Icon unlock scale|(not found)|1.75,1.75,1.75|


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

|Level      |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |240810|240809|240808|240807|240806|240805|240804|240803|240802|240801|
|Point value|3     |2.600 |2.400 |2.200 |2     |1.800 |1.600 |1.400 |1.200 |1     |


