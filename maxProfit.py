class Solution:
    def maxProfit(self, prices: list[int])->int:
        curProfit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]
                curProfit = max(curProfit, profit)
                
        return curProfit

s= Solution()
prices = [7,1,5,3,6,4]
ret = s.maxProfit(prices)
print(ret)
