from typing import List

nums1 = [4,5,6]
nums2 = [1,2,3]
sum1,sum2 = sum(nums1),sum(nums2)
if sum1 == sum2:
	a = 1
#	return 0
elif sum1 > sum2:
	sum1,sum2 = sum2,sum1
	nums1,nums2 = nums2,nums1

print(sum1,sum2,nums1,nums2)

