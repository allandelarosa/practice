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
        
        def helper(root, p, q):
            if not root:
                return None, False, False
            
            left = helper(root.left, p, q)
            if left[0]:
                return left
            
            right = helper(root.right, p, q)
            if right[0]:
                return right
            
            if (left[1] and right[2]) or (left[2] and right[1]):
                return root, True, True
            
            p_found = left[1] or right[1] or root == p
            q_found = left[2] or right[2] or root == q
            
            if p_found and q_found:
                return root, True, True
            
            return None, p_found, q_found
        
        return helper(root, p, q)[0]
            
            
                