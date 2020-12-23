class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        # given source point, find original color
        # perform bfs to find all points with that same color
        # change the color of these points to new color
        
        def getNeighbors(x, y, m, n):
            neighbors = []
            
            if x - 1 >= 0:
                neighbors.append((x - 1, y))
            if y - 1 >= 0:
                neighbors.append((x, y - 1))
            if x + 1 < m:
                neighbors.append((x + 1, y))
            if y + 1 < n:
                neighbors.append((x, y + 1))
                
            return neighbors
        
        origColor = image[sr][sc]
        m = len(image)
        n = len(image[0])
        
        q = deque([(sr, sc)])
        while q:
            x, y = q.popleft()
            
            if image[x][y] == newColor:
                continue
            image[x][y] = newColor
            
            for (nx, ny) in getNeighbors(x, y, m, n):
                if image[nx][ny] != origColor:
                    continue
                q.append((nx, ny))
                
        return image