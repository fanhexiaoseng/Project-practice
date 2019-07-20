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
3. fork主进程结束程序就会跳出命令行<br>
4. 全局变量，局部变量，所有的变量在多进程中数据不共享<br>
5. multprocessing-Process<br>
```
from multiprocessing import Process
import time


def text():    
    print("---text---")
    time.sleep(1)


if __name__ == '__main__':
    #创建一个进程
    p = Process(target=text)
    #子进程开始
    p.start()
    p.join()#解堵塞，等到子进程结束在继续向后执行

    print("---main--- ")

```
6. Process主进程等待子进程先结束<br>
7. Process子类创建子进程<br>
```
from multiprocessing import Process
import time

class MyNewProcess(Process):
    def run(self):
            while True:
                    print("---1---")
                    time.sleep(1)

p = MyNewProcess()
p.start()

while True:
    print("---main---")
    time.sleep(1)
```
8. 进程池Pool<br>
```
from multiprocessing import Pool
import os
import random


def worker():
    for i in range(random.randint(1,3)):
        print("---pid=%d---"%os.getpid())
#三个进程
pool = Pool(3)
for i in range(10):
    print("===%d==="%i)
    #进程池任务添加，任务多会等待空余进程
    pool.apply_async(worker)#非堵塞 ，apply堵塞

pool.close()#关闭进程池，不能添加任务
pool.join()#默认不会等待进程池任务完成，join会让主进程等待进程池结束
```
9. Queue<br>
Queue.qsize():返回队列的消息数量<br>
Queue.empty():队列为空，返回True<br>
Queue.full():队列为满，返回True<br>
Queue.get():获取一条消息<br>
Queue.get_nowait():Queue.get(False)非阻塞，抛出异常<br>
Queue.put(item):将item写入队列<br>
Queue.put_nowait():Queue.put(item,False)如果没有空间抛出异常<br>
- ### Linux系统编程-线程
1. threading-Thread<br>
```
from threading import Thread
import time


def text():
    print("---lalalalala----")
    time.sleep(1)


for i in range(5):
    #开启线程
    t = Thread(target=text)
    t.start()

```
2. Thread子类创建多线程<br>
```
 
```
