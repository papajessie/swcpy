# Confirmed bugs

This file tries to list confirmed bugs in units, buildings and others.

## Definitely bugs

### Prestige medic droids/repair droids

The [medic droid](Medic.html) at level 11 doesn't heal units beyond the one he locked on at level 11 (Prestige).
The [repair droid](Technician.html) at level 11 is probably affected too.

  * **Analysis:** There are missing commas in the splash damage, leading to a bizarre splash percentage that certainly doesn't extend at radius 4 like normal.
  * **Bug confirmed:** yes, by Tye Peer (JJO/J-Reb), video posted in line:SWC Quality Control on 2018-11-13 (12:13 UTC). https://www.youtube.com/watch?v=KKpv76ZfvMA
  * **Bug confirmation process:** in chapter, dropped level 11 medic near heavy + hero guy, then level 9. Level 11 heals only the heavy it is attached to. 

### Imperial IDT Traps

The [Imperial dropship trap](empireTrapDropship.html) at level 11 generates 5 stormtroopers instead of 4 heavy troopers. Only the Imperial faction suffers from this. See below for the Rebel IDT Trap.

  * **Analysis:** The [Imperial Dropship](ImperialDropship.html) called by the trap at level 11 is not the same as the [Imperial Dropship](ImperialDropshipTrap.html) at level 10 and below (they bear the same name, but have different ID). The one at level 11 is the same as the usual dropship (buildable in the factory) whereas the one called by the trap gives heavy troopers. None of these are skinnable (they are not regular or heavy troopers, even if they look very similar).
  * **Bug confirmed:** yes, multiple sources. Waiting for a timestamp and an official test. https://www.youtube.com/watch?v=Vvc7FDqrkt0&
  * **Bug confirmation process:** (not required)

### Rebel V-4X-D Ski Speeder

The [Rebel V-4X-D Ski Speeder](PolarShip.html) has a displayed damage that is going down from level 9 to level 11 (instead of up) without any other stats increasing. The calculated damage increases from level 9 to 10, but drops at level 11 (below level 7).

  * **Analysis:**
    * _displayed damage_: The displayed damage per second is computed correctly according to the current formula until level 9. The level 10 value was diminished in update 1171 (the Prestige one) so that it would seem to increase from level 10 to 11. In a posterior update, the level 11 was re-computed in version 1176 or 1177 from a wrong value to a wrong value (according to the current formula), but a bit larger (so that it would show better, possibly).
    * _computed damage_: The computed damage drops with level 11 because the shot delay is 300 ms instead of 200 ms (so the fire rate drops).
  * **Bug confirmed:** not yet
  * **Bug confirmation process:** to be done


## Design bugs

### Prestige A-Wings/TIE Advanced vs Shields

The [A-wing](AWing.html) at prestige level cannot pierce an [imperial shield](empireShieldGenerator.html).

The situation is symmetric for Empire [TIE Advanced](TieAdvanced.html) vs [rebel shields](rebelShieldGenerator.html).

  * **Analysis:** The problem is clear from the numbers. This may have been an overlook by the dev team, or a conscious design decision to make defence at level 11 easier.
  * **Bug confirmed:** yes, multiple sources. Waiting for a timestamp and an official test.

### Rebel IDT Traps

As expressed above, the [Rebel IDT trap](rebelTrapDropship.html) is only a bit healthier, costs more to rearm, but does not drop better troops.

  * **Analysis:** The [Clone Wars Gunship](CloneWarsGunshipTrap.html) was not given a level 11, so the trap is set to simply use the level 10. Other stats of the trap were increased in a seemingly sound way.
  * **Bug confirmed:** yes, multiple sources. Waiting for a timestamp and an official test.
  * **Bug confirmation process:** (not required)

### A-A5 Speeder Truck and Imperial Troop Transport : Units without a prestige level

While this may be by design, a number of playable units don't have a
prestige level.

All mercenaries, all creatures have no prestige level.

The [Rebel A-A5 Speeder Truck](RebelTransportVehicle.html) also has no prestige level, as well as the [Imperial Troop Transport](EmpireTransportVehicle.html).

  * **Analysis:** There is no prestige level. The fragment follows the same as the mercenaries for AA5 and ITT.
  * **Bug confirmed:** yes, multiple sources.
  * **Bug confirmation process:** (not required)
