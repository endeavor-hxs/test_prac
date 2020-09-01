'''
通讯录页面
'''
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage
from test_appium.page.manage_member_page import ManageMember
from test_appium.page.memberaddpage import AddMemberPage
from test_appium.page.memberdelpage import MemberDeletePage


class ContactPage(BasePage):
    add_mem = (MobileBy.XPATH, "//*[@text='添加成员']")
    click_op = (MobileBy.ID, "com.tencent.wework:id/hjz")
    edit_mem = (MobileBy.XPATH, "//*[@text='编辑成员']")
    click_to_man = (MobileBy.ID, "com.tencent.wework:id/hk4")
    search_mem = (MobileBy.ID, "com.tencent.wework:id/hk9")

    def go_to_add_member_page(self):
        self.find_and_click(self.add_mem)
        return AddMemberPage(self.driver)

    def click_member(self, name):
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']").click( )
        self.find_and_click(self.click_op)
        self.find_and_click(self.edit_mem)
        return MemberDeletePage(self.driver)

    def go_to_manage_contact(self):
        self.find_and_click(self.click_to_man)
        return ManageMember(self.driver)

    def search_member(self, name):
        self.find_and_click(self.search_mem)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        sear_mem_text = self.driver.find_element(MobileBy.XPATH, "//*[@text='无搜索结果']").text
        return sear_mem_text
