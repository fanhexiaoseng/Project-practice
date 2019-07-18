#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

# _*_ coding :utf-8 _*_
from functools import reduce

a = []

for i in range(2, 1001):
    a = []
    s = i
    for j in range(1, i):
        if i % j == 0:
            s -= j
            a.append(j)

    if s == 0:
        print(i)
        b = [str(i) for i in a]
        print(",".join(b))

    # print(reduce(lambda x, y: x + y, a))

6
1,2,3
28
1,2,4,7,14
496
1,2,4,8,16,31,62,124,248
