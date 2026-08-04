# 00 — Bench & Instrumentation

- **Module:** 0 — The Bench
- **Status:** Ready
- **Prerequisites:** none
- **Est. time:** 1–2 hours (plus an ordering break for the parts kit)

## Objective

Get the workspace and instruments ready to *learn* — not just to build. By the
end you can produce a known test signal, measure it accurately, and trust your
numbers. Most of this course lives or dies on trusting the scope.

## Concepts introduced

- Probe compensation and the 10× vs 1× setting (what it does to bandwidth and loading).
- The scope's controls that matter for learning: timebase, volts/div, trigger,
  coupling (AC/DC), cursors, and automatic measurements.
- The probe-compensation output as a free ~1 kHz square-wave signal source.
- Making a reliable ground connection (and why a long ground lead lies to you at
  high frequency).

## Bench setup checklist

- [ ] Stable place for the scope where you can see it while your hands are on the breadboard.
- [ ] Good light and, ideally, a magnifier for small parts.
- [ ] Soldering iron with a clean, tinned tip; the QMX+ has a lot of toroids to wind.
- [ ] Anti-static habit if you're handling the QMX+'s STM32 / MOSFETs.
- [ ] A notebook or the **Log** sections in these files for recording results.

## Instrument warm-up (do this once)

1. **Probe check.** Set the probe to 10×. Clip it to the scope's probe-comp
   terminal (the little square-wave test point). Adjust the trimmer on the probe
   until the square wave has crisp, flat tops — no overshoot (too much) and no
   rounded corners (too little). You've done this; the point here is to *notice*
   what over/under-compensation looks like, because you'll see the same shapes
   caused by real circuits later.
2. **Know your free signal.** That probe-comp output is a real square wave,
   typically ~1 kHz at 3–5 V. Measure its frequency and amplitude with the
   scope's automatic measurements and write them in the Log — this is the source
   for Experiments 01 and 02.
3. **AC vs DC coupling.** Switch coupling between DC and AC while viewing the
   square wave and watch the trace shift. DC shows the true level; AC removes the
   average and centers the signal. You'll use AC coupling to see small ripple
   riding on a big DC voltage in the power-supply module.
4. **Cursors.** Practice putting time cursors on one period and voltage cursors
   across the amplitude. You'll measure a time constant this way in Experiment 01.

## Multimeter warm-up

- Measure a few resistors and compare to their color codes / markings.
- Measure the probe-comp output's *DC average* on the meter and compare to what
  the scope shows — a square wave's average is not its peak. Note the difference.

## Starter parts kit — bill of materials

You can buy these as a bundle or individually. Quantities are "enough to play."

| Category | Specific parts | Why |
|---|---|---|
| Resistors | Assortment 10 Ω–1 MΩ, 1/4 W (esp. 1 k, 10 k, 100 k) | Everything |
| Ceramic caps | 100 pF, 1 nF, 10 nF, 100 nF | RC/filters, decoupling |
| Electrolytic caps | 1 µF, 10 µF, 100 µF, 470 µF | Power supply, audio |
| Inductors | 100 µH, 1 mH, plus a few toroids (T37-x) | RL, LC resonance, RF |
| Diodes | 1N4148 (signal), 1N4007 (power), a Schottky (1N5817) | Rectification, detectors |
| LEDs | a few, any color | Indicators, visible current |
| Transistors | 2N3904 (NPN), 2N3906 (PNP), 2N7000 (N-MOSFET) | Switch & amplifier |
| ICs | LM358 (op-amp), NE555 (timer), 78L05 (regulator) | Op-amps, oscillators, power |
| Trimmer pot | 10 k | Biasing, adjustable dividers |
| Misc | breadboard jumper kit, 9 V battery + clip, alligator leads | Wiring |

- **Later, for the RF modules and QMX+ work:** a NanoVNA, a small assortment of
toroid cores (T37-2, T37-6, FT37-43), enameled wire, and some crystals.

## The "aha"

The scope isn't a meter that shows one number — it's a *window into time*. Once
you can make a known signal and measure it with cursors, every later experiment
becomes "predict the shape, then look." That predict-then-look habit is the whole
game.

## Going further

- Find your scope's bandwidth and sample-rate specs and note them — they set the
  ceiling on what you can trust at RF frequencies later.
- Read the QMX+ assembly manual's parts-inventory section and lay out its parts;
  it's a good habit before a big build and previews components you'll meet here.

## Log

Record what you measured (fill in as you go):

- Probe-comp frequency (scope): 
- Probe-comp amplitude (scope, pk-pk): 
- Probe-comp DC average (multimeter): 
- Scope bandwidth / max sample rate: 
- Notes / surprises: 
