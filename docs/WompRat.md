---
title: Womp Rat (WompRat)
category: unit
---

# Womp Rat (WompRat) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Buildable unit: Yes
  * Role: Generic
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: infantry

|Level |1  |2  |3  |4   |5   |6   |7   |8   |9   |10  |
|------|---|---|---|----|----|----|----|----|----|----|
|Health|500|600|700|1920|2160|2400|2640|2880|3120|3600|


### Training stats


### Upgrading stats

  * Upgrade time: 0s

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|1500$|5000$|14000$|24000$|50000$|100000$|200000$|750000$|2000000$|4000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

|Level    |1, 2|3 |4, 5, 6, 7, 8, 9, 10|
|---------|----|--|--------------------|
|Max speed|40  |50|40                  |


## Main attack : WompRat

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * View range: 12

|Level             |1                                                                                                                                                                                                                                                                                                                                                                                                      |2, 3, 4, 5, 6, 7, 8, 9, 10                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Target preferences|**Turret (80)**, Droideka (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Headquarters (40), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Flying infantry (0), Flying vehicle (0), Trap (0)|**Support troop (100)**, _Turret (80)_, Droideka (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Headquarters (40), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Flying infantry (0), Flying vehicle (0), Trap (0)|


### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 0s
  * Retargeting offset: 4
  * Self-centered targeting: No
  * Shot count: 5
  * Time between shots: 1.250s
  * Target locking: No

|Level          |1 |2 |3 |4  |5  |6  |7  |8  |9  |10 |
|---------------|--|--|--|---|---|---|---|---|---|---|
|Damage per shot|55|65|76|437|492|546|601|656|710|819|


### Projectile

|Level                       |1 |2     |3     |4      |5      |6      |7      |8      |9      |10     |
|----------------------------|--|------|------|-------|-------|-------|-------|-------|-------|-------|
|Displayed damage per second |50|59    |69    |397    |447    |496    |546    |596    |645    |744    |
|Calculated damage per second|50|59.091|69.091|397.273|447.273|496.364|546.364|596.364|645.455|744.545|


  * Cannons per sequence: 1
  * Cliptime: 5.500s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, **(50)**: Trap, Turret, Wall, **(20)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Vehicule hero, **(0)**: Flying infantry, Flying vehicle
  * Pass through shield: No
  * Salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: WompRat

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 1000
  * Arcs: No
  * Audio attack: "sfx_attack_creatures_womprat_1":15,"sfx_attack_creatures_womprat_2":15,"sfx_attack_creatures_womprat_3":15,"sfx_attack_creatures_womprat_4":55
  * Audio death: "sfx_death_creatures_womprat_1":15,"sfx_death_creatures_womprat_2":15,"sfx_death_creatures_womprat_3":15,"sfx_attack_creatures_womprat_4":55
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: none
  * Max scale: 100
  * Name: WompRat
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1               |2                    |3                   |4               |5                    |6                   |7               |8                    |9                   |10                  |
|---------------------------|----------------|---------------------|--------------------|----------------|---------------------|--------------------|----------------|---------------------|--------------------|--------------------|
|Asset name                 |womprat_neu-ani |wompratmedium_neu-ani|wompratlarge_neu-ani|womprat_neu-ani |wompratmedium_neu-ani|wompratlarge_neu-ani|womprat_neu-ani |wompratmedium_neu-ani|wompratlarge_neu-ani|wompratlarge_neu-ani|
|Buff asset offset          |(not found)     |0.00,0.25,0.00       |0.00,0.33,0.00      |(not found)     |0.00,0.25,0.00       |0.00,0.33,0.00      |(not found)     |0.00,0.25,0.00       |0.00,0.33,0.00      |0.00,0.33,0.00      |
|Bundle name                |womprat_neu-ani |wompratmedium_neu-ani|wompratlarge_neu-ani|womprat_neu-ani |wompratmedium_neu-ani|wompratlarge_neu-ani|womprat_neu-ani |wompratmedium_neu-ani|wompratlarge_neu-ani|wompratlarge_neu-ani|
|Displayed damage per second|50              |59                   |69                  |397             |447                  |496                 |546             |596                  |645                 |744                 |
|Icon camera position       |11.42,11.67,7.56|13.51,14.12,9.05     |11.42,11.67,7.56    |11.42,11.67,7.56|13.51,14.12,9.05     |11.42,11.67,7.56    |11.42,11.67,7.56|13.51,14.12,9.05     |11.42,11.67,7.56    |11.42,11.67,7.56    |
|Icon lookat position       |-0.07,0.16,-0.08|-0.2,0.39,-0.08      |-0.07,0.16,-0.08    |-0.07,0.16,-0.08|-0.2,0.39,-0.08      |-0.07,0.16,-0.08    |-0.07,0.16,-0.08|-0.2,0.39,-0.08      |-0.07,0.16,-0.08    |-0.07,0.16,-0.08    |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |330901|330902|330903|330904|330905|330906|330907|330908|330909|330910|
|Point value|1     |1.200 |1.400 |1.600 |1.800 |2     |2.200 |2.400 |2.600 |3     |


