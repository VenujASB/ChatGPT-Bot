from pyrogram import Client, filters
from pyrogram.types import Message
import openai
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
def start_handler(_, message: Message):
    message.reply_text(
        "Hello! I am a simple chat bot. You can send me any message, and I will use OpenAI's GPT to generate a response."
    )


# Handle any message sent to the bot
@app.on_message(filters.text)
def message_handler(client, message):
    # Generate a response using ChatGPT
    prompt = message.text.strip()
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text.strip()

    # Send the response back to the user
    message.reply_text(response)


if __name__ == "__main__":
    app.run()

