---
title: Mortar Turret (empireMortar)
category: building
---

# Mortar Turret (empireMortar)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: turret
  * Cross credits: 0
  * Cross time: 10s
  * Side: Empire
  * Force reticle when targeted: No
  * Hide if locked: No
  * Produce: 0
  * Time: 10s
  * Type: turret

|Level          |11    |10    |9     |8     |7    |6    |5    |4    |3   |2   |1   |
|---------------|------|------|------|------|-----|-----|-----|-----|----|----|----|
|Cross materials|702000|540000|360000|135000|90000|72000|27000|13500|4500|900 |450 |
|Health         |28500 |27000 |24500 |22000 |17500|16000|14500|12000|9000|7500|5000|
|Max quantity   |22    |20    |18    |16    |14   |12   |10   |8    |6   |4   |2   |


### Training stats

  * Training cost: 1 All.

|Level   |11                              |10                              |9                              |8                              |7                              |6                              |5                              |4                              |1-3                            |
|--------|--------------------------------|--------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
|Building|[Headquarters 11](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 4](empireHQ.html)|[Headquarters 3](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Empire Mortar Turret


### Targeting

  * Turret max attack range: 11
  * Turret min attack range: 4
  * Turret target preference strength: 90
  * Turret target preferences: **Turret droideka (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1), Turret flying infantry (0), Turret flying vehicle (0)

|Level            |11|1-10|
|-----------------|--|----|
|Turret view range|11|10  |


### Shooting

  * Turret animation delay: 0s
  * Turret charge time: 1.650s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 1s
  * Turret can shoot over walls: Yes
  * Turret reload time: 1.500s
  * Turret shot count: 1
  * Turret shot delay: 1ms

|Level                 |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------|----|----|----|----|----|----|----|----|----|----|----|
|Turret damage per shot|5208|5198|4736|4389|4043|3696|3350|2772|2079|1733|1155|


  * Turret attack splash damage percentages: 100,30,20,10,10

|Level                                     |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |1585|1575|1435|1330|1225|1120|1015|840 |630 |525 |350 |
|Turret attack calculated damage per second|1653|1650|1503|1393|1283|1173|1063|880 |660 |550 |366 |
|Turret attack calculated damage per clip  |5208|5198|4736|4389|4043|3696|3350|2772|2079|1733|1155|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 3.150s
  * Turret attack directional: No
  * Turret attack is deflectable: No
  * Turret attack max speed: 4
  * Turret attack damage multipliers: **(100)**: Turret attack droideka, Turret attack headquarters, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack wall, **(80)**: Turret attack infantry, Turret attack infantry hero, **(60)**: Turret attack heavy infantry, Turret attack heavy infantry hero, **(50)**: Turret attack light vehicle, Turret attack vehicule hero, **(25)**: Turret attack heavy vehicle, Turret attack heavy vehicule hero, **(0)**: Turret attack flying infantry, Turret attack flying vehicle
  * Turret attack pass through shield: No
  * Turret attack salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: mortar_turret
  * Turret projectile type: projectileEmpireMortar

|Level    |11              |10              |9              |8              |7              |6              |5              |4              |3              |2              |1              |
|---------|----------------|----------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
|Turret id|t_empireMortar11|t_empireMortar10|t_empireMortar9|t_empireMortar8|t_empireMortar7|t_empireMortar6|t_empireMortar5|t_empireMortar4|t_empireMortar3|t_empireMortar2|t_empireMortar1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_mortarlaunch_1":50,"sfx_attack_mortarlaunch_2":50
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio impact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Stash order: 80
  * Turret attack S transition: 100
  * Turret attack arcs: Yes
  * Turret attack bullet: fx_mortar_projectile_r_sm
  * Turret attack hit spark: fx_mortar_hit_r_sm
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_mortar_muzzle_r_sm
  * Turret attack name: Empire Mortar Turret
  * Turret attack spin speed: 2
  * Turret favorite target type: infantry
  * Turret gun position: "locator_gun":1
  * Turret max scale: 2

|Level                             |11                                 |10                                 |9                                |8                                |7                                |6                                |5                                |4                                |3                                |2                                |1                                |
|----------------------------------|-----------------------------------|-----------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
|Asset name                        |mortarturret_emp-mod-up11          |mortarturret_emp-mod-up10          |mortarturret_emp-mod-up9         |mortarturret_emp-mod-up8         |mortarturret_emp-mod-up7         |mortarturret_emp-mod-up6         |mortarturret_emp-mod-up5         |mortarturret_emp-mod-up4         |mortarturret_emp-mod-up3         |mortarturret_emp-mod-up2         |mortarturret_emp-mod-up1         |
|Buff asset offset                 |-1.2,2,-1.2                        |-1.2,2,-1.2                        |-1.2,2,-1.2                      |-1.2,2,-1.2                      |-1.2,2,-1.2                      |-1.4,1.6,-1.4                    |-1.6,1.6,-1.6                    |-1,3,-1                          |-1,3,-1                          |-1,3,-1                          |-1,3,-1                          |
|Bundle name                       |mortarturret_emp-mod-up11          |mortarturret_emp-mod-up10          |mortarturret_emp-mod-up9         |mortarturret_emp-mod-up8         |mortarturret_emp-mod-up7         |mortarturret_emp-mod-up6         |mortarturret_emp-mod-up5         |mortarturret_emp-mod-up4         |mortarturret_emp-mod-up3         |mortarturret_emp-mod-up2         |mortarturret_emp-mod-up1         |
|Icon camera position              |-25.64,30.71,29.55                 |-25.64,30.71,29.55                 |-25.64,30.71,29.55               |-23.91,25.41,24.96               |-23.91,25.41,24.96               |-23.91,25.41,24.96               |-23.91,25.41,24.96               |-23.91,25.41,24.96               |-23.91,25.41,24.96               |-23.91,25.41,24.96               |-23.91,25.41,24.96               |
|Icon lookat position              |0.41,2.03,-0.59                    |0.41,2.03,-0.59                    |0.41,2.03,-0.59                  |0.34,1.59,-0.27                  |0.34,1.59,-0.27                  |0.34,1.59,-0.27                  |0.34,1.59,-0.27                  |0.34,1.59,-0.27                  |0.34,1.59,-0.27                  |0.34,1.59,-0.27                  |0.34,1.59,-0.27                  |
|Prestige                          |true                               |(not found)                        |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |
|Store tab                         |(not found)                        |(not found)                        |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |(not found)                      |decorations                      |
|Turret displayed damage per second|1585                               |1575                               |1435                             |1330                             |1225                             |1120                             |1015                             |840                              |630                              |525                              |350                              |
|Turret tracker name               |mortarMesh_up11/barrelbaseMesh_up11|mortarMesh_up10/barrelbaseMesh_up10|mortarMesh_up9/barrelbaseMesh_up9|mortarMesh_up8/barrelbaseMesh_up8|mortarMesh_up7/barrelbaseMesh_up7|mortarMesh_up6/barrelbaseMesh_up6|mortarMesh_up5/barrelbaseMesh_up5|mortarMesh_up4/barrelbaseMesh_up4|mortarMesh_up3/barrelbaseMesh_up3|mortarMesh_up2/barrelbaseMesh_up2|mortarMesh_up1/barrelbaseMesh_up1|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 21
  * Turret arming delay: 0
  * Turret attack S1 time: 300ms
  * Turret attack S2 time: 300ms
  * Turret attack seeks target: No
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 0.333333333299999978738270556277711875736713409423828125

|Level |11  |10  |9   |8  |7  |6  |5  |4  |3  |2  |1 |
|------|----|----|----|---|---|---|---|---|---|---|--|
|Max XP|1630|1400|1170|960|770|600|450|320|210|120|50|
|Xp    |75  |70  |65  |60 |55 |50 |45 |40 |35 |30 |25|


