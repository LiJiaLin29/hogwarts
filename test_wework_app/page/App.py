"""
 @description: app常用的方法，包括：启动、关闭,测试用例执行的入口
 @author: 29263
 @date: 2020-09-09 11:13
"""
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from test_wework_app.page.main_page import MainPage


class App:
    driver: WebDriver = None
    _package = "com.tencent.wework"
    _activity = ".launch.LaunchSplashActivity"
    @classmethod
    def start(cls):
        # 初始化driver
        caps = {
            'platformName': 'Android',
            'platformVersion': '6.0.1',  # 填写android虚拟机的系统版本
            'deviceName': 'MuMu',  # 填写安卓虚拟机的设备名称
            'appPackage': cls._package,  # 填写被测试包名
            'appActivity': cls._activity,  # 填写被测试app入口
            'udid': '127.0.0.1:7555',  # 填写通过命令行 adb devices 查看到的 uuid
            'autoLaunch': False,  # 跳过安装
            'automationName': 'uiautomator2',  # 识别Toast内容
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        cls.driver.implicitly_wait(8)
        cls.driver.launch_app()

        return MainPage(cls.driver)

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.start()
        return cls.driver

    @classmethod
    def stop(cls):
        cls.driver.quit()

    @classmethod
    def restart(cls):
        cls.stop()
        cls.driver.start_activity(cls._package, cls._activity)
