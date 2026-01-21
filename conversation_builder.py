import os
from google import genai

def build_conversation(
    transcript_path="meeting_transcript.txt",
    output_path="conversation_transcript.txt"
):
    if not os.path.exists(transcript_path):
        raise FileNotFoundError(f"Transcript not found: {transcript_path}")

    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript_text = f.read().strip()

    if not transcript_text:
        raise ValueError("Transcript is empty.")

    prompt = f"""
Convert the following meeting transcript into a conversation-style format.

Rules:
- Do NOT summarize
- Do NOT remove any information
- Preserve all content
- Split into logical conversational turns
- Use generic labels like Speaker 1, Speaker 2, etc.
- Do NOT invent facts
- Output ONLY the conversation

Transcript:
{transcript_text}
"""

    print("🔹 Sending transcript to Gemini for conversation building...")

    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    conversation_text = response.text.strip()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(conversation_text)

    print(f"✅ Conversation transcript saved to {output_path}")
    return conversation_text


# Standalone execution (UNCHANGED)
if __name__ == "__main__":
    build_conversation()
