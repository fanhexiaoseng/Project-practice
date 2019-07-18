#题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。 


# _*_ coding :utf-8 _*_
fp = open("text1.txt", "r")
a = fp.read()
fp.close()

fp = open("text2.txt", "r")
b = fp.read()
fp.close()

fp = open("text3.txt", "w")
c = sorted(a + b)
fp.write("".join(c))
fp.close()

fp = open("text3.txt", "r")
c = fp.read()
fp.close()


