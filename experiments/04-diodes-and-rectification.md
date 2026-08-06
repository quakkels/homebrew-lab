# 04 — Diodes & Rectification

- **Module:** 2 — Diodes & Power
- **Prerequisites:** [02 — RC Filters](02-rc-filters.md)
- **Est. time:** ~60 min

## Objective

Meet the diode as a one-way valve for current, measure its forward voltage drop with your own meter, then use it to turn an AC sine wave into (pulsating, then smoothed) DC on the scope. This is the first genuinely *nonlinear* part in the course, and the front end of every power supply and every radio detector.

## Concepts introduced

- The diode conducts one way and blocks the other; the ~0.6–0.7 V silicon **forward drop** (≈0.2–0.3 V for a Schottky).
- **Rectification:** keeping only one polarity of a swinging signal.
- A **reservoir capacitor** turns pulsating DC into nearly-flat DC with a little leftover **ripple** — and the ripple size is set by the same RC idea from Exp. 01.
- The diode as a **steering/protection** element (the seed of the keyboard matrix and the relay flyback diode in Exp. 06).

## Parts & instruments

- 1 × **1N4148** (small-signal Si) and 1 × **1N4007** (rectifier Si)
- 1 × **1N5817** (or any Schottky) for comparison
- 1 × **10 kΩ** resistor (load), assorted caps: **1 µF**, **10 µF**
- Signal generator (or the probe-comp square wave as a rough AC source), scope, multimeter with a **diode-test** setting

## Background (the why)

A resistor obeys Ohm's law — double the voltage, double the current, in either direction. A **diode breaks that symmetry.** Current flows freely when the anode is more positive than the cathode (forward bias), and is blocked when reversed. The catch is that forward conduction costs a roughly fixed **forward voltage**:

```
silicon diode:    ≈ 0.6–0.7 V
Schottky diode:   ≈ 0.2–0.3 V   (less drop = less wasted power/heat)
```

That drop is nearly constant over a wide current range, which is why "0.7 V" is a number you'll carry in your head forever as a sanity-check landmark.

**Rectification** uses this one-way behavior to throw away half of an AC wave. Feed a sine through a single diode into a load and only the positive humps survive (minus the 0.7 V it costs to turn the diode on) — that's **half-wave** rectification. The output is bumpy DC: always ≥ 0, but far from steady.

To smooth it, park a **reservoir capacitor** across the load. The cap charges up on each hump and then holds the voltage while the diode is off, discharging slowly into the load. What's left is a small sawtooth **ripple** riding on a DC level. Its size is:

```
ΔV_ripple ≈ I_load / (f · C)          (half-wave)
```

Bigger cap or higher frequency → smaller ripple. This is literally Experiment 01's `τ = RC` again: the cap and load form an RC that must discharge *slowly* compared to the time between humps.

## Procedure

### Part A — Measure the forward drop

1. Set the multimeter to **diode-test**. Put the red lead on the anode, black on the cathode (the banded end). Read the forward drop.
2. Record it for the **1N4148**, the **1N4007**, and the **Schottky**. Expect ~0.6–0.7 V for the silicon parts and ~0.2–0.3 V for the Schottky.
3. Reverse the leads: the meter should read open (no conduction). You've just confirmed the one-way behavior directly.

### Part B — Half-wave rectifier on the scope

4. Build: signal generator (say **4 V peak-to-peak sine, ~1 kHz**) → diode → node → 10 kΩ to ground. Probe the node.

   ```
   GEN ──►|──┬── probe tip        (►| = diode, band toward the node)
        1N4148│
            [ 10kΩ ]
              │
             GND ── probe ground clip
   ```

5. Set the scope to show a couple of cycles. You should see **only the positive humps**, each starting about **0.6 V lower** than the input (the diode's toll). The negative half of the sine is simply gone.

### Part C — Add a reservoir cap and measure ripple

6. Place **1 µF** across the 10 kΩ load (watch polarity if electrolytic: + to the node). The bumpy output jumps up toward the peak and holds — now it's *almost* flat with a **sawtooth ripple**.
7. Switch the scope input to **AC coupling** and turn up volts/div to zoom in on just the ripple. Measure its peak-to-peak size.
8. Predict it: with ~3 V across 10 kΩ, `I_load ≈ 0.3 mA`, `f = 1 kHz`, `C = 1 µF` → `ΔV ≈ 0.3 mA / (1 kHz × 1 µF) ≈ 0.3 V`. Compare to what you see.
9. Swap **1 µF → 10 µF**. Ripple should shrink by ~10× (to ~30 mV). Bigger reservoir = smoother DC, exactly as the formula says.

## What to observe / measure

- The diode-test numbers: silicon ~0.65 V, Schottky ~0.25 V, open when reversed.
- Half-wave: negative half of the sine vanishes; positive humps are offset down by one forward drop.
- With a reservoir cap: a mostly-DC level with a sawtooth ripple that **shrinks as C grows**, tracking `ΔV ≈ I/(fC)`.

## The "aha"

A single 3-cent part turned a symmetric AC wave into one-directional DC, and a capacitor turned *that* into something you could almost call a battery. You can see the ripple, and you can *predict its size* from the same RC relationship you measured in Experiment 01. Every wall-wart on your bench does exactly this inside.

## Going further (experiments to try and log)

- **Full-wave bridge (concept + preview).** Four diodes in a bridge use *both* halves of the wave, doubling the ripple frequency and halving the ripple. It needs a *floating* (isolated) source, so we build the real thing with a transformer in Experiment 05 — but sketch the bridge now and predict its output.
- **Schottky vs silicon in the rectifier.** Rebuild Part B with the Schottky and watch the output humps sit ~0.4 V higher (less drop). In a low-voltage supply that saved 0.4 V matters.
- **The steering idea.** Point two diodes' cathodes at a common node from two sources — the higher source "wins." This OR-ing/steering behavior is exactly how a diode stops **ghosting** in the keyboard matrix (Exp. 14) and how a battery backup takes over. Rig it and confirm.

## Why this matters (where you'll meet it)

The diode is the simplest device that *does* something nonlinear — a one-way valve for current — and that one trick shows up in a surprising number of places.

- **Every power supply starts here.** Turning AC into DC (rectification) is step one of Exp. 05 and of literally every mains-powered device you'll build or repair.
- **It's how radio began.** A diode "envelope detector" is the entire front end of a crystal radio — you'll build one in Exp. 13 and recover audio from a carrier with almost no parts. Detection is one of the two core radio operations.
- **Steering and protection.** Diodes block current going the wrong way — which is exactly what stops "ghosting" in your **keyboard matrix**, protects circuits from a reversed battery, and tames the inductive spike from a relay (the flyback diode in Exp. 06).
- **Repair win.** A shorted or open rectifier diode is one of the most common faults in dead gear; the diode-test on your multimeter finds it in seconds.
- **A number you'll carry forever:** the ~0.6–0.7 V silicon forward drop becomes a mental landmark you'll use to sanity-check circuits at a glance.

## Log

- Measured forward drops — 1N4148: ___ V, 1N4007: ___ V, Schottky: ___ V
- Half-wave output: peak height vs input, offset observed:
- Ripple with 1 µF: ___ mV (expected ~300 mV); with 10 µF: ___ mV (expected ~30 mV)
- Surprises / questions:
