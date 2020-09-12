"""
 @description: 通讯录-个人信息页
 @author: 29263
 @date: 2020-09-12 1:35
"""
from test_wework_app.page.base_page import BasePage
from test_wework_app.page.contact_setting_page import ContactSettingPage


class ContactDetailPage(BasePage):
    _file_path = BasePage.root_dir + "/resources/po_file/ContactDetail.yaml"

    def click_menu(self):
        """
        点击隐藏菜单
        """
        self.step_load("click_menu", ContactDetailPage._file_path)
        return ContactSettingPage(self.driver)