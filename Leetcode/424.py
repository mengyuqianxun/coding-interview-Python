class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num = [0] * 26
        n = len(s)
        left = right = maxn = 0
        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn,num[ord(s[right]) - ord("A")])
            if (right - left + 1) - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        
        return right - left