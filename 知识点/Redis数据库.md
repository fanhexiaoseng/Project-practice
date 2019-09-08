## Redis数据库
**************
- ### 安装
见崔庆财网站
- ### 数据操作
1. 字符串string
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
3. 哈希hash
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
4. 列表list
```
-在头部插入数据
LPUSH key value [value ...]
-在尾部插入数据
RPUSH key value [value ...]
-在一个元素的前|后插入新元素
LINSERT key BEFORE|AFTER pivot value
-设置指定索引的元素值
-索引是基于0的下标
-索引可以是负数，表示偏移量是从list尾部开始计数，如-1表示列表的最后一个元素
LSET key index value
-移除并且返回 key 对应的 list 的第一个元素
LPOP key
-移除并返回存于 key 的 list 的最后一个元素
RPOP key
-返回存储在 key 的列表里指定范围内的元素
start 和 end 偏移量都是基于0的下标
-偏移量也可以是负数，表示偏移量是从list尾部开始计数，如-1表示列表的最后一个元素
LRANGE key start stop
-裁剪列表，改为原集合的一个子集
start 和 end 偏移量都是基于0的下标
-偏移量也可以是负数，表示偏移量是从list尾部开始计数，如-1表示列表的最后一个元素
LTRIM key start stop
-返回存储在 key 里的list的长度
LLEN key
-返回列表里索引对应的元素
LINDEX key index
```
5. 集合set
```
-添加元素
SADD key member [member ...]
-返回key集合所有的元素
SMEMBERS key
-返回集合元素个数
SCARD key
-求多个集合的交集
SINTER key [key ...]
-求某集合与其它集合的差集
SDIFF key [key ...]
-求多个集合的合集
SUNION key [key ...]
-判断元素是否在集合中
SISMEMBER key member
```
6. 有序集合zset
```
-添加
ZADD key score member [score member ...]
-返回指定范围内的元素
ZRANGE key start stop
-返回元素个数
ZCARD key
-返回有序集key中，score值在min和max之间的成员
ZCOUNT key min max
-返回有序集key中，成员member的score值
ZSCORE key member
```
- ### 高级
1. 发布订阅
```
-订阅
SUBSCRIBE 频道名称 [频道名称 ...]
-取消订阅
-如果不写参数，表示取消所有订阅
UNSUBSCRIBE 频道名称 [频道名称 ...]
-发布
PUBLISH 频道 消息
```
2. 主从配置
```
-设置主服务器的配置
bind 192.168.1.10
-设置从服务器的配置
-注意：在slaveof后面写主机ip，再写端口，而且端口必须写
bind 192.168.1.11
slaveof 192.168.1.10 6379
-在master和slave分别执行info命令，查看输出信息
-在master上写数据
set hello world
-在slave上读数据
get hello
```
3. 与python交互
```
# 引入模块
import redis
# 连接
try:
    r=redis.StrictRedis(host='localhost',port=6379)
except Exception,e:
    print e.message
# 方式一：根据数据类型的不同，调用相应的方法，完成读写
# 更多方法同前面学的命令
r.set('name','hello')
r.get('name')
# 方式二：pipline
# 缓冲多条命令，然后一次性执行，减少服务器-客户端之间TCP数据库包，从而提高效率
pipe = r.pipeline()
pipe.set('name', 'world')
pipe.get('name')
pipe.execute()
```
```
# 连接redis服务器部分是一致的
# 这里将string类型的读写进行封装
import redis
class RedisHelper():
    def __init__(self,host='localhost',port=6379):
        self.__redis = redis.StrictRedis(host, port)
    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
    def set(self,key,value):
        self.__redis.set(key,value)
```
