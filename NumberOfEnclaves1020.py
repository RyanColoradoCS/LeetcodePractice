# 1020. Number of Enclaves

class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        ROWS, COLS = len(grid), len(grid[0])
		
        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return 0

            grid[r][c] = 0

            count = 1
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1) and grid[i][j] == 1:
                    dfs(i, j)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    ans += dfs(i,j)

        return ans
