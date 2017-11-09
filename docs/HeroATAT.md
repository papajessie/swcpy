---
title: Elite AT-AT (HeroATAT)
category: unit
---

# Elite AT-AT (HeroATAT) — version 1098

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

|Level |1    |4    |8    |9    |5    |3    |10   |6    |2    |7    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|24000|38400|57600|62400|43200|33600|72000|48000|28800|52800|


### Training stats

|Level        |1                                           |4                                      |8                                      |9                                      |5                                      |3                                      |10                                      |6                                      |2                                      |7                                      |
|-------------|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|3m30s                                       |4m                                     |4m40s                                  |4m50s                                  |4m10s                                  |3m50s                                  |5m                                      |4m20s                                  |3m40s                                  |4m30s                                  |
|Training cost|1000$                                       |2200$                                  |3800$                                  |4200$                                  |2600$                                  |1800$                                  |4600$                                   |3000$                                  |1400$                                  |3400$                                  |
|Building     |[Hero Command 5](empireTacticalCommand.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|


### Upgrading stats

|Level               |1    |4     |8      |9       |5     |3     |10      |6      |2    |7      |
|--------------------|-----|------|-------|--------|------|------|--------|-------|-----|-------|
|Upgrade time        |0s   |8h    |1w     |1w3d    |1d    |3h    |2w      |3d     |1h30m|5d     |
|Upgrade requirements|6500$|20000$|450000$|1500000$|50000$|10000$|2500000$|135000$|5000$|225000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: Yes
  * Flying unit: No
  * Max speed: 10
  * Propensity to go around obstacles: 200
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x2

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

|Level          |1  |4   |8   |9   |5   |3   |10  |6   |2   |7   |
|---------------|---|----|----|----|----|----|----|----|----|----|
|Damage per shot|844|1350|2025|2194|1519|1182|2532|1688|1013|1857|


### Projectile

|Level                       |1       |4   |8   |9       |5       |3       |10      |6       |2       |7       |
|----------------------------|--------|----|----|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |1800    |2880|4320|4680    |3240    |2521    |5401    |3601    |2161    |3961    |
|Calculated damage per second|3000.889|4800|7200|7800.889|5400.889|4202.667|9002.667|6001.778|3601.778|6602.667|


  * Cannons per sequence: 4
  * Cliptime: 2.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Shield, Shield generator, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 2

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: HeroATAT

|Level    |1    |4    |8    |9    |5    |3    |10    |6    |2    |7    |
|---------|-----|-----|-----|-----|-----|-----|------|-----|-----|-----|
|Hero data|hero1|hero4|hero8|hero9|hero5|hero3|hero10|hero6|hero2|hero7|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: atathero_emp-ani
  * Audio attack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * Audio death: "sfx_death_hero_walker_1":100
  * Audio placement: "sfx_placement_empire_atat_1":100
  * Buff asset offset: 0.00,4.96,0.0
  * Bullet: fx_blaster_beam_r_med
  * Bundle name: atathero_emp-ani
  * Decal asset name: tac_hero_emp
  * Decal bundle name: tac_hero_emp
  * Decal size: 320
  * Effect type: 2
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: shieldGenerator
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_r_med
  * Hologram uid: HeroHologramEmpire2
  * Icon camera position: 49.18,33.65,54.14
  * Icon lookat position: -2.41,4.25,-0.65
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_r_med
  * Name: HeroATAT
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1   |4   |8   |9   |5   |3   |10  |6   |2   |7   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|1800|2880|4320|4680|3240|2521|5401|3601|2161|3961|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 0
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |4     |8     |9     |5     |3     |10    |6     |2     |7     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |110501|110504|110508|110509|110505|110503|110510|110506|110502|110507|
|Point value|20    |32    |48    |52    |36    |28    |60    |40    |24    |44    |


