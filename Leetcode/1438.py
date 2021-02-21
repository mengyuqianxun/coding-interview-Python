from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = SortedList()
        l,r,ans = 0,0,0
        while r < len(nums):
            s.add(nums[r])
            while s[-1] - s[0] > limit:
                s.remove(nums[l])
                l += 1
            ans = max(ans,r - l + 1)
            r += 1
        return ans



