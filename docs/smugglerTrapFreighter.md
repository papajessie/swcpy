---
title: bldtitlesmugglerTrapFreighter (smugglerTrapFreighter)
category: building
---

# bldtitlesmugglerTrapFreighter (smugglerTrapFreighter) — version 1106

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: trap
  * Side: Independant units
  * Force reticle when targeted: Yes
  * Health: 5000
  * Hide if locked: Yes
  * Time: 10s
  * Trap disarm conditions: EventSuccess
  * Trap rearm credits cost: 0
  * Trap target type: Self
  * Trap trigger conditions: Radius(2) & ArmorNot(flierInfantry)
  * Type: trap

|Level                    |1                                              |2                                              |3                                              |4                                              |5                                              |6                                              |7                                              |8                                              |9                                              |10                                              |
|-------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|------------------------------------------------|
|Max quantity             |1                                              |1                                              |1                                              |2                                              |2                                              |2                                              |2                                              |2                                              |2                                              |2                                               |
|Trap air strike          |["shp_title_XWingTrap" level 1](XWingTrap.html)|["shp_title_XWingTrap" level 2](XWingTrap.html)|["shp_title_XWingTrap" level 3](XWingTrap.html)|["shp_title_XWingTrap" level 4](XWingTrap.html)|["shp_title_XWingTrap" level 5](XWingTrap.html)|["shp_title_XWingTrap" level 6](XWingTrap.html)|["shp_title_XWingTrap" level 7](XWingTrap.html)|["shp_title_XWingTrap" level 8](XWingTrap.html)|["shp_title_XWingTrap" level 9](XWingTrap.html)|["shp_title_XWingTrap" level 10](XWingTrap.html)|
|Trap rearm materials cost|300                                            |600                                            |900                                            |1200                                           |1800                                           |2000                                           |2700                                           |3000                                           |3500                                           |6000                                            |


### Training stats

  * Training cost: 1000$

|Level   |1                                            |2                                            |3                                            |4                                            |5                                            |6                                            |7                                            |8                                            |9                                            |10                                            |
|--------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|----------------------------------------------|
|Building|["bld_title_syndicateHQ" 1](syndicateHQ.html)|["bld_title_syndicateHQ" 2](syndicateHQ.html)|["bld_title_syndicateHQ" 3](syndicateHQ.html)|["bld_title_syndicateHQ" 4](syndicateHQ.html)|["bld_title_syndicateHQ" 5](syndicateHQ.html)|["bld_title_syndicateHQ" 6](syndicateHQ.html)|["bld_title_syndicateHQ" 7](syndicateHQ.html)|["bld_title_syndicateHQ" 8](syndicateHQ.html)|["bld_title_syndicateHQ" 9](syndicateHQ.html)|["bld_title_syndicateHQ" 10](syndicateHQ.html)|


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

  * Asset name: fx_trap_starship_strike_smg
  * Buff asset offset: -1,1,-1
  * Bundle name: fx_trap_starship_strike_smg
  * Destruct FX: fx_debris_{0}x{1}
  * Stash order: 1000
  * Store tab: not_in_store
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:xwingholo_rbl-mod Contents/HomeAssets/holo_spent:xwingholo_rbl-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_rbl-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

## Uninterpreted stats

Seriously, we don't really know what to do with these.

|Level |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------|----|----|----|----|----|----|----|----|----|----|
|Max XP|5   |8   |11  |26  |32  |36  |42  |46  |52  |56  |
|Order |1208|1209|1210|1211|1212|1213|1214|1215|1216|1217|
|Xp    |5   |8   |11  |13  |16  |18  |21  |23  |26  |28  |


