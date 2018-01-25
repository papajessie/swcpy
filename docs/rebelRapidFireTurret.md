---
title: Rapid Fire Turret (rebelRapidFireTurret)
category: building
---

# Rapid Fire Turret (rebelRapidFireTurret) — version 1119

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
|Building     |[Headquarters 1](rebelHQ.html)|[Headquarters 2](rebelHQ.html)|[Headquarters 3](rebelHQ.html)|[Headquarters 4](rebelHQ.html)|[Headquarters 5](rebelHQ.html)|[Headquarters 6](rebelHQ.html)|[Headquarters 7](rebelHQ.html)|[Headquarters 8](rebelHQ.html)|[Headquarters 9](rebelHQ.html)|[Headquarters 10](rebelHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Rebel Standard Turret


### Targeting

  * Turret max attack range: 10
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret support troop (100)**, _Turret droideka (60)_, _Turret flying infantry (60)_, _Turret flying vehicle (60)_, _Turret headquarters (60)_, _Turret heavy infantry (60)_, _Turret heavy vehicle (60)_, _Turret infantry (60)_, _Turret light vehicle (60)_, _Turret other building (60)_, _Turret ressource generator (60)_, _Turret storage (60)_, _Turret turret (60)_, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

### Shooting

  * Turret animation delay: 0
  * Turret time between start of clip and first shot: 600ms
  * Turret clip retargeting: Yes
  * Turret gun shooting sequence: 1,2
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret time between end of clip and start of clip: 650ms
  * Turret shot count: 6
  * Turret time between shots: 250ms

|Level                 |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|----------------------|---|---|---|---|---|---|---|---|---|---|
|Turret damage per shot|104|156|188|250|302|354|406|458|510|563|


|Level                                     |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|---|---|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |500|750|900 |1200|1450|1600|1750|1900|2050|2250|
|Turret attack calculated damage per second|226|340|410 |545 |658 |772 |885 |999 |1112|1228|
|Turret attack calculated damage per clip  |624|936|1128|1500|1812|2124|2436|2748|3060|3378|


  * Turret attack cannons per sequence: 2
  * Turret attack cliptime: 2.750s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 20
  * Turret attack damage multipliers: **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 6

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: rapid_fire_turret
  * Turret projectile type: projectileRebelRapidFireTurret

|Level    |1                      |2                      |3                      |4                      |5                      |6                      |7                      |8                      |9                      |10                      |
|---------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------|
|Turret id|t_rebelRapidFireTurret1|t_rebelRapidFireTurret2|t_rebelRapidFireTurret3|t_rebelRapidFireTurret4|t_rebelRapidFireTurret5|t_rebelRapidFireTurret6|t_rebelRapidFireTurret7|t_rebelRapidFireTurret8|t_rebelRapidFireTurret9|t_rebelRapidFireTurret10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_rebel_rapidfireturret_1":35,"sfx_attack_rebel_rapidfireturret_2":35,"sfx_attack_rebel_rapidfireturret_3":30
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Stash order: 50
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_b_lrg
  * Turret attack hit spark: fx_blaster_hit_b_lrg
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_blaster_flash_b_lrg
  * Turret attack name: Rebel Standard Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret max scale: 0

|Level                             |1                                                        |2                                                        |3                                                        |4                                                        |5                                                        |6                                                        |7                                                        |8                                                        |9                                                        |10                                                         |
|----------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------|
|Asset name                        |standardturret_rbl-mod-up1                               |standardturret_rbl-mod-up2                               |standardturret_rbl-mod-up3                               |standardturret_rbl-mod-up4                               |standardturret_rbl-mod-up5                               |standardturret_rbl-mod-up6                               |standardturret_rbl-mod-up7                               |standardturret_rbl-mod-up8                               |standardturret_rbl-mod-up9                               |standardturret_rbl-mod-up10                                |
|Buff asset offset                 |-1,3,-1                                                  |-1,3,-1                                                  |-1,3,-1                                                  |-1.4,3.6,-1.4                                            |-1.4, 3.4, -2.8                                          |-2.8,3.4,-2.8                                            |-2.8,3.4,-2.8                                            |-1.4,4.2,-1.4                                            |-1.4,4.2,-1.4                                            |-1.4,4.2,-1.4                                              |
|Bundle name                       |standardturret_rbl-mod-up1                               |standardturret_rbl-mod-up2                               |standardturret_rbl-mod-up3                               |standardturret_rbl-mod-up4                               |standardturret_rbl-mod-up5                               |standardturret_rbl-mod-up6                               |standardturret_rbl-mod-up7                               |standardturret_rbl-mod-up8                               |standardturret_rbl-mod-up9                               |standardturret_rbl-mod-up10                                |
|Icon camera position              |-26.92,29.15,28.59                                       |-26.65,28.83,31.82                                       |-26.65,28.83,31.82                                       |-26.65,28.83,31.82                                       |-26.65,28.83,31.82                                       |-26.65,28.83,31.82                                       |-26.65,28.83,31.82                                       |-28.96,28.56,31.03                                       |-26.94,32.16,31.02                                       |-26.94,32.16,31.02                                         |
|Icon lookat position              |0.72,1.97,-0.26                                          |0.47,2.02,-0.41                                          |0.47,2.02,-0.41                                          |0.47,2.02,-0.41                                          |0.47,2.02,-0.41                                          |0.47,2.02,-0.41                                          |0.47,2.02,-0.41                                          |0.48,1.83,-0.44                                          |0.41,2.03,-0.59                                          |0.41,2.03,-0.59                                            |
|Store tab                         |decorations                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                              |(not found)                                                |
|Turret displayed damage per second|500                                                      |750                                                      |900                                                      |1200                                                     |1450                                                     |1600                                                     |1750                                                     |1900                                                     |2050                                                     |2250                                                       |
|Turret gun position               |"topMesh_up1/locator_gun1":1,"topMesh_up1/locator_gun2":2|"topMesh_up2/locator_gun1":1,"topMesh_up2/locator_gun2":2|"topMesh_up3/locator_gun1":1,"topMesh_up3/locator_gun2":2|"topMesh_up4/locator_gun1":1,"topMesh_up4/locator_gun2":2|"topMesh_up5/locator_gun1":1,"topMesh_up5/locator_gun2":2|"topMesh_up6/locator_gun1":1,"topMesh_up6/locator_gun2":2|"topMesh_up7/locator_gun1":1,"topMesh_up7/locator_gun2":2|"topMesh_up8/locator_gun1":1,"topMesh_up8/locator_gun2":2|"topMesh_up9/locator_gun1":1,"topMesh_up9/locator_gun2":2|"topMesh_up10/locator_gun1":1,"topMesh_up10/locator_gun2":2|
|Turret tracker name               |topMesh_up1                                              |topMesh_up2                                              |topMesh_up3                                              |topMesh_up4                                              |topMesh_up5                                              |topMesh_up6                                              |topMesh_up7                                              |topMesh_up8                                              |topMesh_up9                                              |topMesh_up10                                               |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 20
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 2.399999999999999911182158029987476766109466552734375

|Level |1 |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|------|--|---|---|---|---|---|---|---|----|----|
|Max XP|50|120|210|320|450|600|770|960|1170|1400|
|Xp    |25|30 |35 |40 |45 |50 |55 |60 |65  |70  |


