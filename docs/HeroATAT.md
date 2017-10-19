---
title: Elite AT-AT (HeroATAT)
category: unit
---

# Elite AT-AT (HeroATAT) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: hero
  * _Not found: Buff health, Can be given, Unlock planet_

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|24000|28800|33600|38400|43200|48000|52800|57600|62400|72000|


### Training stats

|Level        |1                                           |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|3m30s                                       |3m40s                                  |3m50s                                  |4m                                     |4m10s                                  |4m20s                                  |4m30s                                  |4m40s                                  |4m50s                                  |5m                                      |
|Training cost|1000$                                       |1400$                                  |1800$                                  |2200$                                  |2600$                                  |3000$                                  |3400$                                  |3800$                                  |4200$                                  |4600$                                   |
|Building     |[Hero Command 5](empireTacticalCommand.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade time        |0s   |1h30m|3h    |8h    |1d    |3d     |5d     |1w     |1w3d    |2w      |
|Upgrade requirements|6500$|5000$|10000$|20000$|50000$|135000$|225000$|450000$|1500000$|2500000$|


### Move stats

  * Acceleration: 0
  * Crushes walls: Yes
  * Flying unit: No
  * Max speed: 10
  * Propensity to go around obstacles: 200
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2
  * _Not found: Ignores walls, Support follow distance_

## Main attack : HeroATAT

### Targeting

  * Attack shield border: Yes
  * Max attack range: 10
  * Min attack range: 1
  * New rotation speed: 3927
  * Target preference strength: 90
  * Target preferences: **Shield (80)**, **Shield generator (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Storage (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,1,1,1
  * Impact delay: 500ms
  * Can shoot over walls: Yes
  * Time between end of clip and start of clip: 1.500s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 8
  * Time between shots: 250ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1  |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|---|----|----|----|----|----|----|----|----|----|
|Damage per shot|844|1013|1182|1350|1519|1688|1857|2025|2194|2532|


### Projectile

  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1       |2       |3       |4   |5       |6       |7       |8   |9       |10      |
|----------------------------|--------|--------|--------|----|--------|--------|--------|----|--------|--------|
|Displayed damage per second |1800    |2161    |2521    |2880|3240    |3601    |3961    |4320|4680    |5401    |
|Calculated damage per second|3000.889|3601.778|4202.667|4800|5400.889|6001.778|6602.667|7200|7800.889|9002.667|


  * Cannons per sequence: 4
  * Cliptime: 2.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400%)**: Shield, Shield generator, **(100%)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75%)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 2
  * _Not found: Length segments, Width segments_

## Other stats

### Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: HeroATAT
  * _Not found: Ability, Apply buffs, Death projectile, Projectile type, Self buff, Spawn apply buffs, Upgrade shard uid_

|Level    |1    |2    |3    |4    |5    |6    |7    |8    |9    |10    |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
|Hero data|hero1|hero2|hero3|hero4|hero5|hero6|hero7|hero8|hero9|hero10|


### Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: atathero_emp-ani
  * Audio attack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * Audio death: "sfx_death_hero_walker_1":100
  * Audio placement: "sfx_placement_empire_atat_1":100
  * Buff asset offset: 0.00,4.96,0.0
  * Bundle name: atathero_emp-ani
  * Decal asset name: tac_hero_emp
  * Decal bundle name: tac_hero_emp
  * Decal size: 320
  * Effect type: 2
  * Factory rotation: 0
  * Factory scale factor: 1
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hologram uid: HeroHologramEmpire2
  * Icon camera position: 49.18,33.65,54.14
  * Icon lookat position: -2.41,4.25,-0.65
  * Targeted type: ENEMIES
  * _Not found: Audio impact, Audio train, Death animation, Event button action, Event button data, Event button string, Event features string, Icon closeup camera position, Icon closeup lookat position, Icon unlock position, Icon unlock rotation, Icon unlock scale, Info UI type, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by event, Unlocked by tournament_

### Attack presentation stats

  * Animation delay: 0
  * Favorite target type: shieldGenerator
  * Arcs: No
  * Bullet: fx_blaster_beam_r_med
  * Hit spark: fx_blaster_hit_r_med
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_med
  * Name: HeroATAT
  * Spin speed: 0
  * _Not found: Charge asset name, Ground bullet, Muzzle flash fade time, Projectile length, S transition_

|Level                      |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|1800|2161|2521|2880|3240|3601|3961|4320|4680|5401|


### Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 0
  * Max scale: No
  * Splash: 0
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |110501|110502|110503|110504|110505|110506|110507|110508|110509|110510|
|Point value|20    |24    |28    |32    |36    |40    |44    |48    |52    |60    |


### Uninterpreted attack stats

  * Arming delay: 0
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: No
  * _Not found: S1 time, S2 time_

