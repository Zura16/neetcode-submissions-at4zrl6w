class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for b in nums:
            if b in a:
                return True
            a.add(b)
        return False
