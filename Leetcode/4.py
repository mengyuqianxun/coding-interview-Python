class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1),len(nums2)
        if (m + n) & 1 != 0:
            return self.getkthEle((m + n)//2 + 1,nums1,nums2)
        else:
            return (self.getkthEle((m + n)//2,nums1,nums2) + \
            self.getkthEle((m + n)//2 + 1,nums1,nums2))/2

    def getkthEle(self,k,nums1,nums2):
        index1,index2 = 0,0
        m,n = len(nums1),len(nums2)
        while True:
            #特殊情况
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1],nums2[index2])
            #一般情况
            newindex1 = min(index1 + k//2 - 1,m - 1)
            newindex2 = min(index2 + k//2 - 1,n - 1)
            if nums1[newindex1] <= nums2[newindex2]:
                k -= newindex1 - index1 + 1
                index1 = newindex1 + 1 
            else:
                k -= newindex2 - index2 + 1
                index2 = newindex2 + 1
