---
title: Burst Turret (rebelBurstTurret)
category: building
---

# Burst Turret (rebelBurstTurret) — version 1119

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: turret
  * Cross credits: 0
  * Side: Rebellion
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


### Training stats

|Level        |1                             |2                             |3                             |4                             |5                             |6                             |7                             |8                             |9                             |10                             |
|-------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|-------------------------------|
|Training cost|1500 All.                     |3000 All.                     |20000 All.                    |55000 All.                    |100000 All.                   |250000 All.                   |500000 All.                   |1000000 All.                  |3000000 All.                  |5000000 All.                   |
|Building     |[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 6](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Rebel Burst Turret


### Targeting

  * Turret max attack range: 9
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret droideka (60)**, **Turret flying infantry (60)**, **Turret flying vehicle (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

### Shooting

  * Turret animation delay: 0
  * Turret charge time: 1.750s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 1.050s
  * Turret shot count: 6
  * Turret shot delay: 175ms

|Level                 |1  |2  |3  |4  |5  |6   |7   |8   |9   |10  |
|----------------------|---|---|---|---|---|----|----|----|----|----|
|Turret damage per shot|337|505|606|809|977|1078|1179|1280|1381|1516|


|Level                                     |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |550 |825 |990 |1320|1594|1761|1926|2090|2255|2475|
|Turret attack calculated damage per second|525 |787 |944 |1260|1522|1680|1837|1994|2152|2362|
|Turret attack calculated damage per clip  |2022|3030|3636|4854|5862|6468|7074|7680|8286|9096|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 3.850s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 10
  * Turret attack damage multipliers: **(125)**: Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 6

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: burst_turret
  * Turret projectile type: projectileRebelBurstTurret

|Level    |1                  |2                  |3                  |4                  |5                  |6                  |7                  |8                  |9                  |10                  |
|---------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|--------------------|
|Turret id|t_rebelBurstTurret1|t_rebelBurstTurret2|t_rebelBurstTurret3|t_rebelBurstTurret4|t_rebelBurstTurret5|t_rebelBurstTurret6|t_rebelBurstTurret7|t_rebelBurstTurret8|t_rebelBurstTurret9|t_rebelBurstTurret10|


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
  * Turret attack bullet: fx_blaster_beam_b_sm
  * Turret attack hit spark: fx_blaster_hit_b_sm
  * Turret attack max scale: 125
  * Turret attack muzzle flash: fx_blaster_flash_b_sm
  * Turret attack name: Rebel Burst Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: lightVehicle
  * Turret gun position: "locator_gun":1
  * Turret max scale: 0
  * Turret tracker name: n/a

|Level                             |1                      |2                      |3                      |4                      |5                      |6                      |7                      |8                      |9                      |10                      |
|----------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|
|Asset name                        |burstturret_rbl-mod-up1|burstturret_rbl-mod-up2|burstturret_rbl-mod-up3|burstturret_rbl-mod-up4|burstturret_rbl-mod-up5|burstturret_rbl-mod-up6|burstturret_rbl-mod-up7|burstturret_rbl-mod-up8|burstturret_rbl-mod-up9|burstturret_rbl-mod-up10|
|Buff asset offset                 |-0.6,2.8,-0.6          |-0.6,2.8,-0.6          |-0.6,2.8,-0.6          |-1,3.4,-1              |-1.8, 2.6, -2.4        |-1.8,3,-2              |-1.8,3,-2              |-1.8,3,-2              |-1.8,3,-2              |-1.8,3,-2               |
|Bundle name                       |burstturret_rbl-mod-up1|burstturret_rbl-mod-up2|burstturret_rbl-mod-up3|burstturret_rbl-mod-up4|burstturret_rbl-mod-up5|burstturret_rbl-mod-up6|burstturret_rbl-mod-up7|burstturret_rbl-mod-up8|burstturret_rbl-mod-up9|burstturret_rbl-mod-up10|
|Icon camera position              |-22.19,26.89,25.49     |-23.6,28.48,27.16      |-22.38,27.17,25.79     |-23.55,28.45,27.14     |-25,30.02,28.81        |-24.56,29.53,28.3      |-25.26,30.3,29.09      |-25.75,30.87,29.66     |-25.48,30.51,29.34     |-25.48,30.51,29.34      |
|Store tab                         |decorations            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)            |(not found)             |
|Turret displayed damage per second|550                    |825                    |990                    |1320                   |1594                   |1761                   |1926                   |2090                   |2255                   |2475                    |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 23
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.6326530612244898321705477428622543811798095703125

|Level |1 |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|------|--|---|---|---|---|---|---|---|----|----|
|Max XP|50|120|210|320|450|600|770|960|1170|1400|
|Xp    |25|30 |35 |40 |45 |50 |55 |60 |65  |70  |


