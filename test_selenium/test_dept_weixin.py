"""
 @description: 测试部门模块功能
 @author: 29263
 @date: 2020-08-27 12:51
"""
from PO.contactsPage import ContactsPage
from PO.homePage import HomePage
from selenium.webdriver.common.by import By
from random import randint


class TestDept:

    def setup(self):
        # 初始化主页
        self.homePage = HomePage()
        # 新增部门名称
        self.dept_name = "部门一"

    def teardown(self):
        self.homePage.close()

    def test_add_dept_by_menu(self):
        """
        通过部门的菜单添加部门
        """
        self.homePage.goto_contacts_by_menu().goto_add_dept_by_tool().add_dept(self.dept_name)
        # 获取部门列表信息，判断是否添加成功
        assert self.dept_name in ContactsPage().get_dept_list()

    def test_add_dept(self):
        """
        通过添加子部门链接添加部门
        """
        self.homePage.goto_contacts_by_menu().goto_add_dept().add_dept(self.dept_name)
        # 获取部门列表信息，判断是否添加成功
        assert self.dept_name in ContactsPage().get_dept_list()

    def test_add_dept_fail1(self):
        """
        部门信息输入为空
        """
        self.homePage.goto_contacts_by_menu().goto_add_dept().add_dept_with_null("  ")
        # 判断是否显示信息提示框
        assert self.homePage.is_visible(By.ID, "js_tips")
        # 判断提示内容是否正确
        assert self.homePage.text_present(By.ID, "js_tips", "请输入部门名称")

    def test_add_dept_fail2(self):
        """
        输入重复部门信息
        """
        self.homePage.goto_contacts_by_menu()  # 跳转到通讯录页面
        dlist = ContactsPage(self.homePage._driver).get_dept_list()  # 获取页面中所有的部门信息
        # 随机取其中的一个部门
        name = dlist[randint(0, len(dlist)-1)]
        self.homePage.goto_contacts_by_menu().goto_add_dept().add_dept_with_null(name)
        # 判断是否显示信息提示框
        assert self.homePage.is_visible(By.ID, "js_tips")
        # 判断提示内容是否正确
        assert self.homePage.text_present(By.ID, "js_tips", "该部门已存在")




