---
title: X-wing Trap (rebelTrapStrikeGeneric)
category: building
---

# X-wing Trap (rebelTrapStrikeGeneric)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: trap
  * Side: Rebellion
  * Force reticle when targeted: Yes
  * Hide if locked: No
  * Time: 10s
  * Trap disarm conditions: EventSuccess
  * Trap rearm credits cost: 0
  * Trap target type: Self
  * Trap trigger conditions: Radius(2) & ArmorNot(flierInfantry)
  * Type: trap

|Level                    |11                                              |10                                              |9                                              |8                                              |7                                              |6                                              |5                                              |4                                              |3                                              |2                                              |1                                              |
|-------------------------|------------------------------------------------|------------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
|Cross credits            |0                                               |(not found)                                     |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |
|Cross materials          |0                                               |(not found)                                     |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |
|Cross time               |0s                                              |(not found)                                     |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |
|Health                   |14250                                           |13500                                           |12250                                          |11000                                          |9750                                           |8500                                           |7250                                           |6000                                           |4500                                           |3750                                           |2500                                           |
|Max quantity             |6                                               |6                                               |6                                              |6                                              |4                                              |4                                              |2                                              |2                                              |1                                              |1                                              |1                                              |
|Produce                  |0                                               |(not found)                                     |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |
|Trap air strike          |["shp_title_XWingTrap" level 10](XWingTrap.html)|["shp_title_XWingTrap" level 10](XWingTrap.html)|["shp_title_XWingTrap" level 9](XWingTrap.html)|["shp_title_XWingTrap" level 8](XWingTrap.html)|["shp_title_XWingTrap" level 7](XWingTrap.html)|["shp_title_XWingTrap" level 6](XWingTrap.html)|["shp_title_XWingTrap" level 5](XWingTrap.html)|["shp_title_XWingTrap" level 4](XWingTrap.html)|["shp_title_XWingTrap" level 3](XWingTrap.html)|["shp_title_XWingTrap" level 2](XWingTrap.html)|["shp_title_XWingTrap" level 1](XWingTrap.html)|
|Trap rearm materials cost|8500                                            |6000                                            |3500                                           |3000                                           |2700                                           |2000                                           |1800                                           |1200                                           |900                                            |600                                            |300                                            |


### Training stats

|Level        |11                             |10                             |9                             |8                             |7                             |6                             |5                             |4                             |1-3                           |
|-------------|-------------------------------|-------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
|Training cost|1 All.                         |1$                             |1$                            |1$                            |1$                            |1$                            |1$                            |1$                            |1$                            |
|Building     |[Headquarters 11](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 6](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 4](rebelHQ.html)|[Headquarters 3](rebelHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |11                       |10                       |9                       |8                       |7                       |6                       |5                       |4                       |3                       |2                       |1                       |
|---------------|-------------------------|-------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|Trap ID        |trap_RebelStrikeGeneric11|trap_RebelStrikeGeneric10|trap_RebelStrikeGeneric9|trap_RebelStrikeGeneric8|trap_RebelStrikeGeneric7|trap_RebelStrikeGeneric6|trap_RebelStrikeGeneric5|trap_RebelStrikeGeneric4|trap_RebelStrikeGeneric3|trap_RebelStrikeGeneric2|trap_RebelStrikeGeneric1|
|Trap event data|specialAttackXWingTrap10 |specialAttackXWingTrap10 |specialAttackXWingTrap9 |specialAttackXWingTrap8 |specialAttackXWingTrap7 |specialAttackXWingTrap6 |specialAttackXWingTrap5 |specialAttackXWingTrap4 |specialAttackXWingTrap3 |specialAttackXWingTrap2 |specialAttackXWingTrap1 |


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Buff asset offset: -0.5, 1.2, -0.6
  * Destruct FX: fx_trap_fighter
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 100
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:xwingholo_rbl-mod Contents/HomeAssets/holo_spent:xwingholo_rbl-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_rbl-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level           |11                               |2-10                        |1                           |
|----------------|---------------------------------|----------------------------|----------------------------|
|Asset name      |fx_trap_starship_strike_rbl-up11 |fx_trap_starship_strike_rbl |fx_trap_starship_strike_rbl |
|Bundle name     |fx_trap_starship_strike_rbl-up11 |fx_trap_starship_strike_rbl |fx_trap_starship_strike_rbl |
|Cycle time      |0s                               |(not found)                 |(not found)                 |
|Icon asset name |icon_starship_trap_xwing_rbl-up11|icon_starship_trap_xwing_rbl|icon_starship_trap_xwing_rbl|
|Icon bundle name|icon_starship_trap_xwing_rbl-up11|icon_starship_trap_xwing_rbl|icon_starship_trap_xwing_rbl|
|Prestige        |true                             |(not found)                 |(not found)                 |
|Store tab       |(not found)                      |(not found)                 |defenses                    |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 14

|Level|11|10|9 |8 |7 |6 |5 |4 |3 |2 |1 |
|-----|--|--|--|--|--|--|--|--|--|--|--|
|Xp   |41|40|39|38|37|36|35|34|33|32|30|


