# Intro to CPS

Coursework and project workspace for **2103610 — Introduction to Cyber Physical System**, Chulalongkorn University.

## Course information

- **Thai title:** ระบบกายภาพที่เชื่อมประสานด้วยเครือข่ายไซเบอร์เบื้องต้น
- **Department:** Mechanical Engineering, Faculty of Engineering
- **Instructor:** Nattapol Damrongplasit (ณัฐพล ดำรงค์พลาสิทธิ์)
- **Credits:** 3.0 (3.0-0.0-9.0)
- **Course page:** 2026/1, Section 1
- **Source:** [myCourseVille syllabus](https://www.mycourseville.com/?q=courseville/course/86695/syllabus) (login required)

## Current project

**Project 2 — Traffic Light Controller** implements a three-mode traffic light using Simulink, Stateflow, and Arduino hardware.

- Normal: Green 5 s → Yellow 2 s → Red 5 s
- Emergency: Red 1 s → Yellow 1 s
- Maintenance: All LEDs on 1 s → All LEDs off 1 s

See [project2/README.md](project2/README.md) for the architecture, hardware wiring, Simulink setup, test plan, and submission checklist.

## Repository structure

```text
intro-to-cps/
├── readme.md
└── project2/
    ├── README.md
    ├── model/
    ├── screenshots/
    ├── hardware/
    ├── report/
    └── demo/
```

## Getting started

1. Install **Simulink Support Package for Arduino Hardware**.
2. Open [project2/README.md](project2/README.md).
3. Add the completed Simulink model under `project2/model/`.
4. Add screenshots, hardware evidence, report, and demonstration materials to their matching folders.

Official requirements and updates remain available on myCourseVille.
