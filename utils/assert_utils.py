import allure
import logging
# 增加提交记录
def log_and_assert_response(response, expect_code=200, description="接口请求"):
    """统一日志打印 + Allure 记录 + 状态断言"""
    try:
        data = response.json()
    except Exception:
        data = response.text

    logging.info(f"{description} 响应: {data}")
    allure.attach(str(data), name=f"{description}响应内容", attachment_type=allure.attachment_type.TEXT)

    assert response.status_code == 200, f"{description} 请求失败，HTTP状态码: {response.status_code}"
    assert data.get("code") == expect_code, f"{description} 响应code异常: {data.get('code')} != {expect_code}"
