---
title: Rapid Fire Turret (smugglerRapidFireTurret)
category: building
---

# Rapid Fire Turret (smugglerRapidFireTurret) — version 1119

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

## Turret attack : Smuggler Standard Turret


### Targeting

  * Turret max attack range: 8
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret support troop (100)**, _Turret droideka (60)_, _Turret flying infantry (60)_, _Turret flying vehicle (60)_, _Turret headquarters (60)_, _Turret heavy infantry (60)_, _Turret heavy vehicle (60)_, _Turret infantry (60)_, _Turret light vehicle (60)_, _Turret other building (60)_, _Turret ressource generator (60)_, _Turret storage (60)_, _Turret turret (60)_, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

### Shooting

  * Turret animation delay: 0
  * Turret charge time: 600ms
  * Turret clip retargeting: Yes
  * Turret gun shooting sequence: 1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 650ms
  * Turret shot count: 3
  * Turret shot delay: 250ms

|Level                 |1  |2  |3  |4  |5  |6  |7   |8   |9   |10  |
|----------------------|---|---|---|---|---|---|----|----|----|----|
|Turret damage per shot|292|438|525|700|846|992|1138|1283|1429|1575|


|Level                                     |1  |2   |3   |4   |5   |6   |7   |8   |9   |10  |
|------------------------------------------|---|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |500|750 |1000|1500|1750|2000|2250|2500|2750|3000|
|Turret attack calculated damage per second|438|657 |787 |1050|1269|1488|1707|1924|2143|2362|
|Turret attack calculated damage per clip  |876|1314|1575|2100|2538|2976|3414|3849|4287|4725|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 2s
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

|Level    |1                         |2                         |3                         |4                         |5                         |6                         |7                         |8                         |9                         |10                         |
|---------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|---------------------------|
|Turret id|t_smugglerRapidFireTurret1|t_smugglerRapidFireTurret2|t_smugglerRapidFireTurret3|t_smugglerRapidFireTurret4|t_smugglerRapidFireTurret5|t_smugglerRapidFireTurret6|t_smugglerRapidFireTurret7|t_smugglerRapidFireTurret8|t_smugglerRapidFireTurret9|t_smugglerRapidFireTurret10|


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
  * Turret timey wimey: 1.7142857142857141905523121749865822494029998779296875

|Level |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|------|---|---|---|---|---|---|---|---|---|---|
|Max XP|30 |48 |54 |72 |84 |102|114|132|144|162|
|Order |550|551|552|553|554|555|556|557|558|559|
|Xp    |5  |8  |9  |12 |14 |17 |19 |22 |24 |27 |


