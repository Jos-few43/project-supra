# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

SSBM (Super Smash Bros. Melee) AI environment using Slippi Dolphin and libmelee for reinforcement learning. Currently Phase 1 skeleton.

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10 |
| ML | PyTorch |
| Game | libmelee (Melee binding) |
| Emulator | Dolphin (Slippi variant) |
| Display | Xvfb (headless rendering) |
| Packaging | Docker (Ubuntu 22.04 base) |

## Project Structure

```
project-supra/
└── phase1/
    ├── Dockerfile     # Ubuntu 22.04, Python 3.10, Dolphin PPA, libmelee, PyTorch
    └── scripts/       # Training scripts placeholder
```

## Key Commands

```bash
docker build -t project-supra-phase1 phase1/
docker run project-supra-phase1 agent.py <args>
```

## Architecture

Dockerfile manages Xvfb virtual display for headless gameplay. Entrypoint starts virtual display then runs agent script.

## Things to Avoid

- Don't use Python 3.12+ — libmelee compatibility requires 3.10
- Don't run without GPU access — PyTorch training needs CUDA
