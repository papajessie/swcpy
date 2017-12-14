---
title: Imperial Astromedic (R5Medic)
category: unit
---

# Imperial Astromedic (R5Medic) — version 1105

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
  * Unit capacity: 5
  * Type: infantry

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|11700|12400|13100|13900|14600|15300|16000|16800|18100|19500|


### Training stats

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|1m40s                            |1m50s                                  |1m55s                                  |2m                                     |2m5s                                   |2m10s                                  |2m15s                                  |2m20s                                  |2m25s                                  |2m30s                                   |
|Training cost|250$                             |350$                                   |450$                                   |550$                                   |650$                                   |750$                                   |850$                                   |1000$                                  |1050$                                  |1150$                                   |
|Building     |[Barracks 2](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 5s
  * Upgrade requirements: 32 data fragments

### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * Support follow distance: 5

## Main attack : Medic

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Heavy infantry (50)**, **Heavy infantry hero (50)**, **Infantry (50)**, **Infantry hero (50)**, Droideka (0), Flying infantry (0), Flying vehicle (0), Headquarters (0), Heavy vehicle (0), Heavy vehicule hero (0), Light vehicle (0), Other building (0), Ressource generator (0), Shield (0), Shield generator (0), Storage (0), Support troop (0), Trap (0), Turret (0), Vehicule hero (0), Wall (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 50ms
  * Clip retargeting: No
  * Damage per shot: 0
  * Gun shooting sequence: 1
  * Impact delay: 250ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 900ms
  * Retargeting offset: 10
  * Self-centered targeting: Yes
  * Shot count: 2
  * Time between shots: 400ms
  * Target locking: Yes

### Projectile

  * Calculated damage per second: 0
  * Calculated damage per clip: 0
  * Splash damage percentages: 100,100,100,100

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|1550|1710|1810|1910|2010|2110|2210|2310|2490|2690|


  * Cannons per sequence: 1
  * Cliptime: 1.350s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(0)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 2

#### Modifier "Adv heal"

  * Adv heal apply value as: relative
  * Adv heal buff ID: buffAdvHeal
  * Adv heal duration: 250ms
  * Adv heal modifier: health
  * Adv heal ms first proc: 0s
  * Adv heal ms per proc: 251ms
  * Adv heal name: Adv heal
  * Adv heal stack: 0
  * Adv heal target: allies
  * Adv heal value: 0

|Level                      |1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Adv heal damage multipliers|**(1637)**: Adv heal infantry, Adv heal infantry hero, **(1091)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(1738)**: Adv heal infantry, Adv heal infantry hero, **(1158)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(1838)**: Adv heal infantry, Adv heal infantry hero, **(1226)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(1940)**: Adv heal infantry, Adv heal infantry hero, **(1293)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(2041)**: Adv heal infantry, Adv heal infantry hero, **(1361)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(2143)**: Adv heal infantry, Adv heal infantry hero, **(1428)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(2243)**: Adv heal infantry, Adv heal infantry hero, **(1495)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(2344)**: Adv heal infantry, Adv heal infantry hero, **(1563)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(2525)**: Adv heal infantry, Adv heal infantry hero, **(1684)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|**(2727)**: Adv heal infantry, Adv heal infantry hero, **(1818)**: Adv heal heavy infantry, Adv heal heavy infantry hero, **(0)**: Adv heal droideka, Adv heal flying infantry, Adv heal flying vehicle, Adv heal headquarters, Adv heal heavy vehicle, Adv heal heavy vehicule hero, Adv heal light vehicle, Adv heal other building, Adv heal ressource generator, Adv heal shield, Adv heal shield generator, Adv heal storage, Adv heal support troop, Adv heal trap, Adv heal turret, Adv heal vehicule hero, Adv heal wall|



## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: R5Medic
  * Upgrade shard uid: shrd_troopR5Medic

|Level      |1           |2           |3           |4           |5           |6           |7           |8           |9           |10           |
|-----------|------------|------------|------------|------------|------------|------------|------------|------------|------------|-------------|
|Apply buffs|buffAdvHeal1|buffAdvHeal2|buffAdvHeal3|buffAdvHeal4|buffAdvHeal5|buffAdvHeal6|buffAdvHeal7|buffAdvHeal8|buffAdvHeal9|buffAdvHeal10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Adv heal asset name: fx_healing_condition
  * Adv heal bundle name: fx_healing
  * Animation delay: 0
  * Arcs: No
  * Asset name: r5droid_emp-ani
  * Audio attack: "sfx_attack_droid_medic_1":50,"sfx_attack_droid_medic_2":50
  * Audio death: "sfx_death_droid_r5_01":50,"sfx_death_droid_r5_02":50
  * Audio placement: "sfx_placement_droid_r5_01":50,"sfx_placement_droid_r5_02":50
  * Audio train: "sfx_ui_unitcomplete_r5droid_01":50,"sfx_ui_unitcomplete_r5droid_02":50
  * Bundle name: r5droid_emp-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Icon camera position: 5.21,9.06,13.12
  * Icon lookat position: -0.19,0.88,-0.37
  * Info UI type: Healer
  * Max scale: 200
  * Muzzle flash: fx_healing_ring
  * Name: Medic
  * Spin speed: 0
  * Targeted type: ALLIES
  * Unlocked by event: true

|Level                      |1    |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|1550 |1710       |1810       |1910       |2010       |2110       |2210       |2310       |2490       |2690       |
|Icon unlock position       |0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation       |0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |1,1,1|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Adv heal is refreshing: No
  * Adv heal tags: heal
  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Seeks target: No
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |134401|134402|134403|134404|134405|134406|134407|134408|134409|134410|
|Point value|5     |6     |7     |8     |9     |10    |11    |12    |13    |15    |


