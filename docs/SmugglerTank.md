---
title: Smuggler Bruiser (SmugglerTank)
category: unit
---

# Smuggler Bruiser (SmugglerTank) — version 1109

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Independant units
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 10
  * Type: vehicle

|Level |1 |2   |3    |4    |5    |6    |7    |8    |9    |10   |
|------|--|----|-----|-----|-----|-----|-----|-----|-----|-----|
|Health|90|8100|18900|21600|27000|30000|33000|36000|39000|45000|


### Training stats

|Level        |1                                                    |2                                                    |3                                                    |4                                                    |5                                                    |6                                                    |7                                                    |8                                                    |9                                                    |10                                                    |
|-------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|
|Training time|3m30s                                                |3m40s                                                |3m50s                                                |4m                                                   |4m10s                                                |4m20s                                                |4m30s                                                |4m40s                                                |4m50s                                                |5m                                                    |
|Training cost|500$                                                 |700$                                                 |900$                                                 |1100$                                                |1300$                                                |1500$                                                |1700$                                                |1900$                                                |2100$                                                |2300$                                                 |
|Building     |["bld_title_smugglerFactory" 3](smugglerFactory.html)|["bld_title_smugglerFactory" 3](smugglerFactory.html)|["bld_title_smugglerFactory" 3](smugglerFactory.html)|["bld_title_smugglerFactory" 4](smugglerFactory.html)|["bld_title_smugglerFactory" 5](smugglerFactory.html)|["bld_title_smugglerFactory" 6](smugglerFactory.html)|["bld_title_smugglerFactory" 7](smugglerFactory.html)|["bld_title_smugglerFactory" 8](smugglerFactory.html)|["bld_title_smugglerFactory" 9](smugglerFactory.html)|["bld_title_smugglerFactory" 10](smugglerFactory.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|1500$|5000$|14000$|24000$|50000$|100000$|200000$|750000$|2000000$|4000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Propensity to go around obstacles: 1
  * Rotation speed: 3.927
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 2x3

|Level    |1 |2-10|
|---------|--|----|
|Max speed|40|30  |


## Main attack : SmugglerTank

### Targeting

  * Attack shield border: No
  * Max attack range: 6
  * Min attack range: 0
  * New rotation speed: 3927
  * Target preference strength: 90
  * View range: 8

|Level             |1-4                                                                                                                                                                                                                                                                                                                                                                                                      |5-10                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Target preferences|**Turret (60)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Support troop (50), Headquarters (40), Other building (40), Ressource generator (40), Shield (40), Shield generator (40), Storage (40), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|**Turret (60)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Heavy infantry (50), Heavy infantry hero (50), Heavy vehicle (50), Heavy vehicule hero (50), Infantry (50), Infantry hero (50), Light vehicle (50), Support troop (50), Vehicule hero (50), Headquarters (40), Other building (40), Ressource generator (40), Shield (40), Shield generator (40), Storage (40), Wall (1), Trap (0)|


### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 2s
  * Retargeting offset: 12
  * Self-centered targeting: No
  * Shot count: 4
  * Time between shots: 200ms
  * Target locking: No

|Level          |1 |2 |3  |4  |5   |6   |7   |8   |9   |10  |
|---------------|--|--|---|---|----|----|----|----|----|----|
|Damage per shot|72|86|629|719|1283|1425|1568|1710|1853|2138|


### Projectile

|Level                       |1  |2  |3   |4   |5   |6   |7   |8   |9   |10  |
|----------------------------|---|---|----|----|----|----|----|----|----|----|
|Displayed damage per second |101|120|882 |1009|1800|2000|2200|2400|2600|3000|
|Calculated damage per second|101|120|882 |1009|1800|2000|2200|2400|2600|3000|
|Calculated damage per clip  |288|344|2516|2876|5132|5700|6272|6840|7412|8552|


  * Cannons per sequence: 1
  * Cliptime: 2.850s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(100)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 4

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerTank

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: aat1_smg-ani
  * Audio attack: "sfx_attack_tank_1":25,"sfx_attack_tank_2":25,"sfx_attack_tank_3":25,"sfx_attack_tank_4":25
  * Audio death: "sfx_death_tank_1":25,"sfx_death_tank_2":25,"sfx_death_tank_3":25,"sfx_death_tank_4":25
  * Audio placement: "sfx_placement_tank_1":25,"sfx_placement_tank_2":25,"sfx_placement_tank_3":25,"sfx_placement_tank_4":25
  * Buff asset offset: 0.00,1.81,0.00
  * Bullet: fx_blaster_beam_y_lrg
  * Bundle name: aat1_smg-ani
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "aat1_rbl_rig_MASTER_MOVER/aat1_rbl_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_y_lrg
  * Icon camera position: 22.61,26.18,29.65
  * Icon lookat position: -0.48,1.51,-0.32
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_lrg
  * Name: SmugglerTank
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |2  |3  |4   |5   |6   |7   |8   |9   |10  |
|---------------------------|---|---|---|----|----|----|----|----|----|----|
|Displayed damage per second|101|120|882|1009|1800|2000|2200|2400|2600|3000|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 2
  * Auto spawn spreading scale: 2
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |341301|341302|341303|341304|341305|341306|341307|341308|341309|341310|
|Point value|10    |12    |14    |16    |18    |20    |22    |24    |26    |30    |


