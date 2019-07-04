---
title: trptitlePhantomNavalStrike (PhantomNavalStrike)
category: unit
---

# trptitlePhantomNavalStrike (PhantomNavalStrike)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: phantom
  * Side: Empire
  * Health: 1
  * Buildable unit: No
  * Can be given: Yes
  * Role: Generic
  * Unit capacity: 1
  * Type: phantom

### Training stats

  * Training time: 1s
  * Training cost: 1$

### Upgrading stats

  * Upgrade time: 1s
  * Upgrade requirements: 1$

### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Ignores walls: Yes
  * Flying unit: Yes
  * Max speed: 60
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * Support follow distance: 5

### Modifiers

#### Modifier "Invulnerable"

  * Invulnerable apply value as: absolutePercent
  * Invulnerable buff ID: buffInvulnerable
  * Invulnerable duration: permanent
  * Invulnerable modifier: defense
  * Invulnerable ms first proc: 0s
  * Invulnerable ms per proc: permanent
  * Invulnerable name: Invulnerable
  * Invulnerable stack: 1
  * Invulnerable target: self
  * Invulnerable value: 0


## Main attack : Phantom Naval Strike

### Targeting

  * Attack shield border: No
  * Max attack range: 1
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 100
  * Target preferences: **Ressource generator (100)**, **Storage (100)**, **Turret (100)**, Shield (50), Shield generator (50), Headquarters (25), Other building (25), Droideka (1), Flying infantry (1), Flying vehicle (1), Heavy infantry (1), Heavy infantry hero (1), Heavy vehicle (1), Heavy vehicule hero (1), Infantry (1), Infantry hero (1), Light vehicle (1), Support troop (1), Vehicule hero (1), Trap (0), Wall (0)
  * View range: 4

### Shooting

  * Animation delay: 0s
  * Charge time: 3s
  * Clip retargeting: Yes
  * Damage per shot: 0
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * New target on reload: Yes
  * Can shoot over walls: Yes
  * Reload time: 500ms
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 1
  * Shot delay: 1s
  * Target locking: No

### Projectile

  * Displayed damage per second: 1
  * Calculated damage per second: 0
  * Calculated damage per cycle: 0

  * Cannons per sequence: 1
  * Shooting cycle duration: 4s
  * Directional: No
  * Is deflectable: No
  * Max speed: 60
  * Damage multipliers: **(100)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Trap, Vehicule hero, Wall
  * Pass through shield: Yes
  * Salvos: 1

#### Modifier "Sum naval strike"

  * Sum naval strike apply value as: absolute
  * Sum naval strike buff ID: buffSumNavalStrike
  * Sum naval strike duration: permanent
  * Sum naval strike modifier: summon
  * Sum naval strike ms first proc: 0s
  * Sum naval strike ms per proc: permanent
  * Sum naval strike name: Sum naval strike
  * Sum naval strike stack: 1
  * Sum naval strike target: enemies
  * Sum naval strike value: 1

|Level                           |10                                                  |9                                                  |8                                                  |7                                                  |6                                                  |5                                                  |4                                                  |3                                                  |2                                                  |1                                                  |
|--------------------------------|----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
|Sum naval strike summon visitors|["shp_title_NavalStrike" level 10](NavalStrike.html)|["shp_title_NavalStrike" level 9](NavalStrike.html)|["shp_title_NavalStrike" level 8](NavalStrike.html)|["shp_title_NavalStrike" level 7](NavalStrike.html)|["shp_title_NavalStrike" level 6](NavalStrike.html)|["shp_title_NavalStrike" level 5](NavalStrike.html)|["shp_title_NavalStrike" level 4](NavalStrike.html)|["shp_title_NavalStrike" level 3](NavalStrike.html)|["shp_title_NavalStrike" level 2](NavalStrike.html)|["shp_title_NavalStrike" level 1](NavalStrike.html)|


  * Sum naval strike summon die with summoner: No
  * Sum naval strike summon max proc: 29
  * Sum naval strike summon same team: No
  * Sum naval strike summon spawn points: 0,0,0
  * Sum naval strike summon target summoner: No
  * Sum naval strike summon visitor type: SpecialAttack

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffInvulnerable1
  * Unit ID: PhantomNavalStrike

|Level                      |10                  |9                  |8                  |7                  |6                  |5                  |4                  |3                  |2                  |1                  |
|---------------------------|--------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|Apply buffs                |buffSumNavalStrike10|buffSumNavalStrike9|buffSumNavalStrike8|buffSumNavalStrike7|buffSumNavalStrike6|buffSumNavalStrike5|buffSumNavalStrike4|buffSumNavalStrike3|buffSumNavalStrike2|buffSumNavalStrike1|
|Sum naval strike details   |sumNavalStrike10    |sumNavalStrike9    |sumNavalStrike8    |sumNavalStrike7    |sumNavalStrike6    |sumNavalStrike5    |sumNavalStrike4    |sumNavalStrike3    |sumNavalStrike2    |sumNavalStrike1    |
|Sum naval strike summon uid|sumNavalStrike10    |sumNavalStrike9    |sumNavalStrike8    |sumNavalStrike7    |sumNavalStrike6    |sumNavalStrike5    |sumNavalStrike4    |sumNavalStrike3    |sumNavalStrike2    |sumNavalStrike1    |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Arcs: No
  * Asset name: phantom_neu-ani
  * Bundle name: phantom_neu-ani
  * Displayed damage per second: 1
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Icon camera position: 0,0,0
  * Icon lookat position: 0,0,0
  * Max scale: 1
  * Name: Phantom Naval Strike
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: No
  * Unlocked by event: false
  * Unlocked by tournament: No

## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Invulnerable cancel tags: damage
  * Invulnerable is refreshing: No
  * Invulnerable tags: invulnerable
  * Max scale: No
  * Point value: 0
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level|10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|120210|120209|120208|120207|120206|120205|120204|120203|120202|120201|


