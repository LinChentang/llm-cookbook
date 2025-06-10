#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: image_demo.py
@time: 2025/6/10 16:03
@project: llm-cookbook
@desc: 
"""
# 导入所需的库
import base64
import io

import gradio as gr
import requests
from PIL import Image

from utils.image2text_chat import get_completion, InputImageType


# 将PIL图像转换为base64编码的字符串
def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))


# 从URL获取图片
def get_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        return Image.open(io.BytesIO(response.content))
    except Exception as e:
        print(f"获取图片失败: {e}")
        return None


# 图像描述生成函数，修改为支持图片文件和图片URL
def captioner(image, image_url, prompt):
    if image and image_url:
        return "请上传图片或输入图片URL，不要同时上传", None
    if image:
        # 处理上传的图片文件
        base64_image = image_to_base64_str(image)
        display_image = image
        result = get_completion(InputImageType.IMAGE_BASE64, base64_image, text_input=prompt)
    elif image_url:
        # 处理图片URL
        pil_image = get_image_from_url(image_url)
        if pil_image:
            display_image = pil_image
        else:
            return "无法获取图片，请检查URL", None
        result = get_completion(InputImageType.IMAGE_URL, image_url, text_input=prompt)
    else:
        return "请上传图片或输入图片URL", None

    return result, display_image


# 关闭之前的Gradio界面（如果有的话）
gr.close_all()

# 创建Gradio界面，接受上传的图像并显示描述
demo = gr.Interface(
    fn=captioner,  # 指定用于处理输入的函数
    inputs=[
        gr.Image(label="上传图片（Image upload）", type="pil"),
        gr.Textbox(label="图片URL（Image URL）", placeholder="请输入图片URL地址"),
        gr.Textbox(label="提示词（Prompt）", placeholder="请输入提示词")
    ],  # 输入部分的设置，允许上传图像和输入图片URL
    outputs=[
        gr.Textbox(label="描述"),
        gr.Image(label="图片展示", type="pil")
    ],  # 输出部分的设置，显示生成的图像描述和展示图片
    title="Image Captioning with BLIP",  # 界面标题
    description="Caption any image using the BLIP model",  # 界面描述
    flagging_mode="never",  # 设置不允许标记内容
)

# 启动共享模式的界面，允许其他用户访问
demo.launch(share=True)
