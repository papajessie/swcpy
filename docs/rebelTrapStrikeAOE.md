---
title: Y-wing Trap (rebelTrapStrikeAOE)
category: building
---

# Y-wing Trap (rebelTrapStrikeAOE)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: trap
  * Side: Rebellion
  * Force reticle when targeted: Yes
  * Hide if locked: No
  * Trap disarm conditions: EventSuccess
  * Trap rearm credits cost: 0
  * Trap target type: Self
  * Trap trigger conditions: Radius(2) & ArmorNot(flierInfantry)
  * Type: trap

|Level                    |1                                              |2                                              |3                                              |4                                              |5                                              |6                                              |7                                              |8                                              |9                                              |10                                              |
|-------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|------------------------------------------------|
|Health                   |2500                                           |3750                                           |4500                                           |6000                                           |7250                                           |8500                                           |9750                                           |11000                                          |12250                                          |13500                                           |
|Max quantity             |2                                              |2                                              |2                                              |2                                              |2                                              |2                                              |3                                              |3                                              |4                                              |4                                               |
|Time                     |1m                                             |15m                                            |2h                                             |12h                                            |1d                                             |1d12h                                          |2d                                             |3d                                             |6d                                             |1w3d                                            |
|Trap air strike          |["shp_title_YWingTrap" level 1](YWingTrap.html)|["shp_title_YWingTrap" level 2](YWingTrap.html)|["shp_title_YWingTrap" level 3](YWingTrap.html)|["shp_title_YWingTrap" level 4](YWingTrap.html)|["shp_title_YWingTrap" level 5](YWingTrap.html)|["shp_title_YWingTrap" level 6](YWingTrap.html)|["shp_title_YWingTrap" level 7](YWingTrap.html)|["shp_title_YWingTrap" level 8](YWingTrap.html)|["shp_title_YWingTrap" level 9](YWingTrap.html)|["shp_title_YWingTrap" level 10](YWingTrap.html)|
|Trap rearm materials cost|500                                            |1000                                           |1500                                           |1800                                           |2000                                           |3000                                           |5000                                           |6000                                           |8000                                           |15000                                           |


### Training stats

|Level        |1                             |2                             |3                             |4                             |5                             |6                             |7                             |8                             |9                             |10                             |
|-------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|-------------------------------|
|Training cost|600 All.                      |2000 All.                     |10000 All.                    |30000 All.                    |60000 All.                    |160000 All.                   |350000 All.                   |500000 All.                   |800000 All.                   |1500000 All.                   |
|Building     |[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 6](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |1                      |2                      |3                      |4                      |5                      |6                      |7                      |8                      |9                      |10                      |
|---------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|
|Trap ID        |trap_RebelStrikeAOE1   |trap_RebelStrikeAOE2   |trap_RebelStrikeAOE3   |trap_RebelStrikeAOE4   |trap_RebelStrikeAOE5   |trap_RebelStrikeAOE6   |trap_RebelStrikeAOE7   |trap_RebelStrikeAOE8   |trap_RebelStrikeAOE9   |trap_RebelStrikeAOE10   |
|Trap event data|specialAttackYWingTrap1|specialAttackYWingTrap2|specialAttackYWingTrap3|specialAttackYWingTrap4|specialAttackYWingTrap5|specialAttackYWingTrap6|specialAttackYWingTrap7|specialAttackYWingTrap8|specialAttackYWingTrap9|specialAttackYWingTrap10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: fx_trap_starship_strike_rbl
  * Buff asset offset: -0.5, 1.2, -0.6
  * Bundle name: fx_trap_starship_strike_rbl
  * Destruct FX: fx_trap_bomber
  * Icon asset name: icon_starship_trap_ywing_rbl
  * Icon bundle name: icon_starship_trap_ywing_rbl
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 110
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:ywingholo_rbl-mod Contents/HomeAssets/holo_spent:ywingholo_rbl-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_rbl-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level    |1       |2-10       |
|---------|--------|-----------|
|Store tab|defenses|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 240

|Level|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|-----|--|--|--|--|--|--|--|--|--|--|
|Xp   |30|32|33|34|35|36|37|38|39|40|


