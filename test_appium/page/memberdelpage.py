'''
删除成员页面
'''
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage


class MemberDeletePage(BasePage):
    del_member = (MobileBy.XPATH, '//*[@text="删除成员"]')
    click_access = (MobileBy.XPATH, '//*[@text="确定"]')
    del_mem = (MobileBy.XPATH, '//*[@text="删除成员"]')
    click_yes = (MobileBy.XPATH, '//*[@text="确定"]')

    def del_member(self):
        self.find_and_click(self.del_member)
        self.find_and_click(self.click_access)
        from test_appium.page.contactpage import ContactPage
        return ContactPage(self.driver)

    def del_mem(self):
        self.find_and_click(self.del_mem)
        self.find_and_click(self.click_yes)
        from test_appium.page.manage_member_page import ManageMember
        return ManageMember(self.driver)
