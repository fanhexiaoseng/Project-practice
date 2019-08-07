## python核心知识
********************
- ### web服务器案例
1. GET 获取数据<br>
POST 修改数据<br>
PUT 保存数据<br>
DELETE 删除<br>
OPTION 询问服务器的某种支持特性<br>
HEAD 返回报文头<br>
2. 返回固定值的web服务器<br>
```
import socket

from multiprocessing import Process

HTML_ROOT_DIR = ""


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request_data:",request_data)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello world"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:", response)
    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))
    # 关闭客户端连接
    client_socket.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)
    while True:
        client_socket, client_address = server_socket.accept()
        # print("[%s:%s]用户连接", client_address[0], client_address[1])
        print("[%s:%s]用户连接",client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
```
3. 静态文件的web服务器面向对象<br>
```
import socket
import re

from multiprocessing import Process

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"


class HTTPServer(object):
    """服务器类"""

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self, port):
        self.server_socket.bind(("", port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s:%s]用户连接" % (client_address[0], client_address[1]))
            print("[%s:%s]用户连接" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request_data:", request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)
        # 解析请求报文
        # 'GET / HTTP/1.1'
        print(request_lines[0].decode("utf-8"))
        request_start_lines = str(request_lines[0].decode("utf-8"))
        print(request_start_lines)
        # 提取用户请求的文件名
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_lines).group(1)
        if "/" == file_name:
            file_name = "/index.html"

        # 打开文件，读取内容
        try:
            f = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            # 构造响应数据
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "the file is not found!"
        else:
            file_data = f.read()
            f.close()
            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            response_body = file_data.decode("utf-8")
        finally:
            response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)
        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端连接
        client_socket.close()


def main():
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()


if __name__ == '__main__':
    main()

```
4. WSGI协议的引入<br>
```
import re
import socket
import sys
from multiprocessing import Process

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"

WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    """"""

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self, port):
        self.server_socket.bind(("", port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s:%s]用户连接" % (client_address[0], client_address[1]))
            print("[%s:%s]用户连接" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def start_response(self, status, headers):

        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s:%s\r\n" % header
            self.response_headers = response_headers

    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request_data:", request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)
        # 解析请求报文
        # 'GET / HTTP/1.1'
        print(request_lines[0].decode("utf-8"))
        request_start_lines = str(request_lines[0].decode("utf-8"))
        print(request_start_lines)
        # 提取用户请求的文件名
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_lines).group(1)
        # 运行/time.py
        if file_name.endswith(".py"):
            m = __import__(file_name[1:-3])
            env = {}
            response_body = m.appliction(env, self.start_response)
            response = self.response_headers + "\r\n" + response_body 

        else:
            if "/" == file_name:
                file_name = "/index.html"

            # 打开文件，读取内容
            try:
                f = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 构造响应数据
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_headers = "Server: My server\r\n"
                response_body = "the file is not found!"
            else:
                file_data = f.read()
                f.close()
                # 构造响应数据
                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_headers = "Server: My server\r\n"
                response_body = file_data.decode("utf-8")
            finally:
                response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)
        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端连接
        client_socket.close()


def main():
    sys.path.insert(1,WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()


if __name__ == '__main__':
    main()

```
```
# coding : utf-8

import time


def appliction(env, start_response):
    status = "200 OK"
    headers = [
        ("Content_Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()

```
5. web框架<br>
MyWebServer<br>
```
import re
import socket
import sys
from multiprocessing import Process


# 设置静态文件根目录
HTML_ROOT_DIR = "./html"

WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    """"""

    def __init__(self, application):
        """构造函数，application指的是框架的app"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = application


    def bind(self, port):
        self.server_socket.bind(("", port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s:%s]用户连接" % (client_address[0], client_address[1]))
            print("[%s:%s]用户连接" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def start_response(self, status, headers):

        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s:%s\r\n" % header
        self.response_headers = response_headers

    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request_data:", request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)
        # 解析请求报文
        # 'GET / HTTP/1.1'
        print(request_lines[0].decode("utf-8"))
        request_start_lines = str(request_lines[0].decode("utf-8"))
        print(request_start_lines)
        # 提取用户请求的文件名
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_lines).group(1)
        method = re.match(r"(\w+) +/[^ ]* ", request_start_lines).group(1)

        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body

        
        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端连接
        client_socket.close()


def main():
    if len(sys.argv) < 2:
        sys.exit("python MyWebServer.py Modile:app")
    sys.path.insert(1, WSGI_PYTHON_DIR)
    module_name, app_name = sys.argv(1).split(":")
    m = __import__(module_name)
    # 返回对象属性值
    app = getattr(m, app_name)



    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()


if __name__ == '__main__':
    main()
```
MyWebFramework<br>
```
import time
# from MyWebServer import HTTPServer

HTML_ROOT_DIR = "./html"
class Application(object):
    """框架的核心部分，框架的主体布局，框架是通用的"""

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        # 路由分发
        path = env.get("PATH_INFO", "/")
        # /static/index.html
        if path.startswith("/static"):
            file_name = path[7:]
            # 打开文件，读取内容
            try:
                f = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 构造响应数据
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                file_data = f.read()
                f.close()
                # 构造响应数据
                status = "200 OK"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")


        for url, header in self.urls:
            if path == url:
                return header(env, start_response)
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Comtent_Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Comtent_Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello itcast"

urls = [
    ("/ctime", show_ctime),
    ("/sayhello", say_hello)
]
# if __name__ == '__main__':
#     urls = [
#         ("/ctime", show_ctime),
#         ("/sayhello", say_hello)
#     ]
#     app = Application(urls)
#
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()

```
