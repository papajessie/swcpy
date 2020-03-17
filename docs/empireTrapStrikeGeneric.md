---
title: TIE Fighter Trap (empireTrapStrikeGeneric)
category: building
---

# TIE Fighter Trap (empireTrapStrikeGeneric)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: trap
  * Side: Empire
  * Force reticle when targeted: Yes
  * Hide if locked: No
  * Time: 10s
  * Trap disarm conditions: EventSuccess
  * Trap rearm credits cost: 0
  * Trap target type: Self
  * Trap trigger conditions: Radius(2) & ArmorNot(flierInfantry)
  * Type: trap

|Level                    |11                                                        |10                                                        |9                                                        |8                                                        |7                                                        |6                                                        |5                                                        |4                                                        |3                                                        |2                                                        |1                                                        |
|-------------------------|----------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Cross credits            |0                                                         |(not found)                                               |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |
|Cross materials          |0                                                         |(not found)                                               |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |
|Cross time               |0s                                                        |(not found)                                               |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |
|Health                   |14250                                                     |13500                                                     |12250                                                    |11000                                                    |9750                                                     |8500                                                     |7250                                                     |6000                                                     |4500                                                     |3750                                                     |2500                                                     |
|Max quantity             |6                                                         |6                                                         |6                                                        |6                                                        |4                                                        |4                                                        |2                                                        |2                                                        |1                                                        |1                                                        |1                                                        |
|Produce                  |0                                                         |(not found)                                               |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |
|Trap air strike          |["shp_title_TIEFighterTrap" level 10](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 10](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 9](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 8](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 7](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 6](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 5](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 4](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 3](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 2](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 1](TIEFighterTrap.html)|
|Trap rearm materials cost|8500                                                      |6000                                                      |3500                                                     |3000                                                     |2700                                                     |2000                                                     |1800                                                     |1200                                                     |900                                                      |600                                                      |300                                                      |


### Training stats

|Level        |11                              |10                              |9                              |8                              |7                              |6                              |5                              |4                              |1-3                            |
|-------------|--------------------------------|--------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|Training cost|1 All.                          |1$                              |1$                             |1$                             |1$                             |1$                             |1$                             |1$                             |1$                             |
|Building     |[Headquarters 11](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 4](empireHQ.html)|[Headquarters 3](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |11                           |10                           |9                           |8                           |7                           |6                           |5                           |4                           |3                           |2                           |1                           |
|---------------|-----------------------------|-----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
|Trap ID        |trap_EmpireStrikeGeneric11   |trap_EmpireStrikeGeneric10   |trap_EmpireStrikeGeneric9   |trap_EmpireStrikeGeneric8   |trap_EmpireStrikeGeneric7   |trap_EmpireStrikeGeneric6   |trap_EmpireStrikeGeneric5   |trap_EmpireStrikeGeneric4   |trap_EmpireStrikeGeneric3   |trap_EmpireStrikeGeneric2   |trap_EmpireStrikeGeneric1   |
|Trap event data|specialAttackTIEFighterTrap10|specialAttackTIEFighterTrap10|specialAttackTIEFighterTrap9|specialAttackTIEFighterTrap8|specialAttackTIEFighterTrap7|specialAttackTIEFighterTrap6|specialAttackTIEFighterTrap5|specialAttackTIEFighterTrap4|specialAttackTIEFighterTrap3|specialAttackTIEFighterTrap2|specialAttackTIEFighterTrap1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Buff asset offset: -1,0.8,-1
  * Destruct FX: fx_trap_fighter
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 100
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:tiefighterholo_emp-mod Contents/HomeAssets/holo_spent:tiefighterholo_emp-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_emp-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level           |11                                    |2-10                             |1                                |
|----------------|--------------------------------------|---------------------------------|---------------------------------|
|Asset name      |fx_trap_starship_strike_emp-up11      |fx_trap_starship_strike_emp      |fx_trap_starship_strike_emp      |
|Bundle name     |fx_trap_starship_strike_emp-up11      |fx_trap_starship_strike_emp      |fx_trap_starship_strike_emp      |
|Cycle time      |0s                                    |(not found)                      |(not found)                      |
|Icon asset name |icon_starship_trap_tiefighter_emp-up11|icon_starship_trap_tiefighter_emp|icon_starship_trap_tiefighter_emp|
|Icon bundle name|icon_starship_trap_tiefighter_emp-up11|icon_starship_trap_tiefighter_emp|icon_starship_trap_tiefighter_emp|
|Prestige        |true                                  |(not found)                      |(not found)                      |
|Store tab       |(not found)                           |(not found)                      |defenses                         |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 14

|Level|11|10|9 |8 |7 |6 |5 |4 |3 |2 |1 |
|-----|--|--|--|--|--|--|--|--|--|--|--|
|Xp   |41|40|39|38|37|36|35|34|33|32|30|


