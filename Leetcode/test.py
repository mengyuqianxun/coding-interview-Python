from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
    	sum1,sum2 = sum(nums1),sum(nums2)
    	if sum1 == sum2:
    		return 0
    	elif sum1 > sum2:
    		sum1,sum2 = sum2,sum1
    		nums1,nums2 = nums2,nums1
    	nums1.sort()
    	nums2.sort()
    	diff = sum2 - sum1
    	#nums1从左往右	nums2从右往左
    	n1,n2 = len(nums1),len(nums2)
    	left,right = 0,n2 - 1
    	count = 0
    	while left < n1 or right >= 0:
    		left_diff = 6 - nums1[left] if left != n1 else 0
    		right_diff = nums2[right] - 1 if right != 0 else 0
    		if left_diff == 0 and right_diff == 0:
    			break
    		if left_diff >= right_diff:
    			diff -= left_diff
    			left += 1
    		else:
    			diff -= right_diff
    			right += 1
    		count += 1
    		if diff <= 0:
    			break
    	return count if diff <= 0 else -1




