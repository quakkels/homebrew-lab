# 05 — A Linear Power Supply

- **Module:** 2 — Diodes & Power
- **Prerequisites:** [04 — Diodes & Rectification](04-diodes-and-rectification.md)
- **Est. time:** ~90 min

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Build the complete **rectify → smooth → regulate** chain and produce clean, stable 5 V DC from an AC source. Measure — with your own scope — how dramatically a regulator crushes ripple and holds the output steady as the load changes.

## Concepts introduced

- The full supply chain: AC source → bridge rectifier → reservoir cap → linear regulator → decoupled output.
- A **linear regulator** (78L05): what dropout, quiescent current, and heat mean.
- **Line** and **load** regulation, and **ripple rejection** (how much cleaner the output is than the input).
- **Decoupling capacitors** — why every IC on every board has a small cap right next to it (it's Experiment 01's RC acting as a local energy reservoir).

## Parts & instruments

- A **9–12 V AC** wall adapter *(labeled AC output — not DC)*, or any low-voltage AC source. **Never rectify wall mains directly.**
- 4 × **1N4007** (bridge) — or a packaged bridge rectifier
- **470 µF** electrolytic (reservoir), 2 × **0.1 µF** ceramic (decoupling)
- **78L05** regulator (TO-92, 100 mA)
- Load resistors: **1 kΩ**, **150 Ω**, **68 Ω** (to draw ~5 mA, ~33 mA, ~75 mA)
- Scope, multimeter

## Background (the why)

