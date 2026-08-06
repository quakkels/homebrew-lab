# 12 — LC Filters & Impedance Matching

- **Module:** 6 — RF Fundamentals
- **Prerequisites:** [03 — Inductors & LC Resonance](03-inductors-and-lc-resonance.md), [02 — RC Filters](02-rc-filters.md)
- **Est. time:** ~2–3 hours

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Build the real filters radios use — a sharp **LC low-pass** (a transmitter harmonic filter) and an **LC band-pass** (a receiver front end) — wind your own toroids for them, and measure their response. Then build an **L-network** impedance match and watch a mismatch turn into a match. This maps directly onto the QMX+'s filter banks and finally makes SWR mechanical.

## Concepts introduced

- **Multi-element LC low-pass** filters — the harmonic filters on every transmitter output — and their cutoff and stopband depth.
- **Band-pass** filters for a receiver front end; insertion loss and shape.
- **Impedance** as a first-class idea: why **50 Ω**, and **maximum power transfer**.
- **L-network** matching, tying straight to the antenna tuning you already do.
- **Winding toroids** accurately and measuring the result (a **NanoVNA** shines).

## Parts & instruments

- **Toroid cores:** T37-2 (red, for ~1–10 MHz) and/or T37-6 (yellow); enameled wire
- **RF capacitors:** C0G/NP0 ceramics or silver-mica, assorted (e.g. 100–470 pF)
- A **NanoVNA** *(strongly recommended — it makes all of this trivial to see)*, or a signal generator + scope with a 50 Ω setup
- Small breadboard or a scrap of copper-clad for RF, 50 Ω terminations

## Background (the why)

At RF, two ideas dominate that you can now build on top of everything so far: **filtering** (from resonance, Exp. 03) and **impedance matching** (new here).

**LC low-pass — the harmonic filter.** In Exp. 11 you saw a crystal oscillator is full of harmonics; a transmitter's amplifier is worse. Radiating those harmonics is illegal and rude (they land in other bands). So every transmitter ends in a **low-pass filter** that passes the operating frequency and crushes everything above it. A multi-element LC low-pass (e.g. a 5-element "Cauer/Chebyshev" C-L-C-L-C) gives a steep cliff just above the band. Rule-of-thumb design for a 50 Ω system with cutoff `f_c`:

```
L ≈ 50 / (2π f_c)          C ≈ 1 / (2π f_c · 50)
```

where **L** = each inductor value (henries, H); **C** = each capacitor value (farads, F); **f_c** = the filter's cutoff frequency (Hz); **50** = the system impedance, 50 ohms (Ω); **π** ≈ 3.14159.

For a 40 m transmitter (7 MHz) you'd set `f_c ≈ 10 MHz`, giving Ls around **0.8 µH** (≈17 turns on a T37-2) and Cs around **330 pF** — then tune from there.

**Impedance and why 50 Ω.** Every RF stage has a characteristic impedance, and **maximum power transfers when source and load impedances match**. Mismatch and some power reflects back instead of moving forward — that reflection *is* SWR. The whole radio world standardized on **50 Ω** as a good compromise between low loss and power handling, which is why your coax, your rigs, and your antennas are all "50 Ω."

**L-network match.** When two impedances differ (say a 50 Ω radio and a 200 Ω antenna feedpoint), a simple **L-network** — one series reactance and one shunt reactance (an inductor and a capacitor) — transforms one into the other at a chosen frequency. This is exactly what an antenna tuner does; you're about to build a miniature one and *measure* the match improve.

## Procedure

### Part A — Wind the inductors

1. Wind a toroid for your low-pass. For ~0.8 µH on a **T37-2** (`A_L ≈ 4 nH/turn²`): `turns ≈ √(L / A_L) = √(800 nH / 4 nH) ≈ 14–17 turns` — where **A_L** is the core's "inductance factor" (the inductance a single turn gives; total inductance grows with the *square* of the number of turns) and **L** is the inductance you want. Space the turns evenly around ~⅔ of the core. Scrape and tin the enamel off the ends.
2. **Measure it.** On the NanoVNA (or by ringing it against a known cap as in Exp. 03) confirm the inductance is in the ballpark. Adjusting turns is how you trim — this is the toroid-winding skill the QMX+ build will lean on hard.

