---
title: Modified SD-K4 (HeroRebelSpiderDroid)
category: unit
---

# Modified SD-K4 (HeroRebelSpiderDroid) — version 1096

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

|Level |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|29100|31000|32800|34700|36500|38400|40200|42100|43900|45800|


### Training stats

|Level        |1                                          |2                                     |3                                     |4                                     |5                                     |6                                     |7                                     |8                                     |9                                     |10                                     |
|-------------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|---------------------------------------|
|Training time|3m50s                                      |3m50s                                 |3m50s                                 |4m                                    |4m                                    |4m10s                                 |4m10s                                 |4m20s                                 |4m20s                                 |4m30s                                  |
|Training cost|1800$                                      |1970$                                 |2150$                                 |2330$                                 |2510$                                 |2680$                                 |2860$                                 |3040$                                 |3220$                                 |3400$                                  |
|Building     |[Hero Command 1](rebelTacticalCommand.html)|[Research Lab 2](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|


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

|Level          |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|---------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Damage per shot|10420|11085|11745|12410|13075|13740|14400|15065|15730|16395|


### Projectile

|Level                       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10   |
|----------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Displayed damage per second |5920 |6295 |6675 |7050 |7430 |7805 |8185 |8560 |8935 |9315 |
|Calculated damage per second|10420|11085|11745|12410|13075|13740|14400|15065|15730|16395|


  * Cannons per sequence: 1
  * Cliptime: 1s
  * Directional: Yes
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(400%)**: Flying infantry, Infantry, Infantry hero, Support troop, **(200%)**: Heavy infantry, Heavy infantry hero, **(150%)**: Flying vehicle, Light vehicle, Vehicule hero, **(125%)**: Heavy vehicle, Heavy vehicule hero, **(100%)**: Droideka, Turret, **(75%)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Trap, Wall
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

|Level                                     |1                                                                    |2                                                                    |3                                                                    |4                                                                    |5                                                                    |6                                                                    |7                                                                    |8                                                                    |9                                                                    |10                                                                    |
|------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------|
|Sum rebel spiderling droid summon visitors|["trp_title_RebelSpiderlingDroid" level 1](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 2](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 3](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 4](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 5](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 6](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 7](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 8](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 9](RebelSpiderlingDroid.html)|["trp_title_RebelSpiderlingDroid" level 10](RebelSpiderlingDroid.html)|


  * Sum rebel spiderling droid summon die with summoner: No
  * Sum rebel spiderling droid summon max proc: 20
  * Sum rebel spiderling droid summon same team: Yes
  * Sum rebel spiderling droid summon spawn points: -2,0,0 2,0,0 0,-2,0
  * Sum rebel spiderling droid summon target summoner: No
  * Sum rebel spiderling droid summon visitor type: Troop

|Level                                         |1                         |2                         |3                         |4                         |5                         |6                         |7                         |8                         |9                         |10                         |
|----------------------------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|---------------------------|
|Sum rebel spiderling droid summon visitor uids|troopRebelSpiderlingDroid1|troopRebelSpiderlingDroid2|troopRebelSpiderlingDroid3|troopRebelSpiderlingDroid4|troopRebelSpiderlingDroid5|troopRebelSpiderlingDroid6|troopRebelSpiderlingDroid7|troopRebelSpiderlingDroid8|troopRebelSpiderlingDroid9|troopRebelSpiderlingDroid10|


  * Secondary attack DPS: 0

  * Secondary attack cannons per sequence: 1
  * Secondary attack cliptime: 20.001s
  * Secondary attack directional: No
  * Secondary attack is deflectable: No
  * Secondary attack max speed: 18
  * Secondary attack mults: **(100%)**: Secondary attack droideka, Secondary attack flying infantry, Secondary attack flying vehicle, Secondary attack headquarters, Secondary attack heavy infantry, Secondary attack heavy infantry hero, Secondary attack heavy vehicle, Secondary attack heavy vehicule hero, Secondary attack infantry, Secondary attack infantry hero, Secondary attack light vehicle, Secondary attack other building, Secondary attack ressource generator, Secondary attack shield, Secondary attack shield generator, Secondary attack storage, Secondary attack support troop, Secondary attack trap, Secondary attack turret, Secondary attack vehicule hero, Secondary attack wall
  * Secondary attack salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Secondary attack projectile type: projectileEmpty
  * Unit ID: HeroRebelSpiderDroid
  * Upgrade shard uid: shrd_troopHeroRebelSpiderDroid

|Level                                |1                           |2                           |3                           |4                           |5                           |6                           |7                           |8                           |9                           |10                           |
|-------------------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|-----------------------------|
|Ability                              |abilityHeroRebelSpiderDroid1|abilityHeroRebelSpiderDroid2|abilityHeroRebelSpiderDroid3|abilityHeroRebelSpiderDroid4|abilityHeroRebelSpiderDroid5|abilityHeroRebelSpiderDroid6|abilityHeroRebelSpiderDroid7|abilityHeroRebelSpiderDroid8|abilityHeroRebelSpiderDroid9|abilityHeroRebelSpiderDroid10|
|Secondary attack self buff           |buffSumRebelSpiderlingDroid1|buffSumRebelSpiderlingDroid2|buffSumRebelSpiderlingDroid3|buffSumRebelSpiderlingDroid4|buffSumRebelSpiderlingDroid5|buffSumRebelSpiderlingDroid6|buffSumRebelSpiderlingDroid7|buffSumRebelSpiderlingDroid8|buffSumRebelSpiderlingDroid9|buffSumRebelSpiderlingDroid10|
|Sum rebel spiderling droid details   |sumRebelSpiderlingDroid1    |sumRebelSpiderlingDroid2    |sumRebelSpiderlingDroid3    |sumRebelSpiderlingDroid4    |sumRebelSpiderlingDroid5    |sumRebelSpiderlingDroid6    |sumRebelSpiderlingDroid7    |sumRebelSpiderlingDroid8    |sumRebelSpiderlingDroid9    |sumRebelSpiderlingDroid10    |
|Sum rebel spiderling droid summon uid|sumRebelSpiderlingDroid1    |sumRebelSpiderlingDroid2    |sumRebelSpiderlingDroid3    |sumRebelSpiderlingDroid4    |sumRebelSpiderlingDroid5    |sumRebelSpiderlingDroid6    |sumRebelSpiderlingDroid7    |sumRebelSpiderlingDroid8    |sumRebelSpiderlingDroid9    |sumRebelSpiderlingDroid10    |


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
  * Secondary attack arcs: No
  * Secondary attack max scale: 100
  * Secondary attack name: Rebel Spider Droid Summon
  * Secondary attack name: EmptyProjectile
  * Secondary attack spin speed: 0
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: No
  * Unlocked by event: true
  * Unlocked by tournament: No

|Level                      |1             |2          |3          |4          |5          |6          |7          |8          |9          |10         |
|---------------------------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|Displayed damage per second|5920          |6295       |6675       |7050       |7430       |7805       |8185       |8560       |8935       |9315       |
|Icon unlock position       |0,0,0         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock rotation       |0,0,0         |(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|
|Icon unlock scale          |0.75,0.75,0.75|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|(not found)|


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
  * Secondary attack seeks target: Yes
  * Secondary attack streams: no
  * Secondary attack strict cool down: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Sum rebel spiderling droid prevent tags: RebelSpiderlingDroid
  * Sum rebel spiderling droid tags: RebelSpiderlingDroid
  * Target in range modifier: 1
  * Xp: 0

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|225701|225702|225703|225704|225705|225706|225707|225708|225709|225710|


