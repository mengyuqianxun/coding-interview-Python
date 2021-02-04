class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmpnums = maxnums= sum(nums[0:k])
        for i in range(1,len(nums) - k + 1):
            tmpnums = tmpnums - nums[i-1] + nums[i + k - 1]
            maxnums = max(maxnums,tmpnums)
        return maxnums/k