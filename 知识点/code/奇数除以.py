#题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

#程序分析：999999 / 13 = 76923。

# _*_ coding :utf-8 _*_
a = int(input("请输入一个奇数："))
i = 1
n = 9
sum = 0
args = 1
while args:
    sum += n * i
    i *= 10
    if sum % a == 0:
        args = 0
print(sum)

#请输入一个奇数：33
99
