from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(nums),len(nums[0])
        if m*n != r*c or r > m*n or c > m*n:
            return nums
        ans = []
        for i in range(r):
            ans.append(nums[i*r:i*r + c])
        return ans

if __name__ == '__main__':
	sol = Solution()
	nums = [[1,2],[3,4]]
	r,c = 1,4
	a = sol.matrixReshape(nums,r,c)
	print(a)