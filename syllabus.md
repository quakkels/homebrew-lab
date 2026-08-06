# Homebrew Lab — An Electronics Curriculum

A self-directed, bench-driven course in electronics, built around one idea: **you learn analog by *seeing* it on a scope.** Every experiment ends with a measurement you make yourself and a number that matches (or surprises) the theory.

## Who this is for (me)

- Software engineer — digital logic and microcontrollers will come easily.
- Amateur radio operator, US General class — already fluent in some RF concepts (frequency, resonance, antennas, transmission lines).
- Has built breadboard circuits and soldered perf boards; built antennas.
- Owns a **QRP Labs QMX+** transceiver kit (the flagship radio build).
- **The real gap to close:** *analog intuition* — component feel, reading signals on a scope, and the connective tissue (filters, impedance, biasing) between "I can follow a schematic" and "I can design one."

## Goals this curriculum serves

1. **Fundamentals** — understand *why* circuits work, not just how to copy them.
2. **Fun projects** — ship things that work and are satisfying to build.
3. **Repair / hardware hacking** — read schematics, probe live circuits, modify.
4. **Two flagship builds:** a **keyboard from scratch** and the **QMX+ homebrew radio** (build it, align it, and understand every stage).

## How to use this course

Each experiment follows the same loop:

> **Build → Observe → Explain → Log**

You build the circuit, observe it on the scope, I explain what you saw and why, and you record your measurements in the **Log** section of that experiment's file. The log is the point — it's your evidence that the theory is real, and a notebook you'll refer back to.

- Every experiment file is a complete lesson: objective, the *why*, a step-by-step procedure with wiring diagrams, what to look for, the "aha," and a Log to fill in.
- Do experiments roughly in order — later ones assume the intuition from earlier ones. The two project tracks branch off once their prerequisites are met.

## Pacing & expectations

**A menu, not a queue.** The experiments cost nothing until you run them. The curriculum is a set of doors to open when ready, not a backlog. It keeps indefinitely — set it down for a month and it resumes exactly where it stopped.

**One session a week is a real, sustainable pace.** At roughly one solid bench session most weeks, the fundamentals take months, not weeks — and that's the intended tempo, not a slow one.

**Bench hours understate calendar time.**

| Chunk | Bench hours | Rough calendar (~1 session/week) |
|---|---|---|
| Experiments 00–14 | ~25–35 h | ~4–7 months |
| Keyboard project | ~20–40 h | KiCad has a real learning curve |
| QMX+ build & understanding | ~20–40 h | a weekend-plus to build, more to *understand* |

Every session carries overhead — set up, re-orient, tear down, write the log — so a "90-minute" experiment is often a 2-hour evening. **The whole arc, both flagship projects included, is realistically a 12–18-month part-time journey.**

**Consolidation is a feature, not a delay.** The intuition this course targets often clicks a few days *after* an experiment rather than during it. One experiment a week, absorbed, beats a cram — depth here comes from spacing, not speed.

**Payoffs arrive before the "end."** The projects don't require finishing all 15 experiments first — the keyboard branches off around Module 7 and the QMX+ off Module 6 — so rewarding milestones come well before the finish line.

**Is this college-equivalent?** In breadth, roughly a first circuits course plus an intro RF/communications course — one to two semesters of an EE program's analog/RF core. It deliberately skips most of the *mathematical machinery* (differential equations, semiconductor physics, electromagnetics) that a degree wraps around the same topics. But it's inverted in emphasis: it's **lab-first**, so it builds bench instinct — reading a scope, debugging a real board — that coursework often underdevelops. It is not a substitute for the credential; the gap a degree would additionally cover is the math and device theory.

## Equipment

**Have:** oscilloscope (probes compensated), multimeter, breadboard, soldering iron, and a **QRP Labs QMX+** kit.

**Need (starter passives kit, ~$20):** assorted 1/4 W resistors, ceramic + electrolytic capacitors, common diodes (1N4148, 1N4007), a few LEDs, an assortment of NPN transistors (2N3904) and an N-channel MOSFET (2N7000), an LM358 op-amp, an NE555, and a handful of inductors. Detailed bill of materials lives in [`experiments/00-bench-and-instrumentation.md`](experiments/00-bench-and-instrumentation.md).

