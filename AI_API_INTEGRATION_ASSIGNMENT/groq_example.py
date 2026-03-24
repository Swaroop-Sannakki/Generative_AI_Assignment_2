from groq import Groq          # Import Groq library to use its API
import os                     # Used to access environment variables
from dotenv import load_dotenv  # Loads variables from .env file

load_dotenv()  # Load API keys from .env file

# Create Groq client using API key from .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function to send prompt to Groq and get response
def query_groq(prompt):
    try:
        # Send user prompt to Groq model
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # AI model used
            messages=[{"role": "user", "content": prompt}]  # User input
        )

        # Return the generated response text
        return response.choices[0].message.content

    except Exception as e:
        # If any error occurs, return error message
        return f"Error: {str(e)}"


# Main program starts here
if __name__ == "__main__":

    # Take input from user
    user_prompt = input("Enter your prompt: ")
    # Show message before calling API
    print("Querying Groq API...")
    # Call function and store result
    result = query_groq(user_prompt)
    # Print the AI response
    print("\nResponse:\n")
    print(result)