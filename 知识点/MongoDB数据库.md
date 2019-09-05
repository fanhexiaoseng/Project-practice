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

```
