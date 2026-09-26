class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0
        while r < len(prices):
            p = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxp = max(maxp, p)
            else:
                l = r
            r += 1
        return maxp