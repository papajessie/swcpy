---
title: bldtitledeathRocketTurret (deathRocketTurret)
category: building
---

# bldtitledeathRocketTurret (deathRocketTurret) — version 1102

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Allow defensive spawn: Yes
  * Armor type: turret
  * Cross credits: 0
  * Side: Other units
  * Force reticle when targeted: No
  * Hide if locked: Yes
  * Produce: 0
  * Type: turret

|Level          |1   |2   |3    |4    |5     |6     |7     |8     |9      |10     |
|---------------|----|----|-----|-----|------|------|------|------|-------|-------|
|Cross materials|3000|6000|30000|90000|180000|480000|600000|900000|2400000|3600000|
|Cross time     |1m  |2m  |3m   |4m   |5m    |6m    |7m    |8m    |9m     |10m    |
|Health         |5000|7500|9000 |12000|14500 |17000 |19500 |22000 |24500  |27000  |
|Max quantity   |2   |4   |6    |8    |10    |12    |14    |16    |18     |20     |
|Time           |1m  |30m |4h   |16h  |1d12h |2d12h |4d    |6d    |1w1d   |1w3d   |


### Training stats

  * Building: [Headquarters 10](smugglerHQ.html)

|Level        |1        |2        |3         |4         |5          |6          |7          |8           |9           |10          |
|-------------|---------|---------|----------|----------|-----------|-----------|-----------|------------|------------|------------|
|Training cost|1500 All.|3000 All.|20000 All.|55000 All.|100000 All.|250000 All.|500000 All.|1000000 All.|3000000 All.|5000000 All.|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Rocket Turret Empire


### Targeting

  * Turret max attack range: 9
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret flying vehicle (100)**, **Turret heavy vehicle (100)**, **Turret light vehicle (100)**, **Turret turret (100)**, Turret droideka (50), Turret flying infantry (50), Turret heavy infantry (50), Turret infantry (50), Turret support troop (50), Turret other building (25), Turret headquarters (1), Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret ressource generator (0), Turret storage (0), Turret wall (0)
  * Turret view range: 10

### Shooting

  * Turret time between start of clip and first shot: 1.750s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1,1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret time between end of clip and start of clip: 1.050s
  * Turret shot count: 6
  * Turret time between shots: 175ms

|Level                 |1  |2  |3  |4  |5  |6  |7   |8   |9   |10  |
|----------------------|---|---|---|---|---|---|----|----|----|----|
|Turret damage per shot|306|459|551|735|888|980|1072|1164|1256|1378|


  * Turret attack splash damage percentages: 100

|Level                                     |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |500 |750 |900 |1200|1450|1600|1750|1900|2050|2250|
|Turret attack calculated damage per second|582 |874 |1049|1400|1691|1866|2041|2217|2392|2624|
|Turret attack calculated damage per clip  |1836|2754|3306|4410|5328|5880|6432|6984|7536|8268|


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

|Level    |1                        |2                        |3                        |4                        |5                        |6                        |7                        |8                        |9                        |10                        |
|---------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|--------------------------|
|Turret id|t_empire_ab_RocketTurret1|t_empire_ab_RocketTurret2|t_empire_ab_RocketTurret3|t_empire_ab_RocketTurret4|t_empire_ab_RocketTurret5|t_empire_ab_RocketTurret6|t_empire_ab_RocketTurret7|t_empire_ab_RocketTurret8|t_empire_ab_RocketTurret9|t_empire_ab_RocketTurret10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_rocket_1":20,"sfx_attack_rocket_2":20,"sfx_attack_rocket_3":20,"sfx_attack_rocket_4":20,"sfx_attack_rocket_5":20
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Icon camera position: -23.91,25.41,24.96
  * Icon lookat position: 0.34,1.59,-0.27
  * Stash order: 1000
  * Store tab: not_in_store
  * Turret animation delay: 0
  * Turret attack arcs: No
  * Turret attack bullet: fx_rocket_projectile_r_med
  * Turret attack hit spark: fx_rocket_hit_r_med
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_rocket_muzzle_r_med
  * Turret attack name: Rocket Turret Empire
  * Turret attack spin speed: 0
  * Turret favorite target type: lightVehicle
  * Turret max scale: 0

