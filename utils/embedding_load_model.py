#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: embedding_load_model.py
@time: 2025/6/10 15:56
@project: llm-cookbook
@desc: 嵌入模型加载
"""

import os

import chromadb.utils.embedding_functions as embedding_functions
from dotenv import load_dotenv, find_dotenv

loaded = load_dotenv(find_dotenv(), override=True)
# 从环境变量中获取 OpenAI API Key 或者直接赋值
API_KEY = os.getenv("API_KEY")

# 如果您使用的是官方 API，就直接用 https://api.siliconflow.cn/v1 就行。
BASE_URL = "https://api.siliconflow.cn/v1"

# 基于chromadb的嵌入模型实例
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=API_KEY,
    api_base=BASE_URL,
    model_name="BAAI/bge-m3",
    dimensions=1024
)
