# 06 — Transistor as a Switch

- **Module:** 3 — Transistors
- **Prerequisites:** [04 — Diodes & Rectification](04-diodes-and-rectification.md)
- **Est. time:** ~75 min

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Use a transistor to let a tiny control signal switch a much larger current on and off. Do it with both a **BJT (2N3904)** and a **MOSFET (2N7000)**, compare how each is driven, and see the destructive inductive spike a coil makes — plus the one diode that tames it. This is the most software-intuitive use of a transistor and a direct prerequisite for the keyboard.

## Concepts introduced

- **BJT saturation:** a small **base current** lets a large **collector current** flow; fully on, the transistor drops only `V_CE(sat) ≈ 0.1–0.2 V`.
- **MOSFET:** switched by **gate voltage**, not current; above the threshold it turns on with a low on-resistance. The modern default.
- The **base resistor** and why it's mandatory for a BJT.
- The **flyback diode** that clamps the spike from switching an inductive load (reuses the diode from Module 2).

## Parts & instruments

- 1 × **2N3904** (NPN BJT), 1 × **2N7000** (N-channel MOSFET)
- 1 × LED, 1 × **330 Ω** (LED), 1 × **4.7 kΩ** (base), 1 × **10 kΩ** (gate pulldown)
- A small **5 V relay**, 1 × **1N4148** (flyback), 5 V supply (from Exp. 05!), scope
- Multimeter

## Background (the why)

A **switch** in electronics doesn't have to be mechanical. A transistor lets a weak signal — a microcontroller pin, a sensor — control a load far bigger than that signal could ever drive directly.

**BJT (current-controlled).** An NPN like the 2N3904 conducts collector→emitter current in proportion to base current: `I_C = β · I_B`, with β ≈ 100–300. To use it as a *switch* you deliberately shove in **more** base current than needed, driving it into **saturation** — fully on, dropping almost nothing. Rule of thumb: aim for `I_B ≈ I_C / 10` (a "force" of 10, well past the β it needs) so it saturates hard regardless of the exact β. The base needs ~0.7 V to turn on, so the base resistor is:

```
R_B = (V_control − 0.7 V) / I_B
```

