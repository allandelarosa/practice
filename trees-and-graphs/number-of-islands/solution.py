class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
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
        
        m = len(grid)
        n = len(grid[0])
        
        # iterate over ever point in grid
        # if 1 is found, increment island count
        # perform bfs; mark all connected 1's as seen
        
        seen = set()
        island_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    island_count += 1
                    q = deque([(i, j)])
                    while q:
                        (x, y) = q.popleft()
                        
                        if (x, y) in seen:
                            continue
                        seen.add((x, y))
                        
                        for (nx, ny) in getNeighbors(x, y, m, n):
                            if (nx, ny) in seen:
                                continue
                            if grid[nx][ny] == '1':
                                q.append((nx, ny))
                    
        return island_count