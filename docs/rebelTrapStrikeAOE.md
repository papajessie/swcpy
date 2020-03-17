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
|Max quantity             |4                                               |4                                               |4                                              |3                                              |3                                              |2                                              |2                                              |2                                              |2                                              |2                                              |2                                              |
|Produce                  |0                                               |(not found)                                     |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |(not found)                                    |
|Trap air strike          |["shp_title_YWingTrap" level 10](YWingTrap.html)|["shp_title_YWingTrap" level 10](YWingTrap.html)|["shp_title_YWingTrap" level 9](YWingTrap.html)|["shp_title_YWingTrap" level 8](YWingTrap.html)|["shp_title_YWingTrap" level 7](YWingTrap.html)|["shp_title_YWingTrap" level 6](YWingTrap.html)|["shp_title_YWingTrap" level 5](YWingTrap.html)|["shp_title_YWingTrap" level 4](YWingTrap.html)|["shp_title_YWingTrap" level 3](YWingTrap.html)|["shp_title_YWingTrap" level 2](YWingTrap.html)|["shp_title_YWingTrap" level 1](YWingTrap.html)|
|Trap rearm materials cost|22000                                           |15000                                           |8000                                           |6000                                           |5000                                           |3000                                           |2000                                           |1800                                           |1500                                           |1000                                           |500                                            |


### Training stats

|Level        |11                             |10                             |9                             |8                             |7                             |6                             |1-5                           |
|-------------|-------------------------------|-------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
|Training cost|1 All.                         |1$                             |1$                            |1$                            |1$                            |1$                            |1$                            |
|Building     |[Headquarters 11](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 6](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |11                      |10                      |9                      |8                      |7                      |6                      |5                      |4                      |3                      |2                      |1                      |
|---------------|------------------------|------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|Trap ID        |trap_RebelStrikeAOE11   |trap_RebelStrikeAOE10   |trap_RebelStrikeAOE9   |trap_RebelStrikeAOE8   |trap_RebelStrikeAOE7   |trap_RebelStrikeAOE6   |trap_RebelStrikeAOE5   |trap_RebelStrikeAOE4   |trap_RebelStrikeAOE3   |trap_RebelStrikeAOE2   |trap_RebelStrikeAOE1   |
|Trap event data|specialAttackYWingTrap10|specialAttackYWingTrap10|specialAttackYWingTrap9|specialAttackYWingTrap8|specialAttackYWingTrap7|specialAttackYWingTrap6|specialAttackYWingTrap5|specialAttackYWingTrap4|specialAttackYWingTrap3|specialAttackYWingTrap2|specialAttackYWingTrap1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Buff asset offset: -0.5, 1.2, -0.6
  * Destruct FX: fx_trap_bomber
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 110
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:ywingholo_rbl-mod Contents/HomeAssets/holo_spent:ywingholo_rbl-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_rbl-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level           |11                               |2-10                        |1                           |
|----------------|---------------------------------|----------------------------|----------------------------|
|Asset name      |fx_trap_starship_strike_rbl-up11 |fx_trap_starship_strike_rbl |fx_trap_starship_strike_rbl |
|Bundle name     |fx_trap_starship_strike_rbl-up11 |fx_trap_starship_strike_rbl |fx_trap_starship_strike_rbl |
|Cycle time      |0s                               |(not found)                 |(not found)                 |
|Icon asset name |icon_starship_trap_ywing_rbl-up11|icon_starship_trap_ywing_rbl|icon_starship_trap_ywing_rbl|
|Icon bundle name|icon_starship_trap_ywing_rbl-up11|icon_starship_trap_ywing_rbl|icon_starship_trap_ywing_rbl|
|Prestige        |true                             |(not found)                 |(not found)                 |
|Store tab       |(not found)                      |(not found)                 |defenses                    |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 15

|Level|11|10|9 |8 |7 |6 |5 |4 |3 |2 |1 |
|-----|--|--|--|--|--|--|--|--|--|--|--|
|Xp   |41|40|39|38|37|36|35|34|33|32|30|


