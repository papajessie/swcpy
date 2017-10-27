---
title: Repair Droid (Technician)
category: unit
---

# Repair Droid (Technician) — version 1093

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: healerInfantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Healer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 4
  * Type: infantry

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2000|2400|2800|3200|3600|4000|4400|4800|5200|6000|


### Training stats

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|1m20s                            |1m28s                                  |1m32s                                  |1m36s                                  |1m40s                                  |1m44s                                  |1m48s                                  |1m52s                                  |1m56s                                  |2m                                      |
|Training cost|200$                             |280$                                   |360$                                   |440$                                   |520$                                   |600$                                   |680$                                   |800$                                   |840$                                   |920$                                    |
|Building     |[Barracks 5](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |30m  |1h30m|5h    |10h   |1d12h  |2d12h  |4d     |6d      |1w2d    |
|Upgrade requirements|3000$|3000$|6000$|12500$|25000$|100000$|160000$|320000$|1000000$|1750000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 40
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * Support follow distance: 5

## Main attack : Technician

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Heavy vehicle (50)**, **Heavy vehicule hero (50)**, **Light vehicle (50)**, **Vehicule hero (50)**, Droideka (0), Flying infantry (0), Flying vehicle (0), Headquarters (0), Heavy infantry (0), Heavy infantry hero (0), Infantry (0), Infantry hero (0), Other building (0), Ressource generator (0), Shield (0), Shield generator (0), Storage (0), Support troop (0), Trap (0), Turret (0), Wall (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Damage per shot: 0
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 10
  * Self-centered targeting: Yes
  * Shot count: 1
  * Time between shots: 500ms
  * Target locking: Yes

### Projectile

  * Calculated damage per second: 0
  * Splash damage percentages: 100,100,100,100

|Level                      |1  |2  |3  |4  |5  |6  |7   |8   |9   |10  |
|---------------------------|---|---|---|---|---|---|----|----|----|----|
|Displayed damage per second|480|576|672|768|864|960|1056|1152|1248|1440|


  * Cannons per sequence: 1
  * Cliptime: 2.250s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(0%)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 1

#### Modifier "Repair"

  * Repair apply value as: relative
  * Repair buff ID: buffRepair
  * Repair duration: 250ms
  * Repair modifier: health
  * Repair ms first proc: 0s
  * Repair ms per proc: 251ms
  * Repair name: Repair
  * Repair stack: 0
  * Repair target: allies
  * Repair value: 0

|Level       |1                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |2                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |3                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |4                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |5                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |6                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |7                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |8                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |9                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |10                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Repair mults|**(1080%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1296%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1512%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1728%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1944%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(2160%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(2376%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(2592%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(2808%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(3240%)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0%)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|



## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Technician

|Level      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10          |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------------|
|Apply buffs|buffRepair1|buffRepair2|buffRepair3|buffRepair4|buffRepair5|buffRepair6|buffRepair7|buffRepair8|buffRepair9|buffRepair10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: techniciandroid_emp-ani
  * Audio attack: "sfx_attack_droid_technician_1":50,"sfx_attack_droid_technician_2":50
  * Audio death: "sfx_death_droid_technician_1":50,"sfx_death_droid_technician_2":50
  * Audio placement: "sfx_placement_droid_technician_1":50,"sfx_placement_droid_technician_2":50
  * Audio train: "sfx_ui_unitcomplete_droid_01":50,"sfx_ui_unitcomplete_droid_02":50
  * Bundle name: techniciandroid_emp-ani
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: vehicles
  * Icon camera position: 7.9,7.91,12.71
  * Icon lookat position: 0.06,2.6,-0.14
  * Info UI type: Healer
  * Max scale: 200
  * Muzzle flash: fx_healing_ring
  * Name: Technician
  * Repair asset name: fx_healing_condition_veh
  * Repair bundle name: fx_healing
  * Spin speed: 0
  * Targeted type: ALLIES

|Level                      |1  |2  |3  |4  |5  |6  |7   |8   |9   |10  |
|---------------------------|---|---|---|---|---|---|----|----|----|----|
|Displayed damage per second|480|576|672|768|864|960|1056|1152|1248|1440|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Repair is refreshing: No
  * Repair tags: repair
  * Seeks target: No
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120501|120502|120503|120504|120505|120506|120507|120508|120509|120510|
|Point value|4     |4.800 |5.600 |6.400 |7.200 |8     |8.800 |9.600 |10.400|12    |


I could not show the following roles, because I was not programmed to : buffRepairmult
