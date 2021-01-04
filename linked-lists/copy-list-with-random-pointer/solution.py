"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = curr.next.next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        dummy = Node(0)
        l2 = dummy
        curr = head
        while curr:
            l2.next = curr.next
            l2 = l2.next
            # restore original list
            curr.next = curr.next.next
            curr = curr.next
            
        return dummy.next