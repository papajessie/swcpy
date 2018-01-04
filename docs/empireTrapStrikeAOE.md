---
title: TIE Bomber Trap (empireTrapStrikeAOE)
category: building
---

# TIE Bomber Trap (empireTrapStrikeAOE) — version 1113

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: trap
  * Side: Empire
  * Force reticle when targeted: Yes
  * Hide if locked: No
  * Trap disarm conditions: EventSuccess
  * Trap rearm credits cost: 0
  * Trap target type: Self
  * Trap trigger conditions: Radius(2) & ArmorNot(flierInfantry)
  * Type: trap

|Level                    |1                                                      |2                                                      |3                                                      |4                                                      |5                                                      |6                                                      |7                                                      |8                                                      |9                                                      |10                                                      |
|-------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|
|Health                   |2500                                                   |3750                                                   |4500                                                   |6000                                                   |7250                                                   |8500                                                   |9750                                                   |11000                                                  |12250                                                  |13500                                                   |
|Max quantity             |2                                                      |2                                                      |2                                                      |2                                                      |2                                                      |2                                                      |3                                                      |3                                                      |4                                                      |4                                                       |
|Time                     |1m                                                     |15m                                                    |2h                                                     |12h                                                    |1d                                                     |1d12h                                                  |2d                                                     |3d                                                     |6d                                                     |1w3d                                                    |
|Trap air strike          |["shp_title_TIEBomberTrap" level 1](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 2](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 3](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 4](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 5](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 6](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 7](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 8](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 9](TIEBomberTrap.html)|["shp_title_TIEBomberTrap" level 10](TIEBomberTrap.html)|
|Trap rearm materials cost|500                                                    |1000                                                   |1500                                                   |1800                                                   |2000                                                   |3000                                                   |5000                                                   |6000                                                   |8000                                                   |15000                                                   |


### Training stats

|Level        |1                              |2                              |3                              |4                              |5                              |6                              |7                              |8                              |9                              |10                              |
|-------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|--------------------------------|
|Training cost|600 All.                       |2000 All.                      |10000 All.                     |30000 All.                     |60000 All.                     |160000 All.                    |350000 All.                    |500000 All.                    |800000 All.                    |1500000 All.                    |
|Building     |[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 10](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |1                          |2                          |3                          |4                          |5                          |6                          |7                          |8                          |9                          |10                          |
|---------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|----------------------------|
|Trap ID        |trap_EmpireStrikeAOE1      |trap_EmpireStrikeAOE2      |trap_EmpireStrikeAOE3      |trap_EmpireStrikeAOE4      |trap_EmpireStrikeAOE5      |trap_EmpireStrikeAOE6      |trap_EmpireStrikeAOE7      |trap_EmpireStrikeAOE8      |trap_EmpireStrikeAOE9      |trap_EmpireStrikeAOE10      |
|Trap event data|specialAttackTIEBomberTrap1|specialAttackTIEBomberTrap2|specialAttackTIEBomberTrap3|specialAttackTIEBomberTrap4|specialAttackTIEBomberTrap5|specialAttackTIEBomberTrap6|specialAttackTIEBomberTrap7|specialAttackTIEBomberTrap8|specialAttackTIEBomberTrap9|specialAttackTIEBomberTrap10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: fx_trap_starship_strike_emp
  * Buff asset offset: -1,0.8,-1
  * Bundle name: fx_trap_starship_strike_emp
  * Destruct FX: fx_trap_bomber
  * Icon asset name: icon_starship_trap_tiebomber_emp
  * Icon bundle name: icon_starship_trap_tiebomber_emp
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 110
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:tiebomberholo_emp-mod Contents/HomeAssets/holo_spent:tiebomberholo_emp-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_emp-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level    |1       |2-10       |
|---------|--------|-----------|
|Store tab|defenses|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 234

|Level|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|-----|--|--|--|--|--|--|--|--|--|--|
|Xp   |30|32|33|34|35|36|37|38|39|40|


