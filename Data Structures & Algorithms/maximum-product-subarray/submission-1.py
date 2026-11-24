class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmax, cmin =  1, 1
        for n in nums:
            tmp = n*cmax
            cmax = max(n, cmax*n, cmin * n)
            cmin = min(n, tmp, cmin*n)
            res = max(res, cmax)
        return res