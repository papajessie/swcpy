---
title: Stolen Mobile Heavy Cannon (StolenMHC)
category: unit
---

# Stolen Mobile Heavy Cannon (StolenMHC) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: No
  * Role: Striker
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 12
  * Type: vehicle

|Level |10   |5    |3    |2    |1    |9    |4    |8    |6    |7    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|32400|19440|15120|12960|10800|28080|17280|25920|21600|23760|


### Training stats

|Level        |10                                     |5                                     |3                                     |2                                     |1                             |9                                     |4                                     |8                                     |6                                     |7                                     |
|-------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|6m                                     |5m                                    |4m36s                                 |4m24s                                 |4m12s                         |5m48s                                 |4m48s                                 |5m36s                                 |5m12s                                 |5m24s                                 |
|Training cost|3000$                                  |1300$                                 |900$                                  |700$                                  |500$                          |2700$                                 |1100$                                 |2400$                                 |1500$                                 |1700$                                 |
|Building     |[Research Lab 10](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Factory 7](rebelFactory.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|


### Upgrading stats

|Level               |10      |5     |3    |2    |1    |9       |4     |8      |6      |7      |
|--------------------|--------|------|-----|-----|-----|--------|------|-------|-------|-------|
|Upgrade time        |1w5d    |20h   |2h30m|1h   |0s   |1w1d    |7h    |6d     |2d12h  |4d     |
|Upgrade requirements|2250000$|35000$|6000$|3000$|6500$|1250000$|15000$|385000$|115000$|200000$|


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

|Level          |10  |5   |3   |2   |1   |9   |4   |8   |6   |7   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|6480|3888|3024|2592|2160|5616|3456|5184|4320|4752|


### Projectile

  * Splash damage percentages: 100,75,50

|Level                       |10  |5   |3   |2   |1   |9   |4   |8   |6   |7   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |3600|2160|1680|1440|1200|3120|1920|2880|2400|2640|
|Calculated damage per second|3600|2160|1680|1440|1200|3120|1920|2880|2400|2640|


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

  * Unit ID: StolenMHC

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

|Level                      |10  |5   |3   |2   |1   |9   |4   |8   |6   |7   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|3600|2160|1680|1440|1200|3120|1920|2880|2400|2640|


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

|Level|10    |5     |3     |2     |1     |9     |4     |8     |6     |7     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|481240|481220|481212|481208|481204|481236|481216|481232|481224|481228|


