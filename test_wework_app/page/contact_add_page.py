"""
 @description: 添加成员信息页
 @author: 29263
 @date: 2020-09-09 12:50
"""
from test_wework_app.page.base_page import BasePage


class ContactAddPage(BasePage):
    _file_path = BasePage.root_dir + "/resources/po_file/ContactAdd.yaml"

    def set_name(self, name):
        # 输入姓名
        self._param_list["name"] = name

    def set_sex(self, sex):
        # 输入性别
        self._param_list["sex"] = sex

    def set_mobile(self, mobile):
        # 输入性别
        self._param_list["mobile"] = mobile

    def input_member(self):
        self.step_load("input_member", ContactAddPage._file_path)
        return self

    def click_save(self):
        self.step_load("click_save", ContactAddPage._file_path)

    def click_delete(self):
        self.step_load("click_delete", ContactAddPage._file_path)