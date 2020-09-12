"""
 @description: 邀请成员页面
 @author: 29263
 @date: 2020-09-09 12:44
"""
from test_wework_app.page.base_page import BasePage
from test_wework_app.page.contact_add_page import ContactAddPage


class MemberInvitePage(BasePage):
    _file_path = BasePage.root_dir + "/resources/po_file/MemberInvite.yaml"

    def click_add_manual(self):
        """
        点击手动添加成员
        """
        self.step_load("click_add_manual", MemberInvitePage._file_path)
        return ContactAddPage(self.driver)
