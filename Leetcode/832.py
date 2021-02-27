class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m,n = len(A),len(A[0])
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][n - j - 1] == 0:
                    ans[i][j] = 1
        return ans

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if A[i][left] == A[i][right]:
                    A[i][left] ^= 1
                    A[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A