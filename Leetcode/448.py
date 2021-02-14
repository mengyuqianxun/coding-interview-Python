#1.python集合
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = set(nums)
        arr2 = set([i for i in range(1,len(nums) + 1)])
        ans = list(arr2 - arr)
        return ans

#2.数组存储
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[(nums[i] - 1) % n] += n
        ans = []
        for i in range(n):
            if nums[i] <= n:
                ans.append(i + 1)
        return ans

