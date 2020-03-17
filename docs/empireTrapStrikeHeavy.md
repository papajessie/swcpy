---
title: TIE Striker Trap (empireTrapStrikeHeavy)
category: building
---

# TIE Striker Trap (empireTrapStrikeHeavy)

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

|Level                    |11                                                    |10                                                    |9                                                    |8                                                    |7                                                    |6                                                    |5                                                    |4                                                    |3                                                    |2                                                    |1                                                    |
|-------------------------|------------------------------------------------------|------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
|Cross credits            |0                                                     |(not found)                                           |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |
|Cross materials          |0                                                     |(not found)                                           |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |
|Cross time               |0s                                                    |(not found)                                           |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |
|Health                   |14250                                                 |13500                                                 |12250                                                |11000                                                |9750                                                 |8500                                                 |7250                                                 |6000                                                 |4500                                                 |3750                                                 |2500                                                 |
|Max quantity             |2                                                     |2                                                     |2                                                    |2                                                    |2                                                    |2                                                    |2                                                    |2                                                    |1                                                    |1                                                    |1                                                    |
|Produce                  |0                                                     |(not found)                                           |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |(not found)                                          |
|Trap air strike          |["shp_title_AtmosMigTrap" level 10](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 10](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 9](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 8](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 7](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 6](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 5](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 4](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 3](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 2](AtmosMigTrap.html)|["shp_title_AtmosMigTrap" level 1](AtmosMigTrap.html)|
|Trap rearm materials cost|33000                                                 |22500                                                 |12000                                                |9000                                                 |7500                                                 |4500                                                 |3000                                                 |2700                                                 |2250                                                 |1500                                                 |750                                                  |


### Training stats

|Level        |11                              |9-10                            |7-8                            |4-6                            |1-3                            |
|-------------|--------------------------------|--------------------------------|-------------------------------|-------------------------------|-------------------------------|
|Training cost|Free                            |1 All.                          |1 All.                         |1 All.                         |1 All.                         |
|Building     |[Headquarters 11](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 7](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |11                         |10                         |9                         |8                         |7                         |6                         |5                         |4                         |3                         |2                         |1                         |
|---------------|---------------------------|---------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
|Trap ID        |trap_EmpireStrikeHeavy11   |trap_EmpireStrikeHeavy10   |trap_EmpireStrikeHeavy9   |trap_EmpireStrikeHeavy8   |trap_EmpireStrikeHeavy7   |trap_EmpireStrikeHeavy6   |trap_EmpireStrikeHeavy5   |trap_EmpireStrikeHeavy4   |trap_EmpireStrikeHeavy3   |trap_EmpireStrikeHeavy2   |trap_EmpireStrikeHeavy1   |
|Trap event data|specialAttackAtmosMigTrap11|specialAttackAtmosMigTrap10|specialAttackAtmosMigTrap9|specialAttackAtmosMigTrap8|specialAttackAtmosMigTrap7|specialAttackAtmosMigTrap6|specialAttackAtmosMigTrap5|specialAttackAtmosMigTrap4|specialAttackAtmosMigTrap3|specialAttackAtmosMigTrap2|specialAttackAtmosMigTrap1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Buff asset offset: -1,0.8,-1
  * Destruct FX: fx_trap_fighter
  * Icon asset name: icon_atmosmig_trap_emp
  * Icon bundle name: icon_atmosmig_trap_emp
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 125
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:atmosmigholo_emp-mod Contents/HomeAssets/holo_spent:atmosmigholo_emp-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_emp-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level      |11                              |2-10                       |1                          |
|-----------|--------------------------------|---------------------------|---------------------------|
|Asset name |fx_trap_starship_strike_emp-up11|fx_trap_starship_strike_emp|fx_trap_starship_strike_emp|
|Bundle name|fx_trap_starship_strike_emp-up11|fx_trap_starship_strike_emp|fx_trap_starship_strike_emp|
|Cycle time |0s                              |(not found)                |(not found)                |
|Prestige   |true                            |(not found)                |(not found)                |
|Store tab  |(not found)                     |(not found)                |defenses                   |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 23

|Level|11|10|9 |8 |7 |6 |5 |4 |3 |2 |1 |
|-----|--|--|--|--|--|--|--|--|--|--|--|
|Xp   |41|40|39|38|37|36|35|34|33|32|30|


