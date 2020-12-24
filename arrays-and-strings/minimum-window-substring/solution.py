class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(t) > len(s):
            return ""
        
        counts = {}
        chars_left = 0
        for c in t:
            counts[c] = counts.get(c, 0) + 1
            chars_left += 1
            
        ans = float('inf'), 0, 0
        i = j = 0
        
        while j < len(s):
            if s[j] in counts:
                counts[s[j]] -= 1
                if counts[s[j]] >= 0:
                    chars_left -= 1
                    
            while i <= j and chars_left == 0:
                if j - i + 1 < ans[0]:
                    ans = j - i + 1, i, j + 1
                    
                if s[i] in counts:
                    counts[s[i]] += 1
                    if counts[s[i]] > 0:
                        chars_left += 1
                        
                i += 1
                
            j += 1
            
        return s[ans[1]:ans[2]]
        
        