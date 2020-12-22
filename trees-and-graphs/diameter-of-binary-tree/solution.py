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
        
        def helper(root, max_len):
            if not root:
                return 0
            
            left = helper(root.left, max_len)
            right = helper(root.right, max_len)
            
            max_len[0] = max(max_len[0], left + right)
            return max(left,right) + 1
            
        max_len = [0]
        helper(root, max_len)
        return max_len[0]