class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxlen, minlen = 1, 1
        for n in nums:
            tmp = maxlen*n
            maxlen = max(n*maxlen, n*minlen, n)
            minlen = min(tmp, n, minlen*n)
            res = max(res, maxlen)
        return res