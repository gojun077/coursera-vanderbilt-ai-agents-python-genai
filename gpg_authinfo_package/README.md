# gpg_authinfo

A Python module to read GPG-encrypted authinfo files for API credentials.

## Installation

```bash
pip install python-gnupg
```

## Usage

As of Sun 14 Sep 2025 the following model providers are supported:

- anthropic
- dashscope (aliyun/alibaba)
- deepseek
- openai
- google
- x.ai

```python
from gpg_authinfo import get_api_key

# Get API key for a provider
openai_key = get_api_key('openai')
anthropic_key = get_api_key('anthropic')
```
