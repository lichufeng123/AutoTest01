# utils/request_tool.py
import logging

from utils.token_handler import TokenHandler
import requests

# use_bearer的值为false的时候表示并非用jwt令牌格式验证
def request_with_token(customer_code, method, url_path, headers=None, use_bearer=False, **kwargs):
    if headers is None:
        headers = {}

    tokens = TokenHandler.get_tokens(customer_code)
    headers['Authorization'] = (
        f"Bearer {tokens['token']}" if use_bearer else tokens['token']
    )
    headers['RefreshToken'] = tokens['refresh_token']  # 如果后端要求
    #  加上日志记录
    logging.info(f"【{customer_code}】请求接口：{method} {url_path}")
    logging.info(f"请求参数：{kwargs.get('json') or kwargs.get('data')}")

    base_url = TokenHandler.get_base_url(customer_code)
    full_url = base_url.rstrip('/') + url_path  # 拼接完整地址
    response = requests.request(method, full_url, headers=headers, **kwargs)

    #  加上日志记录
    logging.info(f"响应状态码：{response.status_code}")
    logging.info(f"响应内容：{response.text}")

    return response
