#菜鸡写法
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        sumcus = sum(c for c,g in zip(customers,grumpy) if g == 0)
        l,r = 0,X
        tmp = 0
        for i in range(X):
            if grumpy[i] == 1:
                tmp += customers[i]
        ans = tmp

        while r < len(customers):
            if grumpy[r] == 1:
                tmp += customers[r]
            if grumpy[l] == 1:
                tmp -= customers[l]
            if tmp > ans:
                ans = tmp
            r += 1
            l += 1
        return ans + sumcus

#Pythoner写法
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        sumcus = sum(c for c,g in zip(customers,grumpy) if g == 0)
        maxincrease = tmp = sum(c*g for c,g in zip(customers[:X],grumpy[:X]))
        for i in range(X,len(customers)):
        	tmp = tmp + customers[i]*grumpy[i] - customers[i-X]*grumpy[i-X]
        	maxincrease = max(tmp,maxincrease)
        return sumcus + maxincrease