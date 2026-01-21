import whisper
import os
os.makedirs("whisper_models", exist_ok=True)
def transcribe_audio(
    audio_path="meeting_audio.mp3",
    output_transcript_path="meeting_transcript.txt"
):
    print("🔹 Loading Whisper model...")
    model = whisper.load_model(
    "small",
    download_root=os.path.join(os.getcwd(), "whisper_models")
)

    print("🔹 Model loaded successfully.")

    # Safety check
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    print("🔹 Audio file found.")
    print("🔹 Starting transcription (this may take time)...")

    result = model.transcribe(
        audio_path,
        fp16=False,
        verbose=True
    )

    print("🔹 Transcription completed.")
    print("🔹 Detected language:", result.get("language"))

    transcribed_text = result.get("text", "").strip()

    with open(output_transcript_path, "w", encoding="utf-8") as f:
        f.write(transcribed_text)

    print(f"✅ Transcription completed and saved to {output_transcript_path}")
    return transcribed_text


# Allows running this file directly (UNCHANGED BEHAVIOR)
if __name__ == "__main__":
    transcribe_audio()
