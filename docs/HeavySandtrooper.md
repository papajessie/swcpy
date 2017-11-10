---
title: Heavy Sandtrooper (HeavySandtrooper)
category: unit
---

# Heavy Sandtrooper (HeavySandtrooper) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: No
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 4
  * Type: infantry

|Level |2   |3    |1   |5    |10   |8    |4    |7    |6    |9    |
|------|----|-----|----|-----|-----|-----|-----|-----|-----|-----|
|Health|9725|11325|8100|14575|24300|19425|12950|17800|16200|21050|


### Training stats

|Level        |2                                      |3                                      |1                                |5                                      |10                                      |8                                      |4                                      |7                                      |6                                      |9                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|1m28s                                  |1m32s                                  |1m20s                            |1m40s                                  |2m                                      |1m52s                                  |1m36s                                  |1m48s                                  |1m44s                                  |1m56s                                  |
|Training cost|280$                                   |360$                                   |200$                             |520$                                   |920$                                    |800$                                   |440$                                   |680$                                   |600$                                   |840$                                   |
|Building     |[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Barracks 6](empireBarracks.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|


### Upgrading stats

|Level               |2    |3    |1    |5     |10      |8      |4     |7      |6      |9       |
|--------------------|-----|-----|-----|------|--------|-------|------|-------|-------|--------|
|Upgrade time        |15m  |1h   |0s   |8h    |1w2d    |3d12h  |3h30m |2d     |1d     |5d      |
|Upgrade requirements|3000$|6000$|3000$|25000$|1750000$|320000$|12500$|160000$|100000$|1000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : HeavyStorm

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 17
  * Time between shots: 75ms
  * Target locking: No

|Level          |2  |3  |1  |5  |10  |8   |4  |7  |6  |9   |
|---------------|---|---|---|---|----|----|---|---|---|----|
|Damage per shot|540|630|450|810|1340|1080|720|980|900|1160|


### Projectile

|Level                       |2       |3       |1       |5       |10      |8       |4       |7       |6       |9       |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |2504    |2916    |2080    |3752    |6244    |5000    |3328    |4576    |4164    |5408    |
|Calculated damage per second|2481.081|2894.595|2067.568|3721.622|6156.757|4962.162|3308.108|4502.703|4135.135|5329.730|


  * Cannons per sequence: 1
  * Cliptime: 3.700s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 30
  * Damage multipliers: **(175)**: Shield, Shield generator, **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Storage, Support troop, Trap, Turret, Vehicule hero, **(80)**: Wall
  * Pass through shield: No
  * Salvos: 17

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: HeavySandtrooper

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: sandheavytrooper_emp-ani
  * Audio attack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * Buff asset offset: 0.00,0.28,0.00
  * Bundle name: sandheavytrooper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_gatling_hit_r_lrg
  * Icon camera position: 7.72,10.75,21.04
  * Icon closeup camera position: 1.24,0.61,11.39
  * Icon closeup lookat position: -0.02,2.5,-0.01
  * Icon lookat position: -0.4,1.77,0.55
  * Max scale: 100
  * Muzzle flash: fx_gatling_muzzle_r_lrg
  * Name: HeavyStorm
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |2   |3   |1   |5   |10  |8   |4   |7   |6   |9   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|2504|2916|2080|3752|6244|5000|3328|4576|4164|5408|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Point value: 1
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level|2     |3     |1     |5     |10    |8     |4     |7     |6     |9     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|300011|300012|300010|300014|300019|300017|300013|300016|300015|300018|


