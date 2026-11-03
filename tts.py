"""Text-to-speech generation using edge-tts."""

import edge_tts


async def generate_speech(text: str, voice: str, output_path: str) -> None:
    """Generate speech audio file from text using edge-tts."""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)
