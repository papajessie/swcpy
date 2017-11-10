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

|Level |8    |7    |4    |6    |5    |9    |1    |3    |10   |2    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|25920|23760|17280|21600|19440|28080|10800|15120|32400|12960|


### Training stats

|Level        |8                                     |7                                     |4                                     |6                                     |5                                     |9                                     |1                             |3                                     |10                                     |2                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|
|Training time|5m36s                                 |5m24s                                 |4m48s                                 |5m12s                                 |5m                                    |5m48s                                 |4m12s                         |4m36s                                 |6m                                     |4m24s                                 |
|Training cost|2400$                                 |1700$                                 |1100$                                 |1500$                                 |1300$                                 |2700$                                 |500$                          |900$                                  |3000$                                  |700$                                  |
|Building     |[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Factory 7](rebelFactory.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|


### Upgrading stats

|Level               |8      |7      |4     |6      |5     |9       |1    |3    |10      |2    |
|--------------------|-------|-------|------|-------|------|--------|-----|-----|--------|-----|
|Upgrade time        |6d     |4d     |7h    |2d12h  |20h   |1w1d    |0s   |2h30m|1w5d    |1h   |
|Upgrade requirements|385000$|200000$|15000$|115000$|35000$|1250000$|6500$|6000$|2250000$|3000$|


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

|Level          |8   |7   |4   |6   |5   |9   |1   |3   |10  |2   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|5184|4752|3456|4320|3888|5616|2160|3024|6480|2592|


### Projectile

  * Splash damage percentages: 100,75,50

|Level                       |8   |7   |4   |6   |5   |9   |1   |3   |10  |2   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |2880|2640|1920|2400|2160|3120|1200|1680|3600|1440|
|Calculated damage per second|2880|2640|1920|2400|2160|3120|1200|1680|3600|1440|


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

|Level                      |8   |7   |4   |6   |5   |9   |1   |3   |10  |2   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|2880|2640|1920|2400|2160|3120|1200|1680|3600|1440|


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

|Level|8     |7     |4     |6     |5     |9     |1     |3     |10    |2     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|481232|481228|481216|481224|481220|481236|481204|481212|481240|481208|


