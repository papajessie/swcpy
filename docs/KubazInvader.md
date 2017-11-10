---
title: Kubaz Invader (KubazInvader)
category: unit
---

# Kubaz Invader (KubazInvader) — version 1098

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

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|1350|1600|1850|2100|2350|2600|2850|3100|3350|3600|


### Training stats

|Level   |1                                |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|--------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Building|[Barracks 4](empireBarracks.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 0s
  * Upgrade requirements: 32 data fragments

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

  * Time between start of clip and first shot: 50ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 250ms
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 2
  * Time between shots: 200ms
  * Target locking: No

|Level          |1   |2   |3   |4   |5   |6   |7    |8    |9    |10   |
|---------------|----|----|----|----|----|----|-----|-----|-----|-----|
|Damage per shot|2500|3775|5050|6325|7600|8875|10150|11425|12700|13975|


### Projectile

|Level                       |1       |2       |3       |4       |5       |6       |7       |8        |9        |10       |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|---------|---------|---------|
|Displayed damage per second |4700    |2545    |3090    |3454    |3818    |4363    |4909    |5272     |5636     |6545     |
|Calculated damage per second|2222.222|3355.556|4488.889|5622.222|6755.556|7888.889|9022.222|10155.556|11288.889|12422.222|


  * Cannons per sequence: 1
  * Cliptime: 2.250s
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

  * Animation delay: 0
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

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|4700|2545|3090|3454|3818|4363|4909|5272|5636|6545|


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

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |134001|134002|134003|134004|134005|134006|134007|134008|134009|134010|
|Point value|3     |3.600 |4.200 |4.800 |5.400 |6     |6.600 |7.200 |7.800 |9     |


