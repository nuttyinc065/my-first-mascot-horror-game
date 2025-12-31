"""
Text-first prototype for "The Anomlys".

This is not a full 3D build; instead it captures the main menu flow,
nightly corruption escalation, and multiplayer session flavor text for
Nutty'Inc. Use it as a narrative and mechanical reference when
implementing the actual 3D multiplayer experience.
"""
from __future__ import annotations

import random
import textwrap
from dataclasses import dataclass, field
from typing import List


LORE = textwrap.dedent(
    """
    Nutty'Inc began as a cheerful toy research hub. Something inside its
    vaults turned the mascot, The Anomlys, into a fractured entity that
    mirrors every guest. Each "night" is a containment shift: lights
    flicker, signage changes, and the mascot's patchwork skin reveals
    more jagged chrome and cracked porcelain.

    Multiplayer runs are framed as simultaneous shifts. Each player sees
    the same facility layout, but corruption indexes are shared: when one
    player disturbs an anomaly, everyone feels the static.
    """
)


CORRUPTION_STAGES = [
    (0, "Clean corridors, muted hum of servers."),
    (15, "Static creeps into the PA system."),
    (30, "Safety posters peel into unreadable glyphs."),
    (45, "Lights dim; mascot murals gain extra eyes."),
    (60, "Gravity hiccups in certain labs."),
    (75, "Reality smears; walls breathe with patchwork seams."),
    (90, "Full distortion; The Anomlys speaks in overlapping voices."),
]


PLAYER_NAMES = [
    "Echo", "Patch", "Naut", "Lumen", "Gasket", "Rivet", "Vox", "Glyph",
]


@dataclass
class GameState:
    nights_survived: int = 0
    corruption: int = 0
    connected_players: List[str] = field(default_factory=list)

    def spawn_players(self, total: int = 3) -> None:
        random.shuffle(PLAYER_NAMES)
        self.connected_players = PLAYER_NAMES[:total]

    def corruption_description(self) -> str:
        stage = max((desc for threshold, desc in CORRUPTION_STAGES if self.corruption >= threshold),
                    default="The facility feels abandoned.")
        return stage

    def new_night(self) -> str:
        self.nights_survived += 1
        added = random.randint(12, 24)
        self.corruption = min(100, self.corruption + added)
        return self.corruption_description()


class NuttyIncGame:
    def __init__(self) -> None:
        self.state = GameState()
        self.state.spawn_players()

    def banner(self) -> None:
        print("=" * 64)
        print("     THE ANOMLYS :: Nutty'Inc Facility // Multiplayer Prototype")
        print("=" * 64)

    def main_menu(self) -> None:
        self.banner()
        print("Main Menu")
        print("1) Begin Night Shift")
        print("2) Review LORE//INTEL")
        print("3) View Session Status")
        print("4) Quit")

    def run(self) -> None:
        while True:
            self.main_menu()
            choice = input("Select option: ").strip()
            if choice == "1":
                self.handle_night_shift()
            elif choice == "2":
                self.show_lore()
            elif choice == "3":
                self.show_session_status()
            elif choice == "4":
                print("Logging out of Nutty'Inc secure mesh. Stay unstable.")
                break
            else:
                print("Unknown selection. The intercom crackles disapprovingly.\n")

    def show_lore(self) -> None:
        self.banner()
        print(textwrap.fill(LORE, width=72))
        input("\nPress Enter to return to the main menu...")

    def show_session_status(self) -> None:
        self.banner()
        print(f"Nights survived: {self.state.nights_survived}")
        print(f"Current corruption: {self.state.corruption}%")
        print(f"Environment: {self.state.corruption_description()}")
        if self.state.connected_players:
            print("Connected players:")
            for name in self.state.connected_players:
                print(f"  - {name}")
        else:
            print("No peers online. The mesh feels too quiet.")
        input("\nPress Enter to return to the main menu...")

    def handle_night_shift(self) -> None:
        self.banner()
        description = self.state.new_night()
        night = self.state.nights_survived
        print(f"Night {night}: corruption rises to {self.state.corruption}%.")
        print(textwrap.fill(description, width=70))
        self.scariness_prompt(night)
        input("\nPress Enter to survive to the next menu...")

    def scariness_prompt(self, night: int) -> None:
        severity = min(5, 1 + night // 2)
        warnings = [
            "You hear The Anomlys scrape along the vents.",
            "A locker pops open; something wearing patchwork skin peers out.",
            "Security drones glitch, hovering just overhead.",
            "Floor panels bloom with black-and-white static.",
            "Your reflection smiles half a second late.",
        ]
        print("\nShift Events:")
        for _ in range(severity):
            print(f" - {random.choice(warnings)}")


def main() -> None:
    game = NuttyIncGame()
    try:
        game.run()
    except KeyboardInterrupt:
        print("\nEmergency logout acknowledged. Corruption contained (for now).")


if __name__ == "__main__":
    main()
