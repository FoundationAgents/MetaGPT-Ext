# MetaGPT Provider for Azure OpenAI

This package provides the Azure OpenAI LLM provider for MetaGPT.

## Installation

```bash
pip install metagpt-provider-azure-openai
```

## Configuration

To use the Azure OpenAI provider, you need to configure it in your `config2.yaml` file:

```yaml
llm:
  api_type: "azure"
  base_url: "https://YOUR_RESOURCE_NAME.openai.azure.com"
  api_key: "YOUR_API_KEY"
  api_version: "2023-07-01-preview" # Or your specific API version
  model: "gpt-4"
  pricing_plan: "" # Optional. Used when model name is not the same as OpenAI's standard names
```

## Usage

```python
from metagpt.core.configs.llm_config import LLMConfig
from metagpt.provider.azure_openai import AzureOpenAILLM

# Configure the LLM
config = LLMConfig(
    api_type="azure",
    base_url="https://YOUR_RESOURCE_NAME.openai.azure.com",
    api_key="YOUR_API_KEY",
    api_version="2023-07-01-preview",
    model="gpt-4"
)

# Create the LLM instance
llm = AzureOpenAILLM(config)

# Use the LLM
response = await llm.aask("Hello, how are you?")
```

## Supported Models

Azure OpenAI supports most OpenAI models, including:
- GPT-4 series (gpt-4, gpt-4-turbo, gpt-4o, etc.)
- GPT-3.5 series (gpt-35-turbo, gpt-3.5-turbo, etc.)

Check the [Azure OpenAI Service Models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models) documentation for the most up-to-date information about available models.