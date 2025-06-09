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

import chromadb.utils.embedding_functions as embedding_functions
from dotenv import load_dotenv, find_dotenv
from langchain_openai.chat_models import ChatOpenAI
from openai import OpenAI

loaded = load_dotenv(find_dotenv(), override=True)
# 从环境变量中获取 OpenAI API Key 或者直接赋值
API_KEY = os.getenv("API_KEY")

# 如果您使用的是官方 API，就直接用 https://api.siliconflow.cn/v1 就行。
BASE_URL = "https://api.siliconflow.cn/v1"

# 基于langchat的OpenAI实例
llm = ChatOpenAI(temperature=0.20, model_name="Qwen/Qwen2.5-Coder-7B-Instruct", max_tokens=4096,
                 openai_api_key=API_KEY, openai_api_base=BASE_URL, max_retries=3,
                 seed=42, presence_penalty=0.1, frequency_penalty=0.1
                 )

# 基于openai的OpenAI实例
openai_client = OpenAI(api_key=API_KEY, base_url=BASE_URL, max_retries=3)

# 基于chromadb的嵌入模型实例
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=API_KEY,
    api_base=BASE_URL,
    model_name="BAAI/bge-m3",
    dimensions=1024
)


def get_completions(llm_prompt, model_endpoint):
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
                                                     max_tokens=512, extra_body=extra_body
                                                     )

    return response.choices[0].message.content.strip()
