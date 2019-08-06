'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        con = len(grid[0])-1
        while con >= 0:
            raw = len(grid)-1
            while raw >= 0:
                if con == len(grid[0])-1:
                    if raw != len(grid)-1:
                        grid[raw][con] += grid[raw+1][con]
                else:
                    if raw == len(grid)-1:
                        grid[raw][con] += grid[raw][con+1]
                    else:
                        grid[raw][con] += min(grid[raw][con+1],grid[raw+1][con])
                raw -= 1 
            con -= 1
        return grid[0][0]
