import openai
import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message

load_dotenv()

# Load configuration from environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI GPT model
openai.api_key = OPENAI_API_KEY
model_engine = "davinci"  # Choose the model engine
prompt = "Hi, how can I assist you today?"  # Choose the prompt

# Initialize the Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# Define command handlers
@app.on_message(filters.command("start"))
async def start_command_handler(client: Client, message: Message):
    """Handler for the /start command."""
    await message.reply_text("Hello, I'm a chatbot powered by OpenAI. How can I help you today?")


# Define message handlers
@app.on_message(filters.text)
async def message_handler(client: Client, message: Message):
    """Handler for incoming messages."""
    # Generate response using OpenAI GPT model
    generated_text = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    ).choices[0].text

    # Send the response to the user
    await message.reply_text(generated_text)


# Start the client
print("Bot is Alive!")
app.run()
