class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        closest = []
        
        for p in points:
            distance = sqrt(p[0] ** 2 + p[1] ** 2)
            
            if len(closest) == K:
                heapq.heappushpop(closest, (-distance, p))
            else:
                heapq.heappush(closest, (-distance, p))
                
        return [p[1] for p in closest]