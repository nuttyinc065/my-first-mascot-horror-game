# The Anomlys

A mascot-horror experience inside Nutty'Inc — now delivered as a
Minecraft datapack that turns your world into a creeping, corrupted
facility run by a sentient mascot. The pack drives a 3D, in-engine loop
with nights, corruption pressure, and ambient scares suitable for
multiplayer sessions.

## What's included
- **Minecraft datapack**: Nightly corruption loop, bossbar tracking,
  ambient effects, and summonable mascot threats to play fully in 3D.
- **Command-driven menu**: Use `/function` calls to start, pause, and
  reset sessions without leaving the world.
- **Legacy console prototype**: The original C++ and Python console
  loops remain for reference while the datapack becomes the primary path
  to play.

## Quickstart (Minecraft datapack)
1. Copy the `minecraft/datapack` folder into your world save under
   `world/datapacks/the-anomlys`.
2. Launch the world, then run:
   ```
   /reload
   /function anomlys:start
   ```
3. Watch the corruption bossbar rise each second. Survive as nights
   advance and the mascot spawns new threats.
4. Pause or wipe progress anytime:
   ```
   /function anomlys:stop
   /function anomlys:reset
   ```

## Quickstart (legacy C++ prototype)
1. Ensure you have a C++17 toolchain and CMake 3.16+ available.
2. Configure and build:
   ```bash
   cmake -S . -B build
   cmake --build build
   ```
3. Run the prototype:
   ```bash
   ./build/the_anomlys
   ```

## Further reading
- [`docs/design.md`](docs/design.md) — tone, level beats, corruption
  phases, and main menu requirements.
- [`docs/minecraft-mode.md`](docs/minecraft-mode.md) — how the datapack
  maps mascot horror beats onto Minecraft systems and how to extend it.
