'''
用类和面向对象的思想，“描述”生活中任意接触到的东西
（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
'''

class Mountain:
    #定义类变量
    zds = "张东升"
    zzy = "朱朝阳"
    yl = "闫良"
    pp = "普普"
    def __init__(self):
        #定义实例变量
        self.parents = "岳父母"
        self.climb = "一起去爬山！"
        self.top = "爬到山顶"
        self.chance = "你看我还有机会嘛？"
        self.photo = "我帮你拍照,怎么样？"

    #定义方法
    def zhangdongsheng(self):
        #使用字面插值
        print(f'{Mountain.zds} 和 {self.parents}')
        #打印实例变量
        print(self.climb)
        print(self.top)
        print(f'{Mountain.zds}问{self.parents}{self.chance}')
        print("==========================")
    def zhuzhaoyang(self):

        print(f'{Mountain.zzy}和{Mountain.yl},{Mountain.pp}')
        print(self.climb)
        print(self.top)
        print(self.photo)
        print("=================================")
    def yanliang(self):

        print(f"{Mountain.yl}说道：我们去写举报信！！！")
        print("----------------")

    def pupu(self):

        print("三人一起去爬山")
        print(self.top)
        print(f'{Mountain.pp}说：我发现有人被推下山崖。')
        print('----------------')

    def yuefumu(self):

        print(f'{self.parents}说道：没得机会了！')
        print(f'{Mountain.zds}将{self.parents}推下山崖。')
        print("============================")





m = Mountain()
m.zhangdongsheng()
m.yuefumu()
m.zhuzhaoyang()
m.pupu()
m.yanliang()