---
title: Security Droid (SecurityDroid)
category: unit
---

# Security Droid (SecurityDroid) — version 1092

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

### Unit stats

  * Armor type: bruiserVehicle
  * Side: Empire
  * Buildable unit: Yes
  * Role: Bruiser
  * Shield cooldown: 0s
  * Shield health: 0
  * Shield range: 0
  * Unit capacity: 4
  * Type: mercenary
  * _Not found: Buff health, Can be given, Unlock planet_

|Level |1    |2    |3    |4    |5    |
|------|-----|-----|-----|-----|-----|
|Health|19200|19800|20480|21240|22080|


### Training stats

|Level        |1                                        |2                                      |3                                      |4                                      |5                                      |
|-------------|-----------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|Training time|5m45s                                    |6m43s                                  |7m47s                                  |8m57s                                  |10m13s                                 |
|Training cost|50 Con.                                  |85 Con.                                |115 Con.                               |145 Con.                               |175 Con.                               |
|Building     |[Cantina 1](empireContrabandCantina.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|


### Upgrading stats

  * Upgrade time: 5s

|Level               |1                |2                |3                |4                 |5                 |
|--------------------|-----------------|-----------------|-----------------|------------------|------------------|
|Upgrade requirements|30 data fragments|45 data fragments|75 data fragments|105 data fragments|135 data fragments|


### Move stats

  * Acceleration: 0
  * Crushes walls: No
  * Flying unit: No
  * Max speed: 20
  * Propensity to go around obstacles: 15
  * Rotation speed: 7.854
  * Run speed: 0
  * Run threshold: 0
  * Unit size on map: 1x1
  * _Not found: Ignores walls, Support follow distance_

## Main attack : Storm

### Targeting

  * Attack shield border: No
  * Max attack range: 7
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 8

### Shooting

  * Time between start of clip and first shot: 500ms
  * Clip retargeting: No
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: No
  * Time between end of clip and start of clip: 500ms
  * Retargeting offset: 10
  * Self-centered targeting: No
  * Shot count: 5
  * Time between shots: 300ms
  * Target locking: No
  * _Not found: New target on reload_

|Level          |1  |2  |3  |4  |5  |
|---------------|---|---|---|---|---|
|Damage per shot|345|388|428|468|508|


### Projectile

  * Displayed damage per second: 1920
  * _Not found: Beam damage, Splash damage percentages_

|Level                       |1      |2      |3      |4       |5       |
|----------------------------|-------|-------|-------|--------|--------|
|Calculated damage per second|784.091|881.818|972.727|1063.636|1154.545|


  * Cannons per sequence: 1
  * Cliptime: 2.200s
  * Directional: Yes
  * Is deflectable: Yes
  * Max speed: 15
  * Damage multipliers: **(100%)**: Droideka, Flying infantry, Flying vehicle, Headquarters, Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Infantry, Infantry hero, Light vehicle, Other building, Ressource generator, Shield, Shield generator, Storage, Support troop, Trap, Turret, Vehicule hero, Wall
  * Pass through shield: No
  * Salvos: 5
  * _Not found: Length segments, Width segments_

## Secondary attack : EMP Grenade

  * Auto: Yes
  * Cooldown on spawn: No
  * Supplementary time between last shot and reload: 15s
  * Description: Grenade
  * Duration: 3.500s
  * Recast ability: Yes
  * Target self: No

### Targeting

  * Max attack range: 8
  * Min attack range: 0
  * New rotation speed: 7854
  * Target preference strength: 90
  * Target preferences: **Droideka (50)**, **Flying infantry (50)**, **Flying vehicle (50)**, **Headquarters (50)**, **Heavy infantry (50)**, **Heavy vehicle (50)**, **Infantry (50)**, **Light vehicle (50)**, **Other building (50)**, **Ressource generator (50)**, **Shield (50)**, **Shield generator (50)**, **Storage (50)**, **Support troop (50)**, **Turret (50)**, Heavy infantry hero (1), Heavy vehicule hero (1), Infantry hero (1), Vehicule hero (1), Wall (1), Trap (0)
  * View range: 12
  * _Not found: Attack shield border_

### Shooting

  * Time between start of clip and first shot: 0s
  * Clip retargeting: No
  * Damage per shot: 0
  * Gun shooting sequence: 1
  * Impact delay: 1s
  * Can shoot over walls: Yes
  * Time between end of clip and start of clip: 1s
  * Retargeting offset: 12
  * Self-centered targeting: No
  * Shot count: 1
  * Time between shots: 790ms
  * Target locking: No
  * _Not found: New target on reload_

  * DPS: 0
  * Splash damage percentages: 100,100,100
  * _Not found: Beam damage_

  * Cannons per sequence: 1
  * Cliptime: 16s
  * Directional: No
  * Is deflectable: No
  * Max speed: 6
  * Secondary attack damage multipliers: **(100%)**: Droideka, Headquarters, Other building, Shield, Shield generator, Support troop, Turret, Wall, **(75%)**: Infantry, Infantry hero, Light vehicle, Vehicule hero, **(50%)**: Heavy infantry, Heavy infantry hero, Heavy vehicle, Heavy vehicule hero, Ressource generator, Storage, **(0%)**: Flying infantry, Flying vehicle, Trap
  * Pass through shield: Yes
  * Salvos: 1
  * _Not found: Length segments, Width segments_

## Other stats

### Internal stats

These stats internal to the system link different parts of data together.

  * Unit ID: SecurityDroid
  * Upgrade shard uid: shrd_troopSecurityDroid
  * _Not found: Apply buffs, Death projectile, Hero data, Self buff, Spawn apply buffs_

|Level          |1                     |2                     |3                     |4                     |5                     |
|---------------|----------------------|----------------------|----------------------|----------------------|----------------------|
|Ability        |abilitySecurityDroid1 |abilitySecurityDroid2 |abilitySecurityDroid3 |abilitySecurityDroid4 |abilitySecurityDroid5 |
|Projectile type|projectileMercGrenade1|projectileMercGrenade2|projectileMercGrenade3|projectileMercGrenade4|projectileMercGrenade5|


Internal values for secondary attack:

|Level      |1                    |2                    |3                    |4                    |5                    |
|-----------|---------------------|---------------------|---------------------|---------------------|---------------------|
|Apply buffs|buffDefenseReduction1|buffDefenseReduction2|buffDefenseReduction3|buffDefenseReduction4|buffDefenseReduction5|


### Presentation stats

These are all sorts of user interface settings, that should not interfere with gameplay.

  * Asset name: securitydroid_con-ani
  * Audio attack: "sfx_attack_blasterrifle_1":25,"sfx_attack_blasterrifle_2":25,"sfx_attack_blasterrifle_3":25,"sfx_attack_blasterrifle_4":25
  * Audio death: "sfx_death_securitydroid_01":50,"sfx_death_securitydroid_02":50
  * Audio placement: "sfx_placement_troop_1":35,"sfx_placement_troop_2":35,"sfx_placement_troop_3":30
  * Audio train: "sfx_ui_unitcomplete_securitydroid_01":100
  * Bundle name: securitydroid_con-ani
  * Event button action: galaxy
  * Event button data: planet1 planet3 planet6 planet8 planet21 planet23
  * Event button string: hn_open_galaxy
  * Event features string: fragment_obtain_gen
  * Factory rotation: 0
  * Factory scale factor: 1
  * Icon camera position: 7.57,15.79,19.1
  * Icon closeup camera position: 3.46,6.58,11.02
  * Icon closeup lookat position: -0.6,2.47,-1.47
  * Icon lookat position: -0.44,1.26,-0.82
  * Icon unlock scale: 1.1,1.1,1.1
  * Targeted type: ENEMIES
  * Unlocked by event: true
  * _Not found: Audio impact, Buff asset offset, Death animation, Decal asset name, Decal bundle name, Decal size, Effect type, Gun position, Hologram uid, Icon unlock position, Icon unlock rotation, Info UI type, Shield asset name, Spawn effect uid, Tooltip height offset, UI decal asset name, Unlocked by campaign, Unlocked by tournament_

### Attack presentation stats

### Secondary attack presentation stats

  * Alt gun locators: 1
  * Animation delay: 810
  * Audio ability activate: "sfx_attack_securitydroid_ability_01":100
  * Audio ability attack: "sfx_explosion_sonicgrenade_01":34,"sfx_explosion_sonicgrenade_02":33,"sfx_explosion_sonicgrenade_03":33
  * Displayed damage per second: 75
  * Favorite target type: generic
  * Name: SecurityDroidSpecial
  * Persistent scaling: 0
  * Arcs: Yes
  * Bullet: fx_grenade_emp_projectile
  * Hit spark: fx_grenade_sonic_hit_01
  * Max scale: 300
  * Name: EMP Grenade
  * Spin speed: 0
  * _Not found: Audio ability loop, Charge asset name, Ground bullet, Muzzle flash, Muzzle flash fade time, Persistent effect, Projectile length, S transition, Weapon trail FX params_

### Uninterpreted stats

Seriously, we don't really know what to do with these.

  * Auto spawn rate scale: 1
  * Auto spawn spreading scale: 1
  * Max scale: No
  * Point value: 4
  * Splash: 0
  * Target in range modifier: 1
  * Xp: 0

|Level|1     |2     |3     |4     |5     |
|-----|------|------|------|------|------|
|Order|115601|115602|115603|115604|115605|


### Uninterpreted attack stats

  * Arming delay: 0
  * Seeks target: Yes
  * Streams: no
  * Strict cool down: No
  * _Not found: S1 time, S2 time_

### Uninterpreted secondary attack stats

  * Arming delay: 0
  * Clip count: 1
  * Kill cooldown reset: No
  * Max speed: 20
  * Strict cool down: Yes
  * Seeks target: No
  * Streams: no
  * _Not found: S1 time, S2 time_

