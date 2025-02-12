from pathlib import Path

from app.openai.config import Config as c

class SpeechToText():


    def transcription(self, audio_path: str) -> str:
        audio_file = open(audio_path, "rb")
        transcription = c.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        print(transcription.text)
        return transcription.text