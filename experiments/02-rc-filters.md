# 02 — RC Filters (low-pass & high-pass)

- **Module:** 1 — Passives & Time
- **Prerequisites:** [01 — The RC Time Constant](01-rc-time-constant.md)
- **Est. time:** 60 min

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Take the *exact same* RC circuit from Experiment 01 and view it in the **frequency domain**: as you change the input frequency, watch some frequencies pass and others get attenuated. Measure the **cutoff frequency** and connect it to τ. This is the conceptual root of every filter you'll ever build — including the QMX+'s band-pass and low-pass filters.

## Concepts introduced

- Reactance: a capacitor's "resistance" falls as frequency rises (`Xc = 1 / (2πfC)`).
- The RC as a frequency-dependent voltage divider → **low-pass** and **high-pass**.
- **Cutoff frequency** `f_c = 1 / (2πRC)`, the −3 dB point (output ≈ 0.707× input), and its identity with the time constant: `f_c = 1 / (2πτ)`.
- Reading amplitude *ratios* (dB) instead of absolute volts.

## Parts & instruments

- 1 × 10 kΩ resistor, 1 × 10 nF capacitor (same as Exp. 01)
- A **variable sine source** — ideally a function/DDS generator. If you don't have one yet, see "If you have no signal generator" below; this is the natural moment to get a cheap DDS module.
- Scope (two channels ideal: one on input, one on output)

## Background (the why)

**What a filter is.** A filter is a circuit that lets some frequencies through while weakening ("attenuating") others — it sorts a signal by frequency. Filters are named by *which* frequencies they keep:

- A **low-pass** filter passes frequencies *below* a chosen **cutoff** and weakens everything above it — it lets the *low* frequencies pass.
- A **high-pass** filter is the mirror image: it passes frequencies *above* the cutoff and weakens everything below it.

The **cutoff frequency** is simply the dividing line between "passed" and "blocked."

**What they're for.** Choosing which frequencies to keep and which to discard turns out to be most of what signal processing is:

- **Audio** — sending bass to a subwoofer (low-pass) and treble to a tweeter (high-pass); the tone and EQ controls on any stereo.
- **Cleaning up a signal** — a low-pass smooths away high-frequency noise; a high-pass strips off an unwanted DC level or low-frequency rumble so only the wanted wiggle is left.
- **Radio** — keeping the band you want and rejecting the rest, and removing junk before it reaches a receiver or leaves a transmitter (you'll build the sharp radio-grade versions in Exp. 12).
- **Interfacing stages** — "coupling" a signal from one circuit to the next while blocking their different DC levels (a high-pass), or smoothing a supply (a low-pass).

Here's the payoff that ties this back to Exp. 01: the cutoff frequency is set by the *same RC time constant* you already measured. From Experiment 01, `τ = RC = 100 µs`. The cutoff is:

```
f_c = 1 / (2π × τ) = 1 / (2π × 100 µs) ≈ 1592 Hz
```

where **f_c** = the cutoff frequency, in hertz (Hz); **π** = the constant ≈ 3.14159; **τ (tau)** = the RC time constant from Exp. 01 (here 100 µs). In words: a 100-microsecond time constant is the same thing as a ~1.6 kHz cutoff.

Below `f_c` the capacitor looks like a high impedance and the low-pass output follows the input. Above `f_c`, `Xc` drops, the divider attenuates, and the output falls at ~20 dB/decade (÷10 in amplitude per ×10 in frequency).

## Procedure

**Low-pass** (resistor in series, cap to ground — same as Exp. 01):

1. Feed a sine into the input; put CH1 on input, CH2 on the R/C node (output).
2. Start at ~100 Hz. Output ≈ input (it passes).
3. Sweep frequency up. At **f_c ≈ 1.6 kHz**, output amplitude should be **0.707×** the input (−3 dB). Measure it.
4. Keep going to 16 kHz: output should be ~1/10 (−20 dB). Note the roll-off.

**High-pass** (swap: cap in series, resistor to ground):

5. Repeat the sweep. Now low frequencies are attenuated and high frequencies pass; the −3 dB point is the same `f_c`.

## What to observe / measure

- The −3 dB (0.707×) point lands near 1.6 kHz for both versions.
- Low-pass: highs shrink; high-pass: lows shrink.
- Optional: note the output *phase* shifting relative to the input as you cross f_c (±45° at cutoff). Phase matters a lot in RF later.

## The "aha"

Experiments 01 and 02 are the **same circuit**. "Time constant" and "cutoff frequency" are two views of one thing, linked by `f_c = 1/(2πτ)`. Filtering isn't a new concept — it's the RC charge/discharge you already saw, described by frequency instead of time.

## If you have no signal generator

- Use a phone/PC tone-generator app into a headphone jack (safe, low voltage) as a rough audio source, or
- Order a cheap DDS module (AD9833 or an "FY"-style generator). You'll use it for the rest of the course. This experiment is the reason to buy one now.

## Going further

- Build **two** low-pass stages in series and measure the steeper roll-off (−40 dB/decade). This is the idea behind multi-pole filters.
- Predict, then measure, the cutoff if you change C to 1 nF (f_c ×10 ≈ 16 kHz).
- Preview: an **LC** filter (Experiment 03/12) rolls off far more sharply and can *resonate* — that sharpness is why radios use LC, not RC, filters.

## Log

- Measured f_c, low-pass: ______ Hz (expected ≈ 1592 Hz)
- Output/input ratio at f_c: ______ (expected 0.707)
- Measured f_c, high-pass: ______ Hz
- Roll-off observed per decade: ______ dB
- Surprises / questions:
