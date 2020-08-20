"""
 @description: 测试计算器加法、减法、乘法、除法功能
 @auther: 29263
 @date: 2020-08-18 20:29
"""

from mathUtil.operations import *
from testing.testFixture.conftest import *


class TestB:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('x, y, expected', yaml_data_with_key('valid_add')[0],
                             ids=yaml_data_with_key('valid_add')[1])
    def test_add(self, x, y, expected):
        r = add(x, y)
        print(f"{x}+{y}=", r)
        assert r == expected

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('x, y', [('2', 'a'), (None, 10)], ids=['包含非数字异常', "包含空值"])
    def test_add_except1(self, x, y):
        # 预期的异常
        with pytest.raises(TypeError) as e:
            div(x, y)
        err_msg = e.value.args[0]
        assert err_msg == "输入包含非数字，类型错误"

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('x, y, expected', yaml_data_with_key('valid_sub')[0],
                             ids=yaml_data_with_key('valid_sub')[1])
    def test_sub(self, x, y, expected):
        r = sub(x, y)
        print(f"{x}-{y}=", r)
        assert r == expected

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('x, y', [('2', 'a')], ids=['包含非数字异常'])
    def test_sub_except1(self, x, y):
        # 预期的异常
        with pytest.raises(TypeError) as e:
            sub(x, y)
        err_msg = e.value.args[0]
        assert err_msg == "输入包含非数字，类型错误"

    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('x, y, expected', yaml_data_with_key('valid_mul')[0],
                             ids=yaml_data_with_key('valid_mul')[1])
    def test_mul(self, x, y, expected):
        r = mul(x, y)
        print(f"{x}*{y}=", r)
        assert r == expected

    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('x, y', [('2', 'a')], ids=['包含非数字异常'])
    def test_mul_except1(self, x, y):
        # 预期的异常
        with pytest.raises(TypeError) as e:
            mul(x, y)
        err_msg = e.value.args[0]
        assert err_msg == "输入包含非数字，类型错误"

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('x, y, expected', yaml_data_with_key('valid_div')[0],
                             ids=yaml_data_with_key('valid_div')[1])
    def test_div(self, x, y, expected):
        r = div(x, y)
        print(f"{x}/{y}=", r)
        assert r == expected

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('x, y', [('2', 0)], ids=['除数为0异常'])
    def test_div_except1(self, x, y):
        # 预期的异常
        with pytest.raises(ZeroDivisionError) as e:
            div(x, y)
        err_msg = e.value.args[0]
        assert err_msg == "发生除数为零错误"

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('x, y', [('[]', 'a')], ids=['包含非数字异常'])
    def test_div_except2(self, x, y):
        # 预期的异常
        with pytest.raises(TypeError) as e:
            div(x, y)
        err_msg = e.value.args[0]
        assert err_msg == "输入包含非数字，类型错误"