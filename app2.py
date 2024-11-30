import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

import aisuite as ai

def ask(message, sys_message="You are a helpful assistant", model="openai:gpt-4o"):
    client = ai.Client()
    messages = [
        {"role": "system", "content": sys_message},
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

print(ask("Provide an overview of the latest trends in AI"))
