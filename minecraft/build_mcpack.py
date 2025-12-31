#!/usr/bin/env python3
"""Build a distributable .mcpack archive for The Anomlys datapack.

This script zips the contents of `minecraft/datapack` into
`minecraft/anomlys.mcpack` so it can be dropped directly into a world or
shared with others. Use --output to change the destination.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def build_mcpack(source_root: Path, output_path: Path, overwrite: bool = False) -> None:
    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"Refusing to overwrite existing file: {output_path}. Use --overwrite to replace it."
        )

    if not source_root.exists():
        raise FileNotFoundError(f"Source datapack folder does not exist: {source_root}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output_path, "w", compression=ZIP_DEFLATED) as archive:
        for file_path in sorted(source_root.rglob("*")):
            if file_path.is_file():
                relative = file_path.relative_to(source_root)
                archive.write(file_path, arcname=relative.as_posix())



def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        "-o",
        default=str(Path(__file__).parent / "anomlys.mcpack"),
        help="Destination .mcpack file (default: minecraft/anomlys.mcpack)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace the existing output file if it already exists.",
    )
    return parser.parse_args(argv)



def main(argv: list[str]) -> int:
    args = parse_args(argv)
    source_root = Path(__file__).parent / "datapack"
    output_path = Path(args.output)

    try:
        build_mcpack(source_root, output_path, overwrite=args.overwrite)
    except Exception as exc:  # noqa: BLE001 - surface actionable errors to the CLI
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Built: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
