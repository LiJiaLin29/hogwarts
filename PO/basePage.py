"""
 @description: 父类定义，包括一些公共方法find,driver实例
 @author: 29263
 @date: 2020-08-26 19:07
"""
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver=None):
        # 判断是否传入driver实例，保证driver在项目中是单例
        if driver is None:
            # 页面加载策略，系统默认是html等待，就是等他加载完，直接设置成none，就是不等待
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities["pageLoadStrategy"] = "none"
            # 复用浏览器
            option = Options()
            option.debugger_address = "localhost:9222"
            driver = webdriver.Chrome(desired_capabilities=desired_capabilities, options=option)
            # 窗口最大化
            driver.maximize_window()
            if self._base_url != "":
                driver.get(self._base_url)
        self._driver = driver

    def find(self, *locator):
        """
        查找单个元素，封装selenium的自带方法，增强可维护性
        :param locator: 定位信息
        :return: 元素对象
        """
        # 隐式等待
        elem = WebDriverWait(self._driver, 15).until(
            EC.element_to_be_clickable(locator)
        )
        print("取得元素", *locator)
        return elem

    def finds(self, *locator):
        """
        查找多个元素，封装selenium的自带方法，增强可维护性
        :param locator: 定位信息
        :return: 元素对象
        """
        elems = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_all_elements_located(locator)
        )
        dlist = []
        for i in elems:
            dlist.append(i.text)
        return dlist

    def is_visible(self, *locator):
        """
        判断元素是否可见
        """
        return EC.visibility_of_element_located(locator)

    def text_present(self, *locator, message=""):
        """
        判断元素是否包含文本
        """
        return EC.text_to_be_present_in_element(locator, message)


    def close(self):
        self._driver.close()
