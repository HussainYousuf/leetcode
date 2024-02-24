class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q2 = []

        def mark(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q2.append((i, j))

        q1 = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q1.append((i, j))

        n = 0
        while q1:
            while q1:
                i, j = q1.pop()
                mark(i - 1, j)
                mark(i + 1, j)
                mark(i, j - 1)
                mark(i, j + 1)
            if q2:
                n += 1
            q1 = q2
            q2 = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return n
