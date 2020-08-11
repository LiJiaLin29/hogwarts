"""
 @description: 描述小猫
 @auther: 29263
 @date: 2020-08-11 12:37c
"""


# 功能描述: 小猫具有姓名，月份，品种；拥有捉老鼠，跳高技能
class Cat:

    def __init__(self, name, month, breed):
        self.name = name
        self.month = month
        self.breed = breed

    def catch_mice(self):
        print("帮主人抓老鼠")

    def jump(self, hight=1):
        print(f"爬屋顶，因为我能跳到{hight}米高")

    def introduce(self):
        print(f"我叫{self.name}，是一只{self.month}个月大的{self.breed}\n我的技能是：")
        self.catch_mice()
        self.jump()


cat = Cat("米老鼠", 10, "中华田园猫")
cat.introduce()
