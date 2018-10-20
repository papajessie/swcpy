---
title: Rage Rancor (RebelRageRancorCreature)
category: unit
---

# Rage Rancor (RebelRageRancorCreature)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 50
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

## Main attack : Rancor Blaster AOE

### Targeting

  * Attack shield border: No
  * Max attack range: 3
  * Min attack range: 0
  * New rotation speed: 2000
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Flying infantry (1), Flying vehicle (1), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
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
  * Shot count: 1
  * Shot delay: 270ms
  * Target locking: No

|Level          |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|---------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot|11724|12930|14136|15343|16549|17755|18961|20167|21373|22579|


### Projectile

  * Splash damage percentages: 100,100,75,50,25

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |3645 |4095 |4545 |4995 |5445 |5895 |6346 |6796 |7246 |7700 |
|Calculated damage per second|3478 |3836 |4194 |4552 |4910 |5268 |5626 |5984 |6342 |6700 |
|Calculated damage per cycle |11724|12930|14136|15343|16549|17755|18961|20167|21373|22579|


  * Cannons per sequence: 2
  * Shooting cycle duration: 3.370s
  * Directional: No
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(200)**: Wall, **(125)**: Trap, Turret, **(100)**: Droideka, Headquarters, Infantry, Infantry hero, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, **(75)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Light vehicle, Vehicule hero, **(0)**: Flying infantry, Flying vehicle
  * Pass through shield: Yes
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: RebelRageRancorCreature
  * Upgrade shard uid: shrd_troopRebelRageRancorCreature

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: rancorrage_neu-ani
  * Audio attack: "sfx_attack_creatures_rancor_1":33,"sfx_attack_creatures_rancor_2":33,"sfx_attack_creatures_rancor_3":34
  * Audio death: "sfx_death_creatures_rancor_1":100
  * Audio impact: "sfx_impact_creatures_rancor_1":33,"sfx_impact_creatures_rancor_2":33,"sfx_impact_creatures_rancor_3":34
  * Audio placement: "sfx_attack_creatures_rancor_1":35,"sfx_attack_creatures_rancor_2":35,"sfx_attack_creatures_rancor_3":30
  * Bundle name: rancorrage_neu-ani
  * Deploy vfx: vfx_prestige_deploy_large_reb
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "rancor_neu_rig_MASTER_MOVER/"rancor_neu_rig_locator_gun1":1,"rancor_neu_rig_MASTER_MOVER/rancor_neu_rig_locator_gun2":2
  * Hit spark: fx_rancor_deathblow
  * Icon camera position: 33.71,44.06,48.37
  * Icon lookat position: -0.61,3.05,-1.83
  * Max scale: 100
  * Name: Rancor Blaster AOE
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|3645       |4095       |4545       |4995       |5445       |5895       |6346       |6796       |7246       |7700       |
|Icon unlock position       |0,-0.75,0  |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation       |0,-30,0    |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |0.6,0.6,0.6|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: No
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |290401|290402|290403|290404|290405|290406|290407|290408|290409|290410|
|Point value|50    |60    |70    |80    |90    |100   |110   |120   |130   |150   |


