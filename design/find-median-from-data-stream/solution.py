class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.larger_vals = []
        self.smaller_vals = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        heapq.heappush(self.smaller_vals, -num)
        heapq.heappush(self.larger_vals, -heapq.heappop(self.smaller_vals))
        
        if len(self.smaller_vals) < len(self.larger_vals):
            heapq.heappush(self.smaller_vals, -heapq.heappop(self.larger_vals))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smaller_vals) == len(self.larger_vals):
            return (self.larger_vals[0] - self.smaller_vals[0]) / 2.0
        return -self.smaller_vals[0] * 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()