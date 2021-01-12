class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        seen = {}
        prev = []
        count = 0
        
        while count < N and tuple(cells) not in seen:
            seen[tuple(cells)] = count
            prev.append(cells[:])
            
            new_cells = []
            for i in range(len(cells)):
                if i == 0:
                    new_cells.append(0)
                elif i == len(cells) - 1:
                    new_cells.append(0)
                else:
                    new_cells.append(1 if cells[i-1] == cells[i+1] else 0)
            cells = new_cells
            count += 1
            
        if count == N:
            return cells
        
        return prev[(N - count) % (len(seen) - seen[tuple(cells)]) + seen[tuple(cells)]]