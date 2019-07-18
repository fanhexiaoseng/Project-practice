# _*_ coding : utf-8 _*_

#  输出日历
import calendar

yy = int(input("输入年份："))
mm = int(input("输入月份："))
print(calendar.calendar(2019, w=2, l=1, c=6))
print(calendar.month(yy, mm))
