# convo.py

from llama_index.core.tools import FunctionTool
import os
from datetime import datetime

conversation_file = os.path.join("data", "conversation.txt")

# Function to save conversation to the file with timestamp
def save_conversation(prompt, response):
    if not os.path.exists(conversation_file):
        open(conversation_file, "w").close()  # Create file if not exists

    # Get current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(conversation_file, "a") as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Response: {response}\n")
        f.write("=" * 40 + "\n")  # Separator for readability

    return "conversation saved"

# Create FunctionTool for conversation saving
conversation_tool = FunctionTool.from_defaults(
    fn=save_conversation,
    name="conversation_saver",
    description="This tool can save the conversation (prompt and response) with timestamp to a file for the user.",
)