|Level                             |1                                                                                                                                                            |2                                                                                                                                                            |3                                                                                                                                                            |4                                                                                                                                                            |5                                                                                                                                                            |6                                                                                                                                                            |7                                                                                                                                                            |8                                                                                                                                                            |9                                                                                                                                                            |10                                                                                                                                                                   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Asset name                        |rocketturret_dth-mod-up1                                                                                                                                     |rocketturret_dth-mod-up2                                                                                                                                     |rocketturret_dth-mod-up3                                                                                                                                     |rocketturret_dth-mod-up4                                                                                                                                     |rocketturret_dth-mod-up5                                                                                                                                     |rocketturret_dth-mod-up6                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                             |
|Buff asset offset                 |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |-1,3.2,-1                                                                                                                                                    |-1,3.2,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                            |
|Bundle name                       |rocketturret_dth-mod-up1                                                                                                                                     |rocketturret_dth-mod-up2                                                                                                                                     |rocketturret_dth-mod-up3                                                                                                                                     |rocketturret_dth-mod-up4                                                                                                                                     |rocketturret_dth-mod-up5                                                                                                                                     |rocketturret_dth-mod-up6                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                             |
|Turret displayed damage per second|500                                                                                                                                                          |750                                                                                                                                                          |900                                                                                                                                                          |1200                                                                                                                                                         |1450                                                                                                                                                         |1600                                                                                                                                                         |1750                                                                                                                                                         |1900                                                                                                                                                         |2050                                                                                                                                                         |2250                                                                                                                                                                 |
|Turret gun position               |"rotateMesh_up1/tiltBarMesh_up1/aimMesh_up1/turretHeadMesh_up1/locator_gun1":1,"rotateMesh_up1/tiltBarMesh_up1/aimMesh_up1/turretHeadMesh_up1/locator_gun2":1|"rotateMesh_up2/tiltBarMesh_up2/aimMesh_up2/turretHeadMesh_up2/locator_gun1":1,"rotateMesh_up2/tiltBarMesh_up2/aimMesh_up2/turretHeadMesh_up2/locator_gun2":1|"rotateMesh_up3/tiltBarMesh_up3/aimMesh_up3/turretHeadMesh_up3/locator_gun1":1,"rotateMesh_up3/tiltBarMesh_up3/aimMesh_up3/turretHeadMesh_up3/locator_gun2":1|"rotateMesh_up4/tiltBarMesh_up4/aimMesh_up4/turretHeadMesh_up4/locator_gun1":1,"rotateMesh_up4/tiltBarMesh_up4/aimMesh_up4/turretHeadMesh_up4/locator_gun2":1|"rotateMesh_up5/tiltBarMesh_up5/aimMesh_up5/turretHeadMesh_up5/locator_gun1":1,"rotateMesh_up5/tiltBarMesh_up5/aimMesh_up5/turretHeadMesh_up5/locator_gun2":1|"rotateMesh_up6/tiltBarMesh_up6/aimMesh_up6/turretHeadMesh_up6/locator_gun1":1,"rotateMesh_up6/tiltBarMesh_up6/aimMesh_up6/turretHeadMesh_up6/locator_gun2":1|"rotateMesh_up7/tiltBarMesh_up7/aimMesh_up7/turretHeadMesh_up7/locator_gun1":1,"rotateMesh_up7/tiltBarMesh_up7/aimMesh_up7/turretHeadMesh_up7/locator_gun2":1|"rotateMesh_up8/tiltBarMesh_up8/aimMesh_up8/turretHeadMesh_up8/locator_gun1":1,"rotateMesh_up8/tiltBarMesh_up8/aimMesh_up8/turretHeadMesh_up8/locator_gun2":1|"rotateMesh_up9/tiltBarMesh_up9/aimMesh_up9/turretHeadMesh_up9/locator_gun1":1,"rotateMesh_up9/tiltBarMesh_up9/aimMesh_up9/turretHeadMesh_up9/locator_gun2":1|"rotateMesh_up10/tiltBarMesh_up10/aimMesh_up10/turretHeadMesh_up10/locator_gun1":1,"rotateMesh_up10/tiltBarMesh_up10/aimMesh_up10/turretHeadMesh_up10/locator_gun2":1|
|Turret tracker name               |rotateMesh_up1                                                                                                                                               |rotateMesh_up2                                                                                                                                               |rotateMesh_up3                                                                                                                                               |rotateMesh_up4                                                                                                                                               |rotateMesh_up5                                                                                                                                               |rotateMesh_up6                                                                                                                                               |rotateMesh_up7                                                                                                                                               |rotateMesh_up8                                                                                                                                               |rotateMesh_up9                                                                                                                                               |rotateMesh_up10                                                                                                                                                      |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.6326530612244898321705477428622543811798095703125

|Level |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|------|---|---|---|---|---|---|---|---|---|---|
|Max XP|10 |32 |66 |104|160|216|294|368|468|560|
|Order |931|932|933|934|935|936|937|938|939|940|
|Xp    |5  |8  |11 |13 |16 |18 |21 |23 |26 |28 |


