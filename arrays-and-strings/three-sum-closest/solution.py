class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        
        i = 0
        closest = float('inf')
        
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                    
                if curr_sum <= target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                    
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
            
        return closest