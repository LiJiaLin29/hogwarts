"""
 @description: 四则运算
 @auther: 29263
 @date: 2020-08-17 14:33
"""
from builtins import *


def add(x, y):
    # 判断是否为数值
    if not isinstance((x, y), int):
        raise TypeError("输入包含非数字，类型错误")
    return int(x) + int(y)


def sub(x, y):
    # 判断是否为数值
    if not isinstance((x, y), int):
        raise TypeError("输入包含非数字，类型错误")
    return x - y


def mul(x, y):
    # 判断是否为数值
    if not isinstance((x, y), int):
        raise TypeError("输入包含非数字，类型错误")
    return x * y


def div(x, y):
    # 判断是否为数值
    if not isinstance((x, y), int):
        raise TypeError("输入包含非数字，类型错误")
    if y == 0:
        raise ZeroDivisionError("发生除数为零错误")
    return x / y


if __name__=="__main__":
    try:
        add('a', 'b')
    except Exception as e:
        print(e)