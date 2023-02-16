import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API configuration
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
