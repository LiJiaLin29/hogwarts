"""
 @description: 
 @author: 29263
 @date: 2020-09-11 12:50
"""
from typing import List
import yaml


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def yaml_data_load(key, path=None):  # 读取yaml数据中的key值，这里的yaml文件名是data
    """
    加载测试数据文件（operation单元测试）
    :param key: 数据key值，唯一
    :param path: 文件路径
    return: 返回元组params(str),value(list)
    """
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)  # 用load方法转字典
    case = data[key]
    # 遍历字典组合成参数列表和测试数据
    param_list: list = case[0].keys()
    dlist = list()
    if len(param_list) > 1:
        for item in case:
            dlist.append(item.values())
    else:
        for item in case:
            dlist.extend(item.values())
    return ",".join(param_list), dlist


if __name__ == "__main__":
    print(yaml_data_load("add_contact_list", "./data/TestContacts.yaml"))
