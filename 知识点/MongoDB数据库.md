## MongoDB数据库
**************
- ### 安装
安装见催庆才GitHub
- ### 数据库操作
1. 查看当前数据库名称：db
2. 列出所有在物理上存在的数据库：show dbs
3. 切换数据库use：数据库名称
4. 集合创建：db.createCollection(name, options)
```
db.createCollection("sub", { capped : true, size : 10 } )
```
5. 查看当前数据库的集合：show collections
6. 删除：db.集合名称.drop()
- ### 数据
1. Object ID：文档ID
2. String：字符串，最常用，必须是有效的UTF-8
3. Boolean：存储一个布尔值，true或false
4. Integer：整数可以是32位或64位，这取决于服务器
5. Double：存储浮点值
6. Arrays：数组或列表，多个值存储到一个键
7. Object：用于嵌入式的文档，即一个值为一个文档
8. Null：存储Null值
9. Timestamp：时间戳
10. Date：存储当前日期或时间的UNIX时间格式
- ### 数据操作
1. 插入
```
db.集合名称.insert(document)
db.stu.insert({name:'gj',gender:1})
s1={_id:'20160101',name:'hr'}
s1.gender=0
db.stu.insert(s1)
```
2. 查询
```
db.集合名称.find()
```
3. 更新
```
db.集合名称.update(
   <query>,
   <update>,
   {multi: <boolean>}
)
db.stu.update({name:'hr'},{name:'mnc'})
修改多条匹配到的数据
db.stu.update({},{$set:{gender:0}},{multi:true})
```
4. 保存
```
db.集合名称.save(document)
db.stu.save({_id:'20160102','name':'yk',gender:1})
```
5. 删除
```
db.集合名称.remove(
   <query>,
   {
     justOne: <boolean>
   }
)
db.stu.remove({gender:0},{justOne:true})
```
6. 查询重点
```
-方法findOne()：查询，只返回第一个
db.集合名称.findOne({条件文档})
-方法pretty()：将结果格式化
db.集合名称.find({条件文档}).pretty()
-等于，默认是等于判断，没有运算符
-小于$lt
-小于或等于$lte
-大于$gt
-大于或等于$gte
-不等于$ne
db.stu.find({age:{$gte:18}})
-逻辑与：默认是逻辑与的关系
-逻辑或：使用$or
db.stu.find({$or:[{age:{$gt:18}},{gender:1}]})
db.stu.find({$or:[{age:{$gte:18}},{gender:1}],name:'gj'})
-使用"$in"，"$nin" 判断是否在某个范围内
db.stu.find({age:{$in:[18,28]}})
-使用//或$regex编写正则表达式
db.stu.find({name:/^黄/})
db.stu.find({name:{$regex:'^黄'}}})
-使用$where后面写一个函数，返回满足条件的数据
db.stu.find({$where:function(){return this.age>20}})
```
7. 文档数量读取
```
-方法limit()：用于读取指定数量的文档
db.集合名称.find().limit(NUMBER)
-方法skip()：用于跳过指定数量的文档
db.集合名称.find().skip(NUMBER)
-查询第5至8条数据
db.stu.find().limit(4).skip(5)
```
8. 投影
```
参数为字段与值，值为1表示显示，值为0不显示
db.集合名称.find({},{字段名称:1,...})
```
9. 排序
```
方法sort()，用于对结果集进行排序
db.集合名称.find().sort({字段:1,...})
参数1为升序排列
参数-1为降序排列
db.stu.find().sort({gender:-1,age:1})
```
10. 统计个数
```
方法count()用于统计结果集中文档条数
db.集合名称.find({条件}).count()
db.集合名称.count({条件})
db.stu.find({gender:1}).count()
```
11. 消除重复
```
方法distinct()对数据进行去重
db.集合名称.distinct('去重字段',{条件})
db.stu.distinct('gender',{age:{$gt:18}})
```
