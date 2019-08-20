## MySQL数据库
**************
- ### 安装
1. 安装命令：sudo apt-get install mysql-server mysql-client<br>
2. 权限设置：chown mysql:mysql -R /var/lib/mysql<br>
3. 初始化：mysqld --initialize<br>
4. 启动服务：service mysql start<br>
4. 创建用户密码：mysqladmin -u root password "new_password"<br>
5. 停止服务：service mysql stop<br>
6. 重启服务：service mysql restart<br>
- ### 数据类型
1. INT	整型	4字节整数类型，范围约+/-21亿
2. BIGINT	长整型	8字节整数类型，范围约+/-922亿亿
3. REAL	浮点型	4字节浮点数，范围约+/-1038
4. DOUBLE	浮点型	8字节浮点数，范围约+/-10308
5. DECIMAL(M,N)	高精度小数	由用户指定精度的小数，例如，DECIMAL(20,10)表示一共20位，其中小数10位，通常用于财务计算
6. CHAR(N)	定长字符串	存储指定长度的字符串，例如，CHAR(100)总是存储100个字符的字符串
7. VARCHAR(N)	变长字符串	存储可变长度的字符串，例如，VARCHAR(100)可以存储0~100个字符的字符串
8. BOOLEAN	布尔类型	存储True或者False
9. DATE	日期类型	存储日期，例如，2018-06-22
10. TIME	时间类型	存储时间，例如，12:20:59
11. DATETIME	日期和时间类型	存储日期+时间，例如，2018-06-22 12:20:59
