# 07 — Transistor as an Amplifier

- **Module:** 3 — Transistors
- **Prerequisites:** [06 — Transistor as a Switch](06-transistor-as-switch.md)
- **Est. time:** ~2 hours

## Objective

Bias a transistor into its *active* region — halfway on, not fully on or off — and get real voltage **gain**. Build a common-emitter amplifier, set its DC operating point with a multimeter, then measure its gain and watch it clip on the scope. This is the single biggest step in building analog intuition.

## Concepts introduced

- The **active region** (vs. saturation/cutoff) and the DC **operating point** (bias) that parks the transistor there.
- The **common-emitter** amplifier: voltage gain, input/output **coupling caps**, and the **emitter-bypass** cap.
- **Emitter degeneration** — trading gain for stability, and why that trade is almost always worth it.
- **Clipping**, headroom, and the phase inversion of an inverting stage.

## Parts & instruments

- 1 × **2N3904**, 12 V supply
- Resistors: **150 kΩ**, **22 kΩ** (bias divider), **4.7 kΩ** (collector), **1 kΩ** (emitter)
- Caps: 2 × **1 µF** (input/output coupling), **10 µF** (emitter bypass)
- Signal generator, 2-channel scope, multimeter

## Background (the why)

As a *switch* (Exp. 06) a transistor lives at the extremes — fully off or fully saturated. In between is the **active region**, where collector current is a faithful, amplified copy of base current. Parking the transistor in the middle of that region is called **biasing**, and doing it well is the skill most self-taught builders never nail. Get it right and everything downstream — op-amps, oscillators, RF stages — makes sense.

**The plan:** set a steady DC operating point so the collector sits at roughly half the supply, leaving room to swing both up and down. Then let a small AC signal ride on top of that DC through a **coupling capacitor** (which blocks DC so the signal source can't disturb the bias).

**Setting the bias (voltage-divider + emitter resistor):**

- The divider (R1 = 150 k, R2 = 22 k from 12 V) sets the base at `V_B ≈ 12 · 22/(150+22) ≈ 1.5 V`.
- The base-emitter drop is ~0.7 V, so `V_E ≈ 0.8 V`.
- The emitter resistor then *sets the current*: `I_C ≈ V_E / R_E ≈ 0.8 V / 1 kΩ ≈ 0.8 mA`. (This is the trick — current is set by resistors, not by the transistor's twitchy β.)
- That current through R_C drops `0.8 mA × 4.7 kΩ ≈ 3.8 V`, putting the collector at `V_C ≈ 12 − 3.8 ≈ 8.2 V`. Plenty of room to swing.

**Gain comes in two flavors here:**

- **With the emitter resistor unbypassed**, gain is stable and modest: `A_v ≈ −R_C / R_E ≈ −4.7`. (The minus sign = inversion.)
- **With a bypass cap across R_E** (10 µF), the emitter is grounded *for AC only* and gain jumps to `A_v ≈ −R_C / r_e`, where `r_e ≈ 26 mV / I_C ≈ 32 Ω` — so `A_v ≈ −4700/32 ≈ −145`. Big, but temperature-sensitive and easy to clip.

That contrast — **stable-but-modest vs. high-but-touchy** — *is* the lesson. Feedback (the emitter resistor) is what buys predictability, and you're about to feel exactly what it costs and what it's worth.

## Procedure

### Part A — Set and verify the DC bias (no signal yet)

1. Build the stage:

   ```
        +12V
     ┌───┴───┐
   [150k]  [4.7k]  R_C
     │        ├──── V_C ──[1µF]──► OUT
     ├─ V_B ──┤ C
   [22k]   (2N3904)
     │        │ E ── V_E ──┬── [1kΩ] R_E ── GND
    GND               [10µF bypass] ── GND
   IN ──[1µF]──► V_B (base)
   ```

2. Power up with **no input signal**. Measure with the multimeter: `V_B ≈ 1.5 V`, `V_E ≈ 0.8 V`, `V_C ≈ 8 V`. If V_C is near 12 V the transistor is cut off; if near V_E it's saturated — re-check your divider. **Getting these three numbers right is 80% of the experiment.**

### Part B — Measure the gain (start unbypassed)

3. Temporarily **leave the 10 µF bypass out**. Inject a small sine — **~100 mV peak-to-peak, 1 kHz** — into the input coupling cap. Put scope ch1 on the input, ch2 on the output.
4. Measure output ÷ input. Expect about **4.7×**, and note the output is **upside down** relative to the input (180° inversion) — the signature of a common-emitter stage.

### Part C — Bypass the emitter and watch gain soar (then clip)

5. Add the **10 µF across R_E**. Re-measure: gain leaps to ~**100–150×**. Same circuit, one cap, a huge change — because you removed the AC feedback.
6. Now **increase the input** until the output can't grow any more: it **clips**, flattening at the top (transistor cutting off) and/or bottom (saturating). You've hit the headroom limit set by your bias point.

## What to observe / measure

- The three DC bias voltages land where predicted — proof you *placed* the operating point.
- Unbypassed gain ≈ −R_C/R_E ≈ −4.7, stable and clean.
- Bypassed gain ≈ −R_C/r_e ≈ −145, large but quick to clip.
- The output is inverted, and clipping flattens the peaks once you exceed headroom.

## The "aha"

You didn't just copy a schematic — you *chose* where to park the transistor, and the multimeter confirmed it sat exactly there. Then a 100 mV whisper came out as a volt-plus swing. The moment the bypass cap multiplied the gain by 30× and the signal started clipping, you *felt* the trade between raw gain and control that every amplifier design is really about. That feeling is analog intuition.

## Going further (experiments to try and log)

- **Warm the transistor.** Pinch the 2N3904 between your fingers while watching the bypassed output. The heavily-bypassed gain drifts noticeably (β and r_e shift with temperature); the unbypassed version barely moves. That's *why* engineers accept lower gain for stability.
- **Partial bypass.** Put a small resistor in series with the bypass cap to set a gain *between* the two extremes — designed gain, on purpose.
- **Measure input impedance.** Add a series resistor at the input and watch the signal divide; you're seeing the stage's input impedance loading the source — the exact problem the op-amp buffer (Exp. 08) will solve.

## Why this matters (where you'll meet it)

Amplification is the *other* half of the transistor, and it's the beating heart of every receiver: turning a microvolt whisper from the antenna into something you can actually hear.

- **Biasing is the skill that separates copying from designing.** Setting an operating point is the thing most self-taught people never really internalize — and it's exactly the intuition that turns schematics from "magic I follow" into "circuits I understand." This experiment is arguably the biggest single step in closing your analog gap.
- **It makes op-amps click.** An op-amp (next module) is just a very good amplifier wrapped in feedback. Having built gain the hard way, you'll *feel* what feedback buys you instead of taking the formulas on faith.
- **Every receiver, including the QMX+, is stages of gain.** Understanding one amplifier stage is understanding the building block they're all made of.
- **Repair / hacking:** recognizing a common-emitter stage and knowing where its DC voltages *should* sit lets you troubleshoot analog gear with a multimeter.
- **Clipping and headroom** intuition matters anywhere you push a signal too hard — audio distortion, overdriving an RF stage, ADC clipping.

## Log

- DC operating point — V_B: ___ V, V_E: ___ V, V_C: ___ V (expected ~1.5 / 0.8 / 8)
- Gain unbypassed: ___× (expected ~4.7); bypassed: ___× (expected ~100–150)
- Input level where clipping starts: ___ mV pp
- Warm-up drift (bypassed vs unbypassed):
- Surprises / questions:
