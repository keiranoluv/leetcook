class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        INF = 10**9

        dist = [[INF] * n for _ in range(m)]

        dq = deque()

        dist[0][0] = grid[0][0]

        dq.appendleft((0, 0))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dq:
            x, y = dq.popleft()
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cost = grid[nx][ny]
                    new_damage = dist[x][y] + cost

                    if new_damage < dist[nx][ny]:
                        dist[nx][ny] = new_damage

                        if cost == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return dist[m - 1][n - 1] < health
