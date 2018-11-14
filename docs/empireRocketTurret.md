---
title: Rocket Turret (empireRocketTurret)
category: building
---

# Rocket Turret (empireRocketTurret)

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
|Building     |[Headquarters 11](empireHQ.html)|[Headquarters 10](empireHQ.html)|[Headquarters 9](empireHQ.html)|[Headquarters 8](empireHQ.html)|[Headquarters 7](empireHQ.html)|[Headquarters 6](empireHQ.html)|[Headquarters 5](empireHQ.html)|[Headquarters 4](empireHQ.html)|[Headquarters 4](empireHQ.html)|[Headquarters 4](empireHQ.html)|[Headquarters 4](empireHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Rocket Turret Empire


### Targeting

  * Turret max attack range: 10
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret flying vehicle (100)**, **Turret heavy vehicle (100)**, **Turret light vehicle (100)**, **Turret turret (100)**, Turret droideka (50), Turret flying infantry (50), Turret heavy infantry (50), Turret infantry (50), Turret support troop (50), Turret other building (25), Turret headquarters (1), Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret ressource generator (0), Turret storage (0), Turret wall (0)

|Level            |11|1-10|
|-----------------|--|----|
|Turret view range|11|10  |


### Shooting

  * Turret animation delay: 0s
  * Turret charge time: 1.750s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1,1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 1.050s
  * Turret shot count: 6
  * Turret shot delay: 175ms

|Level                 |11  |10  |9   |8   |7   |6  |5  |4  |3  |2  |1  |
|----------------------|----|----|----|----|----|---|---|---|---|---|---|
|Turret damage per shot|1451|1378|1256|1164|1072|980|888|735|551|459|306|


  * Turret attack splash damage percentages: 100

|Level                                     |11  |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |2260|2250|2050|1900|1750|1600|1450|1200|900 |750 |500 |
|Turret attack calculated damage per second|2763|2624|2392|2217|2041|1866|1691|1400|1049|874 |582 |
|Turret attack calculated damage per clip  |8706|8268|7536|6984|6432|5880|5328|4410|3306|2754|1836|


  * Turret attack cannons per sequence: 2
  * Turret attack cliptime: 3.150s
  * Turret attack directional: Yes
  * Turret attack is deflectable: No
  * Turret attack max speed: 12
  * Turret attack damage multipliers: **(200)**: Turret attack flying vehicle, Turret attack light vehicle, Turret attack vehicule hero, **(150)**: Turret attack heavy vehicle, Turret attack heavy vehicule hero, **(100)**: Turret attack droideka, Turret attack headquarters, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack trap, Turret attack turret, Turret attack wall, **(50)**: Turret attack flying infantry, Turret attack infantry, Turret attack infantry hero, Turret attack support troop, **(25)**: Turret attack heavy infantry, Turret attack heavy infantry hero
  * Turret attack pass through shield: No
  * Turret attack salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: rocket_turret
  * Turret projectile type: projectileRocketTurretEmpire

|Level    |11                    |10                    |9                    |8                    |7                    |6                    |5                    |4                    |3                    |2                    |1                    |
|---------|----------------------|----------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|
|Turret id|t_empireRocketTurret11|t_empireRocketTurret10|t_empireRocketTurret9|t_empireRocketTurret8|t_empireRocketTurret7|t_empireRocketTurret6|t_empireRocketTurret5|t_empireRocketTurret4|t_empireRocketTurret3|t_empireRocketTurret2|t_empireRocketTurret1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_rocket_1":20,"sfx_attack_rocket_2":20,"sfx_attack_rocket_3":20,"sfx_attack_rocket_4":20,"sfx_attack_rocket_5":20
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio impact: "sfx_explosion_impact_1":50,"sfx_explosion_impact_2":50
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Stash order: 70
  * Turret attack arcs: No
  * Turret attack bullet: fx_rocket_projectile_r_med
  * Turret attack hit spark: fx_rocket_hit_r_med
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_rocket_muzzle_r_med
  * Turret attack name: Rocket Turret Empire
  * Turret attack spin speed: 0
  * Turret favorite target type: lightVehicle
  * Turret max scale: 0

|Level                             |11                                                                                                                                                                   |10                                                                                                                                                                   |9                                                                                                                                                            |8                                                                                                                                                            |7                                                                                                                                                            |6                                                                                                                                                            |5                                                                                                                                                            |4                                                                                                                                                            |3                                                                                                                                                            |2                                                                                                                                                            |1                                                                                                                                                            |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Asset name                        |rocketturret_emp-mod-up11                                                                                                                                            |rocketturret_emp-mod-up10                                                                                                                                            |rocketturret_emp-mod-up9                                                                                                                                     |rocketturret_emp-mod-up8                                                                                                                                     |rocketturret_emp-mod-up7                                                                                                                                     |rocketturret_emp-mod-up6                                                                                                                                     |rocketturret_emp-mod-up5                                                                                                                                     |rocketturret_emp-mod-up4                                                                                                                                     |rocketturret_emp-mod-up3                                                                                                                                     |rocketturret_emp-mod-up2                                                                                                                                     |rocketturret_emp-mod-up1                                                                                                                                     |
|Buff asset offset                 |-1,3.4,-1                                                                                                                                                            |-1,3.4,-1                                                                                                                                                            |-1,3.4,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                    |-1,3.2,-1                                                                                                                                                    |-1,3.2,-1                                                                                                                                                    |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |
|Bundle name                       |rocketturret_emp-mod-up11                                                                                                                                            |rocketturret_emp-mod-up10                                                                                                                                            |rocketturret_emp-mod-up9                                                                                                                                     |rocketturret_emp-mod-up8                                                                                                                                     |rocketturret_emp-mod-up7                                                                                                                                     |rocketturret_emp-mod-up6                                                                                                                                     |rocketturret_emp-mod-up5                                                                                                                                     |rocketturret_emp-mod-up4                                                                                                                                     |rocketturret_emp-mod-up3                                                                                                                                     |rocketturret_emp-mod-up2                                                                                                                                     |rocketturret_emp-mod-up1                                                                                                                                     |
|Icon camera position              |-27.02,32.27,31.11                                                                                                                                                   |-27.02,32.27,31.11                                                                                                                                                   |-27.02,32.27,31.11                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |-23.91,25.41,24.96                                                                                                                                           |
|Icon lookat position              |0.41,2.03,-0.59                                                                                                                                                      |0.41,2.03,-0.59                                                                                                                                                      |0.41,2.03,-0.59                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |0.34,1.59,-0.27                                                                                                                                              |
|Prestige                          |true                                                                                                                                                                 |(not found)                                                                                                                                                          |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |
|Store tab                         |(not found)                                                                                                                                                          |(not found)                                                                                                                                                          |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |(not found)                                                                                                                                                  |decorations                                                                                                                                                  |
|Turret displayed damage per second|2260                                                                                                                                                                 |2250                                                                                                                                                                 |2050                                                                                                                                                         |1900                                                                                                                                                         |1750                                                                                                                                                         |1600                                                                                                                                                         |1450                                                                                                                                                         |1200                                                                                                                                                         |900                                                                                                                                                          |750                                                                                                                                                          |500                                                                                                                                                          |
|Turret gun position               |"rotateMesh_up11/tiltBarMesh_up11/aimMesh_up11/turretHeadMesh_up11/locator_gun1":1,"rotateMesh_up11/tiltBarMesh_up11/aimMesh_up11/turretHeadMesh_up11/locator_gun2":1|"rotateMesh_up10/tiltBarMesh_up10/aimMesh_up10/turretHeadMesh_up10/locator_gun1":1,"rotateMesh_up10/tiltBarMesh_up10/aimMesh_up10/turretHeadMesh_up10/locator_gun2":1|"rotateMesh_up9/tiltBarMesh_up9/aimMesh_up9/turretHeadMesh_up9/locator_gun1":1,"rotateMesh_up9/tiltBarMesh_up9/aimMesh_up9/turretHeadMesh_up9/locator_gun2":1|"rotateMesh_up8/tiltBarMesh_up8/aimMesh_up8/turretHeadMesh_up8/locator_gun1":1,"rotateMesh_up8/tiltBarMesh_up8/aimMesh_up8/turretHeadMesh_up8/locator_gun2":1|"rotateMesh_up7/tiltBarMesh_up7/aimMesh_up7/turretHeadMesh_up7/locator_gun1":1,"rotateMesh_up7/tiltBarMesh_up7/aimMesh_up7/turretHeadMesh_up7/locator_gun2":1|"rotateMesh_up6/tiltBarMesh_up6/aimMesh_up6/turretHeadMesh_up6/locator_gun1":1,"rotateMesh_up6/tiltBarMesh_up6/aimMesh_up6/turretHeadMesh_up6/locator_gun2":1|"rotateMesh_up5/tiltBarMesh_up5/aimMesh_up5/turretHeadMesh_up5/locator_gun1":1,"rotateMesh_up5/tiltBarMesh_up5/aimMesh_up5/turretHeadMesh_up5/locator_gun2":1|"rotateMesh_up4/tiltBarMesh_up4/aimMesh_up4/turretHeadMesh_up4/locator_gun1":1,"rotateMesh_up4/tiltBarMesh_up4/aimMesh_up4/turretHeadMesh_up4/locator_gun2":1|"rotateMesh_up3/tiltBarMesh_up3/aimMesh_up3/turretHeadMesh_up3/locator_gun1":1,"rotateMesh_up3/tiltBarMesh_up3/aimMesh_up3/turretHeadMesh_up3/locator_gun2":1|"rotateMesh_up2/tiltBarMesh_up2/aimMesh_up2/turretHeadMesh_up2/locator_gun1":1,"rotateMesh_up2/tiltBarMesh_up2/aimMesh_up2/turretHeadMesh_up2/locator_gun2":1|"rotateMesh_up1/tiltBarMesh_up1/aimMesh_up1/turretHeadMesh_up1/locator_gun1":1,"rotateMesh_up1/tiltBarMesh_up1/aimMesh_up1/turretHeadMesh_up1/locator_gun2":1|
|Turret tracker name               |rotateMesh_up11                                                                                                                                                      |rotateMesh_up10                                                                                                                                                      |rotateMesh_up9                                                                                                                                               |rotateMesh_up8                                                                                                                                               |rotateMesh_up7                                                                                                                                               |rotateMesh_up6                                                                                                                                               |rotateMesh_up5                                                                                                                                               |rotateMesh_up4                                                                                                                                               |rotateMesh_up3                                                                                                                                               |rotateMesh_up2                                                                                                                                               |rotateMesh_up1                                                                                                                                               |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 22
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.63265306100000007205608199001289904117584228515625

|Level |11  |10  |9   |8  |7  |6  |5  |4  |3  |2  |1 |
|------|----|----|----|---|---|---|---|---|---|---|--|
|Max XP|1630|1400|1170|960|770|600|450|320|210|120|50|
|Xp    |75  |70  |65  |60 |55 |50 |45 |40 |35 |30 |25|


