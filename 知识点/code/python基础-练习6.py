class Dog(object):

        #私有类属性
        __instance = None
        __init_flag = False
        #单例模式

        def __new__(cls,name):
                if cls.__instance == None:
                        cls.__instance = object.__new__(cls)
                        return cls.__instance  
                else:
                        return cls.__instance
        def __init__(self,name):  
                if Dog.__init_flag == False:
                        self.name = name
                        Dog.__init_flag =True
a = Dog("随机附送") 
print(id(a))
print(a.name)
b = Dog("塑封机司法局华") 
print(id(b))
print(b.name)
