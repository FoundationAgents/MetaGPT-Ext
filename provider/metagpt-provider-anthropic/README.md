# MetaGPT Provider Anthropic

This package provides Anthropic (Claude) integration for MetaGPT.

## Installation

```bash
pip install metagpt-provider-anthropic
```

## Usage

```python
from metagpt.provider.anthropic import AnthropicLLM
from metagpt.configs.llm_config import LLMConfig

config = LLMConfig(
    api_type="anthropic",
    api_key="your-api-key",
    model="claude-3-opus-20240229"
)

# Initialize the Anthropic LLM
llm = AnthropicLLM(config)

# Ask a question
response = await llm.aask("What is artificial intelligence?")
print(response)
```

## Configuration

The following configuration parameters are supported:

- `api_type`: Must be set to "anthropic" to use this provider
- `api_key`: Your Anthropic API key
- `model`: The Claude model to use (default: "claude-3-opus-20240229")
- `base_url`: Optional base URL for the Anthropic API