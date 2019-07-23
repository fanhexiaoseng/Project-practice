## python核心知识
********************
- ### 网络编程
1. tcp/ip（协议族）<br>
　　　　　　　链路层-->网络层-->传输层-->　　　　　　　　　应用层<br>
物理层-->数据链路层-->网络层-->传输层-->会话层-->表示层-->应用层<br>
2. 端口用来区分进程<br>
3. ip用来区分唯一一台电脑（主机）<br>
4. socket-udp发送数据<br>
```
from socket import *

# 创建套接字UDP
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 接收方地址
sendAddr = ("192.168.1.103", 8080)

# 发送的数据
sendData = input("请输入要发送的数据：")

# 发送数据到指定电脑上
udpSocket.sendto(sendData.encode("utf-8"), sendAddr)

# 关闭套接字
udpSocket.close()
```
5. udp接收信息，绑定端口<br>
```
from socket import *

# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定本地相关信息
bindAddr = ("", 7788)
udpSocket.bind(bindAddr)

# 等待接收对方发送的数据
receData = udpSocket.recvfrom(1024)
content, destinfo = receData

# 显示接收的数据
print("content is %s"%content.decode("gb2312"))

udpSocket.close()
```
6. udp广播<br>
```
import socket
# 广播地址
dest = ("<broadcast>", 7788)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 对套接字进行修改，否则不能广播
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 广播发出
s.sendto("hi", dest)
while True:
    (buf, address) = s.recvfrom(2048)
    print("Received from %s: %s" % (address, buf))

```
7. 
