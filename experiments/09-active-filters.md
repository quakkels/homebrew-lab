# 09 — Active Filters

- **Module:** 4 — Op-Amps
- **Prerequisites:** [08 — Op-Amp Fundamentals](08-op-amp-fundamentals.md), [02 — RC Filters](02-rc-filters.md)
- **Est. time:** ~2 hours

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Combine op-amps with RC networks to build filters that have **gain** and **sharp, tunable** responses — no inductors required. Build a Sallen–Key low-pass, then a narrow audio **band-pass** centered on a CW pitch, and (optionally) hear a weak signal pop out of the noise.

## Concepts introduced

- **Active vs. passive filters:** op-amps add gain, buffer stages from each other, and let you get sharp responses without bulky inductors.
- The **Sallen–Key** low-pass topology; setting cutoff frequency and **Q**.
- A **multiple-feedback band-pass**: center frequency `f₀`, bandwidth, and Q.
- Why a **narrow audio band-pass** is the classic tool for CW reception.

## Parts & instruments

- 1 × **LM358** (or **TL072** if you have one — quieter for audio)
- Low-pass: 2 × **16 kΩ**, 2 × **10 nF**
- Band-pass: 2 × **100 nF**, **11 kΩ** (or 12 k), **22 kΩ**, **220 Ω**
- 9 V supply + the 4.5 V mid-rail reference from Exp. 08, signal generator, scope

## Background (the why)

A **filter** decides which frequencies to keep and which to throw away — and that turns out to be most of what signal processing *is*. In Experiment 02 you built passive RC filters; they work, but they're gentle (they roll off slowly), they have no gain, and each one loads the next. Wrapping RC networks around an op-amp fixes all three: you get **gain**, **buffering**, and **sharpness** you can dial in.

**Sallen–Key low-pass.** Two resistors and two caps around one op-amp give a **second-order** low-pass — twice as steep as a single RC. In the equal-component form (both R equal, both C equal):

```
f_c = 1 / (2π R C)
```

where **f_c** = the cutoff frequency (Hz); **R** = resistance (Ω); **C** = capacitance (F); **π** ≈ 3.14159. (Further down: **Q** = quality factor — how sharp the filter is; **f₀** = the band-pass center frequency; **bandwidth** = how wide the passband is.)

