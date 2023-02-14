import os
import openai
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Enter your OpenAI API key here
openai.api_key = "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"

# Get your Telegram bot token from environment variables
bot_token = os.environ.get("6172113599:AAGZm96NR0vgzyWy9IFgrHiN6VSfyGXukaI")

# Get your Pyrogram API ID and API hash from environment variables
api_id = 18862638
api_hash = os.environ.get("2a4a8dc0c1f6c9cb65f9f144439558ae")

# Create a new Pyrogram client
app = Client(
    "my_bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
)

# Handle the /start command
@app.on_message(filters.command("start"))
def start_command_handler(client, message):
    # Send a welcome message with buttons
    keyboard = [
        [InlineKeyboardButton("Button 1", callback_data="button1")],
        [InlineKeyboardButton("Button 2", callback_data="button2")],
        [InlineKeyboardButton("Button 3", callback_data="button3")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text("Welcome to my bot!", reply_markup=reply_markup)

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
        temperature=0.7,
    ).choices[0].text.strip()

    # Send the response back to the user
    message.reply_text(response)

# Start the bot
app.run()
