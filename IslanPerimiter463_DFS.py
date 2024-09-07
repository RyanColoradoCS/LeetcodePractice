class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
		
        def dfs(r, c):
            # if r, c is water or a grid boundary, add 1 to perimiter
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return 1
            if (r, c) in visit:
                return 0

            visit.add((r, c))

            count = 0
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        perimiter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimiter =  dfs(i,j)
                    return perimiter

        return perimiter
