import openai
import pyrogram

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up Pyrogram client
app = pyrogram.Client(
    "ChatGPTBot",
    api_id=18862638,
    api_hash="2a4a8dc0c1f6c9cb65f9f144439558ae",
    bot_token="6172113599:AAGZm96NR0vgzyWy9IFgrHiN6VSfyGXukaI"
)

# Define a function to send messages
def send_message(chat_id, text):
    app.send_message(chat_id, text)

# Define a function to handle the /start command
@app.on_message(pyrogram.filters.command("start"))
def start_command(client, message):
    # Send a welcome message
    send_message(message.chat.id, "Hi, I'm Chat Bot!")

# Define a function to process incoming messages
@app.on_message()
def handle_message(client, message):
    # Get the message text
    message_text = message.text.lower()

    # Use OpenAI's GPT-3 API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=message_text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Send the generated response back to the user
    send_message(message.chat.id, response.choices[0].text)

# Run the Pyrogram client
app.run()
