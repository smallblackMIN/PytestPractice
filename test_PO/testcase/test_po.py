import pytest

from test_PO.page.main import Main


class TestPo():
    # @pytest.mark.skip
    def test_add_member(self):
        '''
        测试添加成员是否成功
        :return:
        '''
        main = Main()
        assert '虞书欣' in main.goto_add_member().add_member().get_members()
    # @pytest.mark.skip
    def test_set_department(self):
        '''
        判断设置部门是否生效
        :return:
        '''
        main = Main()
        assert '舞蹈部' in main.goto_edit_contact().set_department()