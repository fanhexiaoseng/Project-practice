'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
'''
# 超时
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        a = [0 for i in range(len(T))]
        i = 0
        while i < len(T):
            k = 0
            for j in range(i+1,len(T)):
                k += 1
                if T[j] > T[i]:
                    a[i] = k
                    break
            i+=1
        return a
