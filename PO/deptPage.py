"""
 @description: 部门页面(新增、编辑)
 @author: 29263
 @date: 2020-08-26 19:38
"""
from .basePage import BasePage
from selenium.webdriver.common.by import By
import time


class DeptPage(BasePage):

    def set_dept_name(self, name):
        # 输入部门名称
        self.find(By.NAME, "name").send_keys(name)

    def add_dept(self, name):
        """
        新增部门功能
        """
        self.set_dept_name(name)
        time.sleep(2)
        # 点击确定，提交部门信息
        self.find(By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck='submit']").click()

    def add_dept_with_null(self, name):
        """
        新增部门功能,输入空字符串
        """
        self.set_dept_name(name)
        time.sleep(2)
        # 点击确定，提交部门信息
        self.find(By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck='submit']").click()

    def add_dept_with_repeat(self, name):
        """
        新增部门功能,输入重复部门名称
        """
        self.set_dept_name(name)
        time.sleep(2)
        # 点击确定，提交部门信息
        self.find(By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck='submit']").click()
