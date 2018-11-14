---
title: bldtitletuskenAutoTurret (tuskenAutoTurret)
category: building
---

# bldtitletuskenAutoTurret (tuskenAutoTurret)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Activation radius: 12
  * Armor type: turret
  * Cross credits: 0
  * Cross materials: 750
  * Cross time: 1m
  * Side: Tusken Raiders
  * Force reticle when targeted: No
  * Hide if locked: Yes
  * Produce: 0
  * Spawn protect: 5
  * Type: turret

|Level       |5    |4    |3    |2   |1   |
|------------|-----|-----|-----|----|----|
|Health      |14500|15000|10000|4000|3200|
|Max quantity|6    |6    |6    |6   |2   |
|Time        |0s   |0s   |0s   |0s  |1m  |


### Training stats

|Level        |5                                  |4                                  |3                                  |2                                  |1                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
|Training cost|1 All.                             |1 All.                             |1 All.                             |1 All.                             |1000 All.                          |
|Building     |[Tusken Raider HQ 5](tuskenHQ.html)|[Tusken Raider HQ 4](tuskenHQ.html)|[Tusken Raider HQ 3](tuskenHQ.html)|[Tusken Raider HQ 2](tuskenHQ.html)|[Tusken Raider HQ 1](tuskenHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Tusken Slug Thrower Shell


### Targeting

  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret view range: 10

|Level                    |5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |1-4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Turret max attack range  |10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|Turret target preferences|**Turret support troop (100)**, _Turret droideka (60)_, _Turret flying infantry (60)_, _Turret flying vehicle (60)_, _Turret headquarters (60)_, _Turret heavy infantry (60)_, _Turret heavy vehicle (60)_, _Turret infantry (60)_, _Turret light vehicle (60)_, _Turret other building (60)_, _Turret ressource generator (60)_, _Turret storage (60)_, _Turret turret (60)_, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)|**Turret droideka (60)**, **Turret flying infantry (60)**, **Turret flying vehicle (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)|


### Shooting

  * Turret animation delay: 0s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 1s
  * Turret can shoot over walls: Yes

|Level                 |5     |4     |3     |2     |1     |
|----------------------|------|------|------|------|------|
|Turret charge time    |750ms |1.500s|1.500s|1.500s|1.500s|
|Turret damage per shot|817   |5400  |4050  |3375  |2250  |
|Turret reload time    |1.200s|3s    |3s    |3s    |3s    |
|Turret shot count     |4     |1     |1     |1     |1     |
|Turret shot delay     |100ms |1ms   |1ms   |1ms   |1ms   |


|Level                                     |5   |4   |3   |2   |1   |
|------------------------------------------|----|----|----|----|----|
|Turret displayed damage per second        |1452|1500|1000|750 |500 |
|Turret attack calculated damage per second|1452|1200|900 |750 |500 |
|Turret attack calculated damage per clip  |3268|5400|4050|3375|2250|


  * Turret attack cannons per sequence: 1
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 20
  * Turret attack damage multipliers: **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No

|Level                 |5     |1-4   |
|----------------------|------|------|
|Turret attack cliptime|2.250s|4.500s|
|Turret attack salvos  |4     |1     |


## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: rapid_fire_turret
  * Turret projectile type: projectileTuskenAutoTurret

|Level    |5                  |4                  |3                  |2                  |1                  |
|---------|-------------------|-------------------|-------------------|-------------------|-------------------|
|Turret id|t_tuskenAutoTurret5|t_tuskenAutoTurret4|t_tuskenAutoTurret3|t_tuskenAutoTurret2|t_tuskenAutoTurret1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: standardturret_tkn-mod
  * Audio attack: "sfx_attack_tusken_autocannon_1":35,"sfx_attack_tusken_autocannon_2":35,"sfx_attack_tusken_autocannon_3":30
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Buff asset offset: -1.2,1.2,-1.2
  * Bundle name: standardturret_tkn-mod
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: effect176
  * Icon camera position: -20.16,23.24,23.78
  * Icon lookat position: 0,1.13,-0.13
  * Stash order: 1000
  * Store tab: not_in_store
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_g_lrg
  * Turret attack hit spark: fx_blaster_hit_g_lrg
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_blaster_flash_g_lrg
  * Turret attack name: Tusken Slug Thrower Shell
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret gun position: "Base/Turret/Pivot/locator_gun":1
  * Turret max scale: 0
  * Turret tracker name: Base/Turret

|Level                             |5   |4   |3   |2  |1  |
|----------------------------------|----|----|----|---|---|
|Turret displayed damage per second|1452|1500|1000|750|500|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No

|Level             |5                                                   |4                                                        |3                                                        |2                                                        |1                                                        |
|------------------|----------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|Max XP            |84                                                  |72                                                       |54                                                       |48                                                       |10                                                       |
|Order             |525                                                 |524                                                      |523                                                      |522                                                      |521                                                      |
|Turret timey wimey|1.77777777799999991970025803311727941036224365234375|0.2222222222000000135810893198140547610819339752197265625|0.2222222222000000135810893198140547610819339752197265625|0.2222222222000000135810893198140547610819339752197265625|0.2222222222000000135810893198140547610819339752197265625|
|Xp                |14                                                  |12                                                       |9                                                        |8                                                        |5                                                        |


