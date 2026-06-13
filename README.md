# RAG Teaching Assistant — Data Science Course

An AI-powered teaching assistant built with Retrieval-Augmented Generation (RAG). It ingests video lectures, transcribes them, indexes the content, and lets students ask questions and get accurate, context-aware answers pulled directly from course material.

---

## What It Does

1. **Video → Audio** — Extracts audio from lecture videos using `ffmpeg`
2. **Audio → Transcript** — Transcribes using OpenAI Whisper (`large-v2`), with Hindi→English translation support
3. **Transcript → Chunks** — Segments transcript into timestamped JSON chunks
4. **Chunks → Vector Store** — Embeds and indexes transcript chunks for semantic search
5. **Query → Answer** — RAG pipeline retrieves relevant chunks and generates answers via LLM

---

## Project Structure

```
.
├── videos/                  # Raw lecture videos
├── audios/                  # Extracted MP3 files
├── transcripts/             # JSON transcript chunks (output.json per video)
├── vectorstore/             # FAISS index (embeddings)
├── process_video.py         # Video → MP3 pipeline
├── stt.py                   # MP3 → transcript chunks (Whisper)
├── embed.py                 # Chunk → vector index (coming)
├── rag.py                   # Query → answer pipeline (coming)
└── README.md
```

---

## Stack

| Layer | Tool |
|---|---|
| Audio extraction | `ffmpeg` |
| Transcription | OpenAI Whisper `large-v2` |
| Embeddings | `sentence-transformers` |
| Vector store | FAISS |
| LLM | Ollama (`qwen2` or similar) |
| Orchestration | LangChain / custom |

---

## Setup

```bash
# Clone
git clone https://github.com/yourusername/rag-teaching-assistant
cd rag-teaching-assistant

# Install dependencies
pip install openai-whisper sentence-transformers faiss-cpu langchain

# Requires ffmpeg installed on system
# Ubuntu/Debian: sudo apt install ffmpeg
# macOS: brew install ffmpeg
```

---

## Usage

### Step 1 — Extract audio from videos
```bash
python process_video.py
```
Reads from `videos/`, writes numbered MP3s to `audios/`.

### Step 2 — Transcribe
```bash
python stt.py
```
Runs Whisper on audio file, outputs timestamped chunks to `output.json`.

### Step 3 — Ask questions *(RAG pipeline — WIP)*
```bash
python rag.py --query "What is the bias-variance tradeoff?"
```

---

## Sample Transcript Output (`output.json`)

```json
[
  { "start": 0.0, "end": 3.0, "text": "Oh, ready for this?" },
  { "start": 3.0, "end": 9.0, "text": "This one has been living in there a very, very long time." }
]
```

---

## Roadmap

- [x] Video → MP3 pipeline
- [x] Whisper transcription with Hindi→English translation
- [ ] Chunk embedding + FAISS indexing
- [ ] RAG query pipeline
- [ ] Streamlit UI for students
- [ ] Multi-video support with metadata tagging
- [ ] Timestamped answer citations ("from lecture 3, 04:12")

---

## Why RAG Over Fine-Tuning

Fine-tuning a model on course content is expensive and goes stale when material updates. RAG keeps the knowledge base separate — swap in new lectures, re-index, done. Answers are grounded in actual course content, not hallucinated from general training.

---

## Author

**ABJ** — Computer Engineering, Zeal College of Engineering and Research, Pune  
Built as part of a larger AI/MLOps portfolio.
