class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums[:])
        lsum = 0
        for i in range(len(nums)):
            if lsum*2 + nums[i] == total:
                return i
            lsum += nums[i]
        return -1