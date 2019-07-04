---
title: trptitleRebelSpiderlingDroid (RebelSpiderlingDroid)
category: unit
---

# trptitleRebelSpiderlingDroid (RebelSpiderlingDroid)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: No
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: vehicle

|Level |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------|----|----|----|----|----|----|----|----|----|----|----|
|Health|6440|6310|6180|6050|5930|5810|5690|5580|5470|5360|5250|


### Training stats

  * Training time: 0s
  * Training cost: Free

### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: Nothing

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

### Modifiers

#### Modifier "Spiderling auto death"

  * Spiderling auto death apply value as: relativePercent
  * Spiderling auto death buff ID: buffSpiderlingAutoDeath
  * Spiderling auto death duration: permanent
  * Spiderling auto death modifier: health
  * Spiderling auto death ms first proc: 10.250s
  * Spiderling auto death ms per proc: permanent
  * Spiderling auto death name: Spiderling auto death
  * Spiderling auto death stack: 1
  * Spiderling auto death target: self
  * Spiderling auto death value: -100.0%


#### Modifier "Spiderling invulnerable"

  * Spiderling invulnerable apply value as: absolutePercent
  * Spiderling invulnerable buff ID: buffSpiderlingInvulnerable
  * Spiderling invulnerable duration: 10s
  * Spiderling invulnerable modifier: defense
  * Spiderling invulnerable ms first proc: 0s
  * Spiderling invulnerable ms per proc: permanent
  * Spiderling invulnerable name: Spiderling invulnerable
  * Spiderling invulnerable stack: 1
  * Spiderling invulnerable target: self
  * Spiderling invulnerable value: 0


## Main attack : RebelSpiderlingDroid

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Flying infantry (70)**, **Infantry (70)**, **Support troop (70)**, _Droideka (60)_, _Flying vehicle (60)_, _Heavy infantry (60)_, _Heavy vehicle (60)_, _Light vehicle (60)_, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 600ms
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Reload time: 500ms
  * Retargeting offset: 4
  * Self-centered targeting: No
  * Shot count: 1
  * Shot delay: 960ms
  * Target locking: No

|Level          |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|3432|3348|3270|3192|3140|3088|3036|2984|2906|2847|2821|


### Projectile

|Level                       |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |3432|3348|3270|3192|3140|3088|3036|2984|2906|2847|2821|
|Calculated damage per second|1666|1625|1587|1549|1524|1499|1473|1448|1410|1382|1369|
|Calculated damage per cycle |3432|3348|3270|3192|3140|3088|3036|2984|2906|2847|2821|


  * Cannons per sequence: 1
  * Shooting cycle duration: 2.060s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(400)**: Flying infantry, Infantry, Infantry hero, Support troop, **(200)**: Heavy infantry, Heavy infantry hero, **(150)**: Flying vehicle, Light vehicle, Vehicule hero, **(125)**: Heavy vehicle, Heavy vehicule hero, **(100)**: Droideka, **(75)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 1

## Death attack : RebelSpiderlingDroidDeath

  * Death projectile delay: 0s
  * Death projectile distance: 0

  * Death attack splash damage percentages: 100,75,40,20

|Level                                  |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------------------------------|----|----|----|----|----|----|----|----|----|----|----|
|Death projectile damage                |5418|5232|5065|4895|4770|4646|4524|4403|4248|4131|4050|
|Death attack calculated damage per clip|5418|5232|5065|4895|4770|4646|4524|4403|4248|4131|4050|


  * Death attack cannons per sequence: 1
  * Death attack cliptime: 0s
  * Death attack directional: No
  * Death attack is deflectable: No
  * Death attack max speed: 18
  * Death attack damage multipliers: **(150)**: Death attack flying infantry, Death attack heavy infantry, Death attack infantry, Death attack infantry hero, **(100)**: Death attack droideka, Death attack flying vehicle, Death attack headquarters, Death attack heavy infantry hero, Death attack heavy vehicle, Death attack heavy vehicule hero, Death attack light vehicle, Death attack other building, Death attack ressource generator, Death attack shield, Death attack shield generator, Death attack storage, Death attack support troop, Death attack trap, Death attack turret, Death attack vehicule hero, Death attack wall
  * Death attack salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Death projectile: projectileRebelSpiderlingDroidDeath
  * Spawn apply buffs: buffSpiderlingAutoDeath1,buffSpiderlingInvulnerable1
  * Unit ID: RebelSpiderlingDroid

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: spiderlingdroid_rbl-ani
  * Audio attack: "sfx_attack_spiderlingdroid_01":30,"sfx_attack_spiderlingdroid_02":35,"sfx_attack_spiderlingdroid_03":35
  * Audio death: "sfx_death_spiderlingdroid_01":30,"sfx_death_spiderlingdroid_02":35,"sfx_death_spiderlingdroid_03":35
  * Audio placement: "sfx_placement_spiderlingdroid_01":30,"sfx_placement_spiderlingdroid_02":35,"sfx_placement_spiderlingdroid_03":35
  * Audio train: "sfx_placement_spiderlingdroid_01":30,"sfx_placement_spiderlingdroid_02":35,"sfx_placement_spiderlingdroid_03":35
  * Bundle name: spiderlingdroid_rbl-ani
  * Death attack arcs: No
  * Death attack hit spark: fx_atmosmig_hit
  * Death attack max scale: 100
  * Death attack muzzle flash: fx_mortar_muzzle_b_lrg
  * Death attack name: RebelSpiderlingDroidDeath
  * Death attack spin speed: 0
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Icon camera position: 7.54,14.62,18.95
  * Icon closeup camera position: 7.54,14.62,18.95
  * Icon closeup lookat position: -0.16,0.47,-0.33
  * Icon lookat position: -0.16,0.47,-0.33
  * Max scale: 100
  * Name: RebelSpiderlingDroid
  * Spiderling auto death audio ability event: "sfx_impact_rocket_01":35,"sfx_impact_rocket_02":35,"sfx_impact_rocket_03":30
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |11         |10                                                    |9                                                     |8                                                     |7                                                     |6                                                     |5                                                     |4                                                     |3                                                     |2                                                     |1                                                     |
|---------------------------|-----------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
|Displayed damage per second|3432       |3348                                                  |3270                                                  |3192                                                  |3140                                                  |3088                                                  |3036                                                  |2984                                                  |2906                                                  |2847                                                  |2821                                                  |
|Gun position               |(not found)|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|"atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Death attack seeks target: No
  * Death attack streams: no
  * Max scale: No
  * Point value: 1
  * Seeks target: Yes
  * Spiderling invulnerable cancel tags: damage
  * Spiderling invulnerable is refreshing: No
  * Spiderling invulnerable tags: invulnerable
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level |11         |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|------|-----------|------|------|------|------|------|------|------|------|------|------|
|Order |290011     |290010|290009|290008|290007|290006|290005|290004|290003|290002|290001|
|Splash|(not found)|0     |0     |0     |0     |0     |0     |0     |0     |0     |0     |


