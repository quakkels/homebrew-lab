# Homebrew Lab

A self-directed, bench-driven electronics course — learn analog by *seeing* it on
a scope. Every experiment ends with a measurement you make yourself and a number
that matches (or surprises) the theory.

> ⚠️ **This curriculum is AI-generated.** It was written with an AI assistant and
> should be treated as a starting map, not an authority. Verify component values,
> procedures, and especially anything involving mains power or RF transmission
> against trusted references (ARRL Handbook, datasheets, *The Art of Electronics*)
> before you rely on it.

## Who it's for

This course is tailored to people who:

- **Come from a software-development background** — comfortable with logic and
  code, and want to understand the *hardware* underneath.
- **Are amateur radio operators (hams)** — already fluent in some RF ideas
  (frequency, resonance, antennas, transmission lines) and want to homebrew gear.

If that's you, the course plays to those strengths while targeting the usual gap:
**analog intuition** — component feel, reading signals on a scope, and the
connective tissue (filters, impedance, biasing) between "I can follow a schematic"
and "I can design one."

## How it works

Each experiment follows one loop:

> **Build → Observe → Explain → Log**

Build the circuit, observe it on the scope, understand what you saw and why, then
record your measurements in the experiment's **Log** section — your evidence that
the theory is real.

## Structure

- **[`syllabus.md`](syllabus.md)** — the master plan: goals, pacing, equipment,
  the full module progression, and a reference library.
- **[`experiments/`](experiments/)** — numbered experiment files (00–14), one per
  topic, from the RC time constant up through RF and embedded systems.
- **[`projects/`](projects/)** — two flagship builds that branch off the modules:
  a **keyboard from scratch** and a **homebrew QMX+ transceiver**.

Start with [`syllabus.md`](syllabus.md), then
[`experiments/00-bench-and-instrumentation.md`](experiments/00-bench-and-instrumentation.md).

## Safety

Some modules involve mains-adjacent power supplies and RF transmission. Transmit
only into a dummy load during testing, radiate only on frequencies and at power
levels your license authorizes, and observe ESD precautions around sensitive parts.
When in doubt, check a trusted reference — see the AI-generated caveat above.
