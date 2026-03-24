from google import genai          # Import Gemini (Google AI) library
import os                         # Used to access environment variables
from dotenv import load_dotenv   # Load variables from .env file

load_dotenv()  # Load API key from .env file

# Create Gemini client using API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to send prompt to Gemini and get response
def query_gemini(prompt):
    try:
        # Send user input to Gemini model
        response = client.models.generate_content(
            model="models/gemini-flash-latest",  # Model name
            contents=prompt                      # User prompt
        )

        # Return generated response text
        return response.text

    except Exception as e:
        # Handle errors and return message
        return f"Error: {str(e)}"


# Main program starts here
if __name__ == "__main__":

    # Take input from user
    user_prompt = input("Enter your prompt: ")

    # Show message before calling API
    print("Querying Gemini...")

    # Call function and store result
    result = query_gemini(user_prompt)

    # Print the response
    print("\nResponse:\n")
    print(result)