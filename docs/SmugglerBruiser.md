---
title: Mercenary Bruiser (SmugglerBruiser)
category: unit
---

# Mercenary Bruiser (SmugglerBruiser) — version 1112

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 5
  * Type: infantry

|Level |1  |2  |3  |4    |5    |6    |7    |8    |9    |10   |
|------|---|---|---|-----|-----|-----|-----|-----|-----|-----|
|Health|500|600|700|12000|13500|15000|16500|18000|19500|22500|


### Training stats

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |6                                  |7                                  |8                                  |9                                  |10                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|------------------------------------|
|Training time|1m45s                              |1m50s                              |1m55s                              |2m                                 |2m5s                               |2m10s                              |2m15s                              |2m20s                              |2m25s                              |2m30s                               |
|Training cost|250$                               |350$                               |450$                               |550$                               |650$                               |750$                               |850$                               |950$                               |1050$                              |1150$                               |
|Building     |[Barracks 2](smugglerBarracks.html)|[Barracks 2](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 10](smugglerBarracks.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|1500$|5000$|14000$|24000$|50000$|100000$|200000$|750000$|2000000$|4000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : SmugglerBruiser

### Targeting

  * Attack shield border: No
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * View range: 12

|Level             |1-4                                                                                                                                                                                                                                                                                                                                                                                                      |5-10                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Max attack range  |7                                                                                                                                                                                                                                                                                                                                                                                                        |5                                                                                                                                                                                                                                                                                                                                                                                                            |
|Target preferences|**Turret (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Support troop (50), Headquarters (40), Other building (40), Ressource generator (40), Shield (40), Shield generator (40), Storage (40), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|**Turret (70)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Heavy infantry (50), Heavy infantry hero (50), Heavy vehicle (50), Heavy vehicule hero (50), Infantry (50), Infantry hero (50), Light vehicle (50), Support troop (50), Vehicule hero (50), Headquarters (40), Other building (40), Ressource generator (40), Shield (40), Shield generator (40), Storage (40), Wall (1), Trap (0)|


### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1,2
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 1.500s
  * Self-centered targeting: No
  * Time between shots: 500ms
  * Target locking: No

|Level             |1  |2  |3  |4  |5   |6   |7   |8   |9   |10  |
|------------------|---|---|---|---|----|----|----|----|----|----|
|Damage per shot   |113|135|158|347|1013|1125|1238|1350|1463|1688|
|Retargeting offset|14 |14 |14 |14 |10  |10  |10  |10  |10  |10  |
|Shot count        |2  |2  |2  |2  |1   |1   |1   |1   |1   |1   |


### Projectile

|Level                       |1  |2  |3  |4  |5   |6   |7   |8   |9   |10  |
|----------------------------|---|---|---|---|----|----|----|----|----|----|
|Displayed damage per second |100|120|140|308|578 |642 |707 |771 |836 |964 |
|Calculated damage per second|100|120|140|308|578 |642 |707 |771 |836 |964 |
|Calculated damage per clip  |226|270|316|694|1013|1125|1238|1350|1463|1688|


  * Cannons per sequence: 2
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(200)**: Wall, **(100)**: Droideka, Shield, Storage, **(50)**: Headquarters, Other building, Ressource generator, Shield generator, Trap, Turret, **(20)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero
  * Pass through shield: No

|Level   |1-4   |5-10  |
|--------|------|------|
|Cliptime|2.250s|1.750s|
|Salvos  |2     |1     |


## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerBruiser

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: bountyhunter_smg-ani
  * Audio attack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Buff asset offset: 0.00,0.08,0.00
  * Bullet: fx_blaster_beam_y_sm
  * Bundle name: bountyhunter_smg-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: turret
  * Gun position: "bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Lt":1,"bountyhunter_smg_rig_MASTER_MOVER/bountyhunter_smg_rig_locator_gun_Rt":2
  * Hit spark: fx_blaster_hit_y_sm
  * Icon camera position: 9,10,11.12
  * Icon lookat position: 0.09,1.4,0.28
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Name: SmugglerBruiser
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|---------------------------|---|---|---|---|---|---|---|---|---|---|
|Displayed damage per second|100|120|140|308|578|642|707|771|836|964|


## Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Arming delay: 0
  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Seeks target: Yes
  * Splash: 0
  * Streams: no
  * Strict cool down: No
  * Target in range modifier: 1
  * Xp: 0

|Level      |1     |2     |3     |4     |5     |6     |7     |8     |9     |10    |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |331101|331102|331103|331104|331105|331106|331107|331108|331109|331110|
|Point value|5     |6     |7     |8     |9     |10    |11    |12    |13    |15    |


