import os
import time

from audtoscript import transcribe_audio
from conversation_builder import build_conversation
from summarizer import generate_summary
from action_items import extract_action_items
from sentiment_analysis import analyze_sentiment


def run_pipeline(audio_path, status_callback=None):
    """
    audio_path: path to uploaded audio (from dashboard or CLI)
    status_callback: optional function to push live updates (Streamlit)
    """

    def update(msg):
        print(msg)  # keep terminal logs
        if status_callback:
            status_callback(msg)

    run_id = f"run_{int(time.time())}"
    run_dir = os.path.join("runs", run_id)
    os.makedirs(run_dir, exist_ok=True)

    audio_out = os.path.join(run_dir, "audio.mp3")
    transcript_out = os.path.join(run_dir, "transcript.txt")
    conversation_out = os.path.join(run_dir, "conversation.txt")

    # Copy audio into run folder
    with open(audio_path, "rb") as src, open(audio_out, "wb") as dst:
        dst.write(src.read())

    update("🔹 Step 1: Transcribing audio...")
    transcript = transcribe_audio(
        audio_path=audio_out,
        output_transcript_path=transcript_out
    )

    update("🔹 Step 2: Building conversation...")
    conversation = build_conversation(
        transcript_path=transcript_out,
        output_path=conversation_out
    )

    update("🔹 Step 3: Generating summary...")
    summary = generate_summary(conversation)

    update("🔹 Step 4: Extracting action items...")
    actions = extract_action_items(summary)

    update("🔹 Step 5: Analyzing sentiment...")
    sentiment = analyze_sentiment(conversation)

    update("✅ Pipeline completed successfully")

    return {
        "run_id": run_id,
        "summary": summary,
        "action_items": actions,
        "sentiment": sentiment,
        "run_dir": run_dir
    }


# Standalone CLI test (UNCHANGED BEHAVIOR)
if __name__ == "__main__":
    result = run_pipeline("meeting_audio.mp3")
    print(result)
