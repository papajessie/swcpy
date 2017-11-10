---
title: "trp_title_PhantomTieBomber" (PhantomTieBomber)
category: unit
---

# "trp_title_PhantomTieBomber" (PhantomTieBomber) — version 1098

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


## Main attack : TIE Bomber Summon

### Targeting

  * Attack shield border: No
  * Max attack range: 1
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 100
  * Target preferences: **Ressource generator (100)**, **Storage (100)**, **Turret (100)**, Shield (50), Shield generator (50), Headquarters (25), Other building (25), Droideka (0), Flying infantry (0), Flying vehicle (0), Heavy infantry (0), Heavy infantry hero (0), Heavy vehicle (0), Heavy vehicule hero (0), Infantry (0), Infantry hero (0), Light vehicle (0), Support troop (0), Trap (0), Vehicule hero (0), Wall (0)
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

  * Cannons per sequence: 1
  * Cliptime: 3.500s
  * Directional: No
  * Is deflectable: No
  * Max speed: 60
  * Damage multipliers: **(100)**: Headquarters, Other building, Ressource generator, Shield, Shield generator, Storage, Turret, **(0)**: Droideka, Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Trap, Vehicule hero, Wall
  * Pass through shield: Yes
  * Salvos: 1

#### Modifier "Sum tie bomber"

  * Sum tie bomber apply value as: absolute
  * Sum tie bomber buff ID: buffSumTieBomber
  * Sum tie bomber duration: permanent
  * Sum tie bomber modifier: summon
  * Sum tie bomber ms first proc: 0s
  * Sum tie bomber ms per proc: permanent
  * Sum tie bomber name: Sum tie bomber
  * Sum tie bomber stack: 1
  * Sum tie bomber target: enemies
  * Sum tie bomber value: 1

|Level                         |2                                   |9                                   |4                                   |6                                   |3, 1                                |7                                   |5                                   |8                                   |10                                   |
|------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|-------------------------------------|
|Sum tie bomber summon visitors|[TIE Bomber level 6](TieBomber.html)|[TIE Bomber level 9](TieBomber.html)|[TIE Bomber level 7](TieBomber.html)|[TIE Bomber level 8](TieBomber.html)|[TIE Bomber level 6](TieBomber.html)|[TIE Bomber level 8](TieBomber.html)|[TIE Bomber level 7](TieBomber.html)|[TIE Bomber level 9](TieBomber.html)|[TIE Bomber level 10](TieBomber.html)|


  * Sum tie bomber summon die with summoner: No
  * Sum tie bomber summon max proc: 29
  * Sum tie bomber summon same team: No
  * Sum tie bomber summon spawn points: 0,0,0
  * Sum tie bomber summon target summoner: No
  * Sum tie bomber summon visitor type: SpecialAttack

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffInvulnerable1
  * Unit ID: PhantomTieBomber

|Level                    |2                |9                |4                |6                |3                |1                |7                |5                |8                |10                |
|-------------------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|------------------|
|Apply buffs              |buffSumTieBomber2|buffSumTieBomber9|buffSumTieBomber4|buffSumTieBomber6|buffSumTieBomber3|buffSumTieBomber1|buffSumTieBomber7|buffSumTieBomber5|buffSumTieBomber8|buffSumTieBomber10|
|Sum tie bomber details   |sumTieBomber2    |sumTieBomber9    |sumTieBomber4    |sumTieBomber6    |sumTieBomber3    |sumTieBomber1    |sumTieBomber7    |sumTieBomber5    |sumTieBomber8    |sumTieBomber10    |
|Sum tie bomber summon uid|sumTieBomber2    |sumTieBomber9    |sumTieBomber4    |sumTieBomber6    |sumTieBomber3    |sumTieBomber1    |sumTieBomber7    |sumTieBomber5    |sumTieBomber8    |sumTieBomber10    |


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
  * Name: TIE Bomber Summon
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
  * Sum tie bomber cancel tags: summonTieBomber
  * Sum tie bomber tags: summonTieBomber
  * Target in range modifier: 1
  * Xp: 0

|Level|2     |9     |4     |6     |3     |1     |7     |5     |8     |10    |
|-----|------|------|------|------|------|------|------|------|------|------|
|Order|400201|400208|400203|400205|400202|400200|400206|400204|400207|400209|


