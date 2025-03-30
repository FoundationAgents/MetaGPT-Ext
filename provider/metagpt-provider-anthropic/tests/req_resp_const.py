#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Default request & response data for provider unittest
"""

from anthropic.types import (
    ContentBlockDeltaEvent,
    Message,
    MessageStartEvent,
    TextBlock,
    TextDelta,
)
from anthropic.types import Usage as AnthropicUsage
from metagpt.core.provider.base_llm import BaseLLM

# Common test data
prompt = "who are you?"
messages = [{"role": "user", "content": prompt}]
resp_cont_tmpl = "I'm {name}"
default_resp_cont = resp_cont_tmpl.format(name="GPT")


# For Anthropic
def get_anthropic_response(name: str, stream: bool = False) -> Message:
    if stream:
        return [
            MessageStartEvent(
                message=Message(
                    id="xxx",
                    model=name,
                    role="assistant",
                    type="message",
                    content=[TextBlock(text="", type="text")],
                    usage=AnthropicUsage(input_tokens=10, output_tokens=10),
                ),
                type="message_start",
            ),
            ContentBlockDeltaEvent(
                index=0,
                delta=TextDelta(text=resp_cont_tmpl.format(name=name), type="text_delta"),
                type="content_block_delta",
            ),
        ]
    else:
        return Message(
            id="xxx",
            model=name,
            role="assistant",
            type="message",
            content=[TextBlock(text=resp_cont_tmpl.format(name=name), type="text")],
            usage=AnthropicUsage(input_tokens=10, output_tokens=10),
        )


# For llm general chat functions call
async def llm_general_chat_funcs_test(llm: BaseLLM, prompt: str, messages: list[dict], resp_cont: str):
    resp = await llm.aask(prompt, stream=False)
    assert resp == resp_cont

    resp = await llm.aask(prompt)
    assert resp == resp_cont

    resp = await llm.acompletion_text(messages, stream=False)
    assert resp == resp_cont

    resp = await llm.acompletion_text(messages, stream=True)
    assert resp == resp_cont
