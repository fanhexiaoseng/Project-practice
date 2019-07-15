## python核心知识
********************
- ### python高级编程
1. 重新导入模块：<br>
```
from imp import *
reload(text)
```
2. is与==的区别<br>
==：内容是否相同<br>
is：地址是否相同<br>
3. 深拷贝与浅拷贝<br>
浅拷贝：指向一个地址，不开辟新的内存<br>
深拷贝：从新开辟一个内存，相同的内容，递归的拷贝，copy.deepcopy（）<br>
copy：从新开辟一个内存，内容相同，但是不递归的拷贝，copy.copy（）<br>
4. 1 Byte(字节B) = 8 bit（比特b）<br>
1 KB= 1024 B<br>
5. 私有化<br>
_num：from 类名 import *不可以导入,子类可以访问<br>
__num：私有属性，外部不可以访问，名字重整(_类名__num)，子类不可以访问<br>
6. property<br>
使用property升级set,get方法<br>
```
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
    money = property(getMoney, setMoney)
```
- ### Linux系统编程
- ### 网络编程
- ### web服务器案例
- ### 正则表达式
