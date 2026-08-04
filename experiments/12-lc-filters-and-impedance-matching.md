# 12 — LC Filters & Impedance Matching

**Module:** 6 — RF Fundamentals
**Status:** Planned
**Prerequisites:** [03 — Inductors & LC Resonance](03-inductors-and-lc-resonance.md), [02 — RC Filters](02-rc-filters.md)
**Est. time:** ~2–3 hours

## Objective

Build the real filters radios use — sharp LC low-pass and band-pass filters — and
learn impedance matching, the concept that makes power actually transfer between
stages and to an antenna. This maps directly onto the QMX+'s band-pass and
low-pass filter banks.

## Concepts to be covered

- Multi-pole LC low-pass filters (the harmonic filters on a transmitter output).
- Band-pass filters for receiver front ends; insertion loss and shape.
- **Impedance** as a first-class idea; why 50 Ω; maximum power transfer.
- L-networks and matching; the antenna-match connection to your existing antenna work.
- Winding toroids accurately and measuring the result (NanoVNA shines here).

## Planned procedure (sketch)

- Wind and build a low-pass filter for one ham band; sweep it (NanoVNA or
  generator + scope) and measure cutoff and stopband depth.
- Build a simple band-pass; measure center frequency and bandwidth.
- Do an L-network match between two different impedances; verify the improvement.

## Parts & instruments

- Toroid cores (T37-2/T37-6), enameled wire, RF-suitable capacitors, NanoVNA
  (strongly recommended), scope, signal source.

## Why this matters (where you'll meet it)

This is the **deepest bridge between your ham background and circuit design**. You
already tune antennas and watch SWR; here you build the filters and matching
networks that make all of that work — and measure them.

- **Impedance matching finally becomes mechanical, not magical.** Maximum power
  transfer is *why* we use 50 Ω, why a mismatch reflects power back, and why an
  antenna tuner exists. After this, SWR is something you understand from the
  inside.
- **The QMX+'s filter banks ARE this experiment.** Its receive band-pass filters
  and transmit low-pass (harmonic) filters are exactly the LC filters you'll build
  here — so this is what lets you align and troubleshoot your radio instead of
  just following the manual.
- **Toroid winding gets good here.** Accurate hand-wound inductors are the
  make-or-break homebrew skill, and you want it solid *before* the QMX+ build
  depends on it.
- **A NanoVNA + this knowledge lets you characterize real hardware** — measure any
  filter or antenna's response, a hugely satisfying and practical capability for
  repair and design.

## Log

- Filter measured cutoff / center vs design: 
- Stopband attenuation: 
- Match before/after (SWR or reflection): 
- Surprises / questions: 
