# _*_ coding : utf-8 _*_

def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


arr = ['A', 'B', 'C', 'D', 'E']
x = 'D'

realut = search(arr, len(arr), x)
if realut != -1:
    print(realut)
else:
    print("不存在！")
#3
