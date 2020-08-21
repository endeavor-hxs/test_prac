'''
企业微信上传文件
'''
import shelve

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class TestWechat:
    def setup(self):
        self.driver = webdriver.Chrome( )
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit( )

    def test_get_cookie(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(5)
        # cookies = self.driver.get_cookies()
        # print(cookies)

        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688852027743033'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'lZmVEf2jwTyKLpWojE8Ha8ZbHoz12zWjbrWOCQhrLq-SOIdYO2SK2iN6A-F_jU4AtByB628fr33YjMmLD2StCTfD3NcRqfFzLLgOxELR1CgDayI_puIUe8AIFvjJPpTQXn3gRnEKdngGwjpoF6AeGBwuREkPPpg1EY4ED74tzqStXIw2UXKGOCY6DRSsuyPn7RalkeONib_SnhoGt6IIcCevGCDQjnDCKggcNula0uWlX8dMg7Sf3dhupwmzZPdVMQYawzMUQ7XO6i-jxoLlug'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688852027743033'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325124158386'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1505818'},
            {'domain': '.qq.com', 'expiry': 1598064615, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.899833321.1597978212'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598009744, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '4poh5od'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '19314102893008936'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'o6vpJ9nqtg1HuEvkf24Q5ZuOVr9olzJhobd2DCgm9JsQ6CTwEz1_bcrDLGQQUBsC'},
            {'domain': '.qq.com', 'expiry': 1597978271, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1661050215, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1346505928.1597978212'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629514208, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600570215, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'}]

        for cookie in cookies:
            if 'expiry' in cookie.keys( ):
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)  # 添加cookie

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)
        self.driver.find_element(By.ID, "menu_contacts").click( )

    def test_upload(self):
        db = shelve.open("dbdata")
        cookies = db['cookie']
        db.close( )
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys( ):
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)  # 添加cookie

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click( )

        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("./test.xlsx")
        assert "test.xlsx" == self.driver.find_element(By.ID, "upload_file_name").text
