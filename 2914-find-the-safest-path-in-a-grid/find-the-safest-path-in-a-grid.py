class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque()
        safety = [[-1] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    safety[i][j] = 0
                    q.append((i, j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n) and (0 <= nc < n) and (safety[nr][nc] == -1):
                    safety[nr][nc] = safety[r][c] + 1
                    q.append((nr, nc))

        max_heap = [(-safety[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while max_heap:
            sf, r, c = heapq.heappop(max_heap)
            sf = -sf

            if (r == n - 1) and (c == n - 1):
                return sf

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n) and (0 <= nc < n) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_sf = min(sf, safety[nr][nc])
                    heapq.heappush(max_heap, (-new_sf, nr, nc))