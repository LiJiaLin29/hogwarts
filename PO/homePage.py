"""
 @description: 企业微信index页
 @author: 29263
 @date: 2020-08-26 19:07
"""
from .basePage import BasePage
from .contactsPage import ContactsPage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contacts_by_menu(self):
        """
        点击菜单栏的通讯录链接
        :return: 返回通讯录页面
        """
        self.find(By.ID, "menu_contacts").click()
        return ContactsPage(self._driver)

