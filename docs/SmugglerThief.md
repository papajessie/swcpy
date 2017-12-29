---
title: Mercenary Thief (SmugglerThief)
category: unit
---

# Mercenary Thief (SmugglerThief) — version 1112

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: infantry
  * Side: Independant units
  * Buildable unit: Yes
  * Role: Looter
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 2
  * Type: infantry

|Level |1  |2  |3  |4  |5   |6   |7   |8   |9   |10  |
|------|---|---|---|---|----|----|----|----|----|----|
|Health|500|600|700|800|4320|4800|5280|5760|6240|7200|


### Training stats

|Level        |1                                  |2                                  |3                                  |4                                  |5                                  |6                                  |7                                  |8                                  |9                                  |10                                  |
|-------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|------------------------------------|
|Training time|42s                                |44s                                |46s                                |48s                                |50s                                |52s                                |54s                                |56s                                |58s                                |1m                                  |
|Training cost|100$                               |140$                               |180$                               |220$                               |260$                               |300$                               |340$                               |380$                               |420$                               |460$                                |
|Building     |[Barracks 3](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 10](smugglerBarracks.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |1    |2    |3     |4     |5     |6      |7      |8      |9       |10      |
|--------------------|-----|-----|------|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|1500$|5000$|14000$|24000$|50000$|100000$|200000$|750000$|2000000$|4000000$|


### Movement stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 40
  * Propensity to go around obstacles: 1
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1

## Main attack : SmugglerThief

### Targeting

  * Attack shield border: No
  * Max attack range: 4
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * View range: 8

|Level             |1-4                                                                                                                                                                                                                                                                                                                                                                                                          |5-10                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Target preferences|**Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|**Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy infantry hero (50), Heavy vehicle (50), Heavy vehicule hero (50), Infantry (50), Infantry hero (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Vehicule hero (50), Wall (1), Trap (0)|


### Shooting

  * Time between start of clip and first shot: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 800ms
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 0s
  * Target locking: No

|Level          |1  |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|---------------|---|---|---|---|---|---|---|---|----|----|
|Damage per shot|105|126|147|168|738|819|901|983|1065|1229|


### Projectile

|Level                       |1  |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|----------------------------|---|---|---|---|---|---|---|---|----|----|
|Displayed damage per second |99 |119|139|159|702|779|858|936|1014|1170|
|Calculated damage per second|100|120|140|160|702|780|858|936|1014|1170|
|Calculated damage per clip  |105|126|147|168|738|819|901|983|1065|1229|


  * Cannons per sequence: 1
  * Cliptime: 1.050s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 18
  * Damage multipliers: **(400)**: Ressource generator, Storage, **(100)**: Droideka, Shield, **(75)**: Flying infantry, Flying vehicle, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Support troop, Vehicule hero, **(50)**: Headquarters, Other building, Shield generator, Trap, Turret, Wall
  * Pass through shield: No
  * Salvos: 1

## Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SmugglerThief

## Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Animation delay: 0
  * Arcs: No
  * Asset name: looter_smg-ani
  * Audio attack: "sfx_attack_heavyblasterrifle_1":25,"sfx_attack_heavyblasterrifle_2":25,"sfx_attack_heavyblasterrifle_3":25,"sfx_attack_heavyblasterrifle_4":25
  * Audio death: "sfx_death_troop_1":10,"sfx_death_troop_2":10,"sfx_death_troop_3":10,"sfx_death_troop_4":10,"sfx_death_troop_5":10,"sfx_death_troop_6":10,"sfx_death_troop_7":10,"sfx_death_troop_8":30
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Bullet: fx_blaster_beam_y_sm
  * Bundle name: looter_smg-ani
  * Death animation: buffFireBurn:15
  * Factory rotation: 0
  * Factory scale factor: 1
  * Favorite target type: resource
  * Gun position: "generalpurpose_smg_rig_MASTER_MOVER/generalpurpose_smg_rig_locator_gun":1
  * Hit spark: fx_blaster_hit_y_sm
  * Icon camera position: 7.62,8.5,9.38
  * Icon lookat position: 0.18,1.32,0.32
  * Max scale: 100
  * Muzzle flash: fx_blaster_flash_y_sm
  * Name: SmugglerThief
  * Spin speed: 0
  * Targeted type: ENEMIES

|Level                      |1 |2  |3  |4  |5  |6  |7  |8  |9   |10  |
|---------------------------|--|---|---|---|---|---|---|---|----|----|
|Displayed damage per second|99|119|139|159|702|779|858|936|1014|1170|


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
|Order      |334401|334402|334403|334404|334405|334406|334407|334408|334409|334410|
|Point value|2     |2.400 |2.800 |3.200 |3.600 |4     |4.400 |4.800 |5.200 |6     |


