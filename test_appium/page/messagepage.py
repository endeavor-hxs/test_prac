'''
首页：消息页
'''
from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.basepage import BasePage
from test_appium.page.contactpage import ContactPage


class MessagePage(BasePage):
    click_contact = (MobileBy.XPATH, "//*[@text='通讯录']")

    def go_to_contact(self):
        self.find_and_click(self.click_contact)
        return ContactPage(self.driver)
