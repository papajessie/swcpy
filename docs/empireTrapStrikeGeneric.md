---
title: TIE Fighter Trap (empireTrapStrikeGeneric)
category: building
---

# TIE Fighter Trap (empireTrapStrikeGeneric) — version 1117

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

|Level                    |1                                                        |2                                                        |3                                                        |4                                                        |5                                                        |6                                                        |7                                                        |8                                                        |9                                                        |10                                                        |
|-------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|
|Health                   |2500                                                     |3750                                                     |4500                                                     |6000                                                     |7250                                                     |8500                                                     |9750                                                     |11000                                                    |12250                                                    |13500                                                     |
|Max quantity             |1                                                        |1                                                        |1                                                        |2                                                        |2                                                        |4                                                        |4                                                        |6                                                        |6                                                        |6                                                         |
|Time                     |1m                                                       |15m                                                      |2h                                                       |12h                                                      |1d                                                       |1d12h                                                    |2d                                                       |3d                                                       |6d                                                       |1w3d                                                      |
|Trap air strike          |["shp_title_TIEFighterTrap" level 1](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 2](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 3](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 4](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 5](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 6](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 7](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 8](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 9](TIEFighterTrap.html)|["shp_title_TIEFighterTrap" level 10](TIEFighterTrap.html)|
|Trap rearm materials cost|300                                                      |600                                                      |900                                                      |1200                                                     |1800                                                     |2000                                                     |2700                                                     |3000                                                     |3500                                                     |6000                                                      |


### Training stats

|Level        |1                              |2                              |3                              |4                              |5                              |6                              |7                              |8                              |9                              |10                              |
|-------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|--------------------------------|
|Training cost|300 All.                       |1000 All.                      |5000 All.                      |15000 All.                     |30000 All.                     |70000 All.                     |150000 All.                    |300000 All.                    |900000 All.                    |1500000 All.                    |
|Building     |[Headquarters 3](empireHQ.html)|[Headquarters 3](empireHQ.html)|[Headquarters 3](empireHQ.html)|[Headquarters 4](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 10](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |1                           |2                           |3                           |4                           |5                           |6                           |7                           |8                           |9                           |10                           |
|---------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|-----------------------------|
|Trap ID        |trap_EmpireStrikeGeneric1   |trap_EmpireStrikeGeneric2   |trap_EmpireStrikeGeneric3   |trap_EmpireStrikeGeneric4   |trap_EmpireStrikeGeneric5   |trap_EmpireStrikeGeneric6   |trap_EmpireStrikeGeneric7   |trap_EmpireStrikeGeneric8   |trap_EmpireStrikeGeneric9   |trap_EmpireStrikeGeneric10   |
|Trap event data|specialAttackTIEFighterTrap1|specialAttackTIEFighterTrap2|specialAttackTIEFighterTrap3|specialAttackTIEFighterTrap4|specialAttackTIEFighterTrap5|specialAttackTIEFighterTrap6|specialAttackTIEFighterTrap7|specialAttackTIEFighterTrap8|specialAttackTIEFighterTrap9|specialAttackTIEFighterTrap10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: fx_trap_starship_strike_emp
  * Buff asset offset: -1,0.8,-1
  * Bundle name: fx_trap_starship_strike_emp
  * Destruct FX: fx_trap_fighter
  * Icon asset name: icon_starship_trap_tiefighter_emp
  * Icon bundle name: icon_starship_trap_tiefighter_emp
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 100
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:tiefighterholo_emp-mod Contents/HomeAssets/holo_spent:tiefighterholo_emp-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_emp-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level    |1       |2-10       |
|---------|--------|-----------|
|Store tab|defenses|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0
  * Order: 232

|Level|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|-----|--|--|--|--|--|--|--|--|--|--|
|Xp   |30|32|33|34|35|36|37|38|39|40|


