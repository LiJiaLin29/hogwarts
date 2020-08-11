"""
 @description: 描述蜡笔小新和小白去给妈妈买菜
 @auther: 29263
 @date: 2020-08-11 13:54
"""


# 功能描述: 小新具有姓名，年龄，幼儿园；拥有帮妈妈买东西技能
class Role:

    def __init__(self, name, age, kindergarten):
        self.name = name
        self.age = age
        self.kindergarten = kindergarten

    def walk_dog(self, dog, timestr):
        print(f"{timestr},我要带着{dog.name}去散步！！")

    def shop(self, money, *foods):
        print(f"妈妈还给了我{money}块,让我去超市买", foods)

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁，在{self.kindergarten}读一年级")


# 功能描述: 小白具有姓名
class Dog:

    def __init__(self, name):
        self.name = name


xiaoba = Dog("小白")
xiaoxin = Role("小新", 5, "双叶幼儿园")
xiaoxin.introduce()
xiaoxin.walk_dog(xiaoba, "今天下午3点半")
foods = ["白菜", "地瓜", "番茄"]
xiaoxin.shop(100, foods)