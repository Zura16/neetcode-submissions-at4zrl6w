class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.h(nums[1:]), self.h(nums[:-1]))

    def h(self, nums):
        n1, n2 = 0, 0
        for n in nums:
            tmp = max(n1+n, n2)
            n1 = n2
            n2 = tmp
        return n2