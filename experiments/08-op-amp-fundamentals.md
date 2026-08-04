# 08 — Op-Amp Fundamentals

**Module:** 4 — Op-Amps
**Status:** Planned
**Prerequisites:** [07 — Transistor as an Amplifier](07-transistor-as-amplifier.md)
**Est. time:** ~90 min

## Objective

Use an op-amp to get precise, predictable gain set by two resistors — the moment
analog design stops being fiddly. Build inverting, non-inverting, and buffer
configurations and measure their gain.

## Concepts to be covered

- The two "golden rules" of ideal op-amps (no input current; inputs driven equal
  by feedback) and how negative feedback enforces them.
- Inverting (`−R_f/R_in`), non-inverting (`1 + R_f/R_in`), and unity buffer.
- Input/output impedance benefits; why a buffer fixes loading problems.
- Real-world limits: supply rails, output swing, single- vs dual-supply (LM358).

## Planned procedure (sketch)

- Non-inverting amp with a chosen gain; verify output/input ratio.
- Inverting amp; confirm the 180° phase flip on the scope.
- Buffer a high-impedance source and show it no longer sags under load.

## Parts & instruments

- LM358, resistors, signal generator, scope.

## Why this matters (where you'll meet it)

This is the experiment where analog design suddenly gets *easy*. After wrestling
with transistor biasing, an op-amp hands you precise gain set by two resistors, with
formulas that just work — it's a genuine morale boost and a turning point.

- **The workhorse of all analog signal handling.** The QMX+ uses op-amps right
  after its quadrature detector to boost tiny received signals before the ADC —
  you'll be looking at that exact role.
- **Buffering solves a problem you'll hit constantly:** "my circuit sags when I
  connect the next stage to it." An op-amp buffer makes stages stop loading each
  other — one of the most practically useful tricks in the whole course.
- **Precision without fuss:** gain, summing, difference, comparison — all become
  clean design problems instead of biasing puzzles. This is where "designing"
  starts to feel achievable.
- **Direct prerequisite for the active filters (Exp. 09)**, including the CW audio
  filter you'd actually use on the air.
- **Schematic-reading / repair:** the inverting and non-inverting configs are so
  common that recognizing them on sight is a core literacy skill.

## Log

- Measured gains vs designed (non-inv, inv): 
- Buffer before/after loading: 
- Surprises / questions: 
