# AI API Integration Assignment

## Assignment Description
This assignment demonstrates integration of multiple AI APIs using Python.
It allows users to input prompts and receive responses from different AI providers.

The project includes:
* Multiple AI API integrations
* Command-line interface (CLI)
* Streamlit-based web UI
* Local and cloud AI models

# APIs Used
1.Groq
2.HuggingFace (local using transformers)
3.Google Gemini
4.Cohere
5.Ollama (local model)

## Setup Instructions

### 1. Create Virtual Environment
python -m venv env

### 2. Activate Environment
env\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt


## How to Obtain API Keys

### 1. Groq
* Visit: https://console.groq.com
* Sign up / login
* Go to API Keys → Create new key

### 2. HuggingFace
* Visit: https://huggingface.co
* Go to Settings → Access Tokens
* Create new token (Read permission)

### 3. Google Gemini
* Visit: https://makersuite.google.com/app/apikey
* Click "Create API Key"

### 4. Cohere
* Visit: https://dashboard.cohere.com
* Create API key from dashboard

### 5. Ollama (Local)
* Download from: https://ollama.ai
* Install and run:
  ollama pull phi

## Environment Variables
Create a `.env` file and add:
GROQ_API_KEY=your_key (just for example)
HUGGINGFACE_API_KEY=your_key
GOOGLE_API_KEY=your_key
COHERE_API_KEY=your_key
OPENAI_API_KEY=your_key

## To Run Programs
### Run Individual APIs

python groq_example.py
python huggingface_example.py
python gemini_example.py
python cohere_example.py
python ollama_example.py
python openai_example.py
python multi_api_query.py
streamlit run app.py

## Bonus Features

* Multi-API selection system
* Streamlit user interface
* Local AI models using Ollama & HuggingFace
* Error handling for API failures


## Screenshots of Working Programs
Screenshots are available in the `screenshots/` folder:
* groq_output.png
* huggingface_output.png
* gemini_output.png
* cohere_output.png
* ollama_output.png


* `.env` file is not uploaded for security reasons
* Ollama runs locally without internet

This assignment demonstrates how to integrate multiple AI APIs into a single Python-based system with both CLI and UI interfaces.
