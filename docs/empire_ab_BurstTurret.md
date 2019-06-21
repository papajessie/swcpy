---
title: Burst Turret (empire_ab_BurstTurret)
category: building
---

# Burst Turret (empire_ab_BurstTurret)

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: turret
  * Cross credits: 0
  * Side: Empire
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

## Turret attack : Empire Burst Turret


### Targeting

  * Turret max attack range: 9
  * Turret min attack range: 0
  * Turret target preference strength: 90
  * Turret target preferences: **Turret droideka (60)**, **Turret flying infantry (60)**, **Turret flying vehicle (60)**, **Turret headquarters (60)**, **Turret heavy infantry (60)**, **Turret heavy vehicle (60)**, **Turret infantry (60)**, **Turret light vehicle (60)**, **Turret other building (60)**, **Turret ressource generator (60)**, **Turret storage (60)**, **Turret support troop (60)**, **Turret turret (60)**, Turret heavy infantry hero (1), Turret heavy vehicule hero (1), Turret infantry hero (1), Turret vehicule hero (1), Turret wall (1)
  * Turret view range: 10

### Shooting

  * Turret animation delay: 0s
  * Turret charge time: 1.750s
  * Turret clip retargeting: No
  * Turret gun shooting sequence: 1
  * Turret impact delay: 250ms
  * Turret can shoot over walls: Yes
  * Turret reload time: 1.200s
  * Turret shot count: 8
  * Turret shot delay: 175ms

|Level                 |10  |9   |8   |7   |6  |5  |4  |3  |2  |1  |
|----------------------|----|----|----|----|---|---|---|---|---|---|
|Turret damage per shot|1292|1177|1091|1005|919|832|689|517|431|287|


|Level                                     |10   |9   |8   |7   |6   |5   |4   |3   |2   |1   |
|------------------------------------------|-----|----|----|----|----|----|----|----|----|----|
|Turret displayed damage per second        |2475 |2255|2090|1926|1761|1594|1320|990 |825 |550 |
|Turret attack calculated damage per second|2475 |2255|2090|1925|1760|1594|1320|990 |825 |549 |
|Turret attack calculated damage per clip  |10336|9416|8728|8040|7352|6656|5512|4136|3448|2296|


  * Turret attack cannons per sequence: 1
  * Turret attack cliptime: 4.175s
  * Turret attack directional: Yes
  * Turret attack is deflectable: Yes
  * Turret attack max speed: 10
  * Turret attack damage multipliers: **(140)**: Turret attack flying infantry, Turret attack flying vehicle, **(125)**: Turret attack heavy infantry, Turret attack heavy infantry hero, Turret attack heavy vehicle, Turret attack heavy vehicule hero, **(100)**: Turret attack droideka, Turret attack headquarters, Turret attack infantry, Turret attack infantry hero, Turret attack light vehicle, Turret attack other building, Turret attack ressource generator, Turret attack shield, Turret attack shield generator, Turret attack storage, Turret attack support troop, Turret attack trap, Turret attack turret, Turret attack vehicule hero, Turret attack wall
  * Turret attack pass through shield: No
  * Turret attack salvos: 8

## Internal stats

These stats internal to the system link different parts of data together.

  * Sub type: burst_turret
  * Turret projectile type: projectileEmpireBurstTurret

|Level    |10                       |9                       |8                       |7                       |6                       |5                       |4                       |3                       |2                       |1                       |
|---------|-------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|Turret id|t_empire_ab_BurstTurret10|t_empire_ab_BurstTurret9|t_empire_ab_BurstTurret8|t_empire_ab_BurstTurret7|t_empire_ab_BurstTurret6|t_empire_ab_BurstTurret5|t_empire_ab_BurstTurret4|t_empire_ab_BurstTurret3|t_empire_ab_BurstTurret2|t_empire_ab_BurstTurret1|


## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Audio attack: "sfx_attack_blasternest_1":20,"sfx_attack_blasternest_2":20,"sfx_attack_blasternest_3":20,"sfx_attack_blasternest_4":20,"sfx_attack_blasternest_5":20
  * Audio death: "sfx_explosion_metal_1":25,"sfx_explosion_metal_2":25,"sfx_explosion_metal_3":25,"sfx_explosion_metal_4":25
  * Audio placement: "sfx_placement_turret_1":100
  * Collect notify: 0
  * Cycle time: 0s
  * Destruct FX: fx_debris_{0}x{1}
  * Icon lookat position: 0.41,2.03,-0.59
  * Stash order: 50
  * Store tab: not_in_store
  * Turret attack arcs: No
  * Turret attack bullet: fx_blaster_beam_r_sm
  * Turret attack hit spark: fx_blaster_hit_r_sm
  * Turret attack max scale: 125
  * Turret attack muzzle flash: fx_blaster_flash_r_sm
  * Turret attack name: Empire Burst Turret
  * Turret attack spin speed: 0
  * Turret favorite target type: infantry
  * Turret gun position: "locator_gun":1
  * Turret max scale: 0
  * Turret tracker name: n/a

|Level                             |10                     |9                      |8                      |7                      |6                      |5                      |4                      |3                      |2                      |1                      |
|----------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|Asset name                        |burstturret_emp-mod-up8|burstturret_emp-mod-up8|burstturret_emp-mod-up8|burstturret_emp-mod-up7|burstturret_emp-mod-up6|burstturret_emp-mod-up5|burstturret_emp-mod-up4|burstturret_emp-mod-up3|burstturret_emp-mod-up2|burstturret_emp-mod-up1|
|Buff asset offset                 |-1.2,4.2,-1.2          |-1.2,4.2,-1.2          |-1.2,4.2,-1.2          |-1.2,4.2,-1.2          |-1.2,3.6,-1.2          |-1,3.6,-1              |-0.6,3,-0.6            |-0.6,3,-0.6            |-0.6,3,-0.6            |-0.6,3,-0.6            |
|Bundle name                       |burstturret_emp-mod-up8|burstturret_emp-mod-up8|burstturret_emp-mod-up8|burstturret_emp-mod-up7|burstturret_emp-mod-up6|burstturret_emp-mod-up5|burstturret_emp-mod-up4|burstturret_emp-mod-up3|burstturret_emp-mod-up2|burstturret_emp-mod-up1|
|Icon camera position              |-27.71,33.03,31.93     |-27.71,33.03,31.93     |-27.71,33.03,31.93     |-28.36,33.75,32.71     |-28.03,33.38,32.27     |-28.3,33.68,32.61      |-28.02,33.36,32.28     |-23.53,28.41,27.14     |-22.49,27.21,25.84     |-22.7,27.44,26.09      |
|Turret displayed damage per second|2475                   |2255                   |2090                   |1926                   |1761                   |1594                   |1320                   |990                    |825                    |550                    |


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Order: 205
  * Turret arming delay: 0
  * Turret attack seeks target: Yes
  * Turret attack streams: no
  * Turret splash: false
  * Turret strict cool down: No
  * Turret timey wimey: 1.9161676649999999089146740516298450529575347900390625

|Level |10  |9   |8  |7  |6  |5  |4  |3  |2  |1 |
|------|----|----|---|---|---|---|---|---|---|--|
|Max XP|1400|1170|960|770|600|450|320|210|120|50|
|Xp    |70  |65  |60 |55 |50 |45 |40 |35 |30 |25|


