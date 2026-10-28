class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        maxr = 0
        l = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxr = max(maxr, count[s[r]])
            while (r-l+1) - maxr > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res
                