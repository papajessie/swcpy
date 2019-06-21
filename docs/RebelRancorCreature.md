---
title: Rancor (RebelRancorCreature)
category: unit
---

# Rancor (RebelRancorCreature)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 20
  * Type: creature

|Level |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|99840|94506|89173|83840|78506|73173|67840|62506|57173|51840|


### Training stats

  * Training time: 3m50s
  * Training cost: 3250$

### Upgrading stats

  * Upgrade time: 5s

|Level               |10                |9                 |8                 |7                 |6                 |5                 |4                 |3                |2                |1                |
|--------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|-----------------|-----------------|-----------------|
|Upgrade requirements|680 data fragments|520 data fragments|400 data fragments|310 data fragments|240 data fragments|180 data fragments|130 data fragments|90 data fragments|60 data fragments|32 data fragments|


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

  * Animation delay: 960ms
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

|Level          |10   |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|-----|----|----|----|----|----|----|----|----|----|
|Damage per shot|10355|9802|9249|8696|8143|7590|7036|6483|5930|5377|


### Projectile

  * Splash damage percentages: 100,25

|Level                       |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |6410 |6038 |5663 |5288 |4913 |4538 |4163 |3788 |3413 |3038 |
|Calculated damage per second|4502 |4261 |4021 |3780 |3540 |3300 |3059 |2818 |2578 |2337 |
|Calculated damage per cycle |20710|19604|18498|17392|16286|15180|14072|12966|11860|10754|


  * Cannons per sequence: 2
  * Shooting cycle duration: 4.600s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Headquarters, Infantry, Infantry hero, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Wall, **(75)**: Heavy infantry, Heavy infantry hero, **(50)**: Light vehicle, Vehicule hero, **(25)**: Heavy vehicle, Heavy vehicule hero, **(0)**: Flying infantry, Flying vehicle
  * Pass through shield: No
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RebelRancorCreature
  * Upgrade shard uid: shrd_troopRebelRancorCreature

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
  * Deploy vfx: vfx_prestige_deploy_large_reb
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

|Level                      |10         |9          |8          |7          |6          |5          |4          |3          |2          |1          |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|6410       |6038       |5663       |5288       |4913       |4538       |4163       |3788       |3413       |3038       |
|Icon unlock position       |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|0,-0.75,0  |
|Icon unlock rotation       |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|0,-30,0    |
|Icon unlock scale          |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|0.6,0.6,0.6|


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

|Level      |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |290110|290109|290108|290107|290106|290105|290104|290103|290102|290101|
|Point value|60    |52    |48    |44    |40    |36    |32    |28    |24    |20    |


