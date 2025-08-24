#!/usr/bin/env python3
# programmatic_prompting_for_agents.py
# Module 1 - Agentic AI Concepts - .. Prompting for Agents
# https://www.coursera.org/learn/ai-agents-python/ungradedWidget/5cdvg/programmatic-prompting-for-agents
#
# Created on: Sun 24 Aug 2025
# Created by: gopeterjun@naver.com
# Last Updatedate: Sun 24 Aug 2025
#
# This script sets a system prompt and then asks OpenAI gpt4o to generate
# code in a functional programming style using 'litellm' as the unified
# LLM API interface.

from gpg_authinfo import get_api_key
from litellm import completion
from typing import List, Dict
import os


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content

def main():
    openai_api_key = get_api_key('openai')
    if openai_api_key:
        os.environ['OPENAI_API_KEY'] = openai_api_key
    messages = [
        {"role": "system",
         "content": "You are an expert software engineer that prefers functional programming."},
        {"role": "user",
         "content": "Write a function to swap the keys and values in a dictionary."}
    ]
    response = generate_response(messages)
    print(response)

if __name__ == '__main__':
    main()
