# Glossary & Key

Everything in the course — the symbols in the wiring diagrams, the letters in the equations, and the jargon — is defined here in plain language. You do not need any prior electronics knowledge to use it. When a term shows up in an experiment, this is where its full definition lives.

## How to read the wiring diagrams

The diagrams are drawn with plain text characters. Here is what each one means:

- `─` and `│` — a **wire** (a connection). Horizontal or vertical, it is just a conductor carrying the signal.
- `┬` `┴` `├` `┤` `┼` — a **junction**: a point where wires actually connect and current can split or join. (Where lines merely cross without one of these, treat them as *not* connected.)
- `[ 10kΩ ]` — a **component drawn as a box with its value inside**. `[10kΩ]` is a 10 kilohm resistor, `[10nF]` a 10 nanofarad capacitor, `[ L 1mH ]` a 1 millihenry inductor. (See the units below.)
- `►|` or `──►|──` — a **diode**. The little bar (the "band," matching the stripe on the real part) is the **cathode**; the diode passes current in the direction the triangle points (toward the bar) and blocks the other way.
- `GND` — **ground**: the circuit's common 0-volt reference. Every voltage in a circuit is measured relative to ground. "Probe ground clip" is where the scope's ground lead attaches.
- `CAL out` / `probe-comp` — the **oscilloscope's calibration output**: a small ~1 kHz square-wave signal built into the scope, used throughout the course as a free test signal.
- `+5V` `+9V` `+12V` `VCC` — a connection to the **positive power supply** at that voltage. `VCC` is a generic name for "the positive supply rail."
- `(2N3904)` and pin letters — a **labeled part**. Letters next to it mark its pins: **C/B/E** = collector/base/emitter (a bipolar transistor), **D/G/S** = drain/gate/source (a MOSFET).
- "probe tip" — where you touch the **oscilloscope probe** to measure the voltage at that point.

## Oscilloscope controls (you set these in Experiment 00)

- **Timebase (time/div)** — how much time each horizontal grid division represents; the horizontal "zoom" on time.
- **Volts/div** — how many volts each vertical division represents; the vertical zoom.
- **Trigger** — the condition (e.g. "the signal crossing 1 V on its way up") that tells the scope when to start drawing, so a repeating wave stands still on screen instead of sliding.
- **Coupling (AC / DC)** — **DC coupling** shows the true voltage including its steady level; **AC coupling** removes the steady part so you can zoom in on a small wiggle (like power-supply ripple) riding on a big DC voltage.
- **Cursors** — movable on-screen markers you position by hand to read off a time interval or a voltage difference directly.
- **Probe compensation / probe-comp** — a small built-in square-wave output on the scope, plus the trimmer adjustment on a ×10 probe that makes that square wave look crisp. Used as a free ~1 kHz signal source throughout this course.
- **×10 / ×1 probe** — a switch on the probe: **×10** divides the signal by ten (less loading on your circuit, more usable bandwidth) at the cost of amplitude; **×1** passes it full-size.
- **Bandwidth** — the highest frequency a scope or probe can display accurately.

## Units, symbols & metric prefixes

**Base units you'll see:**

- **V — volt.** Unit of voltage (electrical "pressure," the push behind current).
- **A — ampere ("amp").** Unit of current (the rate of charge flow).
- **Ω — ohm.** Unit of resistance (opposition to current). The symbol is the Greek capital omega.
- **F — farad.** Unit of capacitance (how much charge a capacitor stores per volt).
- **H — henry.** Unit of inductance (how strongly a coil opposes changes in current).
- **Hz — hertz.** Unit of frequency: cycles per second.
- **W — watt.** Unit of power (energy per second, = volts × amps).
- **s — second.** Unit of time. (`µs` = microsecond, `ms` = millisecond.)
- **dB — decibel.** A ratio expressed on a logarithmic scale; used for gain and attenuation. Every 20 dB is a factor of 10 in voltage; 3 dB is about ×1.4 (or half power).

**Metric prefixes** (they scale a unit up or down):

