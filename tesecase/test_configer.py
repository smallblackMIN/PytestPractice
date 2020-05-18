import yaml
from func.Calc import Calc
import pytest
class TestDemo():
    def setup(self):
        self.calc = Calc()

    def getsteps(self,a,b,c,a1,b1,c1):
        '''
        测试步骤参数化
        '''
        self.getyaml = yaml.safe_load(open("test_steps.yaml"))
        for i in self.getyaml:
            if 'add' == i:
                # self.list = yaml.safe_load(open("./add_normal_data.yaml"))
                # assert self.calc.add(list[0],list[1]) == list[2]
                assert self.calc.add(a,b) == c
            elif 'div' == i:
                # self.list = yaml.safe_load(open("./div_normal_data.yaml"))
                # assert self.calc.div(list[0],list[1]) == list[2]
                assert self.calc.div(a1,b1) == c1

    @pytest.mark.parametrize(("a","b","c"),yaml.safe_load(open("./add_normal_data.yaml")))
    @pytest.mark.parametrize(("a1","b1","c1"),yaml.safe_load(open("./div_normal_data.yaml")))
    def calc_mix(self,a,b,c,a1,b1,c1):
        self.getsteps(a,b,c,a1,b1,c1)

