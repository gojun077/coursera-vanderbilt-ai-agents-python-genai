#!/usr/bin/env python3
# litllm_test.py
#
# Created on: Sun 24 Aug 2025
# Created by: gopeterjun@naver.com
# Last Updated: Sun 24 Aug 2025
#
# This script tests API connections to various model providers via
# 'litellm' using API credentials read from a gpg-encrypted netrc formatted
# file.

from gpg_authinfo import get_api_key
from litellm import completion
import argparse
import os
import sys


def test_aliyun() -> int:
    """Tests the Aliyun API call and returns an exit code."""
    print("### Testing Aliyun API call in LiteLLM")
    try:
        aliyun_api_key = get_api_key('dashscope')
        if aliyun_api_key:
            os.environ['DASHSCOPE_API_KEY'] = aliyun_api_key
            messages = [{"role": "user", "content": "hello from litellm"}]
            response = completion(
                model="dashscope/qwen-turbo",
                messages = messages
                )
            print(response)
            return 0
        else:
            print("Aliyun/Dashscope API key not found!", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"An exception occurred during the Aliyun test: {e}",
              file=sys.stderr)
        return 1

def test_anthropic() -> int:
    """Tests the Anthropic API call and returns an exit code."""
    print("### Testing Anthropic API call in LiteLLM")
    try:
        anthropic_api_key = get_api_key('anthropic')
        if anthropic_api_key:
            os.environ['ANTHROPIC_API_KEY'] = anthropic_api_key
            messages = [{"role": "user", "content": "Hey! how's it going?"}]
            response = completion(
                model = "claude-sonnet-4-20250514",
                messages = messages)
            print(response)
            return 0
        else:
            print("Anthropic API key not found!", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"An exception occurred during the Anthropic test: {e}",
              file=sys.stderr)
        return 1

def test_deepseek() -> int:
    """Tests the DeepSeek API call and returns an exit code."""
    print("### Testing DeepSeek API call in LiteLLM")
    try:
        deepseek_api_key = get_api_key('deepseek')
        if deepseek_api_key:
            os.environ['DEEPSEEK_API_KEY'] = deepseek_api_key
            messages = [{"role": "user", "content": "hello from litellm"}]
            response = completion(
                model = "deepseek/deepseek-chat",
                messages = messages,
            )
            print(response)
            return 0
        else:
            print("Deepseek API key not found!", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"An exception occurred during the DeepSeek test: {e}",
              file=sys.stderr)
        return 1

def test_gemini() -> int:
    print("### Testing Gemini API call in LiteLLM")
    try:
        gemini_api_key = get_api_key('google')
        if gemini_api_key:
            os.environ['GEMINI_API_KEY'] = gemini_api_key
            messages = [{"role": "user",
                         "content": "What is the capital of France?"}]
            response = completion(
                model = "gemini/gemini-2.5-flash",
                messages = messages
            )
            print(response)
            return 0
        else:
            print("Gemini API key not found!", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"An exception occurred during the Gemini test: {e}",
              file=sys.stderr)
        return 1

def test_openai() -> int:
    print("### Testing OpenAI API call in LiteLLM")
    try:
        openai_api_key = get_api_key('openai')
        if openai_api_key:
            os.environ['OPENAI_API_KEY'] = openai_api_key
            messages = [{"role": "user",
                         "content": "Hello, from liteLLM! TEST"}]
            response = completion(
                model = "gpt-5",
                messages = messages
            )
            print(response)
            return 0
        else:
            print("OpenAI API key not found!", file=sys.stderr)
            return 1
    except Exception as e:
        print(f"An exception occurred during the OpenAI test: {e}",
              file=sys.stderr)
        return 1

def test_xai() -> int:
    print("### Testing X.AI API call in LiteLLM")
    try:
        xai_api_key = get_api_key('x.ai')
        if xai_api_key:
            os.environ['XAI_API_KEY'] = xai_api_key
            messages = [{"role": "user",
                         "content":
                         "Greetings from liteLLM! TEST"}]
            response = completion(
                model = "xai/grok-4",
                messages = messages,
                max_tokens=1024,
                response_format={ "type": "json_object" },
                seed=123,
                temperature=0.2,
                top_p=0.9,
                user="user-debug-run")
            print(response)
            return 0
    except Exception as e:
        print(f"An exception occurred during the xAI test: {e}",
              file=sys.stderr)
        return 1

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run API connectivity tests for various LLM providers."
    )
    parser.add_argument(
        '--aliyun',
        action='store_true', # Makes it a flag, e.g., no value needed
        help='Run the Aliyun API test.'
    )
    parser.add_argument(
        '--anthropic',
        action='store_true',
        help='Run the Anthropic API test.'
    )
    parser.add_argument(
        '--deepseek',
        action='store_true',
        help='Run the DeepSeek API test.'
    )
    parser.add_argument(
        '--gemini',
        action='store_true',
        help='Run the Gemini API test.'
    )
    parser.add_argument(
        '--openai',
        action='store_true',
        help='Run the OpenAI API test.'
    )
    parser.add_argument(
        '--xai',
        action='store_true',
        help='Run the xAI API test.'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all available API tests.'
    )
    args = parser.parse_args()
    testL = [args.aliyun, args.anthropic, args.deepseek, args.gemini,
             args.openai, args.xai, args.all]

    # If no test is specified, show help and exit
    if not any(testL):
        parser.print_help()
        print("\nNo tests specified. Please select a test to run.",
              file=sys.stderr)
        return 1

    exit_code = 0
    if args.aliyun or args.all:
        print("\n--- Running Aliyun Test ---")
        if test_aliyun() != 0:
            exit_code = 1 # Mark failure if any test fails
            print("--- Aliyun Test FAILED ---\n")
        else:
            print("--- Aliyun Test PASSED ---\n")

    if args.anthropic or args.all:
        print("\n--- Running Anthropic Test ---")
        if test_anthropic() != 0:
            exit_code = 1 # Mark failure if any test fails
            print("--- Anthropic Test FAILED ---\n")
        else:
            print("--- Anthropic Test PASSED ---\n")

    if args.deepseek or args.all:
        print("\n--- Running Deepseek Test ---")
        if test_deepseek() != 0:
            exit_code = 1
            print("--- Deepseek Test FAILED ---\n")
        else:
            print("--- Deepseek Test PASSED ---\n")

    if args.gemini or args.all:
        print("\n--- Running Gemini Test ---")
        if test_gemini() != 0:
            exit_code = 1
            print("--- Gemini Test FAILED ---\n")
        else:
            print("--- Gemini Test PASSED ---\n")

    if args.openai or args.all:
        print("\n--- Running OpenAI Test ---")
        if test_openai() != 0:
            exit_code = 1
            print("--- OpenAI Test FAILED ---\n")
        else:
            print("--- OpenAI Test PASSED ---\n")

    if args.xai or args.all:
        print("\n--- Running xAI Test ---")
        if test_xai() != 0:
            exit_code = 1
            print("--- xAI Test FAILED ---\n")
        else:
            print("--- xAI Test PASSED ---\n")

    if exit_code == 0:
        print("✅ All selected tests completed successfully!")
    else:
        print("❌ Some tests failed.")

    return exit_code

if __name__ == "__main__":
    sys.exit(main())
