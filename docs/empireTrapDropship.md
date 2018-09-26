---
title: IDT Trap (empireTrapDropship)
category: building
---

# IDT Trap (empireTrapDropship)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: trap
  * Side: Empire
  * Force reticle when targeted: Yes
  * Hide if locked: No
  * Max quantity: 2
  * Trap disarm conditions: EventSuccess
  * Trap rearm credits cost: 0
  * Trap target type: Self
  * Trap trigger conditions: Radius(5)
  * Type: trap

|Level                    |1                                                               |2                                                               |3                                                               |4                                                               |5                                                               |6                                                               |7                                                               |8                                                               |9                                                               |10                                                               |
|-------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------|
|Cross credits            |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                      |
|Cross materials          |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                      |
|Cross time               |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                      |
|Health                   |2500                                                            |3750                                                            |4500                                                            |6000                                                            |7250                                                            |8500                                                            |9750                                                            |11000                                                           |12250                                                           |13500                                                            |
|Produce                  |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                     |(not found)                                                      |
|Time                     |1m                                                              |15m                                                             |2h                                                              |12h                                                             |1d                                                              |1d12h                                                           |2d                                                              |3d                                                              |6d                                                              |1w3d                                                             |
|Trap air strike          |[Imperial Dropship Transport level 1](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 2](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 3](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 4](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 5](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 6](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 7](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 8](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 9](ImperialDropshipTrap.html)|[Imperial Dropship Transport level 10](ImperialDropshipTrap.html)|
|Trap rearm materials cost|2000                                                            |4000                                                            |6000                                                            |8000                                                            |10000                                                           |12000                                                           |14000                                                           |16000                                                           |18000                                                           |22000                                                            |


|Level                    |11                                                           |
|-------------------------|-------------------------------------------------------------|
|Cross credits            |0                                                            |
|Cross materials          |0                                                            |
|Cross time               |0s                                                           |
|Health                   |14250                                                        |
|Produce                  |0                                                            |
|Time                     |5d                                                           |
|Trap air strike          |[Imperial Dropship Transport level 11](ImperialDropship.html)|
|Trap rearm materials cost|26000                                                        |


### Training stats

|Level        |1                              |2                              |3                              |4                              |5                              |6                              |7                              |8                              |9                              |10                              |
|-------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|--------------------------------|
|Training cost|1800 All.                      |3600 All.                      |20000 All.                     |75000 All.                     |150000 All.                    |400000 All.                    |800000 All.                    |1000000 All.                   |2000000 All.                   |3500000 All.                    |
|Building     |[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 10](empireHQ.html)|


|Level        |11                              |
|-------------|--------------------------------|
|Training cost|4550000 All.                    |
|Building     |[Headquarters 11](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Unit size on map: 1x1

## Internal stats

These stats internal to the system link different parts of data together.

  * Trap event type: SpecialAttack

|Level          |1                                 |2                                 |3                                 |4                                 |5                                 |6                                 |7                                 |8                                 |9                                 |10                                 |
|---------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|-----------------------------------|
|Trap ID        |trap_EmpireDropship1              |trap_EmpireDropship2              |trap_EmpireDropship3              |trap_EmpireDropship4              |trap_EmpireDropship5              |trap_EmpireDropship6              |trap_EmpireDropship7              |trap_EmpireDropship8              |trap_EmpireDropship9              |trap_EmpireDropship10              |
|Trap event data|specialAttackImperialDropshipTrap1|specialAttackImperialDropshipTrap2|specialAttackImperialDropshipTrap3|specialAttackImperialDropshipTrap4|specialAttackImperialDropshipTrap5|specialAttackImperialDropshipTrap6|specialAttackImperialDropshipTrap7|specialAttackImperialDropshipTrap8|specialAttackImperialDropshipTrap9|specialAttackImperialDropshipTrap10|


|Level          |11                             |
|---------------|-------------------------------|
|Trap ID        |trap_EmpireDropship11          |
|Trap event data|specialAttackImperialDropship11|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Buff asset offset: -1,0.8,-1
  * Destruct FX: fx_debris_3x3
  * Icon camera position: -32.79,29.4,27.07
  * Icon lookat position: 0.79,2.54,-0.62
  * Stash order: 100
  * Trap add ons: Contents/SharedAssets/active_holo/holo_armed:dropshipholo_emp-mod Contents/HomeAssets/holo_spent:dropshipholo_emp-mod_red Contents/HomeAssets/holo_spent:fx_repair_smoke Contents/SharedAssets/trap_spent/starshiptrap_emp-mod_disarmed:fx_starship_trap_spent_cone_emitter
  * Trap reveal audio: sfx_trap_appear

|Level           |1                          |2-10                       |11                              |
|----------------|---------------------------|---------------------------|--------------------------------|
|Asset name      |fx_trap_starship_strike_emp|fx_trap_starship_strike_emp|fx_trap_starship_strike_emp-up11|
|Bundle name     |fx_trap_starship_strike_emp|fx_trap_starship_strike_emp|fx_trap_starship_strike_emp-up11|
|Cycle time      |(not found)                |(not found)                |0s                              |
|Icon asset name |icon_dropship_trap_emp     |icon_dropship_trap_emp     |icon_dropship_trap_emp-up11     |
|Icon bundle name|icon_dropship_trap_emp     |icon_dropship_trap_emp     |icon_dropship_trap_emp-up11     |
|Prestige        |(not found)                |(not found)                |true                            |
|Store tab       |defenses                   |(not found)                |(not found)                     |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 24

|Level |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------|--|--|--|--|--|--|--|--|--|--|
|Max XP|60|64|66|68|70|72|74|76|78|80|
|Xp    |30|32|33|34|35|36|37|38|39|40|


|Level |11|
|------|--|
|Max XP|82|
|Xp    |41|


