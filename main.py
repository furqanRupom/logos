#!/usr/bin/env python3
"""Logos: Minimal Text-to-Speech CLI using Microsoft Edge TTS.

Installation:
  pip install edge-tts

Usage:
  python3 main.py "Hello, world!"
  python3 main.py "Hello, world!" --male
  python3 main.py "Hello, world!" --female
  python3 main.py "Hello, world!" -o output.mp3
  echo "Hello from stdin" | python3 main.py
"""

import asyncio
import os
from pathlib import Path
import sys
import tempfile

# Ensure the module directory is in sys.path when invoked directly or via symlink
sys.path.insert(0, str(Path(__file__).resolve().parent))

from cli import get_text_input, parse_args
from config import DEFAULT_FEMALE_VOICE, DEFAULT_MALE_VOICE
from player import PlayerError, play_audio
from tts import generate_speech


def run() -> None:
    args = parse_args()

    try:
        text = get_text_input(args.text)
    except ValueError as err:
        sys.exit(f"Error: {err}")

    voice = DEFAULT_MALE_VOICE if args.male else DEFAULT_FEMALE_VOICE
    save_file = args.output
    should_play = args.play or not save_file

    try:
        if save_file:
            asyncio.run(generate_speech(text, voice, save_file))
            if should_play:
                play_audio(save_file)
        else:
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                tmp_path = tmp.name
            try:
                asyncio.run(generate_speech(text, voice, tmp_path))
                play_audio(tmp_path)
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
    except KeyboardInterrupt:
        sys.exit(130)
    except (PlayerError, Exception) as exc:
        sys.exit(f"Error: {exc}")


if __name__ == "__main__":
    run()
