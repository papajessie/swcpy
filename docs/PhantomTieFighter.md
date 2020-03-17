---
title: trptitlePhantomTieFighter (PhantomTieFighter)
category: unit
---

# trptitlePhantomTieFighter (PhantomTieFighter)

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

#### Modifier "Sum tie fighter"

  * Sum tie fighter apply value as: absolute
  * Sum tie fighter buff ID: buffSumTieFighter
  * Sum tie fighter duration: permanent
  * Sum tie fighter modifier: summon
  * Sum tie fighter ms first proc: 0s
  * Sum tie fighter ms per proc: permanent
  * Sum tie fighter name: Sum tie fighter
  * Sum tie fighter stack: 1
  * Sum tie fighter target: enemies
  * Sum tie fighter value: 1

|Level                          |11                                                                  |10                                                                  |8-9                                                                |6-7                                                                |4-5                                                                |1-3                                                                |
|-------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
|Sum tie fighter summon visitors|["shp_title_TieFighterEqpSummon" level 11](TieFighterEqpSummon.html)|["shp_title_TieFighterEqpSummon" level 10](TieFighterEqpSummon.html)|["shp_title_TieFighterEqpSummon" level 9](TieFighterEqpSummon.html)|["shp_title_TieFighterEqpSummon" level 8](TieFighterEqpSummon.html)|["shp_title_TieFighterEqpSummon" level 7](TieFighterEqpSummon.html)|["shp_title_TieFighterEqpSummon" level 6](TieFighterEqpSummon.html)|


  * Sum tie fighter summon die with summoner: No
  * Sum tie fighter summon max proc: 29
  * Sum tie fighter summon same team: No
  * Sum tie fighter summon spawn points: 0,0,0
  * Sum tie fighter summon target summoner: No
  * Sum tie fighter summon visitor type: SpecialAttack

## Internal stats

These stats internal to the system link different parts of data together.

  * Spawn apply buffs: buffInvulnerable1
  * Unit ID: PhantomTieFighter

|Level                     |11                 |10                 |9                 |8                 |7                 |6                 |5                 |4                 |3                 |2                 |1                 |
|--------------------------|-------------------|-------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|
|Apply buffs               |buffSumTieFighter11|buffSumTieFighter10|buffSumTieFighter9|buffSumTieFighter8|buffSumTieFighter7|buffSumTieFighter6|buffSumTieFighter5|buffSumTieFighter4|buffSumTieFighter3|buffSumTieFighter2|buffSumTieFighter1|
|Sum tie fighter details   |sumTieFighter11    |sumTieFighter10    |sumTieFighter9    |sumTieFighter8    |sumTieFighter7    |sumTieFighter6    |sumTieFighter5    |sumTieFighter4    |sumTieFighter3    |sumTieFighter2    |sumTieFighter1    |
|Sum tie fighter summon uid|sumTieFighter11    |sumTieFighter10    |sumTieFighter9    |sumTieFighter8    |sumTieFighter7    |sumTieFighter6    |sumTieFighter5    |sumTieFighter4    |sumTieFighter3    |sumTieFighter2    |sumTieFighter1    |


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
  * Name: TIE Fighter Summon
  * Spin speed: 0
  * Targeted type: ENEMIES
  * Unlocked by campaign: No
  * Unlocked by event: false
  * Unlocked by tournament: No

|Level     |11                           |1-10       |
|----------|-----------------------------|-----------|
|Deploy vfx|vfx_prestige_deploy_small_emp|(not found)|


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
  * Sum tie fighter cancel tags: summonTie
  * Sum tie fighter tags: summonTie
  * Target in range modifier: 1
  * Xp: 0

|Level|11    |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----|------|------|------|------|------|------|------|------|------|------|------|
|Order|120411|120410|120409|120408|120407|120406|120405|120404|120403|120402|120401|


