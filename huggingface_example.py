from transformers import pipeline   # Import pipeline to use HuggingFace models

# Function to generate response using HuggingFace model
def query_huggingface(prompt):
    try:
        # Load text generation model (runs locally)
        generator = pipeline("text-generation", model="distilgpt2")

        # Generate response based on user input
        result = generator(prompt, max_length=100, num_return_sequences=1)

        # Return generated text
        return result[0]["generated_text"]

    except Exception as e:
        # Handle errors and return message
        return f"Error: {str(e)}"


# Main program starts here
if __name__ == "__main__":

    # Take input from user
    user_prompt = input("Enter your prompt: ")
    # Show message before generating response
    print("Querying HuggingFace (local model)...")
    # Call function and store result
    result = query_huggingface(user_prompt)
    # Print the generated response
    print("\nResponse:\n")
    print(result)