# 03 — Inductors & LC Resonance

- **Module:** 1 — Passives & Time
- **Status:** Planned
- **Prerequisites:** [02 — RC Filters](02-rc-filters.md)
- **Est. time:** ~90 min

## Objective

Meet the inductor as the capacitor's mirror image, then combine L and C into a
**resonant circuit** — the single most important idea in all of radio. Measure a
resonant peak and match it to `f = 1/(2π√(LC))`.

## Concepts to be covered

- Inductor resists *changes in current* (mirror of the capacitor's voltage rule);
  `V = L·di/dt`. Reactance `X_L = 2πfL` rises with frequency.
- RL time constant `τ = L/R` — the inductor analog of Experiment 01.
- **LC resonance:** energy sloshing between L and C; the resonant frequency
  `f₀ = 1/(2π√(LC))`.
- **Q** (sharpness) of the resonance and why high-Q = selective.
- Series vs parallel resonant circuits (tank).

## Planned procedure (sketch)

- RL step response on the scope (mirror of Exp. 01).
- Sweep a series LC with the generator; find and measure the resonant dip/peak.
- Compute f₀ from measured L and C; compare to the observed peak.
- Estimate Q from the −3 dB bandwidth.

## Parts & instruments

- Assorted inductors / a toroid you wind yourself, a known capacitor, resistor,
  signal generator, scope. A NanoVNA makes the resonance measurement trivial and
  is worth introducing here.

## Why this matters (where you'll meet it)

Resonance is *the* central idea in all of radio. As a ham you already feel it —
tuning an antenna, a resonant trap, the sharpness of a filter — but here you build
it, see it, and measure it directly for the first time.

- **It's how a radio picks one station out of thousands.** Every band-pass and
  band-reject filter, every oscillator's frequency-setting element, and every
  antenna match is LC resonance. Selectivity *is* resonance.
- **Q makes it real.** The "sharpness" you'll measure is exactly the difference
  between a filter that cleanly separates signals and one that's mushy — the same
  Q that decides how tightly your receiver rejects the station next door.
- **You make the component yourself.** Inductors are the one part you *wind* by
  hand. The toroid-winding skill you start here is a hard requirement for the
  QMX+ build (its filters are hand-wound toroids).
- **Direct prerequisite** for Module 6 (RF filters, impedance) and for
  understanding — and aligning — the QMX+ filters.

## Log

- Winding details (core, turns, measured L): 
- Measured f₀ vs computed f₀: 
- Estimated Q: 
- Surprises / questions: 
