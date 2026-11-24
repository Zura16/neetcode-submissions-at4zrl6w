class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cmax, cmin = 1, 1
        for n in nums:
            if n == 0:
                cmin, cmax = 1, 1
                continue
            tmp = n * cmax
            cmax = max(n*cmax, n, n*cmin)
            cmin = min(tmp, n, n*cmin)
            res = max(res, cmax)
        return res