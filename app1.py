import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

import aisuite as ai

client = ai.Client()

provider = "openai"
model_id = "gpt-4o"

messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Provide an overview of the latest trends in AI"},
]

response = client.chat.completions.create(
    model = f"{provider}:{model_id}",
    messages = messages,
)

print(response.choices[0].message.content)