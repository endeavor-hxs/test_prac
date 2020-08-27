from selenium.webdriver.common.by import By

from page_test_object.page.base_page import BasePage


class AddDeaprtMember(BasePage):
    _name = (By.XPATH, "//input[@name='name']")
    _inputname = (By.XPATH, "//input[@name='name']")
    _partname = (By.CSS_SELECTOR, ".js_parent_party_name")
    _form_sele = (By.CSS_SELECTOR, ".form li:nth-child(1)")
    _dialog = (By.XPATH, '//div[@class="qui_dialog_foot ww_dialog_foot"]/a[1]')

    def add_depart_member(self, com_name):
        from page_test_object.page.contact_page import ContactPage
        self.driver.implicitly_wait(5)
        self.find(*self._name).click( )
        self.find(*self._inputname).send_keys(com_name)
        self.find(*self._partname).click( )
        self.find(*self._form_sele).click( )
        self.find(*self._dialog).click( )

        return ContactPage(self.driver)

    def get_error_mess(self):
        error_mess = self.driver.find_element(By.XPATH, '//div[@id="js_tips"]').text
        return error_mess
