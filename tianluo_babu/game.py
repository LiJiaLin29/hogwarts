# TongLao属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
# see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，
# 如果传入“丁春秋”，打印“叛徒！我杀了你”
# fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合
# 制对打，打完之后，比较双方血量。血多的一方获胜。


class TongLao:

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, person_name):

        if person_name == "WYZ":
            print("师弟！！！！")
        elif person_name == "李秋水":
            print("呸，贱人")
        elif person_name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("......哪来的毛头小子")

    def fight_zms(self, enm_hp, enm_power):
        # 武力值瞬间提升10倍，血量缩减2倍
        self.power = self.power * 10
        self.hp = self.hp / 2
        print("使出一招天山折梅手~~")
        # 对打
        self.hp -= enm_power
        enm_hp -= self.power
        if self.hp > enm_hp:
            print("无敌了~~")
        elif self.hp == enm_hp:
            print("打成平手，点到为止~~")
        else:
            print("对手太强~~")


# 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
class XuZhu(TongLao):

    def see_people(self, person_name):

        if person_name == "WYZ":
            print("师父好")
        elif person_name == ("李秋水" or "TongLao"):
            print("师伯好")
        elif person_name == "乔峰":
            print("乔大哥，好久不见")
        elif person_name == "丁春秋":
            print("丁师伯，我会继承师父的遗愿，不会让出掌门之位的")
        else:
            print("......不认识")

    def read(self):
        print("罪过罪过")


print("武林大会开始，虚竹登场~~\n开始打招呼")
xz = XuZhu(1000, 80)
xz.see_people("WYZ")
xz.see_people("李秋水")
xz.see_people("丁春秋")
xz.see_people("乔峰")
xz.read()
print("虚竹开始战斗")
xz.fight_zms(500, 95)
print("天山童姥登场~~\n开始打招呼")
tl = TongLao(700, 70)
tl.see_people("WYZ")
tl.see_people("李秋水")
tl.see_people("丁春秋")
tl.see_people("乔峰")
tl.fight_zms(600, 100)
xz.read()
