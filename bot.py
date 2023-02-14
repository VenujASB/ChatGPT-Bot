import os
import logging
import pyrogram
import openai

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Load environment variables
TELEGRAM_API_ID = os.environ[18862638]
TELEGRAM_API_HASH = os.environ['2a4a8dc0c1f6c9cb65f9f144439558ae']
TELEGRAM_BOT_TOKEN = os.environ['6172113599:AAGZm96NR0vgzyWy9IFgrHiN6VSfyGXukaI']
OPENAI_API_KEY = os.environ['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']

# Set up Pyrogram and OpenAI API clients
app = pyrogram.Client('chatbot', api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH, bot_token=TELEGRAM_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# Define welcome message and buttons
WELCOME_MESSAGE = 'Welcome to my chatbot!'
DEVELOPER_BUTTON = pyrogram.InlineKeyboardButton('Developer', url='https://www.example.com/developer')
GITHUB_BUTTON = pyrogram.InlineKeyboardButton('GitHub', url='https://github.com/example')

# Define command handlers
@app.on_message(pyrogram.filters.command(['start']))
def start_command_handler(client, message):
    # Send welcome message and buttons
    buttons = [DEVELOPER_BUTTON, GITHUB_BUTTON]
    client.send_message(chat_id=message.chat.id, text=WELCOME_MESSAGE, reply_markup=pyrogram.InlineKeyboardMarkup([buttons]))

@app.on_message(pyrogram.filters.text)
def text_message_handler(client, message):
    # Generate response using OpenAI
    prompt = message.text
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    text = response.choices[0].text.strip()
    
    # Send response message
    client.send_message(chat_id=message.chat.id, text=text)

# Run the bot
app.run()
