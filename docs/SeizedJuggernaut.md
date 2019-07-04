---
title: Seized Juggernaut (SeizedJuggernaut)
category: unit
---

# Seized Juggernaut (SeizedJuggernaut)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Empire
  * Buildable unit: No
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 20
  * Type: vehicle

|Level |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|60000|52000|48000|44000|40000|36000|32000|28000|24000|20000|


### Training stats

|Level        |10                                      |9                                      |8                                      |7                                      |6                                      |5                                      |4                                      |3                                      |2                                      |1                              |
|-------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|-------------------------------|
|Training time|6m4s                                    |5m44s                                  |5m24s                                  |3m36s                                  |3m28s                                  |3m20s                                  |3m12s                                  |3m4s                                   |2m56s                                  |2m48s                          |
|Training cost|4600$                                   |4200$                                  |4000$                                  |3400$                                  |3000$                                  |2600$                                  |2200$                                  |1800$                                  |1400$                                  |1000$                          |
|Building     |[Research Lab 10](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Factory 5](empireFactory.html)|


### Upgrading stats

|Level               |10      |9       |8      |7      |6      |5     |4     |3     |2    |1    |
|--------------------|--------|--------|-------|-------|-------|------|------|------|-----|-----|
|Upgrade time        |1w5d    |1w1d    |6d     |4d     |2d12h  |20h   |7h    |2h30m |1h   |0s   |
|Upgrade requirements|2500000$|1500000$|450000$|225000$|135000$|50000$|20000$|10000$|5000$|4000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: Yes
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 2
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2

## Main attack : Juggernaut

### Targeting

  * Attack shield border: Yes
  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 2000
  * Target preference strength: 90
  * Target preferences: **Shield (70)**, **Shield generator (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0s
  * Charge time: 1s
  * Clip retargeting: No
  * Gun shooting sequence: 1,1
  * Impact delay: 500ms
  * Can shoot over walls: Yes
  * Reload time: 1s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 2
  * Shot delay: 250ms
  * Target locking: No

|Level          |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|6750|5850|5400|4950|4500|4050|3600|3150|2700|2250|


### Projectile

|Level                       |10   |9    |8    |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|-----|-----|-----|----|----|----|----|----|----|----|
|Displayed damage per second |5600 |5200 |4800 |4400|4000|3600|3200|2800|2400|2000|
|Calculated damage per second|6750 |5850 |5400 |4950|4500|4050|3600|3150|2700|2250|
|Calculated damage per cycle |13500|11700|10800|9900|9000|8100|7200|6300|5400|4500|


  * Cannons per sequence: 2
  * Shooting cycle duration: 2s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Shield, Shield generator, **(200)**: Heavy infantry hero, Heavy vehicule hero, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy vehicle, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SeizedJuggernaut

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: attacktank_rbl-ani
  * Audio attack: "sfx_attack_rebel_attacktank_1":30,"sfx_attack_rebel_attacktank_2":35,"sfx_attack_rebel_attacktank_3":35
  * Audio death: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * Audio placement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * Buff asset offset: 0.00,1.84,0.00
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: attacktank_rbl-ani
  * Factory rotation: 0
  * Factory scale factor: 0.72299999999999997601918266809661872684955596923828125
  * Favorite target type: shieldGenerator
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun1":1, "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun2":1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 35.28,24.86,45.37
  * Icon lookat position: -0.89,1.38,-0.23
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: Juggernaut
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|5600|5200|4800|4400|4000|3600|3200|2800|2400|2000|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 3
  * Auto spawn spreading scale: 3
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level|10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order|83310|83309|83308|83307|83306|83305|83304|83303|83302|83301|


