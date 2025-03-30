# MetaGPT Provider Bedrock

AWS Bedrock provider for MetaGPT.

This package provides support for various models on AWS Bedrock service, including:

- Anthropic (Claude)
- Mistral
- Meta (Llama)
- AI21
- Cohere
- Amazon's own models

## Installation

```bash
pip install metagpt-provider-bedrock
```

## Requirements

- metagpt-core>=1.0.0
- boto3

## Configuration

You will need AWS credentials to use this provider. You can set these up either:

1. As environment variables:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`
   - `AWS_SESSION_TOKEN` (optional)

2. Or in your config file:

```yaml
llm:
  api_type: "bedrock"
  model: "anthropic.claude-3-sonnet-20240229-v1:0"  # Choose an appropriate model ID
  access_key: "your-access-key"
  secret_key: "your-secret-key"
  region_name: "us-east-1"  # Choose your preferred AWS region
  session_token: ""  # Optional
```

## Usage

```python
from metagpt.provider.bedrock import BedrockLLM
from metagpt.core.configs.llm_config import LLMConfig, LLMType

# Configure the provider
config = LLMConfig(
    api_type=LLMType.BEDROCK,
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    access_key="your-access-key",
    secret_key="your-secret-key",
    region_name="us-east-1",
)

# Initialize the provider
llm = BedrockLLM(config)

# Use the provider
response = await llm.aask("What is AWS Bedrock?")
print(response)
```