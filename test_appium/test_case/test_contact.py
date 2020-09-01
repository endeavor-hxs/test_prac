'''
测试用例
'''
import pytest
from test_appium.page.app import App


class TestContact:
    def setup(self):
        self.app = App( )
        self.main = self.app.start( ).go_to_messagepage( )

    def teardown(self):
        self.app.stop( )

    @pytest.mark.parametrize('name,gender,phonenum', [("张三", "男", "13033333333")])
    def test_add_contact(self, name, gender, phonenum):
        add_cont = self.main.go_to_contact( ).go_to_add_member_page( ).add_member( ).input_member_info(name, gender,
                                                                                                       phonenum) \
            .get_toast( )
        assert '添加成功' == add_cont

    @pytest.mark.parametrize('name', ["张三"])
    def test_del_contact(self, name):
        '''
        第一种方式删除成员
        :return:搜索结果
        '''
        del_mem = self.main.go_to_contact( ).click_member(name).del_member( ).search_member(name)
        assert '无搜索结果' == del_mem

    @pytest.mark.parametrize('name', ["张三"])
    def test_man_todel_contact(self, name):
        '''
        采用第二种方式删除成员
        :return:搜索结果
        '''
        del_man_contact = self.main.go_to_contact( ).go_to_manage_contact( ).go_to_memberdelpage(name) \
            .del_mem( ).close_manage_page( ).search_member(name)
        assert '无搜索结果' == del_man_contact
