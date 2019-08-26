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
1. alter table student add birthday datetime：增加字段
2. alter table student modify birthday date：修改字段的数据类型与约束
3. alter table student change birthday birth datetime：修改字段的名字
4. alter table student drop birthday ：删除字段
- ### CURD
1. 增加
```
insert into student values(0,"马思远"),(1,"李奥飞");
insert into student (id,name) values(0,"马思远");
```
2. 修改
```
update student set mane="马思远" where id=1;
```
3. 查询
```
select * from student where id=1;
select id as "编号"，name as "姓名" from student;
```
4. 删除
```
delete from student where id=1;
alter table student add id_delete bit default 0;
update student set is_delete=1 where id=1;
```
- ### 查询
1. 消除重复
```
select distinct gender from student;
```
2. 逻辑条件
```
select * from student where age>18 and age<28;
```
3. 模糊查询
```
select name from student where name like "__%";
```
4. 范围查询
```
select name, age from student where age in (12,18,34);
select name, age from student where age between 12 and 34;
select * from student where height is null;
```
5. 排序
```
select * from student where (age between 18 and 34) and gender=1 order by age;
select * from student where (age between 18 and 34) and gender=2 order by age desc,height asc;
```
6. 聚合
```
select count(*) from student where is_delete=0;max,min,sum,avg
select * from student where id=(select min(id) from student where is_delete=0);
```
7. 分组
```
select gender as 性别 ,count(*) from student group by gender;
select gender as 性别 ,count(*) from student group by gender having gender="男";
```
8. 分页
```
select * from student limit 5,10;
limit (n-1)*m,m
```
