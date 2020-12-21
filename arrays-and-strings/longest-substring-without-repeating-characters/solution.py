class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) < 2:
            return len(s)
        
        seen = defaultdict(int)
        seen[s[0]] = 1
        
        i = 0
        j = 1
        max_len = 0
        
        while j < len(s):
            if seen[s[j]] == 1:
                while s[i] != s[j]:
                    seen[s[i]] = 0
                    i += 1
                i += 1
            
            max_len = max(max_len, j - i + 1)
            
            seen[s[j]] = 1
            j += 1
            
        return max_len