# Google Gemini Provider for MetaGPT

This package provides Google Gemini integration for MetaGPT.

## Installation

```bash
pip install metagpt-provider-google-gemini
```

## Usage

### Basic Usage

```python
from metagpt.core.configs.llm_config import LLMConfig
from metagpt.provider.google_gemini import GeminiLLM

config = LLMConfig(
    api_type="gemini",
    api_key="your_gemini_api_key",
    model="gemini-1.5-flash-002"  # or other available Gemini models, if ignored, will use the default model, currently "gemini-1.5-flash-002"
)

llm = GeminiLLM(config)

# Synchronous API
response = llm.ask("What is artificial intelligence?")
print(response)

# Asynchronous API
async def ask_gemini():
    response = await llm.aask("What is artificial intelligence?")
    print(response)
    
    # Stream response
    async for chunk in llm.aask_stream("Tell me a short story about AI."):
        print(chunk, end="")
```

### Environment Variables

You can also set your Google Gemini API key using environment variables:

```bash
export GEMINI_API_KEY=your_gemini_api_key
```

## Features

- Support for Google Gemini API
- Streaming responses
- Token counting and usage tracking
- Proxy support
- Full integration with MetaGPT framework

## Requirements

- Python 3.9+
- google-generativeai
- metagpt-core