---
title: Burst Turret (empireBurstTurret)
category: building
---

# Burst Turret (empireBurstTurret)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: turret
  * Cross credits: 0
  * Side: Empire
  * Force reticle when targeted: No
  * Hide if locked: No
  * Produce: 0
  * Type: turret

|Level          |11    |10    |9     |8     |7    |6    |5    |4    |3    |2   |1   |
|---------------|------|------|------|------|-----|-----|-----|-----|-----|----|----|
|Cross materials|702000|540000|360000|135000|90000|72000|27000|13500|4500 |900 |450 |
|Cross time     |3d    |2d    |1d12h |1d4h  |20h  |14h  |8h   |4h48m|1h12m|12m |10m |
|Health         |28500 |27000 |24500 |22000 |17500|16000|14500|12000|9000 |7500|5000|
|Max quantity   |22    |20    |18    |16    |14   |12   |10   |8    |6    |4   |2   |
|Time           |1w1d  |1w3d  |1w1d  |6d    |4d   |2d12h|1d12h|16h  |4h   |30m |1m  |


### Training stats

|Level        |11                              |10                              |9                              |8                              |7                              |6                              |5                              |4                              |3                              |2                              |1                              |
|-------------|--------------------------------|--------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|Training cost|6500000 All.                    |5000000 All.                    |3000000 All.                   |1000000 All.                   |500000 All.                    |250000 All.                    |100000 All.                    |55000 All.                     |20000 All.                     |3000 All.                      |1500 All.                      |
|Building     |[Headquarters 11](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Empire Burst Turret


### Targeting

  * Turret max attack range: 9
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret flying infantry (80)**, **Turret heavy infantry (80)**, _Turret droideka (60)_, _Turret flying vehicle (60)_, _Turret headquarters (60)_, _Turret heavy vehicle (60)_, _Turret infantry (60)_, _Turret light vehicle (60)_, _Turret other building (60)_, _Turret ressource generator (60)_, _Turret storage (60)_, _Turret support troop (60)_, _Turret turret (60)_, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)

|Level            |11|1-10|
|-----------------|--|----|
|Turret view range|11|10  |


### Shooting

  * Turret animation delay: 0s
  * Turret charge time: 1.750s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 1.200s
  * Turret shot count: 8
  * Turret shot delay: 175ms

|Level                 |11  |10  |9   |8   |7   |6   |5  |4  |3  |2  |1  |
|----------------------|----|----|----|----|----|----|---|---|---|---|---|
|Turret damage per shot|1508|1432|1305|1209|1114|1019|923|764|573|477|318|


|Level                                     |11   |10   |9    |8   |7   |6   |5   |4   |3   |2   |1   |
|------------------------------------------|-----|-----|-----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |2485 |2475 |2255 |2090|1926|1761|1594|1320|990 |825 |550 |
|Turret attack calculated damage per second|2889 |2743 |2500 |2316|2134|1952|1768|1463|1097|914 |609 |
|Turret attack calculated damage per clip  |12064|11456|10440|9672|8912|8152|7384|6112|4584|3816|2544|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 4.175s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 10
  * Turret attack damage multipliers: **(140)**: Turret attack flying infantry, Turret attack flying vehicle, **(125)**: Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, **(100)**: Turret attack droideka, Turret attack headquarters, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 8

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: burst_turret
  * Turret projectile type: projectileEmpireBurstTurret

|Level    |11                   |10                   |9                   |8                   |7                   |6                   |5                   |4                   |3                   |2                   |1                   |
|---------|---------------------|---------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
|Turret id|t_empireBurstTurret11|t_empireBurstTurret10|t_empireBurstTurret9|t_empireBurstTurret8|t_empireBurstTurret7|t_empireBurstTurret6|t_empireBurstTurret5|t_empireBurstTurret4|t_empireBurstTurret3|t_empireBurstTurret2|t_empireBurstTurret1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_blasternest_1":20,"sfx_attack_blasternest_2":20,"sfx_attack_blasternest_3":20,"sfx_attack_blasternest_4":20,"sfx_attack_blasternest_5":20
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Icon lookat position: 0.41,2.03,-0.59
  * Stash order: 60
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_r_sm
  * Turret attack hit spark: fx_blaster_hit_r_sm
  * Turret attack max scale: 125
  * Turret attack muzzle flash: fx_blaster_flash_r_sm
  * Turret attack name: Empire Burst Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: bruiserInfantry
  * Turret gun position: "locator_gun":1
  * Turret max scale: 0
  * Turret tracker name: n/a

|Level                             |11                      |10                      |9                      |8                      |7                      |6                      |5                      |4                      |3                      |2                      |1                      |
|----------------------------------|------------------------|------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|Asset name                        |burstturret_emp-mod-up11|burstturret_emp-mod-up10|burstturret_emp-mod-up9|burstturret_emp-mod-up8|burstturret_emp-mod-up7|burstturret_emp-mod-up6|burstturret_emp-mod-up5|burstturret_emp-mod-up4|burstturret_emp-mod-up3|burstturret_emp-mod-up2|burstturret_emp-mod-up1|
|Buff asset offset                 |-1.2,4.2,-1.2           |-1.2,4.2,-1.2           |-1.2,4.2,-1.2          |-1.2,4.2,-1.2          |-1.2,4.2,-1.2          |-1.2,3.6,-1.2          |-1,3.6,-1              |-0.6,3,-0.6            |-0.6,3,-0.6            |-0.6,3,-0.6            |-0.6,3,-0.6            |
|Bundle name                       |burstturret_emp-mod-up11|burstturret_emp-mod-up10|burstturret_emp-mod-up9|burstturret_emp-mod-up8|burstturret_emp-mod-up7|burstturret_emp-mod-up6|burstturret_emp-mod-up5|burstturret_emp-mod-up4|burstturret_emp-mod-up3|burstturret_emp-mod-up2|burstturret_emp-mod-up1|
|Icon camera position              |-27.3,32.57,31.45       |-27.3,32.57,31.45       |-27.3,32.57,31.45      |-27.71,33.03,31.93     |-28.36,33.75,32.71     |-28.03,33.38,32.27     |-28.3,33.68,32.61      |-28.02,33.36,32.28     |-23.53,28.41,27.14     |-22.49,27.21,25.84     |-22.7,27.44,26.09      |
|Prestige                          |true                    |(not found)             |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |
|Store tab                         |(not found)             |(not found)             |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |decorations            |
|Turret displayed damage per second|2485                    |2475                    |2255                   |2090                   |1926                   |1761                   |1594                   |1320                   |990                    |825                    |550                    |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 23
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.9161676649999999089146740516298450529575347900390625

|Level |11  |10  |9   |8  |7  |6  |5  |4  |3  |2  |1 |
|------|----|----|----|---|---|---|---|---|---|---|--|
|Max XP|1630|1400|1170|960|770|600|450|320|210|120|50|
|Xp    |75  |70  |65  |60 |55 |50 |45 |40 |35 |30 |25|


