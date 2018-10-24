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

|Level          |1   |2   |3    |4    |5    |6    |7    |8     |9     |10    |
|---------------|----|----|-----|-----|-----|-----|-----|------|------|------|
|Cross materials|450 |900 |4500 |13500|27000|72000|90000|135000|360000|540000|
|Cross time     |10m |12m |1h12m|4h48m|8h   |14h  |20h  |1d4h  |1d12h |2d    |
|Health         |5000|7500|9000 |12000|14500|16000|17500|22000 |24500 |27000 |
|Max quantity   |2   |4   |6    |8    |10   |12   |14   |16    |18    |20    |
|Time           |1m  |30m |4h   |16h  |1d12h|2d12h|4d   |6d    |1w1d  |1w3d  |


|Level          |11    |
|---------------|------|
|Cross materials|702000|
|Cross time     |3d    |
|Health         |28500 |
|Max quantity   |22    |
|Time           |1w1d  |


### Training stats

|Level        |1                              |2                              |3                              |4                              |5                              |6                              |7                              |8                              |9                              |10                              |
|-------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|--------------------------------|
|Training cost|1500 All.                      |3000 All.                      |20000 All.                     |55000 All.                     |100000 All.                    |250000 All.                    |500000 All.                    |1000000 All.                   |3000000 All.                   |5000000 All.                    |
|Building     |[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 10](empireHQ.html)|


|Level        |11                              |
|-------------|--------------------------------|
|Training cost|6500000 All.                    |
|Building     |[Headquarters 11](empireHQ.html)|


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

|Level            |1-10|11|
|-----------------|----|--|
|Turret view range|10  |11|


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

|Level                 |1  |2  |3  |4  |5  |6   |7   |8   |9   |10  |
|----------------------|---|---|---|---|---|----|----|----|----|----|
|Turret damage per shot|318|477|573|764|923|1019|1114|1209|1305|1432|


|Level                 |11  |
|----------------------|----|
|Turret damage per shot|1508|


|Level                                     |1   |2   |3   |4   |5   |6   |7   |8   |9    |10   |
|------------------------------------------|----|----|----|----|----|----|----|----|-----|-----|
|Turret displayed damage per second        |550 |825 |990 |1320|1594|1761|1926|2090|2255 |2475 |
|Turret attack calculated damage per second|609 |914 |1097|1463|1768|1952|2134|2316|2500 |2743 |
|Turret attack calculated damage per clip  |2544|3816|4584|6112|7384|8152|8912|9672|10440|11456|


|Level                                     |11   |
|------------------------------------------|-----|
|Turret displayed damage per second        |2485 |
|Turret attack calculated damage per second|2889 |
|Turret attack calculated damage per clip  |12064|


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

|Level    |1                   |2                   |3                   |4                   |5                   |6                   |7                   |8                   |9                   |10                   |
|---------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|---------------------|
|Turret id|t_empireBurstTurret1|t_empireBurstTurret2|t_empireBurstTurret3|t_empireBurstTurret4|t_empireBurstTurret5|t_empireBurstTurret6|t_empireBurstTurret7|t_empireBurstTurret8|t_empireBurstTurret9|t_empireBurstTurret10|


|Level    |11                   |
|---------|---------------------|
|Turret id|t_empireBurstTurret11|


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

|Level                             |1                      |2                      |3                      |4                      |5                      |6                      |7                      |8                      |9                      |10                      |
|----------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|
|Asset name                        |burstturret_emp-mod-up1|burstturret_emp-mod-up2|burstturret_emp-mod-up3|burstturret_emp-mod-up4|burstturret_emp-mod-up5|burstturret_emp-mod-up6|burstturret_emp-mod-up7|burstturret_emp-mod-up8|burstturret_emp-mod-up9|burstturret_emp-mod-up10|
|Buff asset offset                 |-0.6,3,-0.6            |-0.6,3,-0.6            |-0.6,3,-0.6            |-0.6,3,-0.6            |-1,3.6,-1              |-1.2,3.6,-1.2          |-1.2,4.2,-1.2          |-1.2,4.2,-1.2          |-1.2,4.2,-1.2          |-1.2,4.2,-1.2           |
|Bundle name                       |burstturret_emp-mod-up1|burstturret_emp-mod-up2|burstturret_emp-mod-up3|burstturret_emp-mod-up4|burstturret_emp-mod-up5|burstturret_emp-mod-up6|burstturret_emp-mod-up7|burstturret_emp-mod-up8|burstturret_emp-mod-up9|burstturret_emp-mod-up10|
|Icon camera position              |-22.7,27.44,26.09      |-22.49,27.21,25.84     |-23.53,28.41,27.14     |-28.02,33.36,32.28     |-28.3,33.68,32.61      |-28.03,33.38,32.27     |-28.36,33.75,32.71     |-27.71,33.03,31.93     |-27.3,32.57,31.45      |-27.3,32.57,31.45       |
|Prestige                          |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)             |
|Store tab                         |decorations            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)             |
|Turret displayed damage per second|550                    |825                    |990                    |1320                   |1594                   |1761                   |1926                   |2090                   |2255                   |2475                    |


|Level                             |11                      |
|----------------------------------|------------------------|
|Asset name                        |burstturret_emp-mod-up11|
|Buff asset offset                 |-1.2,4.2,-1.2           |
|Bundle name                       |burstturret_emp-mod-up11|
|Icon camera position              |-27.3,32.57,31.45       |
|Prestige                          |true                    |
|Store tab                         |(not found)             |
|Turret displayed damage per second|2485                    |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 23
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.9161676649999999089146740516298450529575347900390625

|Level |1 |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|------|--|---|---|---|---|---|---|---|----|----|
|Max XP|50|120|210|320|450|600|770|960|1170|1400|
|Xp    |25|30 |35 |40 |45 |50 |55 |60 |65  |70  |


|Level |11  |
|------|----|
|Max XP|1630|
|Xp    |75  |


