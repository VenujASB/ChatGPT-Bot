import openai
import os

# Load API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define function for generating text using OpenAI API
def generate_text(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()
