class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(nums),len(nums[0])
        if m*n != r*c or r > m*n or c > m*n:
            return nums
        ans = []
        tmp = []
        for i in range(m):
            for j in range(n):
                tmp.append(nums[i][j])
                if len(tmp) == c:
                    ans.append(tmp)
                    tmp = []
        return ans