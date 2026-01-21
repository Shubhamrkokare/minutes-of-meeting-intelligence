# 🧠 Minutes of Meeting Intelligence System

An end-to-end AI system that converts raw meeting audio into structured **Minutes of Meeting (MoM)** with summaries, action items, and sentiment insights — delivered through an interactive dashboard.

---

## 🚀 Overview

This project automates the complete post-meeting documentation workflow by combining **speech recognition**, **LLM-based reasoning**, and **fine-tuned summarization models**.

Given a meeting audio file, the system:
- Transcribes speech to text
- Structures conversation context
- Generates concise MoM summaries
- Extracts action items
- Performs sentiment analysis
- Presents results in a professional Streamlit dashboard

---

## 🧩 System Architecture

Audio File
↓
Speech-to-Text (Whisper)
↓
Conversation Structuring (LLM)
↓
Summarization (Fine-tuned BART + LoRA)
↓
Action Item Extraction
↓
Sentiment Analysis
↓
Streamlit Dashboard + Artifacts


Each run is isolated and stored inside a timestamped `runs/` directory for traceability.

---

## 🔧 Tech Stack

### Core Technologies
- **Python**
- **Streamlit** – Interactive dashboard
- **OpenAI Whisper** – Speech-to-text transcription
- **BART (facebook/bart-large-cnn)** – Summarization
- **LoRA (PEFT)** – Parameter-efficient fine-tuning
- **NLTK (VADER)** – Sentiment analysis
- **Gemini API** – Conversation structuring & reasoning

### ML & NLP
- Hugging Face Transformers
- PEFT (LoRA)
- DialogSum dataset (for fine-tuning)

---

## 📁 Project Structure

Minutes of Meetings/
│
├── dashboard/
│ └── app.py # Streamlit UI
│
├── models/
│ └── bart_dialogsum_lora/ # Fine-tuned LoRA adapters
│
├── runs/
│ └── run_<timestamp>/ # Per-run artifacts
│
├── audtoscript.py # Whisper transcription
├── conversation_builder.py # Conversation structuring
├── summarizer.py # BART-based summarization
├── action_items.py # Action item extraction
├── sentiment_analysis.py # Sentiment scoring
├── pipeline.py # End-to-end pipeline
├── pdf_generator.py # PDF export (optional)
├── .gitignore
└── README.md


---

## 🧪 How It Works (Pipeline)

1. **Audio Upload**
   - User uploads `.mp3` or `.wav` file via dashboard

2. **Transcription**
   - Whisper converts audio → raw transcript

3. **Conversation Structuring**
   - Transcript is structured into speaker-aware dialogue

4. **Summarization**
   - Fine-tuned BART (LoRA) generates MoM-style summary

5. **Action Item Extraction**
   - Tasks, responsibilities, and follow-ups are identified

6. **Sentiment Analysis**
   - Overall and detailed sentiment scores are computed

7. **Results Display**
   - Output shown in Streamlit UI
   - Artifacts stored in `runs/`

---

## 🖥️ Dashboard Features

- Audio upload & validation
- Real-time processing feedback
- Clean MoM summary view
- Action item section
- Sentiment indicators
- Run metadata & artifact tracking

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/minutes-of-meeting-intelligence.git
cd minutes-of-meeting-intelligence

2️⃣ Create Virtual Environment
        python -m venv .venv
        .\.venv\Scripts\Activate.ps1   # Windows

3️⃣ Install Dependencies
        pip install -r requirements.txt

4️⃣ Run Dashboard
        streamlit run dashboard/app.py
