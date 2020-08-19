"""
 @description: 
 @auther: 29263
 @date: 2020-08-17 17:28
"""
from typing import List

import pytest
import yaml


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 加载测试数据文件（operation单元测试）
def yaml_data_with_key(key):  # 读取yaml数据中的key值，这里的yaml文件名是data
    with open('./datas/data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)  # 用load方法转字典
    return data[key]

