#!/usr/bin/env python3
# programmatic_prompting_for_agents.py
# Module 1 - Agentic AI Concepts - .. Prompting for Agents II
# https://www.coursera.org/learn/ai-agents-python/ungradedWidget/dn7kg/programmatic-prompting-for-agents-ii
#
# Created on: Sun 24 Aug 2025
# Created by: gopeterjun@naver.com
# Last Updatedate: Sun 24 Aug 2025
#
# This script sets a system prompt and then asks OpenAI gpt4o to generate
# code in a functional programming style using 'litellm' as the unified
# LLM API interface. In this variation, we will tweak the system prompt
# to only respond using Base64-encoded text.

from gpg_authinfo import get_api_key
from litellm import completion
from typing import Dict, List, Union
import base64
import binascii
import os


def generate_response_b64(messages: List[Dict]) -> bytes:
    """Call LLM to get response in base64 (bytes)"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content

def decode_b64(data: Union[str, bytes]) -> str:
    """
    Safely decodes a Base64 string or bytes object to UTF-8 plaintext.

    >>> decode_b64("UHl0aG9uIGlzIGF3ZXNvbWUh")
    'Python is awesome!'

    >>> decode_b64(b"SGVsbG8sIFdvcmxkIQ==")
    'Hello, World!'

    >>> decode_b64("UHl0aG9uIGl#IGF3ZXNvbWUh")
    'Error decoding Base64: Incorrect padding'
    """
    try:
        # Decode the Base64 data into bytes, then decode the bytes into a
        # UTF-8 string
        return base64.b64decode(data).decode('utf-8')
    except (binascii.Error, UnicodeDecodeError) as e:
        # Handle incorrect padding, invalid characters, or non-UTF8 results
        return f"Error decoding Base64: {e}"

def main():
    openai_api_key = get_api_key('openai')
    if openai_api_key:
        os.environ['OPENAI_API_KEY'] = openai_api_key
    messages = [
        {"role": "system",
         "content": "You are an expert programming oracle that prefers functional programming and can only respond in Base64-encoded text."},
        {"role": "user",
         "content": "Write a function to swap the keys and values in a dictionary."}
    ]
    response = generate_response_b64(messages)
    print(f"Base64 text: {response}")
    print(f"UTF8 text: {decode_b64(response)}")

if __name__ == '__main__':
    main()
