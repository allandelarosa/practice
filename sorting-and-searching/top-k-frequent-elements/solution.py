class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        counts = Counter(nums)
        
        h = []
        for num, count in counts.items():
            if len(h) == k:
                heapq.heappushpop(h, (count, num))
            else:
                heapq.heappush(h, (count, num))
        
        return [num for count, num in h]