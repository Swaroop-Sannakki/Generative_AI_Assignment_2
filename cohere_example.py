import cohere            # Import Cohere library to use its API
import os                     # Used to access environment variables
from dotenv import load_dotenv  # Load variables from .env file

load_dotenv()  # Load API key from .env file

# Create Cohere client using API key
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Function to send prompt to Cohere and get response
def query_cohere(prompt):
    try:
        # Send user input to Cohere chat model
        response = co.chat(
            model="command-r-08-2024",  # Model name
            message=prompt              # User prompt
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
    print("Querying Cohere...")
    # Call function and store result
    result = query_cohere(user_prompt)
    # Print the response
    print("\nResponse:\n")
    print(result)