# AISuite Examples

Simple, unified interface to multiple Generative AI providers.

`aisuite` makes it easy for developers to use multiple LLM through a standardized interface. Using an interface similar to OpenAI's, `aisuite` makes it easy to interact with the most popular LLMs and compare the results. It is a thin wrapper around python client libraries, and allows creators to seamlessly swap out and test responses from different LLM providers without changing their code. Today, the library is primarily focussed on chat completions. We will expand it cover more use cases in near future.

Currently supported providers are -
OpenAI, Anthropic, Azure, Google, AWS, Groq, Mistral, HuggingFace and Ollama.
To maximize stability, `aisuite` uses either the HTTP endpoint or the SDK for making calls to the provider.

## Installation

You can install just the base `aisuite` package, or install a provider's package along with `aisuite`.

This installs just the base package without installing any provider's SDK.

```shell
pip install aisuite
```

This installs aisuite along with anthropic's library.
```shell
pip install 'aisuite[anthropic]'
```

This installs all the provider-specific libraries
```shell
pip install 'aisuite[all]'
```

## Set up

To get started, you will need API Keys for the providers you intend to use. You'll need to
install the provider-specific library either separately or when installing aisuite.

The API Keys can be set as environment variables, or can be passed as config to the aisuite Client constructor.
You can use tools like [`python-dotenv`](https://pypi.org/project/python-dotenv/) or [`direnv`](https://direnv.net/) to set the environment variables manually. Please take a look at the `examples` folder to see usage.

Here is a short example of using `aisuite` to generate chat completion responses from gpt-4o and claude-3-5-sonnet.

Set the API keys.
```shell
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

Use the python client.
```python
import aisuite as ai
client = ai.Client()

models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]

messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)

```