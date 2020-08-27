"""
 @description: 企业微信通讯录页
 @author: 29263
 @date: 2020-08-26 19:35
"""
from .basePage import BasePage
from .deptPage import DeptPage
from selenium.webdriver.common.by import By


class ContactsPage(BasePage):

    def goto_add_dept_by_tool(self, parent=None):
        """
        先选择指定名称部门，点击部门功能菜单，点击添加子部门菜单项
        :return: 返回添加部门页面
        """
        if parent is not None:
            self.select_dept(parent)

        self.find(By.CSS_SELECTOR, ".jstree-clicked").click()  #展开部门菜单树
        self.find(By.CSS_SELECTOR, ".jstree-clicked span").click()  # 再点击部门的功能菜单
        self.find(By.XPATH, "/html/body/ul/li[1]").click()  # 获取添加子部门菜单项
        return DeptPage(self._driver)

    def goto_add_dept(self, parent=None):
        """
        先选择指定名称部门，点击添加子部门链接
        :return: 返回添加部门页面
        """
        if parent is not None:
            self.select_dept(parent)

        self.find(By.CSS_SELECTOR, ".js_add_sub_party").click()  # 点击添加子部门链接
        return DeptPage(self._driver)

    def select_dept(self, name):
        """
        根据部门名称选中部门
        """
        self.find(By.LINK_TEXT, name).click()

    def get_dept_list(self):
        """
        获取所有部门名称
        :return: 返回列表
        """
        return self.finds(By.CSS_SELECTOR, ".member_colLeft_bottom .jstree-container-ul a")


