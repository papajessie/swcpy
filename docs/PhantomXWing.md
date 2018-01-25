---
title: trptitlePhantomXWing (PhantomXWing)
category: unit
---

# trptitlePhantomXWing (PhantomXWing) — version 1119

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: phantom
  * Side: Rebellion
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


## Main attack : TIE Fighter Summon

### Targeting

  * Attack shield border: No
  * Max attack range: 1
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 100
  * Target preferences: **Ressource generator (100)**, **Storage (100)**, **Turret (100)**, Shield (50), Shield generator (50), Headquarters (25), Other building (25), Droideka (1), Flying infantry (1), Flying vehicle (1), Heavy infantry (1), Heavy infantry hero (1), Heavy vehicle (1), Heavy vehicule hero (1), Infantry (1), Infantry hero (1), Light vehicle (1), Support troop (1), Vehicule hero (1), Trap (0), Wall (0)
  * View range: 4

### Shooting

  * Time between start of clip and first shot: 3s
  * Clip retargeting: Yes
  * Damage per shot: 0
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * New target on reload: Yes
  * Can shoot over walls: Yes
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 1s
  * Target locking: No

### Projectile

  * Displayed damage per second: 1
  * Calculated damage per second: 0
  * Calculated damage per clip: 0

  * Cannons per sequence: 1
  * Cliptime: 3.500s
  * Directional: No
  * Is deflectable: No
  * Max speed: 60
  * Damage multipliers: **(100)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Trap, Vehicule hero, Wall
  * Pass through shield: Yes
  * Salvos: 1

#### Modifier "Sum X wing"

  * Sum X wing apply value as: absolute
  * Sum X wing buff ID: buffSumXWing
  * Sum X wing duration: permanent
  * Sum X wing modifier: summon
  * Sum X wing ms first proc: 0s
  * Sum X wing ms per proc: permanent
  * Sum X wing name: Sum X wing
  * Sum X wing stack: 1
  * Sum X wing target: enemies
  * Sum X wing value: 1

|Level                     |1-3                                     |4-5                                     |6-7                                     |8-9                                     |10                                       |
|--------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|-----------------------------------------|
|Sum X wing summon visitors|[X-wing Starfighter level 6](XWing.html)|[X-wing Starfighter level 7](XWing.html)|[X-wing Starfighter level 8](XWing.html)|[X-wing Starfighter level 9](XWing.html)|[X-wing Starfighter level 10](XWing.html)|


  * Sum X wing summon die with summoner: No
  * Sum X wing summon max proc: 29
  * Sum X wing summon same team: No
  * Sum X wing summon spawn points: 0,0,0
  * Sum X wing summon target summoner: No
  * Sum X wing summon visitor type: SpecialAttack

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffInvulnerable1
  * Unit ID: PhantomXWing

|Level                |1            |2            |3            |4            |5            |6            |7            |8            |9            |10            |
|---------------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|--------------|
|Apply buffs          |buffSumXWing1|buffSumXWing2|buffSumXWing3|buffSumXWing4|buffSumXWing5|buffSumXWing6|buffSumXWing7|buffSumXWing8|buffSumXWing9|buffSumXWing10|
|Sum X wing details   |sumXWing1    |sumXWing2    |sumXWing3    |sumXWing4    |sumXWing5    |sumXWing6    |sumXWing7    |sumXWing8    |sumXWing9    |sumXWing10    |
|Sum X wing summon uid|sumXWing1    |sumXWing2    |sumXWing3    |sumXWing4    |sumXWing5    |sumXWing6    |sumXWing7    |sumXWing8    |sumXWing9    |sumXWing10    |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
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
  * Name: TIE Fighter Summon
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
  * Sum X wing cancel tags: summonXWing
  * Sum X wing tags: summonXWing
  * Target in range modifier: 1
  * Xp: 0

|Level|1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|400400|400401|400402|400403|400404|400405|400406|400407|400408|400409|


