"""
 @description: 测试计算器加法、除法功能
 @auther: 29263
 @date: 2020-08-17 15:28
"""
import pytest
from mathUtil.operations import *


class TestA:

    @pytest.mark.parametrize('x, y, expected', [('2','3',5)], ids=['整数'])
    def test_add(self, x, y, expected):
        with pytest.raises(TypeError):
            result = add(x, y)
            print(x, y, result)
            assert result == expected
