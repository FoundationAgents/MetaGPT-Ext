#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Desc   : default request & response data for provider unittest

from metagpt.core.provider.base_llm import BaseLLM

prompt = "who are you?"
messages = [{"role": "user", "content": prompt}]
resp_cont_tmpl = "I'm {name}"
default_resp_cont = resp_cont_tmpl.format(name="GPT")

# For gemini
gemini_messages = [{"role": "user", "parts": prompt}]


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
