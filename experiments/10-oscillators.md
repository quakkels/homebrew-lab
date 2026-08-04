# 10 — Oscillators (555 & RC)

- **Module:** 5 — Oscillators & Signals
- **Status:** Planned
- **Prerequisites:** [08 — Op-Amp Fundamentals](08-op-amp-fundamentals.md)
- **Est. time:** ~90 min

## Objective

Make a circuit generate its *own* signal instead of measuring an external one.
Build a 555 astable and an op-amp RC oscillator; measure frequency and see how
RC sets it.

## Concepts to be covered

- Feedback that sustains oscillation (the Barkhausen idea, informally).
- 555 astable: charge/discharge thresholds; frequency set by R and C (reuses Exp. 01).
- Relaxation vs sine oscillators; duty cycle.
- Op-amp relaxation oscillator and (optionally) a Wien-bridge sine oscillator.

## Planned procedure (sketch)

- Build a 555 astable; predict frequency from R/C, then measure it.
- Vary R (or a pot) and watch frequency track; check duty cycle.
- Build an op-amp oscillator; compare waveform quality.

## Parts & instruments

- NE555, LM358, resistors/pot, capacitors, scope.

## Why this matters (where you'll meet it)

Up to now you've *measured* signals; here a circuit **generates its own**. That's a
real conceptual milestone — oscillators are the source of every clock, tone, carrier,
and blink in existence.

- **The 555 is the most-used chip in history.** Knowing it means you can improvise
  timing, tones, blinkers, and PWM for any project without reaching for a
  microcontroller.
- **PWM is a superpower.** Varying a square wave's duty cycle is how you dim LEDs
  (your keyboard's backlight), control motor speed, and — conceptually — how
  class-D audio and the QMX+'s switching PA make power efficiently.
- **Feedback, seen from the other side.** Op-amps used feedback to *stabilize*;
  oscillators use feedback to *sustain*. Seeing both makes the whole idea of
  feedback click.
- **It sets up the crystal oscillator (Exp. 11)** — the difference between "an
  oscillator" and "an oscillator stable enough to trust on a ham band."

## Log

- 555 predicted vs measured frequency: 
- Duty cycle observed: 
- Surprises / questions: 
