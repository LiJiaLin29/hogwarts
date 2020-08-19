"""
 @description: 
 @auther: 29263
 @date: 2020-08-17 17:28
"""
import pytest
import yaml
import os


# 加载测试数据文件（operation单元测试）
def yaml_data_with_key(key):  # 读取yaml数据中的key值，这里的yaml文件名是data
    # 获取测试数据的路径testing
    cur_path = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')
    with open(cur_path+'/datas/data_fixture.yaml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)  # 用load方法转字典
    datas = mydatas[key]['datas']
    ids = mydatas[key]['ids']
    return datas, ids


# test测试方法前置/后置操作
@pytest.fixture(scope="module", autouse=True)
def attatch_info():
        print("开始计算")
        yield
        print("\n计算结束")


if __name__ == "__main__":
    print(yaml_data_with_key('valid_add'))