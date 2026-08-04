# 06 — Transistor as a Switch

- **Module:** 3 — Transistors
- **Status:** Planned
- **Prerequisites:** [04 — Diodes & Rectification](04-diodes-and-rectification.md)
- **Est. time:** ~75 min

## Objective

Use a transistor to let a small signal control a large current — the "switch"
mode. Do it with both a BJT (2N3904) and a MOSFET (2N7000) and compare. This is
the most software-intuitive transistor use and directly feeds the keyboard build.

## Concepts to be covered

- BJT saturation: base current controls collector current; `V_CE(sat)`.
- MOSFET: voltage-controlled; gate threshold; why it's the modern default.
- Driving an LED / relay / small load; the base resistor and why it's needed.
- Flyback diode for inductive loads (relay) — reuses the diode from Module 2.
- Switching speed on the scope (rise/fall) — preview of class-D/E PA in the QMX+.

## Planned procedure (sketch)

- BJT LED driver; measure base vs collector current, confirm saturation.
- MOSFET version; compare gate drive and on-resistance.
- Switch a relay with a flyback diode; view the inductive spike with/without it.

## Parts & instruments

- 2N3904, 2N7000, LEDs, resistors, a small relay, 1N4148 flyback diode, scope.

## Why this matters (where you'll meet it)

The transistor-as-switch is the **atom of everything digital**. Every logic gate
in the RP2040 and STM32 you'll use is just transistors switching on and off — so
as a software engineer, this is the literal hardware sitting under all your
abstractions.

- **Control anything a microcontroller pin can't drive directly:** relays, motors,
  LED strips, higher-power loads, band-switching in a radio. A GPIO can nudge a
  transistor; the transistor does the muscle work.
- **Keyboard:** driving key-scan lines and indicator LEDs is GPIO-as-switch — this
  is a direct prerequisite for that build.
- **The QMX+ PA is this idea at speed.** Its class-D/E power amplifier is
  transistors switching *hard* to make RF power efficiently — this experiment is
  the seed of understanding how a switching amplifier works.
- **The flyback-diode lesson prevents mystery failures.** Switching anything with
  a coil (relay, motor) produces a destructive inductive spike; you'll *see* it on
  the scope and learn the one diode that tames it — a reliability must-know.
- **BJT vs MOSFET** teaches you which to reach for and why modern designs favor
  MOSFETs (voltage-controlled, low on-resistance).

## Log

- BJT: base current vs collector current at saturation: 
- Inductive spike with vs without flyback diode: 
- Surprises / questions: 
