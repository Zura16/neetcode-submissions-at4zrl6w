class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxp = max(profit, maxp)
            else:
                l = r
            r += 1
        return maxp