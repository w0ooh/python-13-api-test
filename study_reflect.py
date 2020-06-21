# _*_coding:utf-8_*_
# Author : wanghua
# Time   : 2020/6/2 14:45
# File   : study_reflect.py
# IDE    : PyCharm

"""解决不同模块间的数据传递--反射 """

#动态---运行时，无需提前实例化，在运行的时候进行添加，获取甚至更改他的属性或者方法
#静态---运行前，如果调用类的属性或方法，需要实例化对象


class Girls:

    single = True   #类属性

    def __init__(self, name, age):
        self.name = name   #对象属性
        self.age = age

    def sing(self):
        print(self.name+'会唱歌')


if __name__== "__main__":
    g=Girls("nicole",18)
    g.sing()

    setattr(g,'hob','dance') #动态给实例g添加了属性hob,只能由实例g调用
    print(g.hob)

    setattr(Girls,'height','163cm') #动态给类Girls添加了属性hob,可以由Girls类的任何实例进行调用
    g2=Girls('nicole2','20')
    print(g2.height)
    print(g.height)

    #根据类的名动态获取属性值,不用通过实例化，直接获取
    print(getattr(Girls,'height'))

    #判断当前类里是否有某个类属性
    print(hasattr(Girls,'name'))  #判断是否有类属性
    print(hasattr(g, 'name'))   #判断是否有对象属性
    print(hasattr(Girls, 'single'))

    #动态清除属性
    # delattr(g,'name')  #删除对象属性
    # print(g.name)  #会报错，因为已删除

    delattr(Girls,'sing')  #删除类属性
    print(Girls.sing)