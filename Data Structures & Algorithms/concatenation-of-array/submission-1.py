class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        '''for n in range(1):
            ans = nums+nums
        return ans'''

        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
