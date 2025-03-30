# MetaGPT DashScope Provider

This package provides DashScope model integration for MetaGPT.

## Installation

```bash
pip install metagpt-provider-dashscope
```

## Usage

```python
from metagpt.provider.dashscope import DashScopeLLM
from metagpt.core.provider.base_llm import LLMConfig

# Configure the DashScope LLM
config = LLMConfig(
    model="qwen-max",  # or other available models: "qwen-plus", "qwen-max", etc.
    api_key="your-dashscope-api-key",
    temperature=0.7,
)

# Create the DashScope LLM instance
llm = DashScopeLLM(config)

# Async usage
async def main():
    response = await llm.aask("Hello, how are you?")
    print(response)
    
    # For chat completion with messages
    messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    response = await llm.acompletion_text(messages)
    print(response)
    
    # For streaming response
    response = await llm.acompletion_text(messages, stream=True)
    print(response)

# Run the async function
import asyncio
asyncio.run(main())
```

## Supported Models

The DashScope provider supports various models including:

- Qwen series: qwen-max, qwen-plus, qwen-turbo, qwen-7b-chat
- LLaMa2 series: llama2-7b-chat, llama2-13b-chat
- Other models: baichuan2-7b-chat-v1, chatglm3-6b

## Features

- Regular text completion
- Streaming responses
- Batch processing
- Cost tracking

## Requirements

- Python >= 3.9
- dashscope
- metagpt-core >= 1.0.0