### Part B — Build and sweep the low-pass

3. Build a **5-element low-pass** (C–L–C–L–C) between a 50 Ω source and 50 Ω load, with your wound Ls and RF caps sized for `f_c ≈ 10 MHz`.
4. **Sweep it** 1–30 MHz on the NanoVNA (S21 / transmission). Read:
   - the **passband** (near-0 dB up to ~10 MHz),
   - the **−3 dB cutoff**, and
   - the **stopband depth at 14 MHz** (the 2nd harmonic of 7 MHz) — you want tens of dB down.
5. If cutoff is off, add/remove a turn or change a cap and re-sweep. *Seeing* the curve move as you tweak is the whole point.

### Part C — Band-pass front end

6. Build a simple **LC band-pass** centered on a band you like (a series or coupled resonant pair from Exp. 03, scaled to RF). Sweep it: find the **center frequency**, the **bandwidth**, and the **insertion loss** at center.

### Part D — L-network match

7. Terminate the network in a **non-50 Ω load** (e.g. 200 Ω). On the NanoVNA (S11 / reflection or Smith chart) note the mismatch/SWR.
8. Add an **L-network** (series L, shunt C — values from a matching calculator for 50↔200 Ω at your frequency) and adjust. Watch the reflection drop toward zero / SWR toward 1:1. You just matched two impedances by hand.

## What to observe / measure

- The low-pass is flat through the band, then falls off a cliff; the 2nd-harmonic frequency is well down in the stopband.
- The band-pass peaks at its center with measurable bandwidth and a little insertion loss.
- Adding the L-network collapses the reflection — a mismatch becoming a match, live on the screen.

## The "aha"

You wound a lump of wire on a ferrite ring, measured its inductance, dropped it into a filter, and watched a sharp RF cliff appear exactly where you designed it — then you took a "bad SWR" load and *tuned it to 50 Ω* with two parts. SWR, harmonic filters, antenna tuners: the things you've operated around as a ham are now circuits you build and measure. This is where your radio hobby and your circuit knowledge fuse.

## Going further (experiments to try and log)

- **Trace the QMX+ filters.** Open the QMX+ schematic and find its transmit low-pass banks and receive band-pass filters. They are *this experiment*, repeated per band — now you can read, align, and troubleshoot them.
- **Harmonic reality check.** Feed your Exp. 11 crystal oscillator (harmonic-rich) through the low-pass and watch the harmonics you found on the receiver disappear.
- **Q and loss.** Compare a filter built with your hand-wound toroids vs. cheap axial inductors; the toroids' higher Q gives lower loss and sharper skirts — you can measure the difference.
- **Smith chart literacy.** Spend time on the NanoVNA's Smith chart while adjusting the L-network; watching the point walk to the center builds matching intuition nothing else does.

## Why this matters (where you'll meet it)

This is the **deepest bridge between your ham background and circuit design**. You already tune antennas and watch SWR; here you build the filters and matching networks that make all of that work — and measure them.

- **Impedance matching finally becomes mechanical, not magical.** Maximum power transfer is *why* we use 50 Ω, why a mismatch reflects power back, and why an antenna tuner exists. After this, SWR is something you understand from the inside.
- **The QMX+'s filter banks ARE this experiment.** Its receive band-pass filters and transmit low-pass (harmonic) filters are exactly the LC filters you'll build here — so this is what lets you align and troubleshoot your radio instead of just following the manual.
- **Toroid winding gets good here.** Accurate hand-wound inductors are the make-or-break homebrew skill, and you want it solid *before* the QMX+ build depends on it.
- **A NanoVNA + this knowledge lets you characterize real hardware** — measure any filter or antenna's response, a hugely satisfying and practical capability for repair and design.

## Log

- Wound inductor: core, turns, measured L:
- Low-pass −3 dB cutoff: ___ MHz; stopband at 14 MHz: ___ dB down
- Band-pass center / bandwidth / insertion loss: ___ / ___ / ___
- Match before/after (SWR or reflection): ___ → ___
- Surprises / questions:
