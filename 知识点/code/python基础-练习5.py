'''
class Cat():
        """定义一个Cat类"""     
        #初始化对象
        def __init__(self,name,age):
                self.name = name
                self.age = age
        def __str__(self):
                return "打印了" 
        #方法
        def eat(self):
                print("猫在吃鱼")       
        
        def drink(self):
                print("猫在喝水")
        
        def introduce(self):
                print("%s的年龄是:%d"%(self.name,self.age))
#创建一个对象
tom = Cat("汤姆",20)
tom.eat()
tom.drink()
tom.introduce()
'''
'''
class Dog():
        def __init__(self,new_name):
                self.name = new_name
                self.__age = 0
        def set_age(self,new_age):
