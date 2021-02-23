class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        nums = [-1]*(m + n -1)
        for i in range(m):
            for j in range(n):
                if nums[j - i + m -1] == -1:
                    nums[j - i + m -1] = matrix[i][j]
                else:
                    if nums[j - i + m -1] != matrix[i][j]:
                        return False
        return True

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True
