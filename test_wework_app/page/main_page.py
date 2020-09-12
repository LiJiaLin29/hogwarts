"""
 @description: 企业微信首页
 @author: 29263
 @date: 2020-09-09 10:18
"""
from test_wework_app.page.address_list_page import AddressListPage
from test_wework_app.page.base_page import BasePage


class MainPage(BasePage):
    _file_path = BasePage.root_dir + "/resources/po_file/Main.yaml"

    def goto_contacts(self):
        self._param_list["text"] = "通讯录"
        self.step_load("goto_contacts", MainPage._file_path)
        return AddressListPage(self.driver)
