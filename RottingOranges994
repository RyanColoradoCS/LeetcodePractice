# 994. Rotting Oranges

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        rotten_queue = deque()
        time = 0
        fresh = 0

        # get count of fresh oranges and add rotten oranges to the queue for BFS
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    fresh += 1
                if grid[m][n] == 2:
                    rotten_queue.append([m,n])
                
        while rotten_queue and fresh > 0:
            for i in range(len(rotten_queue)):
                r, c = rotten_queue.popleft()

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        grid[r + dr][c + dc] == 0 or grid[r + dr][c + dc] == 2):
                        continue # do nothing if out of bounds, rotten, or empty
                    rotten_queue.append((r + dr, c + dc))
                    # visit.add((r + dr, c + dc))
                    # change value to 2 instead of adding to visited
                    grid[r + dr][c + dc] = 2
                    fresh -= 1 # decrease count of fresh
            time += 1
        
        if fresh == 0:
            return time
        return -1
        
