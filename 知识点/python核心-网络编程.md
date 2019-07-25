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
7. tcp服务器流程<br>
```
from socket import *
# 创建套接字
serverSocket = socket(AF_INET, SOCK_STREAM)
# 绑定端口
serverSocket.bind(("", 7788))
# 改为被动接听模式
serverSocket.listen(5)
# 等待接电话，此时堵塞，clientsocket为新的服务客户的客户端，clientaddr为客户地址
clientsocket, clientaddr = serverSocket.accept()
# 新套接字接受信息
recvDate = clientsocket.recv(1024)

print("%s:%s" % (str(clientaddr), recvDate))

clientsocket.close()
serverSocket.close()
```
8. tcp客户端流程<br>
```
from socket import *

# 创建套接字
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("192.168.1.124", 7788))

clientSocket.send("hahah".encode("gb2312"))
recvData = clientSocket.recv(1024)

print("recvData:%s" % recvData)

clientSocket.close()
```
9. 浏览器访问百度的过程<br>
1.先要解析出baidu.com对应的ip地址<br>
　　1.先知道默认网关的mac<br>
　　　1.1使用arp获取默认网关的mac地址<br>
　　2.组织数据发送给默认网关（ip还是dns服务器的ip，但是mac地址是默认网关的mac地址）<br>
　　3.默认网关拥有转发数据的能力，把数据转发给路由器<br>
　　4.路由器根据自己的路由协议，来选择一个合适的较快的路径转发给目的网关<br>
　　5.目的网关（dns服务器所在的网关），把数据转发给dns服务器<br>
　　6.dns服务器查询解析出baidu.com对应的ip地址，并把它原路返回给请求这个域名的client<br>
2.得到了baidu.com对应的ip地址之后，会发送tcp的3次握手，进行连接<br>
3.使用http协议发送请求数据给web服务器<br>
4.web服务器收到数据请求之后，通过查询自己服务器得到相应的结果，原路返回给浏览器<br>
5.历览器接受到数据后通过浏览器自己渲染功能来显示这个网页<br>
6.浏览器关闭tcp连接，既4次挥手<br>
完成整个访问过程<br>
10. 图示<br>
![image](https://github.com/fanhexiaoseng/Project-practice/blob/master/%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E3%80%81%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B.png)
11. 多进程服务器<br>
```
from multiprocessing import *
from socket import *

# 多进程函数
def dealWithClient(newSocket, destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print("revv[%s]:[%s]" % (str(destAddr), recvData))
        else:
            print("[%s]客户端已关闭" % str(destAddr))
            break
    newSocket.close()

def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    # 套接字可重复使用,注意跟广播参数不一样
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ("", 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)
    try:
        while True:
            print("-----主进程等待新客户端的到来-----")
            newSocket, destAddr = serSocket.accept()
            print("-----创建一个新的进程负责处理数据[%s]" % str(destAddr))

            client = Process(target=dealWithClient, args=(newSocket, destAddr))
            client.start()
            #进程可以关闭这个新客户端，但是线程不可以关闭这个套接字，因为线程共享数据
            newSocket.close()
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()
```
12. 
