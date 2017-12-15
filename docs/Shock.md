---
title: Shock Trooper (Shock)
category: unit
---

# Shock Trooper (Shock) — version 1106

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Breacher
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 3
  * Type: infantry
  * Unlock planet: Unlock on Tatooine

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|5760|6090|6440|6810|7210|7630|8080|8560|9070|9610|


### Training stats

|Level        |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|42s                              |44s                                    |46s                                    |48s                                    |50s                                    |52s                                    |54s                                    |1m52s                                  |1m56s                                  |2m                                      |
|Training cost|200$                             |280$                                   |360$                                   |440$                                   |520$                                   |600$                                   |680$                                   |800$                                   |840$                                   |920$                                    |
|Building     |[Barracks 1](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 5s
  * Upgrade requirements: 32 data fragments

### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

|Level                            |1 |2-10|
|---------------------------------|--|----|
|Propensity to go around obstacles|15|200 |


## Main attack : Shock Rocket

### Targeting

  * Attack shield border: No
  * Max attack range: 9
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Trap (90)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1)
  * View range: 21

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 3s
  * Retargeting offset: 18
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 250ms
  * Target locking: No

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2340|2512|2692|2892|3100|3332|3580|3852|4152|4470|


### Projectile

  * Splash damage percentages: 100,50,10,5

|Level                       |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |2340|2512|2692|2892|3100|3332|3580|3852|4152|4470|
|Calculated damage per second|668 |717 |769 |826 |885 |952 |1022|1100|1186|1277|
|Calculated damage per clip  |2340|2512|2692|2892|3100|3332|3580|3852|4152|4470|


  * Cannons per sequence: 1
  * Cliptime: 3.500s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(700)**: Wall, **(500)**: Trap, **(200)**: Headquarters, **(100)**: Droideka, Flying vehicle, Light vehicle, Vehicule hero, **(75)**: Heavy vehicle, Heavy vehicule hero, Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(50)**: Flying infantry, Infantry, Infantry hero, Support troop, **(25)**: Heavy infantry, Heavy infantry hero
  * Pass through shield: Yes
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: Shock
  * Upgrade shard uid: shrd_troopShock

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: shotrper_emp-ani
  * Audio attack: "sfx_attack_rocket_1":20,"sfx_attack_rocket_2":20,"sfx_attack_rocket_3":20,"sfx_attack_rocket_4":20,"sfx_attack_rocket_5":20
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio impact: "sfx_impact_rocket_01":35,"sfx_impact_rocket_02":35,"sfx_impact_rocket_03":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_stormtrooper_01":35,"sfx_ui_unitcomplete_stormtrooper_02":35,"sfx_ui_unitcomplete_stormtrooper_03":30
  * Bullet: fx_rocket_projectile_r_sm
  * Bundle name: shotrper_emp-ani
  * Death animation: buffFireBurn:15
  * Event button action: planet
  * Event button data: planet1
  * Event button string: hn_open_tat
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: trap
  * Gun position: "pathfndr_rbl_rig_MASTER_MOVER/pathfndr_rbl_rig_locator_gun_Rt":1
  * Hit spark: fx_shocktrooper_vanguard_hit
  * Icon camera position: 12.08,15.01,15.66
  * Icon closeup camera position: 0.64,0.41,9.27
  * Icon closeup lookat position: 0.07,2.85,0.16
  * Icon lookat position: -0.06,1.53,-0.1
  * Max scale: 100
  * Muzzle flash: fx_rocket_muzzle_r_sm
  * Name: Shock Rocket
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |1    |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|2340 |2512       |2692       |2892       |3100       |3332       |3580       |3852       |4152       |4470       |
|Icon unlock position       |0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation       |0,0,0|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |1,1,1|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


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
|Order      |121201|121202|121203|121204|121205|121206|121207|121208|121209|121210|
|Point value|3     |3.600 |4.200 |4.800 |5.400 |6     |6.600 |7.200 |7.800 |9     |


