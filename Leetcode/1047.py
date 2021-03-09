class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = list()
        for s in S:
            if not stk or stk[-1] != s:
                stk.append(s)
            else:
                stk.pop()
        return ''.join(stk)