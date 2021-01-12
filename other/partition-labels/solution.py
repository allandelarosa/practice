class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        # variation of merge intervals solution
        
        seen = {}
        intervals = []
        
        for i, c in enumerate(S):
            if c in seen:
                seen[c][1] = i
            else:
                seen[c] = [i, i]
                
            curr = seen[c]
            while intervals and (intervals[-1][1] > curr[0] or intervals[-1][0] >= curr[0]):
                curr[0] = min(curr[0], intervals[-1][0])
                curr[1] = max(curr[1], intervals[-1][1])
                intervals.pop()
            
            intervals.append(curr)
            
        return [interval[1] - interval[0] + 1 for interval in intervals]
        