---
title: Rebel Hailfire Droid (Hailfire)
category: unit
---

# Rebel Hailfire Droid (Hailfire) — version 1119

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 7
  * Type: vehicle

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2800|3360|3920|4480|5040|5600|6160|6720|7280|8400|


### Training stats

|Level        |1                             |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|2m48s                         |2m56s                                 |3m4s                                  |3m12s                                 |3m20s                                 |3m28s                                 |3m36s                                 |3m16s                                 |3m23s                                 |3m30s                                  |
|Training cost|350$                          |490$                                  |630$                                  |770$                                  |910$                                  |1050$                                 |1190$                                 |1400$                                 |1470$                                 |1610$                                  |
|Building     |[Factory 7](rebelFactory.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

|Level               |1   |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s  |45m  |2h   |6h    |12h   |2d     |3d     |5d     |1w      |1w3d    |
|Upgrade requirements|700$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2

## Main attack : projectileHailfire

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, _Droideka (60)_, _Flying infantry (60)_, _Flying vehicle (60)_, _Heavy infantry (60)_, _Heavy infantry hero (60)_, _Heavy vehicle (60)_, _Heavy vehicule hero (60)_, _Infantry (60)_, _Infantry hero (60)_, _Light vehicle (60)_, _Support troop (60)_, _Vehicule hero (60)_, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0
  * Time between start of clip and first shot: 1s
  * Clip retargeting: Yes
  * Gun shooting sequence: 1,2
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 6
  * Time between shots: 100ms
  * Target locking: No

|Level          |1  |2  |3  |4  |5  |6  |7  |8  |9  |10  |
|---------------|---|---|---|---|---|---|---|---|---|----|
|Damage per shot|368|441|515|588|662|735|809|882|956|1103|


### Projectile

  * Splash damage percentages: 100,75,50

|Level                       |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |630 |756 |882 |1008|1134|1260|1386|1512|1638|1890|
|Calculated damage per second|630 |756 |882 |1008|1134|1260|1386|1512|1638|1890|
|Calculated damage per clip  |2208|2646|3090|3528|3972|4410|4854|5292|5736|6618|


  * Cannons per sequence: 2
  * Cliptime: 3.500s
  * Directional: No
  * Is deflectable: No
  * Max speed: 12
  * Damage multipliers: **(300)**: Flying vehicle, Light vehicle, Vehicule hero, **(250)**: Heavy vehicle, Heavy vehicule hero, **(200)**: Trap, Turret, **(100)**: Droideka, **(80)**: Wall, **(50)**: Flying infantry, Heavy infantry, Heavy infantry hero, Infantry, Infantry hero, Support troop, **(25)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage
  * Pass through shield: No
  * Salvos: 6

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Hailfire

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: hailfiredroid_rbl-ani
  * Audio attack: "sfx_attack_rebel_hailfire_1":35,"sfx_attack_rebel_hailfire_2":35,"sfx_attack_rebel_hailfire_3":30
  * Audio death: "sfx_death_rebel_hailfire_1":100
  * Audio impact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * Audio placement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * Buff asset offset: 0.00,0.88,0.00
  * Bullet: fx_rocket_projectile_b_sm
  * Bundle name: hailfiredroid_rbl-ani
  * Factory rotation: 90
  * Factory scale factor: 0.71499999999999996891375531049561686813831329345703125
  * Favorite target type: turret
  * Gun position: "hailfiredroid_rbl_rig_locator_gun1":1,"hailfiredroid_rbl_rig_locator_gun2":2
  * Hit spark: fx_rocket_hit_b_sm
  * Icon camera position: 36.69,22.39,29.86
  * Icon lookat position: -0.49,1.9,-0.43
  * Max scale: 100
  * Muzzle flash: fx_rocket_muzzle_b_sm
  * Name: projectileHailfire
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |2  |3  |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|---|---|---|----|----|----|----|----|----|----|
|Displayed damage per second|630|756|882|1008|1134|1260|1386|1512|1638|1890|


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
|Order      |230701|230702|230703|230704|230705|230706|230707|230708|230709|230710|
|Point value|7     |8.400 |9.800 |11.200|12.600|14    |15.400|16.800|18.200|21    |


