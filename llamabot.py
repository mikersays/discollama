import discord
import requests
import asyncio

# Your Discord bot token
DISCORD_TOKEN = 'your_discord_bot_token'  # Replace with your actual bot token

# Create a Discord client instance
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
client = discord.Client(intents=intents)

# Ollama API endpoint
OLLAMA_API_URL = 'http://localhost:11434/v1/completions'

# The model to use
MODEL_NAME = 'llama3.2'

# The command trigger
COMMAND_TRIGGER = '!l'

# Dictionary to store conversation history per channel
conversation_history = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # Avoid responding to the bot's own messages
    if message.author == client.user:
        return

    # Check if the message starts with the command trigger
    if message.content.startswith(COMMAND_TRIGGER):
        # Remove the trigger from the message content to get the user's prompt
        user_input = message.content[len(COMMAND_TRIGGER):].strip()

        # Get the channel ID to maintain context per channel
        channel_id = message.channel.id

        # Initialize conversation history for the channel if it doesn't exist
        if channel_id not in conversation_history:
            conversation_history[channel_id] = []

        # Append the user's message to the conversation history
        conversation_history[channel_id].append(f"User: {user_input}")

        # Limit the conversation history to the last N exchanges to manage context length
        MAX_HISTORY_LENGTH = 5  # Adjust this value as needed
        history = conversation_history[channel_id][-MAX_HISTORY_LENGTH:]

        # Construct the prompt by joining the conversation history
        prompt = "\n".join(history) + "\nAssistant:"

        # Prepare the payload for the Ollama API
        payload = {
            'model': MODEL_NAME,
            'prompt': prompt,
            'max_tokens': 500,  # Increased from 150 to allow longer responses
            'temperature': 0.7,
            'n': 1,
            'stop': ["User:", "Assistant:"]  # Optional stop tokens
        }

        try:
            # Send a POST request to the Ollama API
            response = requests.post(OLLAMA_API_URL, json=payload)

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                response_data = response.json()
                generated_text = response_data['choices'][0]['text'].strip()

                # Append the assistant's response to the conversation history
                conversation_history[channel_id].append(f"Assistant: {generated_text}")

                # Function to split the message into chunks of 2000 characters
                def split_message(text, max_length=2000):
                    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

                # Send the assistant's response back to the Discord channel
                for chunk in split_message(generated_text):
                    await message.channel.send(chunk)
            else:
                error_message = response.text
                await message.channel.send(f'Error from API: {error_message}')

        except Exception as e:
            # Print the full stack trace for debugging
            import traceback
            traceback.print_exc()
            await message.channel.send(f'Sorry, I encountered an error: {e}')

# Run the bot
client.run(DISCORD_TOKEN)
