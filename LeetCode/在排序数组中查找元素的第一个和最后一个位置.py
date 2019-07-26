'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

'''
class Solution(object):
    def extreme_insertion_index(self,nums,target,left):
        lo = 0
        hi = len(nums)
        while lo <hi:
            mid = (lo+hi)//2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid +1
        return lo
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # a = []
        # k = 0
        # while k <len(nums):
        #     if target == nums[k]:
        #         a.append(k)
        #         k+=1
        # if not a:
        #     return [-1,-1]
        # elif a[1] is None:
        #     a.append(-1)
        #     return a
        # else:
        #     return [a[0],a[len(a)-1]]
        left_idx = self.extreme_insertion_index(nums,target,True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1,-1]
        return [left_idx,self.extreme_insertion_index(nums,target,False)-1]
