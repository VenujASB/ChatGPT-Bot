import os
import openai
from pyrogram import Client, filters

# Set up OpenAI API key
openai.api_key = os.getenv("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")

# Create a new Pyrogram client instance
app = Client(
    "my_telegram_bot",
    api_id=os.getenv("API_ID"),
    api_hash=os.getenv("2a4a8dc0c1f6c9cb65f9f144439558ae"),
    bot_token=os.getenv("6172113599:AAGZm96NR0vgzyWy9IFgrHiN6VSfyGXukaI"),
)

# Define a message handler function
@ app.on_message(filters.private)
def handle_message(client, message):
    # Get the user's message
    user_message = message.text.lower()

    # If the user sends "/start", send a welcome message
    if user_message == "/start":
        message.reply_text(
            f"Hi there! I'm a chatbot powered by OpenAI's GPT-3. Just send me a message and I'll respond with something intelligent! 😊"
        )
    else:
        # Generate a response using OpenAI's GPT-3 API
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Send the response back to the user
        message.reply_text(response.choices[0].text)

# Start the Pyrogram client
app.run()
