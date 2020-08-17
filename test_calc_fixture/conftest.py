import pytest


@pytest.fixture(scope='module')
def calc_print():
    print("开始计算")
    yield
    print("结束计算")
