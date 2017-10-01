---
title: The units stats explained
---
# Units stats

This is an explanation as far as we know (since we do not have access to the source code of the application). Stats can be found in the [units descriptions](unit.html).

## Main stats

  * **Side:** Empire, Rebel, or a few others, but basically all others mean "neutral". Most others are used in PvE scenarios.
  * **Buildable unit:** Some units are buildable by players of the correct side, some others can only be obtained as gifts (or in PvE). Be aware that some non-buildable units look like other units equipment, but they are not the same (esp. they would work on Sullust, if someone got some in inventory).
  * **Type:** the unit can either be a droideka (_champion_), a hero, infantry, vehicle or mercenary.
  * **Armor type:** this is the value used to determine the damage multiplier when the unit is attacked.
  * **Role:** this value is used in game to describe the behaviour of the unit. However, this behaviour is actually set by other parameters.
  * **Levels available:** usually 1-10, but others value can be found.
  * **Unit capacity:** the space occupied by the unit in the transports (except of heroes and droidekas, which do not count).
  * **Upgrade time** and **Upgrade requirements:** the various things required to upgrade the unit _to_ the indicated level (not _from_ the corresponding level).
  * **Shield health:** the health of the shield (obviously). Remark that the value show in-game is wrong.
  * **Shield range:** the size of the shield _(unsure)_.
  * **Shield cooldown:** the time after which a still and untouched shield goes up again (with full health).
  * **Damage:** This is the value displayed in-game for the damage, and it is supposed to be the damage per second of the unit. However, it comes in fact from other parameters. It may be correct, but for some units is not. See below for [the damage explanation](#damage)
  * **Damage per shot:** This is the damage per shot for the damage. This one is correct. See below for [the damage explanation](#damage)

## Targeting

All these numbers refer to how the unit shoots at others and especially
how it chooses its target. If a unit has no target, it will pick
one. Basically, if there are only targets in view range, then the
strongest target preference indicate which unit is picked (if there is
an equality, the closest is taken). If the preferred target is out of
view range, then the preference is reduced by an unknown formula, but
where the target in range modifier and the target preference strength
play a role.

  * **Target preferences:** this is an ordered list of the basic preferences of the unit as target.
  * **View range:** see above.
  * **Target preferences strength:** see above.
  * **Max. range:** maximal distance at which the unit can shoot.
  * **Min. range:** minimal distance at which the unit can shoot.
  * **overWalls:** whether the unit can shoot over walls or not.
  * **Targeted type:** tells about selecting enemies or allies (support units, for example).
  * **Retargeting offset:** role unknown, probably related to distance and retargetting _(unsure)_
  * **clipRetargeting:** whether or not the unit will try to pick a better target at the end of a clip (or only when the current target is destroyed).
  * **Target shield border:** whether the unit will target the shield border instead of targeting something inside the shield (eg. shield busters such as ATAT or juggernauts).
  * **Self-centered targeting:** whether the unit "shoots" all around itself (used mostly for support troops, for their beneficial effect). _(unsure, possibly just another name for Target locking)_

## Movement

TBD

  * **Target locking:** whether the unit locks its movement to its target. Used especially for support units.

## Damage

TBD

## Presentation

A lot of stats refer to the graphics or audio or other minor details of
the unit that don't influence the unit behaviour at all. They will not
be listed here.