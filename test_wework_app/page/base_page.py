"""
 @description: 
 @author: 29263
 @date: 2020-09-09 13:14
"""
import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import os

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _param_list = {}  # 替换参数变量字典
    _select_list = {}  # 选择框的值
    black_list = []
    driver: WebDriver = None
    ERR_COUNT = 0
    MAX_COUNT = 5
    # 测试模块根路径
    root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def __init__(self, driver=None):
        if self.driver is None:
            self.driver = driver

    def find(self, complex: dict):
        """
        查找UI元素并点击
        :param complex: list列表类型的定位条件[by:value,by:value2]，支持uiautomator组合定位
        """
        # 判断是否为滚动查找
        if "scroll" in complex.keys():
            return self.scroll_find(complex["scroll"])
        # 使用组合定位，遍历定位条件
        if "parent" in complex.keys():
            str_express = (f'new UiSelector().textContains("{complex["parent"]}").'
                           f'fromParent({self.find_me(complex)})')
        else:
            str_express = self.find_me(complex)
        try:
            # print(str_express)
            return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, str_express)
        except Exception as e:
            # 处理弹窗
            self.ERR_COUNT += 1
            if self.ERR_COUNT >= self.MAX_COUNT:  # 最大查找次数
                raise e
            for black in self.black_list:
                elem = self.driver.find_elements(*black)
                if elem:
                    elem[0].click()
                    self.ERR_COUNT = 0
            return self.find(complex)

    def find_me(self, complex=None):
        # 根据属性获取定位条件表达式
        str_list = ["new UiSelector()"]
        if "id" in complex.keys():
            str_list.append(f'resourceId("{complex["id"]}")')
        if "text" in complex.keys():
            text: str = complex["text"]
            # 定位文本如果从python传入,文本替换
            for param in self._param_list.keys():
                if text.find('${' + param + '}') >= 0:  # 查找到替换的字段
                    text = text.replace('${' + param + '}', self._param_list[param])
                    break
            str_list.append(f'text("{text}")')
        if "class" in complex.keys():
            str_list.append(f'className("{complex["class"]}").instance(0)')
        return ".".join(str_list)

    def scroll_find(self, text):
        """
        滚动查找文本
        """
        # 定位文本如果从python传入,文本替换
        for param in self._param_list.keys():
            if text.find('${' + param + '}') >= 0:  # 查找到替换的字段
                text = text.replace('${' + param + '}', self._param_list[param])
                break
        loc = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).' \
            f'scrollIntoView(new UiSelector().textContains("{text}").instance(0))'
        try:
            # print(loc)
            elem = WebDriverWait(self.driver, 5). \
                until(expected_conditions.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR, loc)))
            return elem
        except Exception as e:
            # 处理弹窗
            self.ERR_COUNT += 1
            if self.ERR_COUNT >= self.MAX_COUNT:  # 最大查找次数
                raise e
            for black in self.black_list:
                elem = self.driver.find_elements(*black)
                if elem:
                    elem[0].click()
                    self.ERR_COUNT = 0
            return self.scroll_find(text)

    def finds(self, loc) -> list:
        """
        根据id查找多个元素
        """
        try:
            return self.driver.find_elements(*loc)
        except Exception as e:
            # 处理弹窗
            self.ERR_COUNT += 1
            if self.ERR_COUNT >= self.MAX_COUNT:  # 最大查找次数
                raise e
            for black in self.black_list:
                elem = self.driver.find_elements(*black)
                if elem:
                    elem[0].click()
                    self.ERR_COUNT = 0
            return self.finds(loc)

    def send(self, obj: WebElement, value):
        try:
            obj.send_keys(value)
        except Exception as e:
            self.ERR_COUNT += 1
            if self.ERR_COUNT >= self.MAX_COUNT:
                raise e
            for black in self.black_list:
                elem = self.driver.find_elements(*black)
                if elem:
                    elem[0].click()
                    self.ERR_COUNT = 0
            return self.send(obj, value)

    def get_toast_text(self):
        """
        获取页面上的toast消息
        :return:
        """
        toast = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((MobileBy.XPATH,
                                                             "//*[@class='android.widget.Toast']"))
        )
        return toast.text

    def step_load(self, method, file_path=None):
        """
        加载测试步骤数据文件
        :param method: page object方法名
        :param file_path: po测试步骤文件路径
        """
        with open(file_path, encoding='utf-8') as f:
            steps: dict[list[dict]] = yaml.safe_load(f)
            if method in steps.keys():  # 执行po方法具体内容
                for item in steps[method]:  # 遍历列表
                    if "by" in item.keys():
                        elem = self.find(item["by"])
                    if "click" in item.keys():
                        elem.click()
                    elif "send" in item.keys():
                        content: str = item["send"]
                        # print("name:", content)
                        # 使用实际传入参数替换文件中的${param}
                        for param in self._param_list.keys():
                            if content.find('${' + param + '}') >= 0:  # 查找到替换的字段
                                content = content.replace('${' + param + '}', str(self._param_list[param]))
                                break
                        # print("name:", content)
                        elem.send_keys(content)
            else:
                raise Exception("No such method in po-file")

    def back(self):
        self.driver.back()
