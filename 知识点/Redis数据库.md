## Redis数据库
**************
- ### 安装
见崔庆财网站
- ### 数据操作
1. string
```
-设置键值
set key value
-设置键值及过期时间，以秒为单位
SETEX key seconds value
-设置多个键值
MSET key value [key value ...]
-根据键获取值，如果不存在此键则返回nil
GET key
-根据多个键获取多个值
MGET key [key ...]
-将key对应的value加1
INCR key
-将key对应的value加整数
INCRBY key increment
-将key对应的value减1
DECR key
-将key对应的value减整数
DECRBY key decrement
-追加值
APPEND key value
-获取值长度
STRLEN key
```
2. 键命令
```
-查找键，参数支持正则
KEYS pattern
-判断键是否存在，如果存在返回1，不存在返回0
EXISTS key [key ...]
-查看键对应的value的类型
TYPE key
-删除键及对应的值
DEL key [key ...]
-设置过期时间，以秒为单位
-创建时没有设置过期时间则一直存在，直到使用使用DEL移除
EXPIRE key seconds
-查看有效时间，以秒为单位
TTL key
```
3. hash
```
-设置单个属性
HSET key field value
-设置多个属性
HMSET key field value [field value ...]
-获取一个属性的值
HGET key field
-获取多个属性的值
HMGET key field [field ...]
-获取所有属性和值
HGETALL key
-获取所有的属性
HKEYS key
-返回包含属性的个数
HLEN key
-获取所有值
HVALS key
-判断属性是否存在
HEXISTS key field
-删除属性及值
HDEL key field [field ...]
-返回值的字符串长度
HSTRLEN key field
```
4. list
```

```
