---
title: Luke Skywalker (HeroLukeSkywalker)
category: unit
---

# Luke Skywalker (HeroLukeSkywalker)

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
  * Unit capacity: 1
  * Type: hero

|Level |11   |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|58320|54000|46800|43200|39600|36000|32400|28800|25200|21600|18000|


### Training stats

  * Training time: 10s

|Level        |11                                     |10                                     |9                                     |8                                     |7                                     |6                                     |5                                     |4                                     |3                                     |2                                     |1                                          |
|-------------|---------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|-------------------------------------------|
|Training cost|7500$                                  |6900$                                  |6300$                                 |5700$                                 |5100$                                 |4500$                                 |3900$                                 |3300$                                 |2700$                                 |2100$                                 |1500$                                      |
|Building     |[Research Lab 11](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Hero Command 8](rebelTacticalCommand.html)|


### Upgrading stats

  * Upgrade time: 10s

|Level               |2-11|1      |
|--------------------|----|-------|
|Upgrade requirements|1$  |Nothing|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 30
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : HERO Luke Attack

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Support troop (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 0s
  * Charge time: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 250ms
  * Can shoot over walls: No
  * Reload time: 500ms
  * Retargeting offset: 14
  * Self-centered targeting: No
  * Shot count: 2
  * Shot delay: 500ms
  * Target locking: No

|Level          |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|4860|4500|3900|3600|3300|3000|2700|2400|2100|1800|1500|


### Projectile

  * Splash damage percentages: 0

|Level                       |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |7780|7200|6240|5760|5280|4800|4320|3840|3360|2880|2400|
|Calculated damage per second|7776|7200|6240|5760|5280|4800|4320|3840|3360|2880|2400|
|Calculated damage per cycle |9720|9000|7800|7200|6600|6000|5400|4800|4200|3600|3000|


  * Cannons per sequence: 1
  * Shooting cycle duration: 1.250s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 25
  * Damage multipliers: **(200)**: Shield, **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy vehicle, Infantry, Infantry hero, Light vehicle, Shield generator, Support troop, Trap, Turret, Vehicule hero, **(85)**: Ressource generator, Storage, **(75)**: Other building, Wall, **(60)**: Heavy infantry, Heavy infantry hero, Heavy vehicule hero
  * Pass through shield: No
  * Salvos: 2

## Secondary attack : HERO Luke Defend

  * Secondary attack auto: No
  * Secondary attack cooldown on spawn: No
  * Secondary attack cooldown Time: 15s
  * Secondary attack description: Lightsaber Defend
  * Secondary attack duration: 10s
  * Secondary attack recast ability: No
  * Secondary attack target self: Yes

### Targeting

  * Secondary attack max attack range: 7
  * Secondary attack min attack range: 0
  * Secondary attack new rotation speed: 7854
  * Secondary attack target preference strength: 90
  * Secondary attack target preferences: **Secondary attack turret (80)**, _Secondary attack shield (60)_, _Secondary attack shield generator (60)_, Secondary attack droideka (50), Secondary attack flying infantry (50), Secondary attack flying vehicle (50), Secondary attack headquarters (50), Secondary attack heavy infantry (50), Secondary attack heavy infantry hero (50), Secondary attack heavy vehicle (50), Secondary attack heavy vehicule hero (50), Secondary attack infantry (50), Secondary attack infantry hero (50), Secondary attack light vehicle (50), Secondary attack other building (50), Secondary attack ressource generator (50), Secondary attack storage (50), Secondary attack support troop (50), Secondary attack vehicule hero (50), Secondary attack wall (1), Secondary attack trap (0)
  * Secondary attack view range: 8

### Shooting

  * Secondary attack animation delay: 0s
  * Secondary attack charge time: 100ms
  * Secondary attack clip retargeting: No
  * Secondary attack damage per shot: 1200
  * Secondary attack gun shooting sequence: 1
  * Secondary attack impact delay: 0s
  * Secondary attack can shoot over walls: No
  * Secondary attack reload time: 0s
  * Secondary attack retargeting offset: 12
  * Secondary attack self-centered targeting: Yes
  * Secondary attack shot count: 5
  * Secondary attack shot delay: 1.900s
  * Secondary attack target locking: No

#### Modifier "Deflect"

  * Deflect apply value as: absolutePercent
  * Deflect buff ID: buffDeflect
  * Deflect duration: permanent
  * Deflect modifier: defense
  * Deflect ms first proc: 0s
  * Deflect ms per proc: permanent
  * Deflect name: Deflect
  * Deflect stack: 1
  * Deflect target: self
  * Deflect value: 0


  * Secondary attack shot calculated damage per second: 625
  * Secondary attack shot calculated damage per clip: 6000
  * Secondary attack shot splash damage percentages: 100,100,100

  * Secondary attack shot cannons per sequence: 1
  * Secondary attack shot cliptime: 9.600s
  * Secondary attack shot directional: Yes
  * Secondary attack shot is deflectable: No
  * Secondary attack shot max speed: 18
  * Secondary attack shot damage multipliers: **(100)**: Secondary attack shot droideka, Secondary attack shot flying infantry, Secondary attack shot flying vehicle, Secondary attack shot headquarters, Secondary attack shot heavy infantry hero, Secondary attack shot heavy vehicle, Secondary attack shot heavy vehicule hero, Secondary attack shot infantry, Secondary attack shot infantry hero, Secondary attack shot light vehicle, Secondary attack shot shield, Secondary attack shot shield generator, Secondary attack shot support troop, Secondary attack shot trap, Secondary attack shot turret, Secondary attack shot vehicule hero, **(95)**: Secondary attack shot ressource generator, Secondary attack shot storage, **(75)**: Secondary attack shot other building, Secondary attack shot wall, **(60)**: Secondary attack shot heavy infantry
  * Secondary attack shot pass through shield: No
  * Secondary attack shot salvos: 5

## Internal stats

These stats internal to the system link different parts of data together.

  * Ability: abilityHeroLukeDefend
  * Secondary attack projectile type: projectileHeroLukeDefend
  * Secondary attack self buff: buffDeflect
  * Unit ID: HeroLukeSkywalker

|Level    |10-11 |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|---------|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Hero data|hero10|hero9|hero8|hero7|hero6|hero5|hero4|hero3|hero2|hero1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: lukeskywalker_rbl-ani
  * Audio attack: "sfx_attack_blasterpistol_1":25,"sfx_attack_blasterpistol_2":25,"sfx_attack_blasterpistol_3":25,"sfx_attack_blasterpistol_4":25
  * Audio death: "sfx_death_hero_luke":100
  * Audio placement: "sfx_placement_hero_luke":100
  * Bullet: fx_blaster_beam_b_sm
  * Bundle name: lukeskywalker_rbl-ani
  * Decal asset name: tac_hero_rbl
  * Decal bundle name: tac_hero_rbl
  * Decal size: 160
  * Deflect audio ability event: "sfx_lightsaber_deflect_1":25,"sfx_lightsaber_deflect_2":25,"sfx_lightsaber_deflect_3":25,"sfx_lightsaber_deflect_4":25
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "lukeskywalker_rbl_rig_MASTER_MOVER/lukeskywalker_rbl_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_b_sm
  * Hologram uid: HeroHologramLukeSkywalker
  * Icon camera position: 9.95,9.78,16.61
  * Icon closeup camera position: 0.34,1.87,9.02
  * Icon closeup lookat position: 0.02,2.48,-0.32
  * Icon lookat position: -0.45,1.28,-0.62
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_b_sm
  * Name: HERO Luke Attack
  * Secondary attack audio ability activate: "sfx_lightsaber_luke_activate_1":100
  * Secondary attack audio ability attack: "sfx_lightsaber_luke_swing_1":30,"sfx_lightsaber_luke_swing_2":35,"sfx_lightsaber_luke_swing_3":35
  * Secondary attack audio ability loop: "sfx_lightsaber_luke_whirlwind":100
  * Secondary attack displayed damage per second: 1000
  * Secondary attack name: Lightsaber Defend Luke
  * Secondary attack persistent effect: fx_aura_rbl
  * Secondary attack persistent scaling: 0
  * Secondary attack shot arcs: No
  * Secondary attack shot max scale: 200
  * Secondary attack shot name: HERO Luke Defend
  * Secondary attack shot spin speed: 0
  * Secondary attack weapon trail FX params: 0.17,0.10
  * Spawn effect uid: effectRebelSpawn
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |11                           |10         |9          |8          |7          |6          |5          |4          |3          |2          |1          |
|---------------------------|-----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Deploy vfx                 |vfx_prestige_deploy_small_reb|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Displayed damage per second|7780                         |7200       |6240       |5760       |5280       |4800       |4320       |3840       |3360       |2880       |2400       |
|Effect type                |1                            |1          |1          |1          |1          |1          |1          |1          |1          |2          |2          |
|Prestige                   |true                         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 0
  * Deflect cancel tags: damage
  * Deflect is refreshing: No
  * Deflect prevent tags: damage
  * Max scale: No
  * Secondary attack arming delay: 0
  * Secondary attack clip count: 1
  * Secondary attack kill cooldown reset: Yes
  * Secondary attack max speed: 3
  * Secondary attack shot seeks target: No
  * Secondary attack shot streams: no
  * Secondary attack strict cool down: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |11    |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|------|
|Order      |200511|200510|200509|200508|200507|200506|200505|200504|200503|200502|200501|
|Point value|60    |60    |52    |48    |44    |40    |36    |32    |28    |24    |20    |


