---
title: bldtitledeathRocketTurret (deathRocketTurret)
category: building
---

# bldtitledeathRocketTurret (deathRocketTurret)

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

|Level          |10     |9      |8     |7     |6     |5     |4    |3    |2   |1   |
|---------------|-------|-------|------|------|------|------|-----|-----|----|----|
|Cross materials|3600000|2400000|900000|600000|480000|180000|90000|30000|6000|3000|
|Cross time     |10m    |9m     |8m    |7m    |6m    |5m    |4m   |3m   |2m  |1m  |
|Health         |27000  |24500  |22000 |19500 |17000 |14500 |12000|9000 |7500|5000|
|Max quantity   |20     |18     |16    |14    |12    |10    |8    |6    |4   |2   |
|Time           |1w3d   |1w1d   |6d    |4d    |2d12h |1d12h |16h  |4h   |30m |1m  |


### Training stats

  * Building: [Headquarters 10](smugglerHQ.html)

|Level        |10          |9           |8           |7          |6          |5          |4         |3         |2        |1        |
|-------------|------------|------------|------------|-----------|-----------|-----------|----------|----------|---------|---------|
|Training cost|5000000 All.|3000000 All.|1000000 All.|500000 All.|250000 All.|100000 All.|55000 All.|20000 All.|3000 All.|1500 All.|


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

  * Turret animation delay: 0s
  * Turret charge time: 1.750s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1,1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 1.050s
  * Turret shot count: 6
  * Turret shot delay: 175ms

|Level                 |10  |9   |8   |7   |6  |5  |4  |3  |2  |1  |
|----------------------|----|----|----|----|---|---|---|---|---|---|
|Turret damage per shot|1378|1256|1164|1072|980|888|735|551|459|306|


  * Turret attack splash damage percentages: 100

|Level                                     |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |2250|2050|1900|1750|1600|1450|1200|900 |750 |500 |
|Turret attack calculated damage per second|2624|2392|2217|2041|1866|1691|1400|1049|874 |582 |
|Turret attack calculated damage per clip  |8268|7536|6984|6432|5880|5328|4410|3306|2754|1836|


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

|Level    |10                        |9                        |8                        |7                        |6                        |5                        |4                        |3                        |2                        |1                        |
|---------|--------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
|Turret id|t_empire_ab_RocketTurret10|t_empire_ab_RocketTurret9|t_empire_ab_RocketTurret8|t_empire_ab_RocketTurret7|t_empire_ab_RocketTurret6|t_empire_ab_RocketTurret5|t_empire_ab_RocketTurret4|t_empire_ab_RocketTurret3|t_empire_ab_RocketTurret2|t_empire_ab_RocketTurret1|


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
  * Turret attack arcs: No
  * Turret attack bullet: fx_rocket_projectile_r_med
  * Turret attack hit spark: fx_rocket_hit_r_med
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_rocket_muzzle_r_med
  * Turret attack name: Rocket Turret Empire
  * Turret attack spin speed: 0
  * Turret favorite target type: lightVehicle
  * Turret max scale: 0

