# _*_ coding :utf-8 _*_
with open("text1.txt", "w") as fp:
    fp.write("lalalala   demaxiya")
with open("text1.txt") as fp:
    a = fp.read()
print(a)

#lalalala   demaxiya
