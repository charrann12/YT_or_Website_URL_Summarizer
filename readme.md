# AI Text Summarizer using LangChain & Groq

An AI-powered text summarization application built using Streamlit, LangChain, and Groq LLMs.  
The application can summarize content from:

- YouTube videos
- Website URLs

The app extracts the content, processes it using LangChain document loaders, and generates concise summaries using Groq-hosted LLMs.

---

## Features

- Summarize YouTube video transcripts
- Summarize website articles and blogs
- Fast inference using Groq LLMs
- Streamlit-based interactive UI
- URL validation
- Supports long content summarization using LangChain `map_reduce` chain

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- YouTube Transcript API
- Unstructured
- Validators

---

## Project Structure

```bash
.
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Required Packages

```txt
streamlit
langchain
langchain-community
langchain-groq
validators
youtube-transcript-api
unstructured
pytube
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Usage

1. Enter your Groq API key in the sidebar
2. Paste a YouTube URL or website URL
3. Click on **Summarize**
4. Get an AI-generated summary instantly

---

## Supported Models

Example model used:

```python
llama-3.3-70b-versatile
```

You can also use:
- `llama-4-scout-17b-16e-instruct`
- `llama-4-maverick-17b-128e-instruct`

---

## Future Improvements

- PDF summarization
- Multi-language support
- Download summary as PDF
- Chat with summarized content
- Transcript display feature

---

## Screenshots

![Streamlit UI](image.png)

---
