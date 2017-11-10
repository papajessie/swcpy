---
title: Repair Droid (Technician)
category: unit
---

# Repair Droid (Technician) — version 1098

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

|Level |8   |5   |7   |3   |2   |10  |1   |4   |9   |6   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|4800|3600|4400|2800|2400|6000|2000|3200|5200|4000|


### Training stats

|Level        |8                                      |5                                      |7                                      |3                                      |2                                      |10                                      |1                                |4                                      |9                                      |6                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|1m52s                                  |1m40s                                  |1m48s                                  |1m32s                                  |1m28s                                  |2m                                      |1m20s                            |1m36s                                  |1m56s                                  |1m44s                                  |
|Training cost|800$                                   |520$                                   |680$                                   |360$                                   |280$                                   |920$                                    |200$                             |440$                                   |840$                                   |600$                                   |
|Building     |[Research Lab 8](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Barracks 5](empireBarracks.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|


### Upgrading stats

|Level               |8      |5     |7      |3    |2    |10      |1    |4     |9       |6      |
|--------------------|-------|------|-------|-----|-----|--------|-----|------|--------|-------|
|Upgrade time        |4d     |10h   |2d12h  |1h30m|30m  |1w2d    |0s   |5h    |6d      |1d12h  |
|Upgrade requirements|320000$|25000$|160000$|6000$|3000$|1750000$|3000$|12500$|1000000$|100000$|


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

|Level                      |8   |5  |7   |3  |2  |10  |1  |4  |9   |6  |
|---------------------------|----|---|----|---|---|----|---|---|----|---|
|Displayed damage per second|1152|864|1056|672|576|1440|480|768|1248|960|


  * Cannons per sequence: 1
  * Cliptime: 2.250s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(0)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
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

|Level       |8                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |5                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |7                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |3                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |2                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |10                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |1                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |4                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |9                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |6                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Repair mults|**(2592)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1944)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(2376)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1512)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1296)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(3240)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1080)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(1728)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(2808)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|**(2160)**: Repair heavy vehicle, Repair heavy vehicule hero, Repair light vehicle, Repair vehicule hero, **(0)**: Repair droideka, Repair flying infantry, Repair flying vehicle, Repair headquarters, Repair heavy infantry, Repair heavy infantry hero, Repair infantry, Repair infantry hero, Repair other building, Repair ressource generator, Repair shield, Repair shield generator, Repair storage, Repair support troop, Repair trap, Repair turret, Repair wall|



## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Technician

|Level      |8          |5          |7          |3          |2          |10          |1          |4          |9          |6          |
|-----------|-----------|-----------|-----------|-----------|-----------|------------|-----------|-----------|-----------|-----------|
|Apply buffs|buffRepair8|buffRepair5|buffRepair7|buffRepair3|buffRepair2|buffRepair10|buffRepair1|buffRepair4|buffRepair9|buffRepair6|


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

|Level                      |8   |5  |7   |3  |2  |10  |1  |4  |9   |6  |
|---------------------------|----|---|----|---|---|----|---|---|----|---|
|Displayed damage per second|1152|864|1056|672|576|1440|480|768|1248|960|


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

|Level      |8     |5     |7     |3     |2     |10    |1     |4     |9     |6     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120508|120505|120507|120503|120502|120510|120501|120504|120509|120506|
|Point value|9.600 |7.200 |8.800 |5.600 |4.800 |12    |4     |6.400 |10.400|8     |


