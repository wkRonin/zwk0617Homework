import logging
import pytest
from pythoncode.calculaltor import Calculator
from testing.datas.get_data import ReadFile
from decimal import *

readfile = ReadFile()
datas = readfile.getData()

class TestCalculator:
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        logging.info("开始计算")

    def teardown(self):
        logging.info("结束计算")

    @pytest.mark.parametrize('add1, add2, expect', datas['add_success']['datas'])
    def test_add(self, add1, add2, expect):
        """
        单元测试加法运算，预期成功
        :param add1: 第一个加数
        :param add2: 第二个加数
        :param expect: 预期结果
        :return: 断言结果
        """
        assert str(expect) == self.calc.add(add1, add2)

    @pytest.mark.parametrize('add1, add2, expect', datas['add_fail']['datas'])
    def test_addexc(self, add1, add2, expect):
        """
        单元测试加法运算，预期异常
        :param add1: 第一个加数
        :param add2: 第二个加数
        :param expect: 预期结果
        :return: 断言结果
        """
        with pytest.raises(Exception) as e:
            self.calc.add(add1, add2)
        assert str(expect) in str(e)


    @pytest.mark.parametrize('div1, div2, expect', datas['div_success']['datas'])
    def test_div(self, div1, div2, expect):
        """
        单元测试除法运算
        :param div1: 被除数
        :param div2: 除数
        :param expect: 预期结果
        :return: 断言结果
        """
        assert str(expect) == self.calc.div(div1, div2)

    @pytest.mark.parametrize('div1, div2, expect', datas['div_fail']['datas'])
    def test_divexc(self, div1, div2, expect):
        """
        单元测试除法运算,预期异常
        :param div1: 被除数
        :param div2: 除数
        :param expect: 预期结果
        :return: 断言结果
        """
        with pytest.raises(Exception) as e:
            self.calc.div(div1, div2)
        assert str(expect) in str(e)

    @pytest.mark.parametrize('div1, div2, expect', datas['div_fail']['data0'])
    def test_divexc0(self, div1, div2, expect):
        """
        单元测试除法运算,预期除数不能为0的异常
        :param div1: 被除数
        :param div2: 除数
        :param expect: 预期结果
        :return: 断言结果
        """
        with pytest.raises(ZeroDivisionError) as e:
            self.calc.div(div1, div2)
        assert str(expect) in str(e)

    @pytest.mark.parametrize('div1, div2, expect', datas['div_success']['dataic'])
    def test_divic(self, div1, div2, expect):
        """
        单元测试除法运算，无限循环的情况
        :param div1: 被除数
        :param div2: 除数
        :param expect: 预期结果为无限循环小数并保留8位小数（四舍五入）
        :return: 断言结果
        """
        div_result = self.calc.div(div1, div2)
        # 把str结果转化成Decimal格式，并保留8位小数（可四舍五入）以修正无限循环小数无法断言问题
        result = Decimal(div_result).quantize(Decimal('0.00000000'))
        assert str(expect) == str(result)
"""
2个坑未解决：
1.无限不循环小数断言 --->已解决（利用decimal的内置方法）
2.除数为0的异常捕获不到，报错提示 Failed: DID NOT RAISE <class 'ZeroDivisionError'> --->已解决（粗心导致）
"""