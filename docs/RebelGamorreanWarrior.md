---
title: Gamorrean Warrior (RebelGamorreanWarrior)
category: unit
---

# Gamorrean Warrior (RebelGamorreanWarrior) — version 1098

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

|Level |5    |7    |9    |2    |1    |4    |10   |3    |6    |8    |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|42960|45520|48080|41040|40400|42320|50000|41680|43600|46800|


### Training stats

|Level        |5                                     |7                                     |9                                     |2                                     |1                                       |4                                     |10                                     |3                                     |6                                     |8                                     |
|-------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|----------------------------------------|--------------------------------------|---------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
|Training time|7m41s                                 |8m39s                                 |9m37s                                 |6m14s                                 |5m45s                                   |7m12s                                 |10m                                    |6m43s                                 |8m10s                                 |9m8s                                  |
|Training cost|95 Con.                               |190 Con.                              |360 Con.                              |25 Con.                               |15 Con.                                 |85 Con.                               |720 Con.                               |50 Con.                               |145 Con.                              |265 Con.                              |
|Building     |[Research Lab 5](rebelOffenseLab.html)|[Research Lab 7](rebelOffenseLab.html)|[Research Lab 9](rebelOffenseLab.html)|[Research Lab 2](rebelOffenseLab.html)|[Cantina 1](rebelContrabandCantina.html)|[Research Lab 4](rebelOffenseLab.html)|[Research Lab 10](rebelOffenseLab.html)|[Research Lab 3](rebelOffenseLab.html)|[Research Lab 6](rebelOffenseLab.html)|[Research Lab 8](rebelOffenseLab.html)|


### Upgrading stats

|Level               |5         |7         |9          |2        |1      |4         |10         |3         |6         |8          |
|--------------------|----------|----------|-----------|---------|-------|----------|-----------|----------|----------|-----------|
|Upgrade time        |1w        |1w2d      |1w4d       |4d       |0s     |6d        |1w5d       |5d        |1w1d      |1w3d       |
|Upgrade requirements|50000 Con.|85000 Con.|140000 Con.|6000 Con.|Nothing|25000 Con.|190000 Con.|13000 Con.|75000 Con.|135000 Con.|


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
  * Defend splash value: -50%


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
  * Target preferences: **Turret (70)**, Droideka (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Ressource generator (50), Shield generator (50), Storage (50), Support troop (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Shield (1), Vehicule hero (1), Wall (1), Flying infantry (0), Flying vehicle (0), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 400ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 0s
  * Target locking: No

|Level          |5   |7   |9   |2   |1   |4   |10  |3   |6   |8   |
|---------------|----|----|----|----|----|----|----|----|----|----|
|Damage per shot|1848|1976|2104|1752|1720|1816|2200|1784|1880|2040|


### Projectile

|Level                       |5       |7       |9       |2       |1       |4       |10      |3       |6       |8       |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
|Displayed damage per second |2048    |2176    |2304    |1952    |1920    |2016    |2400    |1984    |2080    |2240    |
|Calculated damage per second|2053.333|2195.556|2337.778|1946.667|1911.111|2017.778|2444.444|1982.222|2088.889|2266.667|


  * Cannons per sequence: 1
  * Cliptime: 900ms
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

|Level                  |5      |7      |9       |2      |1      |4      |10      |3   |6      |8      |
|-----------------------|-------|-------|--------|-------|-------|-------|--------|----|-------|-------|
|Death projectile damage|2750   |3250   |3750    |2000   |1750   |2500   |4000    |2250|3000   |3500   |
|Death attack DPS       |763.889|902.778|1041.667|555.556|486.111|694.444|1111.111|625 |833.333|972.222|


  * Death attack cannons per sequence: 1
  * Death attack cliptime: 3.600s
  * Death attack directional: Yes
  * Death attack is deflectable: No
  * Death attack max speed: 4
  * Death attack mults: **(300)**: Death attack wall, **(200)**: Death attack other building, Death attack turret, **(100)**: Death attack droideka, Death attack headquarters, Death attack heavy infantry, Death attack heavy infantry hero, Death attack heavy vehicle, Death attack heavy vehicule hero, Death attack infantry, Death attack infantry hero, Death attack light vehicle, Death attack ressource generator, Death attack shield, Death attack shield generator, Death attack storage, Death attack support troop, Death attack trap, Death attack vehicule hero, **(0)**: Death attack flying infantry, Death attack flying vehicle
  * Death attack pass through shield: Yes
  * Death attack salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Death projectile: projectileDeathVibroAx
  * Spawn apply buffs: buffDefendSplash1,buffReduceHeals1
  * Unit ID: RebelGamorreanWarrior

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 600
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

|Level                      |5   |7   |9   |2   |1   |4   |10  |3   |6   |8   |
|---------------------------|----|----|----|----|----|----|----|----|----|----|
|Displayed damage per second|2048|2176|2304|1952|1920|2016|2400|1984|2080|2240|


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

|Level      |5     |7     |9     |2     |1     |4     |10    |3     |6     |8     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |215105|215107|215109|215102|215101|215104|215110|215103|215106|215108|
|Point value|7.200 |8.800 |10.400|4.800 |4     |6.400 |12    |5.600 |8     |9.600 |


