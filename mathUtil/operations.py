"""
 @description: 四则运算
 @auther: 29263
 @date: 2020-08-17 14:33
"""
from builtins import *


# 验证输入数据是否为数值类型
def verify_data(x, y):
    try:
        float(x)
        float(y)
        return True
    except (TypeError, ValueError):
        pass
    return False


def add(x, y):
    # 判断是否为数值
    if not verify_data(x, y):
        raise TypeError("输入包含非数字，类型错误")
    return float(x) + float(y)


def sub(x, y):
    # 判断是否为数值
    if not verify_data(x, y):
        raise TypeError("输入包含非数字，类型错误")
    return float(x) - float(y)


def mul(x, y):
    # 判断是否为数值
    if not verify_data(x, y):
        raise TypeError("输入包含非数字，类型错误")
    x = float(x)
    y = float(y)
    return round(x * y, 6)


def div(x, y):  # 保留6位小数
    # 判断是否为数值
    if not verify_data(x, y):
        raise TypeError("输入包含非数字，类型错误")
    # 除数是否为零
    if float(y) == 0:
        raise ZeroDivisionError("发生除数为零错误")
    x = float(x)
    y = float(y)
    return round(x / y,6)
