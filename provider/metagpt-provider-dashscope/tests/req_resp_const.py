#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : constants for test

from typing import AsyncGenerator, Union

from dashscope.api_entities.dashscope_response import (
    DashScopeAPIResponse,
    GenerationOutput,
    GenerationResponse,
    GenerationUsage,
)

# Test constants
name = "qwen-max"
resp_cont_tmpl = "I'm {name}"
resp_cont = resp_cont_tmpl.format(name=name)
prompt = "who are you?"
messages = [{"role": "user", "content": prompt}]


def get_dashscope_response(name: str) -> GenerationResponse:
    """Create a mock dashscope response"""
    return GenerationResponse.from_api_response(
        DashScopeAPIResponse(
            status_code=200,
            output=GenerationOutput(
                **{
                    "text": "",
                    "finish_reason": "",
                    "choices": [
                        {
                            "finish_reason": "stop",
                            "message": {"role": "assistant", "content": resp_cont_tmpl.format(name=name)},
                        }
                    ],
                }
            ),
            usage=GenerationUsage(**{"input_tokens": 12, "output_tokens": 98, "total_tokens": 110}),
        )
    )


@classmethod
def mock_dashscope_call(
    cls,
    messages: list[dict],
    model: str,
    api_key: str,
    result_format: str,
    temperature: float = None,
    incremental_output: bool = True,
    stream: bool = False,
    **kwargs,
) -> GenerationResponse:
    """Mock the dashscope API call with specific parameters that match the actual API"""
    return get_dashscope_response(name)


@classmethod
async def mock_dashscope_acall(
    cls,
    messages: list[dict],
    model: str,
    api_key: str,
    result_format: str,
    temperature: float = None,
    incremental_output: bool = True,
    stream: bool = False,
    **kwargs,
) -> Union[AsyncGenerator[GenerationResponse, None], GenerationResponse]:
    """Mock the async dashscope API call with specific parameters that match the actual API"""
    resps = [get_dashscope_response(name)]
    if stream:

        async def aresp_iterator(resps: list[GenerationResponse]):
            for resp in resps:
                yield resp

        return aresp_iterator(resps)
    else:
        return resps[0]


async def llm_general_chat_funcs_test(llm, prompt, messages, resp_cont):
    """Test general chat functions for LLM providers"""
    # Test aask
    resp = await llm.aask(prompt, stream=False)
    assert resp == resp_cont

    resp = await llm.aask(prompt)
    assert resp == resp_cont

    # Test acompletion_text
    resp = await llm.acompletion_text(messages, stream=False)
    assert resp == resp_cont

    resp = await llm.acompletion_text(messages, stream=True)
    assert resp == resp_cont
