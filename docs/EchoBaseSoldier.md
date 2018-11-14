---
title: Cold-weather Soldier (EchoBaseSoldier)
category: unit
---

# Cold-weather Soldier (EchoBaseSoldier)

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
  * Unit capacity: 1
  * Type: infantry

|Level |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|8100|7025|6475|5950|5400|4850|4325|3775|3500|2925|


### Training stats

|Level        |10                                     |9                                     |8                                     |7                                     |6                                     |5                                     |4                                     |3                                     |2                                     |1                               |
|-------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------|
|Training time|30s                                    |29s                                   |28s                                   |27s                                   |26s                                   |25s                                   |24s                                   |23s                                   |22s                                   |20s                             |
|Training cost|230$                                   |210$                                  |200$                                  |170$                                  |150$                                  |130$                                  |110$                                  |90$                                   |70$                                   |50$                             |
|Building     |[Research Lab 10](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Barracks 1](rebelBarracks.html)|


### Upgrading stats

|Level               |10      |9       |8      |7      |6      |5     |4     |3    |2    |1      |
|--------------------|--------|--------|-------|-------|-------|------|------|-----|-----|-------|
|Upgrade time        |1w1d    |5d      |3d12h  |2d     |1d     |8h    |3h30m |1h   |15m  |0s     |
|Upgrade requirements|1750000$|1000000$|320000$|160000$|100000$|25000$|12500$|4000$|1500$|Nothing|


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

## Main attack : Soldier

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Animation delay: 0s
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Reload time: 500ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 5
  * Shot delay: 100ms
  * Target locking: No

|Level          |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|880|760|700|640|590|530|470|410|380|320|


### Projectile

|Level                       |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |3340|2896|2672|2448|2228|2004|1780|1560|1448|1208|
|Calculated damage per second|3142|2714|2500|2285|2107|1892|1678|1464|1357|1142|
|Calculated damage per cycle |4400|3800|3500|3200|2950|2650|2350|2050|1900|1600|


  * Cannons per sequence: 1
  * Shooting cycle duration: 1.400s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: EchoBaseSoldier

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: echobasesoldier_rbl-ani
  * Audio attack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: echobasesoldier_rbl-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 11.3,12.63,13.85
  * Icon closeup camera position: 1.25,2.81,10.32
  * Icon closeup lookat position: -0.07,2.61,-0.75
  * Icon lookat position: -0.02,1.8,0.13
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: Soldier
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|3340|2896|2672|2448|2228|2004|1780|1560|1448|1208|


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

|Level|10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|270710|270709|270708|270707|270706|270705|270704|270703|270702|270701|


