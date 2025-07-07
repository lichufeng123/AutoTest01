from utils.request_tool import request_with_token

def test_goods_list_customer_a():
    url = "http://114.132.41.62:8174/information/goods/page"
    data = {
        "data": {
            "moduleId": "120003",
            "keyword": "",
            "statusList": [0, 1, 2]
        },
        "page": 1,
        "pageSize": 50,
        "moduleId": "120003"
    }
    resp = request_with_token("customer_a", "POST", url, json=data)
    assert resp.status_code == 200
