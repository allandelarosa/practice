# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        dummy = ListNode()
        curr_dummy = dummy
        
        prev_head = head
        curr = head
        count = 0
        
        while curr:
            curr = curr.next
            count += 1
            
            if count == k:
                count = 0
                curr = prev_head
                
                while count < k:
                    temp = curr.next
                    curr.next = curr_dummy.next
                    curr_dummy.next = curr
                    curr = temp
                    count += 1
                    
                while curr_dummy.next:
                    curr_dummy = curr_dummy.next
                    
                prev_head = curr
                count = 0
                
        curr_dummy.next = prev_head
            
        return dummy.next