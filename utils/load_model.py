#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: load_model.py
@time: 2025/6/4 17:50
@project: llm-cookbook
@desc: 
"""

import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

loaded = load_dotenv(find_dotenv(), override=True)
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
client = OpenAI(api_key=api_key, base_url=base_url)


def get_completion(prompt, model="Qwen/Qwen2-7B-Instruct"):
    """
    prompt: 对应的提示词
    model: 调用的模型，默认为Qwen/Qwen2-7B-Instruct
    """
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        seed=0,
    )
    #  0penAI 的 ChatCompletion 接口
    return response.choices[0].message.content
