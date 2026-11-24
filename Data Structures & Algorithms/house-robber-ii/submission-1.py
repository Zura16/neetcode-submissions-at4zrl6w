class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.h(nums[1:]), self.h(nums[:-1]))

    def h(self, nums):
        r1, r2 = 0, 0
        for i in nums:
            tmp = max(r1+i, r2)
            r1 = r2
            r2 = tmp     
        return r2   