---
title: Phase II Dark Trooper (Dark)
category: unit
---

# Phase II Dark Trooper (Dark) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 4
  * Type: infantry

|Level |1   |4    |10   |6    |9    |5    |7    |3   |2   |8    |
|------|----|-----|-----|-----|-----|-----|-----|----|----|-----|
|Health|7200|10880|20400|13600|17680|12240|14960|9520|8640|16320|


### Training stats

|Level        |1                                |4                                      |10                                      |6                                      |9                                      |5                                      |7                                      |3                                      |2                                      |8                                      |
|-------------|---------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|42s                              |48s                                    |2m                                      |52s                                    |1m56s                                  |50s                                    |54s                                    |46s                                    |44s                                    |1m52s                                  |
|Training cost|200$                             |440$                                   |920$                                    |600$                                   |840$                                   |520$                                   |680$                                   |360$                                   |280$                                   |800$                                   |
|Building     |[Barracks 2](empireBarracks.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |4     |10      |6      |9       |5     |7      |3    |2    |8      |
|--------------------|-----|------|--------|-------|--------|------|-------|-----|-----|-------|
|Upgrade time        |0s   |5h    |1w1d    |1d12h  |5d      |10h   |2d12h  |1h30m|30m  |3d12h  |
|Upgrade requirements|3000$|12500$|1750000$|100000$|1000000$|25000$|160000$|6000$|3000$|320000$|


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

## Main attack : Dark

### Targeting

  * Attack shield border: No
  * Max attack range: 5
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, _Flying infantry (60)_, _Flying vehicle (60)_, _Support troop (60)_, Droideka (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 500ms
  * Target locking: No

|Level          |1  |4  |10 |6  |9  |5  |7  |3, 2|8  |
|---------------|---|---|---|---|---|---|---|----|---|
|Damage per shot|304|416|780|520|676|468|572|364 |624|


### Projectile

|Level                       |1      |4  |10 |6  |9  |5  |7  |3, 2|8  |
|----------------------------|-------|---|---|---|---|---|---|----|---|
|Displayed damage per second |280    |384|720|480|624|432|528|336 |576|
|Calculated damage per second|280.615|384|720|480|624|432|528|336 |576|


  * Cannons per sequence: 1
  * Cliptime: 3.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Turret, Wall, **(50)**: Flying infantry, Flying vehicle, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(25)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Dark

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: darktrooper_emp-ani
  * Audio attack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_darktrooper_01":35,"sfx_ui_unitcomplete_darktrooper_02":35,"sfx_ui_unitcomplete_darktrooper_03":30
  * Buff asset offset: 0.00,0.42,0.00
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: darktrooper_emp-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 11.04,12.38,13.5
  * Icon closeup camera position: 0.77,1.01,11.04
  * Icon closeup lookat position: -0.03,3.09,-1.21
  * Icon lookat position: -0.02,1.7,0.06
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: Dark
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |4  |10 |6  |9  |5  |7  |3, 2|8  |
|---------------------------|---|---|---|---|---|---|---|----|---|
|Displayed damage per second|280|384|720|480|624|432|528|336 |576|


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

|Level      |1     |4     |10    |6     |9     |5     |7     |3     |2     |8     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |120201|120204|120210|120206|120209|120205|120207|120203|120202|120208|
|Point value|4     |6.400 |12    |8     |10.400|7.200 |8.800 |5.600 |4.800 |9.600 |


