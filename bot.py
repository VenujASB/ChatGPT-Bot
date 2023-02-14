
import openai
import pyrogram
import os

# Set up OpenAI API credentials
openai.api_key = os.environ.get('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')

# Set up Pyrogram client
app = pyrogram.Client(
    "my_bot",
    api_id=os.environ.get('18862638'),
    api_hash=os.environ.get('2a4a8dc0c1f6c9cb65f9f144439558ae'),
    bot_token=os.environ.get('6172113599:AAGZm96NR0vgzyWy9IFgrHiN6VSfyGXukaI')
)

# Define a function to send messages
def send_message(chat_id, text):
    app.send_message(chat_id, text)

# Define a function to handle the /start command
@app.on_message(pyrogram.filters.command("start"))
def start_command(client, message):
    # Send a welcome message with buttons
    buttons = [
        [
            pyrogram.InlineKeyboardButton(
                "Developer", url="https://example.com/developer"
            ),
            pyrogram.InlineKeyboardButton(
                "GitHub", url="https://github.com/example"
            )
        ]
    ]
    message_text = "Hi, I'm Chat Bot!\n\nHow can I help you today?"
    client.send_message(
        chat_id=message.chat.id,
        text=message_text,
        reply_markup=pyrogram.InlineKeyboardMarkup(buttons)
    )

# Define a function to process incoming messages
@app.on_message(pyrogram.filters.text)
def handle_message(client, message):
    # Get the message text
    message_text = message.text.lower()

    # Check if the message is a greeting
    if "hello" in message_text or "hi" in message_text:
        send_message(message.chat.id, "Hello! How can I help you today?")
    else:
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
