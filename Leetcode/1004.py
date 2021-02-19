#1.经典滑动窗口
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        L = 0                       #标准滑动窗口框架  左端点
        window_1_cnt = 0            #滑动窗口内1的个数
        for R in range(len(A)):     #滑动窗口右端点
            if A[R] == 1:
                window_1_cnt += 1
            window_0_cnt = R - L + 1 - window_1_cnt #滑动窗口内0的个数
            while window_0_cnt > K:     #判断条件，L右移
                if A[L] == 1:
                    window_1_cnt -= 1
                else:
                    window_0_cnt -= 1
                L += 1
            res = max(res, R-L+1)
        return res
#2.自己写的滑动窗口
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        ans = 0
        cnt_0 = 0
        for r in range(len(A)):
            if A[r] == 0:
                cnt_0 += 1
                if cnt_0 > K:
                    while A[l]:
                        l += 1
                    l += 1
                    cnt_0 -= 1
            ans = max(ans,r - l + 1)
        return ans

#3.官方
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = lsum = rsum = 0
        ans = 0
        
        for right in range(n):
            rsum += 1 - A[right]
            while lsum < rsum - K:
                lsum += 1 - A[left]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans