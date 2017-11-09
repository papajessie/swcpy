---
title: Alliance Starfighter Pilot (XWingPilot)
category: unit
---

# Alliance Starfighter Pilot (XWingPilot) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Looter
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 3
  * Type: infantry

|Level |3   |9   |4   |10  |6   |5   |7   |8   |1   |2   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|7350|9250|7630|9610|8240|7930|8560|8900|6810|7070|


### Training stats

|Level        |3                                     |9                                     |4                                     |10                                     |6                                     |5                                     |7                                     |8                                     |1                               |2                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------|--------------------------------------|
|Training time|27s                                   |30s                                   |28s                                   |30s                                    |28s                                   |28s                                   |29s                                   |29s                                   |26s                             |27s                                   |
|Training cost|170$                                  |220$                                  |190$                                  |230$                                   |200$                                  |200$                                  |210$                                  |210$                                  |150$                            |160$                                  |
|Building     |[Research Lab 3](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Barracks 2](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|


### Upgrading stats

  * Upgrade requirements: 32 data fragments

|Level       |3  |9     |4     |10    |6     |5     |7  |8     |1     |2     |
|------------|---|------|------|------|------|------|---|------|------|------|
|Upgrade time|37m|44m35s|38m15s|45m50s|40m45s|39m30s|42m|43m15s|34m10s|35m45s|


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

### Modifiers

#### Modifier "Sum phtm X wing"

  * Sum phtm X wing apply value as: absolute
  * Sum phtm X wing buff ID: buffSumPhtmXWing
  * Sum phtm X wing duration: permanent
  * Sum phtm X wing modifier: summon
  * Sum phtm X wing ms first proc: 0s
  * Sum phtm X wing ms per proc: permanent
  * Sum phtm X wing name: Sum phtm X wing
  * Sum phtm X wing stack: 1
  * Sum phtm X wing target: self
  * Sum phtm X wing value: 1

|Level                          |3                                                    |9                                                    |4                                                    |10                                                    |6                                                    |5                                                    |7                                                    |8                                                    |1                                                    |2                                                    |
|-------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
|Sum phtm X wing summon visitors|["trp_title_PhantomXWing" level 3](PhantomXWing.html)|["trp_title_PhantomXWing" level 9](PhantomXWing.html)|["trp_title_PhantomXWing" level 4](PhantomXWing.html)|["trp_title_PhantomXWing" level 10](PhantomXWing.html)|["trp_title_PhantomXWing" level 6](PhantomXWing.html)|["trp_title_PhantomXWing" level 5](PhantomXWing.html)|["trp_title_PhantomXWing" level 7](PhantomXWing.html)|["trp_title_PhantomXWing" level 8](PhantomXWing.html)|["trp_title_PhantomXWing" level 1](PhantomXWing.html)|["trp_title_PhantomXWing" level 2](PhantomXWing.html)|


  * Sum phtm X wing summon die with summoner: Yes
  * Sum phtm X wing summon max proc: 1
  * Sum phtm X wing summon random spawn radius: 5
  * Sum phtm X wing summon same team: Yes
  * Sum phtm X wing summon spawn points: 0,0,0
  * Sum phtm X wing summon target summoner: No
  * Sum phtm X wing summon visitor type: Troop

|Level                              |3                    |9                    |4                    |10                    |6                    |5                    |7                    |8                    |1                    |2                    |
|-----------------------------------|---------------------|---------------------|---------------------|----------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|Sum phtm X wing summon visitor uids|troopRebPhantomXWing3|troopRebPhantomXWing9|troopRebPhantomXWing4|troopRebPhantomXWing10|troopRebPhantomXWing6|troopRebPhantomXWing5|troopRebPhantomXWing7|troopRebPhantomXWing8|troopRebPhantomXWing1|troopRebPhantomXWing2|


## Main attack : Scout

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * View range: 8

|Level             |3, 9, 4, 10, 6                                                                                                                                                                                                                                                                                                                                                                                               |5                                                                                                                                                                                                                                                                                                                                                                                                             |7, 8, 1, 2                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Target preferences|**Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|**Turret (100)**, _Ressource generator (80)_, _Storage (80)_, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|**Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|


### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * New target on reload: No
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 800ms
  * Retargeting offset: 8
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 200ms
  * Target locking: No

|Level          |3  |9  |4  |10 |6  |5  |7  |8  |1  |2  |
|---------------|---|---|---|---|---|---|---|---|---|---|
|Damage per shot|480|670|510|710|570|540|600|630|430|450|


### Projectile

|Level                       |3      |9       |4       |10      |6       |5       |7       |8       |1      |2      |
|----------------------------|-------|--------|--------|--------|--------|--------|--------|--------|-------|-------|
|Displayed damage per second |220    |330     |240     |360     |270     |250     |280     |310     |190    |210    |
|Calculated damage per second|993.103|1386.207|1055.172|1468.966|1179.310|1117.241|1241.379|1303.448|889.655|931.034|


  * Cannons per sequence: 1
  * Cliptime: 1.450s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Ressource generator, Storage, **(100)**: Droideka, Shield, **(75)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(50)**: Headquarters, Other building, Shield generator, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: XWingPilot
  * Upgrade shard uid: shrd_troopXWingPilot

|Level                     |3                |9                |4                |10                |6                |5                |7                |8                |1                |2                |
|--------------------------|-----------------|-----------------|-----------------|------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
|Spawn apply buffs         |buffSumPhtmXWing3|buffSumPhtmXWing9|buffSumPhtmXWing4|buffSumPhtmXWing10|buffSumPhtmXWing6|buffSumPhtmXWing5|buffSumPhtmXWing7|buffSumPhtmXWing8|buffSumPhtmXWing1|buffSumPhtmXWing2|
|Sum phtm X wing details   |sumPhtmXWing3    |sumPhtmXWing9    |sumPhtmXWing4    |sumPhtmXWing10    |sumPhtmXWing6    |sumPhtmXWing5    |sumPhtmXWing7    |sumPhtmXWing8    |sumPhtmXWing1    |sumPhtmXWing2    |
|Sum phtm X wing summon uid|sumPhtmXWing3    |sumPhtmXWing9    |sumPhtmXWing4    |sumPhtmXWing10    |sumPhtmXWing6    |sumPhtmXWing5    |sumPhtmXWing7    |sumPhtmXWing8    |sumPhtmXWing1    |sumPhtmXWing2    |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: xwingpilot_rbl-ani
  * Audio attack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_rebeltrooper_01":35,"sfx_ui_unitcomplete_rebeltrooper_02":35,"sfx_ui_unitcomplete_rebeltrooper_03":30
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: xwingpilot_rbl-ani
  * Death animation: buffFireBurn:15
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: resource
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 7.2,8.02,18.77
  * Icon closeup camera position: 3.52,5.89,9.71
  * Icon closeup lookat position: -0.45,2.02,-1.27
  * Icon lookat position: -0.39,1.33,-0.8
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: Scout
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: No
  * Unlocked by event: true
  * Unlocked by tournament: No

|Level                      |3          |9          |4          |10         |6          |5          |7          |8          |1             |2          |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|--------------|-----------|
|Displayed damage per second|220        |330        |240        |360        |270        |250        |280        |310        |190           |210        |
|Icon unlock position       |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|0,0,0         |(not found)|
|Icon unlock rotation       |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|0,0,0         |(not found)|
|Icon unlock scale          |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|1.25,1.25,1.25|(not found)|


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

|Level      |3     |9     |4     |10    |6     |5     |7     |8     |1     |2     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |314902|314908|314903|314909|314905|314904|314906|314907|314900|314901|
|Point value|1.400 |2.600 |1.600 |3     |2     |1.800 |2.200 |2.400 |1     |1.200 |


