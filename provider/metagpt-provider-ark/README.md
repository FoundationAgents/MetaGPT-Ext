# MetaGPT Provider for Volcengine Ark

This package provides the Volcengine Ark LLM provider for MetaGPT.

## Installation

```bash
pip install metagpt-provider-ark
```

## Configuration

To use the Volcengine Ark provider, you need to configure it in your `config2.yaml` file:

```yaml
llm:
  base_url: "https://ark.cn-beijing.volces.com/api/v3"
  api_type: "ark"
  endpoint: "ep-2024080514xxxx-dxxxx"
  api_key: "d47xxxx-xxxx-xxxx-xxxx-d6exxxx0fd77"
  pricing_plan: "doubao-lite"
```

## Usage

```python
from metagpt.core.configs.llm_config import LLMConfig
from metagpt.provider.ark import ArkLLM

# Configure the LLM
config = LLMConfig(
    api_type="ark",
    api_key="your_api_key",
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    endpoint="your_endpoint"
)

# Create the LLM instance
llm = ArkLLM(config)

# Use the LLM
response = await llm.aask("Hello, how are you?")
print(response)
```

## Documentation

See [Volcengine Ark API Documentation](https://www.volcengine.com/docs/82379/1263482) for more information.