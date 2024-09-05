# this uses BFS
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit = set()
        queue = deque()
        ans = 0
        ROWS, COLS = len(grid), len(grid[0])
		
        def bfs(r, c):
            queue.append((r, c))
            visit.add((r, c))
            length = 0
            ans = 0

            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        # calculate new r and c
                        nr, nc = r + dr, c + dc
                        # if dr, dc is water or a grid boundary, add 1 to perimiter
                        if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                            ans += 1
                        # else, add it to the queue
                        elif (nr, nc) not in visit:
                            queue.append((nr, nc))
                            visit.add((nr, nc))
                    length += 1

            return ans


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans =  bfs(i,j)
                    return ans

        return ans 