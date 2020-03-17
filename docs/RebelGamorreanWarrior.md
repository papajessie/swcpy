---
title: Gamorrean Warrior (RebelGamorreanWarrior)
category: unit
---

# Gamorrean Warrior (RebelGamorreanWarrior)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserInfantry
  * Side: Rebellion
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 6
  * Type: mercenary

|Level |10   |9    |8    |7    |6    |5    |4    |3    |2    |1    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|50000|48080|46800|45520|43600|42960|42320|41680|41040|40400|


### Training stats

  * Training time: 10s
  * Training cost: 1 Con.

|Level   |10                                     |9                                     |8                                     |7                                     |6                                     |5                                     |4                                     |3                                     |2                                     |1                                       |
|--------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|----------------------------------------|
|Building|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 5](rebelOffenseLab.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Cantina 1](rebelContrabandCantina.html)|


### Upgrading stats

|Level               |2-10  |1      |
|--------------------|------|-------|
|Upgrade time        |10s   |0s     |
|Upgrade requirements|1 Con.|Nothing|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

### Modifiers

#### Modifier "Defend splash"

  * Defend splash apply value as: relativePercent
  * Defend splash buff ID: buffDefendSplash
  * Defend splash duration: permanent
  * Defend splash modifier: splashDefense
  * Defend splash ms first proc: 0s
  * Defend splash ms per proc: permanent
  * Defend splash name: Defend splash
  * Defend splash stack: 1
  * Defend splash target: self
  * Defend splash value: -50.0%


#### Modifier "Reduce heals"

  * Reduce heals apply value as: absolutePercent
  * Reduce heals buff ID: buffReduceHeals
  * Reduce heals duration: permanent
  * Reduce heals modifier: healDefense
  * Reduce heals ms first proc: 0s
  * Reduce heals ms per proc: permanent
  * Reduce heals name: Reduce heals
  * Reduce heals stack: 0
  * Reduce heals target: self
  * Reduce heals value: 25


## Main attack : Melee Vibro Ax

### Targeting

  * Attack shield border: No
  * Max attack range: 2
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Turret (70)**, Droideka (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield generator (50), Storage (50), Support troop (50), Flying infantry (1), Flying vehicle (1), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Shield (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Animation delay: 600ms
  * Charge time: 400ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Reload time: 500ms
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 1
  * Shot delay: 0s
  * Target locking: No

|Level          |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|2200|2104|2040|1976|1880|1848|1816|1784|1752|1720|


### Projectile

|Level                       |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second |2370|2304|2240|2176|2080|2048|2016|1984|1952|1920|
|Calculated damage per second|1466|1402|1360|1317|1253|1232|1210|1189|1168|1146|
|Calculated damage per cycle |2200|2104|2040|1976|1880|1848|1816|1784|1752|1720|


  * Cannons per sequence: 1
  * Shooting cycle duration: 1.500s
  * Directional: No
  * Is deflectable: No
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Headquarters, Other building, Shield, Shield generator, Support troop, Turret, Wall, **(75)**: Infantry, Infantry hero, Light vehicle, Vehicule hero, **(50)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Ressource generator, Storage, **(0)**: Flying infantry, Flying vehicle, Trap
  * Pass through shield: No
  * Salvos: 1

## Death attack : Death Ax

  * Death projectile delay: 3.600s
  * Death projectile distance: 17

  * Death attack splash damage percentages: 100,100,100,100

|Level                                    |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|-----------------------------------------|----|----|----|----|----|----|----|----|----|----|
|Death projectile damage                  |4000|3750|3500|3250|3000|2750|2500|2250|2000|1750|
|Death attack calculated damage per second|1111|1041|972 |902 |833 |763 |694 |625 |555 |486 |
|Death attack calculated damage per clip  |4000|3750|3500|3250|3000|2750|2500|2250|2000|1750|


  * Death attack cannons per sequence: 1
  * Death attack cliptime: 3.600s
  * Death attack directional: Yes
  * Death attack is deflectable: No
  * Death attack max speed: 4
  * Death attack damage multipliers: **(300)**: Death attack wall, **(200)**: Death attack other building, Death attack turret, **(100)**: Death attack droideka, Death attack headquarters, Death attack heavy infantry, Death attack heavy infantry hero, Death attack heavy vehicle, Death attack heavy vehicule hero, Death attack infantry, Death attack infantry hero, Death attack light vehicle, Death attack ressource generator, Death attack shield, Death attack shield generator, Death attack storage, Death attack support troop, Death attack trap, Death attack vehicule hero, **(0)**: Death attack flying infantry, Death attack flying vehicle
  * Death attack pass through shield: Yes
  * Death attack salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Death projectile: projectileDeathVibroAx
  * Spawn apply buffs: buffDefendSplash1,buffReduceHeals1
  * Unit ID: RebelGamorreanWarrior

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: Yes
  * Asset name: gamorreanguard_con-ani
  * Audio attack: "sfx_attack_gamorreanwarrior_01":25,"sfx_attack_gamorreanwarrior_02":25,"sfx_attack_gamorreanwarrior_03":25,"sfx_attack_gamorreanwarrior_04":25,
  * Audio death: "sfx_death_gamorreanwarrior_01":35,"sfx_death_gamorreanwarrior_02":35,"sfx_death_gamorreanwarrior_03":30
  * Audio impact: "sfx_impact_gamoreanwarrior_01":25,"sfx_impact_gamoreanwarrior_02":25,"sfx_impact_gamoreanwarrior_03":25,"sfx_impact_gamoreanwarrior_04":25
  * Audio placement: "sfx_placement_gamorreanwarrior_01":35,"sfx_placement_gamorreanwarrior_01":35,"sfx_placement_gamorreanwarrior_01":30
  * Audio train: "sfx_ui_unitcomplete_gamorreanwarrior_01":35,"sfx_ui_unitcomplete_gamorreanwarrior_02":35,"sfx_ui_unitcomplete_gamorreanwarrior_03":30
  * Buff asset offset: 0.00,0.43,0.0
  * Bundle name: gamorreanguard_con-ani
  * Death attack arcs: No
  * Death attack hit spark: fx_gamGuard_deathblow
  * Death attack max scale: 100
  * Death attack name: Death Ax
  * Death attack spin speed: 0
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Icon camera position: 9.14,6.79,20.25
  * Icon closeup camera position: 1.9,1.83,14.68
  * Icon closeup lookat position: 0.18,2.49,0.11
  * Icon lookat position: 0.43,1.85,0.73
  * Max scale: 100
  * Muzzle flash: fx_gamGuard_melee
  * Name: Melee Vibro Ax
  * Spin speed: 2
  * Targeted type: ENEMIES

|Level                      |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|2370|2304|2240|2176|2080|2048|2016|1984|1952|1920|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Death attack seeks target: No
  * Death attack streams: no
  * Defend splash is refreshing: No
  * Max scale: No
  * Reduce heals is refreshing: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |240110|240109|240108|240107|240106|240105|240104|240103|240102|240101|
|Point value|12    |10.400|9.600 |8.800 |8     |7.200 |6.400 |5.600 |4.800 |4     |


