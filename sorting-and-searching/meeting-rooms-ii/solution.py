class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)

        count = j = 0
        
        for start in starts:
            if start >= ends[j]:
                j += 1
            else:
                count += 1
        
        return count