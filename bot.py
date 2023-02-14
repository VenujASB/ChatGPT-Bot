import os
import logging
import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Initialize the OpenAI API
openai.api_key = os.getenv("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")

# Initialize the Pyrogram client
app = pyrogram.Client(
    "my_bot",
    api_id=os.getenv(18862638),
    api_hash=os.getenv("2a4a8dc0c1f6c9cb65f9f144439558ae"),
    bot_token=os.getenv("6172113599:AAGZm96NR0vgzyWy9IFgrHiN6VSfyGXukaI")
)

# Define the welcome message and buttons
WELCOME_MESSAGE = "Hello! I'm ChatGPT, a chatbot powered by OpenAI's GPT-3. How can I assist you today?"
DEVELOPER_BUTTON = InlineKeyboardButton("Developer", url="https://example.com/developer")
GITHUB_BUTTON = InlineKeyboardButton("GitHub", url="https://github.com/example")

# Define the /start command handler
@app.on_message(filters.command("start"))
def start(bot, update):
    # Send the welcome message with the buttons
    keyboard = [[DEVELOPER_BUTTON, GITHUB_BUTTON]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=update.chat.id, text=WELCOME_MESSAGE, reply_markup=reply_markup)

# Define the message handler
@app.on_message(filters.text)
def message(bot, update):
    # Generate a response using ChatGPT
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=update.text,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7
        ).choices[0].text.strip()
    except Exception as e:
        response = str(e)

    # Send the response
    bot.send_message(chat_id=update.chat.id, text=response)

# Run the bot
app.run()
