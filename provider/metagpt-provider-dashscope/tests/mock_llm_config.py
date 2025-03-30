#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : mock LLM configs

from metagpt.core.provider.base_llm import LLMConfig

mock_llm_config_dashscope = LLMConfig(
    model="qwen-max",
    api_key="fake-api-key",
    temperature=0.7,
)
