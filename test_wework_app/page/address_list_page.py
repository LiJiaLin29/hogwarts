"""
 @description: 通讯录tab页面
 @author: 29263
 @date: 2020-09-09 11:27
"""
from test_wework_app.page.base_page import BasePage
from test_wework_app.page.contact_detail_page import ContactDetailPage
from test_wework_app.page.contact_search_page import ContactSearchPage
from test_wework_app.page.member_invite_page import MemberInvitePage


class AddressListPage(BasePage):
    _file_path = BasePage.root_dir + "/resources/po_file/AddressList.yaml"

    def click_add_member(self):
        """
        点击添加成员
        """
        self.step_load("click_add_member", AddressListPage._file_path)
        return MemberInvitePage(self.driver)

    def click_member(self, name):
        """
        点击用户
        """
        self._param_list["name"] = name
        self.step_load("click_member", AddressListPage._file_path)
        return ContactDetailPage(self.driver)

    def search(self, name):
        """
        搜索用户
        """
        self._param_list["name"] = name
        self.step_load("search", AddressListPage._file_path)
        return ContactSearchPage(self.driver)