from decimal import *


class Calculator:
    def add(self, a, b):
        """
        实现加法运算
        :param a: 加数
        :param b: 加数
        :return: 两个加数的和
        """
        if not isinstance(a, (int, float)):
            raise Exception(f'must be int or float: {a}')
        if not isinstance(b, (int, float)):
            raise Exception(f'must be int or float: {b}')
        add_result = Decimal(str(a)) + Decimal(str(b))
        return str(add_result)

    def div(self, a, b):
        """
        实现除法运算
        :param a: 被除数
        :param b: 除数
        :return: 被除数除以除数的商
        """
        if not isinstance(a, (int, float)):
            raise Exception(f'must be int or float: {a}')
        if not isinstance(b, (int, float)):
            raise Exception(f'must be int or float: {a}')
        if b != 0:
            div_result = Decimal(str(a)) / Decimal(str(b))
        else:
            raise ZeroDivisionError(f'除数不能为0: 除数={b}')
        return str(div_result)

if __name__ == '__main__':
    calc = Calculator()


