## python核心知识
********************
- ### Linux系统编程
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

