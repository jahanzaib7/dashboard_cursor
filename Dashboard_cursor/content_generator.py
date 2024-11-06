import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key

def generate_content(keywords):
    # Create a prompt using the provided keywords
    prompt = f"Generate a detailed description about the following crypto keywords: {', '.join(keywords)}."

    try:
        # Call the OpenAI API to generate content
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )

        # Extract and return the generated text
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating content: {e}")
        return "Error generating content. Please try again later."

if __name__ == "__main__":
    # Example usage
    keywords = input("Enter keywords separated by commas: ").split(',')
    keywords = [keyword.strip() for keyword in keywords]
    content = generate_content(keywords)
    print("\nGenerated Content:\n")
    print(content)