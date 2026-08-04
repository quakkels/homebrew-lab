# 11 — Crystal Oscillator

- **Module:** 5 — Oscillators & Signals
- **Status:** Planned
- **Prerequisites:** [10 — Oscillators (555 & RC)](10-oscillators.md), [03 — Inductors & LC Resonance](03-inductors-and-lc-resonance.md)
- **Est. time:** ~90 min

## Objective

Build an oscillator whose frequency is set by a quartz crystal, and appreciate
why crystals give the stability and precision that RC/LC oscillators can't. This
is the conceptual bridge to how a radio knows exactly what frequency it's on.

## Concepts to be covered

- A crystal as an extremely high-Q resonator; its equivalent LC model.
- Series vs parallel resonance; load capacitance and "pulling."
- A simple Colpitts or Pierce crystal oscillator.
- Frequency stability vs temperature; why radios discipline oscillators.
- Bridge to synthesizers: how the QMX+'s Si5351 generates precise frequencies.

## Planned procedure (sketch)

- Build a single-transistor crystal oscillator; confirm oscillation on the scope
  (and, if possible, by listening on a nearby receiver).
- Measure frequency precisely; try pulling it slightly with load capacitance.
- Compare stability to the RC oscillator from Exp. 10.

## Parts & instruments

- A common crystal (e.g. a color-burst or HF crystal), 2N3904, caps, resistors,
  scope, and optionally a receiver / frequency counter.

## Why this matters (where you'll meet it)

Frequency *precision* is what makes radio possible at all. Without a stable
reference you couldn't stay on frequency or tune predictably — something you rely on
as a ham every time you dial in a band.

- **A crystal is Exp. 03's resonance taken to the extreme** — an LC resonator with
  absurdly high Q. This experiment connects the resonance idea to the real-world
  part that anchors every transmitter and receiver.
- **It demystifies the QMX+'s Si5351 synthesizer.** That chip multiplies a crystal
  reference up to any operating frequency; after this you'll know exactly what it's
  referencing and *why* the result is rock-stable.
- **Every microcontroller you'll use has one.** Your RP2040 and the QMX+'s STM32
  each have a crystal setting their clock — same part, same reason. This ties the
  radio and digital sides together.
- **"Pulling" a crystal** (nudging its frequency with a little capacitance) is the
  basis of VXOs and fine-tuning — a classic homebrew trick you'll try here.

## Log

- Measured oscillation frequency: 
- Pulling range with load capacitance: 
- Stability vs RC oscillator: 
- Surprises / questions: 
