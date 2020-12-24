class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        banned = set(banned)
        
        paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = paragraph.split()
        
        counts = defaultdict(int)
        max_count = 0
        
        for word in words:
            if word in banned:
                continue
            counts[word] += 1
            max_count = max(max_count, counts[word])
        
        for word, count in counts.items():
            if count == max_count:
                return word
                
        return ''