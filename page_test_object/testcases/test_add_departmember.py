from page_test_object.page.add_department_page import AddDeaprtMember
from page_test_object.page.main_page import MainPage


class TestAddDepartMember:

    def setup_class(self):
        self.main = MainPage( )

    def test_add_depart_member(self):
        result = self.main.go_to_contact( ).go_to_add_department( ).add_depart_member("测试员001").get_add_member_status( )
        assert result == "新建部门成功"

    def test_add_depart_member_fail(self):
        self.main.go_to_contact( ).go_to_add_department( ).add_depart_member(" ")
        result2 = AddDeaprtMember(self.main.driver).get_error_mess( )
        assert result2 == "请输入部门名称"
