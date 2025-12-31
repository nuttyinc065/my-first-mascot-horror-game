# The Anomlys: Nutty'Inc Facility (Design Outline)

This document captures the playable pillars of **The Anomlys**, a 3D
multiplayer mascot-horror experience set inside Nutty'Inc.

## Tone & Mascot
- **Mascot**: "The Anomlys" — a patchwork mascot wrapped in cracked
  porcelain plates and metallic seams reminiscent of the provided
  reference image (black, gold, and white tiles). Its skin shifts during
  corruption, exposing chrome and stray puppet joints.
- **Threat Profile**: The mascot mirrors player silhouettes, imitating
  nearby animations with distorted timing.
- **VO/Audio**: Layered radio-static murmurs; nursery-rhyme fragments
  that desync as corruption rises.

## Setting: Nutty'Inc
- Toy innovation campus with research labs, mascot rehearsal stage,
  fabrication floor, and a maintenance tunnel network.
- Environmental storytelling through signage, shipping labels, and
  mascot rehearsal scripts.

## Game Loop (Nights)
1. **Prep (Lobby/Main Menu)**: Players see the shift briefing, pick
   gadgets, and ready up. Host can start the shift when a quorum is
   ready.
2. **Exploration (Night)**: Objectives shift nightly (restore power,
   retrieve mascot routine cards, reboot cameras).
3. **Corruption Tick**: Every few minutes (or after loud actions),
   corruption rises. Visuals smear, UI glitches, and mascot patrols gain
   new routes.
4. **Extraction**: Escape or seal the wing before the corruption meter
   reaches 100%.

## Corruption Escalation
- **0-25%**: Clean environment, stable lighting; mascot dormant.
- **25-50%**: Flickering lights, posters distort; mascot hums in vents.
- **50-75%**: Physics hiccups, doubled footsteps; mascot stalks in
  mirrored hallways.
- **75-100%**: Reality breaks, level geometry warps, mascot fully
  aggressive; UI shaders corrupt.

## Main Menu Requirements
- Title splash with Nutty'Inc security warning.
- Options: Start Shift, Intel/Lore, Session Status, Settings, Quit.
- Background: looping camera feed of the rehearsal stage with occasional
  corruption glitches.

## Multiplayer Pillars
- **Co-op**: Up to 4 players; shared corruption meter.
- **Session Host**: Determines start of night; matchmaking via room code.
- **Shared Events**: Mascot triggers ripple effects visible to all
  players (e.g., synchronized light bursts).
- **Voice/Proximity Chat**: Distorts with corruption.

## Nightly Objective Pool
- Recover mascot choreography cards to calm its pathfinding.
- Recalibrate projector arrays to slow corruption ticks.
- Seal vent covers while The Anomlys attempts to mirror players.
- Escort a toy prototype cart without letting The Anomlys touch it.

## Prototype Notes
- The `game/main.py` script provides a text-first mock-up of the menu and
  night progression. Use it to validate pacing before building the full
  3D levels.
