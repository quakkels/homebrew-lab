# 14 — Digital Logic & Microcontrollers

**Module:** 7 — Digital & Embedded
**Status:** Planned
**Prerequisites:** [06 — Transistor as a Switch](06-transistor-as-switch.md)
**Est. time:** ~2–3 hours (spread over sessions)

## Objective

Bridge from analog into the digital/embedded world you already know as a
software engineer — but from the *hardware* side. Understand logic levels,
GPIO electrically, and get a microcontroller reading inputs and driving outputs.
This is the on-ramp to the keyboard build.

## Concepts to be covered

- Logic levels, thresholds, noise margin; pull-up/pull-down resistors and *why*.
- GPIO as a transistor switch (reuses Exp. 06); input vs output; open-drain.
- Reading a switch (and contact **bounce** — an RC/scope observation!).
- A microcontroller (RP2040) toolchain: blink, read a button, scan a small matrix.
- Communication buses at a glance: I²C/SPI/UART — what a scope trace of each looks like.

## Planned procedure (sketch)

- Scope a mechanical switch closing and *see* the bounce; debounce it (RC and/or firmware).
- Blink an LED and read a button on an RP2040.
- Scan a 2×2 key matrix with diodes (the keyboard in miniature) and print keypresses.

## Parts & instruments

- RP2040 board (e.g. Pico), tactile switches, diodes (1N4148), resistors, LEDs, scope.

## Why this matters (where you'll meet it)

This is where your **software brain finally meets the hardware it's been running
on** — GPIO, logic levels, and buses from the *electrical* side rather than the
API side.

- **Contact bounce is a delightful "aha."** A switch closing isn't clean — you'll
  *see* the RC-like ringing on the scope and understand why every keyboard needs
  debouncing. It's an analog problem hiding inside a digital project, and it ties
  straight back to Exp. 01.
- **Pull-up/pull-down resistors** are the thing every embedded tutorial tells you
  to add without explaining. Here you'll know exactly *why*, electrically.
- **Matrix scanning with diodes is the keyboard in miniature** — this experiment is
  the direct dress rehearsal for that build, including why the diodes are there.
- **Bus literacy is a debugging superpower.** Recognizing I²C/SPI/UART on a scope
  lets you troubleshoot embedded hardware and reverse-engineer / hack existing
  devices — squarely in your hardware-hacking goal.

## Log

- Switch bounce duration observed on scope: 
- Matrix scan working (keys reported correctly?): 
- Surprises / questions: 
