# _*_ coding : utf-8 _*_

# key_value = {}
#
# # 初始化
# key_value[2] = 56
# key_value[1] = 2
# key_value[5] = 12
# key_value[4] = 24
# key_value[6] = 18
# key_value[3] = 323
#
# print(key_value)
# print(key_value.items())

L = [('b', 1), ('a', 2), ('c', 3), ('d', 4)]
print(sorted(L, key=lambda x: x[1]))
#[('b', 1), ('a', 2), ('c', 3), ('d', 4)]
