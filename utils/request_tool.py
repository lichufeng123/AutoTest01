# utils/request_tool.py

from utils.token_handler import TokenHandler
import requests

def request_with_token(customer_code, method, url, headers=None, **kwargs):
    if headers is None:
        headers = {}

    tokens = TokenHandler.get_tokens(customer_code)
    headers['Authorization'] = f"Bearer {tokens['token']}"
    headers['RefreshToken'] = tokens['refresh_token']  # 如果后端要求

    return requests.request(method, url, headers=headers, **kwargs)
