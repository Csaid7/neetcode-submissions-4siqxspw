class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        # [1 - 10 = -9, 5 - 10 = -5, 6- 10 = -4 , 7 - 10 = -3, 1 - 10 = -9]
        # [5 - 1 = 4, 6- 1, = 5, 7 - 1 = 6, 1- 1 = 0 res = 6 and ]
        r, l = 1, 0
        maxP = 0

        while r < len(prices):
            #profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                #found lowest price( means we foudn min)
                # ex 
                l = r
                
            r += 1 
        return maxP

                

