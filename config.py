"""Configuration constants for voices and audio players."""

DEFAULT_FEMALE_VOICE = "en-US-AriaNeural"
DEFAULT_MALE_VOICE = "en-US-GuyNeural"

PLAYERS = [
    ("mpv", ["--no-terminal"]),
    ("ffplay", ["-nodisp", "-autoexit", "-loglevel", "quiet"]),
    ("mpg123", ["-q"]),
    ("afplay", []),
]
