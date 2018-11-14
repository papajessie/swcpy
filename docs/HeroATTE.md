---
title: Elite AT-TE Walker (HeroATTE)
category: unit
---

# Elite AT-TE Walker (HeroATTE)

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

|Level |11   |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|75840|72000|65600|60800|57600|54400|51200|48000|44800|41600|38400|


### Training stats

|Level        |11                                     |10                                     |9                                     |8                                     |7                                     |6                                     |5                                     |4                                     |3                                     |2                                     |1                                          |
|-------------|---------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|-------------------------------------------|
|Training time|5m10s                                  |5m                                     |4m50s                                 |4m40s                                 |4m30s                                 |4m20s                                 |4m10s                                 |4m                                    |3m50s                                 |3m40s                                 |3m30s                                      |
|Training cost|5000$                                  |4600$                                  |4200$                                 |3800$                                 |3400$                                 |3000$                                 |2600$                                 |2200$                                 |1800$                                 |1400$                                 |1000$                                      |
|Building     |[Research Lab 11](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Hero Command 5](rebelTacticalCommand.html)|


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

  * Animation delay: 0s
  * Charge time: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 500ms
  * Can shoot over walls: Yes
  * Reload time: 1s
  * Retargeting offset: 20
  * Self-centered targeting: No
  * Shot count: 3
  * Shot delay: 400ms
  * Target locking: No

|Level          |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|7876|7292|6318|5832|5348|4861|4374|3888|3404|2917|2430|


### Projectile

|Level                       |11   |10   |9    |8    |7    |6    |5    |4    |3    |2   |1   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|----|
|Displayed damage per second |5688 |5401 |4680 |4320 |3961 |3601 |3240 |2880 |2521 |2161|1800|
|Calculated damage per second|10273|9511 |8240 |7606 |6975 |6340 |5705 |5071 |4440 |3804|3169|
|Calculated damage per cycle |23628|21876|18954|17496|16044|14583|13122|11664|10212|8751|7290|


  * Cannons per sequence: 1
  * Shooting cycle duration: 2.300s
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

|Level    |10-11 |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|---------|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Hero data|hero10|hero9|hero8|hero7|hero6|hero5|hero4|hero3|hero2|hero1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

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

|Level                      |11                           |10         |9          |8          |7          |6          |5          |4          |3          |2          |1          |
|---------------------------|-----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |vfx_prestige_deploy_large_reb|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|5688                         |5401       |4680       |4320       |3961       |3601       |3240       |2880       |2521       |2161       |1800       |
|Icon unlock rotation       |(not found)                  |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|0,-20,0    |
|Icon unlock scale          |(not found)                  |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|0.5,0.5,0.5|
|Prestige                   |true                         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


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

|Level      |11    |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|------|
|Order      |200711|200710|200709|200708|200707|200706|200705|200704|200703|200702|200701|
|Point value|60    |60    |52    |48    |44    |40    |36    |32    |28    |24    |20    |


