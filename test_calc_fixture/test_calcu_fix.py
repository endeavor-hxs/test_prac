'''
作业1：
1、补全计算器（加减乘除）的测试用例
2、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
3、将 Fixture 方法存放在conftest.py ，设置scope=module
'''

import pytest
import yaml
import os
from calculator_pract.calculator_pract import Calculator


# 加法数据参数化
def addd_data_calc():
    filepath = os.path.dirname(__file__) + "/data_calc.yml"
    with open(filepath, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        add_data = data['add']['datas']
        ids = data['add']['ids']
    return [add_data, ids]


# 减法数据参数化
def sub_data_calc():
    filepath = os.path.dirname(__file__) + "/data_calc.yml"
    with open(filepath, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        sub_data = data['sub']['datas']
        ids = data['sub']['ids']
    return [sub_data, ids]


class TestCalcu:
    calcu = Calculator()

    # 加法运算
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', [(11, 11, 22), (0.1, 0.1, 0.2)])
    def test_add(self, a, b, expect, calc_print):
        re = self.calcu.add(a, b)
        assert re == expect

    # 加法小数类型计算
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', addd_data_calc()[0], ids=addd_data_calc()[1])
    def test_add_deci(self, a, b, expect, calc_print):
        re = round(self.calcu.add(a, b), 3)
        assert re == expect

    # 除法计算
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a,b,expect', [(22, 11, 2), (0.2, 0.1, 2), (2, 0, 0), (0.05, 2, 0.025), (0.3, 0.1, 3)])
    def test_div(self, a, b, expect, calc_print):
        try:
            re = round(self.calcu.div(a, b), 3)
            assert expect == re
        except ZeroDivisionError:
            print("除数不能为零！")
        except Exception:
            print("输入数据异常！")

    # 减法运算
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', sub_data_calc()[0], ids=sub_data_calc()[1])
    def test_sub(self, a, b, expect, calc_print):
        re = self.calcu.sub(a, b)
        assert re == expect

    # 乘法运算
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', [(11, 11, 121), (0.1, 0.2, 0.02)])
    def test_mul(self, a, b, expect, calc_print):
        re = round(self.calcu.mul(a, b), 2)
        assert re == expect
