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
    gender enum("男"，"女")，
    foreign key(subid) references subjects(id)外键 
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
9. 级联操作
```
alter table scores add constraint stu_sco foreign key(stuid) references students(id) on delete cascade;
restrict（限制）：默认值，抛异常
cascade（级联）：如果主表的记录删掉，则从表中相关联的记录都将被删除
set null：将外键设置为空
no action：什么都不做
```
10. 连接
```
select students.sname,subjects.stitle,scores.score
from scores
inner join students on scores.stuid=students.id
inner join subjects on scores.subid=subjects.id;
表A inner join 表B：表A与表B匹配的行会出现在结果中
表A left join 表B：表A与表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充
表A right join 表B：表A与表B匹配的行会出现在结果中，外加表B中独有的数据，未对应的数据使用null填充
```
11. 视图
```
create view stuscore as 
select students.*,scores.score from scores
inner join students on scores.stuid=students.id;
select * from stuscore;
```
12. 事务
```
事务四大特性(简称ACID)
原子性(Atomicity)：事务中的全部操作在数据库中是不可分割的，要么全部完成，要么均不执行
一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序串行执行的结果相一致
隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的
持久性(Durability)：对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障
事务语句
开启begin;
提交commit;
回滚rollback;
```
13. 与python交互
```
conn=connect(参数列表)
参数host：连接的mysql主机，如果本机是'localhost'
参数port：连接的mysql主机的端口，默认是3306
参数db：数据库的名称
参数user：连接的用户名
参数password：连接的密码
参数charset：通信采用的编码方式，默认是'gb2312'，要求与数据库创建时指定的编码一致，否则中文会乱码
close()关闭连接
commit()事务，所以需要提交才会生效
rollback()事务，放弃之前的操作
cursor()返回Cursor对象，用于执行sql语句并获得结果
```
```
cursor1=conn.cursor()
close()关闭
execute(operation [, parameters ])执行语句，返回受影响的行数
fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
next()执行查询语句时，获取当前行的下一行
fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
scroll(value[,mode])将行指针移动到某个位置
    mode表示移动的方式
    mode的默认值为relative，表示基于当前行移动到value，value为正则向下移动，value为负则向上移动
    mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0
```
14. 封装语句
```
#encoding=utf8
import MySQLdb

class MysqlHelper():
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset

    def connect(self):
      self.conn=MySQLdb.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cursor=self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self,sql,params=()):
        result=None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception, e:
            print e.message
        return result

    def get_all(self,sql,params=()):
        list=()
        try:
            self.connect()
            self.cursor.execute(sql,params)
            list=self.cursor.fetchall()
            self.close()
        except Exception,e:
            print e.message
        return list

    def insert(self,sql,params=()):
        return self.__edit(sql,params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self,sql,params):
        count=0
        try:
            self.connect()
            count=self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
        except Exception,e:
            print e.message
        return count
```
15. 
