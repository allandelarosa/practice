class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        counts = Counter(nums)
        unique = counts.keys()
        
        oi, oj = 0, len(unique) - 1
        while oi < oj:
            i, j, l = oi, oj, randint(oi, oj)
            unique[i], unique[l] = unique[l], unique[i]
            
            pivot = counts[unique[i]]
            i += 1
            
            while True:
                while i < j and counts[unique[i]] > pivot:
                    i += 1
                while i <= j and counts[unique[j]] <= pivot:
                    j -= 1
                if i >= j:
                    break
                unique[i], unique[j] = unique[j], unique[i]
            unique[oi], unique[j] = unique[j], unique[oi]
            
            if k > j + 1:
                oi = j + 1
            elif k < j + 1:
                oj = j - 1
            else:
                break
        
        return unique[:k]