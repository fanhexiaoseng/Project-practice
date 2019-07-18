#题目：列表转换为字典。

# _*_ coding :utf-8_*_
a = [1, 2]
b = ["g", "c"]
f = dict(a='a', b='b', t='t')
f = dict(zip([1, 2, 3], [4, 5, 6]))
f = dict([(1, 2), (6, 5)])
print(f)

#{1: 2, 6: 5}
