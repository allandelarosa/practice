class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = [1] * len(nums)
        
        i = 0
        prod = 1
        
        while i < len(nums):
            output[i] *= prod
            prod *= nums[i]
            i += 1
            
        i -= 1
        prod = 1
        while i >= 0:
            output[i] *= prod
            prod *= nums[i]
            i -= 1
            
        return output