# 10 — Oscillators (555 & RC)

- **Module:** 5 — Oscillators & Signals
- **Prerequisites:** [08 — Op-Amp Fundamentals](08-op-amp-fundamentals.md)
- **Est. time:** ~90 min

## Objective

Make a circuit generate its *own* signal instead of measuring an external one. Build a **555 astable** and an **op-amp relaxation oscillator**, predict each frequency from its R and C, and measure it. This is a real conceptual milestone: the circuit becomes a source.

## Concepts introduced

- **Feedback that sustains oscillation** (positive feedback + a timing delay), vs. the *negative* feedback that stabilized the op-amp.
- The **555 astable**: it charges and discharges a cap between two thresholds; R and C set the frequency (this is Experiment 01's RC, put to work).
- **Duty cycle** and how the 555's charge/discharge asymmetry sets it.
- An **op-amp relaxation oscillator** (comparator + hysteresis + RC), and how its waveform compares.

## Parts & instruments

- 1 × **NE555**, 1 × **LM358**
- 555 timing: **4.7 kΩ** (R1), **4.7 kΩ** (R2), **100 nF** (C); a **10 kΩ** pot (optional, to vary frequency)
- Op-amp osc: 2 × **10 kΩ** + **10 kΩ** (hysteresis divider), **10 kΩ** + **100 nF** (timing), plus the 4.5 V reference from Exp. 08
- 9 V supply, scope

## Background (the why)

Every clock, tone, carrier, and blink starts with an **oscillator** — a circuit that produces a periodic signal with no periodic input. The recipe is always the same: **amplify, feed some output back in phase (positive feedback), and include a delay** so the thing swings back and forth instead of just latching. A **relaxation oscillator** builds that delay from an RC charging toward a threshold — so everything you learned about `τ = RC` now *sets a frequency*.

**The 555 astable.** The classic timer chip. It charges the timing cap **C** through **R1 + R2** up to ⅔ of the supply, then discharges it through **R2** down to ⅓, forever. The result is a square-ish wave at:

```
f = 1.44 / ((R1 + 2·R2) · C)
```

With `R1 = R2 = 4.7 kΩ` and `C = 100 nF`: `f = 1.44 / (14.1 kΩ · 100 nF) ≈ 1.0 kHz`. The duty cycle (fraction of time high) is `(R1 + R2)/(R1 + 2R2) ≈ 67%`, because charging goes through more resistance than discharging.

**The op-amp relaxation oscillator.** An op-amp used as a **comparator** with **positive** feedback (a divider from output to **+**) has two "snap" thresholds — this is a **Schmitt trigger**. Add an RC from the output back to the **−** input and the cap charges toward whichever rail the output is at, until it crosses the threshold and the output snaps the other way. It oscillates with a triangle-ish wave on the cap and a square wave at the output.

## Procedure

### Part A — 555 astable at ~1 kHz

1. Wire the 555 astable: `R1 (4.7k)` from +9 V to **DIS(7)**; `R2 (4.7k)` from **DIS(7)** to **THR(6)+TRIG(2)**; `C (100 nF)` from **THR(6)** to ground. Tie **RESET(4)** to +9 V, **CTRL(5)** through 10 nF to ground, **OUT(3)** is your signal, **VCC(8)** to +9 V, **GND(1)** to ground.
2. **Predict, then measure.** You computed ~1 kHz. Put the scope on OUT(3) and read the frequency. Then move the probe to the cap (THR) and watch the **exponential charge/discharge ramps** between the ⅓ and ⅔ thresholds — that's Experiment 01 living inside the chip.
3. Measure the **duty cycle** (high time ÷ period). Expect ~67%.

### Part B — Vary the frequency

4. Replace R1 (or R2) with the **10 kΩ pot**. Turn it and watch the frequency track R×C. Confirm the direction and rough magnitude match `f = 1.44/((R1+2R2)C)`.

### Part C — Op-amp relaxation oscillator

5. Build the Schmitt-trigger oscillator: output → **10 kΩ** → **+** input, and **10 kΩ** from **+** to the 4.5 V reference (this sets the two thresholds). Output → **10 kΩ** → **−** input, and **100 nF** from **−** to the reference (the timing RC).
6. Scope both the **−** input (triangle-ish cap voltage) and the **output** (square). Estimate the frequency and compare its waveform quality to the 555's.

## What to observe / measure

- The 555 output is a steady ~1 kHz square wave with ~67% duty, and the cap shows the RC ramps between ⅓ and ⅔ supply.
- Turning the pot slides the frequency exactly as R×C predicts.
- The op-amp oscillator self-starts and produces a triangle-on-the-cap / square-at- the-output pair.

## The "aha"

Nothing periodic went *in*, yet a clean tone came *out* — the circuit is generating time itself from a cap charging through a resistor. You've now seen both faces of feedback: negative feedback (Exp. 08) that *stabilizes*, and positive feedback here that *sustains*. That pair is the whole idea of feedback, and it just clicked.

## Going further (experiments to try and log)

- **Hear it.** Put the 555 output through a resistor into a small speaker or piezo — 1 kHz is an audible tone. Sweep the pot and you've made a simple siren.
- **PWM / dimming.** Add diodes so charge and discharge take different paths, making the **duty cycle** adjustable independent of frequency. Feed that to an LED and vary its brightness — you've built pulse-width modulation, the same trick behind class-D audio and the QMX+'s switching PA.
- **Frequency divider preview.** Feed the 555 output into a later digital counter (Exp. 14) to divide it down — the bridge from "a tone" to "a clock."
- **Why it's not good enough for radio.** Warm the timing cap/resistor and watch the frequency drift. Fine for a blinker, hopeless for staying on a ham band — which is exactly the problem the crystal (Exp. 11) solves.

## Why this matters (where you'll meet it)

Up to now you've *measured* signals; here a circuit **generates its own**. That's a real conceptual milestone — oscillators are the source of every clock, tone, carrier, and blink in existence.

- **The 555 is the most-used chip in history.** Knowing it means you can improvise timing, tones, blinkers, and PWM for any project without reaching for a microcontroller.
- **PWM is a superpower.** Varying a square wave's duty cycle is how you dim LEDs (your keyboard's backlight), control motor speed, and — conceptually — how class-D audio and the QMX+'s switching PA make power efficiently.
- **Feedback, seen from the other side.** Op-amps used feedback to *stabilize*; oscillators use feedback to *sustain*. Seeing both makes the whole idea of feedback click.
- **It sets up the crystal oscillator (Exp. 11)** — the difference between "an oscillator" and "an oscillator stable enough to trust on a ham band."

## Log

- 555 predicted vs measured frequency: ___ / ___ Hz
- Duty cycle observed: ___ % (expected ~67%)
- Frequency range across the pot: ___ to ___ Hz
- Op-amp oscillator frequency / waveform notes:
- Drift when warmed:
- Surprises / questions:
