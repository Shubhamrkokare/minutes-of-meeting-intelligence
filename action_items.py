import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "gemini-2.5-flash"

def extract_action_items(summary: str) -> str:
    prompt = f"""
From the following meeting summary, extract clear action items.

Rules:
- List action items in bullet points
- Mention WHO (if known)
- Mention WHAT needs to be done
- Mention DEADLINE if present
- If no action items, say "No explicit action items found"

Summary:
{summary}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()
