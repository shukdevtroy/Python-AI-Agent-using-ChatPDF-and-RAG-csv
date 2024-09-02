import openai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in the .env file.")

# Initialize the OpenAI client with the API key
openai.api_key = api_key

# Use the OpenAI client to make a request
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a sentence in English, and your task is to translate it into French."
    },
    {
      "role": "user",
      "content": "My name is Jane. What is yours?"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)

# Print the response
print(response.choices[0].message['content'])
