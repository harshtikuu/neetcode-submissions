from collections import defaultdict,deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0

        m,n = len(grid),len(grid[0])

        def bfs(i,j):
            q = deque([(i,j)])

            while q:
                tx,ty = q.popleft()
                nbrs = []

                if tx > 0 and grid[tx-1][ty] == "1":
                    nbrs.append((tx-1,ty))

                if tx < m-1 and grid[tx+1][ty] == "1":
                    nbrs.append((tx+1,ty))

                if ty > 0 and grid[tx][ty-1] == "1":
                    nbrs.append((tx,ty-1))

                if ty < n-1 and grid[tx][ty+1] == "1":
                    nbrs.append((tx,ty+1))

                for nx,ny in nbrs:
                    if (nx,ny) not in seen:
                        seen.add((nx,ny))
                        q.append((nx,ny))


        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and grid[i][j] == "1":
                    bfs(i,j)
                    count +=1

        return count
