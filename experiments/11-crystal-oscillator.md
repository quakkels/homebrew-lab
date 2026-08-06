# 11 — Crystal Oscillator

- **Module:** 5 — Oscillators & Signals
- **Prerequisites:** [10 — Oscillators (555 & RC)](10-oscillators.md), [03 — Inductors & LC Resonance](03-inductors-and-lc-resonance.md)
- **Est. time:** ~90 min

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Build an oscillator whose frequency is set by a **quartz crystal**, confirm it on the scope, and prove — by warming it and by "pulling" it — why a crystal holds a frequency that an RC or LC oscillator never could. This is the bridge to how a radio knows exactly what frequency it's on.

## Concepts introduced

- A crystal as an **extremely high-Q resonator** — Experiment 03's LC resonance taken to a ridiculous extreme (Q in the tens of thousands).
- The crystal's equivalent circuit; **series vs. parallel** resonance and **load capacitance**.
- A single-transistor **Colpitts** crystal oscillator.
- **Pulling** (nudging the frequency slightly) and why crystals barely drift.

## Parts & instruments

- A common crystal — a **3.579545 MHz** "color-burst" crystal is cheap and ideal
- 1 × **2N3904**, resistors: **100 kΩ**, **10 kΩ**, **1 kΩ**
- Caps: 2 × **100 pF** (Colpitts feedback), **10 nF** (decoupling), a small **trimmer or 33 pF** for pulling
- 9 V supply, scope (≥ ~20 MHz bandwidth helps), optionally an AM/SW receiver or frequency counter

## Background (the why)

An RC oscillator's frequency depends on resistor and capacitor values that drift with temperature, age, and voltage — you *watched* a 555 wander in Experiment 10. For radio that's fatal: drift of even a few parts per million smears your signal across the band. The fix is a resonator with **enormous Q** — one so sharp it essentially refuses to oscillate at any frequency but its own.

**A quartz crystal is that resonator.** Quartz is piezoelectric: squeeze it and it makes a voltage; apply a voltage and it flexes. A thin slab of it has a mechanical resonance so precise and low-loss that, electrically, it looks like an LC circuit with a **Q of 10,000–100,000** (compare your hand-wound tank's Q of ~20). Its equivalent circuit is a very large "motional" inductance in series with a tiny capacitance, giving:

- a **series-resonant** frequency where it looks like a small resistance, and
- a **parallel-resonant** frequency a hair higher (set with the circuit's **load capacitance**).

Because that inductance and capacitance are properties of a *physical quartz crystal*, not of drifty R's and C's, the frequency barely moves — typically tens of parts per million over a wide temperature range. That stability is the whole reason you can dial up 14.060 MHz and actually be there.

**Pulling.** You can nudge the frequency a *tiny* bit by changing the load capacitance (a series trimmer). That's the basis of a VXO (variable crystal oscillator) and of how a synthesizer's reference gets trimmed exactly onto frequency.

## Procedure

### Part A — Build a Colpitts crystal oscillator

1. Bias a 2N3904 like a normal amplifier stage: **100 kΩ** from +9 V to base, **10 kΩ** base to ground, **1 kΩ** emitter to ground, collector to +9 V through a small choke or straight (this simple form runs the collector to +9 V and takes output at the emitter). Decouple the supply with 10 nF.
2. Form the Colpitts feedback network: the **crystal** from collector/base node into the feedback path, with the two **100 pF** caps forming the capacitive divider from the transistor's output back to its input, their junction to the emitter. (Follow a standard Colpitts crystal oscillator diagram — the crystal replaces the inductor of a normal Colpitts.)
3. Power up and probe the output with the scope. You should see a **sine-ish oscillation at ~3.58 MHz**. If it won't start, tweak the emitter resistor or the feedback caps.

### Part B — Measure it precisely

4. Read the frequency on the scope (or a counter). It should sit within a **few hundred Hz** of 3.579545 MHz — that's ~0.01%, far tighter than anything RC.
5. If you have a shortwave receiver, tune near 3.58 MHz and listen for the carrier (or its harmonics on higher bands) to confirm it's really there and steady.

### Part C — Prove the stability (warm it and pull it)

6. **Warm it:** pinch the crystal (or the transistor) between your fingers, as you did in Experiment 07. The frequency shifts only slightly — orders of magnitude less than the 555 drifted. *This* is what high Q buys.
7. **Pull it:** put the trimmer/33 pF in series with the crystal and adjust. Watch the frequency move a small, controllable amount, then return. You've just built the core of a VXO.

## What to observe / measure

- A clean ~3.58 MHz oscillation that starts on its own.
- Measured frequency within a tiny fraction of a percent of the marked value.
- Warming produces a barely-perceptible shift (vs. the obvious drift of the RC oscillator in Exp. 10).
- Series capacitance pulls the frequency a small, repeatable amount.

## The "aha"

The RC oscillator wandered when you looked at it funny; this one sits on 3.579545 MHz and *stays there* even as you heat it with your fingers. A sliver of quartz is enforcing a frequency to a precision your resistors and caps could never dream of — and that unglamorous stability is the bedrock the entire radio spectrum is organized around.

## Going further (experiments to try and log)

- **Harmonics on the air.** A square-ish crystal oscillator is rich in harmonics. With your receiver, find the 2nd (7.16 MHz) or 4th (14.3 MHz) harmonic — a vivid reminder of why transmitters need the harmonic **low-pass filters** you'll build in Exp. 12.
- **Compare Q directly.** Recall your LC tank's Q (~20) from Exp. 03. The crystal's is thousands of times higher; that ratio *is* the difference between "a tuner that's roughly right" and "a reference you can trust."
- **The synthesizer leap (conceptual).** The QMX+'s **Si5351** takes exactly this kind of crystal reference and multiplies/divides it digitally (a PLL) to synthesize any frequency it needs. You've now built the thing it starts from.

## Why this matters (where you'll meet it)

Frequency *precision* is what makes radio possible at all. Without a stable reference you couldn't stay on frequency or tune predictably — something you rely on as a ham every time you dial in a band.

- **A crystal is Exp. 03's resonance taken to the extreme** — an LC resonator with absurdly high Q. This experiment connects the resonance idea to the real-world part that anchors every transmitter and receiver.
- **It demystifies the QMX+'s Si5351 synthesizer.** That chip multiplies a crystal reference up to any operating frequency; after this you'll know exactly what it's referencing and *why* the result is rock-stable.
- **Every microcontroller you'll use has one.** Your RP2040 and the QMX+'s STM32 each have a crystal setting their clock — same part, same reason. This ties the radio and digital sides together.
- **"Pulling" a crystal** (nudging its frequency with a little capacitance) is the basis of VXOs and fine-tuning — a classic homebrew trick you'll try here.

## Log

- Measured oscillation frequency: ___ MHz (marked 3.579545)
- Pulling range with series capacitance: ___ Hz
- Frequency shift when warmed (vs. the RC oscillator's drift):
- Harmonics found on a receiver:
- Surprises / questions:
