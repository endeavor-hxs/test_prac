'''
添加成员页
'''
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage


class AddMemberPage(BasePage):
    input_add = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def add_member(self):
        self.find_and_click(self.input_add)
        from test_appium.page.addmemberinfopage import AddMemberInfo
        return AddMemberInfo(self.driver)

    def get_toast(self):
        self.driver.implicitly_wait(5)
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toasttext
