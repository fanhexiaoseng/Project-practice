'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true

示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
'''
# 方法一：
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        if x < 0:
            return False
        elif a[::-1] == a:
            return True
        else:
            return False
            
# 方法二
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or not x % 10 and x: return False
        r = 0
        while x > r:
            x, rem = x // 10, x % 10
            r = r * 10 + rem
        return x == r or x == r // 10
