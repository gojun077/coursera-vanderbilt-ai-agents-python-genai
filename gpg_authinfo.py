# gpg_authinfo_.py
#
# Created on: Sun 24 Aug 2025
# Created by: gopeterjun@naver.com
# Last Updated: Sun 24 Aug 2025
#
# This file contains a helper function to open a GPG-encrypted 'authinfo'
# file that stores API credentials in 'netrc' format. This file is intended
# to be called by other Python programs as a library and will not be
# executed directly.

# The following lines show sample content of an 'authinfo.gpg' file in
# plaintext:
#
# machine my-macbookair login myuser port sudo password REDACTED
# machine api.anthropic.com login apikey password LONG-API-SECRET-KEY
# # the following entry is required for Emacs Efrit
# machine api.anthropic.com login personal password LONG-API-SECRET-KEY
# machine api.openai.com login apikey password LONG-API-SECRET-KEY
#
# Each sublist will have the following index-to-field mapping:
#
# - List[0]: (remote) host field - can be one of 'machine' or 'default'
# - List[1]: (remote) host field value - i.e. 'api.openai.com'
# - List[2]: login field - 'login'
# - List[3]: login field value - i.e. 'apikey', 'personal', etc
# - List[4]: password field - 'password'
# - List[5]: password field value - password or secret key
#
# 'gpg_authinfo.py' requires the pip package 'python-gnupg' which provides
# 'gnupg' module for working with GNU Privacy Guard on Linux.


import gnupg
import os

def get_creds_authinfo(filename: str) -> list[list[str]]:
    """
    Given str 'filename' including full path to gpg-encrypted file
    in 'netrc' format, return a ListOf[ListOf[str]] containing the
    plaintext contents of the gpg-encrypted file.
    """
    try:
        gpg = gnupg.GPG(use_agent=True)
        with open(os.path.expanduser(filename), 'rb') as f:
            decrypted_data = gpg.decrypt_file(f)
            if decrypted_data.ok:
                credsL = [line.split() for line in str(decrypted_data).split('\n') if line.startswith('machine')]
                return credsL
            else:
                print(f"Decryption failed: {decrypted_data.stderr}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_api_key(provider: str) -> str:
    """
    Given str 'provider' ('anthropic', 'openai', 'deepseek', 'alibaba',
    'google', 'x.ai', etc), open a netrc-formatted gpg-encrypted credential
    file and search for the model provider and return the API secret key
    for the requested provider.
    """
    try:
        providersL = ['anthropic', 'openai', 'deepseek', 'alibaba',
                      'google', 'x.ai']
        if provider not in providersL:
            print(f"Unknown model provider! Please try one of {providersL}")
            return None
        creds = get_creds_authinfo("~/.authinfo.gpg")
        if creds:
            for line in creds:
                if provider in line[1]:
                    return line[5]
            print(f"Model provider {provider} not found in credentials!")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
