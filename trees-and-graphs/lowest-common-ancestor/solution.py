# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        stack = []
        curr = root
        
        p_found = q_found = False
        
        while stack or curr:
            while curr:
                p_found = q_found = False
                stack.append((curr, p_found, q_found, False))
                curr = curr.left
                
            curr, p_temp, q_temp, popped = stack.pop()
            
            p_found = p_temp or p_found
            q_found = q_temp or q_found

            if p_found and q_found:
                return curr
            
            if popped:
                p_found = p_found or curr == p
                q_found = q_found or curr == q
                
                if p_found and q_found:
                    return curr
                
                curr = None
                
            else:
                stack.append((curr, p_found, q_found, True))
                curr = curr.right
