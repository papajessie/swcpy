---
title: Rapid Fire Turret (smugglerRapidFireTurret)
category: building
---

# Rapid Fire Turret (smugglerRapidFireTurret)

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

|Level          |10   |9    |8    |7    |6    |5    |4    |3   |2   |1   |
|---------------|-----|-----|-----|-----|-----|-----|-----|----|----|----|
|Cross materials|11905|11111|10417|4167 |2778 |2000 |1500 |1556|1250|750 |
|Cross time     |10m  |9m   |8m   |7m   |6m   |5m   |4m   |3m  |2m  |1m  |
|Health         |30000|27500|25000|22500|20000|17500|15000|6000|5500|3800|


### Training stats

  * Training cost: 1 All.

|Level   |10                                |9                                |8                                |7                                |6                                |5                                |4                                |3                                |2                                |1                                |
|--------|----------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
|Building|[Headquarters 10](smugglerHQ.html)|[Headquarters 9](smugglerHQ.html)|[Headquarters 8](smugglerHQ.html)|[Headquarters 7](smugglerHQ.html)|[Headquarters 6](smugglerHQ.html)|[Headquarters 5](smugglerHQ.html)|[Headquarters 4](smugglerHQ.html)|[Headquarters 3](smugglerHQ.html)|[Headquarters 2](smugglerHQ.html)|[Headquarters 1](smugglerHQ.html)|


### Upgrading stats

  * Upgrade requirements: Nothing

### Movement stats

  * Acceleration: 0
  * Max speed: 0
  * Unit size on map: 2x2

## Turret attack : Smuggler Standard Turret


### Targeting

  * Turret max attack range: 8
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret support troop (100)**, _Turret droideka (60)_, _Turret flying infantry (60)_, _Turret flying vehicle (60)_, _Turret headquarters (60)_, _Turret heavy infantry (60)_, _Turret heavy vehicle (60)_, _Turret infantry (60)_, _Turret light vehicle (60)_, _Turret other building (60)_, _Turret ressource generator (60)_, _Turret storage (60)_, _Turret turret (60)_, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

### Shooting

  * Turret animation delay: 0s
  * Turret charge time: 600ms
  * Turret clip retargeting: Yes
  * Turret gun shooting sequence: 1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 650ms
  * Turret shot count: 3
  * Turret shot delay: 250ms

|Level                 |10  |9   |8   |7   |6  |5  |4  |3  |2  |1  |
|----------------------|----|----|----|----|---|---|---|---|---|---|
|Turret damage per shot|1575|1429|1283|1138|992|846|700|525|438|292|


|Level                                     |10  |9   |8   |7   |6   |5   |4   |3   |2   |1  |
|------------------------------------------|----|----|----|----|----|----|----|----|----|---|
|Turret displayed damage per second        |3000|2750|2500|2250|2000|1750|1500|1000|750 |500|
|Turret attack calculated damage per second|2700|2449|2199|1950|1700|1450|1200|900 |750 |500|
|Turret attack calculated damage per clip  |4725|4287|3849|3414|2976|2538|2100|1575|1314|876|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 1.750s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 20
  * Turret attack damage multipliers: **(100)**: Turret attack droideka, Turret attack flying infantry, Turret attack flying vehicle, Turret attack headquarters, Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 3

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: rapid_fire_turret
  * Turret projectile type: projectileSmugglerRapidFireTurret

|Level    |10                         |9                         |8                         |7                         |6                         |5                         |4                         |3                         |2                         |1                         |
|---------|---------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
|Turret id|t_smugglerRapidFireTurret10|t_smugglerRapidFireTurret9|t_smugglerRapidFireTurret8|t_smugglerRapidFireTurret7|t_smugglerRapidFireTurret6|t_smugglerRapidFireTurret5|t_smugglerRapidFireTurret4|t_smugglerRapidFireTurret3|t_smugglerRapidFireTurret2|t_smugglerRapidFireTurret1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: standardturret_smg-mod
  * Audio attack: "sfx_attack_rebel_rapidfireturret_1":35,"sfx_attack_rebel_rapidfireturret_2":35,"sfx_attack_rebel_rapidfireturret_3":30
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Buff asset offset: -1.6,2,-1.4
  * Bundle name: standardturret_smg-mod
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Icon camera position: -20.57,21.82,36.12
  * Icon lookat position: 0.37,1.29,-0.37
  * Stash order: 1000
  * Store tab: not_in_store
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_y_lrg
  * Turret attack hit spark: fx_blaster_hit_y_lrg
  * Turret attack max scale: 100
  * Turret attack muzzle flash: fx_blaster_flash_y_lrg
  * Turret attack name: Smuggler Standard Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret gun position: "turretBase/turretHeadMesh/turretGunMesh/locator_gun":1
  * Turret max scale: 0
  * Turret tracker name: turretBase/turretHeadMesh

|Level                             |10  |9   |8   |7   |6   |5   |4   |3   |2  |1  |
|----------------------------------|----|----|----|----|----|----|----|----|---|---|
|Turret displayed damage per second|3000|2750|2500|2250|2000|1750|1500|1000|750|500|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.7142857140000000715218675395590253174304962158203125

|Level |10 |9  |8  |7  |6  |5  |4  |3  |2  |1  |
|------|---|---|---|---|---|---|---|---|---|---|
|Max XP|162|144|132|114|102|84 |72 |54 |48 |30 |
|Order |559|558|557|556|555|554|553|552|551|550|
|Xp    |27 |24 |22 |19 |17 |14 |12 |9  |8  |5  |


