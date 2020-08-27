from selenium.webdriver.common.by import By
from page_test_object.page.add_department_page import AddDeaprtMember
from page_test_object.page.base_page import BasePage


class ContactPage(BasePage):
    _member = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _create = (By.CSS_SELECTOR, ".js_create_party")
    _add_mem = (By.XPATH, '//div[@id="js_tips"]')

    def go_to_add_department(self):
        self.find(*self._member).click( )
        self.find(*self._create).click( )
        return AddDeaprtMember(self.driver)

    def get_add_member_status(self):
        text_mess = self.find(*self._add_mem).text
        return text_mess
