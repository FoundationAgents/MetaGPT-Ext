#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Default request & response data for provider unittest
"""

from typing import AsyncIterator, List

from metagpt.core.provider.base_llm import BaseLLM
from openai.types.chat import ChatCompletion, ChatCompletionChunk
from openai.types.chat.chat_completion import Choice
from openai.types.chat.chat_completion_chunk import Choice as ChunkChoice
from openai.types.chat.chat_completion_chunk import ChoiceDelta

# Fix import for OpenAI 1.64.0 compatibility
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from openai.types.completion_usage import CompletionUsage

# Common test data
prompt = "who are you?"
messages = [{"role": "user", "content": prompt}]
resp_cont_tmpl = "I'm {name}"
default_resp_cont = resp_cont_tmpl.format(name="GPT")

# Usage data
USAGE = {"completion_tokens": 1000, "prompt_tokens": 1000, "total_tokens": 2000}


# For OpenAI-compatible response
def get_openai_chat_completion(name: str) -> ChatCompletion:
    """Get mock OpenAI chat completion response"""
    return ChatCompletion(
        id="chatcmpl-123",
        choices=[
            Choice(
                finish_reason="stop",
                index=0,
                message=ChatCompletionMessage(
                    content=resp_cont_tmpl.format(name=name), role="assistant", function_call=None, tool_calls=None
                ),
                logprobs=None,
            )
        ],
        created=1716278586,
        model="doubao-pro-32k-240515",
        object="chat.completion",
        system_fingerprint=None,
        usage=CompletionUsage(**USAGE),
    )


# For Ark stream responses
def create_chat_completion_chunk(
    content: str, finish_reason: str = None, choices: List[ChunkChoice] = None
) -> ChatCompletionChunk:
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
        model="doubao-pro-32k-240515",
        object="chat.completion.chunk",
        system_fingerprint=None,
        usage=None if choices else CompletionUsage(**USAGE),
    )


async def chunk_iterator(chunks: List[ChatCompletionChunk]) -> AsyncIterator[ChatCompletionChunk]:
    """Create an async iterator from a list of chunks"""
    for chunk in chunks:
        yield chunk


# For llm general chat functions call
async def llm_general_chat_funcs_test(llm: BaseLLM, prompt: str, messages: list[dict], resp_cont: str):
    """Test common LLM interaction methods"""
    resp = await llm.aask(prompt, stream=False)
    assert resp == resp_cont
    resp = await llm.aask(prompt)
    assert resp == resp_cont
    resp = await llm.acompletion_text(messages, stream=False)
    assert resp == resp_cont
    resp = await llm.acompletion_text(messages, stream=True)
    assert resp == resp_cont
