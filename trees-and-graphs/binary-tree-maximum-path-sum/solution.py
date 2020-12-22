# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(root, max_sum):
            if not root:
                return 0
            
            left = helper(root.left, max_sum)
            right = helper(root.right, max_sum)
            
            max_sum[0] = max(max_sum[0], root.val + max(left, 0) + max(right, 0))
            return root.val + max(0, left, right)
        
        max_sum = [-2147483648]
        helper(root, max_sum)
        return max_sum[0]