#题目：求1+2!+3!+...+20!的和。

#程序分析：此程序只是把累加变成了累乘。 

# _*_ coding : utf-8 _*-
# s = 0
#
# t = 1
# for n in range(1,21):
#     t = t * n
#     s= s + t
# print(s)
l = range(1, 21)


def fangsum(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

#2561327494111820313
