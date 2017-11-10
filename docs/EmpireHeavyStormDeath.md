---
title: Heavy Undead Trooper (EmpireHeavyStormDeath)
category: unit
---

# Heavy Undead Trooper (EmpireHeavyStormDeath) — version 1098

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

|Level |1   |5    |9    |10   |8    |3    |6    |7    |2   |4    |
|------|----|-----|-----|-----|-----|-----|-----|-----|----|-----|
|Health|7500|13500|19500|22500|18000|10500|15000|16500|9000|12000|


### Training stats

|Level        |1                                 |5                                      |9                                      |10                                      |8                                      |3                                      |6                                      |7                                      |2                                      |4                                      |
|-------------|----------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|1m20s                             |1m40s                                  |1m56s                                  |2m                                      |1m52s                                  |1m32s                                  |1m44s                                  |1m48s                                  |1m28s                                  |1m36s                                  |
|Training cost|200$                              |520$                                   |840$                                   |920$                                    |760$                                   |360$                                   |600$                                   |680$                                   |280$                                   |440$                                   |
|Building     |[Barracks 10](empireBarracks.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |5     |9       |10      |8      |3    |6      |7      |2    |4     |
|--------------------|-----|------|--------|--------|-------|-----|-------|-------|-----|------|
|Upgrade time        |0s   |8h    |5d      |1w1d    |3d12h  |1h   |1d     |2d     |15m  |3h30m |
|Upgrade requirements|3000$|25000$|1000000$|1750000$|320000$|6000$|100000$|160000$|3000$|12500$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 10
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

### Modifiers

#### Modifier "Reduce heals"

  * Reduce heals apply value as: absolutePercent
  * Reduce heals buff ID: buffReduceHeals
  * Reduce heals duration: permanent
  * Reduce heals modifier: healDefense
  * Reduce heals ms first proc: 0s
  * Reduce heals ms per proc: permanent
  * Reduce heals name: Reduce heals
  * Reduce heals stack: 0
  * Reduce heals target: self
  * Reduce heals value: 50


## Main attack : HeavyStormDeath

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy infantry hero (50)**, **Heavy vehicle (50)**, **Heavy vehicule hero (50)**, **Infantry (50)**, **Infantry hero (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, **Vehicule hero (50)**, Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 10
  * Time between shots: 100ms
  * Target locking: No

|Level          |1  |5  |9  |10 |8  |3  |6  |7  |2  |4  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|170|306|442|510|408|238|340|374|204|272|


### Projectile

|Level                       |1  |5  |9   |10  |8   |3  |6   |7   |2  |4  |
|----------------------------|---|---|----|----|----|---|----|----|---|---|
|Displayed damage per second |500|900|1300|1500|1200|700|1000|1100|600|800|
|Calculated damage per second|500|900|1300|1500|1200|700|1000|1100|600|800|


  * Cannons per sequence: 1
  * Cliptime: 3.400s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 30
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, **(80)**: Wall
  * Pass through shield: No
  * Salvos: 10

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffReduceHeals2
  * Unit ID: EmpireHeavyStormDeath

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: heavytrooper_dth-ani
  * Audio attack: "sfx_attack_gatlinggun_1":30,"sfx_attack_gatlinggun_2":35,"sfx_attack_gatlinggun_3":35
  * Audio death: "sfx_death_deathtrooper_1":35,"sfx_death_deathtrooper_2":35,"sfx_death_deathtrooper_3":30
  * Audio placement: "sfx_placement_deathtrooper_1":35,"sfx_placement_deathtrooper_2":35,"sfx_placement_deathtrooper_3":30
  * Buff asset offset: 0.00,0.27,0.00
  * Bundle name: heavytrooper_dth-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: deathheavytrooper_emp_rig_MASTER_MOVER/deathheavytrooper_emp_rig_locator_gun_Rt:1
  * Hit spark: fx_gatling_hit_r_lrg
  * Icon camera position: 4.46,8.55,22.59
  * Icon closeup camera position: 3.27,3.36,10.55
  * Icon closeup lookat position: -0.05,2.29,-0.46
  * Icon lookat position: -0.36,1.33,-0.66
  * Max scale: 100
  * Muzzle flash: fx_gatling_muzzle_r_lrg
  * Name: HeavyStormDeath
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |5  |9   |10  |8   |3  |6   |7   |2  |4  |
|---------------------------|---|---|----|----|----|---|----|----|---|---|
|Displayed damage per second|500|900|1300|1500|1200|700|1000|1100|600|800|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Reduce heals is refreshing: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |5     |9     |10    |8     |3     |6     |7     |2     |4     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |133001|133005|133009|133010|133008|133003|133006|133007|133002|133004|
|Point value|4     |7.200 |10.400|12    |9.600 |5.600 |8     |8.800 |4.800 |6.400 |


