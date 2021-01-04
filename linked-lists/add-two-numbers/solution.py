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
        
        dummy = ListNode()
        l3 = dummy
        carry = 0
        
        while l1 or l2:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
                
            if l2:
                y = l2.val
                l2 = l2.next
            else:
                y = 0
                
            l3.next = ListNode((x + y + carry) % 10)
            carry = (x + y + carry) // 10
            l3 = l3.next
            
        if carry > 0:
            l3.next = ListNode(carry)
            
        return dummy.next