## python基础知识
**************
- ### 字符串操作
1.　左查找：find（“”）   查不到返回：-1<br>
2.　右查找：rfind（“”）  查不到返回：-1<br>
3.　查找：index（“”）    查不到返回：报错<br>
4.　次数：count（“”）<br>
5.　替换：replace（“”，“”），个数）<br>
6.　切割：split（“”） 不填：切空白字符<br>
7.　首字母大写：capitalize（）<br>
8.　所有单词首字母大写：title（）<br>
9.　以···开头：startwith（“”）<br>
10.　以···结尾：endswith（“”）<br>
11.　小写：lower（）<br>
12.　大写：upper（）<br>
13.　左对齐：ljust（数字）空格补全<br>
14.　右对齐：rjust（）<br>
15.　居中：center（）<br>
16.　左空格删除：lstrip（）<br>
17.　右空格删除：rstrip（）<br>
18.　两边删除：strip（）<br>
19.　按“”分割：partition（“”） 返回元祖，分成三个<br>
　　　　　　rpartition（“”）<br>
20.　按行分割：splitline（“”）<br>
21.　是否是字母：isalpha（）<br>
　是否是数字：isdigit（）<br>
　是否数字或字母：isalnum（）<br>
　是否是空格：isspace（）<br> 
22.　连接：b.join(a) a1ba2ba3<br>
- ### 列表字典元组集合
- #### 列表
1.　增加：append（）<br>
　　　　extend（）<br>
　　　　insert（）<br>
2.　删除：pop（）<br>
　　　　remove（）<br>
　　　　del name[0]<br>
3.　改：利用切片更改<br>
4.　降序：sort（reverse=True）<br>
　倒序：revers（）<br>
- #### 字典
1.　查找：infor.get（“name”）<br>
2.　删除：del infor[“name”]<br>
3.　字典不重复<br>
- #### 元组
1.　一旦创建不可更改<br>
2.　按照key排序：sort（key=lambda x：x["name"]）<br>
- #### 集合
1.　set：无序（不能取下标）不重复元素集<br>
- ### 函数
1.　声明全局变量：global+变量<br>
2.　全局变量与局部变量名称相同时：局部变量优先<br>
3.　缺省参数：如果传值就用传的，没传值就用默认的<br>
4.　不定长参数：\*args（0-多个）元祖 没有变量名的<br>
　　　　　　　\**kwargs（0-多个）字典 带变量名的<br>
5.　拆包：传值前用\*元组\**字典可以拆开里面的内容<br>
6.　执行字母串表达式：eval（）<br>
7.　对于可变类型：num+=num 先看可不可以更改，可以更改直接更改，外部变量也改变<br>
　　　　　　　　num=num+num 内部num指向一个新的变量，外部不改变<br>
8.　关于python函数传参：<br>
　　首先还是应该科普下函数参数传递机制，传值和传引用是什么意思？<br>
　　函数参数传递机制问题在本质上是调用函数（过程）和被调用函数（过程）在调用发生时进行通信的方法问题。基本的参数传递机制有两种：值传递和引用传递。<br>
　　值传递（passl-by-value）过程中，被调函数的形式参数作为被调函数的局部变量处理，即在堆栈中开辟了内存空间以存放由主调函数放进来的实参的值，从而成为了实参的一个副本。值传递的特点是被调函数对形式参数的任何操作都是作为局部变量进行，不会影响主调函数的实参变量的值。<br>
　　引用传递(pass-by-reference)过程中，被调函数的形式参数虽然也作为局部变量在堆栈中开辟了内存空间，但是这时存放的是由主调函数放进来的实参变量的地址。被调函数对形参的任何操作都被处理成间接寻址，即通过堆栈中存放的地址访问主调函数中的实参变量。正因为如此，被调函数对形参做的任何操作都影响了主调函数中的实参变量。<br>
- ### 文件读写
1.　r：读 w：写 a：追加 rb wb ab r+ w+ a+ <br>
2.　读取行:readline（）<br>
3.　生成列表：readlines（）一行一个元素<br>
4.　大文件的读取方法：while True：read（1024）<br>
5.　指针更改：f.seek（2,0）0-开头 1-当前 2-结尾<br>
6.　显示指针位置：f.tell（）<br>
7.　文件改名：os.rename（“原名”，“改名”）<br>
8.　删除文件：os.remove（“”）<br>
9.　创建文件：os.mkdir（“”）<br>
10.　删除文件：os.rmdir（“”）<br>
11.　当前路径：os.getcwd（）<br>
12.　更改默认路径：os.chdir（“../”）<br>
13.　当前目录：os.listdir（“./”）<br>
- ### 面向对象
1.　三大特征：封装，继承，多态<br>
2.　类的名称，类的属性，类的方法<br>
3.　实例属性，实例方法，类属性，类方法（@classmethod），静态方法（@staticmethod）<br>
4.　初始化：\_\_init\_\_()<br>
5.　打印：\_\_str\_\_():return <br>
6.　删除或程序退出时:\_\_del\_\_()<br>
7.　创建对象：\_\_new\_\_()<br>
8.　导入时可以使用：\_\_all\_\_=["text",]<br>
9.　引用计数：sys.getrefcount（）<br>
10.　隐藏属性：set方法 get方法<br>
11.　私有属性：\_\_num 外部不允许使用<br>
12.　私有方法：\_\_text()内部调用<br>
13.　调用被重写的父类：Dog.bark（self）<br>
　　　　　　　　　　super（）.bark（）<br>
14.　解耦：利用函数和类解耦<br>
- ### 其他
1.　给程序传参数：import sys  print（sys.args）<br>
2.　列表生成式：a = [i for i in range(1,18) if i%2==0]<br>
　　　　　　　a = [(i,j)for i in range(3) for j in range(2)]<br>