Experiment 04 got you bumpy DC with ripple. Real circuits need DC that is **flat** (no ripple to leak into your signal) and **stiff** (doesn't sag when the load changes). The linear supply gets there in four stages:

1. **Bridge rectifier** — four diodes that use *both* halves of the AC wave. Because it flips the negative half up instead of discarding it, the output pulses at **twice** the line frequency, which is easier to smooth. It costs **two** diode drops (~1.4 V) since current always flows through two diodes.
2. **Reservoir cap** — holds the peak between pulses. Full-wave ripple is:

   ```
   ΔV_ripple ≈ I_load / (2 · f_line · C)
   ```

   where **ΔV_ripple** = the leftover ripple voltage; **I_load** = the current the load draws (amps, A); **f_line** = the AC line frequency (hertz, e.g. 60); **C** = the reservoir capacitance (farads, F). The **× 2** is there because a bridge makes two humps per AC cycle (twice as many as half-wave), so the cap has half as long to sag.

3. **Regulator (78L05)** — actively watches its own output and adjusts to hold it at exactly 5 V, absorbing the ripple and any load changes. It needs its input to stay a bit above 5 V at all times — the **dropout voltage** (~1.7 V for a 78L05, so keep the input above ~7 V even at the ripple *troughs*).
4. **Decoupling caps** — small ceramics at the regulator's input and output (and later next to every chip) that supply fast current spikes the regulator can't react to quickly enough.

The magic number is **ripple rejection**: a 78L05 knocks ripple down by roughly **60 dB (≈1000×)**. A volt of ripple going in becomes a millivolt coming out — and you're going to *watch* that happen.

> ⚠️ **Safety:** Use only a low-voltage AC adapter. Electrolytic caps are polarized — backwards, they can vent or pop. The regulator gets warm; that's normal. When in doubt, verify against a datasheet (this file is AI-generated).

## Procedure

### Part A — Build the front end (bridge + reservoir)

1. Wire the four 1N4007s as a bridge; connect the AC adapter to the two **AC** corners. The **+** and **−** corners are your rectified output.

   ```
   AC ──►|──┬──►|── AC          top pair to +, bottom pair from −
        │   +    │
   AC ──|◄──┴──|◄── AC
            −
   ```

   *Diagram key:* the two `AC` corners connect to the AC adapter; `──►|──` and `──|◄──` are diodes (each triangle points the way it lets current flow, toward its bar/cathode); `+` and `−` are the DC output corners; `┬`/`┴` are junctions. Symbols: [glossary](../glossary.md).

2. Put the **470 µF** across + and − (**+ lead to the + corner**). Probe + with the scope on **AC coupling** and measure the ripple. With `I` small and `f_line = 60 Hz` (→ 120 Hz full-wave), a light load gives a few hundred mV of sawtooth. Note the DC level too (DC coupling): roughly `V_peak − 1.4 V`.

### Part B — Add the regulator

3. 78L05 pinout (flat facing you): **1 = Input, 2 = Ground, 3 = Output**. Feed the reservoir + into pin 1, ground pin 2, take 5 V from pin 3. Put a **0.1 µF** from pin 1 to ground and another from pin 3 to ground, close to the chip.
4. Connect a **1 kΩ** load from the 5 V output to ground. Confirm ~5.0 V on the meter.
5. **The payoff measurement:** scope on **AC coupling**, look at the *input* ripple (pin 1) then the *output* ripple (pin 3) at the same volts/div. The output ripple should nearly vanish — hundreds of mV in, ~1 mV out. That's ripple rejection you can see.

### Part C — Load regulation and dropout

6. Swap the load 1 kΩ → 150 Ω → 68 Ω (drawing more current each time) and watch the 5 V output on the meter. A good regulator barely moves — that's **load regulation**.
7. **Find dropout:** if your AC source is adjustable (or add series resistance), lower the input until the 5 V output starts to fall. That's the moment the input dropped below 5 V + dropout. Note the input voltage where it lets go.

## What to observe / measure

- Bridge + reservoir: a DC level with sawtooth ripple at **120 Hz** (twice line).
- Across the regulator: input ripple of hundreds of mV becomes output ripple of ~1 mV — a ~1000× improvement, visible only because you're using AC coupling.
- The 5 V output holds steady from light to ~75 mA load, then collapses once the input sags into dropout.

## The "aha"

You put a ragged, ripply, load-dependent voltage *in* and got a flat, stiff 5 V *out* — and you could point at exactly where each stage did its job. This is the mental model that lets you look at a dead device and reason "rectifier → reservoir → regulator," find the bulged cap or the dead regulator, and bring it back to life.

## Going further (experiments to try and log)

- **Under-size the reservoir.** Drop 470 µF → 10 µF and reload at 68 Ω. The input ripple troughs now dip into dropout and the 5 V output grows ripple — you've *caused* a real-world supply fault on purpose.
- **Feel the heat.** At 68 Ω the regulator drops (V_in − 5) volts × the load current as heat. Compute it, then carefully feel the package warm up. This is why bigger linear supplies need heatsinks — and why switching supplies exist.
- **Decoupling test.** Remove the output 0.1 µF and, later (after Exp. 10), feed the supply a fast-switching load; you'll see spikes the regulator can't catch. That little ceramic is doing real work.

## Why this matters (where you'll meet it)

Power is the most *universal* topic in electronics — every single thing you build, repair, or hack has a power supply, and a shockingly large fraction of the skill is in that one subsystem.

- **Repair / hardware-hacking — the single highest-yield skill.** A huge share of dead consumer electronics are dead *power supplies*: a bulged electrolytic cap, a failed regulator, a cracked solder joint on the rectifier. Once you can look at a supply and reason "rectifier → reservoir cap → regulator," you can revive a lot of "broken" gear that others throw away. This experiment is the mental model behind those repairs.
- **RF, specifically — supply noise becomes signal.** On a receiver, ripple and supply noise show up as audible hum, whine, or "birdies"; on a transmitter, they become spurious emissions that put junk on the air. A clean supply is a *performance* feature in radio, not just a housekeeping detail — the QMX+ cares a great deal, and so will anything you homebrew.
- **Decoupling capacitors — the "why is there a 100 nF next to every chip?"** This experiment answers that. It's the same RC idea from Exp. 01/02 acting as a local energy reservoir, and getting it wrong causes maddening intermittent bugs.
- **A scope skill you'll reuse constantly:** measuring small ripple riding on a big DC level using **AC coupling**. That "look at the tiny wiggle on top of the steady voltage" move comes up everywhere.
- **Foundation for what's next:** understanding a *linear* regulator is the stepping stone to switching supplies (buck/boost) — the things inside every USB charger and the 3.3 V rail on your future keyboard.

## Log

- Reservoir ripple (light load): ___ mV at 120 Hz
- Ripple in vs out across the 78L05: ___ mV → ___ mV (rejection ≈ ___×)
- Output voltage at 1 kΩ / 150 Ω / 68 Ω loads: ___ / ___ / ___ V
- Dropout: output fell when input reached ___ V
- Surprises / questions:
