'''
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''
import pytest
import yaml
from calculator_pract.calculator_pract import Calculator


def addd_data_calc():
    with open('../data_calc.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        add_data = data['add']['datas']
        ids = data['add']['ids']
    return [add_data, ids]


class TestCalcu:
    def setup_class(self):
        print("计算器类方法开始")
        self.calcu = Calculator()

    def teardown_class(self):
        print("计算器类方法结束")

    def setup(self):
        print("计算器方法执行开始")

    def teardown(self):
        print("计算器执行方法结束")

    @pytest.mark.parametrize('a,b,expect', [(11, 11, 22), (0.1, 0.1, 0.2)])
    def test_add(self, a, b, expect):
        re = self.calcu.add(a, b)
        assert re == expect

    @pytest.mark.parametrize('a,b,expect', addd_data_calc()[0], ids=addd_data_calc()[1])
    def test_add_deci(self, a, b, expect):
        re = round(self.calcu.add(a, b), 2)
        assert re == expect

    @pytest.mark.parametrize('a,b,expect', [(22, 11, 2), (0.2, 0.1, 2), (2, 0, 0), (0.05, 2, 0.025), (0.3, 0.1, 3)])
    def test_div(self, a, b, expect):
        try:
            re = self.calcu.div(a, b)
            assert expect == re
        except ZeroDivisionError:
            print("除数不能为零！")

    @pytest.mark.parametrize('a,b,expect', [(0.3, 0.1, 3)])
    def test_div_deci(self, a, b, expect):
        re = round(self.calcu.div(a, b), 2)
        assert re == expect
