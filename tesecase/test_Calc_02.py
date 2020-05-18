from func.Calc import Calc
import pytest
import yaml


class Test_Calc_02():

    def setup(self):
        self.calc = Calc()
    @pytest.mark.parametrize(["a","b","c"], yaml.safe_load(open("add_normal_data.yaml")))
    def calc_add_normal(self,a,b,c):
        '''
        针对加法中正常数值的等价类用例
        :param a: 加数1
        :param b: 加数2
        :param c: 结果
        将数字类型划分为正整数，负整数，正浮点数，负浮点数，进行组合相加
        '''
        data = (a,b)
        assert round(self.calc.add(*data),1) == c
        # assert round(self.calc.add1(data)) == c

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open("add_error_data.yaml")))
    def calc_add_error(self,a,b,c):
        '''
        针对加法异常值的用例
        :param a: 加数1
        :param b: 加数2
        :param c: 结果
        设计了两个加数中存在不是数字类型的用例
        '''
        with pytest.raises(TypeError):  #捕获异常
            assert self.calc.add(a, b) == c

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./div_normal_data.yaml")))
    def calc_div_normal(self,a,b,c):
        '''
        针对div方法正常值的等价类用例
        :param a: 分子
        :param b: 分母
        :param c: 结果
        分子划分为：0，正数，负数，分母划分为：正数，负数
        '''
        assert round(self.calc.div(a, b), 1) == c

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./div_error_data.yaml")))
    def calc_div_error_01(self,a,b,c):
        '''
        针对div方法异常输入的等价类用例
        :param a: 分子
        :param b: 分母
        :param c: 结果
        分子分母中存在非数字类型的用例
        '''
        with pytest.raises(TypeError) as exc:    #捕获异常
            round(self.calc.div(a, b), 1)
            assert exc.type == c

    def calc_div_error_02(self):
        '''
        针对div方法中非法数字输入的用例，即分母为0的情况
        :return:
        '''
        with pytest.raises(ZeroDivisionError) as exc: #捕获异常
            self.calc.div(4,0)
            assert exc.type == ZeroDivisionError

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./sub_normal_data.yaml")))
    def calc_sub_normal(self,a,b,c):
        '''
        针对sub方法中正常值的用例
        :param a: 被减数
        :param b: 减数
        :param c: 结果
        被减数和减数分为以下几个等价类：正整数，负整数，正浮点数，负浮点数
        1、正整数相减
        2、正整数减负整数
        3、负整数相减
        4、正浮点数相减
        5、负浮点数相减
        '''
        assert round(self.calc.sub(a, b), 1) == c

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./sub_error_data.yaml")))
    def calc_sub_error(self,a,b,c):
        '''
        针对sub方法进行异常值检查，针对输入为非数字类型的测试数据进行检测
        :param a: 被减数
        :param b: 减数
        :param c: 结果
        '''
        with pytest.raises(TypeError):  #捕获异常
            assert self.calc.sub(a, b) == c

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./mul_normal_data.yaml")))
    def calc_mul_normal(self,a,b,c):
        '''
        针对mul方法中正常值的用例
        :param a: 乘数1
        :param b: 乘数2
        :param c: 结果
        被减数和减数分为以下几个等价类：正整数，负整数，正浮点数，负浮点数,0
        1、正整数相乘
        2、正整数乘负整数
        3、负整数相乘
        4、正浮点数相乘
        5、负浮点数相乘
        6、正浮点乘以负浮点
        7、乘数中存在一个0
        8、乘数均为0
        '''
        assert round(self.calc.mul(a, b), 2) == c

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./mul_error_data.yaml")))
    def calc_mul_error(self,a,b,c):
        '''
        针对mul方法进行异常值检查，针对输入为非数字类型的测试数据进行检测
        :param a: 乘数1
        :param b: 乘数2
        :param c: 结果
        '''
        with pytest.raises(TypeError):  #捕获异常
            assert self.calc.mul(a, b) == c


if __name__ == '__main__':
    pytest.main(["-m"],["add"],["test_Calc_02.py"])
    # pytest.main('-m div test_Calc_02.py')