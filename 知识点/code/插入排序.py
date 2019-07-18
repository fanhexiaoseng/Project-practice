# _*_ coding :utf-8_*_
# 插入排序


def insertsearch(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i -1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertsearch(arr)
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i])
#排序后的数组:
5
6
11
12
13
