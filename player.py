"""Audio playback functionality across supported system players."""

import shutil
import subprocess
from config import PLAYERS


class PlayerError(Exception):
    """Raised when audio playback fails or no player is available."""
    pass


def play_audio(file_path: str) -> None:
    """Play an audio file using the first available system player."""
    for player, extra_args in PLAYERS:
        if shutil.which(player):
            try:
                subprocess.run([player, *extra_args, file_path], check=True)
                return
            except subprocess.CalledProcessError as err:
                raise PlayerError(f"Playback failed with {player}: {err}") from err

    raise PlayerError(
        "No supported audio player found (install mpv, ffplay, mpg123, or afplay)."
    )
