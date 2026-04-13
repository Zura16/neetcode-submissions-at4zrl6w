class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = Counter(s)
        hast = Counter(t)
        for char in hashs:
            if char not in hast or hashs[char] != hast[char]:
                return False
        return True


        