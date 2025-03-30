#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Request and response constants for testing purposes.
"""

from metagpt.core.provider.base_llm import BaseLLM

# For Amazon Bedrock
# Check the API documentation of each model
# https://docs.aws.amazon.com/bedrock/latest/userguide
BEDROCK_PROVIDER_REQUEST_BODY = {
    "mistral": {"prompt": "", "max_tokens": 0, "stop": [], "temperature": 0.0, "top_p": 0.0, "top_k": 0},
    "meta": {"prompt": "", "temperature": 0.0, "top_p": 0.0, "max_gen_len": 0},
    "ai21": {
        # Different format for different AI21 models
        "j2": {
            "prompt": "",
            "temperature": 0.0,
            "topP": 0.0,
            "maxTokens": 0,
            "stopSequences": [],
            "countPenalty": {"scale": 0.0},
            "presencePenalty": {"scale": 0.0},
            "frequencyPenalty": {"scale": 0.0},
        },
        "jamba": {
            "messages": [],
            "temperature": 0.0,
            "top_p": 0.0,
            "max_tokens": 0,
        },
    },
    "cohere": {
        # Standard format for Cohere Command models
        "standard": {
            "prompt": "",
            "temperature": 0.0,
            "p": 0.0,
            "k": 0.0,
            "max_tokens": 0,
            "stop_sequences": [],
            "return_likelihoods": "NONE",
            "stream": False,
            "num_generations": 0,
            "logit_bias": {},
            "truncate": "NONE",
        },
        # Format for Command-R models
        "command-r": {"message": "", "chat_history": [], "temperature": 0.0, "max_tokens": 0},
    },
    "anthropic": {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 0,
        "system": "",
        "messages": [{"role": "", "content": ""}],
        "temperature": 0.0,
        "top_p": 0.0,
        "top_k": 0,
        "stop_sequences": [],
    },
    "amazon": {
        "inputText": "",
        "textGenerationConfig": {"temperature": 0.0, "topP": 0.0, "maxTokenCount": 0, "stopSequences": []},
    },
}

# Different response formats for different models
BEDROCK_PROVIDER_RESPONSE_BODY = {
    "mistral": {"outputs": [{"text": "Hello World", "stop_reason": ""}]},
    "meta": {"generation": "Hello World", "prompt_token_count": 0, "generation_token_count": 0, "stop_reason": ""},
    "ai21": {
        # J2 format
        "id": "",
        "prompt": {"text": "Hello World", "tokens": []},
        "completions": [
            {"data": {"text": "Hello World", "tokens": []}, "finishReason": {"reason": "length", "length": 2}}
        ],
        # For Jamba models, add the choices field with correct structure
        "choices": [{"message": {"content": "Hello World", "role": "assistant"}, "finish_reason": "stop", "index": 0}],
    },
    "cohere": {
        "generations": [
            {
                "finish_reason": "",
                "id": "",
                "text": "Hello World",
                "likelihood": 0.0,
                "token_likelihoods": [{"token": 0.0}],
                "is_finished": True,
                "index": 0,
            }
        ],
        "id": "",
        "prompt": "",
    },
    "anthropic": {
        "id": "",
        "model": "",
        "type": "message",
        "role": "assistant",
        "content": [{"type": "text", "text": "Hello World"}],
        "stop_reason": "",
        "stop_sequence": "",
        "usage": {"input_tokens": 0, "output_tokens": 0},
    },
    "amazon": {
        "inputTextTokenCount": 0,
        "results": [{"tokenCount": 0, "outputText": "Hello World", "completionReason": ""}],
    },
}


# Modified function to handle nested structure for different model formats
def get_bedrock_request_body(model_id) -> dict:
    parts = model_id.split(".")
    provider = parts[0]

    # Handle region prefixed model names like us.anthropic.xxx
    if provider == "us" and len(parts) >= 2:
        provider = parts[1]

    if provider == "ai21":
        # Check if this is a Jamba model (vs J2)
        if "jamba" in model_id:
            return BEDROCK_PROVIDER_REQUEST_BODY[provider]["jamba"]
        else:
            return BEDROCK_PROVIDER_REQUEST_BODY[provider]["j2"]
    elif provider == "cohere":
        # Check if this is a Command-R model
        if "command-r" in model_id:
            return BEDROCK_PROVIDER_REQUEST_BODY[provider]["command-r"]
        else:
            return BEDROCK_PROVIDER_REQUEST_BODY[provider]["standard"]

    return BEDROCK_PROVIDER_REQUEST_BODY[provider]


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
