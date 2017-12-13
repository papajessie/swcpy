---
title: bldtitletuskenAutoTurret (tuskenAutoTurret)
category: building
---

# bldtitletuskenAutoTurret (tuskenAutoTurret) — version 1104

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

|Level       |1   |2   |3    |4    |5    |
|------------|----|----|-----|-----|-----|
|Health      |3200|4000|10000|15000|14500|
|Max quantity|2   |6   |6    |6    |6    |
|Time        |1m  |0s  |0s   |0s   |0s   |


### Training stats

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
|Training cost|1000 All.                          |1 All.                             |1 All.                             |1 All.                             |1 All.                             |
|Building     |[Tusken Raider HQ 1](tuskenHQ.html)|[Tusken Raider HQ 2](tuskenHQ.html)|[Tusken Raider HQ 3](tuskenHQ.html)|[Tusken Raider HQ 4](tuskenHQ.html)|[Tusken Raider HQ 5](tuskenHQ.html)|


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

|Level                    |1-4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Turret max attack range  |8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|Turret target preferences|**Turret droideka (60)**, **Turret flying infantry (60)**, **Turret flying vehicle (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)|**Turret support troop (100)**, _Turret droideka (60)_, _Turret flying infantry (60)_, _Turret flying vehicle (60)_, _Turret headquarters (60)_, _Turret heavy infantry (60)_, _Turret heavy vehicle (60)_, _Turret infantry (60)_, _Turret light vehicle (60)_, _Turret other building (60)_, _Turret ressource generator (60)_, _Turret storage (60)_, _Turret turret (60)_, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)|


### Shooting

  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 1s
  * Turret can shoot over walls: Yes

|Level                                            |1     |2     |3     |4     |5     |
|-------------------------------------------------|------|------|------|------|------|
|Turret time between start of clip and first shot |1.500s|1.500s|1.500s|1.500s|750ms |
|Turret damage per shot                           |2250  |3375  |4050  |5400  |817   |
|Turret time between end of clip and start of clip|3s    |3s    |3s    |3s    |1.200s|
|Turret shot count                                |1     |1     |1     |1     |4     |
|Turret time between shots                        |1ms   |1ms   |1ms   |1ms   |100ms |


|Level                                     |1   |2   |3   |4   |5   |
|------------------------------------------|----|----|----|----|----|
|Turret displayed damage per second        |500 |750 |1000|1500|1452|
|Turret attack calculated damage per second|500 |750 |900 |1200|1452|
|Turret attack calculated damage per clip  |2250|3375|4050|5400|3268|


  * Turret attack cannons per sequence: 1
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 20
  * Turret attack damage multipliers: **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No

|Level                 |1-4   |5     |
|----------------------|------|------|
|Turret attack cliptime|4.500s|2.250s|
|Turret attack salvos  |1     |4     |


## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: rapid_fire_turret
  * Turret projectile type: projectileTuskenAutoTurret

|Level    |1                  |2                  |3                  |4                  |5                  |
|---------|-------------------|-------------------|-------------------|-------------------|-------------------|
|Turret id|t_tuskenAutoTurret1|t_tuskenAutoTurret2|t_tuskenAutoTurret3|t_tuskenAutoTurret4|t_tuskenAutoTurret5|


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
  * Turret animation delay: 0
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

|Level                             |1  |2  |3   |4   |5   |
|----------------------------------|---|---|----|----|----|
|Turret displayed damage per second|500|750|1000|1500|1452|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No

|Level             |1                                                      |2                                                      |3                                                      |4                                                      |5                                                   |
|------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------|
|Max XP            |10                                                     |48                                                     |54                                                     |72                                                     |84                                                  |
|Order             |521                                                    |522                                                    |523                                                    |524                                                    |525                                                 |
|Turret timey wimey|0.22222222222222220988641083749826066195964813232421875|0.22222222222222220988641083749826066195964813232421875|0.22222222222222220988641083749826066195964813232421875|0.22222222222222220988641083749826066195964813232421875|1.77777777777777767909128669998608529567718505859375|
|Xp                |5                                                      |8                                                      |9                                                      |12                                                     |14                                                  |


