'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for index in nums:
            if index in dict:
                dict[index] += 1
            else:
                dict[index] = 1
        for i in dict:
            if dict[i] > len(nums)/2:
                return i
'''              
想法

我们知道出现次数最多的元素大于 ⌊n2⌋\lfloor \dfrac{n}{2} \rfloor⌊2n​⌋ 次，所以可以用哈希表来快速统计每个元素出现的次数。

算法

我们使用哈希表来存储每个元素，然后用一个循环在线性时间内遍历 nums ，然后我们只需要返回有最大值的键。
'''
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
'''
复杂度分析

    时间复杂度：O(n)O(n)O(n)

    我们将 nums 迭代一次，哈希表的插入是常数时间的。所以总时间复杂度为 O(n)O(n)O(n) 时间的。

    空间复杂度：O(n)O(n)O(n)

    哈希表最多包含 n−⌊n2⌋n - \lfloor \dfrac{n}{2} \rfloorn−⌊2n​⌋ 个关系，所以占用的空间为 O(n)O(n)O(n) 。这是因为任意一个长度为 nnn 的数组最多只能包含 nnn 个不同的值，但题中保证 nums 一定有一个众数，会占用（最少） ⌊n2⌋+1\lfloor \dfrac{n}{2} \rfloor + 1⌊2n​⌋+1 个数字。因此最多有 n−(⌊n2⌋+1)n - (\lfloor \dfrac{n}{2} \rfloor + 1)n−(⌊2n​⌋+1) 个不同的其他数字，所以最多有 n−⌊n2⌋n - \lfloor \dfrac{n}{2} \rfloorn−⌊2n​⌋ 个不同的元素。
'''
