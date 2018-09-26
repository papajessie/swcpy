---
title: Rancor (EmpireRancorCreature)
category: unit
---

# Rancor (EmpireRancorCreature)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 20
  * Type: creature

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|51840|57173|62506|67840|73173|78506|83840|89173|94506|99840|


### Training stats

  * Training time: 3m50s
  * Training cost: 3250$

### Upgrading stats

  * Upgrade time: 5s

|Level               |1                |2                |3                |4                 |5                 |6                 |7                 |8                 |9                 |10                |
|--------------------|-----------------|-----------------|-----------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|
|Upgrade requirements|32 data fragments|60 data fragments|90 data fragments|130 data fragments|180 data fragments|240 data fragments|310 data fragments|400 data fragments|520 data fragments|680 data fragments|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 1
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : Rancor Blaster

### Targeting

  * Attack shield border: No
  * Max attack range: 3
  * Min attack range: 0
  * New rotation speed: 2000
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Headquarters (40), Flying infantry (1), Flying vehicle (1), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 16

### Shooting

  * Animation delay: 960
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 2,1
  * Impact delay: 960ms
  * Can shoot over walls: No
  * Reload time: 1.910s
  * Retargeting offset: 8
  * Self-centered targeting: No
  * Shot count: 2
  * Shot delay: 270ms
  * Target locking: No

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10   |
|---------------|----|----|----|----|----|----|----|----|----|-----|
|Damage per shot|5377|5930|6483|7036|7590|8143|8696|9249|9802|10355|


### Projectile

  * Splash damage percentages: 100,25

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |3038 |3413 |3788 |4163 |4538 |4913 |5288 |5663 |6038 |630  |
|Calculated damage per second|2208 |2435 |2662 |2889 |3117 |3344 |3571 |3798 |4025 |4252 |
|Calculated damage per cycle |10754|11860|12966|14072|15180|16286|17392|18498|19604|20710|


  * Cannons per sequence: 2
  * Shooting cycle duration: 4.870s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Headquarters, Infantry, Infantry hero, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Wall, **(75)**: Heavy infantry, Heavy infantry hero, **(50)**: Light vehicle, Vehicule hero, **(25)**: Heavy vehicle, Heavy vehicule hero, **(0)**: Flying infantry, Flying vehicle
  * Pass through shield: No
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EmpireRancorCreature
  * Upgrade shard uid: shrd_troopEmpireRancorCreature

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: rancor_neu-ani
  * Audio attack: "sfx_attack_creatures_rancor_1":33,"sfx_attack_creatures_rancor_2":33,"sfx_attack_creatures_rancor_3":34
  * Audio death: "sfx_death_creatures_rancor_1":100
  * Audio impact: "sfx_impact_creatures_rancor_1":33,"sfx_impact_creatures_rancor_2":33,"sfx_impact_creatures_rancor_3":34
  * Audio placement: "sfx_attack_creatures_rancor_1":35,"sfx_attack_creatures_rancor_2":35,"sfx_attack_creatures_rancor_3":30
  * Buff asset offset: 0.00,4.30,0.00
  * Bundle name: rancor_neu-ani
  * Death animation: buffFireBurn:15
  * Deploy vfx: vfx_prestige_deploy_large_emp
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "rancor_neu_rig_MASTER_MOVER/"rancor_neu_rig_locator_gun1":1,"rancor_neu_rig_MASTER_MOVER/rancor_neu_rig_locator_gun2":2
  * Icon camera position: 38.76,41.86,47.24
  * Icon lookat position: -0.95,2.74,-1.82
  * Max scale: 100
  * Muzzle flash: fx_melee_headbutt_lrg
  * Name: Rancor Blaster
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|3038       |3413       |3788       |4163       |4538       |4913       |5288       |5663       |6038       |630        |
|Icon unlock position       |0,-0.75,0  |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation       |0,-30,0    |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |0.6,0.6,0.6|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |90101|90102|90103|90104|90105|90106|90107|90108|90109|90110|
|Point value|20   |24   |28   |32   |36   |40   |44   |48   |52   |60   |


