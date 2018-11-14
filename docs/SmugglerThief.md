---
title: Mercenary Thief (SmugglerThief)
category: unit
---

# Mercenary Thief (SmugglerThief)

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

|Level |10  |9   |8   |7   |6   |5   |4  |3  |2  |1  |
|------|----|----|----|----|----|----|---|---|---|---|
|Health|7200|6240|5760|5280|4800|4320|800|700|600|500|


### Training stats

|Level        |10                                  |9                                  |8                                  |7                                  |6                                  |5                                  |4                                  |3                                  |2                                  |1                                  |
|-------------|------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
|Training time|1m                                  |58s                                |56s                                |54s                                |52s                                |50s                                |48s                                |46s                                |44s                                |42s                                |
|Training cost|460$                                |420$                               |380$                               |340$                               |300$                               |260$                               |220$                               |180$                               |140$                               |100$                               |
|Building     |[Barracks 10](smugglerBarracks.html)|[Barracks 9](smugglerBarracks.html)|[Barracks 8](smugglerBarracks.html)|[Barracks 7](smugglerBarracks.html)|[Barracks 6](smugglerBarracks.html)|[Barracks 5](smugglerBarracks.html)|[Barracks 4](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|[Barracks 3](smugglerBarracks.html)|


### Upgrading stats

  * Upgrade time: 0s

|Level               |10      |9       |8      |7      |6      |5     |4     |3     |2    |1    |
|--------------------|--------|--------|-------|-------|-------|------|------|------|-----|-----|
|Upgrade requirements|4000000$|2000000$|750000$|200000$|100000$|50000$|24000$|14000$|5000$|1500$|


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

|Level             |5-10                                                                                                                                                                                                                                                                                                                                                                                                             |1-4                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Target preferences|**Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy infantry hero (50), Heavy vehicle (50), Heavy vehicule hero (50), Infantry (50), Infantry hero (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Vehicule hero (50), Wall (1), Trap (0)|**Ressource generator (80)**, **Storage (80)**, Droideka (50), Flying infantry (50), Flying vehicle (50), Headquarters (50), Heavy infantry (50), Heavy vehicle (50), Infantry (50), Light vehicle (50), Other building (50), Shield (50), Shield generator (50), Support troop (50), Turret (50), Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)|


### Shooting

  * Animation delay: 0s
  * Charge time: 250ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 0s
  * Can shoot over walls: No
  * Reload time: 800ms
  * Retargeting offset: 100
  * Self-centered targeting: No
  * Shot count: 1
  * Shot delay: 0s
  * Target locking: No

|Level          |10  |9   |8  |7  |6  |5  |4  |3  |2  |1  |
|---------------|----|----|---|---|---|---|---|---|---|---|
|Damage per shot|1229|1065|983|901|819|738|168|147|126|105|


### Projectile

|Level                       |10  |9   |8  |7  |6  |5  |4  |3  |2  |1  |
|----------------------------|----|----|---|---|---|---|---|---|---|---|
|Displayed damage per second |2310|1014|936|858|779|702|159|139|119|99 |
|Calculated damage per second|1170|1014|936|858|780|702|160|140|120|100|
|Calculated damage per cycle |1229|1065|983|901|819|738|168|147|126|105|


  * Cannons per sequence: 1
  * Shooting cycle duration: 1.050s
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

|Level                      |10  |9   |8  |7  |6  |5  |4  |3  |2  |1 |
|---------------------------|----|----|---|---|---|---|---|---|---|--|
|Displayed damage per second|2310|1014|936|858|779|702|159|139|119|99|


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

|Level      |10    |9     |8     |7     |6     |5     |4     |3     |2     |1     |
|-----------|------|------|------|------|------|------|------|------|------|------|
|Order      |461710|461709|461708|461707|461706|461705|461704|461703|461702|461701|
|Point value|6     |5.200 |4.800 |4.400 |4     |3.600 |3.200 |2.800 |2.400 |2     |


