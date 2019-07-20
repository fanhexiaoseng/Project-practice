## python核心知识
********************
- ### Linux系统编程-进程
1. fork<br>
```
import os
import time
#多任务fork实现进程

ret = os.fork()
#fork后出现两个进程,也就是出现两个箭头,分别执行,返回值一个为大于0的一个为0

if ret == 0:
        while True:
                print("-----1-----")
                time.sleep(1)
else:

        while True:
                print("-----2-----")
                time.sleep(1)

```
2. pid<br>
```
import os

ret = os.fork()
print(ret)
if ret > 0:
#父进程,getpid为获取进程号
        print("----父进程-----%d"%os.getpid())
else:
#子进程,ret的数字是子进程的进程号,getppid为回去父进程的进程号
        print("----子进程-----%d--%d"%(os.getpid(),os.getppid()))
#20570 父进程>0显示的是子进程的进程号
#0 子进程
#-----父进程----20569
#-----子进程----20570--20569

```
3. 主进程结束程序就会跳出命令行<br>
4. 全局变量，局部变量，所有的变量在多进程中数据不共享<br>
5. 
