# Project 2 — Traffic Light Controller

Traffic light controller implemented using **Simulink + Stateflow** and deployed to Arduino hardware. The assignment uses a Mealy-style state machine with three operating modes and three external LEDs.

## Required behavior

| Mode input | Mode | Repeating sequence |
| ---: | --- | --- |
| `0` | Normal | Green 5 s → Yellow 2 s → Red 5 s |
| `1` | Emergency | Red 1 s → Yellow 1 s |
| `2` | Maintenance | All LEDs on 1 s → All LEDs off 1 s |

## System architecture

```text
Dashboard Knob / Constant
           |
           v
     Stateflow Chart
      |     |     |
   green yellow  red
      |     |     |
 Boolean conversion
      |     |     |
     D10   D11   D12
      |     |     |
   Green Yellow  Red LEDs
```

## Stateflow hierarchy

```text
TrafficLightController
├── Normal
│   ├── N_Green      (5 s)
│   ├── N_Yellow     (2 s)
│   └── N_Red        (5 s)
├── Emergency
│   ├── E_Red        (1 s)
│   └── E_Yellow     (1 s)
└── Maintenance
    ├── M_AllOn      (1 s)
    └── M_AllOff     (1 s)
```

The design has three composite mode states and seven operating substates. Mode-level transitions allow the controller to change mode during one simulation run.

## Stateflow data

| Name | Scope | Type | Description |
| --- | --- | --- | --- |
| `mode` | Input | `uint8` | 0 Normal, 1 Emergency, 2 Maintenance |
| `green` | Output | `boolean` | Green LED command |
| `yellow` | Output | `boolean` | Yellow LED command |
| `red` | Output | `boolean` | Red LED command |

Timed transitions use temporal logic such as:

```text
[after(5,sec)]/{green=0; yellow=1; red=0;}
```

## Hardware setup

Required parts:

- Arduino Nano 33 BLE family board and USB data cable
- Green, yellow, and red LEDs
- Three 220–330 Ω current-limiting resistors
- Breadboard and jumper wires

```text
D10 ── resistor ── Green LED  ── GND
D11 ── resistor ── Yellow LED ── GND
D12 ── resistor ── Red LED    ── GND
```

The long LED leg (anode) faces the GPIO/resistor side. The short leg (cathode) connects to GND. Each LED must have its own resistor.

## Simulink hardware configuration

1. Install **Simulink Support Package for Arduino Hardware** from MATLAB Add-Ons.
2. Connect the board using a USB data cable.
3. In **Model Settings → Hardware Implementation**, select the hardware target matching the board.
4. Test one channel using `Constant(1) → Digital Output D10`.
5. Connect Stateflow outputs to Digital Output blocks on D10, D11, and D12.
6. Use **Monitor & Tune** to change `mode` and observe the chart and physical LEDs.
7. Use **Build, Deploy & Start** for standalone execution.

## Test plan

| Test | Expected result |
| --- | --- |
| Normal | Green 5 s, yellow 2 s, red 5 s for at least two cycles |
| Emergency | Red and yellow alternate every 1 s; green remains off |
| Maintenance | All LEDs turn on and off together every 1 s |
| Normal → Emergency | Enter Emergency and start with red |
| Emergency → Maintenance | Enter Maintenance and start with all LEDs on |
| Maintenance → Normal | Enter Normal and start with green |
| Hardware | Physical LEDs match Stateflow outputs and Dashboard Lamps |

## Repository layout

```text
project2/
├── README.md
├── model/          # Simulink .slx file
├── screenshots/    # Model, Stateflow, and Scope captures
├── hardware/       # Wiring diagram and hardware photographs
├── report/         # Final report
└── demo/           # Demonstration video link or notes
```

## Submission checklist

- [ ] Top-level Simulink diagram screenshot
- [ ] Stateflow chart screenshot
- [ ] Explanation of operating principle
- [ ] State count and refinement-state explanation
- [ ] Simulation results for all three modes
- [ ] Mode-switching test
- [ ] Working Arduino and external LED demonstration
- [ ] Screen recording showing Stateflow and traffic-light outputs
- [ ] Final `.slx` model and report
