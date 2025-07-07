import logging
import os


def pytest_configure(config):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 当前 conftest.py 所在路径
    log_dir = os.path.join(base_dir, 'TestCase', 'MemberSystem', 'log')
    os.makedirs(log_dir, exist_ok=True) #  自动创建目录

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="log/test_log.log",
        filemode="w"
    )
