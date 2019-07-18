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
    money = property(setMoney,getMoney)
```
另一种实现方式<br>
```
class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
```
7. 生成器<br>
列表生成式-->（）<br>
```
L = [ x*2 for x in range(5)]
G = ( x*2 for x in range(5))
G
<generator object <genexpr> at 0x7f626c132db0>
```
带yield函数，next（）调用，a.\_\_next\_\_()调用<br>
```
def fib(times):
     n = 0
     a,b = 0,1
     while n<times:
         yield b
         a,b = b,a+b
         n+=1
     return 'done' 
```
生成器-多任务(协程)<br>
```
def text1():
    while True:
        print("----1----")
        yield None
def text2():
    while True:
        print("----2----")
        yield None
        
t1 = text1()
t2 = text2()
while True:
    t1.__next__()
    t2.__next__()
```
8. 可迭代对象(Iterable)：可以作用于for循环的list,dict,tuple,str,set,生成器，带yield<br>
迭代器(Iterator)：一定可以迭代，可以用next（）方法的，生成器都是迭代器，iter（）将可迭代对象变成迭代器<br>
9. 装饰器<br>
```
def w1(func):
    def inner():
        print("------验证------")
        func()
    return inner
#f1 = w1(f1)
@w1
def f1():
    print("------f1------")
f1()
```
通用装饰器<br>
```
def func(functionName):
    def func_in(*args,**kwargs):
        print("----记录日志----")
        ret = functionName(*args,**kwargs)
        return ret
    return func_in

@func
def text1():
    print("----1-----")
@func
def text2():
    print("----2-----")
    return "haha"
@func
def text3(a):
    print("----3-----")

text1()
ret = text2()
print(ret)
text3()
```
装饰器带参数<br>
```
def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__,ctime(),pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("python")
def foo():
    print("I am foo")

foo()
```
两个装饰器的情况，先执行下面的函数<br>
10.  类中动态添加方法  
```
p1.run = types.MethodType(run,p1)
```
11. 限制实例属性(对继承的子类不起作用)<br>
```
class Person(object):
    __slots__ = ("name","age")
```
12. 小整数[-5,256]共用对象，常驻内存<br>
单个字符共用对象，常驻内存<br>
单个单词，不可修改，默认开启intern机制，共用对象，引用计数为0，则销毁 <br>
字符串（含有空格），不可修改，没开启intern机制，不共用对象，引用计数为0，销毁<br>
大整数不共用内存，引用计数为0，销毁<br>
13. 内建函数<br>
range：range(start, stop[, step]) -> list of integers<br>
map：map函数会根据提供的函数对指定序列做映射，map(function, sequence[, sequence, ...]) -> list<br>
filter：filter函数会对指定序列执行过滤操作，filter(function or None, sequence) -> list, tuple, or string<br>
reduce：reduce函数会对参数序列中元素进行累积，reduce(function, sequence[, initial]) -> value<br>
sorted：sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list<br>
- ### Linux系统编程
- ### 网络编程
- ### web服务器案例
- ### 正则表达式
