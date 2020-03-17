---
title: Rapid Fire Turret (empire_ab_RapidFireTurret)
category: building
---

# Rapid Fire Turret (empire_ab_RapidFireTurret)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: turret
  * Cross credits: 0
  * Side: Empire
  * Force reticle when targeted: No
  * Hide if locked: Yes
  * Produce: 0
  * Time: 1s
  * Type: turret

|Level          |10     |9      |8     |7     |6     |5     |4    |3    |2   |1   |
|---------------|-------|-------|------|------|------|------|-----|-----|----|----|
|Cross materials|3600000|2400000|900000|600000|480000|180000|90000|30000|6000|3000|
|Cross time     |10m    |9m     |8m    |7m    |6m    |5m    |4m   |3m   |2m  |1m  |
|Health         |27000  |24500  |22000 |19500 |17000 |14500 |12000|9000 |7500|5000|
|Max quantity   |20     |18     |16    |14    |12    |10    |8    |6    |4   |2   |


### Training stats

  * Training cost: 1 All.
  * Building: [Headquarters 10](smugglerHQ.html)

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

  * Turret animation delay: 0s
  * Turret charge time: 425ms
  * Turret clip retargeting: Yes
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 250ms
  * Turret shot count: 2
  * Turret shot delay: 500ms

|Level                       |10  |9   |8   |7   |6  |5  |4  |3  |2  |1  |
|----------------------------|----|----|----|----|---|---|---|---|---|---|
|Turret damage per shot      |1322|1204|1116|1028|940|852|705|529|441|294|
|Turret gun shooting sequence|1,2 |1,2 |1,2 |1,2 |1  |1  |1  |1  |1  |1  |


|Level                                     |10  |9   |8   |7   |6   |5   |4   |3   |2  |1  |
|------------------------------------------|----|----|----|----|----|----|----|----|---|---|
|Turret displayed damage per second        |2250|2050|1900|1750|1600|1450|1200|900 |750|500|
|Turret attack calculated damage per second|1855|1689|1566|1442|1319|1195|989 |742 |618|412|
|Turret attack calculated damage per clip  |2644|2408|2232|2056|1880|1704|1410|1058|882|588|


  * Turret attack cliptime: 1.425s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 20
  * Turret attack damage multipliers: **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 2

|Level                             |7-10|1-6|
|----------------------------------|----|---|
|Turret attack cannons per sequence|2   |1  |


## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: rapid_fire_turret
  * Turret projectile type: projectileEmpireRapidFireTurret

|Level    |10                           |9                           |8                           |7                           |6                           |5                           |4                           |3                           |2                           |1                           |
|---------|-----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|
|Turret id|t_empire_ab_RapidFireTurret10|t_empire_ab_RapidFireTurret9|t_empire_ab_RapidFireTurret8|t_empire_ab_RapidFireTurret7|t_empire_ab_RapidFireTurret6|t_empire_ab_RapidFireTurret5|t_empire_ab_RapidFireTurret4|t_empire_ab_RapidFireTurret3|t_empire_ab_RapidFireTurret2|t_empire_ab_RapidFireTurret1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Stash order: 50
  * Store tab: not_in_store
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_r_lrg
  * Turret attack hit spark: fx_blaster_hit_r_lrg
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_blaster_flash_r_lrg
  * Turret attack name: Empire Rapid Fire Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret max scale: 0

|Level                             |10                                                                                   |9                                                                                |8                                                                                |7                                                                                |6                                      |5                                      |4                                      |3                                      |2                                      |1                                      |
|----------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Asset name                        |standardturret_emp-mod-up8                                                           |standardturret_emp-mod-up8                                                       |standardturret_emp-mod-up8                                                       |standardturret_emp-mod-up7                                                       |standardturret_emp-mod-up6             |standardturret_emp-mod-up5             |standardturret_emp-mod-up4             |standardturret_emp-mod-up3             |standardturret_emp-mod-up2             |standardturret_emp-mod-up1             |
|Buff asset offset                 |-1.4,3.8,-1.4                                                                        |-1.4,3.8,-1.4                                                                    |-1.4,3.8,-1.4                                                                    |-1.4,3.6,-1.4                                                                    |-1.4,3.6,-1.4                          |-1.2,3.6,-1.2                          |-1,3.6,-1                              |-1,3,-1                                |-1,3,-1                                |-1,3,-1                                |
|Bundle name                       |standardturret_emp-mod-up8                                                           |standardturret_emp-mod-up8                                                       |standardturret_emp-mod-up8                                                       |standardturret_emp-mod-up7                                                       |standardturret_emp-mod-up6             |standardturret_emp-mod-up5             |standardturret_emp-mod-up4             |standardturret_emp-mod-up3             |standardturret_emp-mod-up2             |standardturret_emp-mod-up1             |
|Icon camera position              |-29.46,31.62,31.2                                                                    |-29.46,31.62,31.2                                                                |-29.46,31.62,31.2                                                                |-26.89,28.33,28.1                                                                |-26.89,28.33,28.1                      |-26.89,28.33,28.1                      |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |
|Icon lookat position              |0.72,1.97,-0.26                                                                      |0.72,1.97,-0.26                                                                  |0.72,1.97,-0.26                                                                  |0.34,1.59,-0.27                                                                  |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |0.34,1.59,-0.27                        |
|Turret displayed damage per second|2250                                                                                 |2050                                                                             |1900                                                                             |1750                                                                             |1600                                   |1450                                   |1200                                   |900                                    |750                                    |500                                    |
|Turret gun position               |"topMesh_up10/gunMesh_up10/locator_gun1":1,"topMesh_up10/gunMesh_up10/locator_gun2":1|"topMesh_up9/gunMesh_up9/locator_gun1":1,"topMesh_up9/gunMesh_up9/locator_gun2":1|"topMesh_up8/gunMesh_up8/locator_gun1":1,"topMesh_up8/gunMesh_up8/locator_gun2":1|"topMesh_up7/gunMesh_up7/locator_gun1":1,"topMesh_up7/gunMesh_up7/locator_gun2":1|"topMesh_up6/gunMesh_up6/locator_gun":1|"topMesh_up5/gunMesh_up5/locator_gun":1|"topMesh_up4/gunMesh_up4/locator_gun":1|"topMesh_up3/gunMesh_up3/locator_gun":1|"topMesh_up2/gunMesh_up2/locator_gun":1|"topMesh_up1/gunMesh_up1/locator_gun":1|
|Turret tracker name               |topMesh_up10                                                                         |topMesh_up9                                                                      |topMesh_up8                                                                      |topMesh_up7                                                                      |topMesh_up6                            |topMesh_up5                            |topMesh_up4                            |topMesh_up3                            |topMesh_up2                            |topMesh_up1                            |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 204
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.702127659999999931272895992151461541652679443359375

|Level |10  |9   |8  |7  |6  |5  |4  |3  |2  |1 |
|------|----|----|---|---|---|---|---|---|---|--|
|Max XP|1400|1170|960|770|600|450|320|210|120|50|
|Xp    |70  |65  |60 |55 |50 |45 |40 |35 |30 |25|


