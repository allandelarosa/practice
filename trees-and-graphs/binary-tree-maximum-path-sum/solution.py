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
        
        max_sum = -2147483648
        
        # on stack, push reference to current node, sum from the left, and boolean to know if ready to update max sum
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                curr_sum = 0
                stack.append((curr, 0, False))
                curr = curr.left
                
            curr, left_sum, ready = stack.pop()
            if ready:
                right_sum = max(curr_sum, 0)
                max_sum = max(max_sum, curr.val + left_sum + right_sum)
                curr_sum = curr.val + max(left_sum, right_sum)
                curr = None
            else:
                left_sum = max(curr_sum, 0)
                stack.append((curr, left_sum, True))
                curr_sum = 0
                curr = curr.right
                
        return max_sum