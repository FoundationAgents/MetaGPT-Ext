#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mock LLM configuration for testing
"""

from metagpt.core.configs.llm_config import LLMConfig

# Mock config for Ark provider
mock_llm_config_ark = LLMConfig(
    api_type="ark", api_key="eyxxx", base_url="https://ark.cn-beijing.volces.com/api/v3", model="ep-xxx"
)
