---
title: Modified SD-K4 (HeroRebelSpiderDroid)
category: unit
---

# Modified SD-K4 (HeroRebelSpiderDroid) — version 1098

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Destroyer
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 1
  * Type: hero

|Level |6    |4    |1    |5    |9    |8    |10   |2    |7    |3    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|38400|34700|29100|36500|43900|42100|45800|31000|40200|32800|


### Training stats

|Level        |6                                     |4                                     |1                                          |5                                     |9                                     |8                                     |10                                     |2                                     |7                                     |3                                     |
|-------------|--------------------------------------|--------------------------------------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|4m10s                                 |4m                                    |3m50s                                      |4m                                    |4m20s                                 |4m20s                                 |4m30s                                  |3m50s                                 |4m10s                                 |3m50s                                 |
|Training cost|2680$                                 |2330$                                 |1800$                                      |2510$                                 |3220$                                 |3040$                                 |3400$                                  |1970$                                 |2860$                                 |2150$                                 |
|Building     |[Research Lab 6](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Hero Command 1](rebelTacticalCommand.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 5s
  * Upgrade requirements: 32 data fragments

### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 40
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : EmprieSpiderDroid

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, _Droideka (60)_, _Flying infantry (60)_, _Flying vehicle (60)_, _Heavy infantry (60)_, _Heavy vehicle (60)_, _Infantry (60)_, _Light vehicle (60)_, _Support troop (60)_, Headquarters (50), Other building (50), Ressource generator (50), Shield (50), Shield generator (50), Storage (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 4
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 960ms
  * Target locking: No

|Level          |6    |4    |1    |5    |9    |8    |10   |2    |7    |3    |
|---------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot|13740|12410|10420|13075|15730|15065|16395|11085|14400|11745|


### Projectile

|Level                       |6    |4    |1    |5    |9    |8    |10   |2    |7    |3    |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |7805 |7050 |5920 |7430 |8935 |8560 |9315 |6295 |8185 |6675 |
|Calculated damage per second|13740|12410|10420|13075|15730|15065|16395|11085|14400|11745|


  * Cannons per sequence: 1
  * Cliptime: 1s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(400)**: Flying infantry, Infantry, Infantry hero, Support troop, **(200)**: Heavy infantry, Heavy infantry hero, **(150)**: Flying vehicle, Light vehicle, Vehicule hero, **(125)**: Heavy vehicle, Heavy vehicule hero, **(100)**: Droideka, Turret, **(75)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Wall
  * Pass through shield: No
  * Salvos: 1

## Secondary attack : EmptyProjectile

  * Secondary attack auto: No
  * Secondary attack cooldown on spawn: No
  * Secondary attack supplementary time between last shot and reload: 20s
  * Secondary attack description: Summon Spiderling
  * Secondary attack duration: 0s
  * Secondary attack recast ability: No
  * Secondary attack target self: Yes

### Targeting

  * Secondary attack max attack range: 2
  * Secondary attack min attack range: 0
  * Secondary attack new rotation speed: 7854
  * Secondary attack target preference strength: 90
  * Secondary attack target preferences: **Secondary attack turret (80)**, _Secondary attack shield (60)_, _Secondary attack shield generator (60)_, Secondary attack droideka (50), Secondary attack flying infantry (50), Secondary attack flying vehicle (50), Secondary attack headquarters (50), Secondary attack heavy infantry (50), Secondary attack heavy infantry hero (50), Secondary attack heavy vehicle (50), Secondary attack heavy vehicule hero (50), Secondary attack infantry (50), Secondary attack infantry hero (50), Secondary attack light vehicle (50), Secondary attack other building (50), Secondary attack ressource generator (50), Secondary attack storage (50), Secondary attack support troop (50), Secondary attack vehicule hero (50), Secondary attack wall (1), Secondary attack trap (0)
  * Secondary attack view range: 8

### Shooting

  * Secondary attack time between start of clip and first shot: 0s
  * Secondary attack clip retargeting: No
  * Secondary attack damage per shot: 0
  * Secondary attack gun shooting sequence: 1
  * Secondary attack impact delay: 0s
  * Secondary attack time between end of clip and start of clip: 1ms
  * Secondary attack retargeting offset: 12
  * Secondary attack self-centered targeting: Yes
  * Secondary attack shot count: 1
  * Secondary attack time between shots: 0s
  * Secondary attack target locking: No

#### Modifier "Sum rebel spiderling droid"

  * Sum rebel spiderling droid apply value as: absolute
  * Sum rebel spiderling droid buff ID: buffSumRebelSpiderlingDroid
  * Sum rebel spiderling droid duration: 60ms
  * Sum rebel spiderling droid modifier: summon
  * Sum rebel spiderling droid ms first proc: 0s
  * Sum rebel spiderling droid ms per proc: 20ms
  * Sum rebel spiderling droid name: Sum rebel spiderling droid
  * Sum rebel spiderling droid stack: 1
  * Sum rebel spiderling droid target: self
  * Sum rebel spiderling droid value: 1

|Level                                     |6                                                                    |4                                                                    |1                                                                    |5                                                                    |9                                                                    |8                                                                    |10                                                                    |2                                                                    |7                                                                    |3                                                                    |
|------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
|Sum rebel spiderling droid summon visitors|["trp_title_RebelSpiderlingDroid" level 6](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 4](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 1](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 5](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 9](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 8](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 10](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 2](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 7](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 3](RebelSpiderlingDroid.html)|


  * Sum rebel spiderling droid summon die with summoner: No
  * Sum rebel spiderling droid summon max proc: 20
  * Sum rebel spiderling droid summon same team: Yes
  * Sum rebel spiderling droid summon spawn points: -2,0,0 2,0,0 0,-2,0
  * Sum rebel spiderling droid summon target summoner: No
  * Sum rebel spiderling droid summon visitor type: Troop

  * Secondary attack shot DPS: 0

  * Secondary attack shot cannons per sequence: 1
  * Secondary attack shot cliptime: 20.001s
  * Secondary attack shot directional: No
  * Secondary attack shot is deflectable: No
  * Secondary attack shot max speed: 18
  * Secondary attack shot mults: **(100)**: Secondary attack shot droideka, Secondary attack shot flying infantry, Secondary attack shot flying vehicle, Secondary attack shot headquarters, Secondary attack shot heavy infantry, Secondary attack shot heavy infantry hero, Secondary attack shot heavy vehicle, Secondary attack shot heavy vehicule hero, Secondary attack shot infantry, Secondary attack shot infantry hero, Secondary attack shot light vehicle, Secondary attack shot other building, Secondary attack shot ressource generator, Secondary attack shot shield, Secondary attack shot shield generator, Secondary attack shot storage, Secondary attack shot support troop, Secondary attack shot trap, Secondary attack shot turret, Secondary attack shot vehicule hero, Secondary attack shot wall
  * Secondary attack shot salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Secondary attack projectile type: projectileEmpty
  * Unit ID: HeroRebelSpiderDroid
  * Upgrade shard uid: shrd_troopHeroRebelSpiderDroid

|Level                                |6                           |4                           |1                           |5                           |9                           |8                           |10                           |2                           |7                           |3                           |
|-------------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|-----------------------------|----------------------------|----------------------------|----------------------------|
|Ability                              |abilityHeroRebelSpiderDroid6|abilityHeroRebelSpiderDroid4|abilityHeroRebelSpiderDroid1|abilityHeroRebelSpiderDroid5|abilityHeroRebelSpiderDroid9|abilityHeroRebelSpiderDroid8|abilityHeroRebelSpiderDroid10|abilityHeroRebelSpiderDroid2|abilityHeroRebelSpiderDroid7|abilityHeroRebelSpiderDroid3|
|Secondary attack self buff           |buffSumRebelSpiderlingDroid6|buffSumRebelSpiderlingDroid4|buffSumRebelSpiderlingDroid1|buffSumRebelSpiderlingDroid5|buffSumRebelSpiderlingDroid9|buffSumRebelSpiderlingDroid8|buffSumRebelSpiderlingDroid10|buffSumRebelSpiderlingDroid2|buffSumRebelSpiderlingDroid7|buffSumRebelSpiderlingDroid3|
|Sum rebel spiderling droid details   |sumRebelSpiderlingDroid6    |sumRebelSpiderlingDroid4    |sumRebelSpiderlingDroid1    |sumRebelSpiderlingDroid5    |sumRebelSpiderlingDroid9    |sumRebelSpiderlingDroid8    |sumRebelSpiderlingDroid10    |sumRebelSpiderlingDroid2    |sumRebelSpiderlingDroid7    |sumRebelSpiderlingDroid3    |
|Sum rebel spiderling droid summon uid|sumRebelSpiderlingDroid6    |sumRebelSpiderlingDroid4    |sumRebelSpiderlingDroid1    |sumRebelSpiderlingDroid5    |sumRebelSpiderlingDroid9    |sumRebelSpiderlingDroid8    |sumRebelSpiderlingDroid10    |sumRebelSpiderlingDroid2    |sumRebelSpiderlingDroid7    |sumRebelSpiderlingDroid3    |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 600
  * Arcs: No
  * Asset name: spiderdroid_rbl-ani
  * Audio attack: "sfx_attack_spiderdroid_01":30,"sfx_attack_spiderdroid_02":35,"sfx_attack_spiderdroid_03":35
  * Audio death: "sfx_death_spiderdroid_01":30,"sfx_death_spiderdroid_02":35,"sfx_death_spiderdroid_03":35
  * Audio placement: "sfx_placement_spiderdroid_01":30,"sfx_placement_spiderdroid_02":35,"sfx_placement_spiderdroid_03":35
  * Audio train: "sfx_ui_unitcomplete_spiderdroid_01":50,"sfx_ui_unitcomplete_spiderdroid_02":50
  * Buff asset offset: 0.00,2,0.00
  * Bundle name: spiderdroid_rbl-ani
  * Decal asset name: tac_hero_rbl
  * Decal bundle name: tac_hero_rbl
  * Decal size: 320
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hologram uid: HeroHologramRebelSpiderDroid
  * Icon camera position: 15.59,27.41,39.64
  * Icon closeup camera position: 16.84,20.12,42.27
  * Icon closeup lookat position: -0.6,2.15,-1.37
  * Icon lookat position: -0.17,1.03,-0.59
  * Max scale: 100
  * Name: EmprieSpiderDroid
  * Secondary attack animation delay: 0
  * Secondary attack name: Rebel Spider Droid Summon
  * Secondary attack shot arcs: No
  * Secondary attack shot max scale: 100
  * Secondary attack shot name: EmptyProjectile
  * Secondary attack shot spin speed: 0
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: No
  * Unlocked by event: true
  * Unlocked by tournament: No

|Level                      |6          |4          |1             |5          |9          |8          |10         |2          |7          |3          |
|---------------------------|-----------|-----------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|7805       |7050       |5920          |7430       |8935       |8560       |9315       |6295       |8185       |6675       |
|Icon unlock position       |(not found)|(not found)|0,0,0         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation       |(not found)|(not found)|0,0,0         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |(not found)|(not found)|0.75,0.75,0.75|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Point value: 1
  * Secondary attack arming delay: 0
  * Secondary attack clip count: 1
  * Secondary attack kill cooldown reset: No
  * Secondary attack max speed: 3
  * Secondary attack shot seeks target: Yes
  * Secondary attack shot streams: no
  * Secondary attack strict cool down: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Sum rebel spiderling droid prevent tags: RebelSpiderlingDroid
  * Sum rebel spiderling droid tags: RebelSpiderlingDroid
  * Target in range modifier: 1
  * Xp: 0

|Level|6     |4     |1     |5     |9     |8     |10    |2     |7     |3     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|225706|225704|225701|225705|225709|225708|225710|225702|225707|225703|


