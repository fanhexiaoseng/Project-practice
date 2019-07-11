# -*- coding:utf-8 -*-
#coding=utf-8
#这是一个注释,(*^__^*) 嘻嘻……

print("hello world")
#定义一个变量
score = 100#单位是分
#输入姓名
'''
name = raw_input("请输入姓名:")
#输入身高
heigh = input("请输入身高:")
#打印姓名,python3运行
print("姓名:%s\n身高是:%d"%(name,heigh))
'''
'''
num = 1
while num <= 10:
        num += 1
        print(num)
'''
i = 1

while i <= 9:
        j = 1
        while j <=i:
                print("%d*%d=%d\t"%(j,i,i*j),end="")
                j+=1
        print("")
        i+=1

