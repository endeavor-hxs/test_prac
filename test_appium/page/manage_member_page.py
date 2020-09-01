'''
管理通讯录页面
'''
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.memberdelpage import MemberDeletePage
from test_appium.page.basepage import BasePage


class ManageMember(BasePage):
    click_close = (MobileBy.ID, "com.tencent.wework:id/hjz")

    def go_to_memberdelpage(self, name):
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{name}']").click( )
        return MemberDeletePage(self.driver)

    def close_manage_page(self):
        self.find_and_click(self.click_close)
        self.driver.implicitly_wait(5)
        from test_appium.page.contactpage import ContactPage
        return ContactPage(self.driver)
