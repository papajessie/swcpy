---
title: Medic Droid (Medic)
category: unit
---

# Medic Droid (Medic) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: healerInfantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Healer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry

|Level |9    |8    |6    |4    |1   |5    |2   |3   |10   |7    |
|------|-----|-----|-----|-----|----|-----|----|----|-----|-----|
|Health|16900|15600|13000|10400|6500|11700|7800|9100|19500|14300|


### Training stats

|Level        |9                                     |8                                     |6                                     |4                                     |1                               |5                                     |2                                     |3                                     |10                                     |7                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|
|Training time|2m25s                                 |2m20s                                 |2m10s                                 |2m                                    |1m40s                           |2m5s                                  |1m50s                                 |1m55s                                 |2m30s                                  |2m15s                                 |
|Training cost|1050$                                 |1000$                                 |750$                                  |550$                                  |250$                            |650$                                  |350$                                  |450$                                  |1150$                                  |850$                                  |
|Building     |[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Barracks 5](rebelBarracks.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|


### Upgrading stats

|Level               |9       |8      |6      |4     |1    |5     |2    |3    |10      |7      |
|--------------------|--------|-------|-------|------|-----|------|-----|-----|--------|-------|
|Upgrade time        |6d      |4d     |1d12h  |5h    |0s   |10h   |30m  |1h30m|1w2d    |2d12h  |
|Upgrade requirements|1000000$|350000$|115000$|15000$|3000$|35000$|3000$|6000$|2000000$|175000$|


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
  * Splash damage percentages: 100,100,100,100

|Level                      |9   |8   |6   |4   |1  |5   |2   |3   |10  |7   |
|---------------------------|----|----|----|----|---|----|----|----|----|----|
|Displayed damage per second|2334|2155|1795|1437|865|1616|1078|1257|2693|1976|


  * Cannons per sequence: 1
  * Cliptime: 1.350s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(0)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 2

#### Modifier "Heal"

  * Heal apply value as: relative
  * Heal buff ID: buffHeal
  * Heal duration: 250ms
  * Heal modifier: health
  * Heal ms first proc: 0s
  * Heal ms per proc: 251ms
  * Heal name: Heal
  * Heal stack: 0
  * Heal target: allies
  * Heal value: 0

|Level     |9                                                                                                                                                                                                                                                                                                                                                                                                                                           |8                                                                                                                                                                                                                                                                                                                                                                                                                                           |6                                                                                                                                                                                                                                                                                                                                                                                                                                           |4                                                                                                                                                                                                                                                                                                                                                                                                                                          |1                                                                                                                                                                                                                                                                                                                                                                                                                                         |5                                                                                                                                                                                                                                                                                                                                                                                                                                           |2                                                                                                                                                                                                                                                                                                                                                                                                                                          |3                                                                                                                                                                                                                                                                                                                                                                                                                                          |10                                                                                                                                                                                                                                                                                                                                                                                                                                          |7                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Heal mults|**(2364)**: Heal infantry, Heal infantry hero, **(1576)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(2183)**: Heal infantry, Heal infantry hero, **(1455)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(1818)**: Heal infantry, Heal infantry hero, **(1212)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(1455)**: Heal infantry, Heal infantry hero, **(970)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(909)**: Heal infantry, Heal infantry hero, **(606)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(1637)**: Heal infantry, Heal infantry hero, **(1091)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(1092)**: Heal infantry, Heal infantry hero, **(728)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(1274)**: Heal infantry, Heal infantry hero, **(849)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(2727)**: Heal infantry, Heal infantry hero, **(1818)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|**(2001)**: Heal infantry, Heal infantry hero, **(1334)**: Heal heavy infantry, Heal heavy infantry hero, **(0)**: Heal droideka, Heal flying infantry, Heal flying vehicle, Heal headquarters, Heal heavy vehicle, Heal heavy vehicule hero, Heal light vehicle, Heal other building, Heal ressource generator, Heal shield, Heal shield generator, Heal storage, Heal support troop, Heal trap, Heal turret, Heal vehicule hero, Heal wall|



## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Medic

|Level      |9        |8        |6        |4        |1        |5        |2        |3        |10        |7        |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|----------|---------|
|Apply buffs|buffHeal9|buffHeal8|buffHeal6|buffHeal4|buffHeal1|buffHeal5|buffHeal2|buffHeal3|buffHeal10|buffHeal7|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: medicdroid_rbl-ani
  * Audio attack: "sfx_attack_droid_medic_1":50,"sfx_attack_droid_medic_2":50
  * Audio death: "sfx_death_droid_medic_1":50,"sfx_death_droid_medic_2":50
  * Audio placement: "sfx_placement_droid_medic_1":50,"sfx_placement_droid_medic_2":50
  * Audio train: "sfx_ui_unitcomplete_droid_01":50,"sfx_ui_unitcomplete_droid_02":50
  * Bundle name: medicdroid_rbl-ani
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: infantry
  * Heal asset name: fx_healing_condition
  * Heal bundle name: fx_healing
  * Icon camera position: 6.65,6.07,11.15
  * Icon closeup camera position: 1.36,0.58,8.63
  * Icon closeup lookat position: 0.03,1.47,-0.14
  * Icon lookat position: 0.26,1.17,0.34
  * Info UI type: Healer
  * Max scale: 200
  * Muzzle flash: fx_healing_ring
  * Name: Medic
  * Spin speed: 0
  * Targeted type: ALLIES

|Level                      |9   |8   |6   |4   |1  |5   |2   |3   |10  |7   |
|---------------------------|----|----|----|----|---|----|----|----|----|----|
|Displayed damage per second|2334|2155|1795|1437|865|1616|1078|1257|2693|1976|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Heal is refreshing: No
  * Heal tags: heal
  * Max scale: No
  * Seeks target: No
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |9     |8     |6     |4     |1     |5     |2     |3     |10    |7     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |220509|220508|220506|220504|220501|220505|220502|220503|220510|220507|
|Point value|13    |12    |10    |8     |5     |9     |6     |7     |15    |11    |


