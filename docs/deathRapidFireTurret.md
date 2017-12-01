---
title: bldtitledeathRapidFireTurret (deathRapidFireTurret)
category: building
---

# bldtitledeathRapidFireTurret (deathRapidFireTurret) — version 1102

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
|Turret damage per shot      |294|441|529|705|852|940|1028|1116|1204|1322|
|Turret gun shooting sequence|1  |1  |1  |1  |1  |1  |1,2 |1,2 |1,2 |1,2 |


|Level                                     |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|---|---|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |500|750|900 |1200|1450|1600|1750|1900|2050|2250|
|Turret attack calculated damage per second|500|750|900 |1200|1450|1600|1749|1899|2049|2250|
|Turret attack calculated damage per clip  |588|882|1058|1410|1704|1880|2056|2232|2408|2644|


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

|Level    |1                           |2                           |3                           |4                           |5                           |6                           |7                           |8                           |9                           |10                           |
|---------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|----------------------------|-----------------------------|
|Turret id|t_empire_ab_RapidFireTurret1|t_empire_ab_RapidFireTurret2|t_empire_ab_RapidFireTurret3|t_empire_ab_RapidFireTurret4|t_empire_ab_RapidFireTurret5|t_empire_ab_RapidFireTurret6|t_empire_ab_RapidFireTurret7|t_empire_ab_RapidFireTurret8|t_empire_ab_RapidFireTurret9|t_empire_ab_RapidFireTurret10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_blastercannon_1":25,"sfx_attack_blastercannon_2":25,"sfx_attack_blastercannon_3":25,"sfx_attack_blastercannon_4":25
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Icon lookat position: 0.34,1.59,-0.27
  * Stash order: 1000
  * Store tab: not_in_store
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
|Asset name                        |standardturret_dth-mod-up1             |standardturret_dth-mod-up2             |standardturret_dth-mod-up3             |standardturret_dth-mod-up4             |standardturret_dth-mod-up5             |standardturret_dth-mod-up6             |standardturret_dth-mod-up7                                                       |standardturret_dth-mod-up7                                                       |standardturret_dth-mod-up7                                                       |standardturret_dth-mod-up7                                                           |
|Buff asset offset                 |-1,3,-1                                |-1,3,-1                                |-1,3,-1                                |-1,3.6,-1                              |-1.2,3.6,-1.2                          |-1.4,3.6,-1.4                          |-1.4,3.6,-1.4                                                                    |-1.4,3.6,-1.4                                                                    |-1.4,3.6,-1.4                                                                    |-1.4,3.6,-1.4                                                                        |
|Bundle name                       |standardturret_dth-mod-up1             |standardturret_dth-mod-up2             |standardturret_dth-mod-up3             |standardturret_dth-mod-up4             |standardturret_dth-mod-up5             |standardturret_dth-mod-up6             |standardturret_dth-mod-up7                                                       |standardturret_dth-mod-up7                                                       |standardturret_dth-mod-up7                                                       |standardturret_dth-mod-up7                                                           |
|Icon camera position              |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-23.91,25.41,24.96                     |-27.49,28.95,28.68                     |-30.11,31.54,31.39                                                               |-30.11,31.54,31.39                                                               |-30.11,31.54,31.39                                                               |-30.11,31.54,31.39                                                                   |
|Turret displayed damage per second|500                                    |750                                    |900                                    |1200                                   |1450                                   |1600                                   |1750                                                                             |1900                                                                             |2050                                                                             |2250                                                                                 |
|Turret gun position               |"topMesh_up1/gunMesh_up1/locator_gun":1|"topMesh_up2/gunMesh_up2/locator_gun":1|"topMesh_up3/gunMesh_up3/locator_gun":1|"topMesh_up4/gunMesh_up4/locator_gun":1|"topMesh_up5/gunMesh_up5/locator_gun":1|"topMesh_up6/gunMesh_up6/locator_gun":1|"topMesh_up7/gunMesh_up7/locator_gun1":1,"topMesh_up7/gunMesh_up7/locator_gun2":1|"topMesh_up8/gunMesh_up8/locator_gun1":1,"topMesh_up8/gunMesh_up8/locator_gun2":1|"topMesh_up9/gunMesh_up9/locator_gun1":1,"topMesh_up9/gunMesh_up9/locator_gun2":1|"topMesh_up10/gunMesh_up10/locator_gun1":1,"topMesh_up10/gunMesh_up10/locator_gun2":1|
|Turret tracker name               |topMesh_up1                            |topMesh_up2                            |topMesh_up3                            |topMesh_up4                            |topMesh_up5                            |topMesh_up6                            |topMesh_up7                                                                      |topMesh_up8                                                                      |topMesh_up9                                                                      |topMesh_up10                                                                         |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.7021276595744680992794428675551898777484893798828125

|Level |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|------|---|---|---|---|---|---|---|---|---|---|
|Max XP|10 |32 |66 |104|160|216|294|368|468|560|
|Order |911|912|913|914|915|916|917|918|919|920|
|Xp    |5  |8  |11 |13 |16 |18 |21 |23 |26 |28 |


