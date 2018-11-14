---
title: Kubaz Invader (KubazInvader)
category: unit
---

# Kubaz Invader (KubazInvader)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 3
  * Type: infantry

|Level |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------|----|----|----|----|----|----|----|----|----|----|----|
|Health|3750|3600|3350|3100|2850|2600|2350|2100|1850|1600|1350|


### Training stats

|Level        |11                                      |10                                      |9                                      |8                                      |7                                      |6                                      |5                                      |4                                      |3                                      |2                                      |1                                |
|-------------|----------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|
|Training time|6m7s                                    |5m40s                                   |5m13s                                  |4m47s                                  |4m22s                                  |3m59s                                  |3m38s                                  |3m19s                                  |3m2s                                   |2m48s                                  |2m40s                            |
|Training cost|2296$                                   |2125$                                   |1954$                                  |1791$                                  |1638$                                  |1494$                                  |1361$                                  |1242$                                  |1137$                                  |1052$                                  |1000$                            |
|Building     |[Research Lab 11](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Barracks 1](empireBarracks.html)|


### Upgrading stats

  * Upgrade requirements: 32 data fragments

|Level       |11|1-10|
|------------|--|----|
|Upgrade time|5s|0s  |


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 45
  * Propensity to go around obstacles: 200
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

### Modifiers

#### Modifier "Personal shield kubaz"

  * Personal shield kubaz apply value as: absolutePercent
  * Personal shield kubaz buff ID: buffPersonalShieldKubaz
  * Personal shield kubaz duration: 5s
  * Personal shield kubaz modifier: defense
  * Personal shield kubaz ms first proc: 0s
  * Personal shield kubaz ms per proc: permanent
  * Personal shield kubaz name: Personal shield kubaz
  * Personal shield kubaz stack: 1
  * Personal shield kubaz target: self
  * Personal shield kubaz value: 0


## Main attack : KubazInvader

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Shield (80)**, **Shield generator (80)**, _Ressource generator (60)_, _Storage (60)_, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Support troop (50), Turret (40), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Animation delay: 0s
  * Charge time: 50ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 250ms
  * Can shoot over walls: No
  * Reload time: 2s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 2
  * Shot delay: 200ms
  * Target locking: No

|Level          |11   |10   |9    |8    |7    |6   |5   |4   |3   |2   |1   |
|---------------|-----|-----|-----|-----|-----|----|----|----|----|----|----|
|Damage per shot|14740|13975|12700|11425|10150|8875|7600|6325|5050|3775|2500|


### Projectile

|Level                       |11   |10   |9    |8    |7    |6    |5    |4    |3    |2   |1   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|----|
|Displayed damage per second |6872 |6545 |5636 |5272 |4909 |4363 |3818 |3454 |3090 |2545|1380|
|Calculated damage per second|13102|12422|11288|10155|9022 |7888 |6755 |5622 |4488 |3355|2222|
|Calculated damage per cycle |29480|27950|25400|22850|20300|17750|15200|12650|10100|7550|5000|


  * Cannons per sequence: 1
  * Shooting cycle duration: 2.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 15
  * Damage multipliers: **(600)**: Shield generator, **(100)**: Shield, **(60)**: Ressource generator, **(50)**: Storage, Wall, **(10)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Support troop, Turret, Vehicule hero, **(0)**: Trap
  * Pass through shield: Yes
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffPersonalShieldKubaz
  * Unit ID: KubazInvader
  * Upgrade shard uid: shrd_troopKubazInvader

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: kubaz_emp-ani
  * Audio attack: "sfx_attack_ionblaster_1":25,"sfx_attack_ionblaster_2":25,"sfx_attack_ionblaster_3":25,"sfx_attack_ionblaster_4":25
  * Audio death: "sfx_death_kubaz_1":50,"sfx_death_kubaz_2":50
  * Audio placement: "sfx_placement_troop_1":33,"sfx_placement_troop_2":33,"sfx_placement_troop_3":33
  * Bullet: fx_blaster_beam_r_sm
  * Bundle name: kubaz_emp-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: shieldGenerator
  * Hit spark: fx_blaster_hit_r_sm
  * Icon camera position: 8.96,11.37,18.33
  * Icon closeup camera position: 4.16,3.05,10.68
  * Icon closeup lookat position: 0.04,2.7,-0.25
  * Icon lookat position: -0.48,1.32,-0.72
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_sm
  * Name: KubazInvader
  * Personal shield kubaz asset name: kubazshield_emp-mod
  * Personal shield kubaz bundle name: kubazshield_emp-mod
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |11                           |10         |9          |8          |7          |6          |5          |4          |3          |2          |1          |
|---------------------------|-----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |vfx_prestige_deploy_small_emp|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|6872                         |6545       |5636       |5272       |4909       |4363       |3818       |3454       |3090       |2545       |1380       |
|Prestige                   |true                         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Personal shield kubaz cancel tags: damage
  * Personal shield kubaz is refreshing: No
  * Personal shield kubaz prevent tags: damage
  * Personal shield kubaz tags: shield
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |11   |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Order      |61011|61010|61009|61008|61007|61006|61005|61004|61003|61002|61001|
|Point value|9    |9    |7.800|7.200|6.600|6    |5.400|4.800|4.200|3.600|3    |


