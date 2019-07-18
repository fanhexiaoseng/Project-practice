# _*_ coding : utf-8 _*_
# 模仿静态变量的用法。


def func():
    vac = 0
    print(vac)
    vac += 1


if __name__ == '__main__':
    for i in range(3):
        func()


class Apple(object):
    pi = 5

    def make_apple(self):
        self.pi += 1
        print(self.pi)


print(Apple.pi)
a = Apple()
for i in range(3):
    Apple().make_apple()

0
0
0
5
6
6
6
