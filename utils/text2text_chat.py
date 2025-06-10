#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: text2text_chat.py
@time: 2025/6/10 15:53
@project: llm-cookbook
@desc: 基于硅基流动的文本生成模型加载
"""

import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

loaded = load_dotenv(find_dotenv(), override=True)
# 从环境变量中获取 OpenAI API Key 或者直接赋值
API_KEY = os.getenv("API_KEY")

# 如果您使用的是官方 API，就直接用 https://api.siliconflow.cn/v1 就行。
BASE_URL = "https://api.siliconflow.cn/v1"

# 基于openai的OpenAI实例
openai_client = OpenAI(api_key=API_KEY, base_url=BASE_URL, max_retries=3)


def get_completions(llm_prompt, model_endpoint="Qwen/Qwen3-8B"):
    extra_body = {}
    if "Qwen3" in model_endpoint:
        extra_body = {
            "enable_thinking": False
        }

    response = openai_client.chat.completions.create(model=model_endpoint,
                                                     messages=[
                                                         {"role": "user",
                                                          "content": llm_prompt
                                                          }
                                                     ],
                                                     n=1, temperature=0, seed=42,
                                                     presence_penalty=0, frequency_penalty=0,
                                                     max_tokens=4096, extra_body=extra_body
                                                     )

    return response.choices[0].message.content.strip()
