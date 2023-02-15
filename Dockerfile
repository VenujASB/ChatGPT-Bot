# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variables
ENV API_ID=18862638
ENV API_HASH=2a4a8dc0c1f6c9cb65f9f144439558ae
ENV BOT_TOKEN=6172113599:AAGZm96NR0vgzyWy9IFgrHiN6VSfyGXukaI
ENV OPENAI_API_KEY=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

# Start the application
CMD ["python", "bot.py"]
