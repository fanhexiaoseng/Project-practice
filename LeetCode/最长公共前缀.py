'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:

所有输入只包含小写字母 a-z 。
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == ""or not strs:
            return ""
        # if len(strs)==1:
        #     return str(strs)
        
        
        lengh = len(strs[0])
        k = strs[0]
        for i in strs:
            if len(i)<lengh:
                lengh = len(i)
                k = i
        
        while lengh > 0:
            a = []
            b = k[:lengh]
            for index in strs:
                if index.startswith(b):
                    a.append(index)
            if len(a) == len(strs):
                    return b
            lengh -= 1
        return ""
