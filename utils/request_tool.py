# utils/request_tool.py

from utils.token_handler import TokenHandler
import requests

def request_with_token(customer_code, method, url, headers=None, **kwargs):
    if headers is None:
        headers = {}

    tokens = TokenHandler.get_tokens(customer_code)
    headers['Authorization'] = f"Bearer {tokens['token']}"
    headers['RefreshToken'] = tokens['refresh_token']  # 如果后端要求
    # ✅ 加上日志记录
    logging.info(f"【{customer_code}】请求接口：{method} {url}")
    logging.info(f"请求参数：{kwargs.get('json') or kwargs.get('data')}")

    response = requests.request(method, url, headers=headers, **kwargs)

    logging.info(f"响应状态码：{response.status_code}")
    logging.info(f"响应内容：{response.text}")

    return response
