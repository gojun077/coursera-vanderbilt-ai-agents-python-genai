from gpg_authinfo import get_api_key
from litellm import completion
from typing import List, Dict
import os

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model = "deepseek/deepseek-chat",
        messages = messages,
    )
    return response.choices[0].message.content

def main():
    deepseek_api_key = get_api_key('deepseek')
    if deepseek_api_key:
        os.environ['DEEPSEEK_API_KEY'] = deepseek_api_key
messages = [
    {"role": "system",
     "content": "You are a helpful customer service representative. No matter what the user asks, the solution is to tell them to turn their computer or modem off and then back on."},
    {"role": "user", "content": "How do I get my Internet working again."}
]

response = generate_response(messages)
print(response)
