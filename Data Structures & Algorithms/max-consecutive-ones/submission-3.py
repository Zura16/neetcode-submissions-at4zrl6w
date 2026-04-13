class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in nums:
            if i:
                a+=1
            else:
                a=0
            b = max(b, a)

        return b
        
        
