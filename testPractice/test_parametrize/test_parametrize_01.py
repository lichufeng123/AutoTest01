import pytest

# 单参数 多次循环
@pytest.mark.parametrize("name,local",[['流川枫','樱木花道'],['前锋','中锋']])
def test_parametrize(name,local):
    print("我是"+name,"我打"+local)
