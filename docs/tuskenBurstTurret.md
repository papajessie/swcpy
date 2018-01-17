---
title: bldtitletuskenBurstTurret (tuskenBurstTurret)
category: building
---

# bldtitletuskenBurstTurret (tuskenBurstTurret) — version 1117

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

|Level       |1   |2   |3   |4    |5    |6    |7    |8    |9    |10   |
|------------|----|----|----|-----|-----|-----|-----|-----|-----|-----|
|Health      |3200|4000|5500|15000|14500|16000|17500|19000|20500|22500|
|Max quantity|2   |6   |6   |6    |6    |6    |6    |6    |6    |6    |
|Time        |1m  |0s  |0s  |0s   |0s   |0s   |0s   |0s   |0s   |0s   |


### Training stats

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |6                                  |7                                                  |8                                                  |9                                                  |10                                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|----------------------------------------------------|
|Training cost|1000 All.                          |1 All.                             |1 All.                             |1 All.                             |1 All.                             |1 All.                             |1 All.                                             |1 All.                                             |1 All.                                             |1 All.                                              |
|Building     |[Tusken Raider HQ 1](tuskenHQ.html)|[Tusken Raider HQ 2](tuskenHQ.html)|[Tusken Raider HQ 3](tuskenHQ.html)|[Tusken Raider HQ 4](tuskenHQ.html)|[Tusken Raider HQ 5](tuskenHQ.html)|[Tusken Raider HQ 6](tuskenHQ.html)|["bld_title_tuskenHQLocked" 7](tuskenHQLocked.html)|["bld_title_tuskenHQLocked" 8](tuskenHQLocked.html)|["bld_title_tuskenHQLocked" 9](tuskenHQLocked.html)|["bld_title_tuskenHQLocked" 10](tuskenHQLocked.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : TuskenHero


### Targeting

  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret droideka (60)**, **Turret flying infantry (60)**, **Turret flying vehicle (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

|Level                  |1-4|5-10|
|-----------------------|---|----|
|Turret max attack range|8  |9   |


### Shooting

  * Turret time between start of clip and first shot: 300ms
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret time between end of clip and start of clip: 1.500s
  * Turret shot count: 8
  * Turret time between shots: 150ms

|Level                 |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|----------------------|---|---|---|---|---|---|---|---|---|---|
|Turret damage per shot|178|267|321|428|568|627|686|745|803|882|


|Level                                     |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |500 |750 |1000|1500|1594|1760|1925|2091|2254|2475|
|Turret attack calculated damage per second|499 |749 |901 |1201|1594|1760|1925|2091|2254|2475|
|Turret attack calculated damage per clip  |1424|2136|2568|3424|4544|5016|5488|5960|6424|7056|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 2.850s
  * Turret attack directional: Yes
  * Turret attack is deflectable: No
  * Turret attack max speed: 18
  * Turret attack damage multipliers: **(125)**: Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 8

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: burst_turret
  * Turret projectile type: projectileTuskenBurstTurret

|Level    |1                   |2                   |3                   |4                   |5                   |6                   |7                   |8                   |9                   |10                   |
|---------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|---------------------|
|Turret id|t_tuskenBurstTurret1|t_tuskenBurstTurret2|t_tuskenBurstTurret3|t_tuskenBurstTurret4|t_tuskenBurstTurret5|t_tuskenBurstTurret6|t_tuskenBurstTurret7|t_tuskenBurstTurret8|t_tuskenBurstTurret9|t_tuskenBurstTurret10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: burstturret_tkn-mod
  * Audio attack: "sfx_attack_tuskenraiders_rifleman_1":35,"sfx_attack_tuskenraiders_rifleman_2":35,"sfx_attack_tuskenraiders_rifleman_3":30
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Buff asset offset: -1.4,1.8,-1.4
  * Bundle name: burstturret_tkn-mod
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: effect176
  * Icon camera position: -34.55,28.66,37.83
  * Icon lookat position: 0.43,0.25,-0.02
  * Stash order: 1000
  * Store tab: not_in_store
  * Turret animation delay: 0
  * Turret attack arcs: No
  * Turret attack bullet: fx_slugthrower_projectile
  * Turret attack hit spark: fx_slugthrower_hit
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_slugthrower_muzzle
  * Turret attack name: TuskenHero
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret gun position: "locator_gun":1
  * Turret max scale: 0
  * Turret tracker name: n/a

|Level                             |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------------|---|---|----|----|----|----|----|----|----|----|
|Turret displayed damage per second|500|750|1000|1500|1594|1760|1925|2091|2254|2475|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 2.8070175438596489669862421578727662563323974609375

|Level |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|------|---|---|---|---|---|---|---|---|---|---|
|Max XP|10 |48 |54 |72 |84 |102|114|132|144|162|
|Order |655|656|657|658|659|660|661|662|663|664|
|Xp    |5  |8  |9  |12 |14 |17 |19 |22 |24 |27 |