where **R_B** = the base resistor value (ohms, Ω); **V_control** = the voltage of your on/off control signal (volts); **0.7 V** = the base-emitter turn-on drop; **I_B** = the base current you want to push in (amps). (Just above, **I_C** = collector current and **β (beta)** = the transistor's current gain.)

Without that resistor, the base-emitter junction is just a forward diode and would draw destructive current.

**MOSFET (voltage-controlled).** The 2N7000 turns on when the **gate-to-source voltage** exceeds its threshold (~2.1 V), and the gate draws essentially **no steady current** — it's a tiny capacitor. That's why modern digital and power design lives on MOSFETs: no base-current budget, very low on-resistance, less wasted heat. A pulldown resistor on the gate keeps it off when the control line floats.

**The inductive spike.** A relay coil (or motor) is an inductor, and from Experiment 03 you know an inductor *fights changes in current* (`V = L·di/dt`). Switch it off and `di/dt` is huge and negative, so it generates a huge **positive voltage spike** — hundreds of volts — trying to keep current flowing. That spike can destroy the transistor. A **flyback diode** across the coil gives that current a harmless loop to die out in, clamping the spike to ~0.7 V above the supply.

## Procedure

### Part A — BJT LED switch

1. Build: 5 V → LED → 330 Ω → **collector** of the 2N3904; **emitter** to ground; **base** through 4.7 kΩ to your control line.

   ```
   +5V ──►|──[330Ω]──┬ C
        LED          (2N3904)
                     E ── GND
   control ──[4.7kΩ]── B
   ```

   *Diagram key:* `+5V` = positive supply; `──►|──`/`LED` = the light-emitting diode; `[330Ω]`/`[4.7kΩ]` = resistors; `(2N3904)` = the transistor, with `C`/`B`/`E` = its collector/base/emitter pins; `control` = your on/off signal; `GND` = ground. Symbols: [glossary](../glossary.md).

2. Tie the control line to 5 V: the LED lights. Tie it to ground: the LED goes out.
3. Measure **V_CE** (collector to emitter) with the LED on — it should be a fraction of a volt (`V_CE(sat)`), proving the transistor is fully on, not burning power.
4. Estimate the currents: `I_C ≈ (5 − V_LED − V_CE)/330 ≈ 8 mA`; the base current you supplied is `≈ (5 − 0.7)/4.7 k ≈ 0.9 mA`. You're forcing far more base drive than β needs — that's what "saturated switch" means.

### Part B — MOSFET version

5. Rebuild with the 2N7000: 5 V → LED → 330 Ω → **drain**; **source** to ground; **gate** to the control line, with a 10 kΩ from gate to ground.
6. Same on/off behavior — but note the gate draws no steady current. Measure **V_DS** on: low, set by the on-resistance. No base resistor needed (though a small series gate resistor is good practice at speed).

### Part C — Switch a relay, meet the spike

7. Replace the LED branch with a **5 V relay coil** from +5 V to the transistor (BJT collector or MOSFET drain). **First without** a flyback diode.
8. Put the scope across the transistor (collector/drain to ground). Toggle the control off and watch for a sharp **voltage spike** at turn-off — it can shoot well above 5 V.
9. Now add the **1N4148 across the coil**, cathode (band) to +5 V, anode to the transistor. Toggle again: the spike is **clamped** to ~0.7 V above the supply. Same circuit, one diode, a night-and-day difference in reliability.

## What to observe / measure

- LED switches cleanly with either device; `V_CE(sat)`/`V_DS(on)` is small (the switch wastes little power).
- The BJT needs real base current; the MOSFET gate does not.
- The relay's turn-off spike is large and fast **without** the diode, and neatly clamped **with** it.

## The "aha"

Under a milliamp of base current — the kind a microcontroller pin trivially supplies — commanded eight milliamps through the LED, and a MOSFET did it with no current at all. You've built the thing that lets *code* move real-world loads. And you saw, on the screen, the invisible inductive spike that quietly kills unprotected switching circuits — and the one cheap diode that stops it.

## Going further (experiments to try and log)

- **Switch faster.** Drive the gate/base from the probe-comp square wave and look at the **rise/fall edges** of V_DS. The sharper the switching, the less time the transistor spends half-on wasting heat — this is the seed of the **class-D/E PA** in the QMX+, where transistors switch *hard* at RF to make power efficiently.
- **Low-side vs high-side.** You built a *low-side* switch (load on top, transistor to ground). Think about why that's the easy case, and what changes if the load must be switched on its ground side.
- **Two BJTs as a logic gate.** Wire two transistors so the output is low only when *both* inputs are high — you've built a NAND-like gate from discrete parts, the literal atom of the digital logic in Exp. 14.

## Why this matters (where you'll meet it)

The transistor-as-switch is the **atom of everything digital**. Every logic gate in the RP2040 and STM32 you'll use is just transistors switching on and off — so as a software engineer, this is the literal hardware sitting under all your abstractions.

- **Control anything a microcontroller pin can't drive directly:** relays, motors, LED strips, higher-power loads, band-switching in a radio. A GPIO can nudge a transistor; the transistor does the muscle work.
- **Keyboard:** driving key-scan lines and indicator LEDs is GPIO-as-switch — this is a direct prerequisite for that build.
- **The QMX+ PA is this idea at speed.** Its class-D/E power amplifier is transistors switching *hard* to make RF power efficiently — this experiment is the seed of understanding how a switching amplifier works.
- **The flyback-diode lesson prevents mystery failures.** Switching anything with a coil (relay, motor) produces a destructive inductive spike; you'll *see* it on the scope and learn the one diode that tames it — a reliability must-know.
- **BJT vs MOSFET** teaches you which to reach for and why modern designs favor MOSFETs (voltage-controlled, low on-resistance).

## Log

- V_CE(sat) with LED on: ___ V; V_DS(on) for the MOSFET: ___ V
- Base current supplied vs collector current: ___ mA / ___ mA
- Relay spike height without flyback: ___ V; with flyback: ___ V
- Surprises / questions:
