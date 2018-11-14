# Confirmed bugs

This file tries to list confirmed bugs in units, buildings and others.

## Definitely bugs

### Prestige medic droids/repair droids

The [medic droid](https://papajessie.github.io/swcpy/Medic.html) at level 11 doesn't heal units beyond the one he locked on at level 11 (Prestige).
The [repair droid](https://papajessie.github.io/swcpy/Technician.html) at level 11 is probably affected too.

Analysis: There are missing commas in the splash damage, leading to a bizarre splash percentage that certainly doesn't extend at radius 4 like normal.
Bug confirmed : yes, by Tye Peer (JJO/J-Reb), video posted in line:SWC Quality Control on 2018-11-13 (12:13 UTC).
Bug confirmation process: in chapter, dropped level 11 medic near heavy + hero guy, then level 9. Level 11 heals only the heavy it is attached to. 

## Design bugs

### Prestige A-Wings/TIE Advanced vs Shields

The [A-wing](https://papajessie.github.io/swcpy/AWing.html) at prestige level cannot pierce an [imperial shield](https://papajessie.github.io/swcpy/empireShieldGenerator.html).

The situation is symmetric for Empire (TIE Advanced)[https://papajessie.github.io/swcpy/TieAdvanced.html] vs (rebel shields)[https://papajessie.github.io/swcpy/rebelShieldGenerator.html].

Analysis: 
Bug confirmed : yes, multiple sources. Waiting for a timestamp and an official test.

