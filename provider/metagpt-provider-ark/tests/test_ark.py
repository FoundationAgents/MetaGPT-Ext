#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test for volcengine Ark Python SDK V3
API docs: https://www.volcengine.com/docs/82379/1263482
"""

from typing import Union

import pytest
from metagpt.provider.ark import ArkLLM
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from tests.mock_llm_config import mock_llm_config_ark
from tests.req_resp_const import (
    USAGE,
    chunk_iterator,
    create_chat_completion_chunk,
    get_openai_chat_completion,
    llm_general_chat_funcs_test,
    messages,
    prompt,
    resp_cont_tmpl,
)

# Setup test data
name = "AI assistant"
resp_cont = resp_cont_tmpl.format(name=name)
default_resp = get_openai_chat_completion(name)
default_resp.model = "doubao-pro-32k-240515"
default_resp.usage = USAGE

# Create test chunks for streaming responses
ark_resp_chunk = create_chat_completion_chunk(content="")
ark_resp_chunk_finish = create_chat_completion_chunk(content=resp_cont, finish_reason="stop")
ark_resp_chunk_last = create_chat_completion_chunk(content="", choices=[])


async def mock_ark_chat_completions_create(
    self, stream: bool = False, **kwargs
) -> Union[ChatCompletionChunk, ChatCompletion]:
    """Mock Ark completions create method"""
    if stream:
        chunks = [ark_resp_chunk, ark_resp_chunk_finish, ark_resp_chunk_last]
        return chunk_iterator(chunks)
    else:
        return default_resp


@pytest.mark.asyncio
async def test_ark_acompletion(mocker):
    """Test Ark non-streaming completion"""
    # Mock the Volcengine Ark client's chat.completions.create method
    mocker.patch(
        "volcenginesdkarkruntime.resources.chat.completions.AsyncCompletions.create", mock_ark_chat_completions_create
    )

    # Initialize Ark LLM with mock config
    llm = ArkLLM(mock_llm_config_ark)

    # Test completion
    resp = await llm.acompletion(messages)
    assert resp.choices[0].finish_reason == "stop"
    assert resp.choices[0].message.content == resp_cont
    assert resp.usage == USAGE

    # Test general chat functions
    await llm_general_chat_funcs_test(llm, prompt, messages, resp_cont)
