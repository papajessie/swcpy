---
title: Desert Soldier (SandSoldier)
category: unit
---

# Desert Soldier (SandSoldier) — version 1098

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

|Level |2   |10  |9   |1   |6   |3   |5   |8   |7   |4   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|3500|8100|7025|2925|5400|3775|4850|6475|5950|4325|


### Training stats

|Level        |2                                     |10                                     |9                                     |1                               |6                                     |3                                     |5                                     |8                                     |7                                     |4                                     |
|-------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|22s                                   |30s                                    |29s                                   |20s                             |26s                                   |23s                                   |25s                                   |28s                                   |27s                                   |24s                                   |
|Training cost|70$                                   |230$                                   |210$                                  |50$                             |150$                                  |90$                                   |130$                                  |200$                                  |170$                                  |110$                                  |
|Building     |[Research Lab 2](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Barracks 1](rebelBarracks.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|


### Upgrading stats

|Level               |2    |10      |9       |1      |6      |3    |5     |8      |7      |4     |
|--------------------|-----|--------|--------|-------|-------|-----|------|-------|-------|------|
|Upgrade time        |15m  |1w1d    |5d      |0s     |1d     |1h   |8h    |3d12h  |2d     |3h30m |
|Upgrade requirements|1500$|1750000$|1000000$|Nothing|100000$|4000$|25000$|320000$|160000$|12500$|


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

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 5
  * Time between shots: 100ms
  * Target locking: No

|Level          |2  |10 |9  |1  |6  |3  |5  |8  |7  |4  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|380|880|760|320|590|410|530|700|640|470|


### Projectile

|Level                       |2       |10      |9       |1       |6       |3       |5       |8   |7       |4       |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|----|--------|--------|
|Displayed damage per second |1448    |3340    |2896    |1208    |2228    |1560    |2004    |2672|2448    |1780    |
|Calculated damage per second|1357.143|3142.857|2714.286|1142.857|2107.143|1464.286|1892.857|2500|2285.714|1678.571|


  * Cannons per sequence: 1
  * Cliptime: 1.400s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SandSoldier

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Audio attack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Bullet: fx_blaster_beam_b_sm
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: closest
  * Gun position: "soldier_rbl_rig_MASTER_MOVER/soldier_rbl_rig_locator_gun":1
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

|Level                      |2                  |10                 |9                  |1                       |6                  |3                  |5                  |8                  |7                  |4                  |
|---------------------------|-------------------|-------------------|-------------------|------------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|Asset name                 |sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandheavysoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|
|Bundle name                |sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandheavysoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|sandsoldier_rbl-ani|
|Displayed damage per second|1448               |3340               |2896               |1208                    |2228               |1560               |2004               |2672               |2448               |1780               |


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

|Level|2     |10    |9     |1     |6     |3     |5     |8     |7     |4     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|300021|300029|300028|300020|300025|300022|300024|300027|300026|300023|


