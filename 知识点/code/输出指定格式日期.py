#题目：输出指定格式的日期。

#程序分析：使用 datetime 模块。

# _*_ coding :utf-8 _*_
import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime("%d/%m/%Y"))
    maketime = datetime.datetime(1996, 5, 2,)
    print(maketime.strftime("%d/%m/%Y"))

    maketimes = maketime + datetime.timedelta(days=1)
    print(maketimes.strftime('%d/%m/%Y'))

    makeyeartime = maketimes.replace(maketimes.year + 1)
    print(makeyeartime.strftime('%d/%m/%Y'))


18/07/2019
02/05/1996
03/05/1996
03/05/1997
