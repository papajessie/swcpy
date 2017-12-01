---
title: bldtitlesmugglerBurstTurret (smugglerBurstTurret)
category: building
---

# bldtitlesmugglerBurstTurret (smugglerBurstTurret) — version 1102

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: turret
  * Cross credits: 0
  * Side: Independant units
  * Force reticle when targeted: No
  * Hide if locked: No
  * Max quantity: 6
  * Produce: 0
  * Time: 0s
  * Type: turret

|Level          |1   |2   |3   |4    |5    |6    |7    |8    |9    |10   |
|---------------|----|----|----|-----|-----|-----|-----|-----|-----|-----|
|Cross materials|750 |1250|1556|1500 |2000 |2778 |4167 |10417|11111|11905|
|Cross time     |1m  |2m  |3m  |4m   |5m   |6m   |7m   |8m   |9m   |10m  |
|Health         |3800|5500|6000|15000|17500|20000|22500|25000|27500|30000|


### Training stats

  * Training cost: 1 All.

|Level   |1                                |2                                |3                                |4                                |5                                |6                                |7                                |8                                |9                                |10                                |
|--------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|----------------------------------|
|Building|[Headquarters 1](smugglerHQ.html)|[Headquarters 2](smugglerHQ.html)|[Headquarters 3](smugglerHQ.html)|[Headquarters 4](smugglerHQ.html)|[Headquarters 5](smugglerHQ.html)|[Headquarters 6](smugglerHQ.html)|[Headquarters 7](smugglerHQ.html)|[Headquarters 8](smugglerHQ.html)|[Headquarters 9](smugglerHQ.html)|[Headquarters 10](smugglerHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Smuggler Burst Turret


### Targeting

  * Turret max attack range: 8
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret droideka (60)**, **Turret flying infantry (60)**, **Turret flying vehicle (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

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
|Turret damage per shot|178|267|321|428|517|606|695|784|873|962|


|Level                                     |1   |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |500 |750 |1000|1500|1750|2000|2250|2500|2750|3000|
|Turret attack calculated damage per second|499 |749 |901 |1201|1451|1701|1950|2200|2450|2700|
|Turret attack calculated damage per clip  |1424|2136|2568|3424|4136|4848|5560|6272|6984|7696|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 2.850s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 10
  * Turret attack damage multipliers: **(125)**: Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 8

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: burst_turret
  * Turret projectile type: projectileSmugglerBurstTurret

|Level    |1                     |2                     |3                     |4                     |5                     |6                     |7                     |8                     |9                     |10                     |
|---------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|-----------------------|
|Turret id|t_smugglerBurstTurret1|t_smugglerBurstTurret2|t_smugglerBurstTurret3|t_smugglerBurstTurret4|t_smugglerBurstTurret5|t_smugglerBurstTurret6|t_smugglerBurstTurret7|t_smugglerBurstTurret8|t_smugglerBurstTurret9|t_smugglerBurstTurret10|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: burstturret_smg-mod
  * Audio attack: "sfx_attack_blasternest_1":20,"sfx_attack_blasternest_2":20,"sfx_attack_blasternest_3":20,"sfx_attack_blasternest_4":20,"sfx_attack_blasternest_5":20
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Buff asset offset: -1.2,2.8,-1.2
  * Bundle name: burstturret_smg-mod
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Icon camera position: -25.17,30.22,28.98
  * Icon lookat position: 0.41,2.03,-0.59
  * Stash order: 1000
  * Store tab: not_in_store
  * Turret animation delay: 0
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_y_sm
  * Turret attack hit spark: fx_blaster_hit_y_sm
  * Turret attack max scale: 125
  * Turret attack muzzle flash: fx_blaster_flash_y_sm
  * Turret attack name: Smuggler Burst Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret gun position: "locator_gun":1
  * Turret max scale: 0
  * Turret tracker name: n/a

|Level                             |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------------|---|---|----|----|----|----|----|----|----|----|
|Turret displayed damage per second|500|750|1000|1500|1750|2000|2250|2500|2750|3000|


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
|Max XP|30 |48 |54 |72 |84 |102|114|132|144|162|
|Order |560|561|562|563|564|565|566|567|568|569|
|Xp    |5  |8  |9  |12 |14 |17 |19 |22 |24 |27 |


