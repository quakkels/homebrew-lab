# 13 — Mixers & Detectors

- **Module:** 6 — RF Fundamentals
- **Status:** Planned
- **Prerequisites:** [12 — LC Filters & Impedance Matching](12-lc-filters-and-impedance-matching.md), [11 — Crystal Oscillator](11-crystal-oscillator.md)
- **Est. time:** ~2–3 hours

## Objective

Learn the two operations at the heart of every radio: **detection** (recovering
information from a carrier) and **mixing** (shifting a signal to a new
frequency). Build a simple receiver front end and understand the quadrature
sampling detector the QMX+ uses.

## Concepts to be covered

- Envelope detection (the crystal-radio diode detector) — reuses Module 2 diodes.
- Mixing = multiplication → sum and difference frequencies; the superhet idea.
- Direct-conversion receivers; I/Q and the **quadrature sampling detector (QSD)**.
- How a switching mixer + op-amp + DSP becomes an SDR (i.e., the QMX+ receiver).
- Image frequencies and why filtering (Exp. 12) precedes mixing.

## Planned procedure (sketch)

- Build a diode envelope detector / crystal-radio front end and hear a station.
- Build or simulate a simple mixer; observe sum/difference products on the scope
  or an SDR waterfall.
- Trace the QMX+ receive path on its schematic block by block using what you've built.

## Parts & instruments

- Diodes, a switching mixer IC or FET switch, LC filters from Exp. 12, an antenna,
  scope and/or an SDR dongle for a spectrum view.

## Why this matters (where you'll meet it)

These are **the two operations at the heart of every radio**: *detection* (getting
the information back out of a carrier) and *mixing* (shifting a signal to a new
frequency). Understand these two and radios stop being magic.

- **You'll hear where radio began.** A diode envelope detector recovers audio from
  a station with almost no parts — connect it to one of your antennas and listen.
  It's a direct line from a crystal set to a modern SDR.
- **Mixing is the superheterodyne principle** behind essentially every receiver
  built since the 1930s: multiply two signals, get their sum and difference, and
  shift a station down to a frequency you can process.
- **The QSD is the QMX+'s (and every SDR's) front end.** The quadrature sampling
  detector and I/Q signals you meet here are exactly how your radio's receiver
  works — this experiment is what makes its schematic *readable* to you.
- **Payoff:** after this, the whole QMX+ receive path is legible, stage by stage —
  the stated goal of the entire RF module, and the moment your ham hobby and your
  circuit knowledge fully merge.

## Log

- Envelope detector — station heard / signal recovered: 
- Mixer sum & difference frequencies observed: 
- QMX+ receive-path stages identified: 
- Surprises / questions: 