**Nice to have later:** bench power supply, function/signal generator (a cheap DDS module or the AD9833 is fine), an LC meter, and a **NanoVNA** — superb for the RF modules and for aligning/characterizing the QMX+ filters (and you'll appreciate it as a ham).

## The progression

### Module 0 — The Bench
Set up the workspace, master the scope as a *learning tool*, and inventory parts.
- [00 — Bench & Instrumentation](experiments/00-bench-and-instrumentation.md)

### Module 1 — Passives & Time (the DNA of everything)
Capacitors and inductors in the time and frequency domains. This is the foundation the whole course — and all of radio — is built on.
- [01 — The RC Time Constant](experiments/01-rc-time-constant.md)
- [02 — RC Filters (low-pass & high-pass)](experiments/02-rc-filters.md)
- [03 — Inductors & LC Resonance](experiments/03-inductors-and-lc-resonance.md)

### Module 2 — Diodes & Power
Rectification and turning AC into clean DC — every project needs power.
- [04 — Diodes & Rectification](experiments/04-diodes-and-rectification.md)
- [05 — A Linear Power Supply](experiments/05-linear-power-supply.md)

### Module 3 — Transistors (the amplifier and the switch)
The active device everything else is made of. Switch first (feeds the keyboard), then amplifier.
- [06 — Transistor as a Switch](experiments/06-transistor-as-switch.md)
- [07 — Transistor as an Amplifier](experiments/07-transistor-as-amplifier.md)

### Module 4 — Op-Amps
The analog building block that makes design *easy*. Gain, buffering, active filters.
- [08 — Op-Amp Fundamentals](experiments/08-op-amp-fundamentals.md)
- [09 — Active Filters](experiments/09-active-filters.md)

### Module 5 — Oscillators & Signals
Making signals instead of just measuring them. Timers, RC oscillators, crystals.
- [10 — Oscillators (555 & RC)](experiments/10-oscillators.md)
- [11 — Crystal Oscillator](experiments/11-crystal-oscillator.md)

### Module 6 — RF Fundamentals (familiar ham territory, deeper)
Where ham knowledge and the analog fundamentals converge — and where the QMX+ blocks come from. Resonant filters, impedance, matching, and the two operations at the heart of every radio.
- [12 — LC Filters & Impedance Matching](experiments/12-lc-filters-and-impedance-matching.md)
- [13 — Mixers & Detectors](experiments/13-mixers-and-detectors.md)

### Module 7 — Digital & Embedded (leverages a software background)
Logic, microcontrollers, and firmware — the on-ramp to the keyboard build.
- [14 — Digital Logic & Microcontrollers](experiments/14-digital-logic-and-microcontrollers.md)

## Project tracks

These are the flagship builds. Each branches off the modules once its prerequisites are met, and has its own phased brief.

- [**Keyboard from scratch**](projects/keyboard/README.md) — matrix scanning, diodes, an RP2040, KiCad PCB, QMK/ZMK firmware. Branches off **Module 7** (with diode/switch intuition from Modules 1–3).
- [**QMX+ homebrew radio**](projects/radio/README.md) — build, test, align, and *understand* the QRP Labs **QMX+**, block by block (band-pass filters → quadrature sampling detector → SDR/DSP on the STM32 → class-D/E PA → low-pass filters), then branch into scratch-built experimental stages. Branches off **Module 6**.

## Reference library

- **ARRL Handbook** — theory to homebrew, in a ham's language.
- **Practical Electronics for Inventors** (Scherz & Monk) — best hobbyist bridge book.
- **The Art of Electronics** (Horowitz & Hill) — the reference bible; dense.
- **EMRFD** (*Experimental Methods in RF Design*) — the homebrew-radio classic.
- **QRP Labs QMX+ assembly & operating manuals** — the primary reference for the radio track.
- **W2AEW** (YouTube) — scope-driven, ham-oriented tutorials.
- **Ben Eater** (YouTube) — breadboard digital, perfect for software folks.
- **AllAboutCircuits.com** — free online textbook.
