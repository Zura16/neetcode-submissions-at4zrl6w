class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = collections.defaultdict(int)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hasmap:               
                return [hasmap[target-num],i]
            hasmap[num] = i
        return False
        