# 13 — Mixers & Detectors

- **Module:** 6 — RF Fundamentals
- **Prerequisites:** [12 — LC Filters & Impedance Matching](12-lc-filters-and-impedance-matching.md), [11 — Crystal Oscillator](11-crystal-oscillator.md)
- **Est. time:** ~2–3 hours

## Objective

Build the two operations at the heart of every radio: **detection** (recovering audio from a carrier) and **mixing** (shifting a signal to a new frequency). Hear a station on a crystal-set detector you built, watch a mixer produce sum and difference frequencies, and then read the QMX+'s quadrature receiver as something you understand.

## Concepts introduced

- **Envelope detection** — the crystal-radio diode detector (reuses Module 2).
- **Mixing = multiplication** → sum and difference frequencies; the superheterodyne idea.
- **Direct conversion**, **I/Q**, and the **quadrature sampling detector (QSD)**.
- How a **switching mixer + op-amp + DSP** becomes an SDR — i.e., the QMX+ receiver.
- **Image frequencies** and why filtering (Exp. 12) has to come *before* mixing.

## Parts & instruments

- Detector: a germanium/Schottky diode (**1N34** or **1N5817**), a tuning LC from Exp. 12 for the AM/SW band, a **10 nF** cap, **high-impedance** earpiece (crystal earphone), and a wire antenna + ground
- Mixer: an **SA612/NE602** mixer IC (easiest) *or* a diode-ring/FET switch, plus your Exp. 11 crystal oscillator as the local oscillator
- Scope, and (very helpful) an **SDR dongle** for a spectrum/waterfall view

## Background (the why)

A radio has to do two things a wire alone can't: **get the information back out of a high-frequency carrier**, and **move signals up or down in frequency** so they can be filtered and processed. Those are detection and mixing.

**Detection (envelope).** An AM signal is a carrier whose *amplitude* wiggles with the audio. A diode (one-way valve, Exp. 04) plus a small cap follows the **envelope** of that wiggle and throws away the carrier — leaving the audio. That's the entire crystal radio: an antenna, a resonant LC to pick one station (Exp. 03/12), a diode, a cap, and an earpiece. No battery, no amplifier — just physics.

**Mixing (frequency shifting).** Multiply two sine waves and trigonometry hands you **two new frequencies**: their sum and their difference.

```
cos(A) · cos(B) = ½[cos(A−B) + cos(A+B)]
```

Feed a received signal at `f_RF` and a local oscillator at `f_LO` into a mixer and you get `f_RF − f_LO` and `f_RF + f_LO`. Pick off the **difference** and you've slid a station down to a low, easy-to-process frequency. Do it once to a fixed intermediate frequency and you have the **superheterodyne** receiver behind almost every radio since the 1930s. Shift it all the way down to *audio* (LO = signal frequency) and you have a **direct-conversion** receiver.

**I/Q and the QSD.** A single mixer can't tell a signal *above* the LO from one an equal distance *below* it — the dreaded **image**. The fix is to mix with **two** LO copies 90° apart, producing two outputs called **I** and **Q**. From I and Q, math (analog or, in an SDR, software) can separate the two sides and demodulate any mode. The **quadrature sampling detector** — a set of analog switches clocked by the LO at 0°/90°/180°/270°, dumping into capacitors and op-amps — is the elegant, cheap way to get I and Q, and it is exactly the QMX+'s front end.

## Procedure

### Part A — Build a crystal-set detector and hear a station

1. Connect a long wire antenna and a ground. Tune it with an LC tank (Exp. 12) to the AM broadcast or a strong shortwave band.
2. From the top of the tank: **diode** → node → **10 nF to ground** → **crystal earpiece to ground**.

   ```
   ANT ─┬─[ L ]─┬──►|──┬────────┬── earpiece ── GND
        │       │   diode│     │
       (tune)  GND    [10nF]  (audio out)
                         │
                        GND
   ```

3. Adjust the tuning. With a decent antenna you'll **hear a station** — audio pulled from the air with no power source. Detection, made real.

### Part B — Mixing: make sum and difference frequencies

4. Wire an **SA612** mixer: RF input from a signal generator at, say, **1.0 MHz**; local oscillator from your Exp. 11 crystal oscillator (or the SA612's built-in oscillator) at, say, **1.1 MHz**.
5. Look at the mixer output on the scope, and ideally on an **SDR/spectrum** view. You should find products at the **difference (100 kHz)** and the **sum (2.1 MHz)**, plus feedthrough of the originals.
6. Put a **low-pass** (Exp. 12) on the output to keep only the 100 kHz difference — you've just down-converted a signal, the core move of every superhet.

### Part C — Read the QMX+ receiver

7. Open the QMX+ schematic. Walk the receive path and label each block with what you built: **band-pass filter** (Exp. 12) → **QSD switching mixer** clocked by the **Si5351** (Exp. 11) → **I/Q op-amp gain** (Exp. 08) → **STM32 DSP** (the digital demodulation/filtering, the software twin of Exp. 09). The whole front end should now read as a sequence of things you understand.

## What to observe / measure

- The crystal set produces faint but real audio, tuning to different stations as you adjust the LC.
- The mixer output contains clear **sum** and **difference** tones (plus the originals), and the low-pass isolates the difference.
- The QMX+ receive chain maps, block for block, onto experiments you've done.

## The "aha"

You pulled a human voice out of thin air with a diode and an earpiece — the whole history of radio compressed into five parts — and then you took two frequencies and *made a third on purpose*. The QSD in your QMX+ stops being a mysterious block labeled "detector" and becomes "switches clocked at four phases, feeding op-amps, feeding DSP" — every piece of which you have now built with your own hands.

## Going further (experiments to try and log)

- **Direct-conversion CW.** Set the LO right at a CW signal's frequency; the difference lands in the audio range and you hear the Morse tone directly. Add the Exp. 09 CW band-pass and you've built a minimal receiver.
- **See the image.** With the SDR, inject a signal equally above and below the LO and watch both appear on top of each other from a single-ended mixer — then reason about how I/Q would separate them.
- **Measure conversion loss/gain.** Compare input and output levels through the mixer; passive mixers *lose* signal, active ones (SA612) give gain — a real design trade.

## Why this matters (where you'll meet it)

These are **the two operations at the heart of every radio**: *detection* (getting the information back out of a carrier) and *mixing* (shifting a signal to a new frequency). Understand these two and radios stop being magic.

- **You'll hear where radio began.** A diode envelope detector recovers audio from a station with almost no parts — connect it to one of your antennas and listen. It's a direct line from a crystal set to a modern SDR.
- **Mixing is the superheterodyne principle** behind essentially every receiver built since the 1930s: multiply two signals, get their sum and difference, and shift a station down to a frequency you can process.
- **The QSD is the QMX+'s (and every SDR's) front end.** The quadrature sampling detector and I/Q signals you meet here are exactly how your radio's receiver works — this experiment is what makes its schematic *readable* to you.
- **Payoff:** after this, the whole QMX+ receive path is legible, stage by stage — the stated goal of the entire RF module, and the moment your ham hobby and your circuit knowledge fully merge.

## Log

- Envelope detector — station heard / signal recovered:
- Mixer sum & difference frequencies observed: ___ / ___
- QMX+ receive-path stages identified:
- Surprises / questions:
