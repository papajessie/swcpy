---
title: Heavy Desert Soldier (HeavySandSoldier)
category: unit
---

# Heavy Desert Soldier (HeavySandSoldier) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: No
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry

|Level |7    |8    |1   |2   |9    |6    |3    |5    |4    |10   |
|------|-----|-----|----|----|-----|-----|-----|-----|-----|-----|
|Health|17800|19425|8100|9725|21050|16200|11325|14575|12950|24300|


### Training stats

|Level        |7                                     |8                                     |1                               |2                                     |9                                     |6                                     |3                                     |5                                     |4                                     |10                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|2m15s                                 |2m20s                                 |1m40s                           |1m50s                                 |2m25s                                 |2m10s                                 |1m55s                                 |2m5s                                  |2m                                    |2m30s                                  |
|Training cost|850$                                  |1000$                                 |250$                            |350$                                  |1050$                                 |750$                                  |450$                                  |650$                                  |550$                                  |1150$                                  |
|Building     |[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Barracks 6](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

|Level               |7      |8      |1    |2    |9       |6      |3    |5     |4     |10      |
|--------------------|-------|-------|-----|-----|--------|-------|-----|------|------|--------|
|Upgrade time        |2d     |3d12h  |0s   |15m  |5d      |1d     |1h   |8h    |3h30m |1w2d    |
|Upgrade requirements|175000$|350000$|3000$|3000$|1000000$|115000$|6000$|35000$|15000$|2000000$|


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

## Main attack : HeavyRebel

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

|Level          |7  |8   |1  |2  |9   |6  |3  |5  |4  |10  |
|---------------|---|----|---|---|----|---|---|---|---|----|
|Damage per shot|980|1080|450|540|1160|900|630|810|720|1340|


### Projectile

|Level                       |7       |8       |1       |2       |9       |6       |3       |5       |4       |10      |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |5728    |6244    |2600    |3128    |6764    |5200    |3644    |4680    |4164    |7800    |
|Calculated damage per second|4502.703|4962.162|2067.568|2481.081|5329.730|4135.135|2894.595|3721.622|3308.108|6156.757|


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

  * Unit ID: HeavySandSoldier

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: sandheavysoldier_rbl-ani
  * Audio attack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Buff asset offset: 0.00,0.30,0.00
  * Bundle name: sandheavysoldier_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_gatling_hit_b_lrg
  * Icon camera position: 3.52,10.26,21.73
  * Icon closeup camera position: -0.24,0.29,11.62
  * Icon closeup lookat position: -0.13,2.39,0.83
  * Icon lookat position: -0.44,1.75,0.53
  * Max scale: 100
  * Muzzle flash: fx_gatling_muzzle_b_lrg
  * Name: HeavyRebel
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |7   |8   |1   |2   |9   |6   |3   |5   |4   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|5728|6244|2600|3128|6764|5200|3644|4680|4164|7800|


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

|Level|7     |8     |1     |2     |9     |6     |3     |5     |4     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|300036|300037|300030|300031|300038|300035|300032|300034|300033|300039|


