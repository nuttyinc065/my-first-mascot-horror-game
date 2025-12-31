# The Anomlys: Minecraft mode

This datapack turns any survival or creative world into a Nutty'Inc
blacksite. It keeps the mascot horror loop entirely in Minecraft so you
get 3D movement, lighting, and co-op without external binaries.

## Feature map
- **Nights & corruption**: A bossbar ticks up every second. When it hits
  100, the night advances, corruption resets to 10, and a new mascot
  encounter is spawned near every player.
- **Mascot pressure**: Each night spawns a carved-pumpkin zombie named
  "Nutty Mascot." Swap the summon in `data/anomlys/functions/advance_night.mcfunction`
  to any custom entity or model from your resource pack.
- **Ambient dread**: Darkness, cave ambience, and soul particles scale
  up as corruption rises. Milestone callouts appear in the action bar.
- **Commands as a menu**:
  - `/function anomlys:start` to begin Night 1 and show the bossbar.
  - `/function anomlys:stop` to pause the loop.
  - `/function anomlys:reset` to wipe state, rejoin players to the
    Anomlys team, and hide the bossbar.

## Installation
1. Copy `minecraft/datapack` into your world save: `world/datapacks/the-anomlys`.
2. In-game run `/reload`.
3. Start a session with `/function anomlys:start`.

## Extending the mode
- **Custom mascot model**: Pair this datapack with a resource pack that
  swaps the `carved_pumpkin` helmet model to your mascot suit. The
  summon is in `advance_night.mcfunction`.
- **Co-op utilities**: Use the `AnomlysPlayers` team created on reset to
  manage friendly fire, glowing outlines, or shared loot tables.
- **Corruption pacing**: Tweak tick speed or thresholds in
  `night_tick.mcfunction` to control how fast nights advance or when
  warning beats fire.

## Version targets
- Datapack `pack_format` is set to `15`, aligning with Minecraft 1.20.5+
  (and 1.21). Adjust the number if you target older versions.
