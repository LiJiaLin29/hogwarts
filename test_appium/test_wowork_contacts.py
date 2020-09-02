"""
 @description: 测试通讯录功能
 @author: 29263
 @date: 2020-09-01 15:46
"""
import pytest
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestContacts:

    def setup(self):
        # 连接参数
        caps = {
            'platformName': 'Android',
            'platformVersion': '6.0.1',  # 填写android虚拟机的系统版本
            'deviceName': 'MuMu',  # 填写安卓虚拟机的设备名称
            'appPackage': 'com.tencent.wework',  # 填写被测试包名
            'appActivity': '.launch.LaunchSplashActivity',  # 填写被测试app入口
            'udid': '127.0.0.1:7555',  # 填写通过命令行 adb devices 查看到的 uuid
            'automationName': 'uiautomator2',  # 识别Toast内容
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeyboard': True,
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.window_size = self.driver.get_window_size()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name', ['布布'])
    def test_del_by_name(self, name):
        """
        根据用户名删除联系人
        1.进入通讯录页面
        2.查找用户
        """
        # 点击通讯录tab键，找到ViewGroup的第二个RelativeLayout（通讯录tab）
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().resourceId("com.tencent.wework:id/h54").'
                                 'childSelector(new UiSelector().className("android.widget.RelativeLayout").index(1))').click()
        # 循环删除用户
        while True:
            # 在通讯录页面查找联系人，然后点击进入个人信息页
            elems = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,
                                              'new UiSelector().resourceId("com.tencent.wework:id/hqr").'
                                              'className("android.view.ViewGroup").'
                                              'childSelector(new UiSelector().className("android.widget.TextView"))')
            contact = None  # 联系人
            for i in range(2, len(elems)-1):  # 不包括外部联系人、自己和添加成员元素
                print(elems[i].text)
                if elems[i].text == name:
                    print("查找到", elems[i].text)
                    contact = elems[i]
                    break
            if contact is None:  # 删除完毕
                print("删除完毕")
                break
            # 点击用户，进入个人信息页
            contact.click()
            # 点击隐藏图标，进入信息隐藏页
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.wework:id/hjz")').click()
            # 点击编辑成员按钮，进入信息编辑页
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.wework:id/b53")').click()
            # 计算滑动起止坐标
            x = self.window_size['width'] * 0.5
            start_y = self.window_size['height'] * 0.9
            end_y = self.window_size['height'] * 0.2

            # 滑动屏幕到底部
            self.driver.swipe(x, start_y, x, end_y, duration=200)
            # 点击删除成员按钮
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.wework:id/e_1")').click()
            # 在弹窗中点击确定
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.wework:id/bfe").text("确定")').\
                click()
            # 显式等待删除完成，通讯录列表页面
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,
                                                             'new UiSelector().resourceId("com.tencent.wework:id/hqr")'))
            )

        # 通过搜索功能，断言是否删除成功
        serach_icon = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.wework:id/hk9")')
        if serach_icon.is_enabled():
            serach_icon.click()  # 点击搜索按钮
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,  # 向搜索栏输入姓名
                                     'new UiSelector().className("android.widget.EditText")').send_keys(name)
            time.sleep(1)
            group = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,  # 定位企业通讯录组名（包括：群聊、企业通讯录等）
                                              'new UiSelector().className("android.widget.ListView").childSelector('
                                              'new UiSelector().className("android.widget.RelativeLayout")).'
                                              'childSelector(new UiSelector().className("android.widget.TextView").text("企业通讯录"))')
            print("用户组：", group)
            if not len(group):  # 没有企业通讯录组，否则，查找元素
                assert True
            else:
                result = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.wework:id/e54").'
                f'childSelector(new UiSelector().text("{name}"))')
                assert result is None











