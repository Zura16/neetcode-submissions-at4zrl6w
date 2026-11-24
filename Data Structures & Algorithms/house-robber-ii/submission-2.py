class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.n(nums[1:]), self.n(nums[:-1]))

    def n(self, nums):
        h1, h2 = 0, 0
        for i in nums:
            tmp = max(h1+i, h2)
            h1 = h2
            h2 = tmp
        return h2