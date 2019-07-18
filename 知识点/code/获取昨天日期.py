# _*_ coding : utf-8 _*_
import datetime


def yesterday():
    today = datetime.date.today()
    yitian = datetime.timedelta(days=1)
    yesterdays = today - yitian
    return yesterdays


print(yesterday())

#2019-07-17
