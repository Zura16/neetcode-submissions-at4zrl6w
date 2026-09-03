class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ro, co = len(matrix), len(matrix[0])
        t, b = 0, ro - 1
        while t <= b:
            m = (t + b) // 2
            if target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1
            else:
                break
            
        if not (t <= b):
            return False
        
        l, r = 0, co - 1
        m = (t + b) // 2
        while l <= r:
            n = (l + r) // 2
            if target > matrix[m][n]:
                l = n + 1
            elif target < matrix[m][n]:
                r = n - 1
            else:
                return True

        return False