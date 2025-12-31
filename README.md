# The Anomlys

A mascot-horror concept set inside Nutty'Inc — a toy innovation facility
where the house mascot fractures into an unpredictable threat. This
repository provides a text-first prototype plus design notes for the
future 3D multiplayer build.

## Features
- **Main menu loop**: Start a shift, read lore, check multiplayer
  presence, or quit.
- **Nightly corruption**: Corruption increases each night, changing
  environmental descriptions and event intensity.
- **Multiplayer flavor**: Simulated peers remind you the experience is
  meant for co-op play.

## Quickstart (Prototype)
1. Ensure you have Python 3.9+ available.
2. Run the prototype:
   ```bash
   python game/main.py
   ```
3. Use the menu to start a shift, read lore, or view session status.

The script is intentionally lightweight and text-based so you can
prototype pacing before implementing the full 3D multiplayer version.

## Design Outline
See [`docs/design.md`](docs/design.md) for tone, level beats, corruption
phases, and main menu requirements tailored for a multiplayer 3D build.
