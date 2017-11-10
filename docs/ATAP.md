---
title: AT-AP Walker (ATAP)
category: unit
---

# AT-AP Walker (ATAP) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 10
  * Type: vehicle

|Level |1   |2   |3   |4   |5   |6   |7    |8    |9    |10   |
|------|----|----|----|----|----|----|-----|-----|-----|-----|
|Health|7200|7610|8050|8510|9000|9530|10090|10680|11320|12000|


### Training stats

|Level   |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|--------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Building|[Factory 4](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |1h   |2h30m|7h    |20h   |2d12h  |4d     |6d     |1w1d    |1w5d    |
|Upgrade requirements|6500$|3000$|6000$|15000$|35000$|115000$|200000$|385000$|1250000$|2250000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x1

## Main attack : ATAP

### Targeting

  * Attack shield border: Yes
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 3927
  * Target preference strength: 90
  * Target preferences: **Shield (70)**, **Shield generator (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,2
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 4
  * Time between shots: 200ms
  * Target locking: No

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|1540|1630|1720|1820|1920|2040|2160|2280|2420|2570|


### Projectile

|Level                       |1       |2       |3       |4       |5       |6       |7       |8   |9       |10      |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|----|--------|--------|
|Displayed damage per second |2160    |2290    |2410    |2550    |2690    |2860    |3030    |3200|3400    |3610    |
|Calculated damage per second|2161.404|2287.719|2414.035|2554.386|2694.737|2863.158|3031.579|3200|3396.491|3607.018|


  * Cannons per sequence: 2
  * Cliptime: 2.850s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 12
  * Damage multipliers: **(400)**: Shield, Shield generator, **(200)**: Heavy infantry hero, Heavy vehicule hero, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy vehicle, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, **(60)**: Wall
  * Pass through shield: No
  * Salvos: 4

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: ATAP

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: atap_rbl-ani
  * Audio attack: "sfx_attack_rebel_atap_1":30,"sfx_attack_rebel_atap_2":35,"sfx_attack_rebel_atap_3":35
  * Audio death: "sfx_death_rebel_atap_1":100
  * Audio placement: "sfx_placement_walker_1":50,"sfx_placement_walker_2":50
  * Buff asset offset: 0.00,1.94,0.00
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: atap_rbl-ani
  * Factory rotation: 0
  * Factory scale factor: 0.85199999999999997957189634689711965620517730712890625
  * Favorite target type: shieldGenerator
  * Gun position: "atap_rbl_rig_locator_gun1":1,"atap_rbl_rig_locator_gun2":2
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 20.98,26.07,34.08
  * Icon lookat position: -0.59,2.38,-0.99
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: ATAP
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|2160|2290|2410|2550|2690|2860|3030|3200|3400|3610|


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
|Order      |230401|230402|230403|230404|230405|230406|230407|230408|230409|230410|
|Point value|10    |12    |14    |16    |18    |20    |22    |24    |26    |30    |


