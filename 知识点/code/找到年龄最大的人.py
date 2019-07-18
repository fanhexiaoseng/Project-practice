#题目：找到年龄最大的人，并输出。请找出程序中有什么问题。

# _*_ coding :utf-8 _*_
# 找出年龄最大的人

if __name__ == '__main__':
    person = {"li": 50, "wang": 50, "zhang": 20, "sun": 22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print('%s,%d' % (m, person[m]))

#li,50
