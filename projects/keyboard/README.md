# Project — Keyboard From Scratch

- **Branches off:** Module 7 ([14 — Digital Logic & Microcontrollers](../../experiments/14-digital-logic-and-microcontrollers.md)), using diode/switch intuition from Modules 1–3.

## Goal

Design and build a mechanical keyboard **from scratch** — not a kit. Own the schematic, the PCB, the firmware, and the assembly. This plays directly to your software strengths while forcing you to make real hardware decisions.

## Why it fits the curriculum

- **Digital + a little analog:** matrix scanning, diodes for N-key rollover, debounce (an RC / scope lesson), GPIO as switches — all covered in Modules 1–3 and 7.
- **Ships something you'll use every day.** High motivation, clear "done."
- **Teaches PCB design** (KiCad) end to end, a skill that transfers to every future board — including radio projects.

## Phased plan

### Phase 0 — Decide the design
- Layout (60%, ergo, split, ortholinear?), switch type, connector (USB-C).
- Controller: **RP2040** (cheap, hacker-friendly, great firmware support).

### Phase 1 — Breadboard proof
- Wire a small key matrix (e.g. 2×2 or 3×3) with per-key diodes.
- Firmware reads the matrix and reports keypresses. Confirm N-key rollover works and understand *why the diodes are there* (current-path blocking / ghosting).
- Scope the debounce (from Experiment 14).

### Phase 2 — Schematic & PCB (KiCad)
- Draw the full matrix, diodes, RP2040, USB-C, reset/boot, decoupling caps.
- Lay out the PCB; footprints for your chosen switches; consider hotswap sockets.
- Design-rule check; export Gerbers; order from a fab.

### Phase 3 — Assemble & bring up
- Solder (SMD RP2040 support components + through-hole switches, or a pre-made controller module to start). Power-on checks before plugging into a real PC.
- Flash firmware; verify every key.

### Phase 4 — Firmware
- **QMK** or **ZMK** for a mature feature set (layers, macros), or write minimal firmware yourself for the full from-scratch experience.
- Tune debounce, add layers/macros.

## Skills / prerequisites checklist

- [ ] Diodes and current steering (Module 2 / Exp. 04)
- [ ] Transistor/GPIO as a switch (Exp. 06)
- [ ] Debounce as an RC + firmware problem (Exp. 01, Exp. 14)
- [ ] Microcontroller matrix scan (Exp. 14)
- [ ] KiCad basics (introduced in this project)

## Tools & materials (gather in Phase 2)

RP2040 (bare chip or module), mechanical switches, keycaps, 1N4148 diodes, USB-C connector, a PCB fab order (JLCPCB/OSHPark), KiCad, soldering gear.

## Log / decisions

- Chosen layout & switches:
- Controller & firmware choice:
- Fab used, board revision notes:
- Bring-up issues and fixes:
