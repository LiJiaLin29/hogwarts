"""
 @description: 使用pytest+selenium webdirver
        实现企业微信功能点的自动化测试
 @auther: 29263
 @date: 2020-08-22 14:38
"""
import time, os
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.conftest import login_winxin


class TestWeiXin:

    def setup(self):
        """
        在测试前，创建出webdriver实例
        """
        # 页面加载策略，系统默认是html等待，就是等他加载完，直接设置成none，就是不等待
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        # 创建webdriver实例
        self.driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

    def teardown(self):
        """
        测试完成后，关闭浏览器标签页
        """
        self.driver.close()

    def test_import_contacts(self):
        """
        使用cookie 登录企业微信,完成导入联系人
        """
        # 调用login_winxin完成登录
        login_winxin(self.driver)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)
        # 获取导入通讯录UI元素
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 页面切换判断
        # 获取上传文件input控件
        filename = '学习.xlsx'
        btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "js_upload_file_input"))
        )
        btn.send_keys(os.path.abspath(f"./data/{filename}"))  # 使用sendkeys上传文件，必须是绝对路径
        # 显示等待,直到上传按钮标签名为重新上传
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "js_upload_label"), "重新上传")
        )

        # 获取页面上传文件名称
        temp = self.driver.find_element(By.ID, "upload_file_name").text
        time.sleep(2)
        assert temp == filename

