"""
 一个多回合制游戏，每个角色都有hp(血量)和power(攻击力)
 规则：1.hp的初始值为1000，power的初始值为200
      2.打斗多个回合，直到一方血量为0
"""
my_hp, enemy_hp = 1000 #血量
my_power, enemy_power = 200 #攻击力

# 打斗函数
def fight():

    while True:
        # 双方互相攻击
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        # 判断游戏是否结束
        if my_hp > 0 and enemy_hp <= 0:
            print("我赢了");break;
        elif my_hp = 0 and enemy_hp = 0:
            print("打成平手");break;
        elif my_hp <= 0 and enemy_hp > 0
            print("敌方赢了");break;

# 调用函数
fight()




