import sys
import os
import time
import tempfile
import streamlit as st

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from pipeline import run_pipeline

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Minutes of Meeting Intelligence",
    layout="wide"
)

# -------------------------------
# Background video (optional)
# -------------------------------
st.markdown("""
<style>
video {
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;
    opacity: 0.15;
}
</style>

<video autoplay muted loop>
  <source src="https://cdn.coverr.co/videos/coverr-typing-on-a-laptop-9711/1080p.mp4" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown("""
# 🧠 Minutes of Meeting — AI Intelligence System
### Audio → Transcript → Insights → Decisions
""")

st.divider()

# -------------------------------
# Upload
# -------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload meeting audio (mp3 / wav)",
    type=["mp3", "wav"]
)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(uploaded_file.getbuffer())
        temp_audio_path = temp_audio.name

    st.success("Audio uploaded successfully")

    if st.button("🚀 Start Analysis", use_container_width=True):

        progress = st.progress(0)
        status = st.empty()

        # Fake live transcription (UX trick)
        status.info("🎙️ Transcribing audio...")
        progress.progress(20)
        time.sleep(1.5)

        status.info("🧩 Structuring conversation...")
        progress.progress(40)
        time.sleep(1.2)

        status.info("📝 Generating summary...")
        progress.progress(60)
        time.sleep(1.0)

        status.info("📌 Extracting action items...")
        progress.progress(80)
        time.sleep(1.0)

        # REAL processing
        start = time.time()
        result = run_pipeline(temp_audio_path)
        elapsed = round(time.time() - start, 2)

        progress.progress(100)
        status.success(f"✅ Completed in {elapsed} seconds")

        st.divider()

        # -------------------------------
        # Results
        # -------------------------------
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("## 📄 Minutes of Meeting")
            st.markdown(
                f"<div style='font-size:18px; line-height:1.7'>{result['summary']}</div>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown("## 📌 Action Items")
            if result["action_items"]:
                st.write(result["action_items"])
            else:
                st.info("No explicit action items found.")

            st.markdown("## 😊 Sentiment")
            st.success(result["sentiment"])

        st.divider()
        st.caption(f"Run ID: `{result['run_id']}`")
        st.caption(f"Artifacts saved in: `{result['run_dir']}`")

        os.remove(temp_audio_path)
