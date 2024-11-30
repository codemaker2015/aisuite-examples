import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

import aisuite as ai

def ask(message, sys_message="You are a helpful assistant", model="openai:gpt-4o"):
    client = ai.Client()
    messages = [
        {"role": "system", "content": sys_message},
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

print(ask("Who is your creator?"))
print(ask('Who is your creator?', model='ollama:qwen2:1.5b'))
print(ask('Who is your creator?', model='groq:llama-3.1-8b-instant'))
print(ask('Who is your creator?', model='anthropic:claude-3-5-sonnet-20241022'))