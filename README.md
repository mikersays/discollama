# Discord Bot with Ollama Integration

This is a Discord bot written in Python that integrates with the Ollama API to generate responses based on user prompts. The bot listens for messages starting with a specific command trigger and replies with generated text from the Ollama language model.

## Features

- **Command Trigger:** Responds to messages starting with `!l`.
- **Conversation History:** Maintains context by storing conversation history per channel.
- **Customizable Model:** Uses the specified Ollama language model for generating responses.

## Prerequisites

- Python 3.6 or higher
- Discord account and a Discord bot token
- Ollama API running locally
- Required Python libraries:
  - `discord.py`
  - `requests`

## Installation

### 1. Clone the Repository or Download the Script

Clone this repository or download the `llamabot.py` script to your local machine.

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Follow these steps to create and activate a virtual environment named `llamavenv`:

**On Windows:**

```bash
python -m venv llamavenv
llamavenv\Scripts\activate
```

**On macOS and Linux:**

```bash
python3 -m venv llamavenv
source llamavenv/bin/activate
```

### 3. Install Required Python Packages

With the virtual environment activated, install the necessary Python packages using `pip`:

```bash
pip install discord.py requests
```

### 4. Set Up the Discord Bot

- Go to the [Discord Developer Portal](https://discord.com/developers/applications).
- Create a new application and add a bot to it.
- Enable the **Message Content Intent** under the bot's settings.
- Copy the bot's token.

### 5. Configure the Script

- Open `llamabot.py` in a text editor.
- Replace `'your_discord_bot_token'` with your actual Discord bot token:

  ```python
  DISCORD_TOKEN = 'your_discord_bot_token'
  ```

- Ensure the Ollama API URL is correct:

  ```python
  OLLAMA_API_URL = 'http://localhost:11434/v1/completions'
  ```

- Set the desired model name:

  ```python
  MODEL_NAME = 'llama3.2'
  ```

### 6. Run the Ollama API Locally

Follow the Ollama API documentation to run it on your local machine. Ensure it's accessible at the URL specified in `OLLAMA_API_URL`.

## Usage

### Starting the Bot

Run the script using Python:

```bash
python llamabot.py
```

### Interacting with the Bot

In any Discord channel where the bot has access:

- Send a message starting with the command trigger followed by your prompt:

  ```
  !l Hello, how are you?
  ```

- The bot will respond with generated text based on your input.

## Customization

### Changing the Command Trigger

Modify the `COMMAND_TRIGGER` variable in `llamabot.py` to change how you invoke the bot:

```python
COMMAND_TRIGGER = '!l'
```

### Adjusting Conversation History Length

Change the `MAX_HISTORY_LENGTH` to keep more or fewer past messages in context:

```python
MAX_HISTORY_LENGTH = 10  # Adjust as needed
```

### Modifying Model Parameters

Adjust the payload parameters to customize the model's behavior:

```python
payload = {
    'model': MODEL_NAME,
    'prompt': prompt,
    'max_tokens': 150,
    'temperature': 0.7,
    'n': 1,
    'stop': None
}
```

- **max_tokens:** The maximum number of tokens to generate.
- **temperature:** Controls the randomness of the output.
- **n:** Number of responses to generate.
- **stop:** A list of tokens at which to stop generation.

## Troubleshooting

### Bot Not Responding

- Ensure the bot is running without errors.
- Verify that the bot has the necessary permissions in the Discord channel.
- Confirm that the **Message Content Intent** is enabled in the bot settings.

### API Errors

- Check if the Ollama API is running and accessible.
- Ensure the model specified in `MODEL_NAME` exists and is properly configured.
- Review the error message returned from the API for specific details.

### Python Exceptions

- Make sure all required libraries are installed within the virtual environment.
- Check the console for stack traces to identify issues.
- Verify that you're using a compatible version of Python.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
