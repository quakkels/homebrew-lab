# 05 — A Linear Power Supply

- **Module:** 2 — Diodes & Power
- **Status:** Planned
- **Prerequisites:** [04 — Diodes & Rectification](04-diodes-and-rectification.md)
- **Est. time:** ~90 min

## Objective

Build a complete rectify → smooth → regulate chain and produce clean, stable DC.
Measure how much a regulator improves ripple and load stability.

## Concepts to be covered

- The full chain: transformer/AC source → bridge → reservoir cap → regulator.
- Linear regulator (78L05) basics: dropout, quiescent current, heat.
- Line and load regulation; measuring ripple rejection.
- Decoupling capacitors and *why* every IC gets one (ties back to RC).

## Planned procedure (sketch)

- Build a 5 V supply from an AC or higher-DC source.
- Measure ripple before and after the regulator (AC coupling on the scope).
- Vary the load and watch output hold steady; find the dropout point.

## Parts & instruments

- Bridge diodes/1N4007, reservoir + decoupling caps, 78L05, load resistors, scope.

## Why this matters (where you'll meet it)

Power is the most *universal* topic in electronics — every single thing you build,
repair, or hack has a power supply, and a shockingly large fraction of the skill
is in that one subsystem.

- **Repair / hardware-hacking — the single highest-yield skill.** A huge share of
  dead consumer electronics are dead *power supplies*: a bulged electrolytic cap,
  a failed regulator, a cracked solder joint on the rectifier. Once you can look
  at a supply and reason "rectifier → reservoir cap → regulator," you can revive a
  lot of "broken" gear that others throw away. This experiment is the mental model
  behind those repairs.
- **RF, specifically — supply noise becomes signal.** On a receiver, ripple and
  supply noise show up as audible hum, whine, or "birdies"; on a transmitter, they
  become spurious emissions that put junk on the air. A clean supply is a
  *performance* feature in radio, not just a housekeeping detail — the QMX+ cares
  a great deal, and so will anything you homebrew.
- **Decoupling capacitors — the "why is there a 100 nF next to every chip?"**
  This experiment answers that. It's the same RC idea from Exp. 01/02 acting as a
  local energy reservoir, and getting it wrong causes maddening intermittent bugs.
- **A scope skill you'll reuse constantly:** measuring small ripple riding on a
  big DC level using **AC coupling**. That "look at the tiny wiggle on top of the
  steady voltage" move comes up everywhere.
- **Foundation for what's next:** understanding a *linear* regulator is the
  stepping stone to switching supplies (buck/boost) — the things inside every USB
  charger and the 3.3 V rail on your future keyboard.

## Log

- Ripple before/after regulator: 
- Dropout voltage observed: 
- Surprises / questions: 
