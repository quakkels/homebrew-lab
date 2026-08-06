# 08 — Op-Amp Fundamentals

- **Module:** 4 — Op-Amps
- **Prerequisites:** [07 — Transistor as an Amplifier](07-transistor-as-amplifier.md)
- **Est. time:** ~90 min

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Get precise, predictable voltage gain set by just **two resistors** — the moment analog design stops being fiddly. Build inverting, non-inverting, and buffer configurations, measure their gain, and prove a buffer cures the "my circuit sags under load" problem you hit in Experiment 07.

## Concepts introduced

- The two **golden rules** of an ideal op-amp with negative feedback: (1) no current flows into the inputs; (2) the op-amp drives its output until the two inputs are at the **same voltage**.
- **Non-inverting** gain `1 + R_f/R_in`, **inverting** gain `−R_f/R_in`, and the **unity-gain buffer**.
- Why a buffer's huge input impedance and tiny output impedance fix inter-stage **loading**.
- Real-world limits: supply rails, output swing, single- vs. dual-supply operation.

## Parts & instruments

- 1 × **LM358** (dual op-amp, happy on a single supply)
- Resistors: 2 × **10 kΩ**, 1 × **100 kΩ**, 2 × **1 MΩ**, 1 × **100 kΩ** (load)
- Caps: **1 µF** (signal coupling), **10 µF** (rail decoupling)
- 9 V supply, signal generator, scope, multimeter

## Background (the why)

Experiment 07 gave you gain, but it was a fussy business — bias points, β drift, gain that changed when you breathed on the transistor. An **op-amp** is a ready-made, very-high-gain amplifier (gain ~100,000) with two inputs: **+** (non-inverting) and **−** (inverting). On its own that raw gain is useless — it just slams to a rail. The trick is **negative feedback**: route some output back to the **−** input, and the op-amp will do whatever it takes to keep its two inputs equal. That single behavior gives the two golden rules, and from them *every* op-amp circuit falls out with grade-school algebra:

- **Non-inverting amp:** signal into **+**, feedback divider (R_f from output to **−**, R_in from **−** to ground). Gain `= 1 + R_f/R_in`.
- **Inverting amp:** signal into **−** through R_in, feedback R_f from output to **−**, **+** tied to reference. Gain `= −R_f/R_in`. The **−** input sits at a "virtual" reference because the op-amp holds it equal to **+**.
- **Buffer:** output tied straight back to **−**, signal into **+**. Gain = **1** — useless for size, invaluable because it presents a near-infinite input impedance and a near-zero output impedance. It *isolates* stages.

In those formulas, **R_f** = the feedback resistor (from the output back to the **−** input); **R_in** = the input resistor; **+** and **−** are the op-amp's two inputs (non-inverting and inverting); "gain" is output voltage ÷ input voltage (a minus sign means the signal is also flipped upside-down).

**Single-supply detail:** the LM358 runs fine on one 9 V rail, but then it can only output positive voltages. To handle an AC signal that swings both ways, we create a **virtual ground at half-supply (~4.5 V)** with a divider and reference the signal to that. (A ±supply avoids this, if you have one.)

## Procedure

> Set up a **4.5 V reference** with two 10 kΩ from 9 V to ground, and a 10 µF to steady it. AC signals get coupled in through a 1 µF cap and biased to this reference. This "mid-rail" trick is worth learning once — it's everywhere in single-supply audio.

### Part A — Non-inverting ×2

1. Signal (coupled, biased to 4.5 V) into **+**. From output: **10 kΩ** to **−**, and **10 kΩ** from **−** to the 4.5 V reference. Gain `= 1 + 10k/10k = 2`.
2. Inject ~**0.5 V pp, 1 kHz**. Measure output ÷ input ≈ **2**, and note output is **in phase** with input.

### Part B — Inverting ×10

3. Rebuild: **+** to the 4.5 V reference. Signal in through **10 kΩ** to **−**, and **100 kΩ** feedback from output to **−**. Gain `= −100k/10k = −10`.
4. Inject a small signal (~**0.2 V pp**) and confirm ~**10×** with a **180° flip** (scope both channels). Notice the **−** input barely moves — it's held at the virtual reference. That's the golden rule, visible.

### Part C — The buffer beats loading

5. Make a weak source: **1 MΩ / 1 MΩ** divider across 9 V (output ~4.5 V, but very high impedance). Measure it unloaded — fine. Now hang a **100 kΩ** load on it and watch the voltage **sag** badly (the load and the 1 MΩ form a divider).
6. Now feed that same divider tap into an LM358 **buffer** (+ input), and put the 100 kΩ load on the **buffer output**. The voltage **holds** — the op-amp supplies the load current so the fragile source doesn't have to.

## What to observe / measure

- Non-inverting gain = 2, in phase; inverting gain = 10, inverted — both matching the resistor ratios to a few percent.
- The inverting **−** node stays pinned at the reference regardless of signal.
- The raw 1 MΩ divider collapses under a 100 kΩ load; through the buffer it doesn't budge.

## The "aha"

After a whole experiment spent coaxing a transistor into giving stable gain, you set the gain here by *picking two resistors* — and the scope agreed to within a percent, no bias fiddling, no drift. Then the buffer made a hopelessly weak source drive a load it never could alone. This is the moment analog design starts feeling *designable* instead of finicky.

## Going further (experiments to try and log)

- **Summing amp.** Feed two signals through two input resistors into the inverting node; the output is their (scaled) sum. This is an analog adder — and the core of an audio mixer.
- **Difference amp.** Amplify the *difference* of two inputs while ignoring what's common to both. This "common-mode rejection" is how sensor and audio gear kills hum.
- **Find the rails.** Crank the gain or input until the output flattens — the LM358 can't swing all the way to 9 V or fully to 0 V. Knowing an op-amp's output-swing limits saves hours of confusion later.
- **Slew/bandwidth peek.** Push a fast square wave through and watch the edges round off — a preview of why op-amp choice matters at higher frequencies.

## Why this matters (where you'll meet it)

This is the experiment where analog design suddenly gets *easy*. After wrestling with transistor biasing, an op-amp hands you precise gain set by two resistors, with formulas that just work — it's a genuine morale boost and a turning point.

- **The workhorse of all analog signal handling.** The QMX+ uses op-amps right after its quadrature detector to boost tiny received signals before the ADC — you'll be looking at that exact role.
- **Buffering solves a problem you'll hit constantly:** "my circuit sags when I connect the next stage to it." An op-amp buffer makes stages stop loading each other — one of the most practically useful tricks in the whole course.
- **Precision without fuss:** gain, summing, difference, comparison — all become clean design problems instead of biasing puzzles. This is where "designing" starts to feel achievable.
- **Direct prerequisite for the active filters (Exp. 09)**, including the CW audio filter you'd actually use on the air.
- **Schematic-reading / repair:** the inverting and non-inverting configs are so common that recognizing them on sight is a core literacy skill.

## Log

- Non-inverting gain: ___ (expected 2); inverting gain: ___ (expected −10)
- Behavior of the inverting **−** node under signal:
- 1 MΩ divider under 100 kΩ load — raw: ___ V, buffered: ___ V
- Output-swing limits observed: ___ V to ___ V
- Surprises / questions:
