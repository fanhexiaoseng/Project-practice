#题目：暂停一秒输出，并格式化当前时间

# _*_ coding : utf-8 _*_
import time

print(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
time.sleep(2)
print(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))

#2019-07-18-09-53-39
#2019-07-18-09-53-41
