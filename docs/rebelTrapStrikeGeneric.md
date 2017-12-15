---
title: X-wing Trap (rebelTrapStrikeGeneric)
category: building
---

# X-wing Trap (rebelTrapStrikeGeneric) — version 1106

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
|Max quantity             |1                                              |1                                              |1                                              |2                                              |2                                              |4                                              |4                                              |6                                              |6                                              |6                                               |
|Time                     |1m                                             |15m                                            |2h                                             |12h                                            |1d                                             |1d12h                                          |2d                                             |3d                                             |6d                                             |1w3d                                            |
|Trap air strike          |["shp_title_XWingTrap" level 1](XWingTrap.html)|["shp_title_XWingTrap" level 2](XWingTrap.html)|["shp_title_XWingTrap" level 3](XWingTrap.html)|["shp_title_XWingTrap" level 4](XWingTrap.html)|["shp_title_XWingTrap" level 5](XWingTrap.html)|["shp_title_XWingTrap" level 6](XWingTrap.html)|["shp_title_XWingTrap" level 7](XWingTrap.html)|["shp_title_XWingTrap" level 8](XWingTrap.html)|["shp_title_XWingTrap" level 9](XWingTrap.html)|["shp_title_XWingTrap" level 10](XWingTrap.html)|
|Trap rearm materials cost|300                                            |600                                            |900                                            |1200                                           |1800                                           |2000                                           |2700                                           |3000                                           |3500                                           |6000                                            |


### Training stats

|Level        |1                             |2                             |3                             |4                             |5                             |6                             |7                             |8                             |9                             |10                             |
|-------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|-------------------------------|
|Training cost|300 All.                      |1000 All.                     |5000 All.                     |15000 All.                    |30000 All.                    |70000 All.                    |150000 All.                   |300000 All.                   |900000 All.                   |1500000 All.                   |
|Building     |[Headquarters 3](rebelHQ.html)|[Headquarters 3](rebelHQ.html)|[Headquarters 3](rebelHQ.html)|[Headquarters 4](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 6](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |1                       |2                       |3                       |4                       |5                       |6                       |7                       |8                       |9                       |10                       |
|---------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|-------------------------|
|Trap ID        |trap_RebelStrikeGeneric1|trap_RebelStrikeGeneric2|trap_RebelStrikeGeneric3|trap_RebelStrikeGeneric4|trap_RebelStrikeGeneric5|trap_RebelStrikeGeneric6|trap_RebelStrikeGeneric7|trap_RebelStrikeGeneric8|trap_RebelStrikeGeneric9|trap_RebelStrikeGeneric10|
|Trap event data|specialAttackXWingTrap1 |specialAttackXWingTrap2 |specialAttackXWingTrap3 |specialAttackXWingTrap4 |specialAttackXWingTrap5 |specialAttackXWingTrap6 |specialAttackXWingTrap7 |specialAttackXWingTrap8 |specialAttackXWingTrap9 |specialAttackXWingTrap10 |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: fx_trap_starship_strike_rbl
  * Buff asset offset: -0.5, 1.2, -0.6
  * Bundle name: fx_trap_starship_strike_rbl
  * Destruct FX: fx_trap_fighter
  * Icon asset name: icon_starship_trap_xwing_rbl
  * Icon bundle name: icon_starship_trap_xwing_rbl
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 100
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:xwingholo_rbl-mod Contents/HomeAssets/holo_spent:xwingholo_rbl-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_rbl-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level    |1       |2-10       |
|---------|--------|-----------|
|Store tab|defenses|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 238

|Level|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|-----|--|--|--|--|--|--|--|--|--|--|
|Xp   |30|32|33|34|35|36|37|38|39|40|


