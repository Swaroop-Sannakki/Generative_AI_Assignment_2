import os                       # Used to access environment variables
from dotenv import load_dotenv # Load variables from .env file

# Groq API
from groq import Groq

# Gemini API
from google import genai

# Cohere API
import cohere

# Ollama (local API using HTTP)
import requests

# HuggingFace (local model)
from transformers import pipeline

# Load API keys from .env file
load_dotenv()

# Initialize API clients using keys
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
gemini_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
cohere_client = cohere.Client(os.getenv("COHERE_API_KEY"))

# Load HuggingFace model (runs locally)
hf_generator = pipeline("text-generation", model="distilgpt2")


# Function to get response from Groq
def query_groq(prompt):
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Groq model
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


# Function to get response from Gemini
def query_gemini(prompt):
    try:
        response = gemini_client.models.generate_content(
            model="models/gemini-flash-latest",  # Gemini model
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


# Function to get response from Cohere
def query_cohere(prompt):
    try:
        response = cohere_client.chat(
            model="command-r-08-2024",  # Cohere model
            message=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


# Function to get response from Ollama (local model)
def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",  # Local Ollama API
            json={
                "model": "phi",     # Lightweight local model
                "prompt": prompt,   # User input
                "stream": False     # Get full response at once
            }
        )
        return response.json().get("response", "No response")
    except Exception as e:
        return f"Error: {e}"


# Function to get response from HuggingFace (local model)
def query_huggingface(prompt):
    try:
        result = hf_generator(prompt, max_length=100, num_return_sequences=1)
        return result[0]["generated_text"]
    except Exception as e:
        return f"Error: {e}"


# Main program starts here
if __name__ == "__main__":

    # Show menu to user
    print("Select AI Provider:")
    print("1. Groq")
    print("2. Gemini")
    print("3. Cohere")
    print("4. Ollama")
    print("5. HuggingFace")

    # Take user choice and prompt
    choice = input("Enter choice (1-5): ")
    prompt = input("Enter your prompt: ")

    # Call respective API based on user choice
    if choice == "1":
        print("\nGroq Response:\n")
        print(query_groq(prompt))

    elif choice == "2":
        print("\nGemini Response:\n")
        print(query_gemini(prompt))

    elif choice == "3":
        print("\nCohere Response:\n")
        print(query_cohere(prompt))

    elif choice == "4":
        print("\nOllama Response:\n")
        print(query_ollama(prompt))

    elif choice == "5":
        print("\nHuggingFace Response:\n")
        print(query_huggingface(prompt))

    else:
        print("Invalid choice")