|Level                             |10                                                                                                                                                                   |9                                                                                                                                                            |8                                                                                                                                                            |7                                                                                                                                                            |6                                                                                                                                                            |5                                                                                                                                                            |4                                                                                                                                                            |3                                                                                                                                                            |2                                                                                                                                                            |1                                                                                                                                                            |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Asset name                        |rocketturret_dth-mod-up7                                                                                                                                             |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up6                                                                                                                                     |rocketturret_dth-mod-up5                                                                                                                                     |rocketturret_dth-mod-up4                                                                                                                                     |rocketturret_dth-mod-up3                                                                                                                                     |rocketturret_dth-mod-up2                                                                                                                                     |rocketturret_dth-mod-up1                                                                                                                                     |
|Buff asset offset                 |-1,3.4,-1                                                                                                                                                            |-1,3.4,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                    |-1,3.4,-1                                                                                                                                                    |-1,3.2,-1                                                                                                                                                    |-1,3.2,-1                                                                                                                                                    |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |-1,3,-1                                                                                                                                                      |
|Bundle name                       |rocketturret_dth-mod-up7                                                                                                                                             |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up7                                                                                                                                     |rocketturret_dth-mod-up6                                                                                                                                     |rocketturret_dth-mod-up5                                                                                                                                     |rocketturret_dth-mod-up4                                                                                                                                     |rocketturret_dth-mod-up3                                                                                                                                     |rocketturret_dth-mod-up2                                                                                                                                     |rocketturret_dth-mod-up1                                                                                                                                     |
|Turret displayed damage per second|2250                                                                                                                                                                 |2050                                                                                                                                                         |1900                                                                                                                                                         |1750                                                                                                                                                         |1600                                                                                                                                                         |1450                                                                                                                                                         |1200                                                                                                                                                         |900                                                                                                                                                          |750                                                                                                                                                          |500                                                                                                                                                          |
|Turret gun position               |"rotateMesh_up10/tiltBarMesh_up10/aimMesh_up10/turretHeadMesh_up10/locator_gun1":1,"rotateMesh_up10/tiltBarMesh_up10/aimMesh_up10/turretHeadMesh_up10/locator_gun2":1|"rotateMesh_up9/tiltBarMesh_up9/aimMesh_up9/turretHeadMesh_up9/locator_gun1":1,"rotateMesh_up9/tiltBarMesh_up9/aimMesh_up9/turretHeadMesh_up9/locator_gun2":1|"rotateMesh_up8/tiltBarMesh_up8/aimMesh_up8/turretHeadMesh_up8/locator_gun1":1,"rotateMesh_up8/tiltBarMesh_up8/aimMesh_up8/turretHeadMesh_up8/locator_gun2":1|"rotateMesh_up7/tiltBarMesh_up7/aimMesh_up7/turretHeadMesh_up7/locator_gun1":1,"rotateMesh_up7/tiltBarMesh_up7/aimMesh_up7/turretHeadMesh_up7/locator_gun2":1|"rotateMesh_up6/tiltBarMesh_up6/aimMesh_up6/turretHeadMesh_up6/locator_gun1":1,"rotateMesh_up6/tiltBarMesh_up6/aimMesh_up6/turretHeadMesh_up6/locator_gun2":1|"rotateMesh_up5/tiltBarMesh_up5/aimMesh_up5/turretHeadMesh_up5/locator_gun1":1,"rotateMesh_up5/tiltBarMesh_up5/aimMesh_up5/turretHeadMesh_up5/locator_gun2":1|"rotateMesh_up4/tiltBarMesh_up4/aimMesh_up4/turretHeadMesh_up4/locator_gun1":1,"rotateMesh_up4/tiltBarMesh_up4/aimMesh_up4/turretHeadMesh_up4/locator_gun2":1|"rotateMesh_up3/tiltBarMesh_up3/aimMesh_up3/turretHeadMesh_up3/locator_gun1":1,"rotateMesh_up3/tiltBarMesh_up3/aimMesh_up3/turretHeadMesh_up3/locator_gun2":1|"rotateMesh_up2/tiltBarMesh_up2/aimMesh_up2/turretHeadMesh_up2/locator_gun1":1,"rotateMesh_up2/tiltBarMesh_up2/aimMesh_up2/turretHeadMesh_up2/locator_gun2":1|"rotateMesh_up1/tiltBarMesh_up1/aimMesh_up1/turretHeadMesh_up1/locator_gun1":1,"rotateMesh_up1/tiltBarMesh_up1/aimMesh_up1/turretHeadMesh_up1/locator_gun2":1|
|Turret tracker name               |rotateMesh_up10                                                                                                                                                      |rotateMesh_up9                                                                                                                                               |rotateMesh_up8                                                                                                                                               |rotateMesh_up7                                                                                                                                               |rotateMesh_up6                                                                                                                                               |rotateMesh_up5                                                                                                                                               |rotateMesh_up4                                                                                                                                               |rotateMesh_up3                                                                                                                                               |rotateMesh_up2                                                                                                                                               |rotateMesh_up1                                                                                                                                               |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.63265306100000007205608199001289904117584228515625

|Level |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|------|---|---|---|---|---|---|---|---|---|---|
|Max XP|560|468|368|294|216|160|104|66 |32 |10 |
|Order |940|939|938|937|936|935|934|933|932|931|
|Xp    |28 |26 |23 |21 |18 |16 |13 |11 |8  |5  |


