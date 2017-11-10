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

|Level |6    |3    |4    |1    |7    |10   |8    |5    |2    |9    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|48000|33600|38400|24000|52800|72000|57600|43200|28800|62400|


### Training stats

|Level        |6                                      |3                                      |4                                      |1                                           |7                                      |10                                      |8                                      |5                                      |2                                      |9                                      |
|-------------|---------------------------------------|---------------------------------------|---------------------------------------|--------------------------------------------|---------------------------------------|----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|4m20s                                  |3m50s                                  |4m                                     |3m30s                                       |4m30s                                  |5m                                      |4m40s                                  |4m10s                                  |3m40s                                  |4m50s                                  |
|Training cost|3000$                                  |1800$                                  |2200$                                  |1000$                                       |3400$                                  |4600$                                   |3800$                                  |2600$                                  |1400$                                  |4200$                                  |
|Building     |[Research Lab 6](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Hero Command 5](empireTacticalCommand.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|


### Upgrading stats

|Level               |6      |3     |4     |1    |7      |10      |8      |5     |2    |9       |
|--------------------|-------|------|------|-----|-------|--------|-------|------|-----|--------|
|Upgrade time        |3d     |3h    |8h    |0s   |5d     |2w      |1w     |1d    |1h30m|1w3d    |
|Upgrade requirements|135000$|10000$|20000$|6500$|225000$|2500000$|450000$|50000$|5000$|1500000$|


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

|Level          |6   |3   |4   |1  |7   |10  |8   |5   |2   |9   |
|---------------|----|----|----|---|----|----|----|----|----|----|
|Damage per shot|1688|1182|1350|844|1857|2532|2025|1519|1013|2194|


### Projectile

|Level                       |6       |3       |4   |1       |7       |10      |8   |5       |2       |9       |
|----------------------------|--------|--------|----|--------|--------|--------|----|--------|--------|--------|
|Displayed damage per second |3601    |2521    |2880|1800    |3961    |5401    |4320|3240    |2161    |4680    |
|Calculated damage per second|6001.778|4202.667|4800|3000.889|6602.667|9002.667|7200|5400.889|3601.778|7800.889|


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

|Level    |6    |3    |4    |1    |7    |10    |8    |5    |2    |9    |
|---------|-----|-----|-----|-----|-----|------|-----|-----|-----|-----|
|Hero data|hero6|hero3|hero4|hero1|hero7|hero10|hero8|hero5|hero2|hero9|


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

|Level                      |6   |3   |4   |1   |7   |10  |8   |5   |2   |9   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|3601|2521|2880|1800|3961|5401|4320|3240|2161|4680|


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

|Level      |6     |3     |4     |1     |7     |10    |8     |5     |2     |9     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |110506|110503|110504|110501|110507|110510|110508|110505|110502|110509|
|Point value|40    |28    |32    |20    |44    |60    |48    |36    |24    |52    |


