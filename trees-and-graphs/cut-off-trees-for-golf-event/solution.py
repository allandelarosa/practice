class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        
        def getNeighbors(x, y, m, n):
            neighbors = []
            
            if x - 1 >= 0:  neighbors.append((x - 1, y))
            if y - 1 >= 0:  neighbors.append((x, y - 1))
            if x + 1 < m:   neighbors.append((x + 1, y))
            if y + 1 < n:   neighbors.append((x, y + 1))

            return neighbors
        
        def bfs(start, target, forest, m, n):
            seen = set()
            q = deque([(start, 0)])
            found = False
            
            while q:
                (x, y), depth = q.popleft()
                
                if forest[x][y] == target:
                    found = True
                    break
                    
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                
                depth += 1
                for (nx, ny) in getNeighbors(x, y, m, n):
                    if forest[nx][ny] > 0:
                        q.append(((nx, ny), depth))
                    
            if found:
                return depth, (x, y)
            return -1, (0, 0)
        
        m, n = len(forest), len(forest[0])
        trees = []
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append(forest[i][j])
        
        if not trees:
            return 0
        trees.sort()
        
        start = (0, 0)
        steps = 0
        for tree in trees:
            step, start = bfs(start, tree, forest, m, n)
            if step == -1:
                return -1
            steps += step
            
        return steps