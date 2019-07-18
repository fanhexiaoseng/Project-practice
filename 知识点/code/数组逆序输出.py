#题目：将一个数组逆序输出。

#程序分析：用第一个与最后一个交换。

# _*_ coding : utf-8 _*_
if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = []
    for i in range(2):
        a[i], a[-i - 1] = a[-i - 1], a[i]

    print(a)

#[5, 4, 3, 2, 1]