- **p — pico** = ×0.000000000001 (10⁻¹²)
- **n — nano** = ×0.000000001 (10⁻⁹)
- **µ — micro** = ×0.000001 (10⁻⁶) (written "u" when the µ symbol isn't handy)
- **m — milli** = ×0.001 (10⁻³)
- **k — kilo** = ×1,000 (10³)
- **M — mega** = ×1,000,000 (10⁶)

So `10 nF` = 10 nanofarads, `4.7 kΩ` = 4,700 ohms, `1 mH` = 0.001 henry, `50 MHz` = 50,000,000 hertz.

**The same value written every way (worked example).** Here is one single capacitance — 4.7 microfarads — written with each prefix. Every row is the *exact same amount of capacitance*; only the prefix and the position of the decimal point change:

| Prefix | This capacitor, written that way |
|---|---|
| pico (pF) | 4,700,000 pF |
| nano (nF) | 4,700 nF |
| micro (µF) | **4.7 µF** ← the natural way to write it |
| milli (mF) | 0.0047 mF |
| (none) | 0.0000047 F |

Each step down the list (pico → nano → micro → milli → farad) multiplies by 1,000, so the decimal point jumps three places each time. The same rule runs the other way for *large* quantities — for a frequency, `3,500,000 Hz` = `3,500 kHz` = `3.5 MHz`; for a resistance, `4,700 Ω` = `4.7 kΩ` = `0.0047 MΩ`. Pick whichever prefix keeps the number conveniently sized (that's why a cap is called "4.7 µF," not "0.0000047 F").

**Letters used in equations:**

- **τ (tau)** — time constant (how fast an RC or RL circuit responds), in seconds.
- **f** — frequency, in hertz. **f_c** = cutoff frequency of a filter; **f₀** = resonant or center frequency.
- **R** — resistance (Ω). **C** — capacitance (F). **L** — inductance (H).
- **V** — voltage. **I** — current. **P** — power.
- **X_L, X_C** — reactance (the frequency-dependent "resistance" of an inductor or capacitor), in ohms.
- **Q** — quality factor: how sharp/selective a resonance is (higher Q = sharper).
- **β (beta)** — a bipolar transistor's current gain (collector current ÷ base current).
- **π (pi)** — the constant ≈ 3.14159.
- **ΔV** — a *change* in voltage (the Greek delta means "change in").

## Glossary of terms (A–Z)

- **Active region** — the operating range where a transistor acts as an *amplifier* (partly on), between fully off (cutoff) and fully on (saturation). See [07](experiments/07-transistor-as-amplifier.md).
- **ADC / DAC** — analog-to-digital converter / digital-to-analog converter: circuits that turn a voltage into a number, or a number back into a voltage.
- **Anode / cathode** — the two ends of a diode. Current flows *in* at the anode and *out* at the cathode; the cathode is marked with a band.
- **Astable** — an oscillator that never settles — it flips back and forth on its own, producing a continuous waveform (e.g. the 555 astable, [10](experiments/10-oscillators.md)).
- **Band-pass / low-pass / high-pass / band-reject** — filter types. They pass, respectively: a band of frequencies; everything below a cutoff; everything above a cutoff; everything except a band.
- **Bias / operating point** — the steady DC voltages and currents you set up so an amplifier sits in its active region, ready to amplify a signal. See [07](experiments/07-transistor-as-amplifier.md).
- **BJT (bipolar junction transistor)** — a common transistor type controlled by *current* into its base. NPN is the polarity used here (e.g. the 2N3904).
- **Buffer** — an amplifier with a gain of 1 whose job is *isolation*: it presents an easy load to a weak source and drives the next stage without the two disturbing each other. See [08](experiments/08-op-amp-fundamentals.md).
- **Bypass capacitor** — a capacitor placed across a resistor (often a transistor's emitter resistor) to "short it out" for AC signals only, raising the AC gain. Related: **decoupling capacitor**.
- **Capacitor** — a component that stores energy in an electric field and *resists changes in voltage*. Passes AC, blocks DC.
- **Clipping** — the flattening of a signal's peaks when an amplifier is pushed past its limits (it runs out of "headroom"). Causes distortion.
- **Common-emitter** — the classic single-transistor amplifier arrangement; it inverts the signal and provides voltage gain. See [07](experiments/07-transistor-as-amplifier.md).
- **Contact bounce** — the rapid, messy make-and-break chatter of a mechanical switch's contacts over a few milliseconds when it closes. Must be "debounced." See [14](experiments/14-digital-logic-and-microcontrollers.md).
- **Coupling capacitor** — a capacitor between two stages that passes the AC signal while blocking their different DC levels from interfering.
- **Cutoff (frequency)** — the frequency where a filter has reduced the signal to 70.7% (−3 dB) of the passband — the edge of what it passes. Also, "cutoff" separately means a transistor turned fully off.
- **CW (continuous wave)** — Morse-code radio: the transmitter is switched on and off ("keyed") to send dots and dashes.
- **Debounce** — to filter out contact bounce, in hardware (an RC + Schmitt trigger) or in firmware (wait and re-check), so one press counts once.
- **Decoupling capacitor** — a small capacitor placed next to a chip's power pins to supply quick bursts of current and keep the supply steady locally. See [05](experiments/05-linear-power-supply.md).
- **Direct conversion** — a receiver that mixes the incoming radio signal straight down to audio in one step (local oscillator set at the signal's frequency). See [13](experiments/13-mixers-and-detectors.md).
- **Diode** — a one-way valve for current: it conducts in one direction (above a small "forward voltage") and blocks the other. See [04](experiments/04-diodes-and-rectification.md).
- **DMM (digital multimeter)** — the handheld meter that measures voltage, current, resistance, and (in diode-test mode) a diode's forward drop.
- **Dropout** — for a linear regulator, the minimum amount its input must stay above its output; below that, the output can no longer hold steady. See [05](experiments/05-linear-power-supply.md).
- **DSP (digital signal processing)** — doing filtering, mixing, or demodulation in *software* on a processor instead of with analog parts. The QMX+'s STM32 does this.
- **Duty cycle** — the fraction of each cycle a square wave spends "high," as a percentage. 50% is a symmetric square wave.
- **Emitter degeneration** — deliberately leaving a resistor in a transistor's emitter (unbypassed) to trade some gain for stability and predictability. See [07](experiments/07-transistor-as-amplifier.md).
- **Envelope detector** — the simplest AM demodulator: a diode and capacitor that follow the "envelope" (amplitude) of a carrier to recover the audio. The heart of a crystal radio. See [13](experiments/13-mixers-and-detectors.md).
- **Feedback** — routing part of a circuit's output back to its input. **Negative** feedback stabilizes (op-amps); **positive** feedback sustains oscillation (oscillators).
- **FET / MOSFET** — field-effect transistor / metal-oxide-semiconductor FET: a transistor controlled by *voltage* on its gate (which draws almost no current). The modern default switch. See [06](experiments/06-transistor-as-switch.md).
- **Floating** — an input pin connected to nothing, so its voltage is undefined and picks up noise. Fixed with a pull-up or pull-down resistor.
- **Flyback diode** — a diode placed across a coil (relay/motor) to safely absorb the high-voltage spike it produces when switched off. See [06](experiments/06-transistor-as-switch.md).
- **Forward voltage (drop)** — the roughly fixed voltage a diode "costs" to conduct: ≈0.6–0.7 V for silicon, ≈0.2–0.3 V for a Schottky.
- **Full-wave / half-wave** — rectification that uses both halves of the AC wave (full-wave, via a bridge) versus only one half (half-wave, a single diode).
- **Gain** — how much an amplifier multiplies a signal (output ÷ input). A negative sign means the signal is also inverted.
- **Ghosting** — false key presses a keyboard matrix reports when several keys are held; blocked by putting a diode in series with each key. See [14](experiments/14-digital-logic-and-microcontrollers.md).
- **Golden rules (op-amp)** — two shortcuts for an ideal op-amp with negative feedback: (1) no current flows into its inputs; (2) it drives its output until its two inputs are at the same voltage. See [08](experiments/08-op-amp-fundamentals.md).
- **GPIO (general-purpose input/output)** — a microcontroller pin your program can set high/low (output) or read as high/low (input).
- **Ground** — the circuit's common 0-volt reference point (labeled `GND`); all voltages are measured relative to it.
- **Harmonic** — a whole-number multiple of a frequency (2×, 3×, …). Oscillators and transmitters produce them, and filters remove the unwanted ones.
- **Headroom** — how much bigger a signal can get before an amplifier clips. Set by the bias point and supply voltage.
- **Hysteresis** — building in two different switching thresholds so a comparator "snaps" cleanly and ignores noise (a Schmitt trigger). See [10](experiments/10-oscillators.md).
- **I²C / SPI / UART** — three common digital communication "buses" that let chips talk to each other over a few wires. Recognizable by their scope traces.
- **I/Q (in-phase / quadrature)** — a pair of signals 90° apart in phase. Together they let a receiver tell apart frequencies above and below the local oscillator and demodulate any mode. See [13](experiments/13-mixers-and-detectors.md).
- **Image (frequency)** — an unwanted second frequency a simple mixer responds to, equally far on the other side of the local oscillator; removed by filtering (or by I/Q).
- **Impedance** — the total opposition to AC (resistance plus reactance), in ohms. Matching impedances lets power transfer efficiently. See [12](experiments/12-lc-filters-and-impedance-matching.md).
- **Impedance matching** — transforming one impedance to another (e.g. with an L-network) so maximum power transfers and reflections (SWR) drop. Why radios and antennas are "50 Ω."
- **Inductor** — a coil that stores energy in a magnetic field and *resists changes in current*. Passes DC, opposes AC. See [03](experiments/03-inductors-and-lc-resonance.md).
- **Insertion loss** — how much signal a filter or part loses even inside its passband.
- **L-network** — the simplest impedance-matching circuit: one series and one shunt reactance (an inductor and a capacitor).
- **LC / RC / RL circuit** — a circuit made from those components: **RC** = resistor+capacitor, **RL** = resistor+inductor, **LC** = inductor+capacitor (which resonates).
- **LED (light-emitting diode)** — a diode that emits light when forward current flows.
- **Local oscillator (LO)** — the internal reference frequency a receiver mixes with an incoming signal to shift it. See [13](experiments/13-mixers-and-detectors.md).
- **Logic level** — a voltage interpreted as a digital 1 (high) or 0 (low), depending on which side of a threshold it's on.
- **Matrix scanning** — reading many keys with few pins by arranging them in a grid of rows and columns and checking one row at a time. See [14](experiments/14-digital-logic-and-microcontrollers.md).
- **Maximum power transfer** — the principle that a source delivers the most power to a load when their impedances match. The reason 50 Ω is standard.
- **Mixing** — multiplying two signals to produce new frequencies at their sum and difference; how radios shift signals up and down in frequency. See [13](experiments/13-mixers-and-detectors.md).
- **NanoVNA** — an inexpensive **vector network analyzer**: a pocket instrument that sweeps frequency and shows how a filter, antenna, or match responds. Excellent for the RF experiments.
- **NPN / PNP** — the two polarities of bipolar transistor. NPN (used here) turns on when the base is made positive relative to the emitter.
- **On-resistance** — the small resistance a MOSFET (or switch) has when fully on; lower is better (less wasted heat).
- **Op-amp (operational amplifier)** — a ready-made, very-high-gain amplifier block whose behavior you tame with feedback resistors to get precise, predictable gain. See [08](experiments/08-op-amp-fundamentals.md).
- **Open-drain** — an output that can only pull *low* (to ground) or let go (float), relying on a pull-up resistor for the high level.
- **PA (power amplifier)** — the final, high-power amplifier stage in a transmitter that drives the antenna.
- **PLL (phase-locked loop)** — a feedback circuit that locks an oscillator to a multiple of a reference frequency; the basis of frequency synthesizers like the Si5351.
- **ppm (parts per million)** — a way to state very small fractions (1 ppm = 0.0001%); used for crystal-frequency accuracy.
- **Pull-up / pull-down resistor** — a resistor that gently ties a pin to the positive rail (pull-up) or to ground (pull-down) so it reads a defined level when nothing else is driving it. See [14](experiments/14-digital-logic-and-microcontrollers.md).
- **Pulling (a crystal)** — nudging a crystal's frequency a tiny amount by adding capacitance; the basis of a VXO. See [11](experiments/11-crystal-oscillator.md).
- **PWM (pulse-width modulation)** — varying a square wave's duty cycle to control average power — used to dim LEDs, drive motors, and make power efficiently. See [10](experiments/10-oscillators.md).
- **Q (quality factor)** — a measure of how sharp a resonance or filter is, and how long a tank "rings." Higher Q = narrower, more selective. See [03](experiments/03-inductors-and-lc-resonance.md).
- **QSD (quadrature sampling detector)** — an elegant switching mixer clocked at four phases (0/90/180/270°) that produces I/Q outputs; the front end of the QMX+ and many SDRs. See [13](experiments/13-mixers-and-detectors.md).
- **Reactance** — the frequency-dependent opposition to AC of a capacitor (`X_C`, falls with frequency) or inductor (`X_L`, rises with frequency), in ohms. See [03](experiments/03-inductors-and-lc-resonance.md).
- **Rectification** — using diodes to convert alternating current (AC) into one-directional (pulsating) DC. Step one of a power supply. See [04](experiments/04-diodes-and-rectification.md).
- **Regulation (line / load)** — how steadily a power supply holds its output when the *input* varies (line) or when the *load current* varies (load).
- **Regulator (linear)** — a chip (e.g. 78L05) that actively holds its output at a fixed voltage, absorbing input ripple and load changes. See [05](experiments/05-linear-power-supply.md).
- **Relaxation oscillator** — an oscillator built from a capacitor charging toward a threshold, then resetting — giving a repeating ramp/square output (the 555 and the op-amp oscillator). See [10](experiments/10-oscillators.md).
- **Reservoir capacitor** — a large capacitor after a rectifier that holds the voltage up between pulses, turning pulsating DC into nearly-flat DC. See [04](experiments/04-diodes-and-rectification.md).
- **Resonance** — the special frequency where an inductor and capacitor exchange energy back and forth and their reactances cancel; the basis of tuning and filtering. See [03](experiments/03-inductors-and-lc-resonance.md).
- **RF (radio frequency)** — frequencies high enough to radiate as radio waves (roughly tens of kHz and up).
- **Ripple** — the small leftover AC wiggle riding on the DC output of a power supply.
- **Ripple rejection** — how strongly a regulator reduces input ripple (a 78L05 ≈ 1000×). See [05](experiments/05-linear-power-supply.md).
- **Sallen–Key** — a popular op-amp filter design (two resistors, two capacitors, one op-amp) giving a sharp second-order response. See [09](experiments/09-active-filters.md).
- **Saturation** — a transistor turned as fully on as it can go (dropping almost no voltage); the "on" state of a transistor switch. See [06](experiments/06-transistor-as-switch.md).
- **Schmitt trigger** — a comparator with hysteresis: it has two thresholds so it switches crisply and rejects noise. See [10](experiments/10-oscillators.md).
- **Schottky diode** — a diode with an unusually low forward drop (~0.2–0.3 V) and fast switching.
- **SDR (software-defined radio)** — a radio that digitizes the signal early and does the demodulation in software (DSP). The QMX+ is one.
- **Si5351** — a programmable clock-generator chip that synthesizes precise frequencies from a crystal reference (via a PLL); the QMX+'s oscillator.
- **Slew rate** — how fast an amplifier's output can change; too slow and fast edges get rounded off.
- **SSB (single sideband)** — an efficient voice mode used on the ham bands.
- **STM32** — the ARM microcontroller family that runs the QMX+'s DSP and control software.
- **Superheterodyne ("superhet")** — the dominant receiver architecture: mix the incoming signal to a fixed intermediate frequency, then filter and amplify there. See [13](experiments/13-mixers-and-detectors.md).
- **SWR (standing wave ratio)** — a measure of impedance mismatch on a feedline; 1:1 is a perfect match, higher means more reflected power. See [12](experiments/12-lc-filters-and-impedance-matching.md).
- **Tank (circuit)** — a parallel inductor+capacitor that resonates and "rings" at one frequency; the basic tuned circuit. See [03](experiments/03-inductors-and-lc-resonance.md).
- **Time constant (τ)** — the characteristic response time of an RC (`τ = R×C`) or RL (`τ = L/R`) circuit; one τ ≈ 63% of the way to the final value. See [01](experiments/01-rc-time-constant.md).
- **Toroid** — a doughnut-shaped magnetic core you wind wire around to make an inductor; the standard homebrew inductor. Cores like **T37-2** (for ~1–10 MHz) are common. See [12](experiments/12-lc-filters-and-impedance-matching.md).
- **Transistor** — the fundamental active device: a small signal at one terminal controls a much larger current between the other two. Used as a switch ([06](experiments/06-transistor-as-switch.md)) or amplifier ([07](experiments/07-transistor-as-amplifier.md)).
- **Virtual ground** — a reference voltage set at half the supply so a single-supply op-amp can handle signals that swing both up and down. See [08](experiments/08-op-amp-fundamentals.md).
- **VXO (variable crystal oscillator)** — a crystal oscillator whose frequency can be pulled slightly for fine tuning.

## Parts quick-reference

The specific components the experiments call for, and what they are:

| Part | What it is |
|---|---|
| **1N4148** | small-signal silicon diode (fast, general purpose) |
| **1N4007** | 1 A silicon rectifier diode (for power supplies) |
| **1N5817** | Schottky diode (low forward drop) |
| **1N34** | germanium diode (very low drop; classic crystal-radio detector) |
| **2N3904** | NPN bipolar transistor (general-purpose switch/amplifier) |
| **2N7000** | N-channel MOSFET (voltage-controlled switch) |
| **NE555** | timer chip (oscillators, delays) |
| **LM358** | dual op-amp that runs on a single supply |
| **TL072** | dual op-amp, low-noise (good for audio) |
| **78L05** | linear voltage regulator, fixed 5 V, 100 mA |
| **SA612 / NE602** | mixer + oscillator chip for receivers |
| **RP2040** | microcontroller (Raspberry Pi Pico) for the digital experiments and keyboard |
| **Si5351** | programmable clock/frequency synthesizer (in the QMX+) |
| **STM32** | microcontroller running the QMX+'s DSP |
| **T37-2 / T37-6** | powdered-iron toroid cores for winding RF inductors |
| **NanoVNA** | pocket vector network analyzer for measuring RF filters/antennas |

*This glossary is AI-generated; check a trusted reference (ARRL Handbook, datasheets, *The Art of Electronics*) before relying on any definition for something safety-critical.*
