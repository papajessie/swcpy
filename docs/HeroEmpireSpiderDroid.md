---
title: SD-K4 (HeroEmpireSpiderDroid)
category: unit
---

# SD-K4 (HeroEmpireSpiderDroid) — version 1105

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: vehicle
  * Side: Empire
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

|Level        |1                                           |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|--------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training time|3m50s                                       |3m50s                                  |3m50s                                  |4m                                     |4m                                     |4m10s                                  |4m10s                                  |4m20s                                  |4m20s                                  |4m30s                                   |
|Training cost|1800$                                       |1970$                                  |2150$                                  |2330$                                  |2510$                                  |2680$                                  |2860$                                  |3040$                                  |3220$                                  |3400$                                   |
|Building     |[Hero Command 1](empireTacticalCommand.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|


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
|Calculated damage per clip  |10420|11085|11745|12410|13075|13740|14400|15065|15730|16395|


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

#### Modifier "Sum empire spiderling droid"

  * Sum empire spiderling droid apply value as: absolute
  * Sum empire spiderling droid buff ID: buffSumEmpireSpiderlingDroid
  * Sum empire spiderling droid duration: 60ms
  * Sum empire spiderling droid modifier: summon
  * Sum empire spiderling droid ms first proc: 0s
  * Sum empire spiderling droid ms per proc: 20ms
  * Sum empire spiderling droid name: Sum empire spiderling droid
  * Sum empire spiderling droid stack: 1
  * Sum empire spiderling droid target: self
  * Sum empire spiderling droid value: 1

|Level                                      |1                                                                      |2                                                                      |3                                                                      |4                                                                      |5                                                                      |6                                                                      |7                                                                      |8                                                                      |9                                                                      |10                                                                      |
|-------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------|
|Sum empire spiderling droid summon visitors|["trp_title_EmpireSpiderlingDroid" level 1](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 2](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 3](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 4](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 5](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 6](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 7](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 8](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 9](EmpireSpiderlingDroid.html)|["trp_title_EmpireSpiderlingDroid" level 10](EmpireSpiderlingDroid.html)|


  * Sum empire spiderling droid summon die with summoner: No
  * Sum empire spiderling droid summon max proc: 20
  * Sum empire spiderling droid summon same team: Yes
  * Sum empire spiderling droid summon spawn points: -2,0,0 2,0,0 0,-2,0
  * Sum empire spiderling droid summon target summoner: No
  * Sum empire spiderling droid summon visitor type: Troop

  * Secondary attack shot calculated damage per second: 0
  * Secondary attack shot calculated damage per clip: 0

  * Secondary attack shot cannons per sequence: 1
  * Secondary attack shot cliptime: 20.001s
  * Secondary attack shot directional: No
  * Secondary attack shot is deflectable: No
  * Secondary attack shot max speed: 18
  * Secondary attack shot damage multipliers: **(100)**: Secondary attack shot droideka, Secondary attack shot flying infantry, Secondary attack shot flying vehicle, Secondary attack shot headquarters, Secondary attack shot heavy infantry, Secondary attack shot heavy infantry hero, Secondary attack shot heavy vehicle, Secondary attack shot heavy vehicule hero, Secondary attack shot infantry, Secondary attack shot infantry hero, Secondary attack shot light vehicle, Secondary attack shot other building, Secondary attack shot ressource generator, Secondary attack shot shield, Secondary attack shot shield generator, Secondary attack shot storage, Secondary attack shot support troop, Secondary attack shot trap, Secondary attack shot turret, Secondary attack shot vehicule hero, Secondary attack shot wall
  * Secondary attack shot salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Secondary attack projectile type: projectileEmpty
  * Unit ID: HeroEmpireSpiderDroid
  * Upgrade shard uid: shrd_troopHeroEmpireSpiderDroid

|Level                                 |1                            |2                            |3                            |4                            |5                            |6                            |7                            |8                            |9                            |10                            |
|--------------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|------------------------------|
|Ability                               |abilityHeroEmpireSpiderDroid1|abilityHeroEmpireSpiderDroid2|abilityHeroEmpireSpiderDroid3|abilityHeroEmpireSpiderDroid4|abilityHeroEmpireSpiderDroid5|abilityHeroEmpireSpiderDroid6|abilityHeroEmpireSpiderDroid7|abilityHeroEmpireSpiderDroid8|abilityHeroEmpireSpiderDroid9|abilityHeroEmpireSpiderDroid10|
|Secondary attack self buff            |buffSumEmpireSpiderlingDroid1|buffSumEmpireSpiderlingDroid2|buffSumEmpireSpiderlingDroid3|buffSumEmpireSpiderlingDroid4|buffSumEmpireSpiderlingDroid5|buffSumEmpireSpiderlingDroid6|buffSumEmpireSpiderlingDroid7|buffSumEmpireSpiderlingDroid8|buffSumEmpireSpiderlingDroid9|buffSumEmpireSpiderlingDroid10|
|Sum empire spiderling droid details   |sumEmpireSpiderlingDroid1    |sumEmpireSpiderlingDroid2    |sumEmpireSpiderlingDroid3    |sumEmpireSpiderlingDroid4    |sumEmpireSpiderlingDroid5    |sumEmpireSpiderlingDroid6    |sumEmpireSpiderlingDroid7    |sumEmpireSpiderlingDroid8    |sumEmpireSpiderlingDroid9    |sumEmpireSpiderlingDroid10    |
|Sum empire spiderling droid summon uid|sumEmpireSpiderlingDroid1    |sumEmpireSpiderlingDroid2    |sumEmpireSpiderlingDroid3    |sumEmpireSpiderlingDroid4    |sumEmpireSpiderlingDroid5    |sumEmpireSpiderlingDroid6    |sumEmpireSpiderlingDroid7    |sumEmpireSpiderlingDroid8    |sumEmpireSpiderlingDroid9    |sumEmpireSpiderlingDroid10    |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 600
  * Arcs: No
  * Asset name: spiderdroid_emp-ani
  * Audio attack: "sfx_attack_spiderdroid_01":30,"sfx_attack_spiderdroid_02":35,"sfx_attack_spiderdroid_03":35
  * Audio death: "sfx_death_spiderdroid_01":30,"sfx_death_spiderdroid_02":35,"sfx_death_spiderdroid_03":35
  * Audio placement: "sfx_placement_spiderdroid_01":30,"sfx_placement_spiderdroid_02":35,"sfx_placement_spiderdroid_03":35
  * Audio train: "sfx_ui_unitcomplete_spiderdroid_01":50,"sfx_ui_unitcomplete_spiderdroid_02":50
  * Buff asset offset: 0.00,2,0.00
  * Bundle name: spiderdroid_emp-ani
  * Decal asset name: tac_hero_emp
  * Decal bundle name: tac_hero_emp
  * Decal size: 320
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "atst_emp_rig_MASTER_MOVER/atst_emp_rig_locator_gun":1
  * Hologram uid: HeroHologramEmpireSpiderDroid
  * Icon camera position: 17.11,25.64,42.53
  * Icon closeup camera position: 17.25,18.81,41.94
  * Icon closeup lookat position: -0.56,2.23,-1.28
  * Icon lookat position: -0.38,1.62,-0.86
  * Max scale: 100
  * Name: EmprieSpiderDroid
  * Secondary attack animation delay: 0
  * Secondary attack name: Empire Spider Droid Summon
  * Secondary attack shot arcs: No
  * Secondary attack shot max scale: 100
  * Secondary attack shot name: EmptyProjectile
  * Secondary attack shot spin speed: 0
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
  * Secondary attack shot seeks target: Yes
  * Secondary attack shot streams: no
  * Secondary attack strict cool down: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Sum empire spiderling droid prevent tags: EmpireSpiderlingDroid
  * Sum empire spiderling droid tags: EmpireSpiderlingDroid
  * Target in range modifier: 1
  * Xp: 0

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|111301|111302|111303|111304|111305|111306|111307|111308|111309|111310|


