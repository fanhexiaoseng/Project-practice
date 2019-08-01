'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

示例 2:

输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。
动态规划问题
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:   # 总数为0，消耗钱为0
            return 0
        if amount < min(coins):   # 总数比所有的硬币面值都小，无解
            return -1
        dp = [0 for i in range(amount+1)]
        for coin in coins:        # 初始化dp数组
            if coin<=amount:
                dp[coin]= 1
        for i in range(1,amount+1):
            if dp[i]==1:
                continue
            min_ = 100000
            for j in coins:
                if i-j>0:
                    min_ = min(min_,dp[i-j]+1)        
            dp[i] = min_
        if dp[-1]<100000:
            return dp[-1]
        else:
            return -1
