---
title: Hunter Rancor (EmpireHunterRancorCreature)
category: unit
---

# Hunter Rancor (EmpireHunterRancorCreature)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 20
  * Type: creature

|Level |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|99840|94506|89173|83840|78506|73173|67840|62506|57173|51840|


### Training stats

  * Training time: 5s
  * Training cost: Free

### Upgrading stats

  * Upgrade time: 5s

|Level               |10                |9                 |8                 |7                 |6                 |5                 |4                 |3                |2                |1                |
|--------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|-----------------|-----------------|-----------------|
|Upgrade requirements|680 data fragments|520 data fragments|400 data fragments|310 data fragments|240 data fragments|180 data fragments|130 data fragments|90 data fragments|60 data fragments|32 data fragments|


### Movement stats

  * Acceleration: 0
  * Crushes walls: Yes
  * Flying unit: No
  * Max speed: 30
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
  * Target preferences: **Heavy infantry (70)**, **Heavy infantry hero (70)**, **Infantry (70)**, **Infantry hero (70)**, _Droideka (60)_, _Heavy vehicle (60)_, _Heavy vehicule hero (60)_, _Light vehicle (60)_, _Vehicule hero (60)_, Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Turret (50), Headquarters (40), Flying infantry (1), Flying vehicle (1), Wall (1), Trap (0)
  * View range: 16

### Shooting

  * Animation delay: 960ms
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

|Level          |10   |9    |8    |7    |6   |5   |4   |3   |2   |1   |
|---------------|-----|-----|-----|-----|----|----|----|----|----|----|
|Damage per shot|11908|11272|10636|10000|9364|8728|8092|7455|6819|6183|


### Projectile

  * Splash damage percentages: 100,50

|Level                       |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |7375 |6944 |6512 |6081 |5650 |5219 |4787 |4356 |3925 |3494 |
|Calculated damage per second|5177 |4900 |4624 |4347 |4071 |3794 |3518 |3241 |2964 |2688 |
|Calculated damage per cycle |23816|22544|21272|20000|18728|17456|16184|14910|13638|12366|


  * Cannons per sequence: 2
  * Shooting cycle duration: 4.600s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(200)**: Heavy infantry, Infantry, **(100)**: Droideka, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(0)**: Flying infantry, Flying vehicle
  * Pass through shield: Yes
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EmpireHunterRancorCreature
  * Upgrade shard uid: shrd_troopEmpireHunterRancorCreature

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: rancorhunter_neu-ani
  * Audio attack: "sfx_attack_creatures_rancor_1":33,"sfx_attack_creatures_rancor_2":33,"sfx_attack_creatures_rancor_3":34
  * Audio death: "sfx_death_creatures_rancor_1":100
  * Audio impact: "sfx_impact_creatures_rancor_1":33,"sfx_impact_creatures_rancor_2":33,"sfx_impact_creatures_rancor_3":34
  * Audio placement: "sfx_attack_creatures_rancor_1":35,"sfx_attack_creatures_rancor_2":35,"sfx_attack_creatures_rancor_3":30
  * Bundle name: rancorhunter_neu-ani
  * Deploy vfx: vfx_prestige_deploy_large_emp
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Gun position: "rancor_neu_rig_MASTER_MOVER/"rancor_neu_rig_locator_gun1":1,"rancor_neu_rig_MASTER_MOVER/rancor_neu_rig_locator_gun2":2
  * Icon camera position: 32.55,42.31,46.76
  * Icon lookat position: -0.58,2.75,-1.64
  * Max scale: 100
  * Muzzle flash: fx_melee_headbutt_lrg
  * Name: Rancor Blaster
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |10         |9          |8          |7          |6          |5          |4          |3          |2          |1          |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|7375       |6944       |6512       |6081       |5650       |5219       |4787       |4356       |3925       |3494       |
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

|Level      |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |90210|90209|90208|90207|90206|90205|90204|90203|90202|90201|
|Point value|60   |52   |48   |44   |40   |36   |32   |28   |24   |20   |


