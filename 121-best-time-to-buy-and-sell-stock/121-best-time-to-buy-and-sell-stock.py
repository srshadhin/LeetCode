class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                temp = prices[r]-prices[l]
                if profit < temp:
                    profit = temp
            else:
                l = r
            r += 1
            
        return profit