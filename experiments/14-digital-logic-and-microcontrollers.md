# 14 — Digital Logic & Microcontrollers

- **Module:** 7 — Digital & Embedded
- **Prerequisites:** [06 — Transistor as a Switch](06-transistor-as-switch.md)
- **Est. time:** ~2–3 hours (spread over sessions)

> **New to any symbol or term?** The wiring-diagram symbols, the unit abbreviations, and every piece of jargon used here are defined in the [glossary](../glossary.md) — no prior electronics knowledge assumed.

## Objective

Cross from analog into the digital/embedded world you already know as a software engineer — but from the *hardware* side. See logic levels and contact bounce on the scope, understand pull-up resistors electrically, then get an RP2040 blinking an LED, reading a button, and scanning a diode key matrix. This is the on-ramp to the keyboard build.

## Concepts introduced

- **Logic levels**, thresholds, noise margin; **pull-up/pull-down** resistors and *why* they exist.
- **GPIO as a transistor switch** (reuses Exp. 06); input vs. output; open-drain.
- Reading a switch, and **contact bounce** — an analog RC/scope observation hiding in a digital project.
- An RP2040 toolchain: **blink**, **read a button**, **scan a 2×2 matrix** with diodes.
- What **I²C / SPI / UART** look like on a scope (bus literacy).

## Parts & instruments

- An **RP2040** board (Raspberry Pi **Pico**), USB cable
- 4 × tactile switches, 4 × **1N4148** diodes, 1 × LED + **330 Ω**, a **10 kΩ** (external pull-up demo), hookup wire, scope

## Background (the why)

Your code has always run on top of pins that are really just **voltages switched by transistors** (Exp. 06). A GPIO pin set "high" connects to the positive rail; "low" connects to ground. As an **input**, the pin just measures voltage and calls it 1 or 0 depending on which side of a threshold it's on.

**Why pull-ups exist.** A plain switch only connects a pin to ground when pressed. When it's *not* pressed the pin is connected to nothing — it **floats**, and picks up noise, reading random 1s and 0s. A **pull-up resistor** gently ties the pin to the positive rail so it reads a solid **1** when open, and the switch yanks it to a solid **0** when pressed. (Pull-downs do the mirror image.) Every microcontroller has these built in and switchable in firmware — now you know what they're for.

**Contact bounce.** A mechanical switch's springy contacts don't close cleanly: they slap together and separate several times over a few milliseconds. Electrically it's an RC-ish mess — and to the microcontroller, running millions of times faster than that, one press can look like **dozens** of presses. You'll *see* this on the scope, and it's why every keyboard **debounces** (in RC hardware, in firmware, or both). It ties straight back to Experiment 01.

**Matrix scanning.** A keyboard doesn't wire one pin per key — that's too many pins. Instead keys sit at the crossings of a grid of **rows** and **columns**. The firmware drives one row at a time and reads which columns respond. A **diode** in series with each key stops phantom "ghost" presses when several keys are held (the same one-way-valve trick from Exp. 04). That's the whole electrical idea behind the keyboard project.

## Procedure

### Part A — See a logic level and a pull-up

1. On the Pico, pick a GPIO as an input. Wire a tactile switch from that pin to ground. With **no** pull-up, print the pin in a loop — watch it read garbage when untouched.
2. Enable the internal pull-up (or add an external 10 kΩ to 3.3 V). Now it reads a steady **1** open, **0** pressed. You just fixed a floating input.

### Part B — Scope the bounce

3. Put the scope on the switch pin (single-shot / normal trigger on a falling edge, timebase ~1 ms/div). Press the button and capture the transition.
4. You'll see the voltage **bounce** — several quick high/low chatters over a few ms before settling. Measure how long the bounce lasts. *This* is why a naive "count every press" loop miscounts.

### Part C — Blink and read (the embedded "hello world")

5. Flash MicroPython (or the Arduino core) onto the Pico. Blink the onboard LED:

   *Code note:* these snippets are **MicroPython** (Python that runs directly on the Pico). `Pin(25, …)` refers to a GPIO pin by its number; `#` begins a comment; `Pin.OUT`/`Pin.IN` set a pin as output/input; `Pin.PULL_UP` turns on the pin's internal pull-up resistor. Terms are in the [glossary](../glossary.md).

   ```python
   from machine import Pin
   from time import sleep
   led = Pin(25, Pin.OUT)          # onboard LED
   while True:
       led.toggle()
       sleep(0.5)
   ```

