# Logos (λόγος)

A minimal, modular, lightweight Python CLI text-to-speech tool powered by Microsoft Edge TTS.

## Project Structure

```text
logos/
├── main.py       # Root CLI entry point
├── cli.py        # Argument parsing & stdin extraction
├── tts.py        # Edge-TTS speech generation logic
├── player.py     # System audio player detection & playback
├── config.py     # Voice & player configurations
└── README.md     # Documentation
```

## Requirements

- Python 3.9+
- External dependency: `edge-tts`
- An installed audio player for playback: `mpv`, `ffplay`, `mpg123`, or `afplay`

## Installation

1. Install the `edge-tts` package:
   ```bash
   pip install edge-tts
   ```

2. Make `main.py` executable:
   ```bash
   chmod +x main.py
   ```

3. (Optional) Create a global command named `logos`:
   ```bash
   mkdir -p ~/.local/bin
   ln -sf "$(pwd)/main.py" ~/.local/bin/logos
   ```
   *Make sure `~/.local/bin` is in your `PATH`.*

## Usage

```bash
# Default playback with natural female voice (en-US-AriaNeural)
python3 main.py "Hello, how are you?"

# Play using natural male voice (en-US-GuyNeural)
python3 main.py "Hello, how are you?" --male

# Play using explicit female voice
python3 main.py "Hello there" --female

# Save to an MP3 file (does not play)
python3 main.py "This is a test" -o hello.mp3

# Read text from stdin
echo "Quick message" | python3 main.py

# Read text from stdin with male voice
echo "Quick message" | python3 main.py --male

# Save and play simultaneously
python3 main.py "Play this message" -o speech.mp3 --play
```

If you created the `logos` symlink:

```bash
logos "Hello, world!"
echo "Piped message" | logos --male
```

## Options

| Option | Description |
|---|---|
| `text` | Positional text argument to speak (or piped via stdin) |
| `--male` | Use male English voice (`en-US-GuyNeural`) |
| `--female` | Use female English voice (`en-US-AriaNeural`, default) |
| `-o, --output` | Path to save speech audio as an MP3 file |
| `--play` | Explicitly play generated audio |
| `-h, --help` | Show help and exit |
