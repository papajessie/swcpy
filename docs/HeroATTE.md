---
title: Elite AT-TE Walker (HeroATTE)
category: unit
---

# Elite AT-TE Walker (HeroATTE) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: hero

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|38400|41600|44800|48000|51200|54400|57600|60800|65600|72000|


### Training stats

|Level   |1                                          |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|--------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Building|[Hero Command 5](rebelTacticalCommand.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 5s
  * Upgrade requirements: 32 data fragments

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

## Main attack : HeroATTE

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
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: Yes
  * Time between end of clip and start of clip: 1s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 3
  * Time between shots: 400ms
  * Target locking: No

|Level          |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2430|2917|3404|3888|4374|4861|5348|5832|6318|7292|


### Projectile

|Level                       |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |1800|2161|2521|2880|3240|3601|3961|4320|4680|5401|
|Calculated damage per second|3169|3804|4440|5071|5705|6340|6975|7606|8240|9511|


  * Cannons per sequence: 1
  * Cliptime: 2.300s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Shield, Shield generator, **(100)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(75)**: Headquarters, Other building, Ressource generator, Storage, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: HeroATTE
  * Upgrade shard uid: shrd_troopHeroATTE

|Level    |1    |2    |3    |4    |5    |6    |7    |8    |9    |10    |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
|Hero data|hero1|hero2|hero3|hero4|hero5|hero6|hero7|hero8|hero9|hero10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: attehero_rbl-ani
  * Audio attack: "sfx_attack_empire_atat_1":50,"sfx_attack_empire_atat_2":25,"sfx_attack_empire_atat_3":25
  * Audio death: "sfx_death_hero_walker_1":100
  * Audio placement: "sfx_placement_empire_atat_1":100
  * Buff asset offset: 0.00,1.46,0.00
  * Bullet: fx_blaster_beam_b_med
  * Bundle name: attehero_rbl-ani
  * Decal asset name: tac_hero_rbl
  * Decal bundle name: tac_hero_rbl
  * Decal size: 320
  * Effect type: 2
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: shieldGenerator
  * Gun position: atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun:1
  * Hit spark: fx_blaster_hit_b_med
  * Hologram uid: HeroHologramATTE
  * Icon camera position: 36.44,26.49,49.08
  * Icon lookat position: 0.12,2.66,-0.82
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_med
  * Name: HeroATTE
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by event: true

|Level                      |1          |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|1800       |2161       |2521       |2880       |3240       |3601       |3961       |4320       |4680       |5401       |
|Icon unlock rotation       |0,-20,0    |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |0.5,0.5,0.5|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


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

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |211201|211202|211203|211204|211205|211206|211207|211208|211209|211210|
|Point value|20    |24    |28    |32    |36    |40    |44    |48    |52    |60    |


