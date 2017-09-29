---
title: Speeder Bike (EmpireSpeeder)
category: unit
---

# Speeder Bike (EmpireSpeeder) — version 1085

You can read an [explanation  of the various unit stats](unitexplained.md).

## Main stats

  * Side: Empire
  * Buildable unit: Yes
  * Type: vehicle
  * Armor type: vehicle
  * Role: Striker
  * Levels available: 1-10
  * Unit capacity: 6
  * Shield Health: 0
  * Shield Cooldown: 0s
  * Shield Range: 0

|Level               |1   |2    |3    |4     |5     |6      |7      |8      |9       |10      |
|--------------------|----|-----|-----|------|------|-------|-------|-------|--------|--------|
|Upgrade requirements|500$|3000$|6000$|15000$|35000$|115000$|175000$|350000$|1000000$|2000000$|
|Upgrade time        |0s  |30m  |1h30m|5h    |10h   |1d12h  |2d12h  |4d     |6d      |1w2d    |
|Health              |9240|10120|11090|12170 |13360 |14690  |16160  |17790  |19610   |21640   |
|Damage*             |970 |1030 |1100 |1170  |1250  |1330   |1420   |1520   |1620    |1730    |
|Damage per second*  |920 |980  |1050 |1110  |1190  |1270   |1620   |1740   |1850    |1980    |

* These values are not necessarily accurate and may be inconsistent with other values

## Targeting

  * Target preferences: **Flying vehicle (70)**, **Infantry (70)**, **Heavy vehicle (70)**, **Flying infantry (70)**, **Droideka (70)**, **Heavy infantry (70)**, **Light vehicle (70)**, **Support troop (70)**, Shield generator (50), HQ (50), Other building (50), Shield (50), Turret (50), Storage (50), Ressource generator (50), Retargeting offset (12), Heavy vehicular hero (1), Infantry hero (1), Heavy infantry hero (1), Vehicle hero (1), Wall (1), Trap (0)
  * Targeted type: ENEMIES
  * View Range: 8
  * Target preferences strength: 90
  * Retargeting offset: 12
  * Clip retargeting: Yes
  * Target shield border: No
  * Max. Range: 6
  * Min. Range: 0
  * Can shoot over walls: No
  * Self-centered targeting: No

## Recruiting

|Level        |1                              |2                                      |3                                      |4                                      |5                                      |6                                      |7                                      |8                                      |9                                      |10                                      |
|-------------|-------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
|Training cost|420$                           |480$                                   |540$                                   |660$                                   |780$                                   |900$                                   |1020$                                  |1200$                                  |1260$                                  |1380$                                   |
|Training time|66                             |67                                     |69                                     |72                                     |75                                     |78                                     |81                                     |168                                    |174                                    |180                                     |
|Building     |[Factory 1](empireFactory.html)|[Research Lab 2](empireOffenseLab.html)|[Research Lab 3](empireOffenseLab.html)|[Research Lab 4](empireOffenseLab.html)|[Research Lab 5](empireOffenseLab.html)|[Research Lab 6](empireOffenseLab.html)|[Research Lab 7](empireOffenseLab.html)|[Research Lab 8](empireOffenseLab.html)|[Research Lab 9](empireOffenseLab.html)|[Research Lab 10](empireOffenseLab.html)|

## Movement

  * Run speed: 0
  * Run Threshold: 0
  * Size: 1x2
  * Flying unit: No
  * Crushes walls: No
  * Target locking: No

|Level       |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|
|------------|--|--|--|--|--|--|--|--|--|--|
|Speed       |40|40|40|40|40|40|80|80|80|80|
|Acceleration|0 |0 |0 |0 |0 |0 |8 |8 |8 |8 |

## Presentation stats

These graphical elements shouldn't interfere with gameplay and can safely be ignored.

  * newRotationSpeed: 3927
  * audioAttack: "sfx_attack_empire_mtv7_1":25,"sfx_attack_empire_mtv7_2":25,"sfx_attack_empire_mtv7_3":25,"sfx_attack_empire_mtv7_4":25
  * audioPlacement: "sfx_placement_empire_mtv7_1":50,"sfx_placement_empire_mtv7_2":50
  * gunPosition: "speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_locator_gun1":1,"speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_MASTER_MOVER/speederbike_emp_rig_locator_gun2":1
  * audioDeath: "sfx_death_empire_mtv7_1":33,"sfx_death_empire_mtv7_2":33,"sfx_death_empire_mtv7_3":34
  * factoryRotation: 0
  * assetName: speederbike_emp-ani
  * rotationSpeed: 3.92698750000000007531752999057061970233917236328125
  * buffAssetOffset: 0,1,0
  * animationDelay: 0
  * bundleName: speederbike_emp-ani
  * factoryScaleFactor: 1
  * iconCameraPosition: 14.03,11.98,20.6
  * iconLookatPosition: -0.26,1.18,-0.59

## Uninterpreted stats

  * impactDelay: 0
  * maxScale: false
  * shotDelay: 0
  * autoSpawnSpreadingScale: 2
  * pathSearchWidth: 15
  * splash: 0
  * armingDelay: 0
  * gunSequence: 1,1
  * favoriteTargetType: infantry
  * chargeTime: 250
  * strictCoolDown: false
  * autoSpawnRateScale: 2
  * targetInRangeModifier: 1
  * xp: 0

|Level         |1                      |2                      |3                      |4                      |5                      |6                      |7                             |8                             |9                             |10                            |
|--------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|------------------------------|------------------------------|------------------------------|------------------------------|
|order         |130101                 |130102                 |130103                 |130104                 |130105                 |130106                 |130107                        |130108                        |130109                        |130110                        |
|shotCount     |1                      |1                      |1                      |1                      |1                      |1                      |2                             |2                             |2                             |2                             |
|projectileType|projectileEmpireSpeeder|projectileEmpireSpeeder|projectileEmpireSpeeder|projectileEmpireSpeeder|projectileEmpireSpeeder|projectileEmpireSpeeder|projectileEmpireSpeederUpgrade|projectileEmpireSpeederUpgrade|projectileEmpireSpeederUpgrade|projectileEmpireSpeederUpgrade|
|reload        |800                    |800                    |800                    |800                    |800                    |800                    |625                           |625                           |625                           |625                           |
|pointValue    |6.000                  |7.200                  |8.400                  |9.600                  |10.800                 |12.000                 |13.200                        |14.400                        |15.600                        |18.000                        |

