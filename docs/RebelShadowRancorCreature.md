---
title: Shadow Rancor (RebelShadowRancorCreature)
category: unit
---

# Shadow Rancor (RebelShadowRancorCreature)

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

|Level |1    |2    |3    |4    |5    |6    |7     |8     |9     |10    |
|------|-----|-----|-----|-----|-----|-----|------|------|------|------|
|Health|62208|68608|75008|81408|87808|94208|100608|107008|113408|119808|


### Training stats

  * Training time: 5s
  * Training cost: Free

### Upgrading stats

  * Upgrade time: 5s

|Level               |1                |2                |3                |4                 |5                 |6                 |7                 |8                 |9                 |10                |
|--------------------|-----------------|-----------------|-----------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|
|Upgrade requirements|32 data fragments|60 data fragments|90 data fragments|130 data fragments|180 data fragments|240 data fragments|310 data fragments|400 data fragments|520 data fragments|680 data fragments|


### Movement stats

  * Acceleration: 0
  * Crushes walls: Yes
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
  * Target preferences: **Other building (60)**, **Ressource generator (60)**, **Storage (60)**, Droideka (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Flying infantry (1), Flying vehicle (1), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 16

### Shooting

  * Animation delay: 960
  * Charge time: 500ms
  * Clip retargeting: Yes
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
|Damage per shot|5377|5930|6483|7036|7589|8142|8696|9249|9802|10355|


### Projectile

  * Splash damage percentages: 100,50

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |3038 |3413 |3788 |4163 |4538 |4913 |5288 |5663 |6038 |6410 |
|Calculated damage per second|2208 |2435 |2662 |2889 |3116 |3343 |3571 |3798 |4025 |4252 |
|Calculated damage per cycle |10754|11860|12966|14072|15178|16284|17392|18498|19604|20710|


  * Cannons per sequence: 2
  * Shooting cycle duration: 4.870s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(125)**: Trap, Turret, **(100)**: Droideka, Headquarters, Infantry, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Wall, **(75)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry hero, Light vehicle, Vehicule hero, **(0)**: Flying infantry, Flying vehicle
  * Pass through shield: Yes
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RebelShadowRancorCreature
  * Upgrade shard uid: shrd_troopRebelShadowRancorCreature

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: rancorshadow_neu-ani
  * Audio attack: "sfx_attack_creatures_rancor_1":33,"sfx_attack_creatures_rancor_2":33,"sfx_attack_creatures_rancor_3":34
  * Audio death: "sfx_death_creatures_rancor_1":100
  * Audio impact: "sfx_impact_creatures_rancor_1":33,"sfx_impact_creatures_rancor_2":33,"sfx_impact_creatures_rancor_3":34
  * Audio placement: "sfx_attack_creatures_rancor_1":35,"sfx_attack_creatures_rancor_2":35,"sfx_attack_creatures_rancor_3":30
  * Bundle name: rancorshadow_neu-ani
  * Deploy vfx: vfx_prestige_deploy_large_reb
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: building
  * Gun position: "rancor_neu_rig_MASTER_MOVER/"rancor_neu_rig_locator_gun1":1,"rancor_neu_rig_MASTER_MOVER/rancor_neu_rig_locator_gun2":2
  * Icon camera position: 34.42,44.79,49.58
  * Icon lookat position: -0.63,2.9,-1.73
  * Max scale: 100
  * Muzzle flash: fx_melee_headbutt_lrg
  * Name: Rancor Blaster
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|3038       |3413       |3788       |4163       |4538       |4913       |5288       |5663       |6038       |6410       |
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

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |290301|290302|290303|290304|290305|290306|290307|290308|290309|290310|
|Point value|20    |24    |28    |32    |36    |40    |44    |48    |52    |60    |


