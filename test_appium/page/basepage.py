'''
基类页面,对于find_element,click,send_keys的封装
'''
from appium.webdriver.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click( )
