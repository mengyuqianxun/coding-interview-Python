class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxl,l = 0,0
        for num in nums:
            if num == 1:
                l += 1
            else:
                maxl = max(l,maxl)
                l = 0
        maxl = max(l,maxl)
        return maxl