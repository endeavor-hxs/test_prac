'''
app类：包含应用的启动，关闭，重启，页面跳转等
'''
from test_appium.page.messagepage import MessagePage
from appium import webdriver
from test_appium.page.basepage import BasePage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app( )
        return self

    def restart(self):
        self.driver.close_app( )
        self.driver.launch_app( )

    def stop(self):
        self.driver.quit( )

    def go_to_messagepage(self):
        return MessagePage(self.driver)
