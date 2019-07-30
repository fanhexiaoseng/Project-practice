'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
           
        return nums[-k]
'''       
最简单的方法就是使用sort()对数组排序，然后直接返回nums[len(nums) - k]，此方法的时间复杂度为O(nlogn)；
使用堆可以进一步降低复杂度至O(nlogk)，做法是：

    建立一个小顶堆，先把nums中[0, k)的元素添加至小顶堆；
    对于[k, len(nums) - 1]的元素，判断其与小顶堆堆顶元素大小关系，若大于则push进堆（每次push进堆时间复杂度为O(logk)），并将堆顶元素pop，这样做是为了保证小顶堆中始终有k`个元素；
    根据以上机制，最终小顶堆中将会保存最大的k个元素，且堆顶为此k元素里最小的那个。

最后返回堆顶即可
'''
import heapq
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heap = []
        for num in nums[:k]:
            heapq.heappush(heap, num)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]

