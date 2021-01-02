class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        
        oi, oj = 0, len(points) - 1
        
        while oi < oj:
            i, j = oi, oj
            k = randint(i, j)
            pivot = dist(k)
            points[i], points[k] = points[k], points[i]
            i += 1
            
            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]
                
            points[oi], points[j] = points[j], points[oi]
            
            if K < j + 1:
                oj = j - 1
            elif K > j + 1:
                oi = j + 1
            else:
                break
                    
        return points[:K]