"""
 @description: 测试联系人添加、删除等功能
 @author: 29263
 @date: 2020-09-09 12:54
"""
import pytest
from test_wework_app.page.App import App
from test_wework_app.testcase.conftest import yaml_data_load
from test_wework_app.testcase.data import data_path


class TestContacts:

    def setup_class(self):
        """
        启动应用
        """
        self.main = App.start()

    def teardown_class(self):
        App.stop()

    def teardown(self):
        self.main.back()

    @pytest.mark.parametrize(*yaml_data_load("add_contact_list", data_path+"/TestContacts.yaml"))
    def test_add_contact(self, name, sex, mobile):
        """
        添加成员
        :return:
        """
        # 进入添加成员页
        p = self.main.goto_contacts().click_add_member().click_add_manual()
        # 输入填写的成员信息
        p.set_name(name)
        p.set_sex(sex)
        p.set_mobile(mobile)
        p.input_member().click_save()  # 填写信息并保存

        assert "添加成功" == p.get_toast_text()

    @pytest.mark.parametrize(*yaml_data_load("delete_by_name", data_path+"/TestContacts.yaml"))
    def test_delete_by_name(self, name):
        """
        删除指定用户名成员
        :return:
        """
        # 通过姓名搜索用户数目
        contact_page = self.main.goto_contacts()
        start_count = contact_page.search(name).result_total_count()
        if start_count == 0:  # 没有该用户
            return
        self.main.back()  # 返回通讯录页
        contact_page.click_member(name).click_menu().click_edit_member().click_delete()
        # 删除操作后，再次搜索用户
        end_count = contact_page.search(name).result_total_count()

        assert start_count == (end_count + 1)





