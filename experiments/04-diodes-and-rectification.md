# 04 — Diodes & Rectification

**Module:** 2 — Diodes & Power
**Status:** Planned
**Prerequisites:** [02 — RC Filters](02-rc-filters.md)
**Est. time:** ~60 min

## Objective

Understand the diode as a one-way valve, see its forward voltage drop, and use
diodes to turn AC into pulsating DC (half-wave and full-wave rectification).

## Concepts to be covered

- Diode I–V curve, the ~0.6–0.7 V forward drop (Si) vs ~0.2–0.3 V (Schottky).
- Half-wave, full-wave (bridge) rectification.
- Adding a reservoir capacitor → ripple; how RC (Exp. 01/02) sets ripple size.
- Diode as a protection/steering element (feeds the keyboard matrix idea).

## Planned procedure (sketch)

- Measure forward drop with the multimeter diode-test and on the scope's I–V.
- Rectify the generator's sine; view half-wave, then a bridge, on the scope.
- Add a smoothing cap and measure ripple with AC coupling; relate to RC.

## Parts & instruments

- 1N4148, 1N4007, 1N5817 Schottky, resistors, caps, signal source, scope.

## Why this matters (where you'll meet it)

The diode is the simplest device that *does* something nonlinear — a one-way valve
for current — and that one trick shows up in a surprising number of places.

- **Every power supply starts here.** Turning AC into DC (rectification) is step
  one of Exp. 05 and of literally every mains-powered device you'll build or repair.
- **It's how radio began.** A diode "envelope detector" is the entire front end of
  a crystal radio — you'll build one in Exp. 13 and recover audio from a carrier
  with almost no parts. Detection is one of the two core radio operations.
- **Steering and protection.** Diodes block current going the wrong way — which is
  exactly what stops "ghosting" in your **keyboard matrix**, protects circuits from
  a reversed battery, and tames the inductive spike from a relay (the flyback
  diode in Exp. 06).
- **Repair win.** A shorted or open rectifier diode is one of the most common
  faults in dead gear; the diode-test on your multimeter finds it in seconds.
- **A number you'll carry forever:** the ~0.6–0.7 V silicon forward drop becomes a
  mental landmark you'll use to sanity-check circuits at a glance.

## Log

- Measured forward drops (Si vs Schottky): 
- Ripple vs reservoir cap value: 
- Surprises / questions: 
