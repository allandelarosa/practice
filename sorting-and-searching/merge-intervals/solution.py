class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        # print(intervals)
        
        stack = [intervals.pop()]
        
        while intervals:
            curr = intervals.pop()
            
            while stack and curr[1] >= stack[-1][1]:
                stack.pop()

            while stack and curr[1] >= stack[-1][0]:
                curr = [curr[0], stack.pop()[1]]
            
            stack.append(curr)
        
        return stack