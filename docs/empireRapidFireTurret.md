---
title: Rapid Fire Turret (empireRapidFireTurret)
category: building
---

# Rapid Fire Turret (empireRapidFireTurret)

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
|Health         |5000|7500|9000 |12000|14500|16000|19500|22000 |24500 |27000 |
|Max quantity   |2   |4   |6    |8    |10   |12   |14   |16    |18    |20    |
|Time           |1m  |30m |4h   |16h  |1d12h|2d12h|4d   |6d    |1w1d  |1w3d  |


### Training stats

|Level        |1                              |2                              |3                              |4                              |5                              |6                              |7                              |8                              |9                              |10                              |
|-------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|--------------------------------|
|Training cost|1500 All.                      |3000 All.                      |20000 All.                     |55000 All.                     |100000 All.                    |250000 All.                    |500000 All.                    |1000000 All.                   |3000000 All.                   |5000000 All.                    |
|Building     |[Headquarters 1](empireHQ.html)|[Headquarters 2](empireHQ.html)|[Headquarters 3](empireHQ.html)|[Headquarters 4](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 10](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Empire Rapid Fire Turret


### Targeting

  * Turret max attack range: 10
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret support troop (100)**, _Turret droideka (60)_, _Turret flying infantry (60)_, _Turret flying vehicle (60)_, _Turret headquarters (60)_, _Turret heavy infantry (60)_, _Turret heavy vehicle (60)_, _Turret infantry (60)_, _Turret light vehicle (60)_, _Turret other building (60)_, _Turret ressource generator (60)_, _Turret storage (60)_, _Turret turret (60)_, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

### Shooting

  * Turret time between start of clip and first shot: 425ms
  * Turret clip retargeting: Yes
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret time between end of clip and start of clip: 250ms
  * Turret shot count: 2
  * Turret time between shots: 500ms

|Level                       |1  |2  |3  |4  |5  |6  |7   |8   |9   |10  |
|----------------------------|---|---|---|---|---|---|----|----|----|----|
|Turret damage per shot      |294|441|529|705|852|999|1146|1293|1439|1586|
|Turret gun shooting sequence|1  |1  |1  |1  |1  |1  |1,2 |1,2 |1,2 |1,2 |


|Level                                     |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|---|---|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |500|750|900 |1200|1450|1600|1750|1900|2050|2250|
|Turret attack calculated damage per second|500|750|900 |1200|1450|1700|1950|2200|2449|2699|
|Turret attack calculated damage per clip  |588|882|1058|1410|1704|1998|2292|2586|2878|3172|


  * Turret attack cliptime: 1.175s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 20
  * Turret attack damage multipliers: **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 2

|Level                             |1-6|7-10|
|----------------------------------|---|----|
|Turret attack cannons per sequence|1  |2   |


## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: rapid_fire_turret
  * Turret projectile type: projectileEmpireRapidFireTurret

|Level    |1                       |2                       |3                       |4                       |5                       |6                       |7                       |8                       |9                       |10                       |
|---------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|-------------------------|
|Turret id|t_empireRapidFireTurret1|t_empireRapidFireTurret2|t_empireRapidFireTurret3|t_empireRapidFireTurret4|t_empireRapidFireTurret5|t_empireRapidFireTurret6|t_empireRapidFireTurret7|t_empireRapidFireTurret8|t_empireRapidFireTurret9|t_empireRapidFireTurret10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Stash order: 50
  * Turret animation delay: 0
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_r_lrg
  * Turret attack hit spark: fx_blaster_hit_r_lrg
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_blaster_flash_r_lrg
  * Turret attack name: Empire Rapid Fire Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret max scale: 0

|Level                             |1                                      |2                                      |3                                      |4                                      |5                                      |6                                      |7                                                                                |8                                                                                |9                                                                                |10                                                                                   |
|----------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|Asset name                        |standardturret_emp-mod-up1             |standardturret_emp-mod-up2             |standardturret_emp-mod-up3             |standardturret_emp-mod-up4             |standardturret_emp-mod-up5             |standardturret_emp-mod-up6             |standardturret_emp-mod-up7                                                       |standardturret_emp-mod-up8                                                       |standardturret_emp-mod-up9                                                       |standardturret_emp-mod-up10                                                          |
|Buff asset offset                 |-1,3,-1                                |-1,3,-1                                |-1,3,-1                                |-1,3.6,-1                              |-1.2,3.6,-1.2                          |-1.4,3.6,-1.4                          |-1.4,3.6,-1.4                                                                    |-1.4,3.8,-1.4                                                                    |-1.4,3.8,-1.4                                                                    |-1.4,3.8,-1.4                                                                        |
|Bundle name                       |standardturret_emp-mod-up1             |standardturret_emp-mod-up2             |standardturret_emp-mod-up3             |standardturret_emp-mod-up4             |standardturret_emp-mod-up5             |standardturret_emp-mod-up6             |standardturret_emp-mod-up7                                                       |standardturret_emp-mod-up8                                                       |standardturret_emp-mod-up9                                                       |standardturret_emp-mod-up10                                                          |
|Icon camera position              |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-26.89,28.33,28.1                      |-26.89,28.33,28.1                      |-26.89,28.33,28.1                                                                |-29.46,31.62,31.2                                                                |-26.05,31.22,30.03                                                               |-26.05,31.22,30.03                                                                   |
|Icon lookat position              |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                                                                  |0.72,1.97,-0.26                                                                  |0.41,2.03,-0.59                                                                  |0.41,2.03,-0.59                                                                      |
|Store tab                         |decorations                            |(not found)                            |(not found)                            |(not found)                            |(not found)                            |(not found)                            |(not found)                                                                      |(not found)                                                                      |(not found)                                                                      |(not found)                                                                          |
|Turret displayed damage per second|500                                    |750                                    |900                                    |1200                                   |1450                                   |1600                                   |1750                                                                             |1900                                                                             |2050                                                                             |2250                                                                                 |
|Turret gun position               |"topMesh_up1/gunMesh_up1/locator_gun":1|"topMesh_up2/gunMesh_up2/locator_gun":1|"topMesh_up3/gunMesh_up3/locator_gun":1|"topMesh_up4/gunMesh_up4/locator_gun":1|"topMesh_up5/gunMesh_up5/locator_gun":1|"topMesh_up6/gunMesh_up6/locator_gun":1|"topMesh_up7/gunMesh_up7/locator_gun1":1,"topMesh_up7/gunMesh_up7/locator_gun2":1|"topMesh_up8/gunMesh_up8/locator_gun1":1,"topMesh_up8/gunMesh_up8/locator_gun2":1|"topMesh_up9/gunMesh_up9/locator_gun1":1,"topMesh_up9/gunMesh_up9/locator_gun2":1|"topMesh_up10/gunMesh_up10/locator_gun1":1,"topMesh_up10/gunMesh_up10/locator_gun2":1|
|Turret tracker name               |topMesh_up1                            |topMesh_up2                            |topMesh_up3                            |topMesh_up4                            |topMesh_up5                            |topMesh_up6                            |topMesh_up7                                                                      |topMesh_up8                                                                      |topMesh_up9                                                                      |topMesh_up10                                                                         |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 20
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.7021276595744680992794428675551898777484893798828125

|Level |1 |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|------|--|---|---|---|---|---|---|---|----|----|
|Max XP|50|120|210|320|450|600|770|960|1170|1400|
|Xp    |25|30 |35 |40 |45 |50 |55 |60 |65  |70  |


