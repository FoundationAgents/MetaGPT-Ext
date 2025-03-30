#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mock LLM configurations for testing purposes.
"""

from metagpt.core.configs.llm_config import LLMConfig

mock_llm_config_bedrock = LLMConfig(
    api_type="bedrock",
    model="xxx",
    region_name="somewhere",
    access_key="123abc",
    secret_key="123abc",
    max_token=10000,
)
