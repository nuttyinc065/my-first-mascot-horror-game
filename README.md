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
1. Option A: Build an importable archive (recommended for Realms/clients)
   ```bash
   python minecraft/build_mcpack.py --overwrite
   ```
   Then drop the generated `minecraft/anomlys.mcpack` into your world save
   under `world/datapacks` (or unzip/rename it to `.zip` if your launcher
   prefers).
2. Option B: Copy the raw `minecraft/datapack` folder directly into your
   world under `world/datapacks`.
3. Launch the world, then run:
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

## Rebuild the .mcpack
If you tweak the datapack files, regenerate the distributable archive
(ignored by Git to keep the repo source-only):

```bash
python minecraft/build_mcpack.py --overwrite
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
