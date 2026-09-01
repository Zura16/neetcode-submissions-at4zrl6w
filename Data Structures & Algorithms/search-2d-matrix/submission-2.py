class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        t, b = 0, r - 1
        while t<=b:
            m = (t + b) // 2
            if target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1
            else:
                break
            
        if not (t<=b):
            return False
        m = (t + b) // 2
        l, ri = 0, c - 1
        while l <= ri:
            n = (l + ri) // 2
            if target > matrix[m][n]:
                l = n + 1
            elif target < matrix[m][n]:
                ri = n - 1
            else:
                return True

        return False

