class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3:
            return []
        
        nums.sort()
        trips = []
        
        i = 0
        while i < len(nums) - 2 and nums[i] <= 0:
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    trips.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                elif curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                    
            while i < len(nums) - 2 and nums[i + 1] == nums[i]:
                i += 1
            i += 1
            
        return trips