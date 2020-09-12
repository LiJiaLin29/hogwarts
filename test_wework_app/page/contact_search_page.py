"""
 @description: 搜索成员信息页
 @author: 29263
 @date: 2020-09-09 12:50
"""
from test_wework_app.page.base_page import BasePage


class ContactSearchPage(BasePage):
    _file_path = BasePage.root_dir + "/resources/po_file/ContactAdd.yaml"
    loc = ("id", "com.tencent.wework:id/b10")

    def result_total_count(self):
        return len(self.finds(ContactSearchPage.loc))

