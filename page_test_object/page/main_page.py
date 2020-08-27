from selenium.webdriver.common.by import By
from page_test_object.page.base_page import BasePage
from page_test_object.page.contact_page import ContactPage


class MainPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame"
    _contacts = (By.ID, "menu_contacts")

    def go_to_contact(self):
        self.find(*self._contacts).click( )
        return ContactPage(self.driver)
