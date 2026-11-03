"""Command-line interface argument parsing and input extraction."""

import argparse
import sys
from config import DEFAULT_FEMALE_VOICE, DEFAULT_MALE_VOICE


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Logos: Minimal, natural-sounding Text-to-Speech CLI."
    )
    parser.add_argument("text", nargs="?", help="Text to convert to speech")
    voice_group = parser.add_mutually_exclusive_group()
    voice_group.add_argument(
        "--male",
        action="store_true",
        help=f"Use natural male voice ({DEFAULT_MALE_VOICE})",
    )
    voice_group.add_argument(
        "--female",
        action="store_true",
        help=f"Use natural female voice ({DEFAULT_FEMALE_VOICE})",
    )
    parser.add_argument("-o", "--output", help="Save generated speech as an MP3 file")
    parser.add_argument(
        "--play",
        action="store_true",
        help="Play audio (default when no output file is set)",
    )
    return parser.parse_args(args)


def get_text_input(pos_text: str | None) -> str:
    """Extract input text from positional arguments or stdin."""
    if pos_text:
        return pos_text.strip()

    if not sys.stdin.isatty():
        piped_text = sys.stdin.read().strip()
        if piped_text:
            return piped_text

    raise ValueError("No text provided. Pass text as an argument or pipe via stdin.")
