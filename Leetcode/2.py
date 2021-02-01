# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = tmp = ListNode()
        flag = 0
        while l1 or l2 or flag:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + flag
            tmp.next = ListNode(val%10)
            tmp = tmp.next
            flag = val//10
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return l.next