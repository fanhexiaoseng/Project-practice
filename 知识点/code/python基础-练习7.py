#coding=utf-8

try:
        print(num)
        print("------1-------")
except (NameError,FileNotFoundError):
        print("如果捕获到异常后做的处理")
except Exception as ret:
        print(ret)
        print("一定捕获异常")
else:
        print("没有错误才会打印")
finally:
        print("有没有异常都会执行 ")
