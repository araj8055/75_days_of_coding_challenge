class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        loss = prices[0]
        profit = 0
        for i in range(0,len(prices)):
            loss = min(loss , prices[i])
            profit = max(profit , prices[i] - loss)
        return profit
