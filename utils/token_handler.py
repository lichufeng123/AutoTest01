# utils/token_handler.py

import sqlite3
import os
import requests

class TokenHandler:
    _cache = {}  # 保存 token 和 refresh_token

    @classmethod
    def get_tokens(cls, customer_code):
        if customer_code in cls._cache:
            return cls._cache[customer_code]  # 返回 dict，包含 token 和 refresh_token

        # 获取数据库路径
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, 'db', 'auth.db')

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT login_url, user_no, password, device_type
            FROM auth_config
            WHERE customer_code = ?
        """, (customer_code,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            raise Exception(f"客户 [{customer_code}] 配置信息不存在")

        login_url, user_no, password, device_type = result
        payload = {
            "userNo": user_no,
            "password": password,
            "deviceType": device_type
        }

        try:
            resp = requests.post(login_url, json=payload)
            resp.raise_for_status()
            resp_json = resp.json()

            # 读取 token 和 refreshToken
            token = resp_json['data']['token']
            refresh_token = resp_json['data']['refreshToken']

            cls._cache[customer_code] = {
                "token": token,
                "refresh_token": refresh_token
            }
            return cls._cache[customer_code]
        except Exception as e:
            raise RuntimeError(f"[{customer_code}] 登录失败：{e}")

    @classmethod
    def get_token(cls, customer_code):
        return cls.get_tokens(customer_code)['token']

    @classmethod
    def get_refresh_token(cls, customer_code):
        return cls.get_tokens(customer_code)['refresh_token']
