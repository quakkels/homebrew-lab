# 03 — Inductors & LC Resonance

- **Module:** 1 — Passives & Time
- **Prerequisites:** [02 — RC Filters](02-rc-filters.md)
- **Est. time:** ~90 min

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Meet the inductor as the capacitor's mirror image, then combine L and C into a **resonant circuit** and watch it *ring* on the scope. You'll measure the ringing frequency and match it to

```
f₀ = 1 / (2π√(LC))
```

where **f₀** = the resonant frequency, **L** = inductance, **C** = capacitance (each defined in full in the Background section below).

using nothing more than your scope and its square-wave source. This one measurement is the seed of every filter, oscillator, and antenna match in radio.

## Concepts introduced

- An inductor resists *changes in current* — the exact mirror of a capacitor resisting changes in voltage. `V = L · di/dt`.
- Inductive reactance `X_L = 2πfL` **rises** with frequency (a capacitor's `X_C = 1/(2πfC)` **falls**). They cross somewhere — that crossing is resonance.
- The RL time constant `τ = L/R` (the inductor analog of Experiment 01's `τ = RC`).
- **LC resonance:** energy sloshing back and forth between the inductor's magnetic field and the capacitor's electric field, at `f₀ = 1/(2π√(LC))`.
- **Q** (quality factor): how many times the energy sloshes before losses damp it out. High Q = sharp, selective resonance.

## Parts & instruments

- 1 × inductor, **1 mH** (a small axial/moulded choke is fine; 100 µH also works, see the note in Going Further)
- 1 × **10 nF** ceramic capacitor
- 1 × **100 Ω** resistor (for the RL part) and 1 × **1 kΩ** resistor (to drive the tank)
- Breadboard, scope, and the probe-comp square-wave output as the source. A function/signal generator is *nice* here but not required.

## Background (the why)

**The inductor is the capacitor turned inside out.** A capacitor stores energy in an electric field and fights changes in *voltage*. An inductor stores energy in a magnetic field and fights changes in *current*:

```
capacitor:  i = C · dV/dt        inductor:  V = L · di/dt
```

where **i** = current (amps, A); **V** = voltage (volts); **C** = capacitance (farads, F); **L** = inductance (henries, H); **dV/dt** and **di/dt** are shorthand for "how fast the voltage / current is changing." In words: the current into a capacitor depends on how fast its voltage changes; the voltage across an inductor depends on how fast its current changes.

Everything you learned in Experiment 01 has a mirror image here. Where the RC circuit had `τ = RC`, the RL circuit has:

```
τ = L / R
```

where **τ (tau)** = the time constant, in seconds; **L** = inductance (H); **R** = resistance (Ω).

**Reactance — the frequency-dependent "resistance."** A capacitor passes high frequencies easily (`X_C` falls as `f` rises); an inductor blocks them (`X_L` rises as `f` rises):

```
X_L = 2πfL          X_C = 1 / (2πfC)
```

where **X_L**, **X_C** = the inductor's and capacitor's **reactance** (their frequency-dependent opposition to AC), in ohms (Ω); **f** = frequency (Hz); **L** = inductance (H); **C** = capacitance (F); **π** ≈ 3.14159.

Put an L and a C together and there is exactly one frequency where `X_L = X_C`. At that frequency they cancel, and the pair behaves in a dramatic way — it **resonates**. Setting `2πfL = 1/(2πfC)` and solving for `f` gives the single most important formula in radio:

```
f₀ = 1 / (2π√(LC))
```

where **f₀** = the resonant frequency, in hertz (Hz); **L** = inductance (H); **C** = capacitance (F); **√** = square root; **π** ≈ 3.14159.

With **L = 1 mH** and **C = 10 nF**:

```
√(LC) = √(1×10⁻³ × 10×10⁻⁹) = √(1×10⁻¹¹) ≈ 3.16×10⁻⁶
f₀    = 1 / (2π × 3.16×10⁻⁶) ≈ 50.3 kHz     (period ≈ 19.9 µs)
```

(This just plugs L = 1 mH and C = 10 nF into the formula above. The result, 50.3 kHz, is the frequency the tank rings at; its **period** — the time for one cycle — is 19.9 µs, or about 20 millionths of a second.)

**Why it "rings."** If you hit an LC pair with a sudden voltage step, energy pours into the cap, then flows into the inductor, then back into the cap, and so on — a pendulum swinging between two forms of energy. On the scope you see a decaying sine wave at `f₀`. Each cycle loses a little energy to resistance, so the ringing dies out. **How slowly it dies is Q:** a high-Q tank rings for many cycles; a lossy one barely rings at all. This is *exactly* the mechanism a receiver uses to ring up on the station you want and ignore the rest.

## Procedure

### Part A — The inductor's time constant (RL, the mirror of Exp. 01)

1. **Build a series RL:** square wave → 100 Ω resistor → inductor → ground. Probe the node *between the resistor and the inductor* (tip on the R/L node, ground clip on the source ground). The voltage there swings as the inductor charges, and the resistor current — hence this node's voltage — follows an exponential.

   ```
   CAL out ──[ 100Ω ]──┬── probe tip
                       │
                     [ L 1mH ]
                       │
                      GND ── probe ground clip
   ```

   *Diagram key:* `CAL out` = the scope's square-wave calibration output (used here as the source); `[ 100Ω ]` = a 100-ohm resistor; `[ L 1mH ]` = a 1-millihenry inductor; `┬` = a junction; `GND` = ground. Full symbol list in the [glossary](../glossary.md).

2. **Set the scope:** timebase ~5 µs/div, trigger on the rising edge. Expect `τ = L/R = 1×10⁻³ / 100 = 10 µs`.
3. **Watch the current ramp.** At a voltage step the inductor initially blocks current (it hates sudden change), so the current — and the voltage across R — ramps up exponentially over ~5τ, then holds. It's Experiment 01's curve, driven by the *opposite* physical law.

   > **Bench reality:** the probe-comp output has its own source resistance, which adds to your 100 Ω and stretches τ. Don't fight it — just measure the actual τ you see and note that the *shape* is the point. A 50 Ω function generator, if you have one, gives a cleaner number.

### Part B — Make an LC tank ring (the main event)

4. **Build a parallel LC tank driven through a resistor:**

   ```
   CAL out ──[ 1kΩ ]──┬─────────┬── probe tip
                      │         │
                   [ L 1mH ] [ C 10nF ]
                      │         │
                     GND ─────GND ── probe ground clip
   ```

   *Diagram key:* `[ 1kΩ ]` = resistor; `[ L 1mH ]` = inductor; `[ C 10nF ]` = capacitor (the inductor and capacitor sit side by side = wired in parallel, forming the "tank"); `┬` = junction; `GND` = ground. Symbols: [glossary](../glossary.md).

   L and C are in parallel (a "tank"); the 1 kΩ feeds it from the square wave and keeps the source from swamping the ringing.
5. **Set the scope:** timebase ~5 µs/div, trigger on the rising edge, and turn the volts/div up until you can see fine detail on each square-wave edge.
6. **Find the ring.** On every edge of the square wave you should see a **decaying sine wave** — the tank ringing. If you don't see it, slow the source down or increase volts/div; the ring sits on top of each transition.
7. **Measure f₀.** Put time cursors on two adjacent ring peaks to get the period `T`, then `f₀ = 1/T`. Expect `T ≈ 20 µs`, so `f₀ ≈ 50 kHz`. Compare to the `50.3 kHz` you computed.
8. **Estimate Q from the decay.** Count how many complete ring cycles it takes for the amplitude to fall to roughly **one-third** (≈37%) of the first peak. Call that `N`. Then:

   ```
   Q ≈ π × N
   ```

   where **Q** = the quality factor (higher = a sharper, longer-ringing resonance); **N** = the number of ring cycles you counted; **π** ≈ 3.14159.

   A clean 1 mH choke and a good cap will give you maybe N ≈ 3–10 cycles, i.e. Q ≈ 10–30.

## What to observe / measure

- **Part A:** a square edge turns into an exponential *ramp* — the inductor's current can't jump, just as the capacitor's voltage couldn't in Exp. 01.
- **Part B:** each square edge kicks off a **damped sine wave** at ~50 kHz. This is the first time in the course a circuit produces an *oscillation* on its own.
- The measured ring frequency lands within a few percent of `1/(2π√(LC))`.
- A higher-Q tank rings longer; deliberately adding series resistance kills the ring — you can *see* Q.

## The "aha"

You hit two inert parts with a single voltage step and they **sang** — a clean tone at a frequency you predicted from `√(LC)` in your head. That ringing is not a curiosity: it is the physical heart of every tuned circuit, every oscillator, and every filter you'll build for the rest of this course. Resonance just stopped being a word and became something you can point at on a screen.

## Going further (experiments to try and log)

- **Change C and re-predict.** Swap 10 nF → 1 nF. `f₀` should rise by √10 ≈ 3.16×, to ~159 kHz. Predict the new period *before* you look.
- **Deliberately spoil Q.** Add a 100 Ω resistor in series with the inductor. The ring dies in far fewer cycles — you've just lowered Q on purpose and watched selectivity drain away.
- **Series vs parallel.** Rebuild L and C *in series* to ground and probe across the pair. A series-resonant circuit is a near-*short* at f₀ (a notch/trap) instead of a peak — the same math, the inverse behavior. Traps on an antenna work exactly this way.
- **Wind your own inductor (preview of Module 6).** Wind ~30 turns of enameled wire on a T37-2 toroid core and measure its ringing against a known cap. Hand-wound toroids are the make-or-break homebrew skill, and the QMX+'s filters are nothing but these. Getting comfortable now pays off directly at Experiment 12.
- **If you have a generator or NanoVNA:** instead of ringing, *sweep* the frequency and watch the tank's response peak (parallel) or dip (series) at f₀, and read Q from the −3 dB bandwidth: `Q = f₀ / Δf`. This is the "frequency-domain" view of the same resonance you just rang in the time domain.

## Why this matters (where you'll meet it)

Resonance is *the* central idea in all of radio. As a ham you already feel it — tuning an antenna, a resonant trap, the sharpness of a filter — but here you build it, see it, and measure it directly for the first time.

- **It's how a radio picks one station out of thousands.** Every band-pass and band-reject filter, every oscillator's frequency-setting element, and every antenna match is LC resonance. Selectivity *is* resonance.
- **Q makes it real.** The "sharpness" you'll measure is exactly the difference between a filter that cleanly separates signals and one that's mushy — the same Q that decides how tightly your receiver rejects the station next door.
- **You make the component yourself.** Inductors are the one part you *wind* by hand. The toroid-winding skill you start here is a hard requirement for the QMX+ build (its filters are hand-wound toroids).
- **Direct prerequisite** for Module 6 (RF filters, impedance) and for understanding — and aligning — the QMX+ filters.

## Log

- Part A — measured RL τ: ______ µs (expected ~10 µs, plus source resistance)
- Winding details, if you wound one (core, turns, measured/ringing L):
- Part B — measured ring period T: ______ µs → f₀ = ______ kHz (expected ~50 kHz)
- Cycles to decay to ~1/3 (N): ______ → Q ≈ π·N = ______
- f₀ with 1 nF instead of 10 nF: ______ kHz (expected ~159 kHz)
- Surprises / questions:
