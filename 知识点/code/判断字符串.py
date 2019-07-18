#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

#程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

# _*_ coding : utf-8 _*_
a = input("请输入字符串：")
letters = 0
space = 0
dight = 0
other = 0
for i in a:
    if i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        dight += 1
    else:
        other += 1
print("a字符串中共计有%d个字母，%d个空格，%d个数字，%d个其它" % (letters, space, dight, other))

#请输入字符串：ad12 #413sdf
a字符串中共计有5个字母，1个空格，5个数字，1个其它
