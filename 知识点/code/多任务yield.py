def text1():
    while True:
        print("----1----")
        yield None
def text2():
    while True:
        print("----2----")
        yield None
t1 = text1()
t2 = text2()
while True:
    t1.__next__()
    t2.__next__()
----1----
----2----
----1----
----2----
----1----
----2----
----1----
----2----
