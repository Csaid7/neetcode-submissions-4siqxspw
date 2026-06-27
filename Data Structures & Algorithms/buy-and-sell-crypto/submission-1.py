class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        for i in range(len(prices)):
            buy = prices[i] # prices to the left( when we buy)
            for j in range(i + 1, len(prices)):
                sell = prices[j] # prices to the right ( when we sell)
                maxP = max(maxP, sell - buy)
        return maxP
