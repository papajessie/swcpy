---
title: Seized Juggernaut (SeizedJuggernaut)
category: unit
---

# Seized Juggernaut (SeizedJuggernaut) — version 1098

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

|Level |7    |9    |4    |10   |3    |5    |6    |1    |8    |2    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|44000|52000|32000|60000|28000|36000|40000|20000|48000|24000|


### Training stats

|Level        |7                                      |9                                      |4                                      |10                                      |3                                      |5                                      |6                                      |1                              |8                                      |2                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|-------------------------------|---------------------------------------|---------------------------------------|
|Training time|3m36s                                  |5m44s                                  |3m12s                                  |6m4s                                    |3m4s                                   |3m20s                                  |3m28s                                  |2m48s                          |5m24s                                  |2m56s                                  |
|Training cost|3400$                                  |4200$                                  |2200$                                  |4600$                                   |1800$                                  |2600$                                  |3000$                                  |1000$                          |4000$                                  |1400$                                  |
|Building     |[Research Lab 7](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Factory 5](empireFactory.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|


### Upgrading stats

|Level               |7      |9       |4     |10      |3     |5     |6      |1    |8      |2    |
|--------------------|-------|--------|------|--------|------|------|-------|-----|-------|-----|
|Upgrade time        |4d     |1w1d    |7h    |1w5d    |2h30m |20h   |2d12h  |0s   |6d     |1h   |
|Upgrade requirements|225000$|1500000$|20000$|2500000$|10000$|50000$|135000$|4000$|450000$|5000$|


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

  * Time between start of clip and first shot: 1s
  * Clip retargeting: No
  * Gun shooting sequence: 1,1
  * Impact delay: 500ms
  * Can shoot over walls: Yes
  * Time between end of clip and start of clip: 1s
  * Retargeting offset: 16
  * Self-centered targeting: No
  * Shot count: 2
  * Time between shots: 250ms
  * Target locking: No

|Level          |7   |9   |4   |10  |3   |5   |6   |1   |8   |2   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|4950|5850|3600|6750|3150|4050|4500|2250|5400|2700|


### Projectile

|Level                       |7   |9   |4   |10  |3   |5   |6   |1   |8   |2   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |4400|5200|3200|6000|2800|3600|4000|2000|4800|2400|
|Calculated damage per second|4950|5850|3600|6750|3150|4050|4500|2250|5400|2700|


  * Cannons per sequence: 2
  * Cliptime: 2s
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

  * Animation delay: 0
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

|Level                      |7   |9   |4   |10  |3   |5   |6   |1   |8   |2   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|4400|5200|3200|6000|2800|3600|4000|2000|4800|2400|


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

|Level|7     |9     |4     |10    |3     |5     |6     |1     |8     |2     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|484828|484836|484816|484840|484812|484820|484824|484804|484832|484808|


