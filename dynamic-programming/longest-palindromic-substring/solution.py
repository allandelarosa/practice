class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        indices = (0, 0)
        
        for k in range(n):
            i = j = k
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                if j - i + 1 > indices[1] - indices[0] + 1:
                    indices = (i, j)
                i -= 1
                j += 1
                
            i, j = k, k + 1
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                if j - i + 1 > indices[1] - indices[0] + 1:
                    indices = (i, j)
                i -= 1
                j +=1
        
        return s[indices[0]:indices[1]+1]