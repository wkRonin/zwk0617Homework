import logging
import shutil
import pytest
import allure
import os
from decimal import *


@allure.feature("计算器测试用例")
class TestCalculator:

    @allure.story("正常数据的加法")
    @allure.title("{add_success_data[0]} + {add_success_data[1]}")
    def test_add(self, add_success_data, setup_class):
        """
        单元测试加法运算，预期正常
        :param add_success_data:加法的参数化正常数据
        :param setup_class: 实例化计算器代码
        :return: 断言结果
        """
        add1, add2, expect = add_success_data
        with allure.step(f'执行计算 {add1} + {add2}'):
            logging.info(f'执行计算 : {add1} + {add2} = {expect}')
            assert str(expect) == str(setup_class.add(add1, add2))

    @allure.story("异常数据的加法")
    @allure.title("{add_fail_data[0]} + {add_fail_data[1]}")
    def test_add_exception(self, add_fail_data, setup_class):
        """
        单元测试加法运算，预期异常
        :param add_fail_data:加法的参数化异常数据
        :param setup_class: 实例化计算器代码
        :return: 断言结果
        """
        add1, add2, expect = add_fail_data
        with allure.step(f'执行计算 {add1} + {add2}'):
            logging.info(f'执行计算 : {add1} + {add2} = {expect}')
            with pytest.raises(Exception):
                setup_class.add(add1, add2)

    @allure.story("正常数据的除法")
    @allure.title("{div_success_data[0]} + {div_success_data[1]}")
    def test_div(self, div_success_data, setup_class):
        """
        单元测试除法运算，预期正常
        :param div_success_data:除法的参数化正常数据
        :param setup_class: 实例化计算器代码
        :return: 断言结果
        """
        div1, div2, expect = div_success_data
        with allure.step(f'执行计算 {div1} / {div2}'):
            logging.info(f'执行计算 : {div1} / {div2} = {expect}')
            assert str(expect) == str(setup_class.div(div1, div2))

    @allure.story("正常数据的除法")
    @allure.title("{div_ic_data[0]} + {div_ic_data[1]}")
    def test_div_ic(self, div_ic_data, setup_class):
        """
        单元测试除法运算，预期无限循环
        :param div_ic_data:商为无限循环的除法参数化数据
        :param setup_class: 实例化计算器代码
        :return: 断言结果
        """
        div1, div2, expect = div_ic_data
        div_result = setup_class.div(div1, div2)
        # 把str结果转化成Decimal格式，并保留8位小数（可四舍五入）以修正无限循环小数无法断言问题
        result = Decimal(div_result).quantize(Decimal('0.00000000'))
        with allure.step(f'执行计算 {div1} / {div2}'):
            logging.info(f'执行计算 : {div1} / {div2} = {expect}')
            assert str(expect) == str(result)

    @allure.story("异常数据的除法")
    @allure.title("{div_fail_data[0]} / {div_fail_data[1]}")
    def test_div_exception(self, div_fail_data, setup_class):
        """
        单元测试除法运算，预期异常
        :param div_fail_data:除法的参数化异常数据
        :param setup_class: 实例化计算器代码
        :return: 断言结果
        """
        div1, div2, expect = div_fail_data
        with allure.step(f'执行计算 {div1} / {div2}'):
            logging.info(f'执行计算 : {div1} / {div2} = {expect}')
            with pytest.raises(Exception):
                setup_class.div(div1, div2)

    @allure.story("异常数据的除法")
    @allure.title("{div_zero_data[0]} / {div_zero_data[1]}")
    def test_div_zero(self, div_zero_data, setup_class):
        """
        单元测试除法运算，预期异常
        :param div_zero_data:除法的参数化异常数据
        :param setup_class: 实例化计算器代码
        :return: 断言结果
        """
        div1, div2, expect = div_zero_data
        with allure.step(f'执行计算 {div1} / {div2}'):
            logging.info(f'执行计算 : {div1} / {div2} = {expect}')
            with pytest.raises(ZeroDivisionError):
                setup_class.div(div1, div2)


if __name__ == '__main__':
    if os.path.exists('report/'):
        shutil.rmtree(path='report/')
    pytest.main(
        args=[
            'testing/',
            '-v',
            # '-n=2',
            f'--alluredir=report/data'])
    # 自动以服务形式打开报告
    # os.system(f'allure serve ./report/data')

    # 本地生成报告
    os.system(f'allure generate ./report/data -o report/html --clean')