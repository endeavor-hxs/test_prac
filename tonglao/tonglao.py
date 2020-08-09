'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
1.see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，
“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，
打印“叛徒！我杀了你”

2.fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，
血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。
血多的一方获胜。
'''

class TongLao:
    #定义类变量
    enemy_hp = int(input("请输入敌人的血量（数字）:"))
    enemy_power = int(input("请输入敌人的能量（数字）:"))
    #综合量 = 武力*0.7 +血量*0.5
    enemy_composite =enemy_power * 0.7 + enemy_hp * 0.5

    def __init__(self,hp,power):
        #定义实例变量
        self.hp = hp
        self.power = power
        # 综合量 = 武力*0.7 +血量*0.5
        self.composite = power * 0.7 + hp * 0.5

    def see_people(self,name):
        # 定义方法传入name
        if name =="WYZ":
            print("师弟！！！！")
        elif name == '李冰水':
            print('呸，贱人!')
        elif name == '丁春秋':
            print('叛徒！我杀了你')


    def fight_zms(self):
        # 天山折梅手方法
        power = self.power*10
        hp = self.hp/2
        self.composite = power * 0.7 + hp * 0.5


    def fight(self):
        #判断综合量是否大于敌人的综合量
        if self.composite > TongLao.enemy_composite :
            print("我赢了！！！")
        else:
            print("敌人赢了！！！")


if __name__ == '__main__':
    TongLao(10,10)

