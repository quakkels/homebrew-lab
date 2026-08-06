# 01 — The RC Time Constant

- **Module:** 1 — Passives & Time
- **Prerequisites:** [00 — Bench & Instrumentation](00-bench-and-instrumentation.md)
- **Est. time:** 45–60 min

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

At `t = τ`, the exponential has reached `1 − e^(−1) ≈ 0.632` — 63.2% of the way. That single number is how you'll *read* time constants off the screen for the rest of your life. With R = 10 kΩ and C = 10 nF:

```
τ = 10,000 Ω × 10 × 10⁻⁹ F = 100 µs
```

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
