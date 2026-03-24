import streamlit as st          # Create web UI
import os                       # Access environment variables
from dotenv import load_dotenv  # Load .env file

# Import APIs
from groq import Groq
from google import genai
import cohere
import requests
from transformers import pipeline

# Load API keys from .env
load_dotenv()

# Initialize API clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
gemini_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

# HuggingFace model (compatible with your version)
hf_generator = pipeline("text-generation", model="distilgpt2")

# Set page title
st.set_page_config(page_title="AI Multi API App", layout="centered")

# Title
st.title("🤖 AI Multi-API App")
st.write("Choose an AI provider and get responses")

# Dropdown
api_choice = st.selectbox(
    "Select AI Provider",
    ["Groq", "Gemini", "Cohere", "Ollama", "HuggingFace"]
)

# Input
prompt = st.text_area("Enter your prompt")


#API FUNCTIONS 

# Groq
def query_groq(prompt):
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# Gemini
def query_gemini(prompt):
    response = gemini_client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )
    return response.text


# Cohere
def query_cohere(prompt):
    response = cohere_client.chat(
        model="command-r-08-2024",
        message=prompt
    )
    return response.text


# Ollama
def query_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json().get("response", "No response")


# HuggingFace (fixed for compatibility)
def query_huggingface(prompt):
    try:
        # Add instruction to improve output
        better_prompt = f"Explain simply: {prompt}"

        result = hf_generator(better_prompt, max_length=150, num_return_sequences=1)

        return result[0]["generated_text"]

    except Exception as e:
        return f"Error: {e}"

if st.button("Generate Response"):

    if not prompt:
        st.warning("Please enter a prompt")

    else:
        st.info(f"Using {api_choice}...")

        try:
            if api_choice == "Groq":
                output = query_groq(prompt)

            elif api_choice == "Gemini":
                output = query_gemini(prompt)

            elif api_choice == "Cohere":
                output = query_cohere(prompt)

            elif api_choice == "Ollama":
                output = query_ollama(prompt)

            elif api_choice == "HuggingFace":
                output = query_huggingface(prompt)

            st.success("Response:")
            st.write(output)

        except Exception as e:
            st.error(f"Error: {e}")