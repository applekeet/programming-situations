# leetcode

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)

        if m == 0:
            return 0

        n = len(grid[0])

        # First row sum
        if n > 1:
            for j in range(1, n):
                grid[0][j] += grid[0][j-1]

        print(grid)
        if m > 1:
            for i in range(1, m):
                grid[i][0] += grid[i-1][0]

        print(grid)

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        print(grid)
        return grid[m-1][n-1]


gridy = [
    [3, 4, 5, 5],
    [1, 2, 1, 7],
    [4, 5, 6, 2]
]

sosl = Solution()
sosl.minPathSum(gridy)
