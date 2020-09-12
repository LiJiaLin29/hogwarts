"""
 @description: 通讯录-个人信息-信息设置页
 @author: 29263
 @date: 2020-09-12 1:35
"""
from test_wework_app.page.base_page import BasePage
from test_wework_app.page.contact_add_page import ContactAddPage


class ContactSettingPage(BasePage):
    _file_path = BasePage.root_dir + "/resources/po_file/ContactSetting.yaml"

    def click_edit_member(self):
        """
        点击编辑成员
        """
        self.step_load("click_edit_member", ContactSettingPage._file_path)
        return ContactAddPage(self.driver)