class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countMap = {}
        for i,j in enumerate(nums):
            diff = target-j
            if diff in countMap:
                return [countMap[diff], i]
            countMap[j] = i