class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanum(ch):
            return (ord('a') <= ord(ch) <= ord('z')) or (ord('0') <= ord(ch) <= ord('9'))
        s = s.lower()
        print(s)
        l = 0
        r = len(s) - 1
        while l < r:     
            print(isalphanum(s[l]))    
            while l < r and not isalphanum(s[l]):
                l += 1
            while l < r and not isalphanum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

        