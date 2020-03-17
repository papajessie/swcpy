---
title: LIN Demolitionmech (EmpireDemoDroid)
category: unit
---

# LIN Demolitionmech (EmpireDemoDroid)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Unit capacity: 4
  * Type: infantry

|Level |11   |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|32650|30950|28150|27050|25800|24250|22500|20500|18300|17250|16050|


### Training stats

  * Training time: 10s

|Level        |11                                      |10                                      |9                                      |8                                      |7                                      |6                                      |5                                      |4                                      |3                                      |2                                      |1                                |
|-------------|----------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|
|Training cost|250$                                    |230$                                    |210$                                   |200$                                   |170$                                   |150$                                   |130$                                   |110$                                   |90$                                    |70$                                    |50$                              |
|Building     |[Research Lab 11](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Barracks 1](empireBarracks.html)|


### Upgrading stats

|Level               |11                |10                |9                 |8                |7                |6                |5                |4                |3                |2                |1                |
|--------------------|------------------|------------------|------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
|Upgrade time        |10s               |0s                |0s                |0s               |0s               |0s               |0s               |0s               |0s               |0s               |0s               |
|Upgrade requirements|220 data fragments|160 data fragments|120 data fragments|90 data fragments|70 data fragments|60 data fragments|50 data fragments|40 data fragments|30 data fragments|28 data fragments|32 data fragments|


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

## Main attack : Demolition Droid Charge

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Other building (100)**, Headquarters (50), Ressource generator (50), Shield generator (50), Storage (50), Turret (50), Droideka (1), Flying infantry (1), Flying vehicle (1), Heavy infantry (1), Heavy infantry hero (1), Heavy vehicle (1), Heavy vehicule hero (1), Infantry (1), Infantry hero (1), Light vehicle (1), Shield (1), Support troop (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Animation delay: 1.370s
  * Charge time: 0s
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Reload time: 200ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 1
  * Shot delay: 2.366s
  * Target locking: No

|Level          |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|4636|4543|4388|4294|4243|4190|4150|4097|4046|3995|3953|


### Projectile

  * Splash damage percentages: 100,70,30,20

|Level                       |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |4570|4440|4140|3910|3740|3570|3430|3300|3180|3080|3020|
|Calculated damage per second|1240|1216|1174|1149|1135|1121|1110|1096|1082|1069|1058|
|Calculated damage per cycle |4636|4543|4388|4294|4243|4190|4150|4097|4046|3995|3953|


  * Cannons per sequence: 1
  * Shooting cycle duration: 3.736s
  * Directional: No
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(100)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Support troop, Vehicule hero, **(50)**: Droideka, **(40)**: Headquarters, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EmpireDemoDroid
  * Upgrade shard uid: shrd_troopEmpireDemoDroid

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: demolitiondroid_emp-ani
  * Audio attack: "sfx_attack_demodroid_01":50,"sfx_attack_demodroid_02":50
  * Audio death: "sfx_death_demodroid_01":50,"sfx_death_demodroid_02":50
  * Audio impact: "sfx_impact_demodroid_01":50,"sfx_impact_demodroid_02":50
  * Audio placement: "sfx_placement_demodroid_01":50,"sfx_placement_demodroid_02":50
  * Audio train: "sfx_ui_unitcomplete_demodroid_01":50,"sfx_ui_unitcomplete_demodroid_02":50
  * Bundle name: demolitiondroid_emp-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: building
  * Hit spark: fx_demodroid_hit_lrg
  * Icon camera position: 8.79,9.6,23.6
  * Icon closeup camera position: 5.71,4.11,14
  * Icon closeup lookat position: -0.29,0.93,-0.61
  * Icon lookat position: -0.31,1.28,-0.61
  * Max scale: 100
  * Name: Demolition Droid Charge
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: Yes
  * Unlocked by event: true
  * Unlocked by tournament: Yes

|Level                      |11                           |10         |9          |8          |7          |6          |5          |4          |3          |2          |1          |
|---------------------------|-----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |vfx_prestige_deploy_small_emp|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|4570                         |4440       |4140       |3910       |3740       |3570       |3430       |3300       |3180       |3080       |3020       |
|Prestige                   |true                         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |11   |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |61411|61410|61409|61408|61407|61406|61405|61404|61403|61402|61401|
|Point value|3    |3    |2.600|2.400|2.200|2    |1.800|1.600|1.400|1.200|1    |


