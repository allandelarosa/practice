# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
            
        max_len = 0
        
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                curr_len = 0
                stack.append((curr, 0, False))
                curr = curr.left
            
            curr, left, ready = stack.pop()
            if ready:
                right = curr_len
                max_len = max(max_len, left + right)
                curr_len = 1 + max(left, right)
                curr = None
            else:
                stack.append((curr, curr_len, True))
                curr_len = 0
                curr = curr.right
                
        return max_len