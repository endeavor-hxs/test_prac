"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""


def game():
    #我的血量1000
    my_hp = 1000
    # 我的能量200
    my_power = 200
    # 你的血量1000
    your_hp = 1000
    # 你的能量199
    your_power = 199

    while True:
        # 我的血量 = 我的血量-你的能量
        my_hp = my_hp - your_power
        # 你的血量= 你的血量- 我的能量
        your_hp = your_hp - my_power
        print(my_hp)
        if my_hp <= 0:
            print("我输了")
            break
        elif your_hp <= 0:
            print("你输了")
            break

#调用game函数
game()