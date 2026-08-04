# 09 — Active Filters

**Module:** 4 — Op-Amps
**Status:** Planned
**Prerequisites:** [08 — Op-Amp Fundamentals](08-op-amp-fundamentals.md), [02 — RC Filters](02-rc-filters.md)
**Est. time:** ~2 hours

## Objective

Combine op-amps with RC networks to build filters with gain and sharp, tunable
responses — including an audio band-pass like the ones used for CW reception.

## Concepts to be covered

- Active vs passive filters: gain, buffering between stages, no inductor needed.
- Sallen–Key low-pass/high-pass topology; setting cutoff and Q.
- Band-pass filters and their center frequency / bandwidth.
- A practical **CW audio filter** (~600–800 Hz) — directly useful with the QMX+.

## Planned procedure (sketch)

- Build a Sallen–Key low-pass; measure cutoff and compare to design.
- Build an audio band-pass centered near your preferred CW pitch; sweep and plot.
- Optionally drive it with real received audio and listen to the difference.

## Parts & instruments

- LM358 (or a TL072 if available), resistors, capacitors, signal generator, scope.

## Why this matters (where you'll meet it)

A filter decides *which frequencies you keep and which you throw away* — and that
turns out to be most of what signal processing is. Active filters do it with gain
and precise control, and without bulky, expensive inductors.

- **CW operating — you'll literally hear the difference.** A narrow audio
  band-pass around your CW pitch is the classic tool for pulling a weak signal out
  of a noisy band. This is the first experiment that builds something you'd
  actually *use on the air* with the QMX+ — and you'll be able to A/B "filter in
  vs. filter out" and hear a buried signal pop out.
- **It demystifies DSP.** The QMX+ does its filtering in *software* on the STM32.
  Building the analog equivalent here means that when you later read "the DSP
  applies a band-pass," you'll know exactly what operation the code is standing in
  for — the software and the op-amp are doing the *same thing*.
- **Every audio and mixed-signal system uses these.** Anti-aliasing filters before
  an ADC, reconstruction filters after a DAC, tone controls, sensor-noise
  smoothing — the same handful of op-amp filter topologies show up again and
  again.
- **Repair / schematic-reading.** The **Sallen–Key** stage you build here is one
  of the most common filter blocks in existence. Once you've built one, you'll
  *recognize it on sight* in other people's schematics and know what it does.
- **It ties the course together.** This is where Module 1 (RC/reactance) and
  Module 4 (op-amps) combine into something greater than either — the moment the
  fundamentals start compounding into real capability.

## Log

- Measured cutoff / center frequency vs design: 
- Bandwidth and Q: 
- Listening notes (if driven with audio): 
- Surprises / questions: 
