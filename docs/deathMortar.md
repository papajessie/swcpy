---
title: bldtitledeathMortar (deathMortar)
category: building
---

# bldtitledeathMortar (deathMortar)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

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

## Turret attack : Empire Mortar Turret


### Targeting

  * Turret max attack range: 11
  * Turret min attack range: 4
  * Turret target preference strength: 90
  * Turret target preferences: **Turret droideka (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1), Turret flying infantry (0), Turret flying vehicle (0)
  * Turret view range: 10

### Shooting

  * Turret animation delay: 0s
  * Turret charge time: 1.500s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 1s
  * Turret can shoot over walls: Yes
  * Turret reload time: 1.500s
  * Turret shot count: 1
  * Turret shot delay: 1ms

|Level                 |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|----------------------|----|----|----|----|----|----|----|----|----|----|
|Turret damage per shot|4725|4305|3990|3675|3360|3045|2520|1890|1575|1050|


  * Turret attack splash damage percentages: 100,30,20,10,10

|Level                                     |10  |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |1575|1435|1330|1225|1120|1015|840 |630 |525 |350 |
|Turret attack calculated damage per second|1575|1435|1330|1225|1120|1015|840 |630 |525 |350 |
|Turret attack calculated damage per clip  |4725|4305|3990|3675|3360|3045|2520|1890|1575|1050|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 3s
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

|Level    |10                  |9                  |8                  |7                  |6                  |5                  |4                  |3                  |2                  |1                  |
|---------|--------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|Turret id|t_empire_ab_Mortar10|t_empire_ab_Mortar9|t_empire_ab_Mortar8|t_empire_ab_Mortar7|t_empire_ab_Mortar6|t_empire_ab_Mortar5|t_empire_ab_Mortar4|t_empire_ab_Mortar3|t_empire_ab_Mortar2|t_empire_ab_Mortar1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_mortarlaunch_1":50,"sfx_attack_mortarlaunch_2":50
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Icon camera position: -33.43,25.45,32.56
  * Icon lookat position: 0.43,2.06,-0.38
  * Stash order: 1000
  * Store tab: not_in_store
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

|Level                             |10                                |9                                |8                                |7                                |6                                |5                                |4                                |3                                |2                                |1                                |
|----------------------------------|----------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
|Asset name                        |mortarturret_dth-mod-up7          |mortarturret_dth-mod-up7         |mortarturret_dth-mod-up7         |mortarturret_dth-mod-up7         |mortarturret_dth-mod-up6         |mortarturret_dth-mod-up5         |mortarturret_dth-mod-up4         |mortarturret_dth-mod-up3         |mortarturret_dth-mod-up2         |mortarturret_dth-mod-up1         |
|Buff asset offset                 |-1.2,2,-1.2                       |-1.2,2,-1.2                      |-1.2,2,-1.2                      |-1.2,2,-1.2                      |-1.4,1.6,-1.4                    |-1.6,1.6,-1.6                    |-1,3,-1                          |-1,3,-1                          |-1,3,-1                          |-1,3,-1                          |
|Bundle name                       |mortarturret_dth-mod-up7          |mortarturret_dth-mod-up7         |mortarturret_dth-mod-up7         |mortarturret_dth-mod-up7         |mortarturret_dth-mod-up6         |mortarturret_dth-mod-up5         |mortarturret_dth-mod-up4         |mortarturret_dth-mod-up3         |mortarturret_dth-mod-up2         |mortarturret_dth-mod-up1         |
|Turret displayed damage per second|1575                              |1435                             |1330                             |1225                             |1120                             |1015                             |840                              |630                              |525                              |350                              |
|Turret tracker name               |mortarMesh_up9/barrelbaseMesh_up10|mortarMesh_up9/barrelbaseMesh_up9|mortarMesh_up8/barrelbaseMesh_up8|mortarMesh_up7/barrelbaseMesh_up7|mortarMesh_up6/barrelbaseMesh_up6|mortarMesh_up5/barrelbaseMesh_up5|mortarMesh_up4/barrelbaseMesh_up4|mortarMesh_up3/barrelbaseMesh_up3|mortarMesh_up2/barrelbaseMesh_up2|mortarMesh_up1/barrelbaseMesh_up1|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack S1 time: 300ms
  * Turret attack S2 time: 300ms
  * Turret attack seeks target: No
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 0.333333333299999978738270556277711875736713409423828125

|Level |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|------|---|---|---|---|---|---|---|---|---|---|
|Max XP|560|468|368|294|216|160|104|66 |32 |10 |
|Order |950|949|948|947|946|945|944|943|942|941|
|Xp    |28 |26 |23 |21 |18 |16 |13 |11 |8  |5  |


