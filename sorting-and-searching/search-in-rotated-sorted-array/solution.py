class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            mid = i + (j - i) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                if target < nums[i] and nums[mid] >= nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if target > nums[j] and nums[mid] <= nums[j]:
                    j = mid - 1
                else:
                    i = mid + 1
        
        return -1