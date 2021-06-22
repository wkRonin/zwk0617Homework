import pytest
import logging
from testing.datas.get_data import ReadFile
from pythoncode.calculaltor import Calculator


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(autouse=True)
def setup_teardown():
    """
    session级的setup与teardown
    :return: null
    """
    logging.info('开始计算')
    yield
    logging.info('结束计算')


@pytest.fixture(scope='class')
def setup_class():
    """
    实例化计算器代码
    :return: null
    """
    calc = Calculator()
    logging.info("计算器实例化完成")
    return calc


@pytest.fixture(params=ReadFile().getData()['add_success']['datas'])
def add_success_data(request):
    """
    参数化加法正向用例数据
    :param request: 内置fixture
    :return:加法正向用例数据
    """
    return request.param


@pytest.fixture(params=ReadFile().getData()['add_fail']['datas'])
def add_fail_data(request):
    """
    参数化加法异常用例数据
    :param request: 内置fixture
    :return:加法异常用例数据
    """
    return request.param


@pytest.fixture(params=ReadFile().getData()['div_success']['datas'])
def div_success_data(request):
    """
    参数化除法异常用例数据
    :param request: 内置fixture
    :return:除法异常用例数据
    """
    return request.param


@pytest.fixture(params=ReadFile().getData()['div_success']['dataic'])
def div_ic_data(request):
    """
    参数化除法结果为无限循环小数用例数据
    :param request: 内置fixture
    :return:除法结果为无限循环小数用例数据
    """
    return request.param


@pytest.fixture(params=ReadFile().getData()['div_fail']['datas'])
def div_fail_data(request):
    """
    参数化除法异常用例数据
    :param request: 内置fixture
    :return:除法异常用例数据
    """
    return request.param


@pytest.fixture(params=ReadFile().getData()['div_fail']['datazero'])
def div_zero_data(request):
    """
    参数化除法的除数为0用例数据
    :param request: 内置fixture
    :return:除法的除数为0用例数据
    """
    return request.param
