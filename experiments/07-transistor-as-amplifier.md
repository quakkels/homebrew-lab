# 07 — Transistor as an Amplifier

- **Module:** 3 — Transistors
- **Status:** Planned
- **Prerequisites:** [06 — Transistor as a Switch](06-transistor-as-switch.md)
- **Est. time:** ~2 hours

## Objective

Bias a transistor into its *active* region and get voltage gain — the heart of
analog. Build a common-emitter amplifier, set its operating point, and measure
gain and clipping on the scope.

## Concepts to be covered

- The active region vs saturation/cutoff; the DC operating point (bias).
- Common-emitter amplifier: voltage gain ≈ −R_C/R_E, input/output coupling caps.
- Why bias stability matters; the emitter-degeneration trick.
- Clipping and distortion; headroom; input/output impedance.
- Small-signal vs large-signal thinking.

## Planned procedure (sketch)

- Build a single-transistor common-emitter stage; set the DC bias point and
  verify with the multimeter.
- Inject a small sine (from Exp. 02's generator); measure the output/input ratio.
- Increase input until it clips; observe on the scope; relate to headroom.

## Parts & instruments

- 2N3904, resistors, coupling capacitors, signal generator, scope (2 channels).

## Why this matters (where you'll meet it)

Amplification is the *other* half of the transistor, and it's the beating heart of
every receiver: turning a microvolt whisper from the antenna into something you can
actually hear.

- **Biasing is the skill that separates copying from designing.** Setting an
  operating point is the thing most self-taught people never really internalize —
  and it's exactly the intuition that turns schematics from "magic I follow" into
  "circuits I understand." This experiment is arguably the biggest single step in
  closing your analog gap.
- **It makes op-amps click.** An op-amp (next module) is just a very good amplifier
  wrapped in feedback. Having built gain the hard way, you'll *feel* what feedback
  buys you instead of taking the formulas on faith.
- **Every receiver, including the QMX+, is stages of gain.** Understanding one
  amplifier stage is understanding the building block they're all made of.
- **Repair / hacking:** recognizing a common-emitter stage and knowing where its DC
  voltages *should* sit lets you troubleshoot analog gear with a multimeter.
- **Clipping and headroom** intuition matters anywhere you push a signal too hard —
  audio distortion, overdriving an RF stage, ADC clipping.

## Log

- DC operating point (V_C, V_E, V_B): 
- Measured voltage gain: 
- Input level where clipping starts: 
- Surprises / questions: 
