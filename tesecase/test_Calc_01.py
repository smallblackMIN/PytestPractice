from func.Calc import Calc
import pytest
import yaml
'''
@用例设计思路
1、针对add(),对输入内容类型做区分：正整数，负整数，正浮点数，负浮点数，非法类型
2、针对div(),将除数和被除数分开，除数等价划分为：正数，负数，0，非法类型；被除数等价划分为：0，正数，负数，非法类型
'''
class Test_Calc_01:

    def setup(self):
        self.calc = Calc()
    @pytest.mark.parametrize(["a","b","c"], yaml.safe_load(open("add_normal_data.yaml")))
    def test_add_normal(self,a,b,c):
        '''
        针对加法中正常数值的等价类用例
        :param a: 加数1
        :param b: 加数2
        :param c: 结果
        将数字类型划分为正整数，负整数，正浮点数，负浮点数，进行组合相加
        '''
        data = (a,b)
        assert round(self.calc.add(*data),1) == c
        assert round(self.calc.add1(data)) == c

    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open("add_error_data.yaml")))
    def test_add_error(self,a,b,c):
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
    def test_div_normal(self,a,b,c):
        '''
        针对div方法正常值的等价类用例
        :param a: 分子
        :param b: 分母
        :param c: 结果
        分子划分为：0，正数，负数，分母划分为：正数，负数
        '''
        assert round(self.calc.div(a, b), 1) == c

    @pytest.mark.parametrize(["a","b","c"],yaml.safe_load(open("./div_error_data.yaml")))
    def test_div_error_01(self,a,b,c):
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

    def test_div_error_02(self):
        '''
        针对div方法中非法数字输入的用例，即分母为0的情况
        :return:
        '''
        with pytest.raises(ZeroDivisionError) as exc: #捕获异常
            self.calc.div(4,0)
            assert exc.type == ZeroDivisionError



if __name__ == '__main__':
    pytest.main()

