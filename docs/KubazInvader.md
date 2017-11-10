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

|Level |7   |5   |10  |6   |8   |4   |9   |1   |3   |2   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2850|2350|3600|2600|3100|2100|3350|1350|1850|1600|


### Training stats

|Level        |7                                      |5                                      |10                                      |6                                      |8                                      |4                                      |9                                      |1                                |3                                      |2                                      |
|-------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------|---------------------------------------|---------------------------------------|
|Training time|4m22s                                  |3m38s                                  |5m40s                                   |3m59s                                  |4m47s                                  |3m19s                                  |5m13s                                  |2m40s                            |3m2s                                   |2m48s                                  |
|Training cost|1638$                                  |1361$                                  |2125$                                   |1494$                                  |1791$                                  |1242$                                  |1954$                                  |1000$                            |1137$                                  |1052$                                  |
|Building     |[Research Lab 7](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Barracks 4](empireBarracks.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|


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

|Level          |7    |5   |10   |6   |8    |4   |9    |1   |3   |2   |
|---------------|-----|----|-----|----|-----|----|-----|----|----|----|
|Damage per shot|10150|7600|13975|8875|11425|6325|12700|2500|5050|3775|


### Projectile

|Level                       |7       |5       |10       |6       |8        |4       |9        |1       |3       |2       |
|----------------------------|--------|--------|---------|--------|---------|--------|---------|--------|--------|--------|
|Displayed damage per second |4909    |3818    |6545     |4363    |5272     |3454    |5636     |4700    |3090    |2545    |
|Calculated damage per second|9022.222|6755.556|12422.222|7888.889|10155.556|5622.222|11288.889|2222.222|4488.889|3355.556|


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

|Level                      |7   |5   |10  |6   |8   |4   |9   |1   |3   |2   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|4909|3818|6545|4363|5272|3454|5636|4700|3090|2545|


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

|Level      |7     |5     |10    |6     |8     |4     |9     |1     |3     |2     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |134007|134005|134010|134006|134008|134004|134009|134001|134003|134002|
|Point value|6.600 |5.400 |9     |6     |7.200 |4.800 |7.800 |3     |4.200 |3.600 |


