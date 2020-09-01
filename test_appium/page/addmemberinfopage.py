'''
添加成员信息填写页面
'''
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage


class AddMemberInfo(BasePage):

    def input_member_info(self, name, gender, phonenum):
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click( )
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click( )
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click( )

        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='设置部门']").click( )
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g_3").click( )
        self.driver.implicitly_wait(3)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click( )
        from test_appium.page.memberaddpage import AddMemberPage
        return AddMemberPage(self.driver)
