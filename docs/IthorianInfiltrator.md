---
title: Ithorian Infiltrator (IthorianInfiltrator)
category: unit
---

# Ithorian Infiltrator (IthorianInfiltrator)

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

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Health|1350|1600|1850|2100|2350|2600|2850|3100|3350|3600|


### Training stats

|Level        |1                               |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|--------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|2m40s                           |2m48s                                 |3m2s                                  |3m19s                                 |3m38s                                 |3m59s                                 |4m22s                                 |4m47s                                 |5m13s                                 |5m40s                                  |
|Training cost|1000$                           |1052$                                 |1137$                                 |1242$                                 |1361$                                 |1494$                                 |1638$                                 |1791$                                 |1954$                                 |2125$                                  |
|Building     |[Barracks 4](rebelBarracks.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


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

  * Animation delay: 0
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

|Level          |1   |2   |3   |4   |5   |6   |7    |8    |9    |10   |
|---------------|----|----|----|----|----|----|-----|-----|-----|-----|
|Damage per shot|2500|3775|5050|6325|7600|8875|10150|11425|12700|13975|


### Projectile

|Level                       |1   |2   |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|----|----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |4700|2545|3090 |3454 |3818 |4363 |4909 |5272 |5636 |6545 |
|Calculated damage per second|2040|3081|4122 |5163 |6204 |7244 |8285 |9326 |10367|11408|
|Calculated damage per clip  |5000|7550|10100|12650|15200|17750|20300|22850|25400|27950|


  * Cannons per sequence: 1
  * Cliptime: 2.450s
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

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|4700|2545|3090|3454|3818|4363|4909|5272|5636|6545|


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

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |234101|234102|234103|234104|234105|234106|234107|234108|234109|234110|
|Point value|3     |3.600 |4.200 |4.800 |5.400 |6     |6.600 |7.200 |7.800 |9     |


