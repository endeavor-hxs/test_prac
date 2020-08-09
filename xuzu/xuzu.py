'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。
每次调用都会打印“罪过罪过”
'''
from tonglao.tonglao import TongLao
class XuZhu(TongLao):

    def __init__(self,hp,power):
    #继承父类的实例变量
        super().__init__(hp,power)

    def read(self):
        print("罪过罪过!")

    def fight(self):
        # 调用父类的变量进行比较综合量
        if self.composite > TongLao.enemy_composite :
            print("我赢了！！！")
        else:
            print("敌人赢了！！！")


f = XuZhu(10,10)

f.fight()