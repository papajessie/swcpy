---
title: Mobile Heavy Cannon (MHC)
category: unit
---

# Mobile Heavy Cannon (MHC) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 12
  * Type: vehicle

|Level |2    |3    |4    |6    |5    |10   |1    |8    |7    |9    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|12960|15120|17280|21600|19440|32400|10800|25920|23760|28080|


### Training stats

|Level        |2                                      |3                                      |4                                      |6                                      |5                                      |10                                      |1                              |8                                      |7                                      |9                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|4m24s                                  |4m36s                                  |4m48s                                  |5m12s                                  |5m                                     |6m                                      |4m12s                          |5m36s                                  |5m24s                                  |5m48s                                  |
|Training cost|700$                                   |900$                                   |1100$                                  |1500$                                  |1300$                                  |3000$                                   |500$                           |2400$                                  |1700$                                  |2700$                                  |
|Building     |[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Factory 7](empireFactory.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|


### Upgrading stats

|Level               |2    |3    |4     |6      |5     |10      |1    |8      |7      |9       |
|--------------------|-----|-----|------|-------|------|--------|-----|-------|-------|--------|
|Upgrade time        |1h   |2h30m|7h    |2d12h  |20h   |1w5d    |0s   |6d     |4d     |1w1d    |
|Upgrade requirements|3000$|6000$|15000$|115000$|35000$|2250000$|6500$|385000$|200000$|1250000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 10
  * Propensity to go around obstacles: 200
  * Rotation speed: 31.416
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2

## Main attack : projectileMHC

### Targeting

  * Attack shield border: No
  * Max attack range: 10
  * Min attack range: 0
  * New rotation speed: 15708
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 900ms
  * Clip retargeting: Yes
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 900ms
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 200ms
  * Target locking: No

|Level          |2   |3   |4   |6   |5   |10  |1   |8   |7   |9   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2592|3024|3456|4320|3888|6480|2160|5184|4752|5616|


### Projectile

  * Splash damage percentages: 100,75,50

|Level                       |2   |3   |4   |6   |5   |10  |1   |8   |7   |9   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |1440|1680|1920|2400|2160|3600|1200|2880|2640|3120|
|Calculated damage per second|1440|1680|1920|2400|2160|3600|1200|2880|2640|3120|


  * Cannons per sequence: 1
  * Cliptime: 1.800s
  * Directional: No
  * Is deflectable: No
  * Max speed: 12
  * Damage multipliers: **(300)**: Flying vehicle, Light vehicle, Vehicule hero, **(250)**: Heavy vehicle, Heavy vehicule hero, **(200)**: Trap, Turret, **(100)**: Droideka, **(80)**: Wall, **(50)**: Flying infantry, Heavy infantry, Heavy infantry hero, Infantry, Infantry hero, Support troop, **(25)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: MHC

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: umhc_emp-ani
  * Audio attack: "sfx_attack_empire_umhc_1":33,"sfx_attack_empire_umhc_2":33,"sfx_attack_empire_umhc_3":34
  * Audio death: "sfx_death_empire_umhc_1":100
  * Audio placement: "sfx_placement_empire_atat_1":100
  * Buff asset offset: 0.00,0.90,0
  * Bullet: fx_UMHC_projectile_r_lrg
  * Bundle name: umhc_emp-ani
  * Factory rotation: 90
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "umhc_emp_rig_MASTER_MOVER/umhc_emp_rig_locator_gun":1
  * Hit spark: fx_UMHC_hit_r_lrg
  * Icon camera position: 30.35,41.15,37.35
  * Icon lookat position: -0.33,0.73,-0.17
  * Max scale: 100
  * Muzzle flash: fx_UMHC_muzzle_r_lrg
  * Name: projectileMHC
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |2   |3   |4   |6   |5   |10  |1   |8   |7   |9   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|1440|1680|1920|2400|2160|3600|1200|2880|2640|3120|


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

|Level      |2     |3     |4     |6     |5     |10    |1     |8     |7     |9     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |130702|130703|130704|130706|130705|130710|130701|130708|130707|130709|
|Point value|14.400|16.800|19.200|24    |21.600|36    |12    |28.800|26.400|31.200|