With `R = 16 kΩ`, `C = 10 nF`: `f_c ≈ 1/(2π·16k·10n) ≈ 1.0 kHz`. Below `f_c` the signal passes; above it, it falls off at 40 dB/decade (steeper than Exp. 02's 20).

**Multiple-feedback band-pass.** For CW (Morse) you want to hear a *single audio tone* and reject everything else. A band-pass passes a narrow window around a center frequency `f₀` and its sharpness is set by **Q = f₀ / bandwidth**. A design centered near **700 Hz** with **Q ≈ 5** (so ~140 Hz wide) is a classic CW filter. Using both caps = 100 nF, the component set below lands right about there — and you'll *measure* how close.

## Procedure

> Reuse the **4.5 V mid-rail reference** from Experiment 08 so the single-supply LM358 can handle AC audio. Both filters reference their "+"/ground returns to it.

### Part A — Sallen–Key low-pass (~1 kHz)

1. Build the equal-component Sallen–Key: signal → **16 kΩ** → node A → **16 kΩ** → op-amp **+** input; **10 nF** from node A to the output; **10 nF** from the op-amp **+** input to the reference; op-amp wired as a unity buffer (output to **−**).

   ```
   IN ─[16k]─A─[16k]─┬─(+)\
                │    │     >── OUT ──┬──►
             [10n]  [10n]  (−)──────┘
                │    (to ref)
               OUT (feedback to node A)
   ```

   *Diagram key:* `IN`/`OUT` = signal in/out; `[16k]` = resistor, `[10n]` = capacitor; `(+)`/`(−)` = the op-amp's two inputs; the `\ > /` shape is the op-amp itself; `node A` is the junction between the two resistors; `ref` = the 4.5 V mid-rail reference. Symbols: [glossary](../glossary.md).

2. **Sweep it.** Feed a constant-amplitude sine and step the frequency: 100 Hz, 300 Hz, 1 kHz, 3 kHz, 10 kHz. Record output amplitude at each.
3. Find the **−3 dB point** (output at 0.707 of the passband level). It should land near **1 kHz**. Above it, note how much faster it falls than your Exp. 02 RC — that's second-order steepness.

### Part B — CW audio band-pass (~700 Hz)

4. Build the multiple-feedback band-pass:

   ```
   IN ─[R1 11k]─┬──[C1 100n]──┬─(−)\
                │             │     >── OUT ──┬──►
             [R3 220Ω]     [C2 100n]  (+)     │
                │             └──[R2 22k]─────┘
               ref          (+ to 4.5V ref)
   ```

   *Diagram key:* `IN`/`OUT` = signal in/out; `[R1 11k]`/`[R2 22k]`/`[R3 220Ω]` = resistors; `[C1 100n]`/`[C2 100n]` = capacitors; `(−)`/`(+)` = the op-amp's inputs; `ref` = the 4.5 V mid-rail reference. Within the circuit, R1 sets the input level, R2 sets the feedback/Q, and R3 tunes f₀. Symbols: [glossary](../glossary.md).
5. **Sweep 100 Hz → 3 kHz.** Find the peak frequency `f₀` (expect ~700 Hz) and the two **−3 dB** frequencies on either side. Compute `Q = f₀ / (f_high − f_low)` — you're aiming for ~5.
6. Listen to the resonance: the passband is narrow enough that as you sweep, the output rises and falls sharply around 700 Hz.

### Part C — (Optional) Hear CW pop out

7. If you can feed real receiver audio (or two mixed tones — a 700 Hz "signal" plus broadband hiss) into the filter, A/B **filter in vs. filter out**. The in-band tone jumps forward while the surrounding noise drops away. This is exactly the experience of switching on a CW filter on the air.

## What to observe / measure

- Low-pass: flat below ~1 kHz, then a steep roll-off; −3 dB near the designed `f_c`.
- Band-pass: a clear peak near 700 Hz with steep skirts; measured Q around 5.
- With audio: a buried tone becomes obviously louder than its surrounding noise when the filter is engaged.

## The "aha"

Two op-amp circuits, a handful of resistors and caps, and **no inductors** — yet you built responses far sharper than passive RC could ever give, and one of them is a tool you'd genuinely switch on to dig a weak CW signal out of the noise. When you later read "the DSP applies a band-pass filter," you'll know precisely what operation the code is standing in for, because you built its analog twin by hand.

## Going further (experiments to try and log)

- **Retune the CW pitch.** Change R3 to move `f₀` to your preferred sidetone (many ops like 600 Hz). Predict the shift, then measure it.
- **Change Q.** Adjust R2 to widen or narrow the passband and watch the skirts get gentler or sharper. Too-high Q rings and sounds "boingy" — a real design trade-off.
- **Cascade.** Follow the band-pass with the low-pass to knock down high-frequency hiss even more. Stages that don't load each other (thanks to the op-amps) is the whole point of *active* filtering.
- **High-pass Sallen–Key.** Swap the R's and C's in Part A to make a high-pass, and confirm the mirror-image response.

## Why this matters (where you'll meet it)

A filter decides *which frequencies you keep and which you throw away* — and that turns out to be most of what signal processing is. Active filters do it with gain and precise control, and without bulky, expensive inductors.

- **CW operating — you'll literally hear the difference.** A narrow audio band-pass around your CW pitch is the classic tool for pulling a weak signal out of a noisy band. This is the first experiment that builds something you'd actually *use on the air* with the QMX+ — and you'll be able to A/B "filter in vs. filter out" and hear a buried signal pop out.
- **It demystifies DSP.** The QMX+ does its filtering in *software* on the STM32. Building the analog equivalent here means that when you later read "the DSP applies a band-pass," you'll know exactly what operation the code is standing in for — the software and the op-amp are doing the *same thing*.
- **Every audio and mixed-signal system uses these.** Anti-aliasing filters before an ADC, reconstruction filters after a DAC, tone controls, sensor-noise smoothing — the same handful of op-amp filter topologies show up again and again.
- **Repair / schematic-reading.** The **Sallen–Key** stage you build here is one of the most common filter blocks in existence. Once you've built one, you'll *recognize it on sight* in other people's schematics and know what it does.
- **It ties the course together.** This is where Module 1 (RC/reactance) and Module 4 (op-amps) combine into something greater than either — the moment the fundamentals start compounding into real capability.

## Log

- Low-pass −3 dB frequency: ___ Hz (expected ~1 kHz)
- Band-pass f₀: ___ Hz; −3 dB points: ___ / ___ Hz → Q = ___ (expected ~5)
- Listening notes (filter in vs out):
- Surprises / questions:
