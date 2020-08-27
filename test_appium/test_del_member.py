from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDelMember:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit( )

    def test_del_member(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click( )
        self.driver.find_element(MobileBy.XPATH, "//*[@text='测试001']").click( )
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click( )
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click( )
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click( )
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click( )
