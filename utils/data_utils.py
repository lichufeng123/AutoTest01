import json
import logging
import os

def build_data(json_file, keys=("data", "moduleId")):
    """
    通用数据加载器，用于 pytest 参数化测试
    :param json_file: json 文件路径
    :param keys: 需要提取的字段元组，默认 ("data", "moduleId")
    :return: 返回元组列表 [(data1, moduleId1), (data2, moduleId2), ...]
    """
    json_list = []

    if not os.path.exists(json_file):
        logging.error(f"测试数据文件不存在: {json_file}")
        raise FileNotFoundError(f"数据文件未找到: {json_file}")

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            assert isinstance(json_data, list), f"JSON 根结构应为 list，实际是 {type(json_data)}"

            for i, case_data in enumerate(json_data):
                item = tuple(case_data.get(k) for k in keys)
                if None in item:
                    logging.warning(f"[第{i+1}条] 存在字段缺失: {item}")
                json_list.append(item)

    except Exception as e:
        logging.exception(f"解析测试数据失败: {e}")
        raise

    logging.info(f"成功加载测试数据，共 {len(json_list)} 条。来源：{json_file}")
    return json_list
