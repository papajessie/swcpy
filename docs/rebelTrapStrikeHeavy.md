---
title: Fang Fighter Trap (rebelTrapStrikeHeavy)
category: building
---

# Fang Fighter Trap (rebelTrapStrikeHeavy) — version 1119

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

|Level                    |1                                                          |2                                                          |3                                                          |4                                                          |5                                                          |6                                                          |7                                                          |8                                                          |9                                                          |10                                                          |
|-------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------|
|Health                   |2500                                                       |3750                                                       |4500                                                       |6000                                                       |7250                                                       |8500                                                       |9750                                                       |11000                                                      |12250                                                      |13500                                                       |
|Max quantity             |1                                                          |1                                                          |1                                                          |2                                                          |2                                                          |2                                                          |2                                                          |2                                                          |2                                                          |2                                                           |
|Time                     |1m30s                                                      |22m30s                                                     |3h                                                         |18h                                                        |1d12h                                                      |2d6h                                                       |3d                                                         |4d12h                                                      |1w2d                                                       |2w1d                                                        |
|Trap air strike          |["shp_title_FangFighterTrap" level 1](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 2](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 3](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 4](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 5](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 6](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 7](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 8](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 9](FangFighterTrap.html)|["shp_title_FangFighterTrap" level 10](FangFighterTrap.html)|
|Trap rearm materials cost|750                                                        |1500                                                       |2250                                                       |2700                                                       |3000                                                       |4500                                                       |7500                                                       |9000                                                       |12000                                                      |22500                                                       |


### Training stats

|Level        |1                             |2                             |3                             |4                             |5                             |6                             |7                             |8                             |9                              |10                             |
|-------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|-------------------------------|-------------------------------|
|Training cost|900 All.                      |3000 All.                     |15000 All.                    |45000 All.                    |90000 All.                    |240000 All.                   |525000 All.                   |750000 All.                   |1200000 All.                   |2250000 All.                   |
|Building     |[Headquarters 7](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |1                            |2                            |3                            |4                            |5                            |6                            |7                            |8                            |9                            |10                            |
|---------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|------------------------------|
|Trap ID        |trap_RebelStrikeHeavy1       |trap_RebelStrikeHeavy2       |trap_RebelStrikeHeavy3       |trap_RebelStrikeHeavy4       |trap_RebelStrikeHeavy5       |trap_RebelStrikeHeavy6       |trap_RebelStrikeHeavy7       |trap_RebelStrikeHeavy8       |trap_RebelStrikeHeavy9       |trap_RebelStrikeHeavy10       |
|Trap event data|specialAttackFangFighterTrap1|specialAttackFangFighterTrap2|specialAttackFangFighterTrap3|specialAttackFangFighterTrap4|specialAttackFangFighterTrap5|specialAttackFangFighterTrap6|specialAttackFangFighterTrap7|specialAttackFangFighterTrap8|specialAttackFangFighterTrap9|specialAttackFangFighterTrap10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: fx_trap_starship_strike_rbl
  * Buff asset offset: -1,0.8,-1
  * Bundle name: fx_trap_starship_strike_rbl
  * Destruct FX: fx_trap_fighter
  * Icon asset name: icon_fangfighter_trap_emp
  * Icon bundle name: icon_fangfighter_trap_emp
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 125
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:fangfighterholo_rbl-mod Contents/HomeAssets/holo_spent:fangfighterholo_rbl-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_rbl-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level    |1       |2-10       |
|---------|--------|-----------|
|Store tab|defenses|(not found)|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Max XP: 0

|Level|1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|-----|--|--|--|--|--|--|--|--|--|--|
|Xp   |30|32|33|34|35|36|37|38|39|40|


