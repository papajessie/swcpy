---
title: trptitlePhantomYWing (PhantomYWing)
category: unit
---

# trptitlePhantomYWing (PhantomYWing)

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

  * Training time: 10s
  * Training cost: 1$

### Upgrading stats

  * Upgrade time: 10s
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


## Main attack : Y-Wing Summon

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

#### Modifier "Sum Y wing"

  * Sum Y wing apply value as: absolute
  * Sum Y wing buff ID: buffSumYWing
  * Sum Y wing duration: permanent
  * Sum Y wing modifier: summon
  * Sum Y wing ms first proc: 0s
  * Sum Y wing ms per proc: permanent
  * Sum Y wing name: Sum Y wing
  * Sum Y wing stack: 1
  * Sum Y wing target: enemies
  * Sum Y wing value: 1

|Level                     |10                                  |8-9                                |6-7                                |4-5                                |1-3                                |
|--------------------------|------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
|Sum Y wing summon visitors|[Y-wing Bomber level 10](YWing.html)|[Y-wing Bomber level 9](YWing.html)|[Y-wing Bomber level 8](YWing.html)|[Y-wing Bomber level 7](YWing.html)|[Y-wing Bomber level 6](YWing.html)|


  * Sum Y wing summon die with summoner: No
  * Sum Y wing summon max proc: 29
  * Sum Y wing summon same team: No
  * Sum Y wing summon spawn points: 0,0,0
  * Sum Y wing summon target summoner: No
  * Sum Y wing summon visitor type: SpecialAttack

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffInvulnerable1
  * Unit ID: PhantomYWing

|Level                |10            |9            |8            |7            |6            |5            |4            |3            |2            |1            |
|---------------------|--------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|Apply buffs          |buffSumYWing10|buffSumYWing9|buffSumYWing8|buffSumYWing7|buffSumYWing6|buffSumYWing5|buffSumYWing4|buffSumYWing3|buffSumYWing2|buffSumYWing1|
|Sum Y wing details   |sumYWing10    |sumYWing9    |sumYWing8    |sumYWing7    |sumYWing6    |sumYWing5    |sumYWing4    |sumYWing3    |sumYWing2    |sumYWing1    |
|Sum Y wing summon uid|sumYWing10    |sumYWing9    |sumYWing8    |sumYWing7    |sumYWing6    |sumYWing5    |sumYWing4    |sumYWing3    |sumYWing2    |sumYWing1    |


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
  * Name: Y-Wing Summon
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
  * Sum Y wing cancel tags: summonYWing
  * Sum Y wing tags: summonYWing
  * Target in range modifier: 1
  * Xp: 0

|Level|10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|320310|320309|320308|320307|320306|320305|320304|320303|320302|320301|


