class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0
        
        # construct adjacency list
        adj_list = defaultdict(list)
        for j, word in enumerate(wordList):
            for i in range(len(word)):
                adj_list[word[:i] + '*' + word[i + 1:]].append(j)
                
        # perform bfs
        q = deque([(beginWord, 1)])
        seen = set()
        
        while q:
            word, depth = q.popleft()
            
            if word in seen:
                continue
            seen.add(word)
                
            depth += 1
            for i in range(len(word)):
                matcher = word[:i] + '*' + word[i + 1:]
                
                for j in adj_list[matcher]:
                    nei = wordList[j]
                    if nei == endWord:
                        return depth
                    if nei in seen:
                        continue
                    q.append((nei, depth))
                    
                adj_list[matcher] = []
                
        return 0