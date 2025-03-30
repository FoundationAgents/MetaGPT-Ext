#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : the unittest of DashScopeLLM

import pytest
from metagpt.provider.dashscope import DashScopeLLM
from tests.mock_llm_config import mock_llm_config_dashscope
from tests.req_resp_const import (
    llm_general_chat_funcs_test,
    messages,
    mock_dashscope_acall,
    mock_dashscope_call,
    prompt,
    resp_cont,
)


@pytest.mark.asyncio
async def test_dashscope_acompletion(mocker):
    """Test DashScope acompletion method"""
    # Mock the dashscope API calls to match the original implementation
    mocker.patch("dashscope.aigc.generation.Generation.call", mock_dashscope_call)
    mocker.patch("metagpt.provider.dashscope.dashscope_api.AGeneration.acall", mock_dashscope_acall)

    # Create DashScopeLLM instance using the mock config
    dashscope_llm = DashScopeLLM(mock_llm_config_dashscope)

    # Test basic completion methods
    resp = dashscope_llm.completion(messages)
    assert resp.choices[0]["message"]["content"] == resp_cont

    resp = await dashscope_llm.acompletion(messages)
    assert resp.choices[0]["message"]["content"] == resp_cont

    # Test all other methods using the common test function
    await llm_general_chat_funcs_test(dashscope_llm, prompt, messages, resp_cont)
