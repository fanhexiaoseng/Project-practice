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
12. 单进程非堵塞服务器<br>
```
from socket import *

serSocket = socket(AF_INET, SOCK_STREAM)
localAddr = ("", 7788)
serSocket.bind(localAddr)
# 让这个socket变成非堵塞，如果accept之前没有客户端连接，会报错
serSocket.setblocking(False)
serSocket.listen(100)

clientAddrList = []

while True:
    try:
        clientSocket, clientAddr = serSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来：%s" % str(clientAddr))
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket, clientAddr))

    for clientSocket, clientAddr in clientAddrList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData) > 0:
                print("%s:%s" % (str(clientAddr), recvData))
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket, clientAddr))
                print("%s已经下线" % str(clientAddr))

```
13. epoll服务器<br>
```
import socket
import select

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 设置可以重复使用绑定的信息
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("",7788))
s.listen(10)

# 创建一个epoll对象
epoll=select.epoll()

# 测试，用来打印套接字对应的文件描述符
# print s.fileno()
# print select.EPOLLIN|select.EPOLLET

# 注册事件到epoll中
# epoll.register(fd[, eventmask])
# 注意，如果fd已经注册过，则会发生异常
# 将创建的套接字添加到epoll的事件监听中
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

connections = {}
addresses = {}

while True:

    # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
    epoll_list=epoll.poll()

    # 对事件进行判断
    for fd,events in epoll_list:

        # print fd
        # print events

        # 如果是socket创建的套接字被激活
        if fd == s.fileno():
            conn,addr=s.accept()

            print('有新的客户端到来%s'%str(addr))

            # 将 conn 和 addr 信息分别保存起来
            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr

            # 向 epoll 中注册 连接 socket 的 可读 事件
            epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)


        elif events == select.EPOLLIN:
            # 从激活 fd 上接收
            recvData = connections[fd].recv(1024)

            if len(recvData)>0:
                print('recv:%s'%recvData)
            else:
                # 从 epoll 中移除该 连接 fd
                epoll.unregister(fd)

                # server 侧主动关闭该 连接 fd
                connections[fd].close()

                print("%s---offline---"%str(addresses[fd])) 
```
14. 计算密集型-需要占用大量的CPU资源-多进程<br>
io密集型-需要网络功能，大量的时间都在等待网络数据的到来-多线程、协程<br>
15. 协程简单实现原理yield<br>
```
import time

def A():
    while True:
        print("----A---")
        yield
        time.sleep(0.5)

def B(c):
    while True:
        print("----B---")
        c.next()
        time.sleep(0.5)

if __name__=='__main__':
    a = A()
    B(a)
```
16. greenlet实现协程sudo pip3 install greenlet<br>
```
from greenlet import greenlet
import time

def test1():
    while True:
        print "---A--"
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print "---B--"
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到gr1中运行
gr1.switch()
```
17. gevent实现协程sudo pip3 install gevent<br>
```
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        # 遇到耗时操作时，将执行权交出去，切换下一个程序
        gevent.sleep(1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
```
18. gevent实现协程服务器<br>
```
import sys
import time
import gevent

from gevent import socket,monkey
monkey.patch_all()

def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("recv:", data)
        conn.send(data)


def server(port):
    s = socket.socket()
    s.bind(('', port))
    s.listen(5)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)

if __name__ == '__main__':
    server(7788)
```