6. Read the button and light the LED when pressed, with a simple debounce:

   ```python
   from machine import Pin
   from time import sleep_ms
   btn = Pin(15, Pin.IN, Pin.PULL_UP)
   led = Pin(25, Pin.OUT)
   while True:
       if btn.value() == 0:        # pressed = pulled low
           sleep_ms(20)            # wait out the bounce
           if btn.value() == 0:
               led.on()
       else:
           led.off()
   ```

### Part D — Scan a 2×2 diode matrix (the keyboard in miniature)

7. Build a 2×2 grid: 2 row pins (outputs), 2 column pins (inputs, pull-up). At each crossing put a tactile switch **in series with a 1N4148** (band toward the row).
8. Scan it: drive one row low at a time, read both columns, and map which switch is down.

   ```python
   from machine import Pin
   rows = [Pin(2, Pin.OUT, value=1), Pin(3, Pin.OUT, value=1)]
   cols = [Pin(4, Pin.IN, Pin.PULL_UP), Pin(5, Pin.IN, Pin.PULL_UP)]
   while True:
       for r, row in enumerate(rows):
           row.value(0)                     # activate this row
           for c, col in enumerate(cols):
               if col.value() == 0:
                   print("key", r, c)
           row.value(1)                     # deactivate
   ```

9. Press keys — including two or three at once — and confirm they report correctly. Then remove the diodes and hold three keys in an "L" shape: a **ghost** key appears. Put the diodes back and it's gone. That's anti-ghosting, demonstrated.

## What to observe / measure

- A floating input reads noise; a pull-up gives a clean, stable level.
- The scope shows real contact bounce lasting a few milliseconds.
- The Pico blinks, reads a debounced button, and correctly scans the matrix.
- Without diodes, multi-key presses create ghosts; with diodes, they don't.

## The "aha"

The abstractions you've coded against for years — `digitalRead`, a pull-up flag, a "key press" — turned into *voltages you can see on a screen*. Contact bounce, the reason `if (pressed)` needs debouncing, is right there as analog chatter. And a 2×2 grid of switches and diodes is, electrically, the entire keyboard you're about to build — you just ran it.

## Going further (experiments to try and log)

- **Grow the matrix.** Extend to 3×3 or 4×4 and adjust the scan loop — the code barely changes, which is exactly why matrices scale.
- **Debounce in hardware.** Add an RC + Schmitt-trigger (Exp. 10) debounce and compare it to the firmware version. Same problem, two layers.
- **Sniff a bus.** Put the scope (or a logic analyzer) on an I²C or SPI sensor and watch the clock and data lines. Recognizing these patterns is a real reverse-engineering / hardware-hacking skill.
- **Straight into the project.** With the matrix scanning, you've met every electrical prerequisite for the [keyboard build](../projects/keyboard/README.md) — the next step is scaling this up and drawing a PCB.

## Why this matters (where you'll meet it)

This is where your **software brain finally meets the hardware it's been running on** — GPIO, logic levels, and buses from the *electrical* side rather than the API side.

- **Contact bounce is a delightful "aha."** A switch closing isn't clean — you'll *see* the RC-like ringing on the scope and understand why every keyboard needs debouncing. It's an analog problem hiding inside a digital project, and it ties straight back to Exp. 01.
- **Pull-up/pull-down resistors** are the thing every embedded tutorial tells you to add without explaining. Here you'll know exactly *why*, electrically.
- **Matrix scanning with diodes is the keyboard in miniature** — this experiment is the direct dress rehearsal for that build, including why the diodes are there.
- **Bus literacy is a debugging superpower.** Recognizing I²C/SPI/UART on a scope lets you troubleshoot embedded hardware and reverse-engineer / hack existing devices — squarely in your hardware-hacking goal.

## Log

- Switch bounce duration observed on scope: ___ ms
- Debounced button read working:
- Matrix scan working (keys reported correctly?):
- Ghosting seen without diodes / fixed with diodes?
- Surprises / questions:
