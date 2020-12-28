# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        def merge(a, b):
            dummy = ListNode()
            c = dummy
            
            while a and b:
                if a.val < b.val:
                    c.next = a
                    a = a.next
                else:
                    c.next = b
                    b = b.next
                c = c.next
            
            while a:
                c.next = a
                a = a.next
                c = c.next
                
            while b:
                c.next = b
                b = b.next
                c = c.next
                
            return dummy.next
        
        dummy = ListNode()
        
        for head in lists:
            dummy.next = merge(dummy.next, head)
            
        return dummy.next