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
7. 登陆：mysql -uroot -p
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
- ### 数据库操作
1. show databases：列出所有的数据库
2. create database text:创建新的数据库
3. drop database text：删除数据库
4. use text：使用数据库
5. select now（）：查看当前时间
6. select version（）：查看版本
7. select database（）：查看当前数据库
- ### 数据表操作
1.
```
create table student(
    id int unsigned not null auto_increment primary key,
    name varchar(30),
    age tinyint unsigned default 0，
    gender enum("男"，"女")
);
```
2. show tables：列出所有表
3. show create table students：查看创建表的SQL语句
4. desc student：查看表结构
5. create student：创建表
6. drop student：删除表
- ### 修改数据表
1. 
