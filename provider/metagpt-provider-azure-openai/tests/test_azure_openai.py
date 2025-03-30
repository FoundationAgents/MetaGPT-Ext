#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test file for the Azure OpenAI provider.
"""

from typing import AsyncIterator, List, Union

import pytest
from metagpt.core.configs.llm_config import LLMConfig, LLMType
from metagpt.core.provider.base_llm import BaseLLM
from metagpt.provider.azure_openai import AzureOpenAILLM
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice, CompletionUsage
from openai.types.chat.chat_completion_chunk import Choice as ChunkChoice
from openai.types.chat.chat_completion_chunk import ChoiceDelta
from openai.types.chat.chat_completion_message import ChatCompletionMessage

# 测试数据常量
name = "Azure AI assistant"
prompt = "who are you?"
messages = [{"role": "user", "content": prompt}]
resp_cont = f"I'm {name}"
USAGE = {"completion_tokens": 1000, "prompt_tokens": 1000, "total_tokens": 2000}


def create_mock_config():
    """Create a mock LLM config for testing"""
    return LLMConfig(
        api_type=LLMType.AZURE,
        base_url="https://test-endpoint.openai.azure.com",
        api_key="test_api_key",
        api_version="2023-07-01-preview",
        model="gpt-4",
    )


def get_azure_chat_completion() -> ChatCompletion:
    """Get mock Azure OpenAI chat completion response"""
    return ChatCompletion(
        id="chatcmpl-123",
        choices=[
            Choice(
                finish_reason="stop",
                index=0,
                message=ChatCompletionMessage(content=resp_cont, role="assistant", function_call=None, tool_calls=None),
                logprobs=None,
            )
        ],
        created=1716278586,
        model="gpt-4",
        object="chat.completion",
        system_fingerprint=None,
        usage=CompletionUsage(**USAGE),
    )


def create_chat_completion_chunk(
    content: str, finish_reason: str = None, choices: List[ChunkChoice] = None
) -> ChatCompletionChunk:
    """Create a mock chat completion chunk"""
    if choices is None:
        choices = [
            ChunkChoice(
                delta=ChoiceDelta(content=content, function_call=None, role="assistant", tool_calls=None),
                finish_reason=finish_reason,
                index=0,
                logprobs=None,
            )
        ]
    return ChatCompletionChunk(
        id="012",
        choices=choices,
        created=1716278586,
        model="gpt-4",
        object="chat.completion.chunk",
        system_fingerprint=None,
        usage=None if choices else CompletionUsage(**USAGE),
    )


async def chunk_iterator(chunks: List[ChatCompletionChunk]) -> AsyncIterator[ChatCompletionChunk]:
    """Create an async iterator from a list of chunks"""
    for chunk in chunks:
        yield chunk


def test_azure_llm_init():
    """Test initialization of AzureOpenAILLM"""
    config = create_mock_config()
    llm = AzureOpenAILLM(config)
    assert llm.config.api_type == LLMType.AZURE
    assert llm.config.base_url == "https://test-endpoint.openai.azure.com"
    assert llm.config.api_key == "test_api_key"
    assert llm.config.api_version == "2023-07-01-preview"
    assert llm.config.model == "gpt-4"


def test_make_client_kwargs():
    """Test creation of client kwargs"""
    config = create_mock_config()
    llm = AzureOpenAILLM(config)
    kwargs = llm._make_client_kwargs()
    assert kwargs["api_key"] == "test_api_key"
    assert kwargs["api_version"] == "2023-07-01-preview"
    assert kwargs["azure_endpoint"] == "https://test-endpoint.openai.azure.com"


async def llm_general_chat_funcs_test(llm: BaseLLM, prompt: str, messages: list[dict], resp_cont: str):
    """Test common LLM interaction methods"""
    # 测试 aask 非流式
    resp = await llm.aask(prompt, stream=False)
    assert resp == resp_cont

    # 测试 aask 流式（默认）
    resp = await llm.aask(prompt)
    assert resp == resp_cont

    # 测试 acompletion_text 非流式
    resp = await llm.acompletion_text(messages, stream=False)
    assert resp == resp_cont

    # 测试 acompletion_text 流式
    resp = await llm.acompletion_text(messages, stream=True)
    assert resp == resp_cont


async def mock_azure_chat_completions_create(
    self, stream: bool = False, **kwargs
) -> Union[ChatCompletionChunk, ChatCompletion]:
    """Mock Azure OpenAI completions create method"""
    if stream:
        # 创建流式响应块
        azure_resp_chunk = create_chat_completion_chunk(content="")
        azure_resp_chunk_finish = create_chat_completion_chunk(content=resp_cont, finish_reason="stop")
        azure_resp_chunk_last = create_chat_completion_chunk(content="", choices=[])
        chunks = [azure_resp_chunk, azure_resp_chunk_finish, azure_resp_chunk_last]
        return chunk_iterator(chunks)
    else:
        # 创建非流式响应
        return get_azure_chat_completion()


@pytest.mark.asyncio
async def test_azure_acompletion(mocker):
    """Test Azure OpenAI non-streaming completion"""
    # 模拟 Azure OpenAI 客户端的 chat.completions.create 方法
    mocker.patch("openai.resources.chat.completions.AsyncCompletions.create", mock_azure_chat_completions_create)

    # 使用模拟配置初始化 Azure OpenAI LLM
    llm = AzureOpenAILLM(create_mock_config())

    # 测试 acompletion（底层 API）
    resp = await llm.acompletion(messages)
    assert resp.choices[0].finish_reason == "stop"
    assert resp.choices[0].message.content == resp_cont
    assert resp.usage.completion_tokens == USAGE["completion_tokens"]
    assert resp.usage.prompt_tokens == USAGE["prompt_tokens"]
    assert resp.usage.total_tokens == USAGE["total_tokens"]

    # 测试所有通用聊天功能
    await llm_general_chat_funcs_test(llm, prompt, messages, resp_cont)
