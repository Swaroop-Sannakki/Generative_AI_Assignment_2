import requests   # Used to send HTTP requests to Ollama API

# Function to send prompt to Ollama and get response
def query_ollama(prompt):
    try:
        # Send POST request to local Ollama server
        response = requests.post(
            "http://localhost:11434/api/generate",  # Local Ollama API URL
            json={
                "model": "phi",     # Model name (lightweight model)
                "prompt": prompt,   # User input
                "stream": False     # Get full response at once
            }
        )
        # Convert response into JSON format
        data = response.json()
        # Print raw response (for debugging purpose)
        print("Raw response:", data)
        # Extract response safely from different possible keys
        if "response" in data:
            return data["response"]
        elif "message" in data:
            return data["message"]
        elif "output" in data:
            return data["output"]
        else:
            return str(data)  # Return full data if no known key found

    except Exception as e:
        # Handle errors and return message
        return f"Error: {str(e)}"


# Main program starts here
if __name__ == "__main__":

    # Take input from user
    user_prompt = input("Enter your prompt: ")
    # Show message before calling Ollama
    print("Querying Ollama...")
    # Call function and store result
    result = query_ollama(user_prompt)
    # Print final response
    print("\nResponse:\n")
    print(result)