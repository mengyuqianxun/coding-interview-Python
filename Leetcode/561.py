class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = 0
        for i in range(0,len(nums),2):
            sums += nums[i]
        return sums

#更简单、更快的写法
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])