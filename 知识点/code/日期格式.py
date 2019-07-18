#题目：字符串日期转换为易读的日期格式。

# _*_ coding : utf-8 _*_
from dateutil import parser

dt = parser.parse("Aug 28 2015 12:00AM")
print(dt)
print("\'7\'")

#2015-08-28 00:00:00
'7'
