---
title: Ithorian Infiltrator (IthorianInfiltrator)
category: unit
---

# Ithorian Infiltrator (IthorianInfiltrator) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 3
  * Type: infantry

|Level |6   |1   |5   |7   |9   |8   |4   |10  |3   |2   |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|2600|1350|2350|2850|3350|3100|2100|3600|1850|1600|


### Training stats

|Level        |6                                     |1                               |5                                     |7                                     |9                                     |8                                     |4                                     |10                                     |3                                     |2                                     |
|-------------|--------------------------------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|
|Training time|3m59s                                 |2m40s                           |3m38s                                 |4m22s                                 |5m13s                                 |4m47s                                 |3m19s                                 |5m40s                                  |3m2s                                  |2m48s                                 |
|Training cost|1494$                                 |1000$                           |1361$                                 |1638$                                 |1954$                                 |1791$                                 |1242$                                 |2125$                                  |1137$                                 |1052$                                 |
|Building     |[Research Lab 6](rebelOffenseLab.html)|[Barracks 4](rebelBarracks.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|


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

#### Modifier "Personal shield ithorian"

  * Personal shield ithorian apply value as: absolutePercent
  * Personal shield ithorian buff ID: buffPersonalShieldIthorian
  * Personal shield ithorian duration: 5s
  * Personal shield ithorian modifier: defense
  * Personal shield ithorian ms first proc: 0s
  * Personal shield ithorian ms per proc: permanent
  * Personal shield ithorian name: Personal shield ithorian
  * Personal shield ithorian stack: 1
  * Personal shield ithorian target: self
  * Personal shield ithorian value: 0


## Main attack : IthorianInfiltrator

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

|Level          |6   |1   |5   |7    |9    |8    |4   |10   |3   |2   |
|---------------|----|----|----|-----|-----|-----|----|-----|----|----|
|Damage per shot|8875|2500|7600|10150|12700|11425|6325|13975|5050|3775|


### Projectile

|Level                       |6       |1       |5       |7       |9        |8        |4       |10       |3       |2       |
|----------------------------|--------|--------|--------|--------|---------|---------|--------|---------|--------|--------|
|Displayed damage per second |4363    |4700    |3818    |4909    |5636     |5272     |3454    |6545     |3090    |2545    |
|Calculated damage per second|7888.889|2222.222|6755.556|9022.222|11288.889|10155.556|5622.222|12422.222|4488.889|3355.556|


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

  * Spawn apply buffs: buffPersonalShieldIthorian
  * Unit ID: IthorianInfiltrator
  * Upgrade shard uid: shrd_troopIthorianInfiltrator

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: ithorian_rbl-ani
  * Audio attack: "sfx_attack_ionblaster_1":25,"sfx_attack_ionblaster_2":25,"sfx_attack_ionblaster_3":25,"sfx_attack_ionblaster_4":25
  * Audio death: "sfx_death_ithorian_1":50,"sfx_death_ithorian_2":50
  * Audio placement: "sfx_placement_troop_1":33,"sfx_placement_troop_2":33,"sfx_placement_troop_3":33
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: ithorian_rbl-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: shieldGenerator
  * Hit spark: fx_blaster_hit_b_sm
  * Icon camera position: 17.05,12.75,14.83
  * Icon closeup camera position: 4.79,2.66,11.07
  * Icon closeup lookat position: -0.26,2.61,-0.85
  * Icon lookat position: 0,1.73,-0.07
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: IthorianInfiltrator
  * Personal shield ithorian asset name: ithorianshield_rbl-mod
  * Personal shield ithorian bundle name: ithorianshield_rbl-mod
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |6   |1   |5   |7   |9   |8   |4   |10  |3   |2   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|4363|4700|3818|4909|5636|5272|3454|6545|3090|2545|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Personal shield ithorian cancel tags: damage
  * Personal shield ithorian is refreshing: No
  * Personal shield ithorian prevent tags: damage
  * Personal shield ithorian tags: shield
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |6     |1     |5     |7     |9     |8     |4     |10    |3     |2     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |234106|234101|234105|234107|234109|234108|234104|234110|234103|234102|
|Point value|6     |3     |5.400 |6.600 |7.800 |7.200 |4.800 |9     |4.200 |3.600 |


