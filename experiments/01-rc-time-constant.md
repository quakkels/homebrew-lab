# 01 — The RC Time Constant

- **Module:** 1 — Passives & Time
- **Prerequisites:** [00 — Bench & Instrumentation](00-bench-and-instrumentation.md)
- **Est. time:** 45–60 min

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

*See* a capacitor charge and discharge, and measure the time constant **τ = R × C** with your own cursors. This one node is the seed of filters, timing, decoupling, and impedance — everything downstream.

## Concepts introduced

- A capacitor resists *changes* in voltage; voltage across it can't jump instantly.
- The exponential charge/discharge curve and the meaning of **τ = RC** (~63% of the way to target in one τ; ~99% in five).
- Why a square-wave input is the perfect way to watch this.

## Parts & instruments

- 1 × 10 kΩ resistor
- 1 × 10 nF ceramic capacitor
- Breadboard, scope, probe on the probe-comp square-wave output as the source

## Background (the why)

Charging a capacitor through a resistor is governed by:

```
V(t) = V_final × (1 − e^(−t/τ)),   τ = R × C
```

where **V(t)** = the capacitor's voltage at time *t*; **V_final** = the voltage it is heading toward; **e** = the mathematical constant ≈ 2.718 (the base of natural growth/decay); **τ (tau)** = the time constant, in seconds; **R** = resistance, in ohms (Ω); **C** = capacitance, in farads (F).

At `t = τ`, the exponential has reached `1 − e^(−1) ≈ 0.632` — 63.2% of the way. That single number is how you'll *read* time constants off the screen for the rest of your life. With R = 10 kΩ and C = 10 nF:

```
τ = 10,000 Ω × 10 × 10⁻⁹ F = 100 µs
```

(10 kΩ = 10,000 ohms; 10 nF = 10 × 10⁻⁹ farads; the answer, 100 µs, is 100 microseconds — 100 millionths of a second.)

**Why the time constant matters.** τ is the single number that tells you *how fast a circuit responds to change*, and almost everything built from resistors and capacitors is governed by it. A large τ means the circuit reacts slowly and smooths things out; a small τ means it reacts quickly and lets sharp changes through. That one idea reappears constantly:

- **Timing and delays** — a capacitor charging through a resistor toward a threshold sets the interval in a 555 timer, a power-on delay, or the pause that "debounces" a switch (Exp. 10 and 14).
- **Filtering** — the very same τ *is* a filter's cutoff frequency (`f_c = 1 / (2πτ)`), deciding which frequencies pass and which are blocked. That's the whole of Exp. 02.
- **Smoothing and decoupling** — a large τ lets a capacitor hold a voltage up between "refills," which is how a power supply removes ripple and how the decoupling cap next to a chip steadies its supply (Exp. 04 and 05).
- **Signal shape and speed limits** — τ sets how fast an edge can rise or fall; in digital circuits the unavoidable stray resistance and capacitance form an RC that caps how fast a wire can switch — a real ceiling on clock speeds.

In short, learning to *see* and predict τ here is learning the pace at which all of analog electronics happens.

## Procedure

1. **Confirm the source.** Probe the probe-comp output directly; verify a clean square wave and note its frequency/amplitude (from Experiment 00).
2. **Build the RC:**

   ```
   CAL out ──[ 10kΩ ]──┬── probe tip
                       │
                     [10nF]
                       │
                      GND ── probe ground clip
   ```

   **Reading this diagram** (the same symbols appear in every experiment — full list in the [glossary](../glossary.md)):
   - `CAL out` — the scope's calibration output, a ~1 kHz square wave, used here as the test signal.
   - `──` and `│` — wires; `┬` — a junction where wires connect.
   - `[ 10kΩ ]` — a component drawn as a box with its value inside (here a 10 kilohm resistor); `[10nF]` is a 10 nanofarad capacitor.
   - `GND` — ground, the circuit's 0-volt reference.
   - "probe tip" / "probe ground clip" — where the two ends of the oscilloscope probe attach.

   Square wave → resistor → node → capacitor → ground. Probe the R/C node.
3. **Set the scope:** timebase ~50 µs/div, adjust volts/div to fill the screen, trigger on the rising edge. You should see exponential curves instead of square edges.
4. **Measure τ.** Put one voltage cursor at the low level, one at 63% of the way up to the high level. Put time cursors from the rising edge to where the trace crosses that 63% line. Read the time — it should be ≈ 100 µs.

## What to observe / measure

- The sharp square edges become smooth exponential ramps (charge up, discharge down).
- The 63% point lands at ≈ τ = 100 µs.
- Full settling takes about 5τ ≈ 500 µs.

## The "aha"

You did the arithmetic in your head (10 k × 10 n = 100 µs) and the *screen agrees*. The abstract formula is now a thing you can see and point at. That's analog intuition being built.

## Going further (experiments to try and log)

- **Bigger cap:** swap 10 nF → 100 nF. τ becomes 1 ms; the cap now barely charges before the square wave flips. Predict the shape *before* you look.
- **Swap R and C positions** (cap on top, resistor to ground, probe the node). Now the *edges* survive as spikes and the flat parts decay — a high-pass / differentiator. Same two parts, opposite behavior.
- **Sweep values** and confirm τ tracks R×C each time.

This "lazy vs spiky" behavior is exactly what becomes a **low-pass** and **high-pass filter** in Experiment 02 — same circuit, viewed in the frequency domain.

## Log

- Measured τ (low-pass, 10 k / 10 nF): ______ µs (expected 100 µs)
- Measured τ with 100 nF: ______ (expected 1 ms)
- High-pass version — what the edges looked like:
- Surprises / questions:
