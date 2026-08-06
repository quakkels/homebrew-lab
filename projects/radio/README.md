# Project — QMX+ Homebrew Radio

- **Branches off:** Module 6 ([12 — LC Filters & Impedance Matching](../../experiments/12-lc-filters-and-impedance-matching.md), [13 — Mixers & Detectors](../../experiments/13-mixers-and-detectors.md)).

## Goal

Build, align, and — most importantly — **understand** the **QRP Labs QMX+**. Not just "follow the manual and hope it works," but trace every block to the fundamentals you built up in the course, so you can test, debug, and eventually modify it.

## What the QMX+ is (and why it's a great teacher)

The QMX+ is a multiband CW/digital + SSB QRP transceiver built on an **SDR** architecture. Its major blocks map cleanly onto this curriculum:

| QMX+ block | Course grounding |
|---|---|
| Band-pass filters (RX front end) | Exp. 12 — LC filters |
| Low-pass filters (TX harmonic filtering) | Exp. 12 — LC filters, impedance |
| Si5351 synthesizer / clock | Exp. 11 — crystal/reference, oscillators |
| Quadrature Sampling Detector (QSD) | Exp. 13 — mixers & detectors, I/Q |
| Op-amp gain stages after the QSD | Module 4 — op-amps, active filters |
| STM32 doing the DSP | Module 7 — embedded/software (your turf) |
| Class-D/E power amplifier | Exp. 06 — switching, and Exp. 12 — matching |
| Power/regulation | Module 2 — power supply |

That table *is* the point of the RF modules: by the time you get here, none of these blocks is a black box.

## Phased plan

### Phase 0 — Read & inventory
- Read the QMX+ assembly and operating manuals end to end before soldering.
- Inventory all parts; identify the toroids and cores you'll wind.
- Set up ESD-safe practices (the STM32 and PA devices care).

### Phase 1 — Understand before you build
- With the schematic open, label each block using the table above.
- For each stage, note "what would I measure here, and what should I see?" — this becomes your test plan.

### Phase 2 — Build
- Follow the manual carefully; **winding toroids accurately** is the make-or-break skill (practiced in Exp. 03 and 12). Count turns, keep tension even.
- Work in the manual's recommended stages; don't rush the magnetics.

### Phase 3 — Test & align
- Use the built-in test/diagnostic modes; a scope and (ideally) a NanoVNA to check filters; a dummy load for any TX testing.
- Align per the manual; record measured filter responses and power output.
- **Transmit only into a dummy load / proper antenna, on bands your license authorizes, at legal power** — you're a General, so operate within your privileges.

### Phase 4 — Operate & understand
- Make contacts; correlate what you hear with the block diagram.
- Revisit any block that's fuzzy and do the matching bench experiment.

### Phase 5 — Modify / extend (stretch)
- Scratch-build an experimental stage (e.g. an outboard band-pass filter or a receive preamp) using Module 6 skills, and compare it to the QMX+'s own.

## Skills / prerequisites checklist

- [ ] LC resonance and filters (Exp. 03, 12)
- [ ] Impedance & matching (Exp. 12)
- [ ] Oscillators / frequency reference (Exp. 10, 11)
- [ ] Mixers, detectors, I/Q (Exp. 13)
- [ ] Op-amp gain/filtering (Module 4)
- [ ] Accurate toroid winding (Exp. 03, 12)
- [ ] Clean power & decoupling (Module 2)

## Tools & materials

The QMX+ kit, fine soldering gear, enameled wire for toroids, a dummy load, scope, and ideally a NanoVNA for filter alignment.

## Safety & regulatory notes

- Transmit into a dummy load during testing; only radiate on authorized frequencies within your **US General** privileges and legal power limits.
- Observe ESD precautions with the STM32 and PA MOSFETs.
- Mind heat on the PA during any extended TX testing.

## Log / decisions

- Build progress by stage:
- Measured filter responses / power output:
- Alignment notes:
- Mods attempted:
