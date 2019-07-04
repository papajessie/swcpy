---
title: Womp Rat (WompRat)
category: unit
---

# Womp Rat (WompRat)

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

|Level |10  |9   |8   |7   |6   |5   |4   |3  |2  |1  |
|------|----|----|----|----|----|----|----|---|---|---|
|Health|3600|3120|2880|2640|2400|2160|1920|700|600|500|


### Training stats

|Level        |10  |9   |8   |7   |6   |5   |4   |3  |2  |1  |
|-------------|----|----|----|----|----|----|----|---|---|---|
|Training time|6s  |6s  |6s  |5s  |5s  |5s  |5s  |5s |4s |4s |
|Training cost|230$|210$|190$|170$|150$|130$|110$|90$|70$|50$|


### Upgrading stats

  * Upgrade time: 0s

|Level               |10      |9       |8      |7      |6      |5     |4     |3     |2    |1    |
|--------------------|--------|--------|-------|-------|-------|------|------|------|-----|-----|
|Upgrade requirements|4000000$|2000000$|750000$|200000$|100000$|50000$|24000$|14000$|5000$|1500$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

|Level    |4-10|3 |1-2|
|---------|----|--|---|
|Max speed|40  |50|40 |


## Main attack : WompRat

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * View range: 12

|Level             |2-10                                                                                                                                                                                                                                                                                                                                                                                                      |1                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Target preferences|**Support troop (100)**, _Turret (80)_, Droideka (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Headquarters (40), Flying infantry (1), Flying vehicle (1), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|**Turret (80)**, Droideka (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Headquarters (40), Flying infantry (1), Flying vehicle (1), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|


### Shooting

  * Animation delay: 1s
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Reload time: 0s
  * Retargeting offset: 4
  * Self-centered targeting: No
  * Shot count: 5
  * Shot delay: 1.250s
  * Target locking: No

|Level          |10 |9  |8  |7  |6  |5  |4  |3 |2 |1 |
|---------------|---|---|---|---|---|---|---|--|--|--|
|Damage per shot|819|710|656|601|546|492|437|76|65|55|


### Projectile

|Level                       |10   |9   |8   |7   |6   |5   |4   |3  |2  |1  |
|----------------------------|-----|----|----|----|----|----|----|---|---|---|
|Displayed damage per second |11676|645 |596 |546 |496 |447 |397 |69 |59 |50 |
|Calculated damage per second|348  |302 |279 |255 |232 |209 |185 |32 |27 |23 |
|Calculated damage per cycle |4095 |3550|3280|3005|2730|2460|2185|380|325|275|


  * Cannons per sequence: 1
  * Shooting cycle duration: 11.750s
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

|Level                      |10                  |9                   |8                    |7               |6                   |5                    |4               |3                   |2                    |1               |
|---------------------------|--------------------|--------------------|---------------------|----------------|--------------------|---------------------|----------------|--------------------|---------------------|----------------|
|Asset name                 |wompratlarge_neu-ani|wompratlarge_neu-ani|wompratmedium_neu-ani|womprat_neu-ani |wompratlarge_neu-ani|wompratmedium_neu-ani|womprat_neu-ani |wompratlarge_neu-ani|wompratmedium_neu-ani|womprat_neu-ani |
|Buff asset offset          |0.00,0.33,0.00      |0.00,0.33,0.00      |0.00,0.25,0.00       |(not found)     |0.00,0.33,0.00      |0.00,0.25,0.00       |(not found)     |0.00,0.33,0.00      |0.00,0.25,0.00       |(not found)     |
|Bundle name                |wompratlarge_neu-ani|wompratlarge_neu-ani|wompratmedium_neu-ani|womprat_neu-ani |wompratlarge_neu-ani|wompratmedium_neu-ani|womprat_neu-ani |wompratlarge_neu-ani|wompratmedium_neu-ani|womprat_neu-ani |
|Displayed damage per second|11676               |645                 |596                  |546             |496                 |447                  |397             |69                  |59                   |50              |
|Icon camera position       |11.42,11.67,7.56    |11.42,11.67,7.56    |13.51,14.12,9.05     |11.42,11.67,7.56|11.42,11.67,7.56    |13.51,14.12,9.05     |11.42,11.67,7.56|11.42,11.67,7.56    |13.51,14.12,9.05     |11.42,11.67,7.56|
|Icon lookat position       |-0.07,0.16,-0.08    |-0.07,0.16,-0.08    |-0.2,0.39,-0.08      |-0.07,0.16,-0.08|-0.07,0.16,-0.08    |-0.2,0.39,-0.08      |-0.07,0.16,-0.08|-0.07,0.16,-0.08    |-0.2,0.39,-0.08      |-0.07,0.16,-0.08|


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

|Level      |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |460210|460209|460208|460207|460206|460205|460204|460203|460202|460201|
|Point value|3     |2.600 |2.400 |2.200 |2     |1.800 |1.600 |1.400 |1.200 |1     |


