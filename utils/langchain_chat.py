#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: langchain_chat.py
@time: 2025/6/10 15:55
@project: llm-cookbook
@desc: 
"""
import os

from dotenv import load_dotenv, find_dotenv
from langchain_openai.chat_models import ChatOpenAI

loaded = load_dotenv(find_dotenv(), override=True)
# 从环境变量中获取 OpenAI API Key 或者直接赋值
API_KEY = os.getenv("API_KEY")

# 如果您使用的是官方 API，就直接用 https://api.siliconflow.cn/v1 就行。
BASE_URL = "https://api.siliconflow.cn/v1"

# 基于langchain的OpenAI实例，用于代码生成
llm = ChatOpenAI(temperature=0.20, model_name="Qwen/Qwen2.5-Coder-7B-Instruct", max_tokens=4096,
                 openai_api_key=API_KEY, openai_api_base=BASE_URL, max_retries=3,
                 seed=42, presence_penalty=0.1, frequency_penalty=0.1
                 )
