import openai

#  OpenAI API key 
API_KEY = "YOUR_API_KEY"
def generate_story(prompt):
    openai.api_key = API_KEY

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,  # Maximum number of tokens in the response
        temperature=0.7,  # Controls the randomness of the output
        n=1,  # Generate a single response
        stop=None,  # Stop generating when reaching a specific token (optional)
    )

    return response.choices[0].text.strip()

def main():
    print("Welcome to the AI Story Generator!")
    prompt = input("Start the story with a prompt: ")

    story = generate_story(prompt)
    print("\nHere's your story:")
    print(story)

if __name__ == "__main__":
    main()
